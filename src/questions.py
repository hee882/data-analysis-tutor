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
    df_name = random.choice(["df", "sales", "data", "df_raw"])
    file_name = random.choice(["data.xlsx", "sales.xlsx", "report.xlsx", "info.xlsx"])
    add_param = random.random() < 0.15
    param_str = ", index_col=0" if add_param else ""
    ans = f"{df_name} = pd.read_excel('{file_name}'{param_str})"
    wrongs = [
        f"{df_name} = pd.load_excel('{file_name}')", 
        f"{df_name} = pd.open('{file_name}')", 
        f"{df_name} = pd.read_csv('{file_name}')"
    ]
    q_add = " (단, 첫 번째 열을 인덱스로 지정하세요.)" if add_param else ""
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 불러오기', 
        'question': f"Pandas를 사용하여 '{file_name}' 엑셀 파일을 읽어와 `{df_name}` 변수에 저장하는 코드를 작성하세요.{q_add}",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.read_excel()은 엑셀(.xlsx, .xls) 파일을 Pandas DataFrame으로 읽어오는 함수입니다. pd.read_csv()와 혼동하지 않도록 주의하세요 — 파일 확장자가 .csv면 read_csv(), .xlsx면 read_excel()을 사용합니다. index_col=0 파라미터는 첫 번째 열을 행 번호(인덱스)로 사용하겠다는 의미이며, 엑셀에 이미 고유 ID 열이 있을 때 활용합니다.",
        'check': lambda x: "read_excel" in _prep(x) and file_name in _prep(x)
    }

def gen_easy_head():
    df_name = random.choice(["df", "sales", "customers", "records"])
    n = random.randint(3, 8)
    ans = f"{df_name}.head({n})"
    wrongs = [f"{df_name}.head(rows={n})", f"{df_name}.show({n})", f"{df_name}.top({n})", f"{df_name}.iloc[:{n}, :].head()"]
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 탐색 (앞부분)', 
        'question': f"데이터프레임 `{df_name}`의 처음 {n}개 행을 출력하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"{df_name}.head(N)은 데이터의 첫 N개 행만 빠르게 미리보기 위한 탐색 도구입니다. 실제 데이터 분석에서는 수백만 건의 데이터를 다루기 때문에 전체를 출력하면 커널이 멈추거나 메모리가 터질 수 있습니다. head()로 먼저 컬럼 구조, 데이터 타입, 값의 형태를 확인하는 것이 EDA(탐색적 데이터 분석)의 첫 번째 습관입니다. 반대로 마지막 N개를 보려면 tail(N)을 사용합니다.",
        'check': lambda x: "head" in _prep(x) and str(n) in _prep(x)
    }

def gen_easy_dtypes():
    df_name = random.choice(["df", "my_data", "users_df"])
    ans = f"{df_name}.dtypes"
    wrongs = [f"{df_name}.types", f"{df_name}.info", f"{df_name}.type()"]
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 데이터 타입 확인', 
        'question': f"데이터프레임 `{df_name}`의 각 컬럼별 데이터 타입을 확인하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"{df_name}.dtypes는 각 컬럼의 데이터 타입(int64, float64, object 등)을 확인하는 속성입니다. 타입 확인이 중요한 이유는, 예를 들어 '나이' 컬럼이 숫자처럼 보여도 실제로 object(문자열) 타입이면 평균이나 필터링 연산이 오류를 냅니다. ML 모델에 넣기 전에 반드시 수치형(int/float)인지, 범주형(object/category)인지 파악해서 적절한 인코딩이나 변환을 적용해야 합니다.",
        'check': lambda x: f"{df_name}.dtypes" in _prep(x)
    }

def gen_easy_isnull():
    df_name = random.choice(["df", "dataset", "table"])
    ans = f"{df_name}.isna().sum()"
    wrongs = [f"{df_name}.isna().count()", f"{df_name}.nulls()", f"{df_name}.count_na()"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 결측치 개수 확인', 
        'question': f"데이터프레임 `{df_name}`의 각 컬럼별 결측치(NaN) 총 개수를 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"{df_name}.isna().sum() (또는 isnull().sum())은 각 컬럼의 결측치 개수를 한 번에 확인합니다. 결측치를 그냥 방치하면 대부분의 ML 모델이 에러를 발생시키거나 해당 행을 무시합니다. 특히 결측 비율이 높은 컬럼(예: 80% 이상)은 그 컬럼 자체를 삭제하는 게 나을 수 있고, 낮은 비율(5% 이하)이면 평균/중앙값으로 채우는(fillna) 전략을 씁니다.",
        'check': lambda x: ("isnull" in _prep(x) or "isna" in _prep(x)) and "sum" in _prep(x)
    }

def gen_easy_dropna():
    df_name = random.choice(["df", "clean_df", "data"])
    add_param = random.random() < 0.15
    ans = f"{df_name}.dropna(inplace=True)" if add_param else f"{df_name}.dropna()"
    wrongs = [f"{df_name}.drop_na()", f"{df_name}.remove_na()", f"{df_name}.delete_nulls()"]
    q_add = " 단, inplace 속성을 사용하여 원본 객체를 직접 변경하세요." if add_param else ""
    return {
        'topic': '[4] 데이터 전처리 - 결측치 삭제', 
        'question': f"데이터프레임 `{df_name}`에서 결측치가 하나라도 포함된 행을 모두 삭제하는 코드를 작성하세요.{q_add}",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "dropna()는 결측치가 있는 행을 제거합니다. 단, 무조건 사용하면 안 됩니다 — 데이터가 적을 때 많은 행을 삭제하면 학습 데이터 자체가 부족해져 모델 성능이 오히려 떨어집니다. 결측치가 전체 데이터의 5~10% 이하일 때만 dropna()를 권장하고, 그 이상이면 fillna()로 대체하거나, 결측 여부 자체를 새 피처(is_missing 컬럼)로 만드는 전략을 씁니다.",
        'check': lambda x: "dropna" in _prep(x)
    }

def gen_easy_filter():
    df_name = random.choice(["df", "people", "items"])
    col = random.choice(["age", "score", "price", "count"])
    threshold = random.randint(10, 100)
    op = random.choice([">=", "<=", ">", "<", "=="])
    ans = f"{df_name}[{df_name}['{col}'] {op} {threshold}]"
    wrongs = [
        f"{df_name}.filter({col} {op} {threshold})", 
        f"{df_name}.where({col} {op} {threshold})", 
        f"{df_name}[{col} {op} {threshold}]"
    ]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 조건부 필터링', 
        'question': f"데이터프레임 `{df_name}`에서 '{col}' 컬럼의 값이 {threshold} {op} 인 행만 필터링하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Pandas의 Boolean Indexing은 조건식이 True인 행만 추출하는 방법입니다. `df[df['col'] > 값]` 형태로 쓰며, 중요한 점은 조건식을 df 안에 다시 넣어줘야 한다는 구조입니다. 여러 조건을 동시에 쓸 때는 `and` 대신 `&`(AND), `|`(OR)를 사용하며, 각 조건을 반드시 괄호로 묶어야 합니다 — 예: `(df['나이'] > 20) & (df['성별'] == '남')`.",
        'check': lambda x: df_name in _prep(x) and op in _prep(x) and str(threshold) in _prep(x) and col in _prep(x)
    }

def gen_easy_loc():
    df_name = random.choice(["df", "matrix", "records"])
    idx = random.randint(0, 10)
    col = random.choice(["name", "title", "address", "status"])
    ans = f"{df_name}.loc[{idx}, '{col}']"
    wrongs = [f"{df_name}.iloc[{idx}, '{col}']", f"{df_name}[{idx}, '{col}']", f"{df_name}.loc['{col}', {idx}]"]
    return {
        'topic': '[3] 데이터 추출 및 확인 - 특정 데이터 접근 (loc)', 
        'question': f"데이터프레임 `{df_name}`에서 인덱스 이름이 {idx}이고 컬럼명이 '{col}'인 곳의 데이터를 가져오는 `.loc` 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': ".loc[]은 '라벨(Label) 기반' 인덱싱입니다. df.loc[행 라벨, 열 이름] 형태로 사용합니다. 반면 .iloc[]은 '정수 위치(Integer Location) 기반'으로, 실제 인덱스 번호가 아닌 몇 번째 행인지로 접근합니다. 혼동하기 쉬운 케이스: 인덱스가 0, 1, 2...가 아닌 'a', 'b', 'c'이거나, reset_index 후 번호가 뒤섞인 상태라면 loc과 iloc의 결과가 완전히 달라집니다.",
        'check': lambda x: f"loc[{idx}," in _prep(x) and col in _prep(x)
    }

def gen_easy_value_counts():
    df_name = random.choice(["df", "survey", "logs"])
    col = random.choice(["category", "grade", "level", "type"])
    add_param = random.random() < 0.15
    ans = f"{df_name}['{col}'].value_counts(normalize=True)" if add_param else f"{df_name}['{col}'].value_counts()"
    wrongs = [f"{df_name}['{col}'].count_values()", f"{df_name}['{col}'].counts()", f"pd.value_counts({df_name}, '{col}')"]
    q_add = " (단, normalize=True 파라미터를 사용하여 비율로 표시하세요.)" if add_param else ""
    return {
        'topic': '[3] 데이터 추출 및 확인 - 카테고리 빈도수 확인', 
        'question': f"데이터프레임 `{df_name}`의 '{col}' 컬럼에 있는 항목별 빈도수를 구하는 코드를 작성하세요.{q_add}",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': ".value_counts()는 시리즈(Series)의 각 고유값이 몇 번 등장하는지 내림차순으로 반환합니다. 범주형 변수의 분포를 파악할 때 가장 먼저 쓰는 함수입니다. normalize=True를 추가하면 절대 빈도수 대신 비율(0~1)로 반환되어, 클래스 불균형(예: 정상 95% vs 사기 5%) 여부를 즉시 파악할 수 있어 ML 모델링 전 필수 체크 사항입니다.",
        'check': lambda x: "value_counts" in _prep(x) and col in _prep(x)
    }

def gen_viz_countplot():
    df_name = random.choice(["df", "data", "events"])
    col = random.choice(["day", "month", "season", "weather"])
    ans = f"sns.countplot(data={df_name}, x='{col}')"
    wrongs = [f"sns.bar({df_name}, '{col}')", f"plt.countplot({df_name}['{col}'])", f"{df_name}.plot(kind='count', x='{col}')"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Countplot)', 
        'question': f"Seaborn을 사용하여 데이터프레임 `{df_name}`의 '{col}' 컬럼별 데이터 개수를 막대 그래프로 시각화하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.countplot()은 범주형 변수의 각 카테고리별 개수(빈도)를 막대 그래프로 보여줍니다. 단순한 bar chart와의 차이점은, countplot은 별도의 y값 계산 없이 데이터 자체를 세어준다는 것입니다. hue 파라미터를 추가하면 (예: hue='성별') 카테고리 안에서 또 다른 범주로 세분화하여 시각화할 수 있어, 두 범주형 변수 간의 관계를 동시에 파악하는 데 강력합니다.",
        'check': lambda x: "countplot" in _prep(x) and col in _prep(x)
    }

def gen_viz_histplot():
    df_name = random.choice(["df", "measurements", "stats"])
    col = random.choice(["tip", "height", "weight", "length"])
    ans = f"sns.histplot(data={df_name}, x='{col}')"
    wrongs = [f"sns.histogram({df_name}, '{col}')", f"plt.histplot({df_name}['{col}'])", f"sns.hist({df_name}['{col}'])"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Histplot)', 
        'question': f"Seaborn을 사용하여 데이터프레임 `{df_name}`의 연속형 숫자 컬럼인 '{col}'의 분포를 히스토그램으로 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.histplot()은 연속형(수치형) 데이터의 분포를 구간(bin)으로 나누어 히스토그램으로 보여줍니다. 이 그래프를 먼저 확인해야 하는 이유는, 데이터가 정규분포(종 모양)인지, 한쪽으로 치우친 왜도(Skew)가 있는지, 이상치(Outlier)가 존재하는지를 한눈에 볼 수 있기 때문입니다. 분포가 심하게 치우쳐 있다면 np.log1p() 로그 변환을 통해 정규분포에 가깝게 만들어 모델 성능을 높일 수 있습니다.",
        'check': lambda x: "histplot" in _prep(x) and col in _prep(x)
    }

def gen_viz_scatter():
    df_name = random.choice(["df", "scatter_data", "points"])
    x_col = random.choice(["age", "width", "speed", "size"])
    y_col = random.choice(["income", "height", "distance", "cost"])
    ans = f"sns.scatterplot(data={df_name}, x='{x_col}', y='{y_col}')"
    wrongs = [f"sns.scatter(x='{x_col}', y='{y_col}')", f"plt.scatter({df_name})", f"{df_name}.plot_scatter('{x_col}', '{y_col}')"]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (Scatter plot)', 
        'question': f"Seaborn을 사용하여 데이터프레임 `{df_name}`에서 x축을 '{x_col}', y축을 '{y_col}'으로 하는 산점도(Scatter plot)를 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.scatterplot()은 두 연속형 변수 간의 관계(상관관계)를 점으로 시각화합니다. 점들이 우상향이면 양의 상관관계(하나가 오르면 다른 하나도 상승), 우하향이면 음의 상관관계입니다. 중요한 점: 상관관계와 인과관계는 다릅니다. 산점도는 '같이 움직이는지'만 보여줄 뿐, '원인'을 설명하지 않습니다. 또한 hue 파라미터로 범주형 변수를 색으로 추가하면 군집(Cluster) 패턴을 발견하는 데 유용합니다.",
        'check': lambda x: "sns.scatterplot" in _prep(x) and x_col in _prep(x) and y_col in _prep(x)
    }

