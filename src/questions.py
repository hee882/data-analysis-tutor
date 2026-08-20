import random
import re

def _prep(text):
    if not text: return ""
    text = text.replace("'", '"')
    text = re.sub(r'\s+', '', text)
    return text.lower()

# =====================================================================
# [EASY POOL] - 기초 문법, 기본 Pandas, 기본 시각화 (총 16문제 출제용)
# =====================================================================

def gen_easy_read_excel():
    ans = "pd.read_excel('data.xlsx')"
    wrongs = ["pd.load_excel('data.xlsx')", "pd.open('data.xlsx')", "pd.read_csv('data.xlsx')"]
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 불러오기', 
        'question': "Pandas를 사용하여 'data.xlsx' 엑셀 파일을 읽어오는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.read_excel() 함수를 사용하여 엑셀 파일을 DataFrame으로 불러옵니다.",
        'check': lambda x: "read_excel" in _prep(x) and "data.xlsx" in _prep(x)
    }

def gen_easy_head():
    n = random.randint(3, 8)
    ans = f"df.head({n})"
    wrongs = [f"df.head(rows={n})", f"df.show({n})", f"df.top({n})", f"df.iloc[:{n}, :].head()"]
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 탐색 (앞부분)', 
        'question': f"데이터프레임 `df`의 처음 {n}개 행을 출력하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"df.head({n})을 사용하면 맨 위에서부터 지정한 개수만큼의 데이터를 확인할 수 있습니다.",
        'check': lambda x: "head" in _prep(x) and str(n) in _prep(x)
    }

def gen_easy_dtypes():
    ans = "df.dtypes"
    wrongs = ["df.types", "df.info", "df.type()"]
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 타입 확인', 
        'question': "데이터프레임 `df`의 각 컬럼별 데이터 타입을 확인하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.dtypes 속성을 통해 각 열의 데이터 타입(int, float, object 등)을 확인할 수 있습니다.",
        'check': lambda x: "df.dtypes" in _prep(x)
    }

def gen_easy_isnull():
    ans = "df.isna().sum()"
    wrongs = ["df.isna().count()", "df.nulls()", "df.count_na()"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 결측치 개수 확인', 
        'question': "데이터프레임 `df`의 각 컬럼별 결측치(NaN) 총 개수를 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.isna().sum() (또는 df.isnull().sum())을 통해 열별 결측치 개수를 집계합니다.",
        'check': lambda x: ("isnull" in _prep(x) or "isna" in _prep(x)) and "sum" in _prep(x)
    }

def gen_easy_dropna():
    ans = "df.dropna()"
    wrongs = ["df.drop_na()", "df.remove_na()", "df.delete_nulls()"]
    return {
        'topic': '[4] 데이터 전처리 - 결측치 삭제', 
        'question': "데이터프레임 `df`에서 결측치가 하나라도 포함된 행을 모두 삭제하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.dropna() 함수를 사용하여 결측치(NaN)가 포함된 행을 제거할 수 있습니다.",
        'check': lambda x: "dropna" in _prep(x)
    }

def gen_easy_filter():
    ans = "df[df['age'] >= 20]"
    wrongs = ["df.filter(age >= 20)", "df.where(age >= 20)", "df[age >= 20]"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 조건부 필터링', 
        'question': "데이터프레임 `df`에서 'age'가 20 이상인 행만 필터링하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Boolean Indexing인 df[조건]을 활용하여 특정 조건에 맞는 행만 추출할 수 있습니다.",
        'check': lambda x: "df" in _prep(x) and ">=" in _prep(x) and "20" in _prep(x) and "age" in _prep(x)
    }

def gen_easy_loc():
    ans = "df.loc[0, 'name']"
    wrongs = ["df.iloc[0, 'name']", "df[0, 'name']", "df.loc['name', 0]"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 특정 데이터 접근 (loc)', 
        'question': "데이터프레임 `df`에서 인덱스 이름이 0이고 컬럼명이 'name'인 곳의 데이터를 가져오거나 수정하려고 합니다. `.loc`를 사용한 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.loc[행이름, 열이름] 형식으로 특정 좌표의 데이터에 라벨 기반으로 접근할 수 있습니다.",
        'check': lambda x: "loc[0," in _prep(x) and "name" in _prep(x)
    }

