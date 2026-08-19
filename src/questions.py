import random

def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    ans = f"df = pd.read_{ext}('data.{ext}')"
    wrongs = [f"df = pd.read(file='data.{ext}', format='{ext}')", f"df = pd.load_{ext}('data.{ext}')", f"df.read_{ext}('data.{ext}')", f"pd.DataFrame('data.{ext}', type='{ext}')"]
    return {
        'topic': '데이터 로드', 'question': f"`data.{ext}` 파일을 읽어 `df`에 할당하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "pd.read_csv 또는 pd.read_excel을 사용합니다.",
        'check': lambda x: f"read_{ext}" in x and "data" in x and "df" in x
    }

def gen_easy_head():
    n = random.randint(3, 8)
    ans = f"df.head({n})"
    wrongs = [f"df.head(rows={n})", f"df.show({n})", f"df.top({n})", f"df.iloc[:{n}, :].head()"]
    return {
        'topic': '데이터 미리보기', 'question': f"`df`의 상단 {n}개 행을 확인하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.head(n) 메서드를 사용합니다.",
        'check': lambda x: "head" in x and str(n) in x
    }

def gen_easy_info():
    ans = "df.info()"
    wrongs = ["df.summary(nulls=True)", "df.describe(types=True)", "pd.info(df)", "df.dtypes().sum()"]
    return {
        'topic': '데이터 메타정보', 'question': "`df`의 행 개수, 컬럼 타입, 결측치를 요약 출력하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.info()는 데이터 전처리의 기본입니다.",
        'check': lambda x: "info" in x
    }

def gen_easy_isnull():
    ans = "df.isnull().sum()"
    wrongs = ["df.isnull().count()", "df.isna().total()", "df.count(nulls=True)", "pd.isnull(df).sum(axis=1)"]
    return {
        'topic': '결측치 집계', 'question': "`df`의 각 컬럼별 결측치(NaN) 총합을 구하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "isnull().sum() 또는 isna().sum()을 사용합니다.",
        'check': lambda x: ("isnull" in x or "isna" in x) and "sum" in x
    }

def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    ans = f"df['{col}'].fillna({val})"
    wrongs = [f"df['{col}'].fillna(value={val}, inplace=False)", f"df.fillna(col='{col}', val={val})", f"df['{col}'].replace(NaN, {val})", f"df['{col}'].dropna().add({val})"]
    return {
        'topic': '결측치 대체', 'question': f"`df['{col}']`의 결측치를 {val} 값으로 일괄 대체하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "fillna() 메서드를 사용합니다.",
        'check': lambda x: "fillna" in x and str(val) in x and col in x
    }

def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    ans = f"df.drop(columns=['{col}'])"
    wrongs = [f"df.drop('{col}', axis=0)", f"df.delete(columns='{col}')", f"df.remove('{col}')", f"del df.columns['{col}']"]
    return {
        'topic': '컬럼 제거', 'question': f"`df`에서 `{col}` 컬럼을 삭제하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "drop(columns=[...]) 또는 drop(..., axis=1)을 사용합니다.",
        'check': lambda x: "drop" in x and col in x and ("columns" in x or "axis=1" in x.replace(" ", ""))
    }

def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    ans = f"df[df['{col}'] >= {val}]"
    wrongs = [f"df.filter(df['{col}'] >= {val})", f"df.where('{col}' >= {val})", f"df.loc['{col}' >= {val}]", f"df[df.{col} => {val}]"]
    return {
        'topic': '조건부 필터링', 'question': f"`df`에서 `{col}` 값이 {val} 이상(>=)인 행만 추출하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "불리언 인덱싱 df[df['col'] >= val] 형태를 사용합니다.",
        'check': lambda x: col in x and str(val) in x and ">=" in x
    }

