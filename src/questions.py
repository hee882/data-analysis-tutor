import random

def _prep(text):
    return str(text).replace(' ', '').replace('"', "'").lower()


def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    ans = f"df = pd.read_{ext}('data.{ext}')"
    wrongs = [f"df = pd.read(file='data.{ext}', format='{ext}')", f"df = pd.load_{ext}('data.{ext}')", f"df.read_{ext}('data.{ext}')", f"pd.DataFrame('data.{ext}', type='{ext}')"]
    return {
        'topic': '데이터 로드', 'question': f"`data.{ext}` 파일을 읽어 `df`에 할당하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "pd.read_csv 또는 pd.read_excel을 사용합니다.",
        'check': lambda x: f"read_{ext}" in _prep(x) and "data" in _prep(x) and "df" in _prep(x)
    }

def gen_easy_head():
    n = random.randint(3, 8)
    ans = f"df.head({n})"
    wrongs = [f"df.head(rows={n})", f"df.show({n})", f"df.top({n})", f"df.iloc[:{n}, :].head()"]
    return {
        'topic': '데이터 미리보기', 'question': f"`df`의 상단 {n}개 행을 확인하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.head(n) 메서드를 사용합니다.",
        'check': lambda x: "head" in _prep(x) and str(n) in _prep(x)
    }

def gen_easy_info():
    ans = "df.info()"
    wrongs = ["df.summary(nulls=True)", "df.describe(types=True)", "pd.info(df)", "df.dtypes().sum()"]
    return {
        'topic': '데이터 메타정보', 'question': "`df`의 행 개수, 컬럼 타입, 결측치를 요약 출력하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.info()는 데이터 전처리의 기본입니다.",
        'check': lambda x: "info" in _prep(x)
    }

def gen_easy_isnull():
    ans = "df.isnull().sum()"
    wrongs = ["df.isnull().count()", "df.isna().total()", "df.count(nulls=True)", "pd.isnull(df).sum(axis=1)"]
    return {
        'topic': '결측치 집계', 'question': "`df`의 각 컬럼별 결측치(NaN) 총합을 구하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "isnull().sum() 또는 isna().sum()을 사용합니다.",
        'check': lambda x: ("isnull" in _prep(x) or "isna" in _prep(x)) and "sum" in _prep(x)
    }

def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    ans = f"df['{col}'].fillna({val})"
    wrongs = [f"df['{col}'].fillna(value={val}, inplace=False)", f"df.fillna(col='{col}', val={val})", f"df['{col}'].replace(NaN, {val})", f"df['{col}'].dropna().add({val})"]
    return {
        'topic': '결측치 대체', 'question': f"`df['{col}']`의 결측치를 {val} 값으로 일괄 대체하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "fillna() 메서드를 사용합니다.",
        'check': lambda x: "fillna" in _prep(x) and str(val).lower() in _prep(x) and col.lower() in _prep(x)
    }

def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    ans = f"df.drop(columns=['{col}'])"
    wrongs = [f"df.drop('{col}', axis=0)", f"df.delete(columns='{col}')", f"df.remove('{col}')", f"del df.columns['{col}']"]
    return {
        'topic': '컬럼 제거', 'question': f"`df`에서 `{col}` 컬럼을 삭제하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "drop(columns=[...]) 또는 drop(..., axis=1)을 사용합니다.",
        'check': lambda x: "drop" in _prep(x) and col.lower() in _prep(x) and ("columns" in _prep(x) or "axis=1" in _prep(x))
    }

def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    ans = f"df[df['{col}'] >= {val}]"
    wrongs = [f"df.filter(df['{col}'] >= {val})", f"df.where('{col}' >= {val})", f"df.loc['{col}' >= {val}]", f"df[df.{col} => {val}]"]
    return {
        'topic': '조건부 필터링', 'question': f"`df`에서 `{col}` 값이 {val} 이상(>=)인 행만 추출하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "불리언 인덱싱 df[df['col'] >= val] 형태를 사용합니다.",
        'check': lambda x: col.lower() in _prep(x) and str(val) in _prep(x) and ">=" in _prep(x)
    }

