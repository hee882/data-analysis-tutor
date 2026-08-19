import os

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
doc_path = os.path.join(repo_path, 'DESIGN_PHILOSOPHY.md')
q_path = os.path.join(repo_path, 'src', 'questions.py')

# 1. Update DESIGN_PHILOSOPHY.md
with open(doc_path, 'r', encoding='utf-8') as f:
    doc_content = f.read()

new_doc_section = """1. **파라미터 튜닝 및 행간(Nuance)의 이해 시나리오:**
   * 단순히 함수의 존재 유무를 묻는 것을 넘어, **파라미터를 다르게 썼을 때 결과물이 어떻게 달라지는지(행간의 의미)**를 묻습니다.
   * `axis=0`(행 방향) vs `axis=1`(열 방향)의 구조적 차이 묻기.
   * `keep='first'` vs `keep='last'`를 사용하여 중복 데이터 처리 시 어떤 데이터가 살아남는지 묻기.
   * "교집합만 남겨라" ➡️ `how='inner'`, "왼쪽 테이블 데이터는 모두 살려라" ➡️ `how='left'`"""

doc_content = doc_content.replace(
    '1. **파라미터 튜닝 시나리오:**\n   * "교집합만 남겨라" ➡️ `how=\'inner\'`\n   * "왼쪽 테이블 데이터는 모두 살려라" ➡️ `how=\'left\'`',
    new_doc_section
)

with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(doc_content)

# 2. Update questions.py to add nuance factories
with open(q_path, 'r', encoding='utf-8') as f:
    q_content = f.read()

new_factories = """
def gen_param_nuance_concat():
    axis = random.choice([0, 1])
    desc = "행(위아래)으로 길게 붙이고 싶습니다" if axis == 0 else "열(좌우)로 넓게 붙이고 싶습니다"
    ans = f"pd.concat([df1, df2], axis={axis})"
    wrong_axis = 1 if axis == 0 else 0
    wrongs = [
        f"pd.concat([df1, df2], axis={wrong_axis})", 
        f"df1.append(df2, axis={axis})", 
        f"pd.merge(df1, df2, how='outer')"
    ]
    return {
        'topic': '파라미터의 차이 (Concat Axis)', 
        'question': f"두 데이터프레임 `df1`과 `df2`를 **{desc}**. 이때 파라미터 `axis`의 값으로 올바른 전체 코드를 작성하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"axis=0은 행 방향(수직 병합), axis=1은 열 방향(수평 병합)을 의미합니다.",
        'check': lambda x: "concat" in x and f"axis={axis}" in x.replace(" ", "")
    }

def gen_param_nuance_dropdup():
    keep = random.choice(['first', 'last'])
    desc = "가장 처음 발견된 원본 데이터" if keep == 'first' else "가장 마지막에 갱신된 데이터"
    ans = f"df.drop_duplicates(subset=['user_id'], keep='{keep}')"
    wrong_keep = 'last' if keep == 'first' else 'first'
    wrongs = [
        f"df.drop_duplicates(subset=['user_id'], keep='{wrong_keep}')", 
        f"df.drop_duplicates(subset=['user_id'], drop='{keep}')", 
        f"df.unique(subset=['user_id'], keep='{keep}')"
    ]
    return {
        'topic': '파라미터의 차이 (중복 제거)', 
        'question': f"`df`에서 'user_id'가 중복되는 행들을 제거하려고 합니다. 단, **{desc}**만 남기고 나머지를 지워야 합니다. 알맞은 파라미터를 사용하세요.",
        'expected': ans, 'wrongs': wrongs, 
        'explanation': f"keep='first'는 첫 번째 값을 유지, keep='last'는 마지막 값을 유지합니다.",
        'check': lambda x: "drop_duplicates" in x and "user_id" in x and f"keep='{keep}'" in x.replace('"', "'")
    }

def _get_factories():"""

q_content = q_content.replace('def _get_factories():', new_factories)
q_content = q_content.replace(
    'gen_hard_dt,',
    'gen_hard_dt, gen_param_nuance_concat, gen_param_nuance_dropdup,'
)

with open(q_path, 'w', encoding='utf-8') as f:
    f.write(q_content)

print("Philosophy and nuance factories added successfully!")
