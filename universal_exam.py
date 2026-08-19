import pandas as pd, numpy as np, os, glob, zipfile
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestClassifier, RandomForestRegressor,
    HistGradientBoostingClassifier, HistGradientBoostingRegressor,
    ExtraTreesClassifier, ExtraTreesRegressor
)
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error
import warnings
import sys
warnings.filterwarnings('ignore')

# ==============================================================================
# [실전 대비 수동 설정 구역] - 자동 탐지가 실패할 경우 이곳의 주석을 풀고 직접 입력하세요!
# ==============================================================================
# MANUAL_TARGET = 'target_column_name'  # 정답 컬럼을 명확히 알 때 (예: 'Survived', 'price')
# MANUAL_TASK = 'REG'                   # 분류는 'CLF', 회귀는 'REG'
# MANUAL_METRIC = 'RMSE'                # 평가지표 (ACCURACY, F1, RMSE, MAE 등)
# ==============================================================================

# ==============================================================================
# [1/7] 파일 스캔 및 자동 탐지 구역
# ==============================================================================
print("=" * 70)
print("[1/7] 데이터 로드 및 자동 파일 스캔")
print("=" * 70)

DATA_DIR = sys.argv[1] if len(sys.argv) > 1 else '.'

# ZIP 파일 자동 압축 해제 로직 추가
all_csvs = glob.glob(os.path.join(DATA_DIR, '*.csv'))
if not all_csvs:
    zip_files = glob.glob(os.path.join(DATA_DIR, '*.zip'))
    for zf in zip_files:
        print(f" - 압축 파일 감지: {zf} (자동 압축 해제 진행)")
        try:
            with zipfile.ZipFile(zf, 'r') as z:
                # 한글 인코딩 처리하며 풀기
                for info in z.infolist():
                    try:
                        info.filename = info.filename.encode('cp437').decode('cp949', 'ignore')
                    except: pass
                    z.extract(info, DATA_DIR)
        except Exception as e:
            print(f" - 압축 해제 실패: {e}")
    # 다시 CSV 스캔
    all_csvs = glob.glob(os.path.join(DATA_DIR, '*.csv')) + glob.glob(os.path.join(DATA_DIR, '*/*.csv'))

PATH_TR, PATH_TE, PATH_SUB, PATH_DATA = None, None, None, None

for f in all_csvs:
    fname = os.path.basename(f).lower()
    if 'train' in fname: PATH_TR = f
    elif 'test' in fname: PATH_TE = f
    elif 'sub' in fname: PATH_SUB = f
    elif fname not in ['dataset.csv']: PATH_DATA = f

if not PATH_TR and not PATH_DATA and os.path.exists(os.path.join(DATA_DIR, 'dataset.csv')):
    PATH_DATA = os.path.join(DATA_DIR, 'dataset.csv')

T, t, sub_df = None, None, None

if PATH_TR and PATH_TE:
    print(f" - Train 파일 감지: {PATH_TR}")
    print(f" - Test 파일 감지: {PATH_TE}")
    T, t = pd.read_csv(PATH_TR), pd.read_csv(PATH_TE)
elif PATH_DATA or PATH_TR:
    single_path = PATH_DATA if PATH_DATA else PATH_TR
    print(f" - 단일 데이터셋 감지: {single_path} (자동 80:20 분할 진행)")
    full_data = pd.read_csv(single_path)
    T, t = train_test_split(full_data, test_size=0.2, random_state=42)
    T, t = T.reset_index(drop=True), t.reset_index(drop=True)
else:
    raise FileNotFoundError("학습할 CSV 파일을 찾을 수 없습니다!")

TARGET_COL = locals().get('MANUAL_TARGET', None)
ID_COL = None

if PATH_SUB:
    print(f" - 제출 양식 감지: {PATH_SUB}")
    sub_df = pd.read_csv(PATH_SUB)
    if len(sub_df.columns) == 1:
        ID_COL = None
        if not TARGET_COL: TARGET_COL = sub_df.columns[0]
    else:
        ID_COL = sub_df.columns[0]
        if not TARGET_COL: TARGET_COL = sub_df.columns[1]
else:
    print(" - 제출 양식 없음: Test 데이터를 기반으로 자동 생성합니다.")
    sub_df = pd.DataFrame()

if not TARGET_COL or TARGET_COL not in T.columns:
    diff = [c for c in T.columns if c not in t.columns]
    if diff:
        TARGET_COL = diff[0]
    else:
        TARGET_COL = T.columns[-1]

print(f" - 타깃 컬럼 확정: {TARGET_COL}")

y = T[TARGET_COL]

# y에 NaN이 있으면 해당 행 전체 삭제
valid_idx = y.notna()
T = T[valid_idx].reset_index(drop=True)
y = T[TARGET_COL]

if 'MANUAL_TASK' in locals():
    TASK = MANUAL_TASK
    METRIC = locals().get('MANUAL_METRIC', 'F1' if TASK == 'CLF' else 'RMSE')
else:
    if pd.api.types.is_object_dtype(y) or pd.api.types.is_string_dtype(y) or pd.api.types.is_bool_dtype(y):
        is_clf = True
    elif pd.api.types.is_integer_dtype(y) and y.nunique() < 30:
        is_clf = True
    else:
        is_clf = False

    TASK = 'CLF' if is_clf else 'REG'
    METRIC = 'F1' if is_clf else 'RMSE'
    
is_clf = (TASK == 'CLF')
print(f" - 문제 유형: {TASK} (평가 지표: {METRIC})")

print("\n" + "=" * 70)
print("[2/7] 데이터 누수(Data Leakage) 차단")
print("=" * 70)
leak_cols = [c for c in T.columns if c not in t.columns and c != TARGET_COL]