def gen_easy_value_counts():
    ans = "df['category'].value_counts()"
    wrongs = ["df['category'].count_values()", "df['category'].counts()", "pd.value_counts(df, 'category')"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 카테고리 빈도수 확인', 
        'question': "데이터프레임 `df`의 'category' 컬럼에 있는 항목별 빈도수(개수)를 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Series 객체의 .value_counts() 메서드를 사용하면 범주형 데이터의 빈도를 알 수 있습니다.",
        'check': lambda x: "value_counts" in _prep(x) and "category" in _prep(x)
    }

def gen_viz_countplot():
    ans = "sns.countplot(data=df, x='day')"
    wrongs = ["sns.bar(df, 'day')", "plt.countplot(df['day'])", "df.plot(kind='count', x='day')"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Countplot)', 
        'question': "Seaborn을 사용하여 데이터프레임 `df`의 'day' 컬럼(요일)별 데이터 개수를 막대 그래프(빈도수)로 시각화하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.countplot()은 범주형 변수의 각 카테고리별 빈도수를 보여주는 직관적인 시각화 도구입니다.",
        'check': lambda x: "countplot" in _prep(x) and "day" in _prep(x)
    }

def gen_viz_histplot():
    ans = "sns.histplot(data=df, x='tip')"
    wrongs = ["sns.histogram(df, 'tip')", "plt.histplot(df['tip'])", "sns.hist(df['tip'])"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Histplot)', 
        'question': "Seaborn을 사용하여 데이터프레임 `df`의 연속형 숫자 컬럼인 'tip'의 분포를 히스토그램으로 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "수치형 데이터의 분포(몰려있는 정도)를 볼 때는 sns.histplot()을 사용합니다.",
        'check': lambda x: "histplot" in _prep(x) and "tip" in _prep(x)
    }

def gen_viz_scatter():
    ans = "sns.scatterplot(data=df, x='age', y='income')"
    wrongs = ["sns.scatter(x='age', y='income')", "plt.scatter(df)", "df.plot_scatter('age', 'income')"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Scatter plot)', 
        'question': "Seaborn을 사용하여 데이터프레임 `df`에서 x축을 'age', y축을 'income'으로 하는 산점도(Scatter plot)를 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "수치형 변수 두 개 간의 관계를 2차원 평면에 점으로 찍어 표현할 때는 sns.scatterplot()을 사용합니다.",
        'check': lambda x: "sns.scatterplot" in _prep(x) and "age" in _prep(x) and "income" in _prep(x)
    }

def gen_py_str_split():
    ans = "text.split(',')"
    wrongs = ["text.split(',')", "text.slice(',')", "text.divide(',')"]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (문자열 분리)', 
        'question': "문자열 `text = '사과,바나나,포도'`가 주어졌을 때, 쉼표(',')를 기준으로 문자를 분리하여 리스트로 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "문자열의 .split('구분자') 메서드를 사용하면 특정 문자를 기준으로 잘라낸 리스트를 얻을 수 있습니다.",
        'check': lambda x: "split" in _prep(x) and "," in _prep(x)
    }


def gen_eda_concept_cat_num():
    ans = "sns.boxplot() 또는 sns.barplot()"
    wrongs = ["sns.scatterplot()", "sns.histplot()", "sns.lineplot()"]
    return {
        'topic': '[7] EDA 및 시각화 - EDA 개념 (범주형+수치형 시각화)', 
        'question': "탐색적 데이터 분석(EDA) 과정에서 '범주형 데이터(예: 요일, 성별)'에 따른 '수치형 데이터(예: 매출액, 나이)'의 차이나 분포를 비교하려고 합니다. 다음 중 가장 적절한 Seaborn 시각화 함수는 무엇일까요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "범주형(Categorical)과 수치형(Numerical) 데이터를 동시에 분석할 때는 분포를 보여주는 boxplot이나 평균을 보여주는 barplot이 가장 적절합니다. scatterplot은 수치+수치 조합에 주로 사용됩니다.",
        'check': lambda x: "box" in _prep(x) or "bar" in _prep(x),
        'force_type': 'radio'
    }

