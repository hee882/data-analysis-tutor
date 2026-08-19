import random
import re

def _prep(text):
    if not text: return ""
    text = text.replace("'", '"')
    text = re.sub(r'\s+', '', text)
    return text.lower()

def gen_easy_read():
    ans = "pd.read_csv('data.csv')"
    wrongs = ["pd.read_excel('data.csv')", "pd.open_csv('data.csv')", "pd.load_csv('data.csv')"]
    return {
        'topic': '데이터 불러오기', 
        'question': "Pandas를 사용하여 'data.csv' 파일을 읽어오는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.read_csv() 함수를 사용하여 CSV 형식의 파일을 DataFrame으로 불러옵니다.",
        'check': lambda x: "read_csv" in _prep(x) and "data.csv" in _prep(x)
    }

def gen_easy_head():
    n = random.randint(3, 8)
    ans = f"df.head({n})"
    wrongs = [f"df.head(rows={n})", f"df.show({n})", f"df.top({n})", f"df.iloc[:{n}, :].head()"]
    return {
        'topic': '데이터 탐색 (앞부분)', 
        'question': f"데이터프레임 `df`의 처음 {n}개 행을 출력하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"df.head({n})을 사용하면 맨 위에서부터 지정한 개수만큼의 데이터를 확인할 수 있습니다.",
        'check': lambda x: "head" in _prep(x) and str(n) in _prep(x)
    }

def gen_easy_info():
    ans = "df.info()"
    wrongs = ["df.dtypes", "df.describe()", "pd.info(df)"]
    return {
        'topic': '데이터 요약 정보', 
        'question': "데이터프레임 `df`의 컬럼명, 데이터 타입, 결측치 수 등의 요약 정보를 한눈에 확인하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.info()는 DataFrame의 전반적인 구조와 결측치 현황을 파악하는 가장 기본적인 함수입니다.",
        'check': lambda x: "df.info" in _prep(x)
    }

def gen_easy_isnull():
    ans = "df.isnull().sum()"
    wrongs = ["df.isna().count()", "df.nulls()", "df.count_na()"]
    return {
        'topic': '결측치 개수 확인', 
        'question': "데이터프레임 `df`의 각 컬럼별 결측치(NaN) 총 개수를 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.isnull().sum() (또는 df.isna().sum())을 통해 열별 결측치 개수를 집계합니다.",
        'check': lambda x: ("isnull" in _prep(x) or "isna" in _prep(x)) and "sum" in _prep(x)
    }

def gen_easy_fillna():
    ans = "df.fillna(0)"
    wrongs = ["df.replace_na(0)", "df.na_fill(0)", "pd.fillna(df, 0)"]
    return {
        'topic': '결측치 대체', 
        'question': "데이터프레임 `df`의 모든 결측치를 0으로 채우는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.fillna() 함수를 사용하여 NaN 값을 원하는 값(여기서는 0)으로 바꿀 수 있습니다.",
        'check': lambda x: "fillna" in _prep(x) and "0" in _prep(x)
    }

def gen_easy_drop():
    ans = "df.drop(columns=['age'])"
    wrongs = ["df.drop('age')", "df.remove_column('age')", "df.delete('age')"]
    return {
        'topic': '컬럼 삭제', 
        'question': "데이터프레임 `df`에서 'age' 컬럼을 삭제하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "df.drop(columns=['col']) 또는 df.drop('col', axis=1)을 사용하여 컬럼을 삭제합니다.",
        'check': lambda x: "drop" in _prep(x) and "age" in _prep(x)
    }

def gen_easy_filter():
    ans = "df[df['age'] >= 20]"
    wrongs = ["df.filter(age >= 20)", "df.where(age >= 20)", "df[age >= 20]"]
    return {
        'topic': '조건부 필터링', 
        'question': "데이터프레임 `df`에서 'age'가 20 이상인 행만 필터링하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Boolean Indexing인 df[조건]을 활용하여 특정 조건에 맞는 행만 추출할 수 있습니다.",
        'check': lambda x: "df" in _prep(x) and ">=" in _prep(x) and "20" in _prep(x) and "age" in _prep(x)
    }

