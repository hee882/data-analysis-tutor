import random

def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    return {'topic': '데이터 로드', 'type': 'code', 'question': f"data.{ext} 파일을 읽어 df에 할당하세요.", 'check': lambda x: f"read_{ext}" in x and "data" in x and "df" in x, 'expected': f"df = pd.read_{ext}('data.{ext}')", 'explanation': "pd.read_csv 또는 pd.read_excel을 사용합니다."}
def gen_easy_head():
    n = random.randint(3, 8)
    return {'topic': '데이터 미리보기', 'type': 'code', 'question': f"df의 상단 {n}개 행을 확인하세요.", 'check': lambda x: "head" in x and str(n) in x, 'expected': f"df.head({n})", 'explanation': "df.head(n) 메서드를 사용합니다."}
def gen_easy_info():
    return {'topic': '데이터 메타정보', 'type': 'code', 'question': "df의 행 개수, 컬럼 타입, 결측치를 요약 출력하세요.", 'check': lambda x: "info" in x, 'expected': "df.info()", 'explanation': "df.info()는 전처리의 기본입니다."}
def gen_easy_isnull():
    return {'topic': '결측치 집계', 'type': 'code', 'question': "df의 각 컬럼별 결측치(NaN) 총합을 구하세요.", 'check': lambda x: ("isnull" in x or "isna" in x) and "sum" in x, 'expected': "df.isnull().sum()", 'explanation': "isnull().sum() 체이닝을 활용합니다."}
def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    return {'topic': '결측치 단일값 대체', 'type': 'code', 'question': f"df['{col}']의 결측치를 {val} 값으로 일괄 변경하세요.", 'check': lambda x: "fillna" in x and str(val) in x and col in x, 'expected': f"df['{col}'].fillna({val})", 'explanation': "fillna() 메서드를 사용합니다."}
def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    return {'topic': '컬럼 제거', 'type': 'code', 'question': f"df에서 {col} 컬럼을 삭제하세요.", 'check': lambda x: "drop" in x and col in x and "columns" in x, 'expected': f"df.drop(columns=['{col}'])", 'explanation': "drop(columns=[...])을 사용합니다."}
def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    return {'topic': '불리언 인덱싱', 'type': 'code', 'question': f"df에서 {col} 값이 {val} 이상(>=)인 행만 추출하세요.", 'check': lambda x: col in x and str(val) in x and ">=" in x, 'expected': f"df[df['{col}'] >= {val}]", 'explanation': "df[df['col'] >= val] 형태를 사용합니다."}
def gen_viz_bar():
    col1 = random.choice(['region', 'category']); col2 = random.choice(['sales', 'count'])
    return {'topic': '막대 그래프', 'type': 'code', 'question': f"Pandas 기본 내장 함수로 x축 '{col1}', y축 '{col2}'의 막대 그래프(bar plot)를 그리세요.", 'check': lambda x: "plot" in x and "bar" in x and col1 in x and col2 in x, 'expected': f"df.plot(kind='bar', x='{col1}', y='{col2}')", 'explanation': ".plot(kind='bar')를 사용합니다."}
def gen_viz_scatter():
    col1 = random.choice(['age', 'height']); col2 = random.choice(['score', 'salary'])
    return {'topic': '산점도', 'type': 'code', 'question': f"Pandas 기본 함수로 x축 '{col1}', y축 '{col2}'의 산점도(scatter plot)를 그리세요.", 'check': lambda x: "plot" in x and "scatter" in x and col1 in x and col2 in x, 'expected': f"df.plot(kind='scatter', x='{col1}', y='{col2}')", 'explanation': ".plot(kind='scatter')를 사용합니다."}
def gen_viz_hist():
    col = random.choice(['score', 'salary']); bins = random.choice([10, 20])
    return {'topic': '히스토그램', 'type': 'code', 'question': f"df['{col}']의 구간(bins)을 {bins}개로 나눈 히스토그램을 그리세요.", 'check': lambda x: "hist" in x and str(bins) in x and col in x.replace('"',"'"), 'expected': f"df['{col}'].plot(kind='hist', bins={bins})", 'explanation': ".plot(kind='hist', bins=N)을 사용합니다."}
def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    return {'topic': '데이터 병합', 'type': 'code', 'question': f"df1과 df2를 'user_id' 컬럼을 기준으로 {how} Join 하세요.", 'check': lambda x: "merge" in x and "user_id" in x and how in x, 'expected': f"pd.merge(df1, df2, on='user_id', how='{how}')", 'explanation': "pd.merge() 함수를 활용합니다."}
def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    return {'topic': '피벗 테이블', 'type': 'code', 'question': f"df에서 행(index) '{idx}', 열(columns) 'month', 값 'sales', 집계 'sum'인 피벗 테이블 코드를 작성하세요.", 'check': lambda x: "pivot_table" in x and idx in x and "month" in x and "sales" in x and "sum" in x, 'expected': f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')", 'explanation': "df.pivot_table()을 사용합니다."}
def gen_hard_str():
    return {'topic': '문자열 파싱', 'type': 'code', 'question': "df['price'] 컬럼 내의 달러 기호('$')를 제거하고 float으로 변환하세요.", 'check': lambda x: "str.replace" in x and "$" in x and "astype" in x and "float" in x, 'expected': "df['price'].str.replace('$', '').astype(float)", 'explanation': ".str.replace() 후 .astype()을 체이닝합니다."}
def gen_hard_dt():
    return {'topic': '시계열 처리', 'type': 'code', 'question': "df['date'] 컬럼(datetime 자료형)에서 '월(month)' 데이터만 추출하세요.", 'check': lambda x: ".dt.month" in x.replace(" ", ""), 'expected': "df['date'].dt.month", 'explanation': ".dt 접근자를 사용합니다."}

def generate_exam_cycle():
    easy_factories = [gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, gen_easy_fillna, gen_easy_drop, gen_easy_filter]
    viz_factories = [gen_viz_bar, gen_viz_scatter, gen_viz_hist]
    hard_factories = [gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt]
    
    return [random.choice(easy_factories)() for _ in range(14)] + \
           [random.choice(viz_factories)() for _ in range(3)] + \
           [random.choice(hard_factories)() for _ in range(3)]