def gen_eda_concept_num_num():
    ans = "sns.scatterplot() 또는 sns.pairplot()"
    wrongs = ["sns.countplot()", "sns.pie()", "sns.boxplot()"]
    return {
        'topic': '[7] EDA 및 시각화 - EDA 개념 (다중 수치형 시각화)', 
        'question': "여러 개의 '수치형 변수'들 간의 상관관계(선형성, 군집 등)를 한눈에 파악하기 위해 산점도 행렬을 그리려고 합니다. 가장 적합한 함수 조합은 무엇일까요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "두 수치형 변수의 관계는 scatterplot을 사용하며, 데이터프레임 내 여러 수치형 변수 간의 관계를 한 번에 조망할 때는 pairplot을 사용합니다. countplot은 단일 범주형 빈도수에 사용됩니다.",
        'check': lambda x: "scatter" in _prep(x) or "pair" in _prep(x),
        'force_type': 'radio'
    }


def gen_easy_fillna():
    ans = "df['age'].fillna(df['age'].median())"
    wrongs = ["df['age'].dropna()", "df['age'] = df['age'].median()", "df.fillna()"]
    return {
        'topic': '[4] 데이터 전처리 - 데이터 전처리 (결측치 대체)', 
        'question': "데이터프레임 `df`의 'age' 컬럼에 있는 결측치(NaN)를 'age' 컬럼의 중앙값(median)으로 채우는(대체하는) 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "결측치를 단순히 제거(dropna)하지 않고, 중앙값이나 평균값으로 대체할 때는 `fillna()`를 사용합니다.",
        'check': lambda x: "fillna" in _prep(x) and "median" in _prep(x)
    }

def gen_ml_concept():
    ans = "분류(Classification)"
    wrongs = ["회귀(Regression)", "군집화(Clustering)", "차원 축소(Dimensionality Reduction)"]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 개념 (지도학습 방법론)', 
        'question': "우리가 예측하려는 타겟(Target) 데이터가 '생존여부(0 또는 1)', '꽃의 종류(Iris-setosa 등)'와 같은 '범주형(Categorical) 데이터'일 때 사용하는 머신러닝 모델링 기법을 무엇이라고 하나요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "타겟이 연속된 수치형(예: 주택 가격)이면 회귀(Regression), 딱 떨어지는 범주형(예: 생존/사망)이면 분류(Classification)를 사용합니다.",
        'check': lambda x: "분류" in x or "class" in x.lower(),
        'force_type': 'radio'
    }

def gen_ml_split_basic():
    ans = "train_test_split(X, y, test_size=0.2, random_state=42)"
    wrongs = [
        "train_test_split(X, y, 0.2, 42)", 
        "split(X, y, test_size=0.2)", 
        "pd.train_test_split(X, y, test_ratio=0.2)"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 데이터 분할 (train_test_split)', 
        'question': "머신러닝 모델 학습과 평가를 위해 특징(X)과 타겟(y) 데이터를 나눕니다. 테스트 데이터 비율(test_size)을 20%로, 난수 고정(random_state)을 42로 설정하여 분할하는 함수 호출 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Scikit-learn의 `train_test_split`은 X와 y를 학습용/테스트용으로 나누어주는 가장 기본적인 데이터 준비 함수입니다.",
        'check': lambda x: "train_test_split" in _prep(x) and "0.2" in _prep(x) and "42" in _prep(x)
    }

def gen_py_list_slice():
    ans = "lst[::-1]"
    wrongs = ["lst[-1:]", "lst.reverse()", "reversed(lst)"]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (리스트 슬라이싱)', 
        'question': "리스트 `lst`의 요소 순서를 완전히 거꾸로 뒤집은 새로운 리스트를 슬라이싱(slicing) 기법만 사용하여 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "[start:stop:step] 구조에서 step을 -1로 지정( [::-1] )하면 역순 슬라이싱이 됩니다.",
        'check': lambda x: "[::-1]" in _prep(x)
    }