def gen_viz_bar():
    ans = "df['category'].value_counts().plot(kind='bar')"
    wrongs = ["plt.bar(df['category'])", "df['category'].barplot()", "df.plot(kind='bar', x='category')"]
    return {
        'topic': '시각화 (Bar chart)', 
        'question': "데이터프레임 `df`의 'category' 컬럼의 항목별 빈도수를 막대 그래프(Bar chart)로 시각화하는 Pandas 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "value_counts()로 빈도수를 계산한 후 .plot(kind='bar')를 이어서 호출하면 손쉽게 막대 그래프가 생성됩니다.",
        'check': lambda x: "value_counts" in _prep(x) and "plot" in _prep(x) and "bar" in _prep(x)
    }

def gen_viz_scatter():
    ans = "df.plot(kind='scatter', x='age', y='income')"
    wrongs = ["df.scatter(x='age', y='income')", "plt.scatter(df)", "df.plot_scatter('age', 'income')"]
    return {
        'topic': '시각화 (Scatter plot)', 
        'question': "데이터프레임 `df`에서 x축을 'age', y축을 'income'으로 하는 산점도(Scatter plot)를 그리는 Pandas 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "DataFrame의 내장 plot 메서드에서 kind='scatter' 옵션을 주어 산점도를 그릴 수 있습니다.",
        'check': lambda x: "plot" in _prep(x) and "scatter" in _prep(x) and "age" in _prep(x) and "income" in _prep(x)
    }

def gen_viz_hist():
    ans = "df['score'].plot(kind='hist')"
    wrongs = ["df['score'].histogram()", "plt.histogram(df['score'])", "df.plot_hist('score')"]
    return {
        'topic': '시각화 (Histogram)', 
        'question': "데이터프레임 `df`의 'score' 컬럼의 분포를 히스토그램(Histogram)으로 그리는 Pandas 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "단일 컬럼(Series)에 대해 .plot(kind='hist') 또는 .hist()를 호출하여 분포를 확인합니다.",
        'check': lambda x: "plot" in _prep(x) and "hist" in _prep(x) and "score" in _prep(x)
    }

def gen_hard_merge():
    ans = "pd.merge(df1, df2, on='id', how='left')"
    wrongs = ["df1.join(df2, on='id', type='left')", "pd.concat([df1, df2], axis=1)", "df1.merge_left(df2, 'id')"]
    return {
        'topic': '데이터 병합 (Left Merge)', 
        'question': "데이터프레임 `df1`과 `df2`를 'id' 컬럼 기준으로 Left Merge(왼쪽 기준 병합) 하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.merge() 함수에서 how='left' 파라미터를 사용하면 왼쪽 데이터프레임을 기준으로 병합을 수행합니다.",
        'check': lambda x: "merge" in _prep(x) and "left" in _prep(x) and "id" in _prep(x)
    }

def gen_hard_pivot():
    ans = "df.pivot_table(index='region', values='sales', aggfunc='mean')"
    wrongs = ["df.groupby('region')['sales'].pivot('mean')", "pd.pivot(df, 'region', 'sales', 'mean')", "df.pivot_table(group='region', target='sales', func='mean')"]
    return {
        'topic': '피벗 테이블 (Pivot Table)', 
        'question': "데이터프레임 `df`에서 'region'을 인덱스로 하고 'sales'의 평균(mean)을 구하는 피벗 테이블 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pivot_table()을 사용하면 엑셀의 피벗 테이블처럼 인덱스, 컬럼, 값(통계량)을 구조화하여 요약할 수 있습니다.",
        'check': lambda x: "pivot_table" in _prep(x) and "region" in _prep(x) and "sales" in _prep(x) and "mean" in _prep(x)
    }

def gen_hard_str():
    ans = "df['email'].str.split('@').str[1]"
    wrongs = ["df['email'].split('@')[1]", "df['email'].extract('@(.*)')", "df['email'].str.split('@')[1]"]
    return {
        'topic': '문자열 처리 (str.split)', 
        'question': "데이터프레임 `df`의 'email' 컬럼에서 '@'를 기준으로 문자열을 분리한 뒤, 도메인 부분(두 번째 요소)만 추출하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Pandas에서 Series의 문자열 메서드를 연쇄적으로 사용할 때는 매번 .str 속성을 명시해야 합니다. (예: .str.split().str[1])",
        'check': lambda x: "str.split" in _prep(x) and "str[" in _prep(x)
    }