def gen_viz_bar():
    col1 = random.choice(['region', 'category']); col2 = random.choice(['sales', 'count'])
    ans = f"df.plot(kind='bar', x='{col1}', y='{col2}')"
    wrongs = [f"df.plot.bar(y='{col1}', x='{col2}')", f"df.plot(type='bar', x='{col1}', y='{col2}')", f"pd.barplot(df, x='{col1}', y='{col2}')", f"df.groupby('{col1}').plot('{col2}', kind='bar')"]
    return {
        'topic': '막대 그래프', 'question': f"Pandas 내장 함수로 x축 '{col1}', y축 '{col2}'의 막대 그래프를 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='bar') 또는 .plot.bar()를 사용합니다.",
        'check': lambda x: "plot" in x and "bar" in x and col1 in x and col2 in x
    }

def gen_viz_scatter():
    col1 = random.choice(['age', 'height']); col2 = random.choice(['score', 'salary'])
    ans = f"df.plot(kind='scatter', x='{col1}', y='{col2}')"
    wrongs = [f"df.plot.scatter(axis_x='{col1}', axis_y='{col2}')", f"df.scatter(x='{col1}', y='{col2}')", f"pd.plot(df, kind='scatter', x='{col1}', y='{col2}')", f"df.plot(x='{col1}', y='{col2}', mode='scatter')"]
    return {
        'topic': '산점도', 'question': f"Pandas 함수로 x축 '{col1}', y축 '{col2}'의 산점도(scatter plot)를 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='scatter')를 사용합니다.",
        'check': lambda x: "plot" in x and "scatter" in x and col1 in x and col2 in x
    }

def gen_viz_hist():
    col = random.choice(['score', 'salary']); bins = random.choice([10, 20])
    ans = f"df['{col}'].plot(kind='hist', bins={bins})"
    wrongs = [f"df['{col}'].plot(kind='hist', split={bins})", f"df.hist(column='{col}', chunks={bins})", f"df['{col}'].plot.histogram({bins})", f"pd.hist(df['{col}'], bins={bins})"]
    return {
        'topic': '히스토그램', 'question': f"`df['{col}']`의 구간(bins)을 {bins}개로 나눈 히스토그램을 그리세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".plot(kind='hist', bins=N)을 사용합니다.",
        'check': lambda x: "hist" in x and str(bins) in x and col in x.replace('"',"'")
    }

def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    ans = f"pd.merge(df1, df2, on='user_id', how='{how}')"
    wrongs = [f"df1.join(df2, on='user_id', type='{how}')", f"pd.concat([df1, df2], axis=1, join='{how}')", f"df1.merge(df2, by='user_id', how='{how}')", f"pd.merge(df1, df2, index='user_id', method='{how}')"]
    return {
        'topic': '데이터 병합', 'question': f"`df1`과 `df2`를 'user_id' 기준으로 `{how}` Join 하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "pd.merge() 함수를 활용합니다.",
        'check': lambda x: "merge" in x and "user_id" in x and how in x
    }

def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    ans = f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')"
    wrongs = [f"df.pivot(group='{idx}', col='month', val='sales', agg='sum')", f"df.groupby(['{idx}', 'month'])['sales'].sum().unstack()", f"df.pivot_table(rows='{idx}', cols='month', data='sales', agg='sum')", f"pd.crosstab(index=df['{idx}'], columns=df['month'], values='sales', aggfunc='sum')"]
    return {
        'topic': '피벗 테이블', 'question': f"`df`에서 행 '{idx}', 열 'month', 값 'sales', 집계 'sum'인 피벗 테이블 코드를 작성하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': "df.pivot_table()을 사용합니다.",
        'check': lambda x: "pivot_table" in x and idx in x and "month" in x and "sales" in x and "sum" in x
    }

def gen_hard_str():
    ans = "df['price'].str.replace('$', '').astype(float)"
    wrongs = ["df['price'].replace('$', '').to_float()", "df['price'].str.remove('$').astype(float)", "df['price'].apply(lambda x: float(x.replace('$', '')))", "df['price'].str.strip('$').astype('float64')"]
    return {
        'topic': '문자열 파싱', 'question': "`df['price']` 컬럼 내의 달러 기호('$')를 제거하고 float으로 변환하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".str.replace() 후 .astype(float)을 체이닝합니다.",
        'check': lambda x: "replace" in x and "$" in x and ("astype" in x or "float" in x)
    }