if not ID_COL and t.shape[1] > 0 and (t.columns[0].lower() in ['id', 'no', 'index']):
    ID_COL = t.columns[0]

X = T.drop(columns=[TARGET_COL] + leak_cols)
X_t = t.drop(columns=[ID_COL]) if ID_COL and ID_COL in t.columns else t.copy()
if ID_COL and ID_COL in X.columns: X = X.drop(columns=[ID_COL])

print("\n" + "=" * 70)
print("[3/7] 시계열 심층 분해 및 100% 결측치 제거")
print("=" * 70)
X.columns = [str(c).replace('/','_').replace(' ','_') for c in X.columns]
X_t.columns = [str(c).replace('/','_').replace(' ','_') for c in X_t.columns]

all_nan_cols = X.columns[X.isnull().all()].tolist()
X, X_t = X.drop(columns=all_nan_cols), X_t.drop(columns=all_nan_cols)

for c in X.select_dtypes(include=['object']).columns:
    try:
        cv = pd.to_datetime(X[c], errors='coerce')
        if cv.notna().sum() > len(X)*0.5:
            for df, d in [(X, cv), (X_t, pd.to_datetime(X_t[c], errors='coerce'))]:
                df[c+'_y'], df[c+'_m'], df[c+'_d'] = d.dt.year, d.dt.month, d.dt.day
                df[c+'_h'], df[c+'_w'] = d.dt.hour, d.dt.dayofweek
            X, X_t = X.drop(columns=[c]), X_t.drop(columns=[c])
    except: pass

print("\n" + "=" * 70)
print("[4/7] 결측치 대체 및 범주형 인코딩 (One-Hot)")
print("=" * 70)
cat = X.select_dtypes(include=['object']).columns
drop = [c for c in cat if X[c].nunique() > 50]
X, X_t = X.drop(columns=drop), X_t.drop(columns=drop)

num, cat = X.select_dtypes(exclude=['object']).columns, X.select_dtypes(include=['object']).columns
if len(num): 
    medians = X[num].median()
    X[num], X_t[num] = X[num].fillna(medians), X_t[num].fillna(medians)
if len(cat): 
    modes = X[cat].mode()
    if not modes.empty:
        X[cat], X_t[cat] = X[cat].fillna(modes.iloc[0]), X_t[cat].fillna(modes.iloc[0])
        
X, X_t = pd.get_dummies(X).align(pd.get_dummies(X_t), join='left', axis=1, fill_value=0)

print("\n" + "=" * 70)
print(f"[5/7] 타깃 레이블 전처리 (과제: {TASK})")
print("=" * 70)

if not is_clf and y.dtype == 'object':
    y = pd.to_numeric(y.astype(str).str.replace(',', ''), errors='coerce').fillna(0)

if is_clf:
    if y.dtype == 'object':
        y = y.astype('category')
        inv_map = dict(enumerate(y.cat.categories))
        y = y.cat.codes
    elif y.dtype in ['int64', 'int32', 'float64', 'float32'] and not set(y.unique()).issubset({0, 1}):
        cats = sorted(y.unique())
        inv_map = {i: c for i, c in enumerate(cats)}
        y = y.map({c: i for i, c in enumerate(cats)})
y_train = y

print("\n" + "=" * 70)
print("[6/7] 3대 앙상블 모델 교차 검증 (배틀)")
print("=" * 70)
stratify_param = y_train if is_clf else None
if len(X) < 10:
    best_m = RandomForestClassifier(random_state=42) if is_clf else RandomForestRegressor(random_state=42)
else:
    X_tr, X_val, y_tr, y_val = train_test_split(X, y_train, test_size=0.2, random_state=42, stratify=stratify_param)
    if is_clf:
        models = [RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42, n_jobs=-1),
                  HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, l2_regularization=0.1, random_state=42),
                  ExtraTreesClassifier(n_estimators=200, class_weight='balanced', random_state=42, n_jobs=-1)]
    else:
        models = [RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1),
                  HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, l2_regularization=0.1, random_state=42),
                  ExtraTreesRegressor(n_estimators=200, random_state=42, n_jobs=-1)]

    best_m, best_score = None, float('-inf') if is_clf else float('inf')
    for i, m in enumerate(models, 1):
        m_name = m.__class__.__name__
        print(f" [{i}/3] {m_name:<30} 학습 중...", end='', flush=True)
        m.fit(X_tr, y_tr)
        p_val = m.predict(X_val)
        if METRIC == 'ACCURACY': s = accuracy_score(y_val, p_val)
        elif METRIC == 'F1': s = f1_score(y_val, p_val, average='macro')
        else: s = np.sqrt(mean_squared_error(y_val, p_val))
        print(f" 검증 점수: {s:.4f}")
        if (s > best_score) if is_clf else (s < best_score):
            best_m, best_score = m, s

print("\n" + "=" * 70)
print(f"[7/7] 최종 재학습 및 파일 저장")
print("=" * 70)
best_m.fit(X, y_train)
p = best_m.predict(X_t)

if is_clf and 'inv_map' in locals(): p = pd.Series(p).map(inv_map)

if not PATH_SUB or sub_df.empty:
    if ID_COL and ID_COL in t.columns:
        sub_df = pd.DataFrame({ID_COL: t[ID_COL], TARGET_COL: p})
    else:
        sub_df = pd.DataFrame({TARGET_COL: p})
else:
    sub_df[TARGET_COL] = p

out_path = os.path.join(DATA_DIR, 'submission.csv')
sub_df.to_csv(out_path, index=False)
print(f"\n[완료] {out_path} 생성 완료! (제출 파일)")