def gen_hard_dt():
    ans = "df['date'].dt.month"
    wrongs = ["df['date'].month", "pd.to_datetime(df['date']).month", "df['date'].get_month()"]
    return {
        'topic': '날짜/시간 처리 (dt 접근자)', 
        'question': "datetime 타입인 데이터프레임 `df`의 'date' 컬럼에서 '월(month)' 정보만 추출하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "날짜 데이터(Series)에서 특정 요소(년, 월, 일 등)를 뽑아낼 때는 .dt 접근자를 사용해야 합니다.",
        'check': lambda x: "dt.month" in _prep(x)
    }

def gen_numpy_array():
    ans = "np.array([1, 2, 3])"
    wrongs = ["np.list([1, 2, 3])", "pd.array([1, 2, 3])", "np.create([1, 2, 3])"]
    return {
        'topic': 'Numpy 배열 생성', 
        'question': "[1, 2, 3] 리스트를 Numpy 배열(ndarray)로 변환하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Numpy의 핵심 자료구조인 ndarray는 np.array() 함수를 통해 리스트 등으로부터 생성합니다.",
        'check': lambda x: "np.array" in _prep(x) and "1" in _prep(x) and "2" in _prep(x) and "3" in _prep(x)
    }

def gen_ml_split():
    ans = "train_test_split(X, y, test_size=0.2)"
    wrongs = ["split_data(X, y, 0.2)", "model_selection.split(X, y, test_size=0.2)", "pd.train_test_split(X, y, 0.2)"]
    return {
        'topic': '데이터 분할 (train_test_split)', 
        'question': "특성 데이터 `X`와 정답 데이터 `y`를 훈련셋 80%, 테스트셋 20%로 분할하는 scikit-learn 코드를 작성하세요. (단축 임포트 가정)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sklearn.model_selection 모듈의 train_test_split 함수를 사용하여 데이터를 나눕니다.",
        'check': lambda x: "train_test_split" in _prep(x) and "0.2" in _prep(x)
    }

def gen_ml_rf():
    ans = "RandomForestClassifier()"
    wrongs = ["RandomForest()", "RFClassifier()", "sklearn.ensemble.RandomForest()"]
    return {
        'topic': '머신러닝 모델 생성 (RandomForest)', 
        'question': "scikit-learn을 사용하여 랜덤 포레스트 분류기(RandomForest Classifier) 객체를 생성하는 코드를 작성하세요. (단축 임포트 가정)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sklearn.ensemble 모듈에서 제공하는 RandomForestClassifier() 클래스를 초기화합니다.",
        'check': lambda x: "randomforestclassifier" in _prep(x)
    }

def gen_viz_sns():
    ans = "sns.scatterplot(data=df, x='age', y='income', hue='gender')"
    wrongs = ["sns.plot(df, 'age', 'income', color='gender')", "plt.scatter(df['age'], df['income'], group=df['gender'])", "sns.scatter('age', 'income', df, 'gender')"]
    return {
        'topic': 'Seaborn 시각화 (Hue 적용)', 
        'question': "Seaborn을 사용하여 데이터 `df`의 x축 'age', y축 'income' 산점도를 그리고, 'gender'별로 색상을 다르게 표현하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Seaborn에서는 hue 파라미터를 사용하여 특정 범주형 변수를 기준으로 색상을 손쉽게 구분할 수 있습니다.",
        'check': lambda x: "sns.scatterplot" in _prep(x) and "hue" in _prep(x) and "gender" in _prep(x)
    }