def gen_sns_boxplot():
    import random
    x = random.choice(['day', 'sex'])
    y = random.choice(['tip', 'total_bill'])
    hue = random.choice(['smoker', 'time'])
    ans = f"sns.boxplot(data=df, x='{x}', y='{y}', hue='{hue}')"
    wrongs = [
        f"sns.violinplot(data=df, x='{x}', y='{y}')", 
        f"sns.boxplot(data=df, x='{y}', y='{x}')", 
        f"sns.histplot(data=df, x='{x}', hue='{hue}')"
    ]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (boxplot)', 
        'question': f"데이터 `df`에서 x축을 '{x}', y축을 '{y}'로 설정하고, '{hue}' 기준으로 쪼개어 박스플롯(Boxplot)을 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.boxplot()은 데이터의 분포와 이상치를 한눈에 파악하기 좋으며, hue 파라미터를 추가하면 그룹별로 비교할 수 있습니다.",
        'check': lambda x: "boxplot" in _prep(x) and x in _prep(x) and y in _prep(x) and hue in _prep(x)
    }

def gen_np_log1p():
    import random
    col = random.choice(['price', 'spc_R', 'population'])
    ans = f"np.log1p(df['{col}'])"
    wrongs = [
        f"np.log(df['{col}'])", 
        f"np.log10(df['{col}'])", 
        f"df['{col}'].log1p()"
    ]
    return {
        'topic': '[4] 데이터 전처리 - Numpy 로그 변환 (log1p)', 
        'question': f"데이터프레임 `df`의 '{col}' 열의 값이 너무 한쪽으로 치우쳐 있어 로그 변환을 하려고 합니다. 0 값 오류를 방지하기 위해 1을 더한 후 로그를 취하는 Numpy 함수를 사용하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "np.log1p()는 log(1+x)를 의미하며, 값이 0일 때 무한대(-inf) 오류가 발생하는 것을 방지하는 안전한 로그 변환 함수입니다.",
        'check': lambda x: "log1p" in _prep(x) and col in _prep(x)
    }

# =====================================================================
# [HARD POOL] - 심화 개념, 함정 문제 (총 4문제 출제용)
# =====================================================================

def gen_hard_apply():
    ans = "df['reg'].apply(get_sido)"
    wrongs = ["df['reg'].map(get_sido())", "apply(get_sido, df['reg'])", "df['reg'].apply(get_sido(x))"]
    return {
        'topic': '[4] 데이터 전처리 - 사용자 정의 함수 적용 (apply)', 
        'question': "`get_sido(x)`라는 사용자 정의 함수가 이미 선언되어 있습니다. 데이터프레임 `df`의 'reg' 컬럼의 모든 행 데이터에 이 함수를 일괄 적용시키는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Series.apply(함수명)을 사용하면 한 열의 모든 데이터에 똑같은 함수 로직을 반복문 없이 쉽게 적용할 수 있습니다. 괄호() 없이 함수 이름만 넘겨야 합니다.",
        'check': lambda x: "apply" in _prep(x) and "get_sido" in _prep(x) and "()" not in _prep(x)
    }

def gen_hard_groupby():
    ans = "df.groupby('sido')['spc_R'].mean()"
    wrongs = ["df.groupby('sido').mean('spc_R')", "df['spc_R'].groupby('sido').mean()", "pd.groupby(df, 'sido')['spc_R'].mean()"]
    return {
        'topic': '[5] 데이터 집계 - 그룹화 집계 (groupby)', 
        'question': "데이터프레임 `df`에서 'sido'(시도) 별로 그룹을 묶은 뒤, 'spc_R'(특목고 진학률)의 평균(mean)을 구하는 Series 반환 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.groupby('그룹기준열')['계산대상열'].통계함수() 형태로 작성하면 카테고리별 집계 데이터를 빠르게 추출할 수 있습니다.",
        'check': lambda x: "groupby" in _prep(x) and "sido" in _prep(x) and "spc_r" in _prep(x) and "mean" in _prep(x)
    }

def gen_hard_merge():
    ans = "pd.merge(df1, df2, on='code', how='left')"
    wrongs = ["df1.join(df2, on='code', type='left')", "pd.concat([df1, df2], axis=1)", "df1.merge_left(df2, 'code')"]
    return {
        'topic': '[6] 데이터 병합 - 데이터 병합 (Left Merge)', 
        'question': "데이터프레임 `df1`과 `df2`를 'code' 컬럼 기준으로 Left Merge(왼쪽 기준 병합) 하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.merge() 함수에서 how='left' 파라미터를 사용하면 왼쪽 데이터프레임을 기준으로 삼아 병합을 수행합니다.",
        'check': lambda x: "merge" in _prep(x) and "left" in _prep(x) and "code" in _prep(x)
    }

