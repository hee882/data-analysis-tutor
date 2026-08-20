import os

with open('src/questions.py', 'r', encoding='utf-8') as f:
    text = f.read()

killer_funcs = """
def gen_killer_chained_assignment():
    ans = "df.loc[df['A'] > 5, 'B'] = 10"
    wrongs = [
        "df[df['A'] > 5]['B'] = 10",
        "df.query('A > 5')['B'] = 10",
        "df.where(df['A'] > 5)['B'] = 10"
    ]
    return {
        'topic': '킬러 - Pandas 인덱싱 (Chained Assignment)',
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
        'topic': '킬러 - Pandas 데이터 병합 (Merge)',
        'question': "Pandas의 `pd.merge(df1, df2)` 동작 방식에 대한 설명으로 올바른 것은 무엇입니까?",
        'expected': ans,
        'wrongs': wrongs,
        'explanation': "`merge`의 기본 동작은 `inner join`이며, `on`을 생략하면 이름이 겹치는 모든 컬럼을 병합 키로 자동 사용합니다. 인덱스 병합은 `left_index=True`, `right_index=True` 옵션으로 `merge`에서도 가능합니다. 공통 컬럼이 병합 키가 아닐 경우 자동으로 접미사(_x, _y)가 붙습니다.",
        'force_type': 'radio'
    }

ALL_KILLER = [gen_killer_chained_assignment, gen_killer_merge_suffixes]
"""

# Append killer funcs before QuizStrategy
text = text.replace("class QuizStrategy:", killer_funcs + "\nclass QuizStrategy:")

# Add killer_pool to QuizStrategy class
text = text.replace("def __init__(self, id, name, description, easy_pool, hard_pool):", "def __init__(self, id, name, description, easy_pool, hard_pool, killer_pool=None):")
text = text.replace("self.hard_pool = hard_pool", "self.hard_pool = hard_pool\n        self.killer_pool = killer_pool or []")

# Update Strategy dictionaries
text = text.replace("hard_pool=ALL_HARD\n    )", "hard_pool=ALL_HARD,\n        killer_pool=ALL_KILLER\n    )")

# Update generate_exam_quizzes logic
bad_generate = """def generate_exam_quizzes(strategy_id='bootcamp_day1_4'):
    strategy = get_strategy(strategy_id)
    easy_pool = strategy.easy_pool
    hard_pool = strategy.hard_pool
    
    quizzes = []
    
    if strategy_id == 'bootcamp_day1_4':
        # 20문제 중 16개는 베이직(Easy) 풀에서 출제
        for _ in range(16):
            f = random.choice(easy_pool)
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
        # 20문제 중 4개는 꼬아낸 심화(Hard) 풀에서 출제
        for _ in range(4):
            f = random.choice(hard_pool)
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
    else:
        # 종합 마스터는 비율을 10:10으로 어렵게
        for _ in range(10):
            f = random.choice(easy_pool)
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
        for _ in range(10):
            f = random.choice(hard_pool)
            q = f()
            q['type'] = 'radio'
            opts = [q['expected']] + q['wrongs'][:3]
            random.shuffle(opts)
            q['choices'] = opts
            quizzes.append(q)
            
    random.shuffle(quizzes)
    return quizzes"""

good_generate = """def generate_exam_quizzes(strategy_id='bootcamp_day1_4'):
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
    return quizzes"""

text = text.replace(bad_generate, good_generate)

os.remove('src/questions.py')
with open('src/questions.py', 'w', encoding='utf-8') as f:
    f.write(text)
