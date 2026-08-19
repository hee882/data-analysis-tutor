import streamlit as st
import random
import pandas as pd
import json
import os
from datetime import datetime
from supabase import create_client

# ==========================================
# 1. 설정 및 UI 스타일링
# ==========================================
st.set_page_config(page_title="Data Analysis Tutor", layout="wide")

st.markdown('''
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.015em;
}
.stApp { background-color: #f8fafc; }
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}

.block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }

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
.custom-header h2 { margin: 0 !important; font-size: 1.4rem !important; font-weight: 800 !important; color: #0f172a !important; }
.custom-header span { font-size: 0.9rem; font-weight: 600; color: #64748b; background-color: #f1f5f9; padding: 0.4rem 0.8rem; border-radius: 20px; }
.custom-footer { text-align: center; padding-top: 2rem; margin-top: 3rem; border-top: 1px solid #e2e8f0; color: #94a3b8; font-size: 0.85rem; }
h1 { display: none; }

[data-baseweb="tab-list"] { gap: 2rem; margin-bottom: 1.5rem; }
[data-baseweb="tab"] { font-size: 1.1rem !important; font-weight: 600 !important; color: #64748b !important; }
[aria-selected="true"] { color: #2563eb !important; }

[data-testid="stVerticalBlockBorderWrapper"], .exam-card {
    background-color: #ffffff;
    border-radius: 16px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
    border: 1px solid #e2e8f0 !important;
    padding: 2.5rem 2rem;
    margin-bottom: 2rem;
}

h3 { font-size: 1.3rem !important; font-weight: 700 !important; color: #1e293b !important; margin-bottom: 1.2rem !important; }
p { font-size: 1.05rem !important; color: #334155 !important; line-height: 1.7 !important; }
.stCaption { font-size: 0.95rem !important; color: #64748b !important; font-weight: 500; }
.stRadio label span { font-size: 1.05rem !important; color: #1e293b !important; }

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
.stButton > button:hover { background-color: #1d4ed8 !important; transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2) !important; }
.stButton > button:active { transform: translateY(0); }

[data-testid="stExpander"] { border-radius: 12px; border: 1px solid #e2e8f0; background-color: #f1f5f9; }
[data-testid="stExpander"] p { color: #475569 !important; }
code { font-family: 'JetBrains Mono', 'D2Coding', monospace !important; font-size: 0.95rem !important; color: #0ea5e9 !important; background-color: #f1f5f9 !important; padding: 0.2rem 0.4rem !important; border-radius: 6px !important; }

.report-correct { border-left: 5px solid #22c55e !important; padding-left: 1rem; margin-bottom: 1rem; }
.report-wrong { border-left: 5px solid #ef4444 !important; padding-left: 1rem; margin-bottom: 1rem; }
</style>
''', unsafe_allow_html=True)

# ==========================================
# 2. 난수 발생 문제 은행
# ==========================================
def gen_easy_read():
    ext = random.choice(['csv', 'excel'])
    return {'topic': '데이터 로드', 'type': 'code', 'question': f"data.{ext} 파일을 읽어 df에 할당하세요.", 'check': lambda x: f"read_{ext}" in x and "data" in x and "df" in x, 'expected': f"df = pd.read_{ext}('data.{ext}')", 'explanation': "pd.read_csv 또는 pd.read_excel을 사용합니다."}
def gen_easy_head():
    n = random.randint(3, 8)
    return {'topic': '데이터 미리보기', 'type': 'code', 'question': f"df의 상단 {n}개 행을 확인하세요.", 'check': lambda x: "head" in x and str(n) in x, 'expected': f"df.head({n})", 'explanation': "df.head(n) 메서드를 사용합니다."}
def gen_easy_info():
    return {'topic': '데이터 메타정보', 'type': 'code', 'question': "df의 행 개수, 컬럼 타입, 결측치를 요약 출력하세요.", 'check': lambda x: "info" in x, 'expected': "df.info()", 'explanation': "df.info()는 전처리의 기본입니다."}
def gen_easy_isnull():
    return {'topic': '결측치 집계', 'type': 'code', 'question': "df의 각 컬럼별 결측치(NaN) 총합을 구하세요.", 'check': lambda x: ("isnull" in x or "isna" in x) and "sum" in x, 'expected': "df.isnull().sum()", 'explanation': "isnull().sum() 체이닝을 활용합니다."}
def gen_easy_fillna():
    col = random.choice(['score', 'price', 'age'])
    val = random.choice([0, -1])
    return {'topic': '결측치 단일값 대체', 'type': 'code', 'question': f"df['{col}']의 결측치를 {val} 값으로 일괄 변경하세요.", 'check': lambda x: "fillna" in x and str(val) in x and col in x, 'expected': f"df['{col}'].fillna({val})", 'explanation': "fillna() 메서드를 사용합니다."}