def gen_hard_pivot():
    ans = "pd.pivot_table(df, index='sex', columns='smoker', values='tip', aggfunc='mean')"
    wrongs = ["df.groupby(['sex','smoker'])['tip'].mean().pivot()", "pd.pivot(df, 'sex', 'smoker', 'tip')", "df.pivot_table(group='sex', target='tip', func='mean')"]
    return {
        'topic': '[5] 데이터 집계 - 피벗 테이블 (Pivot Table)', 
        'question': "데이터프레임 `df`에서 인덱스(행)를 'sex', 컬럼(열)을 'smoker'로 설정하고 'tip'의 평균(mean)을 구하는 2차원 피벗 테이블 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.pivot_table()을 사용하면 엑셀의 피벗 테이블처럼 복수의 카테고리에 대한 통계량(2차원 매트릭스)을 요약할 수 있습니다.",
        'check': lambda x: "pivot_table" in _prep(x) and "sex" in _prep(x) and "smoker" in _prep(x) and "tip" in _prep(x)
    }

def gen_ml_knn():
    ans = "KNeighborsClassifier(n_neighbors=5)"
    wrongs = [
        "KNeighborsRegressor()", 
        "KNNClassifier(k=5)", 
        "KNeighborsClassifier.fit()"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 모델 튜닝 (KNN)', 
        'question': "주변 이웃 데이터들의 클래스를 다수결로 판단하는 K-최근접 이웃(KNN) 분류 모델 객체를 생성하되, 이웃의 수(K)를 5로 설정하는 파라미터를 포함해 작성하세요. (단축 임포트 가정)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "KNeighborsClassifier(n_neighbors=K)에서 n_neighbors 파라미터는 모델의 복잡도를 결정하는 핵심 하이퍼파라미터입니다.",
        'check': lambda x: "kneighborsclassifier" in _prep(x) and "n_neighbors" in _prep(x)
    }

def gen_ml_split_stratify():
    ans = "train_test_split(X, y, test_size=0.2, stratify=y)"
    wrongs = [
        "train_test_split(X, y, 0.2)", 
        "train_test_split(X, y, test_size=0.2, balance=True)", 
        "pd.train_test_split(X, y, test_size=0.2, stratify=y)"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 데이터 분할과 층화추출 (stratify)', 
        'question': "`train_test_split`을 사용하여 데이터를 훈련셋 80%, 검증셋 20%로 나눌 때, 타겟 변수 `y`의 원본 클래스 비율(예: 1:1:1)을 훈련셋과 검증셋에서도 동일하게 유지하도록 강제하는 파라미터를 포함해 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "stratify=y 파라미터를 지정하면 샘플링 편향을 막고 데이터의 원래 클래스 분포 비율을 그대로 유지하며 분할합니다.",
        'check': lambda x: "train_test_split" in _prep(x) and "stratify=y" in _prep(x)
    }

def gen_ml_cv():
    ans = "cross_val_score(knn, train_x, train_y, cv=4).mean()"
    wrongs = [
        "cross_validate(knn, train_x, train_y, k=4).mean()", 
        "knn.score(train_x, train_y, cv=4)", 
        "cross_val_score(knn, train_x, train_y, fold=4).average()"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 교차 검증 (Cross Validation)', 
        'question': "학습된 패턴이 우연인지 아닌지 확인하기 위해, 모델 `knn`과 훈련데이터 `train_x`, `train_y`를 4-Fold 교차 검증(Cross Validation)하여 얻어진 4개의 평가 점수 평균(mean)을 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "cross_val_score() 함수에 cv=4(폴드 수)를 주어 교차 검증을 수행한 뒤, 반환된 배열의 .mean()을 호출하여 평균 정확도를 봅니다.",
        'check': lambda x: "cross_val_score" in _prep(x) and "cv=4" in _prep(x) and "mean" in _prep(x)
    }