def gen_viz_bar():
    col1 = random.choice(['region', 'category']); col2 = random.choice(['sales', 'count'])
    ans = f"df.plot(kind='bar', x='{col1}', y='{col2}')"
    wrongs = [f"df.plot.bar(y='{col1}', x='{col2}')", f"df.plot(type='bar', x='{col1}', y='{col2}')", f"pd.barplot(df, x='{col1}', y='{col2}')", f"df.groupby('{col1}').plot('{col2}', kind='bar')"]
    return {
        'topic': '막대 그래프', 'question': f"Pandas 내장 함수로 x축 '{col1}', y축 '{col2}'의 막대 그래프를 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='bar') 또는 .plot.bar()를 사용합니다.",
        'check': lambda x: "plot" in _prep(x) and "bar" in _prep(x) and col1.lower() in _prep(x) and col2.lower() in _prep(x)
    }

def gen_viz_scatter():
    col1 = random.choice(['age', 'height']); col2 = random.choice(['score', 'salary'])
    ans = f"df.plot(kind='scatter', x='{col1}', y='{col2}')"
    wrongs = [f"df.plot.scatter(axis_x='{col1}', axis_y='{col2}')", f"df.scatter(x='{col1}', y='{col2}')", f"pd.plot(df, kind='scatter', x='{col1}', y='{col2}')", f"df.plot(x='{col1}', y='{col2}', mode='scatter')"]
    return {
        'topic': '산점도', 'question': f"Pandas 함수로 x축 '{col1}', y축 '{col2}'의 산점도(scatter plot)를 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='scatter')를 사용합니다.",
        'check': lambda x: "plot" in _prep(x) and "scatter" in _prep(x) and col1.lower() in _prep(x) and col2.lower() in _prep(x)
    }

def gen_viz_hist():
    col = random.choice(['score', 'salary']); bins = random.choice([10, 20])
    ans = f"df['{col}'].plot(kind='hist', bins={bins})"
    wrongs = [f"df['{col}'].plot(kind='hist', split={bins})", f"df.hist(column='{col}', chunks={bins})", f"df['{col}'].plot.histogram({bins})", f"pd.hist(df['{col}'], bins={bins})"]
    return {
        'topic': '히스토그램', 'question': f"`df['{col}']`의 구간(bins)을 {bins}개로 나눈 히스토그램을 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='hist', bins=N)을 사용합니다.",
        'check': lambda x: "hist" in _prep(x) and str(bins) in _prep(x) and col.lower() in _prep(x)
    }

def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    ans = f"pd.merge(df1, df2, on='user_id', how='{how}')"
    wrongs = [f"df1.join(df2, on='user_id', type='{how}')", f"pd.concat([df1, df2], axis=1, join='{how}')", f"df1.merge(df2, by='user_id', how='{how}')", f"pd.merge(df1, df2, index='user_id', method='{how}')"]
    return {
        'topic': '데이터 병합', 'question': f"`df1`과 `df2`를 'user_id' 기준으로 `{how}` Join 하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "pd.merge() 함수를 활용합니다.",
        'check': lambda x: "merge" in _prep(x) and "user_id" in _prep(x) and how.lower() in _prep(x)
    }

def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    ans = f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')"
    wrongs = [f"df.pivot(group='{idx}', col='month', val='sales', agg='sum')", f"df.groupby(['{idx}', 'month'])['sales'].sum().unstack()", f"df.pivot_table(rows='{idx}', cols='month', data='sales', agg='sum')", f"pd.crosstab(index=df['{idx}'], columns=df['month'], values='sales', aggfunc='sum')"]
    return {
        'topic': '피벗 테이블', 'question': f"`df`에서 행 '{idx}', 열 'month', 값 'sales', 집계 'sum'인 피벗 테이블 코드를 작성하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.pivot_table()을 사용합니다.",
        'check': lambda x: "pivot_table" in _prep(x) and idx.lower() in _prep(x) and "month" in _prep(x) and "sales" in _prep(x) and "sum" in _prep(x)
    }