def gen_py_str_split():
    text_var = random.choice(["text", "sentence", "words"])
    sep = random.choice([",", " ", "-", "|"])
    items = ["사과", "바나나", "포도"]
    random.shuffle(items)
    sample_text = sep.join(items)
    ans = f"{text_var}.split('{sep}')"
    wrongs = [f"{text_var}.slice('{sep}')", f"{text_var}.divide('{sep}')", f"split({text_var}, '{sep}')"]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (문자열 분리)', 
        'question': f"문자열 `{text_var} = '{sample_text}'`가 주어졌을 때, '{sep}' 문자를 기준으로 분리하여 리스트로 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': ".split('구분자')는 문자열을 특정 구분자 기준으로 나눠 리스트로 반환합니다. 반환 결과가 리스트임을 기억하세요 — '사과,바나나,포도'.split(',')의 결과는 ['사과', '바나나', '포도']입니다. 실무에서는 주소 데이터를 '시/구/동'으로 분리하거나, CSV 파싱, 로그 파일에서 특정 값만 추출할 때 자주 쓰입니다. 구분자 없이 split()만 쓰면 공백 기준으로 분리합니다.",
        'check': lambda x: "split" in _prep(x) and sep in _prep(x)
    }

def gen_eda_concept_cat_num():
    ans = "sns.boxplot() 또는 sns.barplot()"
    wrongs = ["sns.scatterplot()", "sns.histplot()", "sns.lineplot()"]
    return {
        'topic': '[7] EDA 및 시각화 - EDA 개념 (범주형+수치형 시각화)', 
        'question': "탐색적 데이터 분석(EDA) 과정에서 '범주형 데이터'에 따른 '수치형 데이터'의 차이나 분포를 비교하려고 합니다. 다음 중 가장 적절한 Seaborn 시각화 함수는 무엇일까요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "범주형(X) + 수치형(Y) 관계 분석에는 boxplot이나 barplot이 적합합니다. Boxplot은 중앙값, 사분위수, 이상치를 한 번에 보여줘서 그룹 간 분포 차이를 파악하기 좋습니다. Barplot은 각 그룹의 평균을 비교합니다. Scatterplot이나 histplot은 수치형 변수끼리, 또는 단일 수치형 변수 분포를 보는 데 쓰이므로 이 상황에는 맞지 않습니다. EDA에서 변수 타입 조합(수치형+수치형, 범주형+수치형 등)에 따라 적절한 시각화를 선택하는 것이 핵심입니다.",
        'check': lambda x: "box" in _prep(x) or "bar" in _prep(x),
        'force_type': 'radio'
    }

def gen_eda_concept_num_num():
    ans = "sns.scatterplot() 또는 sns.pairplot()"
    wrongs = ["sns.countplot()", "sns.pie()", "sns.boxplot()"]
    return {
        'topic': '[7] EDA 및 시각화 - EDA 개념 (다중 수치형 시각화)', 
        'question': "여러 개의 '수치형 변수'들 간의 상관관계를 한눈에 파악하기 위해 산점도 행렬을 그리려고 합니다. 가장 적합한 함수 조합은 무엇일까요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "수치형 변수 두 개의 관계는 scatterplot으로, 여러 수치형 변수들 사이의 관계를 격자 형태로 한 번에 보려면 pairplot을 사용합니다. pairplot은 내부적으로 모든 변수 쌍의 scatterplot + 대각선에 단변수 분포(histplot)를 그려줍니다. 이를 통해 '어떤 변수 쌍이 강한 상관관계를 가지는지'를 빠르게 스캔할 수 있어, 피처 선택(Feature Selection)과 다중공선성 진단에 유용합니다.",
        'check': lambda x: "scatter" in _prep(x) or "pair" in _prep(x),
        'force_type': 'radio'
    }

def gen_easy_fillna():
    df_name = random.choice(["df", "base_df", "train"])
    col = random.choice(["age", "salary", "score"])
    method = random.choice(["mean", "median"])
    add_param = random.random() < 0.15
    ans = f"{df_name}['{col}'].fillna({df_name}['{col}'].{method}(), inplace=True)" if add_param else f"{df_name}['{col}'].fillna({df_name}['{col}'].{method}())"
    wrongs = [f"{df_name}['{col}'].dropna()", f"{df_name}['{col}'] = {df_name}['{col}'].{method}()", f"{df_name}.fillna()"]
    q_add = " 단, inplace 속성을 사용하여 원본 객체를 직접 변경하세요." if add_param else ""
    korean_method = "평균값(mean)" if method == "mean" else "중앙값(median)"
    return {
        'topic': '[4] 데이터 전처리 - 데이터 전처리 (결측치 대체)', 
        'question': f"데이터프레임 `{df_name}`의 '{col}' 컬럼에 있는 결측치(NaN)를 '{col}' 컬럼의 {korean_method}으로 채우는 코드를 작성하세요.{q_add}",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"fillna()는 결측치를 특정 값으로 채우는 함수입니다. 평균(mean)은 데이터 분포가 정규분포에 가깝고 이상치가 없을 때 사용합니다. 반면 '연봉', '집값' 같이 소수의 초고값(이상치)이 있어 분포가 한쪽으로 치우친 경우엔 평균이 실제 중심보다 크게 왜곡되므로, 이상치에 영향받지 않는 중앙값(median)을 사용하는 것이 더 안전합니다. fillna 후에는 반드시 isna().sum()으로 결측치가 사라졌는지 재검증해야 합니다.",
        'check': lambda x: "fillna" in _prep(x) and method in _prep(x)
    }

def gen_ml_concept():
    ans = "분류(Classification)"
    wrongs = ["회귀(Regression)", "군집화(Clustering)", "차원 축소(Dimensionality Reduction)"]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 개념 (지도학습 방법론)', 
        'question': "우리가 예측하려는 타겟(Target) 데이터가 '생존여부(0 또는 1)', '꽃의 종류(Iris-setosa 등)'와 같은 '범주형(Categorical) 데이터'일 때 사용하는 머신러닝 모델링 기법을 무엇이라고 하나요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "ML 문제는 타겟 변수의 유형에 따라 크게 두 가지로 나뉩니다. 타겟이 '생존(0/1)', '스팸(True/False)', '꽃의 종류' 처럼 이산적인 범주(Category)라면 분류(Classification), '주택 가격', '기온' 처럼 연속적인 숫자라면 회귀(Regression)입니다. 분류와 회귀를 혼동하면 손실 함수, 평가 지표(정확도 vs RMSE), 출력층 설계가 모두 어긋나기 때문에 데이터를 받는 즉시 타겟 변수 유형을 파악하는 것이 ML 엔지니어링의 시작점입니다.",
        'check': lambda x: "분류" in x or "class" in x.lower(),
        'force_type': 'radio'
    }

def gen_ml_split_basic():
    x_var = random.choice(["X", "features"])
    y_var = random.choice(["y", "target"])
    t_size = round(random.uniform(0.1, 0.4), 2)
    r_state = random.randint(10, 99)
    ans = f"train_test_split({x_var}, {y_var}, test_size={t_size}, random_state={r_state})"
    wrongs = [
        f"train_test_split({x_var}, {y_var}, {t_size}, {r_state})", 
        f"split({x_var}, {y_var}, test_size={t_size})", 
        f"pd.train_test_split({x_var}, {y_var}, test_ratio={t_size})"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 데이터 분할 (train_test_split)', 
        'question': f"머신러닝 학습을 위해 특징({x_var})과 타겟({y_var}) 데이터를 분할합니다. 테스트 데이터 비율(test_size)을 {t_size}로, 난수 고정(random_state)을 {r_state}로 설정하여 분할하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "train_test_split()은 학습용(Train)과 평가용(Test) 데이터를 분리합니다. 이 분리 없이 같은 데이터로 학습하고 평가하면 모델이 데이터를 '암기'한 것이므로 성능이 실제보다 훨씬 높게 나옵니다 — 이것을 과적합(Overfitting)이라 합니다. random_state는 매번 실행 시 같은 분할 결과를 보장하는 난수 시드(Seed)입니다. test_size=0.2는 전체의 20%를 테스트에 사용한다는 의미입니다.",
        'check': lambda x: "train_test_split" in _prep(x) and str(t_size) in _prep(x) and str(r_state) in _prep(x)
    }

def gen_py_list_slice():
    lst_var = random.choice(["lst", "my_list", "arr"])
    ans = f"{lst_var}[::-1]"
    wrongs = [f"{lst_var}[-1:]", f"{lst_var}.reverse()", f"reversed({lst_var})"]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (리스트 슬라이싱)', 
        'question': f"리스트 `{lst_var}`의 요소 순서를 완전히 거꾸로 뒤집은 새로운 리스트를 슬라이싱(slicing) 기법만 사용하여 만드는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "파이썬 슬라이싱의 구조는 [start:stop:step]입니다. step을 -1로 지정하면 뒤에서부터 역순으로 순회합니다. `lst[::-1]`은 리스트 전체를 뒤집어 새 리스트를 반환합니다. 주의: `lst.reverse()`는 원본 리스트를 직접 뒤집고 None을 반환하는 반면, `lst[::-1]`은 원본을 그대로 두고 새 리스트를 반환합니다. 불변(Immutable)이 필요한 상황이라면 슬라이싱을 사용해야 합니다.",
        'check': lambda x: "[::-1]" in _prep(x)
    }

def gen_sns_boxplot():
    df_name = random.choice(["df", "dataset", "stats_df"])
    x = random.choice(['day', 'sex', 'category', 'group'])
    y = random.choice(['tip', 'total_bill', 'score', 'value'])
    hue = random.choice(['smoker', 'time', 'type', 'status'])
    ans = f"sns.boxplot(data={df_name}, x='{x}', y='{y}', hue='{hue}')"
    wrongs = [
        f"sns.violinplot(data={df_name}, x='{x}', y='{y}')", 
        f"sns.boxplot(data={df_name}, x='{y}', y='{x}')", 
        f"sns.histplot(data={df_name}, x='{x}', hue='{hue}')"
    ]
    return {
        'topic': '[7] EDA 및 시각화 - Seaborn 시각화 (boxplot)', 
        'question': f"데이터프레임 `{df_name}`에서 x축을 '{x}', y축을 '{y}'로 설정하고, '{hue}' 기준으로 쪼개어 박스플롯(Boxplot)을 그리는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "sns.boxplot()은 데이터의 5가지 통계 요약(최솟값, 1사분위, 중앙값, 3사분위, 최댓값)을 박스 형태로 보여주며, 박스 바깥의 점들은 이상치(Outlier)로 간주됩니다. 범주형 변수를 x축에 놓으면 그룹별 분포를 비교할 수 있습니다. hue 파라미터로 세 번째 변수를 추가하면 한 그래프에서 2개의 범주형 변수와 1개의 수치형 변수를 동시에 분석할 수 있어 EDA의 핵심 도구입니다.",
        'check': lambda x: "boxplot" in _prep(x) and x in _prep(x) and y in _prep(x) and hue in _prep(x)
    }

def gen_np_log1p():
    df_name = random.choice(["df", "data", "records"])
    col = random.choice(['price', 'spc_R', 'population', 'sales'])
    ans = f"np.log1p({df_name}['{col}'])"
    wrongs = [
        f"np.log({df_name}['{col}'])", 
        f"np.log10({df_name}['{col}'])", 
        f"{df_name}['{col}'].log1p()"
    ]
    return {
        'topic': '[4] 데이터 전처리 - Numpy 로그 변환 (log1p)', 
        'question': f"데이터프레임 `{df_name}`의 '{col}' 열에 0 값 오류를 방지하기 위해 1을 더한 후 로그를 취하는 Numpy 함수를 적용하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "np.log1p()는 log(1+x)를 계산합니다. 단순 np.log()를 쓰면 값이 0일 때 log(0)=-∞가 되어 오류 또는 무한대 값이 발생합니다. +1을 먼저 더함으로써 0인 값도 안전하게 처리합니다. 로그 변환을 하는 이유: '가격', '인구' 같이 한쪽으로 심하게 치우친(Skewed) 분포를 정규분포에 가깝게 만들어 선형 모델의 성능을 높이기 위해서입니다. 로그 변환한 값으로 예측한 뒤에는 반드시 np.expm1()로 역변환해야 원래 스케일의 예측값을 얻습니다.",
        'check': lambda x: "log1p" in _prep(x) and col in _prep(x)
    }

# =====================================================================
# [HARD POOL] - 심화 개념, 함정 문제 (총 4문제 출제용)
# =====================================================================