# -------------------------------------------------------------------
# PLUGIN SYSTEM / STRATEGY REGISTRY
# -------------------------------------------------------------------


def gen_killer_chained_assignment():
    ans = "df.loc[df['A'] > 5, 'B'] = 10"
    wrongs = [
        "df[df['A'] > 5]['B'] = 10",
        "df.query('A > 5')['B'] = 10",
        "df.where(df['A'] > 5)['B'] = 10"
    ]
    return {
        'topic': '[0] 기타 - 킬러 - Pandas 인덱싱 (Chained Assignment)',
        'question': "데이터프레임 `df`에서 'A' 컬럼의 값이 5보다 큰 행들의 'B' 컬럼 값을 10으로 변경하려고 합니다. `SettingWithCopyWarning`을 피하면서 원본 데이터를 안전하게 수정하는 올바른 코드는 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "마스킹 조건으로 데이터를 필터링한 후 다시 컬럼에 접근하여 값을 할당하는 행위(`df[...][...] = ...`)는 Chained Assignment를 발생시켜 원본 데이터가 변경되지 않을 수 있습니다. 반드시 `.loc[행조건, 열이름]`을 사용하여 단일 연산으로 값을 할당해야 합니다.",
        'force_type': 'radio'
    }

def gen_killer_merge_suffixes():
    ans = "df1과 df2에 공통된 이름의 컬럼이 병합 키가 아닌 경우, 구분을 위해 '_left', '_right' 접미사가 붙는다."
    wrongs = [
        "merge는 기본적으로 outer join으로 수행되며, 누락된 값은 0으로 채워진다.",
        "on 파라미터를 지정하지 않으면 에러가 발생하므로 반드시 지정해야 한다.",
        "인덱스를 기준으로 병합할 때는 merge 함수 대신 반드시 join 함수만 사용해야 한다."
    ]
    return {
        'topic': '[6] 데이터 병합 - 킬러 - Pandas 데이터 병합 (Merge)',
        'question': "Pandas의 `pd.merge(df1, df2)` 동작 방식에 대한 설명으로 올바른 것은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "`merge`의 기본 동작은 `inner join`이며, `on`을 생략하면 이름이 겹치는 모든 컬럼을 병합 키로 자동 사용합니다. 인덱스 병합은 `left_index=True`, `right_index=True` 옵션으로 `merge`에서도 가능합니다. 공통 컬럼이 병합 키가 아닐 경우 자동으로 접미사(_x, _y)가 붙습니다.",
        'force_type': 'radio'
    }

ALL_KILLER = [gen_killer_chained_assignment, gen_killer_merge_suffixes]

class QuizStrategy:
    def __init__(self, id, name, description, easy_pool, hard_pool, killer_pool=None):
        self.id = id
        self.name = name
        self.description = description
        self.easy_pool = easy_pool
        self.hard_pool = hard_pool
        self.killer_pool = killer_pool or []


def gen_easy_while_loop():
    ans = "012"
    wrongs = ["0123", "12", "123", "01"]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (반복문)', 
        'question': "다음 코드의 실행 결과로 올바른 것을 고르시오.\n\n```python\ncount = 0\nwhile count < 3:\n    print(count, end='')\n    count += 1\n```",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "while 반복문은 count가 0, 1, 2일 때 실행되며, end='' 옵션으로 인해 줄바꿈 없이 012가 연속 출력됩니다.",
        'force_type': 'radio'
    }

def gen_easy_list_mutability():
    ans = "리스트는 수정이 가능하며, 문자열은 새로운 객체가 생성된다."
    wrongs = ["문자열은 수정이 가능하며, 리스트는 새로운 객체가 생성된다.", "리스트와 문자열 모두 수정할 수 있다.", "리스트와 문자열 모두 수정할 수 없다.", "리스트는 수정이 불가능하며, 문자열만 수정할 수 있다."]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (자료형)', 
        'question': "다음 코드를 실행했을 때, 리스트와 문자열의 결과 처리에 대한 설명으로 옳은 것을 고르시오.\n\n```python\nmy_list = [1, 2, 3]\nmy_string = 'hello'\nmy_list[0] = 10\nmy_string = 'H' + my_string[1:]\n```",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "리스트(List)는 가변(Mutable) 객체이므로 값 수정이 가능하지만, 문자열(String)은 불변(Immutable) 객체이므로 재할당 시 새로운 객체가 생성됩니다.",
        'force_type': 'radio'
    }