def gen_hard_str():
    ans = "df['price'].str.replace('$', '').astype(float)"
    wrongs = ["df['price'].replace('$', '').to_float()", "df['price'].str.remove('$').astype(float)", "df['price'].apply(lambda x: float(x.replace('$', '')))", "df['price'].str.strip('$').astype('float64')"]
    return {
        'topic': '문자열 파싱', 'question': "`df['price']` 컬럼 내의 달러 기호('$')를 제거하고 float으로 변환하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".str.replace() 후 .astype(float)을 체이닝합니다.",
        'check': lambda x: "replace" in _prep(x) and "$" in _prep(x) and ("astype" in _prep(x) or "float" in _prep(x))
    }

def gen_hard_dt():
    ans = "df['date'].dt.month"
    wrongs = ["df['date'].month", "pd.to_datetime(df['date']).get_month()", "df['date'].time.month", "df['date'].dt.get('month')"]
    return {
        'topic': '시계열 처리', 'question': "`df['date']` 컬럼(datetime 형)에서 '월(month)' 데이터만 추출하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".dt 접근자를 사용합니다.",
        'check': lambda x: ".dt.month" in _prep(x)
    }

def gen_numpy_array():
    shape = random.choice([(3,3), (2,4), (4,4)])
    ans = f"np.zeros({shape})"
    wrongs = [f"np.empty({shape[0]}, {shape[1]})", f"np.array(0, shape={shape})", f"pd.zeros({shape})", f"np.matrix(zeros=True, size={shape})"]
    return {
        'topic': 'Numpy 배열 생성', 'question': f"모든 원소가 0으로 채워진 크기가 `{shape}`인 Numpy 배열을 생성하세요.",
        'expected': ans, 'wrongs': wrongs, 'explanation': "np.zeros((행, 열)) 함수를 사용합니다.",
        'check': lambda x: "zeros" in _prep(x) and str(shape[0]) in _prep(x) and str(shape[1]) in _prep(x)
    }

def gen_ml_split():
    size = random.choice([0.2, 0.25, 0.3])
    ans = f"train_test_split(X, y, test_size={size}, random_state=42)"
    wrongs = [f"split_data(X, y, ratio={1-size})", f"train_test_split(y, X, train_size={size})", f"model_selection.split(X, y, test={size})", f"train_test_split(X, y, test_ratio={size})"]
    return {
        'topic': '머신러닝 데이터 분할', 'question': f"Scikit-learn을 사용하여 특성 데이터 `X`와 타겟 `y`를 테스트 세트 비율 `{size}`로 분할하세요. (random_state=42)",
        'expected': ans, 'wrongs': wrongs, 'explanation': "sklearn.model_selection.train_test_split()을 사용합니다.",
        'check': lambda x: "train_test_split" in _prep(x) and str(size) in _prep(x) and "42" in _prep(x)
    }

def gen_ml_rf():
    estimators = random.choice([100, 200, 500])
    ans = f"RandomForestClassifier(n_estimators={estimators}, random_state=42)"
    wrongs = [f"RandomForest(trees={estimators})", f"RandomForestClassifier(max_trees={estimators})", f"EnsembleRF(n={estimators})", f"RandomForestClassifier(count={estimators})"]
    return {
        'topic': '머신러닝 모델 객체 생성', 'question': f"Scikit-learn을 사용하여 트리의 개수가 `{estimators}`개인 랜덤 포레스트 분류기 객체를 생성하세요. (random_state=42)",
        'expected': ans, 'wrongs': wrongs, 'explanation': "RandomForestClassifier(n_estimators=...)을 사용합니다.",
        'check': lambda x: "randomforestclassifier" in _prep(x) and str(estimators) in _prep(x)
    }