def gen_hard_apply():
    df_name = random.choice(["df", "dataset", "info_df"])
    col = random.choice(["reg", "code", "text_col"])
    func_name = random.choice(["get_sido", "clean_text", "process_data"])
    ans = f"{df_name}['{col}'].apply({func_name})"
    wrongs = [f"{df_name}['{col}'].map({func_name}())", f"apply({func_name}, {df_name}['{col}'])", f"{df_name}['{col}'].apply({func_name}(x))"]
    return {
        'topic': '[4] 데이터 전처리 - 사용자 정의 함수 적용 (apply)', 
        'question': f"`{func_name}(x)`라는 사용자 정의 함수가 이미 선언되어 있습니다. 데이터프레임 `{df_name}`의 '{col}' 컬럼의 모든 행 데이터에 이 함수를 일괄 적용시키는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Series.apply(함수명)은 각 행/원소에 함수를 순차적으로 적용합니다. 함수명만 전달하는 것이지 함수를 호출(())하는 것이 아닙니다 — apply(get_sido)가 맞고, apply(get_sido())는 함수의 '결과값'을 인자로 넘기는 잘못된 코드입니다. apply는 for 반복문보다 훨씬 빠르며, 정규표현식 파싱, 카테고리 매핑, 복잡한 파생 변수 계산 등 단순 산술 연산으로 해결 안 되는 경우에 사용합니다.",
        'check': lambda x: "apply" in _prep(x) and func_name in _prep(x) and "()" not in _prep(x)
    }

def gen_hard_groupby():
    df_name = random.choice(["df", "sales", "logs"])
    g_col = random.choice(["sido", "department", "region"])
    t_col = random.choice(["spc_R", "revenue", "profit"])
    agg = random.choice(["mean", "sum", "max", "min"])
    add_param = random.random() < 0.15
    ans = f"{df_name}.groupby('{g_col}', observed=False)['{t_col}'].{agg}()" if add_param else f"{df_name}.groupby('{g_col}')['{t_col}'].{agg}()"
    wrongs = [f"{df_name}.groupby('{g_col}').{agg}('{t_col}')", f"{df_name}['{t_col}'].groupby('{g_col}').{agg}()", f"pd.groupby({df_name}, '{g_col}')['{t_col}'].{agg}()"]
    q_add = " (단, observed=False 파라미터를 사용하세요.)" if add_param else ""
    return {
        'topic': '[5] 데이터 집계 - 그룹화 집계 (groupby)', 
        'question': f"데이터프레임 `{df_name}`에서 '{g_col}' 별로 그룹을 묶은 뒤, '{t_col}'의 '{agg}'(을)를 구하는 Series 반환 코드를 작성하세요.{q_add}",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "groupby()는 SQL의 GROUP BY와 같은 개념입니다. df.groupby('기준컬럼')['대상컬럼'].통계함수() 순서로 작성합니다. 기준컬럼 기준으로 데이터를 묶은 뒤, 대상컬럼에 mean/sum/max 등의 집계를 수행합니다. 결과는 기본적으로 Series로 반환되며, 기준컬럼이 인덱스가 됩니다. as_index=False를 주면 기준컬럼이 인덱스가 아닌 일반 컬럼으로 유지되어 DataFrame으로 반환됩니다.",
        'check': lambda x: "groupby" in _prep(x) and g_col in _prep(x) and t_col in _prep(x) and agg in _prep(x)
    }

def gen_hard_merge():
    df1 = random.choice(["df1", "users", "left_df"])
    df2 = random.choice(["df2", "orders", "right_df"])
    on_col = random.choice(["code", "user_id", "key"])
    how = random.choice(["left", "right", "outer", "inner"])
    ans = f"pd.merge({df1}, {df2}, on='{on_col}', how='{how}')"
    wrongs = [f"{df1}.join({df2}, on='{on_col}', type='{how}')", f"pd.concat([{df1}, {df2}], axis=1)", f"{df1}.merge_{how}({df2}, '{on_col}')"]
    return {
        'topic': '[6] 데이터 병합 - 데이터 병합 (Left Merge)', 
        'question': f"데이터프레임 `{df1}`(과)와 `{df2}`(을)를 '{on_col}' 컬럼 기준으로 {how} Merge 하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.merge()는 두 DataFrame을 특정 키(on) 컬럼을 기준으로 합칩니다. how 파라미터가 핵심: inner(기본값)는 양쪽에 모두 있는 것만 남기고, left는 왼쪽 DataFrame은 모두 유지, right는 오른쪽 모두 유지, outer는 양쪽 합집합입니다. how를 잘못 선택하면 행 수가 예상치 못하게 줄거나 NaN이 대량 발생합니다. 병합 후에는 결과 df의 shape을 꼭 확인하는 습관을 가지세요.",
        'check': lambda x: "merge" in _prep(x) and how in _prep(x) and on_col in _prep(x)
    }

def gen_hard_pivot():
    df_name = random.choice(["df", "sales_df", "records"])
    idx = random.choice(["sex", "region", "category"])
    col = random.choice(["smoker", "season", "type"])
    val = random.choice(["tip", "sales", "count"])
    agg = random.choice(["mean", "sum", "max"])
    ans = f"pd.pivot_table({df_name}, index='{idx}', columns='{col}', values='{val}', aggfunc='{agg}')"
    wrongs = [
        f"{df_name}.groupby(['{idx}','{col}'])['{val}'].{agg}().pivot()", 
        f"pd.pivot({df_name}, '{idx}', '{col}', '{val}')", 
        f"{df_name}.pivot_table(group='{idx}', target='{val}', func='{agg}')"
    ]
    return {
        'topic': '[5] 데이터 집계 - 피벗 테이블 (Pivot Table)', 
        'question': f"데이터프레임 `{df_name}`에서 인덱스를 '{idx}', 컬럼을 '{col}'로 설정하고 '{val}'의 '{agg}'(을)를 구하는 피벗 테이블 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "pd.pivot_table()은 엑셀의 피벗 테이블과 동일한 개념으로, 행(index)과 열(columns)의 교차점에 집계값(aggfunc)을 배치합니다. 예를 들어 index='성별', columns='흡연 여부', values='팁', aggfunc='mean'이면 성별×흡연 여부 조합별 평균 팁이 매트릭스 형태로 출력됩니다. groupby보다 결과를 2D 매트릭스로 보여줘서 교차 분석이 직관적입니다. 단, aggfunc를 지정하지 않으면 기본값 mean이 적용됩니다.",
        'check': lambda x: "pivot_table" in _prep(x) and idx in _prep(x) and col in _prep(x) and val in _prep(x)
    }

def gen_ml_knn():
    k = random.randint(3, 11)
    ans = f"KNeighborsClassifier(n_neighbors={k})"
    wrongs = [
        "KNeighborsRegressor()", 
        f"KNNClassifier(k={k})", 
        "KNeighborsClassifier.fit()"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 모델 튜닝 (KNN)', 
        'question': f"K-최근접 이웃(KNN) 분류 모델 객체를 생성하되, 이웃의 수(K)를 {k}(으)로 설정하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "KNN(K-최근접 이웃)은 새로운 데이터 포인트에서 가장 가까운 K개의 학습 데이터를 찾아 다수결로 클래스를 결정합니다. K값이 클수록 결정 경계가 부드러워져(과소적합 방향), 작을수록 경계가 복잡해집니다(과적합 방향). K=1이면 훈련 정확도 100%지만 새 데이터에서는 노이즈에 민감합니다. 또한 KNN은 거리 기반이므로 반드시 StandardScaler 등으로 스케일링을 해야 큰 범위의 변수가 거리 계산을 지배하는 현상을 막을 수 있습니다.",
        'check': lambda x: "kneighborsclassifier" in _prep(x) and "n_neighbors" in _prep(x)
    }

def gen_ml_split_stratify():
    x_var = random.choice(["X", "features"])
    y_var = random.choice(["y", "target"])
    t_size = round(random.uniform(0.1, 0.4), 2)
    ans = f"train_test_split({x_var}, {y_var}, test_size={t_size}, stratify={y_var})"
    wrongs = [
        f"train_test_split({x_var}, {y_var}, {t_size})", 
        f"train_test_split({x_var}, {y_var}, test_size={t_size}, balance=True)", 
        f"pd.train_test_split({x_var}, {y_var}, test_size={t_size}, stratify={y_var})"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 데이터 분할과 층화추출 (stratify)', 
        'question': f"`train_test_split`을 사용하여 테스트 비율을 {t_size}로 분할할 때, 타겟 변수 `{y_var}`의 원본 클래스 비율을 유지하게 만드는 파라미터를 포함하여 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "stratify=y를 지정하면 Train/Test 분할 시 타겟 클래스의 비율을 원본과 동일하게 유지합니다. 왜 중요한가: 사기 거래가 전체의 1%인 데이터를 단순 랜덤 분할하면 우연히 Test에 사기 건수가 0개가 될 수도 있습니다. 이러면 모델이 사기를 전혀 탐지하지 못해도 Test 정확도가 높게 나오는 함정에 빠집니다. 불균형 데이터에서 stratify는 선택이 아닌 필수입니다.",
        'check': lambda x: "train_test_split" in _prep(x) and f"stratify={y_var.lower()}" in _prep(x)
    }

def gen_ml_cv():
    model = random.choice(["knn", "rf_model", "clf"])
    x_var = random.choice(["train_x", "X_train"])
    y_var = random.choice(["train_y", "y_train"])
    cv_num = random.randint(3, 10)
    ans = f"cross_val_score({model}, {x_var}, {y_var}, cv={cv_num}).mean()"
    wrongs = [
        f"cross_validate({model}, {x_var}, {y_var}, k={cv_num}).mean()", 
        f"{model}.score({x_var}, {y_var}, cv={cv_num})", 
        f"cross_val_score({model}, {x_var}, {y_var}, fold={cv_num}).average()"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 교차 검증 (Cross Validation)', 
        'question': f"모델 `{model}`(과)와 훈련데이터 `{x_var}`, `{y_var}`를 {cv_num}-Fold 교차 검증하여 얻어진 점수들의 평균(mean)을 구하는 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "cross_val_score()는 데이터를 cv개의 fold로 나누어 (cv-1)개로 학습하고 1개로 검증하는 과정을 cv번 반복한 뒤 점수 배열을 반환합니다. 단순 train/test split에 비해 훨씬 신뢰성 높은 성능 추정이 가능합니다 — 특정 분할 방식의 운(luck)에 덜 의존하기 때문입니다. .mean()으로 평균 점수를, .std()로 분산(일관성)을 함께 보는 것이 좋습니다. 단, 데이터가 시계열이라면 fold의 시간 순서를 지키는 TimeSeriesSplit을 사용해야 합니다.",
        'check': lambda x: "cross_val_score" in _prep(x) and f"cv={cv_num}" in _prep(x) and "mean" in _prep(x)
    }

# -------------------------------------------------------------------
# PLUGIN SYSTEM / STRATEGY REGISTRY
# -------------------------------------------------------------------

def gen_killer_chained_assignment():
    df_name = random.choice(["df", "data"])
    col1 = random.choice(["A", "X", "val1"])
    col2 = random.choice(["B", "Y", "val2"])
    cond = random.randint(1, 10)
    target = random.randint(10, 100)
    ans = f"{df_name}.loc[{df_name}['{col1}'] > {cond}, '{col2}'] = {target}"
    wrongs = [
        f"{df_name}[{df_name}['{col1}'] > {cond}]['{col2}'] = {target}",
        f"{df_name}.query('{col1} > {cond}')['{col2}'] = {target}",
        f"{df_name}.where({df_name}['{col1}'] > {cond})['{col2}'] = {target}"
    ]
    return {
        'topic': '[0] 기타 - 킬러 - Pandas 인덱싱 (Chained Assignment)',
        'question': f"데이터프레임 `{df_name}`에서 '{col1}' 컬럼의 값이 {cond}보다 큰 행들의 '{col2}' 컬럼 값을 {target}(으)로 변경하려고 합니다. `SettingWithCopyWarning`을 피하면서 원본 데이터를 안전하게 수정하는 올바른 코드는 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "Chained Assignment(연쇄 인덱싱)는 df[조건][열] = 값처럼 인덱싱을 두 번 연결하는 방식입니다. 이것이 위험한 이유: 첫 번째 인덱싱 df[조건]이 원본 DataFrame의 복사본(copy)을 반환할 수도 있고, 뷰(view)를 반환할 수도 있는데, 이는 Pandas 내부 구현에 따라 달라집니다. 복사본이 반환된 경우 두 번째 인덱싱으로 값을 변경해도 원본에는 반영되지 않아 조용히 실패합니다. df.loc[조건, 열] = 값은 단일 연산으로 원본을 직접 수정하므로 항상 안전합니다.",
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
        'explanation': "pd.merge()의 기본값: how='inner'(교집합), on=공통 컬럼 자동 탐지. 공통 컬럼이 병합 키가 아닌 경우(즉 on 파라미터로 지정되지 않은 공통 컬럼) '_x', '_y' 접미사가 자동으로 붙습니다. suffixes 파라미터로 커스텀 접미사 지정 가능합니다: suffixes=('_left', '_right'). 인덱스 기반 병합은 left_index=True, right_index=True로 merge에서도 가능합니다(join 함수가 아니어도 됩니다). 병합 후 예상보다 행이 많다면 키 컬럼에 중복이 있는 것이므로 반드시 확인해야 합니다.",
        'force_type': 'radio'
    }