def gen_easy_scaling_reason():
    ans = "변수들의 범위를 일정하게 맞추기 위해서"
    wrongs = ["변수들의 상관관계를 파악하기 위해서", "변수들의 선형 관계를 파악하기 위해서", "학습시간을 줄이기 위해서", "이상치를 자동으로 제거하기 위해서"]
    return {
        'topic': '[4] 데이터 전처리 - 데이터 전처리 (스케일링)', 
        'question': "데이터 분석 및 머신러닝 학습 시, 변수들의 스케일링(Scaling)이 필요한 이유를 가장 잘 설명한 것을 고르시오.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "스케일링(StandardScaler, MinMaxScaler 등)은 서로 다른 단위와 범위를 가진 변수(특성)들의 범위를 일정하게 맞추어, 모델 학습 시 특정 변수가 과도한 영향을 미치는 것을 방지하기 위해 수행합니다.",
        'force_type': 'radio'
    }

def gen_easy_iloc_slicing():
    ans = "df.iloc[0:2]"
    wrongs = ["df.loc[0:2]", "df.iloc[0:1]", 'df.loc["A"]']
    return {
        'topic': '[1] 파이썬 Basic - 데이터프레임 슬라이싱 (iloc)', 
        'question': "데이터프레임 df에서 첫 번째 행과 두 번째 행(0번과 1번 위치)만 정확히 선택하는 코드로 올바른 것을 고르시오.\n\n(단, 인덱스는 기본 RangeIndex를 사용함)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "iloc[0:2]는 위치 기반 인덱싱으로 0번째와 1번째 행(마지막 인덱스 2는 포함 안 함)을 선택합니다. loc[0:2]는 0, 1, 2행까지 총 3개의 행을 가져오게 되므로 주의해야 합니다.",
        'force_type': 'radio'
    }

def gen_hard_random_forest_concept():
    ans = "Random Forest는 주로 선형 회귀 문제에 사용된다."
    wrongs = [
        "Random Forest는 Decision Tree 모델에 앙상블 학습을 적용한 모델이다.",
        "Random Forest에서 bagging은 분산을 줄이기 위해 사용된다.",
        "Random Forest는 overfitting 문제를 완화한다.",
        "Random Forest는 여러 개의 Decision Tree를 생성하고, 그 예측 결과들을 통해 최종 예측을 만든다."
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 개념 (앙상블)', 
        'question': "다음 중 Random Forest 알고리즘에 대한 설명으로 틀린 것을 고르시오.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Random Forest는 트리 기반의 앙상블 모델로, 분류(Classification)와 비선형 회귀(Regression) 문제 모두에 널리 사용됩니다. 단순히 선형 회귀에만 사용된다는 것은 틀린 설명입니다.",
        'force_type': 'radio'
    }

def gen_hard_train_predict():
    ans = "X_test"
    wrongs = ["X_train", "y_test", "X", "Y"]
    return {
        'topic': '[8] 머신러닝 기초 - 모델 예측 API', 
        'question': "다음 코드에서 결정 트리 모델을 학습시키고, 테스트 데이터에 대한 예측을 수행하려고 합니다. 빈칸에 들어갈 코드로 가장 적절한 것을 고르시오.\n\n```python\ntree = DecisionTreeClassifier()\ntree.fit(X_train, y_train)\n\ny_pred = tree.predict(________)\n```",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "모델 학습(fit)에는 훈련 데이터(X_train, y_train)가 사용되고, 새로운 데이터에 대한 예측(predict)을 수행할 때는 테스트 데이터의 피처(X_test)를 입력으로 제공해야 합니다.",
        'force_type': 'radio'
    }

def gen_hard_confusion_matrix():
    ans = "Confusion Matrix"
    wrongs = ["Feature Importance", "Hyperparameter Tuning", "Data Scaling", "Normalization"]
    return {
        'topic': '[8] 머신러닝 기초 - 모델 평가 지표', 
        'question': "Scikit-Learn에서 분류 모델의 학습 성능을 평가하기 위해 사용할 수 있는 방법 중 하나로 가장 적절한 것을 고르시오.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Confusion Matrix(혼동 행렬)는 분류 모델의 정답과 오답 패턴(TP, FP, FN, TN)을 파악하여 정확도, 정밀도, 재현율 등을 도출하는 핵심적인 평가 도구입니다.",
        'force_type': 'radio'
    }