def gen_viz_sns():
    x_col = random.choice(['total_bill', 'age'])
    y_col = random.choice(['tip', 'salary'])
    ans = f"sns.scatterplot(data=df, x='{x_col}', y='{y_col}')"
    wrongs = [f"sns.scatter(x='{x_col}', y='{y_col}', df=data)", f"df.sns.plot('{x_col}', '{y_col}')", f"sns.plot(kind='scatter', x='{x_col}', y='{y_col}')", f"sns.scatterplot('{x_col}', '{y_col}')"]
    return {
        'topic': 'Seaborn 시각화', 'question': f"Seaborn 라이브러리를 사용하여 `df`의 x축 '{x_col}', y축 '{y_col}' 산점도를 그리세요.",
        'expected': ans, 'wrongs': wrongs, 'explanation': "sns.scatterplot(data=..., x=..., y=...)을 사용합니다.",
        'check': lambda x: "sns.scatterplot" in _prep(x) and x_col.lower() in _prep(x) and y_col.lower() in _prep(x)
    }


def gen_param_nuance_concat():
    axis = random.choice([0, 1])
    desc = "행(위아래)으로 길게 붙이고 싶습니다" if axis == 0 else "열(좌우)로 넓게 붙이고 싶습니다"
    ans = f"pd.concat([df1, df2], axis={axis})"
    wrong_axis = 1 if axis == 0 else 0
    wrongs = [
        f"pd.concat([df1, df2], axis={wrong_axis})", 
        f"df1.append(df2, axis={axis})", 
        f"pd.merge(df1, df2, how='outer')"
    ]
    return {
        'topic': '파라미터의 차이 (Concat Axis)', 
        'question': f"두 데이터프레임 `df1`과 `df2`를 **{desc}**. 이때 파라미터 `axis`의 값으로 올바른 전체 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"axis=0은 행 방향(수직 병합), axis=1은 열 방향(수평 병합)을 의미합니다.",
        'check': lambda x: "concat" in _prep(x) and f"axis={axis}" in _prep(x)
    }

def gen_param_nuance_dropdup():
    keep = random.choice(['first', 'last'])
    desc = "가장 처음 발견된 원본 데이터" if keep == 'first' else "가장 마지막에 갱신된 데이터"
    ans = f"df.drop_duplicates(subset=['user_id'], keep='{keep}')"
    wrong_keep = 'last' if keep == 'first' else 'first'
    wrongs = [
        f"df.drop_duplicates(subset=['user_id'], keep='{wrong_keep}')", 
        f"df.drop_duplicates(subset=['user_id'], drop='{keep}')", 
        f"df.unique(subset=['user_id'], keep='{keep}')"
    ]
    return {
        'topic': '파라미터의 차이 (중복 제거)', 
        'question': f"`df`에서 'user_id'가 중복되는 행들을 제거하려고 합니다. 단, **{desc}**만 남기고 나머지를 지워야 합니다. 알맞은 파라미터를 사용하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"keep='first'는 첫 번째 값을 유지, keep='last'는 마지막 값을 유지합니다.",
        'check': lambda x: "drop_duplicates" in _prep(x) and "user_id" in _prep(x) and f"keep='{keep}'" in _prep(x)
    }


def gen_py_loop_control():
    break_val = random.choice([3, 4])
    skip_val = random.choice([1, 2])
    
    code = f"s = 0\nfor i in range(5):\n    if i == {skip_val}:\n        continue\n    if i == {break_val}:\n        break\n    s += i\nprint(s)"
    
    s = 0
    for i in range(5):
        if i == skip_val: continue
        if i == break_val: break
        s += i
        
    expected = str(s)
    wrongs = [str(s + skip_val), str(s + break_val), str(s - 1), str(s + 1), "0"]
    wrongs = list(set([w for w in wrongs if w != expected]))
        
    return {
        'topic': 'Python 제어문 (break/continue)',
        'question': f"다음 파이썬 코드의 최종 출력(print) 결과를 예측하세요.\n```python\n{code}\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"i가 {skip_val}일 때는 continue로 넘어갔고, {break_val}일 때 break로 반복문이 완전히 종료되었습니다. 따라서 누적합은 {expected}입니다.",
        'check': lambda x: _prep(expected) in _prep(x)
    }

