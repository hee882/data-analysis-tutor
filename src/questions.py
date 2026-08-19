import random

def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    ans = f"df = pd.read_{ext}('data.{ext}')"
    wrongs = [f"df = pd.load_{ext}('data.{ext}')", f"df = pd.open_{ext}('data.{ext}')", f"df = pd.read('data.{ext}')"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '데이터 로드', 'question': f"data.{ext} 파일을 읽어 df에 할당하는 올바른 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "pd.read_csv 또는 pd.read_excel을 사용합니다."}

def gen_easy_head():
    n = random.randint(3, 8)
    ans = f"df.head({n})"
    wrongs = [f"df.top({n})", f"df.show({n})", f"df.first({n})"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '데이터 미리보기', 'question': f"df의 상단 {n}개 행을 확인하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "df.head(n) 메서드를 사용합니다."}

def gen_easy_info():
    ans = "df.info()"
    wrongs = ["df.meta()", "df.desc()", "df.summary()"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '데이터 메타정보', 'question': "df의 행 개수, 컬럼 타입, 결측치를 요약 출력하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "df.info()는 전처리의 기본입니다."}

def gen_easy_isnull():
    ans = "df.isnull().sum()"
    wrongs = ["df.isnull().count()", "df.isna().total()", "df.nulls()"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '결측치 집계', 'question': "df의 각 컬럼별 결측치(NaN) 총합을 구하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "isnull().sum() 체이닝을 활용합니다."}

def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    ans = f"df['{col}'].fillna({val})"
    wrongs = [f"df['{col}'].replace_na({val})", f"df.fillna('{col}', {val})", f"df['{col}'].fill({val})"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '결측치 대체', 'question': f"df['{col}']의 결측치를 {val} 값으로 일괄 변경하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "fillna() 메서드를 사용합니다."}

def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    ans = f"df.drop(columns=['{col}'])"
    wrongs = [f"df.remove('{col}')", f"df.delete('{col}')", f"df.drop('{col}', axis=0)"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '컬럼 제거', 'question': f"df에서 {col} 컬럼을 삭제하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "drop(columns=[...])을 사용합니다."}

def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    ans = f"df[df['{col}'] >= {val}]"
    wrongs = [f"df.filter('{col}' >= {val})", f"df.where('{col}' >= {val})", f"df['{col}'] >= {val}"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '조건부 필터링', 'question': f"df에서 {col} 값이 {val} 이상(>=)인 행만 추출하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "df[조건식] 형태의 불리언 인덱싱을 사용합니다."}

def gen_viz_bar():
    col1 = random.choice(['region', 'category']); col2 = random.choice(['sales', 'count'])
    ans = f"df.plot(kind='bar', x='{col1}', y='{col2}')"
    wrongs = [f"df.bar(x='{col1}', y='{col2}')", f"df.plot.barplot('{col1}', '{col2}')", f"pd.bar(df, '{col1}', '{col2}')"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '막대 그래프', 'question': f"Pandas 내장 함수로 x축 '{col1}', y축 '{col2}'의 막대 그래프를 그리는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': ".plot(kind='bar')를 사용합니다."}

def gen_viz_scatter():
    col1 = random.choice(['age', 'height']); col2 = random.choice(['score', 'salary'])
    ans = f"df.plot(kind='scatter', x='{col1}', y='{col2}')"
    wrongs = [f"df.scatter('{col1}', '{col2}')", f"df.plot.point('{col1}', '{col2}')", f"pd.scatter(df, x='{col1}', y='{col2}')"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '산점도', 'question': f"Pandas 함수로 x축 '{col1}', y축 '{col2}'의 산점도(scatter plot)를 그리는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': ".plot(kind='scatter')를 사용합니다."}

def gen_viz_hist():
    col = random.choice(['score', 'salary']); bins = random.choice([10, 20])
    ans = f"df['{col}'].plot(kind='hist', bins={bins})"
    wrongs = [f"df['{col}'].histogram(bins={bins})", f"df.hist('{col}', split={bins})", f"df['{col}'].plot(kind='bar', bins={bins})"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '히스토그램', 'question': f"df['{col}']의 구간(bins)을 {bins}개로 나눈 히스토그램을 그리는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': ".plot(kind='hist', bins=N)을 사용합니다."}

def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    ans = f"pd.merge(df1, df2, on='user_id', how='{how}')"
    wrongs = [f"df1.join(df2, on='user_id', type='{how}')", f"pd.concat([df1, df2], axis=1, how='{how}')", f"df1.merge(df2, by='user_id', method='{how}')"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '데이터 병합', 'question': f"df1과 df2를 'user_id' 기준으로 {how} Join 하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "pd.merge() 함수를 활용합니다."}

def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    ans = f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')"
    wrongs = [f"df.pivot(group='{idx}', col='month', val='sales', agg='sum')", f"df.groupby(['{idx}', 'month'])['sales'].sum().unstack()", f"df.crosstab(index='{idx}', columns='month', values='sales')"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '피벗 테이블', 'question': f"df에서 행 '{idx}', 열 'month', 값 'sales', 집계 'sum'인 피벗 테이블 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': "df.pivot_table()을 사용합니다."}

def gen_hard_str():
    ans = "df['price'].str.replace('$', '').astype(float)"
    wrongs = ["df['price'].replace('$', '').to_float()", "df['price'].remove('$').astype('float')", "df['price'].str.strip('$').float()"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '문자열 파싱', 'question': "df['price'] 컬럼 내의 달러 기호('$')를 제거하고 float으로 변환하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': ".str.replace() 후 .astype(float)을 체이닝합니다."}

def gen_hard_dt():
    ans = "df['date'].dt.month"
    wrongs = ["df['date'].month", "pd.to_datetime(df['date']).get_month()", "df['date'].time.month"]
    choices = [ans] + wrongs
    random.shuffle(choices)
    return {'topic': '시계열 처리', 'question': "df['date'] 컬럼(datetime 형)에서 '월(month)' 데이터만 추출하는 코드를 고르세요.", 'expected': ans, 'choices': choices, 'explanation': ".dt 접근자를 사용합니다."}

def generate_exam_cycle():
    easy_factories = [gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, gen_easy_fillna, gen_easy_drop, gen_easy_filter]
    viz_factories = [gen_viz_bar, gen_viz_scatter, gen_viz_hist]
    hard_factories = [gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt]
    
    return [random.choice(easy_factories)() for _ in range(14)] + \
           [random.choice(viz_factories)() for _ in range(3)] + \
           [random.choice(hard_factories)() for _ in range(3)]