def gen_param_nuance_concat():
    ans = "pd.concat([df1, df2], axis=1)"
    wrongs = ["pd.concat([df1, df2], axis=0)", "pd.merge([df1, df2], axis=1)", "df1.concat(df2, axis='col')"]
    return {
        'topic': '매개변수 뉘앙스 (concat axis)', 
        'question': "`pd.concat([df1, df2])`는 기본적으로 위아래(행 방향)로 병합됩니다. 좌우(열 방향)로 나란히 이어 붙이려면 어떤 파라미터를 추가해야 하나요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Pandas에서 대부분의 연산은 axis=0(행)이 기본값이며, 열 기준으로 방향을 틀려면 axis=1을 명시해야 합니다.",
        'check': lambda x: "axis=1" in _prep(x)
    }

def gen_param_nuance_dropdup():
    ans = "df.drop_duplicates(keep='last')"
    wrongs = ["df.drop_duplicates(keep='first')", "df.drop_duplicates(keep=False)", "df.remove_duplicates(last=True)"]
    return {
        'topic': '매개변수 뉘앙스 (drop_duplicates keep)', 
        'question': "데이터프레임 `df`에서 중복된 행을 제거할 때, 가장 마지막에 등장한(최신) 데이터만 남기고 싶습니다. 어떤 코드를 작성해야 하나요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "drop_duplicates()의 기본값은 keep='first'(첫 번째 남김)이며, keep='last'를 쓰면 마지막 행을 보존합니다.",
        'check': lambda x: "keep" in _prep(x) and "last" in _prep(x)
    }


def gen_py_for_loop():
    ans = "for i in range(5):"
    wrongs = ["for i in 5:", "for i=0 to 5:", "loop i in range(5):"]
    return {
        'topic': 'Python 기초 (반복문)', 
        'question': "0부터 4까지 총 5번 반복하는 기본적인 파이썬 `for` 반복문의 첫 줄을 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "파이썬에서 지정된 횟수만큼 반복할 때는 `range()` 함수를 사용합니다. `range(5)`는 0부터 4까지의 숫자를 생성합니다.",
        'check': lambda x: "for" in _prep(x) and "range(5)" in _prep(x)
    }

def gen_py_function():
    ans = "def my_func(a, b):"
    wrongs = ["function my_func(a, b):", "def my_func(a, b)", "func my_func(a, b):"]
    return {
        'topic': 'Python 기초 (함수 정의)', 
        'question': "두 개의 인자(a, b)를 받는 파이썬 함수 `my_func`를 정의하는 첫 줄 코드를 작성하세요. (콜론 포함)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "파이썬에서 함수를 정의할 때는 `def` 키워드를 사용하며, 선언문 끝에 반드시 콜론(`:`)을 붙여야 합니다.",
        'check': lambda x: "def" in _prep(x) and "my_func" in _prep(x) and ":" in _prep(x)
    }

def gen_py_basic_type():
    ans = "type(data)"
    wrongs = ["typeof(data)", "class(data)", "dtype(data)"]
    return {
        'topic': 'Python 기초 (자료형 확인)', 
        'question': "변수 `data`의 파이썬 내장 자료형(Type)이 무엇인지 확인하는 내장 함수를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "파이썬의 기본 내장 함수인 `type()`을 사용하여 객체의 자료형(예: int, str, list 등)을 확인할 수 있습니다. Pandas의 `dtype`과는 다릅니다.",
        'check': lambda x: "type(" in _prep(x) and "data" in _prep(x)
    }

def gen_py_loop_control():
    ans = "break"
    wrongs = ["continue", "pass", "stop"]
    return {
        'topic': '파이썬 기초 (반복문 제어)', 
        'question': "`for` 또는 `while` 반복문을 실행하던 도중, 특정 조건을 만족했을 때 즉시 반복문을 완전히 탈출(종료)하게 만드는 키워드는 무엇인가요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "break는 반복문을 즉시 탈출하며, continue는 이번 차례의 나머지 코드를 건너뛰고 다음 반복으로 넘어갑니다.",
        'check': lambda x: "break" == _prep(x)
    }

