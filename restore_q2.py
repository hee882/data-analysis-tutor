import os

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
q_path = os.path.join(repo_path, 'src', 'questions.py')

q_part2 = '''def gen_param_nuance_concat():
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

ALL_EASY = [
    gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, 
    gen_easy_fillna, gen_easy_drop, gen_easy_filter,
    gen_viz_bar, gen_viz_scatter, gen_viz_hist,
    gen_py_loop_control, gen_py_str_split, gen_py_list_slice, gen_py_dict_get,
    gen_sns_pairplot, gen_sns_boxplot, gen_np_log1p
]

ALL_HARD = [
    gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt,
    gen_numpy_array, gen_ml_split, gen_ml_rf, gen_viz_sns,
    gen_param_nuance_concat, gen_param_nuance_dropdup,
    gen_ml_knn, gen_ml_stratify
]

STRATEGIES = {
    'bootcamp_day1_4': QuizStrategy(
        id='bootcamp_day1_4',
        name='Day 1~4 Bootcamp (시험 대비)',
        description='단기 부트캠프 진도에 맞춘 핵심 위주의 출제 모드입니다.',
        easy_pool=ALL_EASY,  
        hard_pool=ALL_HARD
    ),
    'comprehensive': QuizStrategy(
        id='comprehensive',
        name='종합 마스터 (전범위 딥다이브)',
        description='모듈화된 모든 라이브러리의 방대한 전범위를 다루는 극한 모드입니다.',
        easy_pool=ALL_EASY,
        hard_pool=ALL_HARD
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
'''

with open(q_path, 'a', encoding='utf-8') as f:
    f.write('\n' + q_part2)

print("Part 2 written!")