def gen_hard_data_leakage():
    domain = random.choice(["금융 사기 탐지", "의료 진단", "주택 가격 예측", "고객 이탈 예측"])
    scaler = random.choice(["StandardScaler", "MinMaxScaler", "RobustScaler"])
    ans = "테스트 데이터(Test Data)에도 fit_transform()을 적용했다."
    wrongs = [
        "학습 데이터(Train Data)에만 fit_transform()을 적용했다.",
        "테스트 데이터(Test Data)에는 transform()만 적용했다.",
        f"{scaler} 대신 다른 스케일러를 사용하지 않았다."
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 데이터 누수(Data Leakage)',
        'question': f"{domain} 모델을 개발하는 과정에서 데이터 누수(Data Leakage)가 발생하여 모델의 성능이 과장되게 측정되었습니다. 다음 중 데이터 누수를 유발한 결정적인 실수로 가장 올바른 것은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "데이터 누수(Data Leakage)란 모델 학습 시 미래 정보나 테스트 데이터의 정보가 훈련 과정에 스며들어, 실제 배포 후 성능이 학습 때보다 훨씬 낮아지는 현상입니다. 스케일러의 경우 Train+Test 전체에 fit()하면 테스트 데이터의 통계(평균, 표준편차)가 스케일러에 반영되어 누수가 발생합니다. 올바른 방법: Train에만 scaler.fit_transform(), Test에는 scaler.transform()만 사용합니다. 모델 선택, 결측치 대체 등 모든 전처리에서 동일한 원칙이 적용됩니다.",
        'force_type': 'radio'
    }

def gen_hard_ml_sequence():
    ans = "데이터 분할(Split) -> 결측치 처리(Imputation) -> 스케일링(Scaling) -> 모델 학습(Fit)"
    wrongs = [
        "결측치 처리(Imputation) -> 스케일링(Scaling) -> 데이터 분할(Split) -> 모델 학습(Fit)",
        "데이터 분할(Split) -> 스케일링(Scaling) -> 결측치 처리(Imputation) -> 모델 학습(Fit)",
        "결측치 처리(Imputation) -> 데이터 분할(Split) -> 스케일링(Scaling) -> 모델 학습(Fit)"
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 파이프라인 시퀀스',
        'question': "머신러닝 전처리 및 학습 과정의 올바른 순서(Sequence)로 가장 적절한 것을 고르시오. (Data Leakage를 방지하는 관점)",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "ML 프로젝트의 올바른 순서가 중요한 이유: EDA 없이 전처리부터 시작하면 어떤 컬럼에 결측치가 많은지, 분포가 어떤지 모른 채 잘못된 전처리를 할 수 있습니다. 가장 중요한 규칙은 Train/Test Split을 전처리 앞에 두는 것 — 스케일링, 결측치 채우기 등의 기준(fit)은 모두 Train 데이터로만 계산하고, Test에는 적용(transform)만 해야 데이터 누수를 방지할 수 있습니다. 전처리 후 분할하면 테스트 정보가 훈련 기준에 섞여 성능이 과장됩니다.",
        'force_type': 'radio'
    }

def gen_hard_precision_recall():
    contexts = [
        ("암 진단", "실제 암 환자를 놓치면(정상으로 오진하면) 치명적이므로", "재현율(Recall)"),
        ("불량품 검출", "실제 불량품이 시장에 유통되면 큰 손실이 발생하므로", "재현율(Recall)"),
        ("스팸 메일 필터링", "정상 메일을 스팸으로 분류하여 중요한 연락을 못 받으면 안 되므로", "정밀도(Precision)"),
        ("무죄 추정 원칙(재판)", "무고한 사람을 범죄자로 판결하는 억울한 상황을 막아야 하므로", "정밀도(Precision)")
    ]
    domain, reason, ans = random.choice(contexts)
    wrongs = ["정밀도(Precision)", "재현율(Recall)", "F1-Score", "정확도(Accuracy)"]
    wrongs.remove(ans) # Remove correct answer to form wrong list
    random.shuffle(wrongs)
    return {
        'topic': '[8] 머신러닝 기초 - 평가 지표 (Precision vs Recall)',
        'question': f"{domain} AI 모델을 설계하려고 합니다. {reason} 어떤 평가지표를 최우선으로 높이는(강조하는) 방향으로 모델의 임계값을 조정해야 합니까?",
        'expected': ans,
        'wrongs': wrongs[:3],
        'explanation': "Precision(정밀도)은 '내가 Positive라고 예측한 것 중 실제 Positive의 비율' — 즉 오탐(FP)을 줄이는 지표입니다. Recall(재현율)은 '실제 Positive 중 내가 맞게 예측한 비율' — 즉 미탐(FN)을 줄이는 지표입니다. 암 진단처럼 '실제 암 환자를 놓치면 치명적'인 경우는 Recall을 극대화해야 합니다. 스팸 필터처럼 '정상 메일이 스팸으로 분류되면 곤란'한 경우는 Precision을 높여야 합니다. 두 지표는 트레이드오프 관계라, 임계값(Threshold)을 낮추면 Recall 증가 & Precision 감소, 높이면 반대입니다.",
        'force_type': 'radio'
    }

def gen_hard_overfitting():
    ans = "과대적합(Overfitting)"
    wrongs = ["과소적합(Underfitting)", "일반화(Generalization)", "정상적합(Good fit)"]
    train_acc = random.randint(97, 100)
    test_acc = random.randint(60, 75)
    return {
        'topic': '[8] 머신러닝 기초 - 과대적합(Overfitting)',
        'question': f"머신러닝 모델을 평가한 결과, 훈련 데이터(Train data)에서의 정확도는 {train_acc}%로 매우 높게 나타났으나, 검증 데이터(Test data)에서의 정확도는 {test_acc}%로 크게 떨어졌습니다. 이 모델의 현재 상태를 설명하는 가장 정확한 용어는 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "과대적합(Overfitting)은 모델이 훈련 데이터의 노이즈까지 '암기'해 훈련 성능은 높지만 새로운 데이터(Test)에서는 형편없는 현상입니다. 원인: 모델이 너무 복잡하거나(예: Decision Tree depth 무제한), 훈련 데이터가 너무 적거나, 훈련을 너무 오래 한 경우입니다. 해결책: 모델 복잡도 제한(max_depth, max_features), 교차 검증(Cross Validation), 규제(Regularization), 더 많은 훈련 데이터 수집 또는 데이터 증강(Augmentation)이 있습니다.",
        'force_type': 'radio'
    }

def gen_hard_scaling_necessity():
    ans = "랜덤 포레스트(Random Forest) 및 결정 트리(Decision Tree) 등 트리 기반 모델"
    wrongs = [
        "K-최근접 이웃(KNN, K-Nearest Neighbors)",
        "서포트 벡터 머신(SVM)",
        "로지스틱 회귀(Logistic Regression)"
    ]
    return {
        'topic': '[4] 데이터 전처리 - 스케일링 필요성 비교',
        'question': "머신러닝 알고리즘 중 값의 크기 차이(Scale)에 영향을 덜 받아 데이터 스케일링(Standardization, Normalization 등)이 필수적으로 요구되지 않는 알고리즘 계열은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "거리 기반 모델(KNN, SVM)과 경사하강법 기반 모델(선형 회귀, 로지스틱 회귀, 신경망)은 변수의 스케일에 민감합니다 — '연봉(1억)'과 '나이(30)' 같이 범위가 다르면 연봉이 거리 계산을 완전히 지배합니다. 반면 Decision Tree와 Random Forest는 각 변수의 특정 값(임계값)을 기준으로 분기할 뿐, 변수 간 크기를 비교하지 않습니다. 따라서 트리 기반 모델은 스케일링 없이도 잘 작동하며, 스케일링이 필요하지 않다는 것이 속도와 해석 측면에서 강점 중 하나입니다.",
        'force_type': 'radio'
    }

def gen_hard_imputation_strategy():
    domain = random.choice(["직원들의 연봉", "고객들의 자산", "부동산 주택 가격", "인터넷 쇼핑몰 결제액"])
    ans = "중앙값(Median)으로 결측치 채우기"
    wrongs = [
        "평균값(Mean)으로 결측치 채우기",
        "최빈값(Mode)으로 결측치 채우기",
        "0으로 일괄 대체하기"
    ]
    return {
        'topic': '[4] 데이터 전처리 - 결측치 처리 전략',
        'question': f"'{domain}' 데이터를 분석하던 중 일부 데이터에 결측치가 발견되었습니다. 이 데이터의 분포는 극단적으로 큰 값(초고소득자 등 이상치)이 소수 존재하여 한쪽으로 꼬리가 긴 비대칭 형태(Skewed)를 보입니다. 결측치를 단일 대푯값으로 대체할 때, 평균 왜곡을 방지하기 위한 가장 안전한 대체 방법은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "평균(Mean)은 이상치에 취약합니다 — 연봉 데이터에서 재벌 한 명의 1조원 연봉이 평균을 10억 이상으로 끌어올려, 나머지 99%의 실제 연봉 중심과 크게 벗어날 수 있습니다. 중앙값(Median)은 데이터를 크기순으로 정렬했을 때 정중앙 값으로, 이상치가 아무리 극단적이어도 영향을 받지 않습니다. 따라서 이상치가 있거나 분포가 한쪽으로 치우진(Skewed) 데이터에서는 Median으로 결측치를 채우는 것이 훨씬 안정적입니다.",
        'force_type': 'radio'
    }

def gen_hard_imbalanced_accuracy():
    fraud_pct = random.randint(1, 5)
    ans = "데이터의 클래스 불균형(Imbalance) 문제 때문에, 정확도(Accuracy)만으로는 모델의 실제 탐지 능력을 판단할 수 없다."
    wrongs = [
        f"모델이 과소적합(Underfitting)되었으므로 훈련을 더 진행하면 정상 사기 탐지가 가능하다.",
        f"모델 성능이 훌륭하므로 즉시 실무에 배포해도 무방하다.",
        f"데이터가 {100-fraud_pct}%로 쏠려 있으므로 사기 건수를 삭제하여 양쪽을 모두 0건으로 맞춰야 한다."
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 불균형 데이터 평가지표 (정확도의 역설)',
        'question': f"전체 결제 데이터 중 정상 결제가 {100-fraud_pct}%, 사기 결제가 {fraud_pct}%인 데이터를 분류하는 모델을 만들었습니다. 이 모델에 테스트 데이터를 넣었더니 정확도(Accuracy)가 {100-fraud_pct}%가 나왔습니다. 이에 대한 설명으로 가장 적절한 방법론적 컨셉은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "이것이 '정확도의 역설(Accuracy Paradox)'입니다. 사기 거래가 1%인 데이터에서 모델이 '무조건 정상'이라고만 예측해도 정확도 99%가 나옵니다. 하지만 이 모델은 사기를 단 한 건도 탐지하지 못합니다. 이런 불균형 데이터에서는 Precision(정밀도), Recall(재현율), F1-Score를 사용해야 합니다. F1-Score = 2 × (Precision × Recall) / (Precision + Recall)로, 두 지표의 조화 평균입니다. '정상'만 예측하는 모델은 Recall=0으로 즉시 탄로납니다.",
        'force_type': 'radio'
    }

def gen_killer_bagging_boosting():
    ans = "배깅(Bagging)은 병렬로 독립적인 트리를 학습하여 분산(Variance)을 줄이고, 부스팅(Boosting)은 순차적으로 이전 트리의 오차를 보완하며 편향(Bias)을 줄인다."
    wrongs = [
        "배깅(Bagging)은 순차적으로 독립적인 트리를 학습하고, 부스팅(Boosting)은 병렬로 이전 모델을 보완한다.",
        "배깅(Bagging)과 부스팅(Boosting) 모두 모델의 편향(Bias)을 줄이는 데만 목적이 있다.",
        "배깅(Bagging)은 가중치를 부여하는 방식이고, 부스팅(Boosting)은 복원 추출(Bootstrap) 방식이다."
    ]
    return {
        'topic': '[8] 머신러닝 기초 - 킬러 - 앙상블 (Bagging vs Boosting)',
        'question': "대표적인 앙상블(Ensemble) 기법인 배깅(Bagging)과 부스팅(Boosting)의 차이점 및 주된 컨셉을 가장 올바르게 설명한 것을 고르시오.",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "배깅(Bagging, Bootstrap Aggregating): 원본 데이터를 복원 추출하여 여러 데이터셋을 만들고, 각각 독립적으로 모델을 병렬 학습합니다. 각 모델이 서로 다른 데이터의 부분집합을 보기 때문에 분산(Variance)이 줄어들어 과적합이 완화됩니다. Random Forest가 대표 예입니다. 부스팅(Boosting): 이전 모델이 틀린 샘플에 더 높은 가중치를 주며 순차적으로 모델을 추가합니다. 편향(Bias)을 줄이는 데 강하지만, 순차적 특성상 배깅보다 학습이 느리고 이상치에 더 민감합니다. XGBoost, LightGBM이 대표 예입니다.",
        'force_type': 'radio'
    }