ALL_EASY = [
    gen_easy_while_loop, gen_easy_list_mutability, gen_easy_scaling_reason, gen_easy_iloc_slicing,
    gen_eda_concept_cat_num,
    gen_easy_read_excel, gen_easy_head, gen_easy_dtypes, gen_easy_isnull, 
    gen_easy_dropna, gen_easy_filter, gen_easy_loc, gen_easy_value_counts,
    gen_viz_countplot, gen_viz_histplot, gen_viz_scatter, gen_sns_boxplot,
    gen_py_str_split, gen_py_list_slice, gen_np_log1p,
    gen_easy_fillna, gen_ml_concept, gen_ml_split_basic
]

ALL_HARD = [
    gen_hard_random_forest_concept, gen_hard_train_predict, gen_hard_confusion_matrix,
    gen_eda_concept_num_num,
    gen_hard_apply, gen_hard_groupby, gen_hard_merge, gen_hard_pivot,
    gen_ml_knn, gen_ml_split_stratify, gen_ml_cv
]

STRATEGIES = {
    'bootcamp_day1_4': QuizStrategy(
        id='bootcamp_day1_4',
        name='Day 1~2 Bootcamp (시험 대비)',
        description='단기 부트캠프 진도에 맞춰, 쉬운 문제 16개와 심화/응용 문제 4개가 출제됩니다.',
        easy_pool=ALL_EASY,  
        hard_pool=ALL_HARD,
        killer_pool=ALL_KILLER
    ),
    'comprehensive': QuizStrategy(
        id='comprehensive',
        name='종합 마스터 (전범위 딥다이브)',
        description='전 범위를 다루는 하드코어 모드입니다. 응용 문제의 비율이 높아집니다.',
        easy_pool=ALL_EASY,
        hard_pool=ALL_HARD,
        killer_pool=ALL_KILLER
    )
}

def get_strategy(strategy_id='bootcamp_day1_4'):
    return STRATEGIES.get(strategy_id, STRATEGIES['bootcamp_day1_4'])

def generate_exam_quizzes(strategy_id='bootcamp_day1_4'):
    strategy = get_strategy(strategy_id)
    easy_pool = strategy.easy_pool
    hard_pool = strategy.hard_pool
    killer_pool = strategy.killer_pool
    
    quizzes = []
    
    def add_questions(pool, count):
        for _ in range(count):
            f = random.choice(pool)
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
            
    if strategy_id == 'bootcamp_day1_4':
        # 모의고사는 20개 중 16개 베이직, 2개 심화, 2개 킬러
        add_questions(easy_pool, 16)
        add_questions(hard_pool, 2)
        add_questions(killer_pool, 2)
    else:
        # 종합 마스터는 비율을 8:8:4 로 더욱 어렵게
        add_questions(easy_pool, 8)
        add_questions(hard_pool, 8)
        if killer_pool:
            add_questions(killer_pool, 4)
            
    random.shuffle(quizzes)
    return quizzes


def get_available_topics(strategy_id='bootcamp_day1_4'):
    strategy = get_strategy(strategy_id)
    pool = strategy.easy_pool + strategy.hard_pool
    topics = set()
    for f in pool:
        topics.add(f()['topic'])
    return ["전체 랜덤"] + sorted(list(topics))

def generate_single_quiz(strategy_id='bootcamp_day1_4', topic=None):
    strategy = get_strategy(strategy_id)
    pool = strategy.easy_pool + strategy.hard_pool
    
    if topic and topic != '전체 랜덤':
        pool = [f for f in pool if f()['topic'] == topic]
        if not pool:
            pool = strategy.easy_pool + strategy.hard_pool
    
    f = random.choice(pool)
    q = f()
    
    q['type'] = 'radio'
    opts = [q['expected']] + q['wrongs'][:3]
    random.shuffle(opts)
    q['choices'] = opts
    return q