def gen_py_str_split():
    ans = "text.split(',')"
    wrongs = ["text.split(',')", "text.slice(',')", "text.divide(',')"]
    return {
        'topic': '파이썬 기초 (문자열 분리)', 
        'question': "문자열 `text = '사과,바나나,포도'`가 주어졌을 때, 쉼표(',')를 기준으로 문자를 분리하여 리스트로 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "문자열의 .split('구분자') 메서드를 사용하면 특정 문자를 기준으로 잘라낸 리스트를 얻을 수 있습니다.",
        'check': lambda x: "split" in _prep(x) and "," in _prep(x)
    }

def gen_py_list_slice():
    ans = "lst[::-1]"
    wrongs = ["lst[-1:]", "lst.reverse()", "reversed(lst)"]
    return {
        'topic': '파이썬 기초 (리스트 슬라이싱)', 
        'question': "리스트 `lst`의 요소 순서를 완전히 거꾸로 뒤집은 새로운 리스트를 슬라이싱(slicing) 기법만 사용하여 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "[start:stop:step] 구조에서 step을 -1로 지정( [::-1] )하면 역순 슬라이싱이 됩니다.",
        'check': lambda x: "[::-1]" in _prep(x)
    }

def gen_py_dict_get():
    ans = "my_dict.get('age', 0)"
    wrongs = ["my_dict['age'] or 0", "my_dict.find('age', 0)", "my_dict.fetch('age', 0)"]
    return {
        'topic': '파이썬 기초 (딕셔너리 안전 탐색)', 
        'question': "딕셔너리 `my_dict`에서 'age' 키의 값을 가져오되, 만약 해당 키가 존재하지 않으면 에러 대신 0을 반환하도록 하는 메서드 기반의 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "dict.get(key, default) 메서드를 사용하면 키 오류(KeyError) 없이 안전하게 값을 꺼내거나 기본값을 설정할 수 있습니다.",
        'check': lambda x: "get" in _prep(x) and "age" in _prep(x) and "0" in _prep(x)
    }

def gen_sns_pairplot():
    import random
    hue = random.choice(['species', 'smoker', 'time'])
    ans = f"sns.pairplot(df, hue='{hue}')"
    wrongs = [
        f"sns.scatterplot(df, hue='{hue}')", 
        f"sns.pairplot(df, color='{hue}')", 
        f"plt.pairplot(df, hue='{hue}')"
    ]
    return {
        'topic': 'Seaborn 시각화 (pairplot)', 
        'question': f"데이터프레임 `df`의 모든 숫자형 변수 쌍에 대해 산점도를 그리고, '{hue}' 열을 기준으로 색상을 구분하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.pairplot()은 변수 간의 모든 쌍(pair)에 대해 산점도를 그려 탐색적 데이터 분석(EDA)에 매우 유용합니다.",
        'check': lambda x: "sns.pairplot" in _prep(x) and hue in _prep(x)
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
        'topic': 'Seaborn 시각화 (boxplot)', 
        'question': f"데이터 `df`에서 x축을 '{x}', y축을 '{y}'로 설정하고, '{hue}' 기준으로 박스플롯(Boxplot)을 그리는 코드를 작성하세요.",
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
        'topic': 'Numpy 로그 변환 (log1p)', 
        'question': f"데이터프레임 `df`의 '{col}' 열의 값이 너무 치우쳐 있어 로그 변환을 하려고 합니다. 0 값 오류를 방지하기 위해 1을 더한 후 로그를 취하는 Numpy 함수를 사용하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "np.log1p()는 log(1+x)를 의미하며, 값이 0일 때 무한대(-inf) 오류가 발생하는 것을 방지하는 안전한 로그 변환 함수입니다.",
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
        'topic': '머신러닝 알고리즘 (KNN 분류기)', 
        'question': "주변의 가까운 이웃 데이터들의 클래스를 다수결로 판단하는 K-최근접 이웃(KNN) 분류 모델 객체를 생성하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sklearn.neighbors 모듈의 KNeighborsClassifier()를 사용해 객체를 생성한 후 fit()으로 학습을 진행합니다.",
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
        'topic': '데이터 분할 비율 유지 (stratify)', 
        'question': "`train_test_split(X, y, ...)`를 사용하여 훈련/검증용 데이터를 나눌 때, 타겟 변수 `y`의 클래스 비율(예: 1:1:1)을 원본과 동일하게 유지하도록 하는 파라미터를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "stratify 파라미터에 타겟 변수를 지정하면, 샘플링 편향을 막고 데이터의 원래 클래스 분포 비율을 그대로 유지하며 분할합니다.",
        'check': lambda x: "stratify=y" in _prep(x)
    }