def gen_killer_encoding_strategy():
    domain_type = random.choice([
        ("혈액형(A, B, O, AB), 성별", "One-hot Encoding (원핫 인코딩)", "명목형(순서나 우열이 없는) 데이터이기 때문에 숫자 크기에 의미를 부여해선 안 되므로"),
        ("학력(초졸, 중졸, 고졸, 대졸), 만족도(1~5)", "Label Encoding (라벨 인코딩)", "순서형(Ordinal) 데이터이므로 카테고리 간의 대소(순서) 관계를 보존해야 하므로")
    ])
    category_examples, ans, reason = domain_type
    
    wrongs = ["One-hot Encoding (원핫 인코딩)", "Label Encoding (라벨 인코딩)", "Scaling (스케일링)", "Mean Encoding (평균 인코딩)"]
    if ans in wrongs: wrongs.remove(ans)
    random.shuffle(wrongs)
    
    return {
        'topic': '[4] 데이터 전처리 - 킬러 - 범주형 데이터 인코딩',
        'question': f"머신러닝 모델 학습을 위해 범주형 변수를 숫자형으로 변환하려고 합니다. 변수의 특성이 '{category_examples}'과 같을 때 가장 권장되는 인코딩 방법론과 그 컨셉적 이유는 무엇입니까?",
        'expected': f"{ans} : {reason}",
        'wrongs': [
            f"{wrongs[0]} : 순서나 의미와 관계없이 가장 계산이 빠르므로",
            f"{wrongs[1]} : 다중공선성(Multicollinearity)을 완벽히 방지할 수 있으므로",
            f"{wrongs[2]} : 트리 기반 알고리즘에서는 무조건적으로 이 방식을 강제하므로"
        ],
        'explanation': "인코딩 전략은 범주 간 순서 관계 유무에 따라 결정됩니다. 명목형(Nominal): 혈액형, 색깔처럼 순서나 크기 의미가 없는 범주 → Label Encoding을 쓰면 A=0, B=1, O=2처럼 숫자를 부여하는데, 모델이 A < B < O라는 잘못된 순서 관계를 학습할 수 있습니다 → One-hot Encoding을 써야 합니다. 순서형(Ordinal): 초졸/중졸/고졸/대졸처럼 순서가 있는 범주 → Label Encoding으로 0, 1, 2, 3을 부여해도 순서 정보가 보존됩니다. 잘못된 인코딩은 모델이 틀린 전제를 학습하게 만들어 성능 저하로 이어집니다.",
        'force_type': 'radio'
    }

def gen_hard_return_type_series_df():
    col = random.choice(["'age'", "'salary'", "'score'"])
    ans = f"df[{col}]는 Series, df[[{col}]]는 DataFrame을 반환한다."
    wrongs = [
        f"둘 다 DataFrame을 반환한다.",
        f"둘 다 Series를 반환한다.",
        f"df[{col}]는 DataFrame, df[[{col}]]는 Series를 반환한다."
    ]
    return {
        'topic': '[3] 데이터 추출 및 확인 - Series vs DataFrame 반환 타입',
        'question': f"Pandas 데이터프레임 df에서 단일 컬럼을 추출할 때, df[{col}] 구문과 df[[{col}]] 구문의 반환(Return) 데이터 타입 차이에 대한 설명으로 올바른 것은?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "df['컬럼명']은 해당 컬럼을 1차원 구조인 Series로 반환합니다. Series는 인덱스를 공유하지만 단일 열입니다. df[['컬럼명']]처럼 이중 대괄호를 사용하면 2차원 구조인 DataFrame으로 반환됩니다. 이 차이가 왜 중요한가: Scikit-learn 모델의 fit(X, y)에서 X는 DataFrame(2D), y는 Series(1D)이어야 합니다. 잘못된 타입을 넣으면 에러가 발생하거나 경고가 뜨므로, 코드 작성 전에 반환 타입을 의식하는 습관이 중요합니다.",
        'force_type': 'radio'
    }

def gen_hard_scaler_return_type():
    scaler = random.choice(["StandardScaler", "MinMaxScaler", "RobustScaler"])
    ans = "Numpy ndarray 타입으로 반환되어, 기존 DataFrame의 컬럼명과 인덱스 정보가 모두 사라진다."
    wrongs = [
        "입력된 DataFrame의 컬럼명과 인덱스를 그대로 유지한 채 DataFrame으로 반환된다.",
        "데이터는 DataFrame으로 유지되지만, 컬럼명이 'scaled_1', 'scaled_2' 등으로 자동 변경된다.",
        "Python 기본 리스트(List) 타입의 중첩 구조로 반환된다."
    ]
    return {
        'topic': '[4] 데이터 전처리 - Scikit-learn 스케일러 반환 타입',
        'question': f"Scikit-learn의 {scaler}() 객체를 생성하고, 데이터프레임 df에 .fit_transform(df)를 적용했을 때 출력되는 결과물의 데이터 타입(Type)과 구조적 특징으로 올바른 것은?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "Scikit-learn의 Transformer들(StandardScaler, PCA, OneHotEncoder 등)은 fit_transform() 결과를 Numpy ndarray(배열)로 반환합니다. 이 과정에서 원래 DataFrame의 컬럼명과 인덱스가 사라집니다. 따라서 스케일링 후 다시 Pandas 기능을 사용하려면 pd.DataFrame(scaled_arr, columns=df.columns, index=df.index)로 감싸서 DataFrame으로 복원해야 합니다. sklearn Pipeline을 사용하면 이 변환 과정이 자동 관리되어 이 문제를 깔끔하게 해결할 수 있습니다.",
        'force_type': 'radio'
    }

def gen_hard_groupby_as_index():
    col1 = random.choice(["department", "region", "category"])
    col2 = random.choice(["salary", "sales", "price"])
    ans = f"그룹화 기준이 된 '{col1}' 컬럼이 인덱스로 들어가지 않고 일반 컬럼(Column)으로 그대로 유지된다."
    wrongs = [
        f"'{col1}' 컬럼이 인덱스로 지정되며, 기존 인덱스는 모두 초기화된다.",
        f"통계 집계 결과인 '{col2}'의 값이 DataFrame의 인덱스로 지정된다.",
        f"출력 결과가 DataFrame이 아닌 Series로 강제 변환된다."
    ]
    return {
        'topic': '[5] 데이터 집계 - groupby as_index 파라미터',
        'question': f"Pandas에서 df.groupby('{col1}', as_index=False)['{col2}'].mean() 코드를 실행했을 때, 파라미터 s_index=False가 출력 결과에 미치는 구조적 컨셉은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "groupby()의 기본 동작(as_index=True)은 그룹 기준 컬럼을 결과의 인덱스로 지정합니다. 이 상태로 추가 Pandas 연산을 하려면 .reset_index()로 인덱스를 다시 컬럼으로 내려야 할 때가 많습니다. as_index=False를 주면 처음부터 기준 컬럼이 일반 컬럼(Column)으로 유지된 DataFrame이 반환됩니다 — SQL의 GROUP BY 결과와 동일한 형태입니다. 실무에서는 이후 merge나 pivot 등에 연결할 때 as_index=False가 더 편리합니다.",
        'force_type': 'radio'
    }

def gen_hard_drop_duplicates_keep():
    keep_param, effect = random.choice([
        ("keep='last'", "마지막으로 발견된 중복 행만 남기고 이전 행들을 모두 삭제한다."),
        ("keep=False", "중복이 한 번이라도 발생한 모든 행을 남김없이 전부 삭제한다.")
    ])
    ans = effect
    wrongs = [
        "가장 처음에 발견된 중복 행만 남기고 이후 행들을 모두 삭제한다.",
        "결측치(NaN)가 포함된 행만 우선적으로 검색하여 삭제한다."
    ]
    if "마지막으로 발견된" not in effect: wrongs.append("마지막으로 발견된 중복 행만 남기고 이전 행들을 모두 삭제한다.")
    if "남김없이 전부 삭제" not in effect: wrongs.append("중복이 한 번이라도 발생한 모든 행을 남김없이 전부 삭제한다.")
    random.shuffle(wrongs)
    return {
        'topic': '[4] 데이터 전처리 - drop_duplicates 파라미터 컨셉',
        'question': f"Pandas의 중복 데이터 제거 함수인 df.drop_duplicates({keep_param})를 호출했을 때, 이 파라미터 설정이 의미하는 동작 방식은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs[:3],
        'explanation': "drop_duplicates()는 중복 행을 제거합니다. keep 파라미터: 'first'(기본값)는 첫 번째 등장한 행을 남기고 이후 중복을 삭제합니다. 'last'는 반대로 마지막에 등장한 행을 남깁니다. keep=False는 중복이 하나라도 있는 모든 행을 전부 삭제하는 강력한 옵션입니다. 실무 팁: 데이터베이스 JOIN 오류로 중복 행이 생겼을 때, keep=False로 완전한 중복을 제거하거나, 특정 컬럼(subset)만 기준으로 중복 판별도 가능합니다.",
        'force_type': 'radio'
    }

def gen_killer_apply_lambda_axis():
    ans = "각 '행(Row)' 단위로 데이터를 순회하며, 변수 x에는 하나의 행(Row)에 속한 모든 컬럼 값들이 Series 형태로 담겨 전달된다."
    wrongs = [
        "각 '열(Column)' 단위로 데이터를 순회하며, 변수 x에는 하나의 열(Column) 전체 데이터가 배열로 전달된다.",
        "데이터프레임의 '모든 단일 셀(Cell)'을 하나씩 순회하며, 변수 x에는 개별 스칼라(Scalar) 값이 전달된다.",
        "각 '행(Row)' 단위로 순회하지만, 반환 결과는 원본 데이터프레임을 덮어쓰는 inplace 형태로 동작한다."
    ]
    return {
        'topic': '[4] 데이터 전처리 - 킬러 - apply 함수와 axis 컨셉',
        'question': "Pandas에서 여러 컬럼의 값을 동시에 활용하여 새로운 파생 변수를 만들기 위해 df.apply(lambda x: x['A'] + x['B'], axis=1) 코드를 실행했습니다. 이때 파라미터 xis=1이 의미하는 동작 컨셉으로 가장 정확한 것은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "통계 함수(mean, sum)에서 axis=1은 '각 행에 대해 열 방향으로 연산'을 의미합니다 — 예: df.mean(axis=1)은 각 행의 평균. 하지만 apply(..., axis=1)에서 axis=1의 의미는 완전히 다릅니다: '함수를 행(Row) 단위로 순회한다'는 뜻입니다. 즉 lambda x에서 x는 한 행 전체가 Series로 전달되어, x['A'], x['B']처럼 컬럼명으로 접근 가능합니다. 이 패턴은 여러 컬럼의 값을 동시에 참조해서 새 파생 변수를 만들 때 매우 강력합니다.",
        'force_type': 'radio'
    }


class QuizStrategy:
    def __init__(self, id, name, description, easy_pool, hard_pool, killer_pool=None):
        self.id = id
        self.name = name
        self.description = description
        self.easy_pool = easy_pool
        self.hard_pool = hard_pool
        self.killer_pool = killer_pool or []

def gen_easy_while_loop():
    limit = random.randint(3, 6)
    ans = "".join(str(i) for i in range(limit))
    wrongs = ["".join(str(i) for i in range(limit+1)), "".join(str(i) for i in range(1, limit)), "".join(str(i) for i in range(1, limit+1)), "".join(str(i) for i in range(limit-1))]
    return {
        'topic': '[1] 파이썬 Basic - 파이썬 기초 (반복문)', 
        'question': f"다음 코드의 실행 결과로 올바른 것을 고르시오.\n\n```python\ncount = 0\nwhile count < {limit}:\n    print(count, end='')\n    count += 1\n```",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"while 반복문은 count가 0부터 {limit-1}일 때 실행되며 연속 출력됩니다.",
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
        'explanation': "스케일링은 서로 다른 단위와 범위를 가진 변수들의 범위를 일정하게 맞추기 위해 수행합니다.",
        'force_type': 'radio'
    }

