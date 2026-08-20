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
        'explanation': "pd.read_excel() 함수를 사용하여 엑셀 파일을 DataFrame으로 불러옵니다.",
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
        'explanation': f"{df_name}.head({n})을 사용하면 맨 위에서부터 지정한 개수만큼의 데이터를 확인할 수 있습니다.",
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
        'explanation': f"{df_name}.dtypes 속성을 통해 각 열의 데이터 타입을 확인할 수 있습니다.",
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
        'explanation': f"{df_name}.isna().sum() (또는 {df_name}.isnull().sum())을 통해 열별 결측치 개수를 집계합니다.",
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
        'explanation': "dropna() 함수를 사용하여 결측치(NaN)가 포함된 행을 제거할 수 있습니다.",
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
        'explanation': "Boolean Indexing을 활용하여 특정 조건에 맞는 행만 추출할 수 있습니다.",
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
        'explanation': f"{df_name}.loc[행이름, 열이름] 형식으로 라벨 기반 접근을 합니다.",
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
        'explanation': "value_counts() 메서드를 사용하면 범주형 데이터의 빈도를 알 수 있습니다.",
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
        'explanation': "sns.countplot()은 범주형 변수의 빈도수를 보여줍니다.",
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
        'explanation': "수치형 데이터의 분포를 볼 때는 sns.histplot()을 사용합니다.",
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
        'explanation': "수치형 변수 두 개 간의 관계를 산점도로 표현할 때는 sns.scatterplot()을 사용합니다.",
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
        'explanation': "문자열의 .split('구분자') 메서드를 사용하면 리스트를 얻을 수 있습니다.",
        'check': lambda x: "split" in _prep(x) and sep in _prep(x)
    }

def gen_eda_concept_cat_num():
    ans = "sns.boxplot() 또는 sns.barplot()"
    wrongs = ["sns.scatterplot()", "sns.histplot()", "sns.lineplot()"]
    return {
        'topic': '[7] EDA 및 시각화 - EDA 개념 (범주형+수치형 시각화)', 
        'question': "탐색적 데이터 분석(EDA) 과정에서 '범주형 데이터'에 따른 '수치형 데이터'의 차이나 분포를 비교하려고 합니다. 다음 중 가장 적절한 Seaborn 시각화 함수는 무엇일까요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "범주형과 수치형 데이터를 동시에 분석할 때는 boxplot이나 barplot이 가장 적절합니다.",
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
        'explanation': "두 수치형 변수의 관계는 scatterplot을 사용하며, 여러 수치형 변수 간의 관계는 pairplot을 사용합니다.",
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
        'explanation': f"결측치를 대체할 때는 `fillna()`와 `{method}()`를 사용합니다.",
        'check': lambda x: "fillna" in _prep(x) and method in _prep(x)
    }

def gen_ml_concept():
    ans = "분류(Classification)"
    wrongs = ["회귀(Regression)", "군집화(Clustering)", "차원 축소(Dimensionality Reduction)"]
    return {
        'topic': '[8] 머신러닝 기초 - 머신러닝 개념 (지도학습 방법론)', 
        'question': "우리가 예측하려는 타겟(Target) 데이터가 '생존여부(0 또는 1)', '꽃의 종류(Iris-setosa 등)'와 같은 '범주형(Categorical) 데이터'일 때 사용하는 머신러닝 모델링 기법을 무엇이라고 하나요?",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': "타겟이 범주형이면 분류(Classification)를 사용합니다.",
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
        'explanation': "Scikit-learn의 `train_test_split`은 X와 y를 학습용/테스트용으로 나누어주는 함수입니다.",
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
        'explanation': "[start:stop:step] 구조에서 step을 -1로 지정( [::-1] )하면 역순 슬라이싱이 됩니다.",
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
        'explanation': "sns.boxplot()은 데이터의 분포와 이상치를 한눈에 파악하기 좋으며, hue 파라미터를 추가하면 그룹별로 비교할 수 있습니다.",
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
        'explanation': "np.log1p()는 log(1+x)를 의미하여 0일 때의 -inf 오류를 방지합니다.",
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
        'explanation': "Series.apply(함수명)을 사용하면 로직을 반복문 없이 적용할 수 있습니다.",
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
        'explanation': f"df.groupby('그룹기준열')['계산대상열'].통계함수() 형태를 사용합니다.",
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
        'explanation': f"pd.merge() 함수에서 how='{how}' 파라미터를 사용합니다.",
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
        'explanation': "pd.pivot_table()을 사용하면 복수의 카테고리에 대한 통계량을 요약할 수 있습니다.",
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
        'explanation': "KNeighborsClassifier(n_neighbors=K)를 사용합니다.",
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
        'explanation': "stratify=y 파라미터를 지정하면 원래 클래스 분포 비율을 그대로 유지하며 분할합니다.",
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
        'explanation': f"cross_val_score() 함수에 cv={cv_num}를 주어 교차 검증을 수행하고 .mean()을 호출합니다.",
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
        'explanation': "Chained Assignment를 피하려면 반드시 `.loc[행조건, 열이름]`을 사용하여 단일 연산으로 값을 할당해야 합니다.",
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
        'explanation': "`merge`의 기본 동작은 `inner join`이며, `on`을 생략하면 이름이 겹치는 모든 컬럼을 병합 키로 자동 사용합니다. 인덱스 병합은 `left_index=True`, `right_index=True` 옵션으로 `merge`에서도 가능합니다. 공통 컬럼이 병합 키가 아닐 경우 자동으로 접미사가 붙습니다.",
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