def gen_py_str_split():
    sep = random.choice([',', '-'])
    idx = random.choice([1, -1])
    sample = "apple,banana,cherry" if sep == ',' else "서울-대전-대구-부산"
    
    code = f"text = '{sample}'\nprint(text.split('{sep}')[{idx}])"
    
    parts = sample.split(sep)
    expected = f"'{parts[idx]}'"
    
    wrong_idx1 = 0 if idx != 0 else 1
    wrong_idx2 = 2 if idx != 2 else 1
    wrongs = [f"'{parts[wrong_idx1]}'", f"'{parts[wrong_idx2]}'", f"'{parts[idx][:2]}'", "IndexError"]
    wrongs = list(set([w for w in wrongs if w != expected]))
    
    return {
        'topic': 'Python 문자열 파싱 (split)',
        'question': f"다음 파이썬 코드의 최종 출력(print) 결과를 예측하세요.\n```python\n{code}\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"split('{sep}')을 통해 리스트로 분리한 후, 인덱스 {idx}에 해당하는 요소를 추출합니다.",
        'check': lambda x: _prep(parts[idx]) in _prep(x)
    }

def gen_py_list_slice():
    lst = [10, 20, 30, 40, 50]
    start = random.choice([1, 2])
    end = random.choice([4, -1])
    
    code = f"nums = {lst}\nprint(nums[{start}:{end}])"
    
    expected = str(lst[start:end])
    wrongs = [
        str(lst[start:end+1]), 
        str(lst[start-1:end]), 
        str(lst[start:end-1]),
        str(lst[start-1:end+1])
    ]
    wrongs = list(set([w for w in wrongs if w != expected]))
        
    return {
        'topic': 'Python 리스트 슬라이싱',
        'question': f"다음 파이썬 코드의 출력 결과를 예측하세요.\n```python\n{code}\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"슬라이싱 [a:b]는 인덱스 a부터 b-1(직전)까지의 요소를 추출합니다.",
        'check': lambda x: _prep(expected) in _prep(x)
    }

def gen_py_dict_get():
    key = random.choice(['age', 'score'])
    default = random.choice([0, -1])
    
    code = f"info = {{'name': 'Alice', 'role': 'Admin'}}\nprint(info.get('{key}', {default}))"
    
    expected = str(default)
    wrongs = ["'Alice'", "KeyError", "None", str(default + 10)]
    wrongs = list(set([w for w in wrongs if w != expected]))
    
    return {
        'topic': 'Python 딕셔너리 (get)',
        'question': f"다음 파이썬 코드의 출력 결과를 예측하세요.\n```python\n{code}\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"딕셔너리의 .get(key, default) 메서드는 키가 존재하지 않을 경우 에러(KeyError)를 발생시키지 않고 default 값({default})을 반환합니다.",
        'check': lambda x: _prep(expected) in _prep(x)
    }


def gen_sns_pairplot():
    hue = random.choice(['species', 'smoker', 'time'])
    ans = f"sns.pairplot(df, hue='{hue}')"
    wrongs = [
        f"sns.scatterplot(df, hue='{hue}')", 
        f"sns.pairplot(df, color='{hue}')", 
        f"plt.pairplot(df, hue='{hue}')"
    ]
    return {
        'topic': 'Seaborn ??? (pairplot)', 
        'question': f"?????? df? ?? ??? ?? ?? ?? ???? ???, '{hue}' ?? ???? ??? ???? ??? ?????.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.pairplot()? ?? ?? ?? ?(pair)? ?? ???? ?? ??? ??? ??(EDA)? ?? ?????.",
        'check': lambda x: "sns.pairplot" in _prep(x) and hue in _prep(x)
    }

def gen_sns_boxplot():
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
        'topic': 'Seaborn ??? (boxplot)', 
        'question': f"??? df?? x?? '{x}', y?? '{y}'? ????, '{hue}' ???? ????(Boxplot)? ??? ??? ?????.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.boxplot()? ???? ??? ???? ??? ???? ???, hue ????? ???? ???? ??? ? ????.",
        'check': lambda x: "boxplot" in _prep(x) and x in _prep(x) and y in _prep(x) and hue in _prep(x)
    }