def gen_easy_drop():
    col = random.choice(['memo', 'temp_id'])
    return {'topic': '컬럼 제거', 'type': 'code', 'question': f"df에서 {col} 컬럼을 삭제하세요.", 'check': lambda x: "drop" in x and col in x and "columns" in x, 'expected': f"df.drop(columns=['{col}'])", 'explanation': "drop(columns=[...])을 사용합니다."}
def gen_easy_filter():
    col = random.choice(['age', 'score', 'sales'])
    val = random.randint(20, 50)
    return {'topic': '불리언 인덱싱', 'type': 'code', 'question': f"df에서 {col} 값이 {val} 이상(>=)인 행만 추출하세요.", 'check': lambda x: col in x and str(val) in x and ">=" in x, 'expected': f"df[df['{col}'] >= {val}]", 'explanation': "df[df['col'] >= val] 형태를 사용합니다."}
def gen_viz_bar():
    col1 = random.choice(['region', 'category']); col2 = random.choice(['sales', 'count'])
    return {'topic': '막대 그래프', 'type': 'code', 'question': f"Pandas 기본 내장 함수로 x축 '{col1}', y축 '{col2}'의 막대 그래프(bar plot)를 그리세요.", 'check': lambda x: "plot" in x and "bar" in x and col1 in x and col2 in x, 'expected': f"df.plot(kind='bar', x='{col1}', y='{col2}')", 'explanation': ".plot(kind='bar')를 사용합니다."}
def gen_viz_scatter():
    col1 = random.choice(['age', 'height']); col2 = random.choice(['score', 'salary'])
    return {'topic': '산점도', 'type': 'code', 'question': f"Pandas 기본 함수로 x축 '{col1}', y축 '{col2}'의 산점도(scatter plot)를 그리세요.", 'check': lambda x: "plot" in x and "scatter" in x and col1 in x and col2 in x, 'expected': f"df.plot(kind='scatter', x='{col1}', y='{col2}')", 'explanation': ".plot(kind='scatter')를 사용합니다."}
def gen_viz_hist():
    col = random.choice(['score', 'salary']); bins = random.choice([10, 20])
    return {'topic': '히스토그램', 'type': 'code', 'question': f"df['{col}']의 구간(bins)을 {bins}개로 나눈 히스토그램을 그리세요.", 'check': lambda x: "hist" in x and str(bins) in x and col in x.replace('"',"'"), 'expected': f"df['{col}'].plot(kind='hist', bins={bins})", 'explanation': ".plot(kind='hist', bins=N)을 사용합니다."}
def gen_hard_merge():
    how = random.choice(['left', 'inner'])
    return {'topic': '데이터 병합', 'type': 'code', 'question': f"df1과 df2를 'user_id' 컬럼을 기준으로 {how} Join 하세요.", 'check': lambda x: "merge" in x and "user_id" in x and how in x, 'expected': f"pd.merge(df1, df2, on='user_id', how='{how}')", 'explanation': "pd.merge() 함수를 활용합니다."}
def gen_hard_pivot():
    idx = random.choice(['region', 'category'])
    return {'topic': '피벗 테이블', 'type': 'code', 'question': f"df에서 행(index) '{idx}', 열(columns) 'month', 값 'sales', 집계 'sum'인 피벗 테이블 코드를 작성하세요.", 'check': lambda x: "pivot_table" in x and idx in x and "month" in x and "sales" in x and "sum" in x, 'expected': f"df.pivot_table(index='{idx}', columns='month', values='sales', aggfunc='sum')", 'explanation': "df.pivot_table()을 사용합니다."}
def gen_hard_str():
    return {'topic': '문자열 파싱', 'type': 'code', 'question': "df['price'] 컬럼 내의 달러 기호('$')를 제거하고 float으로 변환하세요.", 'check': lambda x: "str.replace" in x and "$" in x and "astype" in x and "float" in x, 'expected': "df['price'].str.replace('$', '').astype(float)", 'explanation': ".str.replace() 후 .astype()을 체이닝합니다."}
def gen_hard_dt():
    return {'topic': '시계열 처리', 'type': 'code', 'question': "df['date'] 컬럼(datetime 자료형)에서 '월(month)' 데이터만 추출하세요.", 'check': lambda x: ".dt.month" in x.replace(" ", ""), 'expected': "df['date'].dt.month", 'explanation': ".dt 접근자를 사용합니다."}

