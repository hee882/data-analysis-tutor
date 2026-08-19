import os
import random

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
q_path = os.path.join(repo_path, 'src', 'questions.py')

with open(q_path, 'r', encoding='utf-8') as f:
    q_content = f.read()

new_factories_code = """
def gen_py_loop_control():
    break_val = random.choice([3, 4])
    skip_val = random.choice([1, 2])
    
    code = f"s = 0\\nfor i in range(5):\\n    if i == {skip_val}:\\n        continue\\n    if i == {break_val}:\\n        break\\n    s += i\\nprint(s)"
    
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
        'question': f"다음 파이썬 코드의 최종 출력(print) 결과를 예측하세요.\\n```python\\n{code}\\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"i가 {skip_val}일 때는 continue로 넘어갔고, {break_val}일 때 break로 반복문이 완전히 종료되었습니다. 따라서 누적합은 {expected}입니다.",
        'check': lambda x: expected in x.strip()
    }

def gen_py_str_split():
    sep = random.choice([',', '-'])
    idx = random.choice([1, -1])
    sample = "apple,banana,cherry" if sep == ',' else "서울-대전-대구-부산"
    
    code = f"text = '{sample}'\\nprint(text.split('{sep}')[{idx}])"
    
    parts = sample.split(sep)
    expected = f"'{parts[idx]}'"
    
    wrong_idx1 = 0 if idx != 0 else 1
    wrong_idx2 = 2 if idx != 2 else 1
    wrongs = [f"'{parts[wrong_idx1]}'", f"'{parts[wrong_idx2]}'", f"'{parts[idx][:2]}'", "IndexError"]
    wrongs = list(set([w for w in wrongs if w != expected]))
    
    return {
        'topic': 'Python 문자열 파싱 (split)',
        'question': f"다음 파이썬 코드의 최종 출력(print) 결과를 예측하세요.\\n```python\\n{code}\\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"split('{sep}')을 통해 리스트로 분리한 후, 인덱스 {idx}에 해당하는 요소를 추출합니다.",
        'check': lambda x: parts[idx] in x
    }

def gen_py_list_slice():
    lst = [10, 20, 30, 40, 50]
    start = random.choice([1, 2])
    end = random.choice([4, -1])
    
    code = f"nums = {lst}\\nprint(nums[{start}:{end}])"
    
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
        'question': f"다음 파이썬 코드의 출력 결과를 예측하세요.\\n```python\\n{code}\\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"슬라이싱 [a:b]는 인덱스 a부터 b-1(직전)까지의 요소를 추출합니다.",
        'check': lambda x: expected.replace(" ", "") in x.replace(" ", "")
    }

def gen_py_dict_get():
    key = random.choice(['age', 'score'])
    default = random.choice([0, -1])
    
    code = f"info = {{'name': 'Alice', 'role': 'Admin'}}\\nprint(info.get('{key}', {default}))"
    
    expected = str(default)
    wrongs = ["'Alice'", "KeyError", "None", str(default + 10)]
    wrongs = list(set([w for w in wrongs if w != expected]))
    
    return {
        'topic': 'Python 딕셔너리 (get)',
        'question': f"다음 파이썬 코드의 출력 결과를 예측하세요.\\n```python\\n{code}\\n```",
        'expected': expected,
        'wrongs': wrongs[:3],
        'explanation': f"딕셔너리의 .get(key, default) 메서드는 키가 존재하지 않을 경우 에러(KeyError)를 발생시키지 않고 default 값({default})을 반환합니다.",
        'check': lambda x: expected in x.strip()
    }

def _get_factories():
"""

q_content = q_content.replace('def _get_factories():\n', new_factories_code)

# Now inject them into easy_factories
old_easy = 'gen_viz_bar, gen_viz_scatter, gen_viz_hist\n    ]'
new_easy = 'gen_viz_bar, gen_viz_scatter, gen_viz_hist,\n        gen_py_loop_control, gen_py_str_split, gen_py_list_slice, gen_py_dict_get\n    ]'
q_content = q_content.replace(old_easy, new_easy)

with open(q_path, 'w', encoding='utf-8') as f:
    f.write(q_content)

print("Python base question factories injected!")
