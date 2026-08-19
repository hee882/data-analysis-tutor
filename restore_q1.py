import os

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
q_path = os.path.join(repo_path, 'src', 'questions.py')

q_part1 = '''import random
import re

def _prep(text):
    if not text: return ""
    text = text.replace("'", '"')
    text = re.sub(r'\\s+', '', text)
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
'''

with open(q_path, 'w', encoding='utf-8') as f:
    f.write(q_part1)

print("Part 1 written")
