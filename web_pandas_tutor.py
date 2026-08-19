import streamlit as st
import random
import pandas as pd
import json
import os
from datetime import datetime

# ==========================================
# 1. 설정 및 UI 스타일링 (상용 서비스 급 테마)
# ==========================================
st.set_page_config(page_title="Data Analysis Tutor", layout="centered")

st.markdown("""
<style>
/* 프리미엄 상용 서비스 폰트 (Pretendard) */
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.015em;
}

/* 전체 배경 및 텍스트 색상 조율 */
.stApp {
    background-color: #f8fafc;
}

/* Streamlit 기본 헤더/푸터 강제 숨김 */
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}

/* 상단 패딩 제거하여 커스텀 헤더가 딱 붙게 */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
}

/* 커스텀 헤더 디자인 */
.custom-header {
    background-color: #ffffff;
    padding: 1rem 2rem;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #3b82f6;
}
.custom-header h2 {
    margin: 0 !important;
    font-size: 1.4rem !important;
    font-weight: 800 !important;
    color: #0f172a !important;
}
.custom-header span {
    font-size: 0.9rem;
    font-weight: 600;
    color: #64748b;
    background-color: #f1f5f9;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
}

/* 커스텀 푸터 디자인 */
.custom-footer {
    text-align: center;
    padding-top: 2rem;
    margin-top: 3rem;
    border-top: 1px solid #e2e8f0;
    color: #94a3b8;
    font-size: 0.85rem;
}

/* 메인 타이틀 (이제 커스텀 헤더가 있으므로 숨기거나 작게) */
h1 {
    display: none; 
}

/* 탭 UI 개선 */
[data-baseweb="tab-list"] {
    gap: 2rem;
    margin-bottom: 1.5rem;
}
[data-baseweb="tab"] {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: #64748b !important;
}
[aria-selected="true"] {
    color: #2563eb !important;
}

/* 문제 컨테이너 (카드 UI) */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
    border: 1px solid #e2e8f0 !important;
    padding: 2.5rem 2rem;
    margin-bottom: 2rem;
}

/* 서브 타이틀 (Question Number) */
h3 {
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: #1e293b !important;
    margin-bottom: 1.2rem !important;
}

/* 일반 텍스트 (본문) */
p {
    font-size: 1.05rem !important;
    color: #334155 !important;
    line-height: 1.7 !important;
}

/* 상태 라벨 및 캡션 */
.stCaption {
    font-size: 0.95rem !important;
    color: #64748b !important;
    font-weight: 500;
}

/* 라디오 버튼 (선택지) 텍스트 크기 */
.stRadio label span {
    font-size: 1.05rem !important;
    color: #1e293b !important;
}

/* 버튼 디자인 (모던 액션 버튼) */
.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.5rem !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    width: 100%;
}
.stButton > button:hover {
    background-color: #1d4ed8 !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2) !important;
}
.stButton > button:active {
    transform: translateY(0);
}

/* 보조 버튼 스타일링 (해설 숨기기 등) */
[data-testid="stExpander"] {
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    background-color: #f1f5f9;
}
[data-testid="stExpander"] p {
    color: #475569 !important;
}

/* 코드 블록 */
code {
    font-family: 'JetBrains Mono', 'D2Coding', monospace !important;
    font-size: 0.95rem !important;
    color: #0ea5e9 !important;
    background-color: #f1f5f9 !important;
    padding: 0.2rem 0.4rem !important;
    border-radius: 6px !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 난수 발생 문제 은행
# ==========================================
def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    return {
        'topic': '데이터 불러오기', 'type': 'code',
        'question': f"data.{ext} 파일을 읽어 df 변수에 할당하는 코드를 작성하세요.",
        'check': lambda x: f"read_{ext}" in x and "data" in x and "df" in x,
        'expected': f"df = pd.read_{ext}('data.{ext}')",
        'explanation': "가장 기초적인 데이터 로드 함수입니다. 확장자에 따라 read_csv 또는 read_excel을 사용합니다."
    }

def gen_easy_head():
    n = random.randint(3, 8)
    return {
        'topic': '데이터 상단 확인', 'type': 'code',
        'question': f"데이터프레임 df의 맨 위 {n}개 행을 확인하는 코드를 작성하세요.",
        'check': lambda x: "head" in x and str(n) in x,
        'expected': f"df.head({n})",
        'explanation': "데이터프레임의 상단 구조를 파악할 때 사용하는 head() 메서드입니다."
    }

def gen_easy_info():
    return {
        'topic': '데이터 요약 정보', 'type': 'code',
        'question': "df의 총 행 개수, 컬럼 타입, 그리고 결측치 여부를 출력하는 메서드를 작성하세요.",
        'check': lambda x: "info" in x,
        'expected': "df.info()",
        'explanation': "데이터 전처리 전, 메타데이터 구조를 파악하기 위한 필수 메서드입니다."
    }

def gen_easy_isnull():
    return {
        'topic': '결측치 집계', 'type': 'code',
        'question': "df의 각 컬럼별 결측치(NaN) 총합을 구하는 코드를 작성하세요.",
        'check': lambda x: ("isnull" in x or "isna" in x) and "sum" in x,
        'expected': "df.isnull().sum()",
        'explanation': "isnull()로 마스킹 후 sum()을 통해 True(1)의 개수를 합산합니다."
    }

def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    return {
        'topic': '결측치 단일값 대체', 'type': 'code',
        'question': f"df['{col}'] 컬럼의 결측치를 {val} 값으로 일괄 변경하는 코드를 작성하세요.",
        'check': lambda x: "fillna" in x and str(val) in x and col in x,
        'expected': f"df['{col}'].fillna({val})",
        'explanation': "fillna() 메서드를 사용하여 Series 내의 NaN을 특정 상수로 대체합니다."
    }

def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    return {
        'topic': '특정 컬럼 제거', 'type': 'code',
        'question': f"df에서 {col} 컬럼을 완전히 삭제하는 코드를 작성하세요.",
        'check': lambda x: "drop" in x and col in x and "columns" in x,
        'expected': f"df.drop(columns=['{col}'])",
        'explanation': "drop() 메서드에 columns 파라미터를 명시하여 안전하게 열(Column)을 제거합니다."
    }

def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    return {
        'topic': '불리언 인덱싱', 'type': 'code',
        'question': f"df에서 {col} 값이 {val} 이상(>=)인 행 데이터만 추출하는 코드를 작성하세요.",
        'check': lambda x: col in x and str(val) in x and ">=" in x,
        'expected': f"df[df['{col}'] >= {val}]",
        'explanation': "대괄호 내부에 조건식을 전달하여 True인 행만 서브셋으로 추출합니다."
    }

def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    return {
        'topic': '데이터 병합 (Merge)', 'type': 'code',
        'question': f"df1과 df2를 'user_id' 컬럼을 기준으로 {how} Join 병합하는 코드를 작성하세요.",
        'check': lambda x: "merge" in x and "user_id" in x and how in x,
        'expected': f"pd.merge(df1, df2, on='user_id', how='{how}')",
        'explanation': "RDB의 JOIN 연산과 동일하게 두 데이터프레임을 특정 키를 기준으로 가로 병합합니다."
    }

def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    return {
        'topic': '피벗 테이블 (Pivot Table)', 'type': 'code',
        'question': f"df에서 행(index)은 '{idx}', 열(columns)은 'month', 값(values)은 'sales', 집계(aggfunc)는 'sum'으로 지정한 피벗 테이블 코드를 작성하세요.",
        'check': lambda x: "pivot_table" in x and idx in x and "month" in x and "sales" in x and "sum" in x,
        'expected': f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')",
        'explanation': "1차원 데이터를 2차원 크로스탭 형태로 요약하여 보고용 데이터를 구축합니다."
    }

def gen_hard_str():
    return {
        'topic': '문자열 파싱 및 형변환', 'type': 'code',
        'question': "df['price'] 컬럼 내의 달러 기호('$')를 제거하고, float 자료형으로 변환하는 코드를 작성하세요.",
        'check': lambda x: "str.replace" in x and "$" in x and "astype" in x and "float" in x,
        'expected': "df['price'].str.replace('$', '').astype(float)",
        'explanation': ".str 접근자를 활용해 텍스트를 처리한 후 astype으로 연속적인 형변환을 수행합니다."
    }

def gen_hard_dt():
    return {
        'topic': '시계열 데이터 처리', 'type': 'code',
        'question': "df['date'] 컬럼(datetime 자료형)에서 '월(month)' 데이터만 별도로 추출하는 코드를 작성하세요.",
        'check': lambda x: ".dt.month" in x.replace(" ", ""),
        'expected': "df['date'].dt.month",
        'explanation': "datetime 자료형에는 .dt 접근자를 사용하여 날짜의 세부 요소를 쉽게 분리할 수 있습니다."
    }

def generate_exam_cycle():
    easy_factories = [gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, gen_easy_fillna, gen_easy_drop, gen_easy_filter]
    hard_factories = [gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt]
    
    easy_quizzes = [random.choice(easy_factories)() for _ in range(16)]
    hard_quizzes = [random.choice(hard_factories)() for _ in range(4)]
    
    return easy_quizzes + hard_quizzes

# ==========================================
# 3. 리더보드 로직
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
# 4. 앱 메인 로직
# ==========================================
if 'quizzes' not in st.session_state:
    st.session_state.quizzes = generate_exam_cycle()
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.show_exp = False
    st.session_state.quiz_finished = False

st.markdown('''
<div class="custom-header">
    <h2>📊 Data Analysis Bootcamp</h2>
    <span>Lv.1 Basic & Advanced</span>
</div>
<p style="color: #64748b; font-size: 1.1rem !important; margin-bottom: 2rem;">
    Pandas 데이터 전처리 및 분석 역량 강화를 위한 20문항 실전 모의고사 시스템입니다.
</p>
''', unsafe_allow_html=True)

tabs = st.tabs(["진행 화면", "리더보드"])

with tabs[0]:
    if st.session_state.quiz_finished:
        st.success(f"평가가 종료되었습니다. 최종 스코어: {st.session_state.score} / 20")
        
        with st.container(border=True):
            st.subheader("결과 등록")
            user_name = st.text_input("학습자 성함을 입력해 주세요:")
            if st.button("스코어 보드에 등록", type="primary"):
                if user_name:
                    save_score(user_name, st.session_state.score)
                    st.success("등록이 완료되었습니다. 리더보드 탭을 확인하세요.")
                else:
                    st.warning("이름을 입력해야 등록이 가능합니다.")
                    
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("새로운 모의고사 세션 시작"):
            st.session_state.clear()
            st.rerun()
            
    else:
        idx = st.session_state.current_idx
        q = st.session_state.quizzes[idx]
        
        # 난이도 표시 텍스트 정제
        level_text = "Section 1: Basic Review" if idx < 16 else "Section 2: Advanced Tasks"
        
        st.caption(f"{level_text} — {idx+1} / 20")
        st.progress((idx) / 20)
        
        with st.container(border=True):
            st.subheader(f"Question {idx+1:02d}. {q['topic']}")
            st.write(q['question'])
            
            user_answer = None
            if q['type'] == 'choice':
                user_answer = st.radio("선택지", q['options'], index=None, label_visibility="hidden")
            else:
                user_answer = st.text_input("Answer code", placeholder="코드를 작성해 주세요", label_visibility="hidden", key=f"ans_{idx}")

        if not st.session_state.show_exp:
            if st.button("제출 및 채점", type="primary"):
                if not user_answer:
                    st.warning("답안을 입력해 주세요.")
                else:
                    st.session_state.show_exp = True
                    is_correct = q['check'](user_answer)
                        
                    st.session_state.is_correct = is_correct
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()
        else:
            if st.session_state.is_correct:
                st.success("Correct Answer")
            else:
                st.error("Incorrect Answer")
                
            with st.expander("해설 및 모범 답안", expanded=True):
                st.code(q['expected'], language='python')
                st.markdown(q['explanation'])
                
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("다음 문항으로 이동", type="primary"):
                st.session_state.show_exp = False
                if idx + 1 >= 20:
                    st.session_state.quiz_finished = True
                else:
                    st.session_state.current_idx += 1
                st.rerun()

with tabs[1]:
    st.subheader("Leaderboard")
    lb = load_leaderboard()
    if not lb:
        st.info("현재 등록된 평가 기록이 없습니다.")
    else:
        df_lb = pd.DataFrame(lb)
        df_lb.index = df_lb.index + 1
        df_lb.columns = ['학습자', '최종 스코어', '평가 일시']
        st.dataframe(df_lb, use_container_width=True)



st.markdown('''
<div class="custom-footer">
    © 2026 Data Analysis Bootcamp. All rights reserved.<br>
    Powered by Python & Streamlit
</div>
''', unsafe_allow_html=True)