def generate_exam_cycle():
    easy_factories = [gen_easy_read, gen_easy_head, gen_easy_info, gen_easy_isnull, gen_easy_fillna, gen_easy_drop, gen_easy_filter]
    viz_factories = [gen_viz_bar, gen_viz_scatter, gen_viz_hist]
    hard_factories = [gen_hard_merge, gen_hard_pivot, gen_hard_str, gen_hard_dt]
    
    return [random.choice(easy_factories)() for _ in range(14)] + \
           [random.choice(viz_factories)() for _ in range(3)] + \
           [random.choice(hard_factories)() for _ in range(3)]

# ==========================================
# 3. 리더보드 로직 (Supabase 연동)
# ==========================================
def get_supabase_client():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception:
        return None

def load_leaderboard():
    supabase = get_supabase_client()
    if supabase:
        try:
            response = supabase.table('leaderboard').select('*').order('score', desc=True).execute()
            return response.data
        except Exception:
            return []
    # 폴백: 로컬 JSON
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_score(name, score):
    supabase = get_supabase_client()
    if supabase:
        try:
            supabase.table('leaderboard').insert({"name": name, "score": score}).execute()
            return True
        except Exception:
            return False
    # 폴백: 로컬 JSON
    lb = load_leaderboard()
    lb.append({"name": name, "score": score, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")})
    lb = sorted(lb, key=lambda x: x['score'], reverse=True)
    with open("leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(lb, f, ensure_ascii=False, indent=4)
    return True

# ==========================================
# 4. 앱 메인 로직 및 탭 분리
# ==========================================
st.markdown('''
<div class="custom-header">
    <h2>📊 Data Analysis Bootcamp</h2>
    <span>Lv.1 Basic & Advanced</span>
</div>
<p style="color: #64748b; font-size: 1.1rem !important; margin-bottom: 2rem;">
    Pandas 데이터 전처리 및 분석 역량 강화를 위한 실전 학습 시스템입니다.
</p>
''', unsafe_allow_html=True)

tabs = st.tabs(["📚 학습 모드 (Study)", "🎯 실전 모의고사 (Exam)", "🏆 명예의 전당"])

# ----------------- 📚 학습 모드 -----------------
with tabs[0]:
    st.info("💡 **학습 모드:** 문제를 제출하고 즉각 피드백을 받습니다. 최대 3번까지 재시도할 수 있으며, 3번 틀리면 해설이 공개됩니다.")
    
    if 's_quizzes' not in st.session_state:
        st.session_state.s_quizzes = generate_exam_cycle()
        st.session_state.s_idx = 0
        st.session_state.s_attempts = 0
        st.session_state.s_show_exp = False
        st.session_state.s_correct = False
        st.session_state.s_finished = False

    if st.session_state.s_finished:
        st.success("🎉 학습 사이클을 완주했습니다!")
        if st.button("새로운 문제 셋으로 학습 다시 시작", key="btn_study_reset"):
            st.session_state.s_quizzes = generate_exam_cycle()
            st.session_state.s_idx = 0
            st.session_state.s_attempts = 0
            st.session_state.s_show_exp = False
            st.session_state.s_correct = False
            st.session_state.s_finished = False
            st.rerun()
    else:
        s_idx = st.session_state.s_idx
        q = st.session_state.s_quizzes[s_idx]
        
        col1, col2 = st.columns([8, 2])
        with col1:
            st.progress((s_idx) / 20)
        with col2:
            if st.button("🔄 섞기", key="btn_study_shuffle", help="문제 세트를 다시 생성합니다."):
                st.session_state.s_quizzes = generate_exam_cycle()
                st.session_state.s_idx = 0
                st.session_state.s_attempts = 0
                st.session_state.s_show_exp = False
                st.session_state.s_correct = False
                st.rerun()
        
        with st.container(border=True):
            st.subheader(f"Question {s_idx+1:02d}. {q['topic']}")
            st.write(q['question'])
            
            user_ans = st.text_input("Answer code", placeholder="코드를 작성해 주세요", label_visibility="hidden", key=f"s_ans_{s_idx}")

        if not st.session_state.s_show_exp:
            if st.button("제출 및 채점", type="primary", key="btn_study_submit"):
                if not user_ans:
                    st.warning("답안을 입력해 주세요.")
                else:
                    is_correct = q['check'](user_ans)
                    if is_correct:
                        st.session_state.s_correct = True
                        st.session_state.s_show_exp = True
                    else:
                        st.session_state.s_attempts += 1
                        if st.session_state.s_attempts >= 3:
                            st.session_state.s_correct = False
                            st.session_state.s_show_exp = True
                    st.rerun()
            
            if st.session_state.s_attempts > 0 and not st.session_state.s_show_exp:
                st.error(f"❌ 오답입니다. 다시 시도해 보세요. (남은 기회: {3 - st.session_state.s_attempts}번)")
        else:
            if st.session_state.s_correct:
                st.success("✅ 정답입니다!")
            else:
                st.error("❌ 3회 오답으로 인해 해설이 공개됩니다.")
                
            with st.expander("해설 및 모범 답안", expanded=True):
                st.code(q['expected'], language='python')
                st.markdown(q['explanation'])
                
            if st.button("다음 문항으로 이동", type="primary", key="btn_study_next"):
                if s_idx + 1 >= 20:
                    st.session_state.s_finished = True
                else:
                    st.session_state.s_idx += 1
                    st.session_state.s_attempts = 0
                    st.session_state.s_show_exp = False
                    st.session_state.s_correct = False
                st.rerun()

# ----------------- 🎯 실전 모의고사 -----------------
with tabs[1]:
    st.info("🚨 **실전 모의고사:** 20문제를 한 번에 풀고 맨 아래에서 '최종 제출'을 눌러야 채점 결과와 성적표가 나옵니다.")
    
    if 'e_quizzes' not in st.session_state:
        st.session_state.e_quizzes = generate_exam_cycle()
        st.session_state.e_submitted = False
        st.session_state.e_score = 0
        st.session_state.e_user_answers = []

    if not st.session_state.e_submitted:
        if st.button("🔄 새로운 모의고사 시험지로 교체", key="btn_exam_shuffle"):
            st.session_state.e_quizzes = generate_exam_cycle()
            st.rerun()
            
        with st.form("exam_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.e_quizzes):
                st.markdown(f"**Q{i+1:02d}. {q['topic']}**")
                st.markdown(f"{q['question']}")
                ans = st.text_input(f"Answer {i+1}", label_visibility="hidden", key=f"exam_ans_{i}")
                user_answers.append(ans)
                st.markdown("---")
            
            submit_exam = st.form_submit_button("최종 답안 제출 및 채점하기", type="primary")
            
            if submit_exam:
                score = 0
                for i, q in enumerate(st.session_state.e_quizzes):
                    if user_answers[i] and q['check'](user_answers[i]):
                        score += 1
                st.session_state.e_score = score
                st.session_state.e_user_answers = user_answers
                st.session_state.e_submitted = True
                st.rerun()
    else:
        st.balloons()
        st.success(f"🎊 시험 종료! 최종 점수: {st.session_state.e_score} / 20 점")
        
        with st.container(border=True):
            st.subheader("🏆 리더보드 점수 등록")
            u_name = st.text_input("학습자 성함을 입력해 주세요:", key="exam_name")
            if st.button("점수 등록", type="primary", key="btn_exam_reg"):
                if u_name:
                    save_score(u_name, st.session_state.e_score)
                    st.success("등록 완료! '명예의 전당' 탭을 확인하세요.")
                else:
                    st.warning("이름을 입력해야 등록이 가능합니다.")
        
        st.markdown("### 📊 상세 성적표 (Report Card)")
        for i, q in enumerate(st.session_state.e_quizzes):
            u_ans = st.session_state.e_user_answers[i]
            is_cor = q['check'](u_ans) if u_ans else False
            
            css_class = "report-correct" if is_cor else "report-wrong"
            st.markdown(f'''<div class="{css_class}">
                <strong>Q{i+1:02d}. {q['topic']}</strong><br>
                내 답안: <code>{u_ans if u_ans else "미입력"}</code><br>
                정답: <code>{q['expected']}</code>
            </div>''', unsafe_allow_html=True)
            
        if st.button("🔄 모의고사 다시 풀기 (새로운 문제)"):
            st.session_state.e_quizzes = generate_exam_cycle()
            st.session_state.e_submitted = False
            st.session_state.e_score = 0
            st.session_state.e_user_answers = []
            st.rerun()

# ----------------- 🏆 명예의 전당 -----------------
with tabs[2]:
    st.subheader("Leaderboard")
    lb = load_leaderboard()
    if not lb:
        st.info("현재 등록된 평가 기록이 없습니다.")
    else:
        df_lb = pd.DataFrame(lb)
        df_lb.index = df_lb.index + 1
        if 'created_at' in df_lb.columns:
            df_lb['created_at'] = pd.to_datetime(df_lb['created_at']).dt.strftime('%Y-%m-%d %H:%M')
            df_lb = df_lb[['name', 'score', 'created_at']]
        else:
            df_lb = df_lb[['name', 'score', 'date']]
        df_lb.columns = ['학습자', '최종 스코어', '평가 일시']
        st.dataframe(df_lb, use_container_width=True)

st.markdown('''
<div class="custom-footer">
    © 2026 Data Analysis Bootcamp. All rights reserved.<br>
    Powered by Python & Streamlit
</div>
''', unsafe_allow_html=True)