def gen_easy_iloc_slicing():
    df_name = random.choice(["df", "data_df"])
    end = random.randint(2, 5)
    ans = f"{df_name}.iloc[0:{end}]"
    wrongs = [f"{df_name}.loc[0:{end}]", f"{df_name}.iloc[0:{end-1}]", f'{df_name}.loc["A"]']
    return {
        'topic': '[1] 파이썬 Basic - 데이터프레임 슬라이싱 (iloc)', 
        'question': f"데이터프레임 {df_name}에서 인덱스 위치 기준 0번부터 {end-1}번까지 정확히 선택하는 코드로 올바른 것을 고르시오.\n\n(단, 인덱스는 기본 RangeIndex를 사용함)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"iloc[0:{end}]는 위치 기반 인덱싱으로 0번째부터 {end-1}번째까지 행을 선택합니다.",
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
    x_test_var = random.choice(["X_test", "features_test", "test_X"])
    ans = x_test_var
    wrongs = ["X_train", "y_test", "X", "Y"]
    return {
        'topic': '[8] 머신러닝 기초 - 모델 예측 API', 
        'question': f"다음 코드에서 결정 트리 모델을 학습시키고, 테스트 데이터에 대한 예측을 수행하려고 합니다. 빈칸에 들어갈 코드로 가장 적절한 것을 고르시오.\n\n```python\ntree = DecisionTreeClassifier()\ntree.fit(X_train, y_train)\n\ny_pred = tree.predict(________)\n```\n(단, 테스트 피처 변수명은 `{x_test_var}`입니다.)",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "모델 학습(fit)에는 훈련 데이터가 사용되고, 예측(predict)에는 테스트 데이터 피처를 제공해야 합니다.",
        'force_type': 'radio'
    }

def gen_hard_confusion_matrix():
    ans = "Confusion Matrix"
    wrongs = ["Feature Importance", "Hyperparameter Tuning", "Data Scaling", "Normalization"]
    return {
        'topic': '[8] 머신러닝 기초 - 모델 평가 지표', 
        'question': "Scikit-Learn에서 분류 모델의 학습 성능을 평가하기 위해 사용할 수 있는 방법 중 하나로 가장 적절한 것을 고르시오.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "Confusion Matrix(혼동 행렬)는 분류 모델의 정답과 오답 패턴을 파악하여 정확도, 정밀도, 재현율 등을 도출하는 평가 도구입니다.",
        'force_type': 'radio'
    }





def gen_py_list_comprehension():
    limit = random.choice([10, 20, 50])
    cond = random.choice(['짝수(even)', '홀수(odd)', '3의 배수'])
    if cond == '짝수(even)':
        ans = f'[x for x in range({limit}) if x % 2 == 0]'
    elif cond == '홀수(odd)':
        ans = f'[x for x in range({limit}) if x % 2 != 0]'
    else:
        ans = f'[x for x in range({limit}) if x % 3 == 0]'
    wrongs = [f'[x if x%2==0 for x in range({limit})]', f'list(filter(lambda x: x%2==0, range({limit})))', f'[x for x in range(1,{limit}) if x%2==0]']
    return {
        'topic': '[1] 파이썬 Basic - 리스트 컴프리헨션',
        'question': f'range(0, {limit}) 중 {cond}만 골라 리스트로 만드는 가장 파이썬다운(Pythonic) 코드를 고르시오.',
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "리스트 컴프리헨션 [표현식 for 변수 in 이터러블 if 조건]은 파이썬다운(Pythonic) 방식으로 리스트를 생성합니다. for 반복문보다 코드가 짧고 일반적으로 더 빠릅니다. filter() 함수도 같은 역할을 하지만 가독성이 낮습니다. 주의: 조건식 위치가 중요합니다 — [x if 조건 else 다른값 for x in range(n)]처럼 if를 for 앞에 두면 삼항연산자(조건부 표현식)가 되어 의미가 완전히 달라집니다.",
        'force_type': 'radio'
    }

def gen_py_dict_operations():
    ops = random.choice([('keys()', '딕셔너리의 모든 키', "dict_keys(['a','b','c'])"), ('values()', '딕셔너리의 모든 값', "dict_values([1,2,3])"), ('items()', '키와 값의 쌍을 튜플로', "dict_items([('a',1),('b',2)])")])
    return {
        'topic': '[1] 파이썬 Basic - 딕셔너리 메서드',
        'question': f'딕셔너리 d = {{"a":1, "b":2, "c":3}}에서 {ops[1]}를 가져오는 메서드와 그 반환 형태로 올바른 것은?',
        'expected': f'd.{ops[0]} → {ops[2]}',
        'wrongs': [
            f'd.{ops[0]} → list',
            f'd.get_{ops[0]} → {ops[2]}',
            f'd.{ops[1]} → {ops[2]}'
        ],
        'explanation': "딕셔너리의 세 가지 핵심 메서드: .keys()는 모든 키의 뷰, .values()는 모든 값의 뷰, .items()는 (키, 값) 튜플 쌍의 뷰를 반환합니다. for k, v in d.items()처럼 언패킹(Unpacking)하면 키와 값을 동시에 순회할 수 있습니다. 실무에서 딕셔너리는 Series.map()과 함께 쓰여 범주형 데이터를 다른 값으로 치환하는 데 자주 활용됩니다 — 예: df['등급'].map({'A': 4.0, 'B': 3.0, 'C': 2.0}).",
        'force_type': 'radio'
    }

def gen_easy_drop_column():
    col = random.choice(['age','city','memo','unused'])
    df = random.choice(['df','data','records'])
    return {
        'topic': '[2] 데이터 로드 및 탐색 - 컬럼 삭제 (axis)',
        'question': f'데이터프레임 `{df}`에서 `{col}` 컬럼을 삭제하는 코드로 올바른 것은? (단, axis=1은 열 방향, axis=0은 행 방향을 의미)',
        'expected': f"{df}.drop('{col}', axis=1)",
        'wrongs': [f"{df}.drop('{col}', axis=0)", f"{df}.remove('{col}')", f"del {df}['{col}']; {df}"],
        'explanation': "df.drop('컬럼명', axis=1)은 열(Column)을 삭제합니다. axis=1은 열 방향, axis=0은 행 방향입니다 — 헷갈리는 이유: DataFrame은 2차원 구조라 방향이 두 가지입니다. axis=0으로 실수하면 해당 컬럼이 아닌 행이 삭제되어 데이터가 예상치 못하게 사라집니다. 여러 컬럼을 동시에 삭제하려면 리스트로 전달합니다: df.drop(['col1', 'col2'], axis=1). inplace=True를 주면 원본을 직접 수정하고 None을 반환합니다.",
        'force_type': 'radio'
    }

def gen_easy_sort_values():
    col = random.choice(['score','sales','date','price'])
    df = random.choice(['df','data','records'])
    asc = random.choice([True, False])
    return {
        'topic': '[3] 데이터 추출 및 확인 - 정렬 (sort_values)',
        'question': f"데이터프레임 `{df}`을(를) '{col}' 컬럼 기준으로 오름차순={asc}으로 정렬하는 코드를 작성하세요.",
        'expected': f"{df}.sort_values('{col}', ascending={asc})",
        'wrongs': [f"{df}.sort('{col}', ascending={asc})", f"{df}.sort_values('{col}')", f"{df}.orderby('{col}', ascending={asc})"],
        'explanation': "sort_values()는 특정 컬럼 기준으로 DataFrame을 정렬합니다. ascending=True(기본값)는 오름차순, ascending=False는 내림차순입니다. 여러 컬럼 기준으로 정렬하려면 리스트로 전달합니다: df.sort_values(['부서', '연봉'], ascending=[True, False]). 주의: 정렬 후 인덱스가 뒤섞이므로, 이후 iloc 접근이 필요하다면 .reset_index(drop=True)로 인덱스를 재정렬해야 합니다.",
        'check': lambda x: "sort_values" in x and col in x and str(asc) in x
    }

def gen_easy_describe():
    return {
        'topic': '[2] 데이터 로드 및 탐색 - describe() 통계 탐색',
        'question': 'df.describe()의 출력에 포함되지 않는 통계량은?',
        'expected': '최빈값(Mode)',
        'wrongs': ['표준편차(std)', '중앙값(50%)', '최솟값(min)'],
        'explanation': "describe()는 수치형 컬럼의 통계 요약(count, mean, std, min, 25%, 50%, 75%, max)을 한 번에 보여줍니다. 여기서 포함되지 않는 값이 최빈값(Mode)입니다 — Mode는 별도로 df['컬럼'].mode()로 확인해야 합니다. describe()에서 주목할 점: mean과 50%(중앙값) 차이가 크면 이상치나 왜도(Skew)가 있다는 신호이며, min과 25% 사이 범위가 비정상적으로 넓으면 이상치 존재를 의심해야 합니다.",
        'force_type': 'radio'
    }

def gen_easy_concat():
    axis_val = random.choice([0, 1])
    axis_desc = '행 방향(아래로 이어 붙이기)' if axis_val==0 else '열 방향(옆으로 이어 붙이기)'
    df1 = random.choice(['df1','left','train'])
    df2 = random.choice(['df2','right','test'])
    return {
        'topic': '[6] 데이터 병합 - pd.concat 기초',
        'question': f"데이터프레임 `{df1}`와 `{df2}`를 {axis_desc} 위해 결합하는 코드로 올바른 것은?",
        'expected': f'pd.concat([{df1}, {df2}], axis={axis_val})',
        'wrongs': [f'pd.merge({df1}, {df2})', f'pd.concat([{df1}, {df2}], axis={1-axis_val})', f'{df1}.append({df2})'],
        'explanation': "pd.concat()은 DataFrame을 이어 붙입니다. axis=0(기본값)은 행 방향으로 아래에 이어 붙이기(행 수 증가), axis=1은 열 방향으로 옆에 붙이기(컬럼 수 증가)입니다. pd.merge()와의 차이: merge는 공통 키 컬럼을 기준으로 관계형 조인을 수행하고, concat은 그냥 물리적으로 이어 붙입니다. 주의: axis=0으로 합칠 때 컬럼명이 다르면 NaN이 채워지므로, 합치기 전 양쪽 컬럼명이 동일한지 확인이 필요합니다.",
        'force_type': 'radio'
    }

def gen_easy_corr():
    return {
        'topic': '[7] EDA 및 시각화 - 상관관계 분석',
        'question': '두 변수 간의 피어슨 상관계수(Pearson Correlation)에 대한 설명으로 올바른 것은?',
        'expected': '값의 범위는 -1에서 +1이며, -1에 가까울수록 강한 음의 선형 관계를 의미한다.',
        'wrongs': ['값의 범위는 0에서 1이며, 0이 완전한 선형 관계를 의미한다.', '두 변수의 인과관계(Causality)를 직접적으로 증명하는 지표다.', '값이 0이면 두 변수 사이에 어떠한 관계도 없음을 확정한다.'],
        'explanation': "피어슨 상관계수(Pearson Correlation)는 두 연속형 변수 사이의 선형 관계 강도를 -1에서 +1로 수치화합니다. +1에 가까울수록 강한 양의 선형 관계(하나 오르면 다른 것도 오름), -1에 가까울수록 강한 음의 관계, 0에 가까울수록 선형 관계 없음입니다. 중요한 주의사항: 상관계수는 선형 관계만 측정하며, 0이어도 비선형 관계(예: U자형)는 존재할 수 있습니다. 또한 상관관계는 인과관계를 의미하지 않습니다.",
        'force_type': 'radio'
    }

def gen_hard_ml_eda_sequence():
    return {
        'topic': '[8] 머신러닝 기초 - ML 프로젝트 전체 시퀀스',
        'question': 'ML 프로젝트의 올바른 진행 순서',
        'expected': 'EDA(탐색) → 결측치/이상치 처리 → Feature Engineering → Train/Test 분할 → 모델 학습(fit) → 성능 평가',
        'wrongs': ['Train/Test 분할 → EDA → 결측치 처리 → 모델 학습 → Feature Engineering → 성능 평가', 'EDA → Feature Engineering → 모델 학습 → Train/Test 분할 → 성능 평가', '결측치 처리 → 모델 학습 → EDA → Train/Test 분할 → Feature Engineering → 성능 평가'],
        'explanation': "올바른 ML 순서에서 가장 중요한 원칙: Train/Test Split은 모든 전처리 이전에 수행해야 합니다. EDA는 데이터 전체를 보며 인사이트를 얻어도 되지만, 실제 결측치 대체값(평균/중앙값) 계산, 스케일링 기준(mean/std) 등은 반드시 Train 데이터로만 fit해야 합니다. 분할 전에 전처리하면 Test 데이터의 통계 정보가 전처리 기준에 스며들어 데이터 누수(Data Leakage)가 발생합니다. 이 순서를 어기면 테스트 성능이 실제보다 과장됩니다.",
        'force_type': 'radio'
    }

def gen_hard_fit_vs_fit_transform():
    scaler = random.choice(['StandardScaler', 'MinMaxScaler'])
    return {
        'topic': '[4] 데이터 전처리 - fit/fit_transform/transform 구분',
        'question': 'Train 데이터와 Test 데이터에 스케일러를 적용하는 올바른 방법',
        'expected': f'Train에는 scaler.fit_transform(X_train), Test에는 scaler.transform(X_test)를 사용한다.',
        'wrongs': ['두 데이터 모두 scaler.fit_transform()을 사용해야 스케일이 정확하게 맞춰진다.', 'Train에는 scaler.fit(), Test에는 scaler.fit_transform()을 사용한다.', '두 데이터 모두 scaler.transform()만 사용하면 자동으로 학습된다.'],
        'explanation': "fit()은 데이터의 통계(평균, 표준편차 등)를 스케일러에 '기억'시키는 과정입니다. fit_transform()은 기억 + 변환을 한 번에 합니다. transform()은 이미 fit된 기준을 사용해 변환만 수행합니다. Test 데이터에 fit()을 다시 호출하면 안 되는 이유: 실제 배포 환경에서는 미래의 Test 데이터 통계를 사전에 알 수 없습니다. Train으로 학습된 스케일 기준을 Test에도 동일하게 적용해야 일관성이 유지됩니다.",
        'force_type': 'radio'
    }

def gen_hard_decision_tree_depth():
    depth = random.choice([1, 2, 3])
    return {
        'topic': '[8] 머신러닝 기초 - Decision Tree max_depth 트레이드오프',
        'question': f'max_depth=None(기본값)인 Decision Tree와 max_depth={depth}인 경우의 차이',
        'expected': 'max_depth=None이면 모든 리프 노드의 불순도(Impurity)가 0이 될 때까지 분기하여 훈련 데이터에 과적합(Overfitting)된다.',
        'wrongs': ['max_depth=None이면 분기를 전혀 하지 않아 항상 최빈 클래스만 예측한다.', f'max_depth={depth}이면 항상 더 높은 정확도를 보장한다.', 'max_depth 값이 클수록 과소적합(Underfitting)에 가까워진다.'],
        'explanation': "Decision Tree는 max_depth를 제한하지 않으면 모든 리프 노드의 불순도(Gini/Entropy)가 0이 될 때까지 계속 분기합니다 — 결국 훈련 데이터의 모든 패턴(노이즈 포함)을 암기하여 훈련 정확도 100%가 되지만, 새 데이터에는 형편없습니다. max_depth를 작게 설정할수록 단순한 모델(과소적합 위험), 크게 설정할수록 복잡한 모델(과적합 위험)이 됩니다. 최적 depth는 Cross Validation으로 탐색하거나, Random Forest처럼 여러 트리의 앙상블로 해결합니다.",
        'force_type': 'radio'
    }

def gen_hard_knn_k_tradeoff():
    k_val = random.choice([1, 3])
    return {
        'topic': '[8] 머신러닝 기초 - KNN K값 과적합/과소적합',
        'question': f'K={k_val}로 설정한 KNN 모델에 대한 설명으로 올바른 것은?',
        'expected': f'K={k_val}은 매우 작은 값으로, 훈련 데이터의 노이즈에 민감하게 반응하여 과적합(Overfitting)이 발생한다.',
        'wrongs': [f'K={k_val}은 매우 작아서 과소적합(Underfitting)이 발생하며 결정 경계가 지나치게 단순해진다.', f'K={k_val}일 때 항상 최적의 성능을 보장한다.', 'KNN에서 K값은 모델 성능에 영향을 주지 않는다.'],
        'explanation': "KNN에서 K는 핵심 하이퍼파라미터입니다. K=1: 가장 가까운 1개의 훈련 데이터를 보므로 훈련 데이터에는 완벽하지만, 노이즈 데이터 하나에도 결정 경계가 요동쳐 과적합(Overfitting)됩니다. K가 매우 큰 경우: 너무 많은 이웃을 보면 결정 경계가 지나치게 단순해져(대부분의 경우 최빈 클래스만 반환), 과소적합(Underfitting)됩니다. 최적 K는 홀수(동점 방지)로 설정하고 Cross Validation으로 탐색합니다.",
        'force_type': 'radio'
    }

def gen_hard_pipeline_why():
    return {
        'topic': '[8] 머신러닝 기초 - sklearn Pipeline 사용 이유',
        'question': 'sklearn Pipeline을 사용하는 핵심 이유',
        'expected': '전처리 단계를 파이프라인에 묶으면, Cross Validation 시 매 Fold마다 훈련 데이터 기준으로만 fit이 적용되어 데이터 누수(Data Leakage)를 원천 차단할 수 있다.',
        'wrongs': ['코드를 짧게 쓸 수 있어 가독성만 높아진다.', 'Pipeline 없이는 sklearn 모델을 사용할 수 없다.', '모델의 정확도를 자동으로 향상시켜 주는 최적화 기능이 있다.'],
        'explanation': "Pipeline이 없을 때의 위험: 수동으로 scaler.fit(X_train) → scaler.transform(X_train) → scaler.transform(X_test) 과정에서 교차 검증(Cross Validation)을 돌리면, 각 fold마다 검증(Validation) 데이터에 대해서도 fit이 실수로 적용될 수 있습니다. Pipeline은 각 step의 fit/transform 타이밍을 자동으로 관리해, CV 시 훈련 fold로만 fit하고 검증 fold에는 transform만 하도록 보장합니다. 이것이 Pipeline을 '모델 배포의 표준'이라 부르는 이유입니다.",
        'force_type': 'radio'
    }

def gen_hard_feature_importance_concept():
    return {
        'topic': '[8] 머신러닝 기초 - Feature Importance 해석',
        'question': '트리 기반 모델의 feature_importances_ 속성에 대한 설명으로 옳은 것은?',
        'expected': '각 변수가 불순도(Gini/Entropy) 감소에 기여한 정도를 나타내며, 스케일(Scale)에 독립적이다.',
        'wrongs': ['수치가 클수록 해당 변수가 타겟과 인과관계(Causality)가 있음을 증명한다.', '스케일링을 적용한 후에만 의미 있는 값을 반환한다.', '모든 변수의 feature importance 합은 100이 된다.'],
        'explanation': "트리 기반 모델의 feature_importances_는 각 피처가 불순도(Gini 또는 Information Gain)를 얼마나 감소시켰는지를 정규화(합=1)하여 수치화한 것입니다. 스케일에 독립적이라 스케일링 없이도 의미 있는 값을 줍니다. 주의사항: 카테고리 수가 많은 범주형 변수(high-cardinality)나 원핫 인코딩으로 여러 컬럼으로 쪼개진 변수는 중요도가 분산되어 실제보다 낮게 보일 수 있습니다. 또한 중요도가 높다고 인과관계가 있는 것은 아닙니다.",
        'force_type': 'radio'
    }

def gen_hard_classification_report():
    tp = random.randint(40, 80)
    fp = random.randint(10, 30)
    fn = random.randint(10, 30)
    precision = round(tp/(tp+fp)*100)
    return {
        'topic': '[8] 머신러닝 기초 - Precision/Recall 수치 계산',
        'question': f'TP={tp}, FP={fp}, FN={fn}일 때 Precision(정밀도)는?',
        'expected': f'{precision}% (모델이 Positive로 예측한 {tp+fp}건 중 실제 Positive {tp}건)',
        'wrongs': [
            f'{round(tp/(tp+fn)*100)}% (모델이 Positive로 예측한 {tp+fn}건 중 실제 Positive {tp}건)',
            f'{round((tp+fp)/(tp+fp+fn)*100)}% (전체 예측 건수 대비 Positive)',
            f'{round(fp/(tp+fp)*100)}% (모델이 Positive로 예측한 {tp+fp}건 중 오답 {fp}건)'
        ],
        'explanation': '정밀도(Precision)는 TP / (TP + FP)로 계산되며, 모델이 Positive로 예측한 것 중 실제 Positive의 비율입니다.',
        'force_type': 'radio'
    }

def gen_hard_logistic_vs_linear():
    scenarios = [('주택 가격 예측', '연속형 수치', '선형 회귀(Linear Regression)'), ('고객 이탈 여부 예측', '이진 범주형(0 또는 1)', '로지스틱 회귀(Logistic Regression)'), ('꽃의 종류 분류(3종)', '다중 범주형', '의사결정나무(Decision Tree) 또는 KNN')]
    scenario = random.choice(scenarios)
    ans = scenario[2]
    wrongs = [s[2] for s in scenarios if s[2] != ans]
    wrongs.append("K-Means 군집화")
    return {
        'topic': '[8] 머신러닝 기초 - 모델 유형 선택 (회귀 vs 분류)',
        'question': f'타겟 변수가 "{scenario[1]}"인 경우 가장 적합한 모델 유형은? (예: {scenario[0]})',
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "모델 선택의 첫 번째 질문은 항상 '타겟(y) 변수의 타입이 무엇인가?'입니다. 타겟이 연속형 숫자(주택 가격, 온도)라면 회귀(Regression) 모델을 사용합니다. 타겟이 이산적인 범주(생존/사망, 스팸/정상, 꽃의 종류)라면 분류(Classification) 모델을 사용합니다. 로지스틱 회귀는 이름에 '회귀'가 있지만 출력이 0~1의 확률값을 임계값(0.5)으로 분류하는 분류 모델입니다. 이 첫 번째 판단을 틀리면 손실 함수, 평가 지표, 코드 모두가 어긋납니다.",
        'force_type': 'radio'
    }

def gen_hard_get_dummies_drop_first():
    return {
        'topic': '[4] 데이터 전처리 - get_dummies drop_first 이유',
        'question': 'pd.get_dummies(df, drop_first=True)에서 drop_first=True를 사용하는 이유',
        'expected': '범주의 수가 k개인 변수를 원핫 인코딩하면 k개 컬럼이 생성되는데, k-1개만으로 정보가 완전히 표현 가능하므로 나머지 1개 제거로 다중공선성(Multicollinearity) 함정을 방지한다.',
        'wrongs': ['첫 번째 컬럼은 무조건 결측치를 의미하기 때문에 모델 학습 시 방해가 되므로 제거한다.', '메모리 사용량을 절반으로 줄여서 학습 속도를 기하급수적으로 높이기 위해서다.', '첫 번째 데이터 포인트(행)를 버려서 아웃라이어를 제거하기 위함이다.'],
        'explanation': "혈액형(A, B, O, AB) 4개를 원핫 인코딩하면 A열, B열, O열, AB열 4개가 생깁니다. 그런데 A+B+O+AB는 항상 1입니다 — 세 개를 알면 나머지 하나는 자동으로 결정됩니다. 이처럼 한 변수가 다른 변수의 선형 조합으로 표현되는 상황을 다중공선성(Multicollinearity)이라 하며, 선형 모델의 계수 추정을 불안정하게 만듭니다. drop_first=True로 첫 번째 더미를 제거하면 k-1개로도 완전히 표현 가능하므로 이 함정을 피할 수 있습니다.",
        'force_type': 'radio'
    }

def gen_hard_model_selection_scenario():
    scenarios = [('고객 구매 여부 예측(구매함/안함)', '분류(Classification)', 'Logistic Regression, Decision Tree, KNN'), ('내일 주가 예측(숫자 값)', '회귀(Regression)', 'Linear Regression, Random Forest Regressor'), ('비슷한 고객 군끼리 그룹화(레이블 없음)', '군집화(Clustering)', 'K-Means, DBSCAN')]
    scenario = random.choice(scenarios)
    ans = scenario[2]
    wrongs = [s[2] for s in scenarios if s[2] != ans]
    wrongs.append("PCA, t-SNE")
    return {
        'topic': '[8] 머신러닝 기초 - 실전 시나리오 모델 선택',
        'question': f'"{scenario[0]}" 문제 해결을 위해 가장 적절한 머신러닝 알고리즘 조합은?',
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "ML 문제 유형 판단 체계: 타겟이 있으면(지도학습) → 범주형이면 분류, 연속형이면 회귀. 타겟이 없으면(비지도학습) → 그룹을 나누면 군집화(K-Means), 차원을 줄이면 차원 축소(PCA). 실전에서 혼동하기 쉬운 케이스: '점수 예측(1~100점)'은 회귀처럼 보이지만 '합격/불합격'으로 변환하면 분류가 됩니다. 문제를 어떻게 정의하느냐에 따라 모델 유형이 바뀌며, 이 정의 자체가 데이터 분석가의 핵심 역량입니다.",
        'force_type': 'radio'
    }

def gen_hard_cross_val_purpose():
    cv = random.choice([5, 10])
    return {
        'topic': '[8] 머신러닝 기초 - K-Fold Cross Validation 목적',
        'question': f'{cv}-Fold Cross Validation을 단순 Train/Test Split 대신 사용하는 핵심 이유',
        'expected': f'데이터를 {cv}번 다르게 분할하여 모델을 반복 평가함으로써, 특정 분할 방식에 의한 우연적 편향 없이 더 신뢰할 수 있는 일반화 성능 추정치를 얻기 위해서',
        'wrongs': ['데이터셋의 크기를 물리적으로 늘려주어 데이터가 적을 때 오버샘플링(Oversampling) 효과를 내기 위해서', '하이퍼파라미터 튜닝 없이도 모델의 정확도를 자동으로 100%에 가깝게 끌어올려 주기 위해서', 'Train 데이터의 노이즈를 완벽하게 제거해주는 전처리 기법이기 때문'],
        'explanation': "단순 Train/Test Split의 문제: 분할 방식에 따라 성능이 크게 달라질 수 있습니다(운의 영향). K-Fold CV는 데이터를 K개로 나눠 K번 학습+검증을 돌려 K개의 성능 점수를 평균내므로, 특정 분할의 우연을 줄여 더 신뢰성 있는 성능 추정이 가능합니다. 추가로 표준편차(std)도 확인하면 모델의 안정성(일관성)도 파악할 수 파악할 수 있습니다. 데이터가 충분치 않을수록 K 값을 크게(예: 10) 설정하는 것이 좋습니다.",
        'force_type': 'radio'
    }

def gen_hard_scaling_method_choice():
    return {
        'topic': '[4] 데이터 전처리 - 스케일러 선택 기준',
        'question': 'MinMaxScaler를 사용했을 때 이상치(Outlier) 1개가 끼치는 영향',
        'expected': '이상치가 min 또는 max 기준점이 되어 나머지 정상 데이터 값이 극단적으로 0 또는 1에 몰리게 된다. 이상치가 많은 경우 RobustScaler가 더 적합하다.',
        'wrongs': ['이상치 여부와 무관하게 모든 데이터가 완벽한 정규분포를 따르게 된다.', '이상치 하나가 스케일링 전체 공식을 망가뜨려 에러를 발생시킨다.', '이상치도 다른 데이터와 동일한 간격으로 축소되어 전혀 문제가 되지 않는다.'],
        'explanation': "MinMaxScaler는 데이터를 [min, max] 범위로 정규화합니다 — 공식: (x - min) / (max - min). 이상치(Outlier)가 하나라도 있으면 그것이 새 min 또는 max가 되어, 나머지 모든 정상 데이터가 0과 1 사이의 아주 좁은 범위로 눌려버립니다. StandardScaler는 평균을 0, 표준편차를 1로 만들지만 이상치에 영향을 받습니다. 이상치가 많을 때 최선의 선택은 중앙값과 IQR을 사용하는 RobustScaler입니다 — 이상치를 무시하고 중간 범위 데이터를 기준으로 스케일링합니다.",
        'force_type': 'radio'
    }

def gen_hard_random_state_purpose():
    val = random.choice([0, 42, 123])
    return {
        'topic': '[8] 머신러닝 기초 - random_state 재현성',
        'question': f'train_test_split(..., random_state={val})을 설정하는 이유',
        'expected': '셔플 과정의 난수 시드(Seed)를 고정하여, 코드를 다시 실행해도 동일한 Train/Test 분할이 재현(Reproducibility)되도록 보장한다.',
        'wrongs': ['무작위 분할 대신 정렬된 상태로 데이터를 순서대로 자르기 위함이다.', '모델의 학습 속도를 높이기 위한 최적화 옵션이다.', '학습할 때마다 다른 데이터를 사용하도록 무작위성을 무한으로 증가시킨다.'],
        'explanation': "머신러닝에서 '재현 가능성(Reproducibility)'은 매우 중요합니다. 코드를 누가, 언제 실행해도 동일한 결과가 나와야 실험이 의미 있습니다. random_state는 파이썬의 난수 생성기 시드(Seed)를 고정하는 파라미터입니다. random_state를 설정하지 않으면 매번 다른 Train/Test 분할이 만들어져, 어제는 정확도 85%, 오늘은 78%처럼 결과가 달라집니다. 팀 협업이나 논문 재현에서는 random_state 명시가 필수적인 코드 관례입니다.",
        'force_type': 'radio'
    }

def gen_hard_confusion_matrix_reading():
    tp = random.randint(50, 90)
    tn = random.randint(50, 90)
    fp = random.randint(5, 20)
    fn = random.randint(5, 20)
    accuracy = round((tp+tn)/(tp+tn+fp+fn)*100, 1)
    precision = round(tp/(tp+fp)*100, 1)
    return {
        'topic': '[8] 머신러닝 기초 - Confusion Matrix 수치 해석',
        'question': f'TP={tp}, TN={tn}, FP={fp}, FN={fn}일 때 다음 중 올바른 것은?',
        'expected': f'정확도(Accuracy) = {accuracy}%, 정밀도(Precision) = {precision}%',
        'wrongs': [
            f'정확도(Accuracy) = {round(tp/(tp+fp)*100, 1)}%, 정밀도(Precision) = {round(tn/(tn+fn)*100, 1)}%',
            f'정확도(Accuracy) = {round((tp+fn)/(tp+tn+fp+fn)*100, 1)}%, 정밀도(Precision) = {round((tp+tn)/(tp+fp)*100, 1)}%',
            f'정확도(Accuracy) = {round(tn/(tp+tn+fp+fn)*100, 1)}%, 정밀도(Precision) = {round(tp/(tp+fn)*100, 1)}%'
        ],
        'explanation': "Confusion Matrix 해석 공식: Precision(정밀도) = TP / (TP + FP), Recall(재현율) = TP / (TP + FN), Accuracy(정확도) = (TP + TN) / 전체. TP(True Positive): 실제 Positive를 Positive로 맞게 예측, TN: 실제 Negative를 Negative로 맞게 예측, FP(False Positive): 실제 Negative를 Positive로 잘못 예측(오탐), FN(False Negative): 실제 Positive를 Negative로 잘못 예측(미탐). FP와 FN 중 어떤 오류가 더 치명적인지에 따라 Precision vs Recall 중 무엇을 최적화할지 결정합니다.",
        'force_type': 'radio'
    }

def gen_hard_multi_condition_filter():
    return {
        'topic': '[3] 데이터 추출 및 확인 - 다중 조건 필터링 함정',
        'question': 'Pandas에서 다중 조건 필터링 시 `and` 대신 `&`를 써야 하는 이유',
        'expected': 'Pandas Boolean Indexing에서 `and`는 Python 스칼라 논리 연산자라 Series에 사용 불가. `&`는 원소별(element-wise) 비트 연산자이며, 조건마다 반드시 ()로 감싸야 한다.',
        'wrongs': ['`and`를 사용하면 에러는 나지 않지만 결과가 항상 False로 나온다.', '`&`는 SQL 문법을 차용한 것으로 `and`와 기능은 완벽히 동일하나 속도가 빠르다.', '`and`는 문자열 필터링에만 사용하고 `&`는 숫자 필터링에만 사용하기 때문이다.'],
        'explanation': "파이썬의 and/or는 스칼라(True/False 하나)에 대한 논리 연산자입니다. Pandas Series는 원소가 여러 개이므로 and/or를 사용하면 'The truth value of a Series is ambiguous' 에러가 발생합니다. 대신 원소별(element-wise) 비트 연산자 &(AND), |(OR), ~(NOT)를 사용해야 합니다. 또한 연산자 우선순위 때문에 각 조건을 ()로 반드시 묶어야 합니다 — 예: (df['A'] > 0) & (df['B'] == 'X'). 괄호 없이 쓰면 예상치 못한 결과가 나옵니다.",
        'force_type': 'radio'
    }

def gen_killer_pipeline_order():
    return {
        'topic': '[8] 머신러닝 기초 - 킬러 - Pipeline 순서',
        'question': 'sklearn Pipeline을 구성할 때 다음 보기 중 올바른 순서를 고르시오.',
        'expected': "Pipeline([('scaler', StandardScaler()), ('pca', PCA(n_components=2)), ('clf', DecisionTreeClassifier())])",
        'wrongs': ["Pipeline([('clf', DecisionTreeClassifier()), ('scaler', StandardScaler()), ('pca', PCA())])", "Pipeline([('pca', PCA()), ('clf', DecisionTreeClassifier()), ('scaler', StandardScaler())])", "Pipeline([('pca', PCA()), ('scaler', StandardScaler()), ('clf', DecisionTreeClassifier())])"],
        'explanation': "sklearn Pipeline의 step 순서는 데이터가 흐르는 순서와 동일합니다. 원칙: 전처리 → 차원 축소 → 모델 순입니다. StandardScaler를 PCA보다 먼저 적용해야 하는 이유: PCA는 분산이 큰 방향으로 주성분을 찾는데, 스케일링 없이 하면 단위가 큰 변수가 분산을 지배해 의미 없는 주성분이 만들어집니다. Classifier는 반드시 마지막에 와야 합니다 — 중간에 모델을 넣으면 이후 transform step이 예측값을 입력으로 받는 비논리적 구조가 됩니다.",
        'force_type': 'radio'
    }

def gen_killer_target_leakage():
    return {
        'topic': '[0] 기타 - 킬러 - 타겟 누수(Target Leakage)',
        'question': 'ML 모델 개발 중 Test 정확도가 비현실적으로 99.8%가 나왔습니다. 원인으로 가장 의심해야 할 것은?',
        'expected': '학습 피처 중에 타겟 변수(미래 정보)가 결정된 이후에야 생성되는 데이터가 포함되어 있을 가능성이 높다. (타겟 누수: Target Leakage)',
        'wrongs': ['하이퍼파라미터가 너무 완벽하게 튜닝되었기 때문이다.', '데이터의 크기가 너무 작아서 발생한 정상적인 현상이다.', 'Cross Validation을 여러 번 반복해서 모델이 테스트 셋을 완벽히 암기했기 때문이다.'],
        'explanation': "타겟 누수(Target Leakage)는 학습 피처 중에 '타겟이 결정된 이후에만 알 수 있는 정보'가 포함된 경우입니다. 예: 신용카드 사기 탐지에서 '사기 신고일' 컬럼을 피처로 사용하면 — 사기가 일어난 후에야 신고하므로, 이 컬럼은 사기 여부와 완벽한 상관관계를 가집니다. 모델이 이것을 '학습'하면 테스트 성능이 비현실적으로 높게 나오지만, 실제 배포 후에는 아직 신고가 없어 이 값이 없으므로 성능이 폭락합니다. 피처를 선택할 때 '이 값이 예측 시점에 실제로 알 수 있는 값인가?'를 반드시 확인해야 합니다.",
        'force_type': 'radio'
    }

def gen_killer_class_imbalance_strategy():
    return {
        'topic': '[8] 머신러닝 기초 - 킬러 - 클래스 불균형 전략',
        'question': '클래스 불균형(Class Imbalance) 해결 전략에 대한 설명 중 가장 올바른 것은?',
        'expected': 'SMOTE는 소수 클래스를 합성 생성하는 오버샘플링 기법으로, 데이터가 충분하지 않을 때 유용하지만 과적합 위험이 있다. class_weight는 모델 자체에 패널티를 부여하는 방식으로 데이터 변형 없이 빠르게 적용 가능하다.',
        'wrongs': ['SMOTE는 다수 클래스의 데이터를 삭제하여 균형을 맞추는 언더샘플링 기법이다.', 'class_weight는 데이터 셋의 소수 클래스 데이터를 실제로 2배 복제해 주는 강력한 파라미터다.', '클래스 불균형 시에는 무조건 오버샘플링을 사용하는 것이 가장 빠르고 완벽한 방법이다.'],
        'explanation': "클래스 불균형 해결 전략 비교: (1) SMOTE(오버샘플링): 소수 클래스 샘플을 보간(Interpolation)하여 합성 데이터를 생성합니다. 데이터가 부족할 때 효과적이지만, 실제 데이터 분포와 다른 인위적 패턴이 생길 수 있습니다. (2) 언더샘플링: 다수 클래스를 줄입니다. 빠르지만 정보 손실이 큽니다. (3) class_weight='balanced': 모델 학습 시 소수 클래스에 더 큰 페널티를 부여합니다 — 데이터를 변형하지 않으므로 가장 안전하며, sklearn 모델 대부분이 지원합니다. 데이터가 충분하다면 class_weight부터 시도하는 것이 실무의 기본 접근법입니다.",
        'force_type': 'radio'
    }
ALL_EASY = [
    gen_py_list_comprehension, gen_py_dict_operations, gen_easy_drop_column, gen_easy_sort_values, gen_easy_describe, gen_easy_concat, gen_easy_corr,     gen_easy_while_loop, gen_easy_list_mutability, gen_easy_scaling_reason, gen_easy_iloc_slicing,
    gen_eda_concept_cat_num,
    gen_easy_read_excel, gen_easy_head, gen_easy_dtypes, gen_easy_isnull, 
    gen_easy_dropna, gen_easy_filter, gen_easy_loc, gen_easy_value_counts,
    gen_viz_countplot, gen_viz_histplot, gen_viz_scatter, gen_sns_boxplot,
    gen_py_str_split, gen_py_list_slice, gen_np_log1p,
    gen_easy_fillna, gen_ml_concept, gen_ml_split_basic
]

ALL_HARD = [
    gen_hard_ml_eda_sequence, gen_hard_fit_vs_fit_transform, gen_hard_decision_tree_depth, gen_hard_knn_k_tradeoff, gen_hard_pipeline_why, gen_hard_feature_importance_concept, gen_hard_classification_report, gen_hard_logistic_vs_linear, gen_hard_get_dummies_drop_first, gen_hard_model_selection_scenario, gen_hard_cross_val_purpose, gen_hard_scaling_method_choice, gen_hard_random_state_purpose, gen_hard_confusion_matrix_reading, gen_hard_multi_condition_filter,     gen_hard_return_type_series_df, gen_hard_scaler_return_type, gen_hard_groupby_as_index, gen_hard_drop_duplicates_keep, gen_hard_data_leakage, gen_hard_ml_sequence, gen_hard_precision_recall, gen_hard_overfitting, gen_hard_scaling_necessity, gen_hard_imputation_strategy, gen_hard_imbalanced_accuracy,     gen_hard_random_forest_concept, gen_hard_train_predict, gen_hard_confusion_matrix,
    gen_eda_concept_num_num,
    gen_hard_apply, gen_hard_groupby, gen_hard_merge, gen_hard_pivot,
    gen_ml_knn, gen_ml_split_stratify, gen_ml_cv
]

ALL_KILLER = [gen_killer_pipeline_order, gen_killer_target_leakage, gen_killer_class_imbalance_strategy, gen_killer_chained_assignment, gen_killer_merge_suffixes, gen_killer_bagging_boosting, gen_killer_encoding_strategy, gen_killer_apply_lambda_axis]

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
        # 중복 출제를 막기 위해 비복원 추출(random.sample) 사용
        actual_count = min(count, len(pool))
        selected_funcs = random.sample(pool, actual_count)
        for f in selected_funcs:
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
            
    if strategy_id == 'bootcamp_day1_4':
        add_questions(easy_pool, 16)
        add_questions(hard_pool, 2)
        add_questions(killer_pool, 2)
    else:
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

def generate_single_quiz(strategy_id='bootcamp_day1_4', topic=None, exclude_funcs=None):
    strategy = get_strategy(strategy_id)
    pool = strategy.easy_pool + strategy.hard_pool
    
    if topic and topic != '전체 랜덤':
        pool = [f for f in pool if f()['topic'] == topic]
        if not pool:
            pool = strategy.easy_pool + strategy.hard_pool
            
    if exclude_funcs:
        filtered_pool = [f for f in pool if f.__name__ not in exclude_funcs]
        if filtered_pool:
            pool = filtered_pool
    
    f = random.choice(pool)
    q = f()
    q['func_name'] = f.__name__
    
    q['type'] = 'radio'
    opts = [q['expected']] + q['wrongs'][:3]
    random.shuffle(opts)
    q['choices'] = opts
    return q