def gen_hard_dt():
    ans = "df['date'].dt.month"
    wrongs = ["df['date'].month", "pd.to_datetime(df['date']).get_month()", "df['date'].time.month", "df['date'].dt.get('month')"]
    return {
        'topic': '시계열 처리', 'question': "`df['date']` 컬럼(datetime 형)에서 '월(month)' 데이터만 추출하세요.", 
        'expected': ans, 'wrongs': wrongs, 'explanation': ".dt 접근자를 사용합니다.",
        'check': lambda x: ".dt.month" in x.replace(" ", "")
    }

def gen_numpy_array():
    shape = random.choice([(3,3), (2,4), (4,4)])
    ans = f"np.zeros({shape})"
    wrongs = [f"np.empty({shape[0]}, {shape[1]})", f"np.array(0, shape={shape})", f"pd.zeros({shape})", f"np.matrix(zeros=True, size={shape})"]
    return {
        'topic': 'Numpy 배열 생성', 'question': f"모든 원소가 0으로 채워진 크기가 `{shape}`인 Numpy 배열을 생성하세요.",
        'expected': ans, 'wrongs': wrongs, 'explanation': "np.zeros((행, 열)) 함수를 사용합니다.",
        'check': lambda x: "zeros" in x and str(shape[0]) in x and str(shape[1]) in x
    }

def gen_ml_split():
    size = random.choice([0.2, 0.25, 0.3])
    ans = f"train_test_split(X, y, test_size={size}, random_state=42)"
    wrongs = [f"split_data(X, y, ratio={1-size})", f"train_test_split(y, X, train_size={size})", f"model_selection.split(X, y, test={size})", f"train_test_split(X, y, test_ratio={size})"]
    return {
        'topic': '머신러닝 데이터 분할', 'question': f"Scikit-learn을 사용하여 특성 데이터 `X`와 타겟 `y`를 테스트 세트 비율 `{size}`로 분할하세요. (random_state=42)",
        'expected': ans, 'wrongs': wrongs, 'explanation': "sklearn.model_selection.train_test_split()을 사용합니다.",
        'check': lambda x: "train_test_split" in x and str(size) in x and "42" in x
    }

def gen_ml_rf():
    estimators = random.choice([100, 200, 500])
    ans = f"RandomForestClassifier(n_estimators={estimators}, random_state=42)"
    wrongs = [f"RandomForest(trees={estimators})", f"RandomForestClassifier(max_trees={estimators})", f"EnsembleRF(n={estimators})", f"RandomForestClassifier(count={estimators})"]
    return {
        'topic': '머신러닝 모델 객체 생성', 'question': f"Scikit-learn을 사용하여 트리의 개수가 `{estimators}`개인 랜덤 포레스트 분류기 객체를 생성하세요. (random_state=42)",
        'expected': ans, 'wrongs': wrongs, 'explanation': "RandomForestClassifier(n_estimators=...)을 사용합니다.",
        'check': lambda x: "RandomForestClassifier" in x and str(estimators) in x
    }

def gen_viz_sns():
    x_col = random.choice(['total_bill', 'age'])
    y_col = random.choice(['tip', 'salary'])
    ans = f"sns.scatterplot(data=df, x='{x_col}', y='{y_col}')"
    wrongs = [f"sns.scatter(x='{x_col}', y='{y_col}', df=data)", f"df.sns.plot('{x_col}', '{y_col}')", f"sns.plot(kind='scatter', x='{x_col}', y='{y_col}')", f"sns.scatterplot('{x_col}', '{y_col}')"]
    return {
        'topic': 'Seaborn 시각화', 'question': f"Seaborn 라이브러리를 사용하여 `df`의 x축 '{x_col}', y축 '{y_col}' 산점도를 그리세요.",
        'expected': ans, 'wrongs': wrongs, 'explanation': "sns.scatterplot(data=..., x=..., y=...)을 사용합니다.",
        'check': lambda x: "sns.scatterplot" in x and x_col in x and y_col in x
    }

def _get_factories():
    easy_factories = [
        gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, 
        gen_easy_fillna, gen_easy_drop, gen_easy_filter,
        gen_viz_bar, gen_viz_scatter, gen_viz_hist
    ]
    hard_factories = [
        gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt,
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