# -------------------------------------------------------------------
# PLUGIN SYSTEM / STRATEGY REGISTRY
# -------------------------------------------------------------------

class QuizStrategy:
    def __init__(self, id, name, description, easy_pool, hard_pool):
        self.id = id
        self.name = name
        self.description = description
        self.easy_pool = easy_pool
        self.hard_pool = hard_pool


# ==========================================
# 1. 종합 마스터 (Comprehensive) 모드 풀
# ==========================================
COMP_EASY = [
    gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, 
    gen_easy_fillna, gen_easy_drop, gen_easy_filter,
    gen_viz_bar, gen_viz_scatter, gen_viz_hist,
    gen_py_for_loop, gen_py_function, gen_py_basic_type,
    gen_py_loop_control, gen_py_str_split, gen_py_list_slice, gen_py_dict_get,
    gen_sns_pairplot, gen_sns_boxplot, gen_np_log1p
]

COMP_HARD = [
    gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt,
    gen_numpy_array, gen_ml_split, gen_ml_rf, gen_viz_sns,
    gen_param_nuance_concat, gen_param_nuance_dropdup,
    gen_ml_knn, gen_ml_stratify
]

# ==========================================
# 2. 베이직 (Basic / Day 1~4) 모드 풀
# ==========================================
# 현업 수준의 치명적 뉘앙스, 시각화 세부 파라미터, 복잡한 ML은 제외하고
# 교안(PDF) 및 수업(Jupyter) 기반의 가장 확실한 뼈대만 남긴 풀
BASIC_EASY = [
    gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, 
    gen_easy_fillna, gen_easy_drop, gen_easy_filter,
    gen_py_for_loop, gen_py_function, gen_py_basic_type,
    gen_py_loop_control, gen_py_str_split, gen_py_list_slice, gen_py_dict_get
]

BASIC_HARD = [
    gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt,
    gen_numpy_array
]

STRATEGIES = {
    'bootcamp_day1_4': QuizStrategy(
        id='bootcamp_day1_4',
        name='Day 1~4 Bootcamp (시험 대비)',
        description='단기 부트캠프 진도에 맞춘 핵심 위주의 출제 모드입니다.',
        easy_pool=BASIC_EASY,  
        hard_pool=BASIC_HARD
    ),
    'comprehensive': QuizStrategy(
        id='comprehensive',
        name='종합 마스터 (전범위 딥다이브)',
        description='모듈화된 모든 라이브러리의 방대한 전범위를 다루는 극한 모드입니다.',
        easy_pool=COMP_EASY,
        hard_pool=COMP_HARD
    )
}

def get_strategy(strategy_id='bootcamp_day1_4'):
    return STRATEGIES.get(strategy_id, STRATEGIES['bootcamp_day1_4'])

def generate_exam_quizzes(strategy_id='bootcamp_day1_4'):
    strategy = get_strategy(strategy_id)
    easy_pool = strategy.easy_pool
    hard_pool = strategy.hard_pool
    
    quizzes = []
    for _ in range(16):
        f = random.choice(easy_pool)
        q = f()
        if random.random() < 0.1:
            q['type'] = 'text'
        else:
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
        quizzes.append(q)
        
    for _ in range(4):
        f = random.choice(hard_pool)
        q = f()
        if random.random() < 0.1:
            q['type'] = 'text'
        else:
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
        quizzes.append(q)
        
    return quizzes

def generate_single_quiz(strategy_id='bootcamp_day1_4'):
    strategy = get_strategy(strategy_id)
    pool = strategy.easy_pool + strategy.hard_pool
    
    f = random.choice(pool)
    q = f()
    
    if random.random() < 0.1:
        q['type'] = 'text'
    else:
        q['type'] = 'radio'
        opts = [q['expected']] + q['wrongs'][:3]
        random.shuffle(opts)
        q['choices'] = opts
    return q
