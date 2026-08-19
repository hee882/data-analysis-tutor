import streamlit as st
import random
import pandas as pd
import json
import os
from datetime import datetime

# ==========================================
# 1. 설정 및 UI 스타일링
# ==========================================
st.set_page_config(page_title="데이터 분석 파이썬 튜터", page_icon="🔥", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div {
    font-family: 'Noto Sans KR', sans-serif !important;
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

h1 {
    animation: slideDown 0.8s ease-out;
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900 !important;
}

@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

[data-testid="stVerticalBlockBorderWrapper"] {
    animation: fadeIn 0.5s ease-out forwards;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
    border: 1px solid #e2e8f0 !important;
    padding: 20px;
}

.stButton > button {
    border-radius: 8px !important;
    font-weight: 700 !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}
.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 7px 14px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 난수 발생 문제 은행 (Easy & Hard Factories)
# ==========================================

# --- EASY (Day1/Day2 복습용) ---
def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    return {
        'topic': '데이터 불러오기 기초', 'type': 'code',
        'question': f"data.{ext} 파일을 읽어 df 변수에 저장하는 코드를 작성하세요.",
        'check': lambda x: f"read_{ext}" in x and "data" in x and "df" in x,
        'expected': f"df = pd.read_{ext}('data.{ext}')",
        'explanation': "가장 기본이 되는 데이터 로드 함수입니다."
    }

def gen_easy_head():
    n = random.randint(3, 10)
    return {
        'topic': '데이터 미리보기', 'type': 'code',
        'question': f"df의 맨 위 {n}개 행을 확인하는 코드를 작성하세요.",
        'check': lambda x: "head" in x and str(n) in x,
        'expected': f"df.head({n})",
        'explanation': "데이터프레임의 상단 일부를 확인할 때 사용합니다."
    }

def gen_easy_info():
    return {
        'topic': '데이터 요약 정보', 'type': 'code',
        'question': "df의 전체 행 개수, 컬럼 타입, 결측치 여부를 한눈에 확인하는 함수를 작성하세요.",
        'check': lambda x: "info" in x,
        'expected': "df.info()",
        'explanation': "데이터 전처리 전 가장 먼저 실행해야 하는 핵심 함수입니다."
    }

def gen_easy_isnull():
    return {
        'topic': '결측치 개수 파악', 'type': 'code',
        'question': "df의 각 컬럼별 결측치(NaN) 총합을 구하는 코드를 작성하세요. (메서드 체이닝 사용)",
        'check': lambda x: ("isnull" in x or "isna" in x) and "sum" in x,
        'expected': "df.isnull().sum()",
        'explanation': "isnull()로 불리언을 만들고 .sum()으로 True의 개수를 셉니다."
    }

def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    return {
        'topic': '결측치 채우기', 'type': 'code',
        'question': f"df['{col}'] 컬럼의 결측치를 숫자 {val}로 일괄 변경하는 코드를 작성하세요.",
        'check': lambda x: "fillna" in x and str(val) in x and col in x,
        'expected': f"df['{col}'].fillna({val})",
        'explanation': "특정 컬럼의 빈 값을 원하는 기본값으로 채워넣습니다."
    }

def gen_easy_drop():
    col = random.choice(['notes', 'temp_id', 'memo'])
    return {
        'topic': '불필요한 열 삭제', 'type': 'code',
        'question': f"df에서 {col} 컬럼을 통째로 삭제하는 코드를 작성하세요. (columns 파라미터 활용)",
        'check': lambda x: "drop" in x and col in x and "columns" in x,
        'expected': f"df.drop(columns=['{col}'])",
        'explanation': "drop(columns=['컬럼명'])을 사용하여 안전하게 열을 제거합니다."
    }

def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 80)
    return {
        'topic': '기초 조건 필터링', 'type': 'code',
        'question': f"df에서 {col} 값이 {val} 이상(>=)인 행만 추출하는 코드를 작성하세요.",
        'check': lambda x: col in x and str(val) in x and ">=" in x,
        'expected': f"df[df['{col}'] >= {val}]",
        'explanation': "불리언 마스크를 이용해 데이터프레임 내부를 필터링합니다."
    }

# --- HARD (고난이도 / 실무 응용) ---
def gen_hard_merge():
    how = random.choice(['left', 'inner', 'outer'])
    return {
        'topic': '[심화] 데이터 병합 (Merge)', 'type': 'code',
        'question': f"df1과 df2를 'user_id' 컬럼을 기준으로 {how} Join 병합하는 코드를 작성하세요.",
        'check': lambda x: "merge" in x and "user_id" in x and how in x,
        'expected': f"pd.merge(df1, df2, on='user_id', how='{how}')",
        'explanation': "데이터를 관계형 DB처럼 결합할 때 사용하는 필수 함수입니다."
    }

def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    col = random.choice(['year', 'month'])
    return {
        'topic': '[심화] 피벗 테이블 (Pivot)', 'type': 'code',
        'question': f"df를 활용하여 행(index)은 '{idx}', 열(columns)은 '{col}', 값(values)은 'sales', 집계(aggfunc)는 'sum'인 피벗 테이블을 만드세요.",
        'check': lambda x: "pivot_table" in x and idx in x and col in x and "sales" in x and "sum" in x,
        'expected': f"df.pivot_table(index='{idx}', columns='{col}', values='sales', aggfunc='sum')",
        'explanation': "데이터를 2차원 교차 리포트로 요약할 때 사용합니다."
    }

def gen_hard_str():
    return {
        'topic': '[심화] 문자열 파싱 및 형변환', 'type': 'code',
        'question': "df['price'] 컬럼(예: '')에서 달러 기호('$')를 빈 문자열('')로 교체하고, float으로 형변환하는 1줄 코드를 작성하세요.",
        'check': lambda x: "str.replace" in x and "$" in x and "astype" in x and "float" in x,
        'expected': "df['price'].str.replace('$', '').astype(float)",
        'explanation': "텍스트 전처리와 타입 변환을 메서드 체이닝으로 한 번에 처리합니다."
    }

def gen_hard_dt():
    return {
        'topic': '[심화] 시계열 파생변수', 'type': 'code',
        'question': "df['date'] 컬럼(datetime 타입)에서 '월(month)'을 추출하는 코드를 작성하세요.",
        'check': lambda x: ".dt.month" in x.replace(" ", ""),
        'expected': "df['date'].dt.month",
        'explanation': "datetime 시리즈에 .dt 접근자를 쓰면 날짜 요소를 쉽게 뽑을 수 있습니다."
    }

def generate_exam_cycle():
    easy_factories = [gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, gen_easy_fillna, gen_easy_drop, gen_easy_filter]
    hard_factories = [gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt]
    
    # 기초 16문제 (중복 허용 랜덤 추출)
    easy_quizzes = [random.choice(easy_factories)() for _ in range(16)]
    # 심화 4문제 (중복 허용 랜덤 추출)
    hard_quizzes = [random.choice(hard_factories)() for _ in range(4)]
    
    # 전체 20문제 합치기
    return easy_quizzes + hard_quizzes

# ==========================================
# 3. 리더보드 (JSON 파일 기반)
# ==========================================
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_score(name, score):
    lb = load_leaderboard()
    lb.append({
        "name": name,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    lb = sorted(lb, key=lambda x: x['score'], reverse=True)
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(lb, f, ensure_ascii=False, indent=4)

# ==========================================
# 4. 세션 초기화 및 앱 메인 로직
# ==========================================
if 'quizzes' not in st.session_state:
    st.session_state.quizzes = generate_exam_cycle()
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.show_exp = False
    st.session_state.quiz_finished = False

st.title("🔥 데이터 분석 파이썬 실전 튜터")
st.markdown("**기초(Day1~2) 복습 16문제 + 심화(Next Level) 4문제 = 총 20문제 1사이클** 모의고사입니다.")

tabs = st.tabs(["📝 모의고사 풀기", "🏆 명예의 전당 (리더보드)"])

with tabs[0]:
    if st.session_state.quiz_finished:
        st.success(f"🎉 모든 문제를 풀었습니다! 최종 점수: {st.session_state.score} / 20")
        
        with st.container(border=True):
            st.subheader("🏆 리더보드에 점수 등록하기")
            user_name = st.text_input("이름(또는 닉네임)을 입력하세요:")
            if st.button("점수 등록", type="primary"):
                if user_name:
                    save_score(user_name, st.session_state.score)
                    st.success("등록 완료! '명예의 전당' 탭에서 순위를 확인하세요.")
                else:
                    st.warning("이름을 입력해주세요!")
                    
        if st.button("새로운 20문제 모의고사 시작하기"):
            st.session_state.clear()
            st.rerun()
            
    else:
        idx = st.session_state.current_idx
        q = st.session_state.quizzes[idx]
        
        # 난이도 라벨
        difficulty_label = "🟢 기초 복습" if idx < 16 else "🔴 심화 레벨"
        
        st.progress((idx) / 20, text=f"진행도: {idx+1} / 20 ({difficulty_label})")
        
        with st.container(border=True):
            st.subheader(f"Q{idx+1}. {q['topic']}")
            st.write(q['question'])
            
            user_answer = None
            if q['type'] == 'choice':
                user_answer = st.radio("정답 선택:", q['options'], index=None)
            else:
                user_answer = st.text_input("파이썬 코드를 작성하세요:", placeholder="코드를 1줄로 입력", key=f"ans_{idx}")

        if not st.session_state.show_exp:
            if st.button("정답 제출", type="primary", use_container_width=True):
                if not user_answer:
                    st.warning("정답을 입력해주세요!")
                else:
                    st.session_state.show_exp = True
                    is_correct = q['check'](user_answer)
                        
                    st.session_state.is_correct = is_correct
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()
        else:
            if st.session_state.is_correct:
                st.success("✅ 정답입니다!")
            else:
                st.error("❌ 오답입니다.")
                
            with st.expander("💡 해설 및 모범 답안", expanded=True):
                st.code(q['expected'], language='python')
                st.markdown(q['explanation'])
                
            if st.button("다음 문제로 ➡️", type="primary"):
                st.session_state.show_exp = False
                if idx + 1 >= 20:
                    st.session_state.quiz_finished = True
                else:
                    st.session_state.current_idx += 1
                st.rerun()

with tabs[1]:
    st.subheader("🏆 튜터 명예의 전당")
    lb = load_leaderboard()
    if not lb:
        st.info("아직 등록된 랭킹이 없습니다. 첫 번째 랭커가 되어보세요!")
    else:
        df_lb = pd.DataFrame(lb)
        df_lb.index = df_lb.index + 1
        df_lb.columns = ['이름/닉네임', '획득 점수', '달성 일시']
        st.dataframe(df_lb, use_container_width=True)