def gen_np_log1p():
    col = random.choice(['price', 'spc_R', 'population'])
    ans = f"np.log1p(df['{col}'])"
    wrongs = [
        f"np.log(df['{col}'])", 
        f"np.log10(df['{col}'])", 
        f"df['{col}'].log1p()"
    ]
    return {
        'topic': 'Numpy ?? ?? (log1p)', 
        'question': f"?????? df? '{col}' ?? ?? ?? ??? ?? ?? ??? ??? ???. 0 ? ??? ???? ?? 1? ?? ? ??? ??? Numpy ??? ?????.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "np.log1p()? log(1+x)? ????, ?? 0? ? ???(-inf) ??? ???? ?? ???? ??? ?? ?? ?????.",
        'check': lambda x: "log1p" in _prep(x) and col in _prep(x)
    }

def gen_ml_knn():
    ans = "KNeighborsClassifier()"
    wrongs = [
        "KNeighborsRegressor()", 
        "KNNClassifier()", 
        "KNeighborsClassifier.fit()"
    ]
    return {
        'topic': '???? ???? (KNN ???)', 
        'question': f"??? ??? ?? ????? ???? ???? ???? K-??? ??(KNN) ?? ?? ??? ???? ??? ?????.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sklearn.neighbors ??? KNeighborsClassifier()? ??? ??? ??? ? fit()?? ??? ?????.",
        'check': lambda x: "kneighborsclassifier" in _prep(x)
    }

def gen_ml_stratify():
    ans = "stratify=y"
    wrongs = [
        "shuffle=y", 
        "random_state=y", 
        "balance=y"
    ]
    return {
        'topic': '??? ?? ?? ?? (stratify)', 
        'question': f"	rain_test_split(X, y, ...)? ???? ??/??? ???? ?? ?, ?? ?? y? ??? ??(?: 1:1:1)? ??? ???? ????? ?? ????? ?????.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "stratify ????? ?? ??? ????, ??? ??? ?? ???? ?? ??? ?? ??? ??? ???? ?????.",
        'check': lambda x: "stratify=y" in _prep(x)
    }

def _get_factories():
    easy_factories = [
        gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, 
        gen_easy_fillna, gen_easy_drop, gen_easy_filter,
        gen_viz_bar, gen_viz_scatter, gen_viz_hist,
        gen_py_loop_control, gen_py_str_split, gen_py_list_slice, gen_py_dict_get,
        gen_sns_pairplot, gen_sns_boxplot, gen_np_log1p
    ]
    hard_factories = [
        gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt, gen_param_nuance_concat, gen_param_nuance_dropdup,
        gen_numpy_array, gen_ml_split, gen_ml_rf, gen_viz_sns
    ]
    return easy_factories, hard_factories

def generate_exam_quizzes():
    easy_factories, hard_factories = _get_factories()
    
    # 16 Easy (Day1~Day4 level), 4 Hard (Advanced concepts)
    quizzes = [random.choice(easy_factories)() for _ in range(16)] + \
              [random.choice(hard_factories)() for _ in range(4)]
              
    for q in quizzes:
        q['type'] = 'radio'
        choices = [q['expected']] + random.sample(q['wrongs'], 3)
        random.shuffle(choices)
        q['choices'] = choices

    # 2문제를 무작위 주관식(text) 변환
    text_indices = random.sample(range(20), 2)
    for idx in text_indices:
        quizzes[idx]['type'] = 'text'
        
    return quizzes

def generate_single_quiz():
    easy_factories, hard_factories = _get_factories()
    all_factories = easy_factories + hard_factories
    
    q = random.choice(all_factories)()
    
    # 10% 확률로 주관식, 90% 확률로 객관식
    if random.random() < 0.1:
        q['type'] = 'text'
    else:
        q['type'] = 'radio'
        choices = [q['expected']] + random.sample(q['wrongs'], 3)
        random.shuffle(choices)
        q['choices'] = choices
        
    return q
