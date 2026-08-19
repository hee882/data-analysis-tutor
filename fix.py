import os
import base64

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
main_path = os.path.join(repo_path, 'web_pandas_tutor.py')
style_path = os.path.join(repo_path, 'src', 'style.py')
img_path = r'C:\Users\user\.gemini\antigravity-cli\brain\40d9afaf-7f02-4b4e-8221-9a93704dd5d8\data_science_logo_1787121178349.jpg'

with open(img_path, 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. Update style.py
with open(style_path, 'r', encoding='utf-8') as f:
    style_content = f.read()

# Replace or add HUD badge CSS
if '.hud-badge' not in style_content:
    hud_badge_css = """
/* 작은 상태 대시보드 (우측 정렬용 뱃지) */
.hud-container { display: flex; justify-content: flex-end; gap: 0.8rem; margin-bottom: 1rem; }
.hud-badge {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.9);
    padding: 0.4rem 1rem;
    border-radius: 99px;
    font-size: 0.9rem;
    font-weight: 700;
    color: #1e293b;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}
.hud-badge span { color: #3b82f6; font-weight: 800; margin-left: 0.3rem; }
"""
    style_content = style_content.replace('</style>', hud_badge_css + '\n</style>')
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(style_content)

# 2. Re-write web_pandas_tutor.py entirely to fix ???
main_content = f"""import streamlit as st
import time
import pandas as pd
from datetime import datetime

# 모듈 임포트
from src.style import get_custom_css
from src.db import load_leaderboard, save_score
from src.timer import inject_timer, remove_timer
from src.questions import generate_exam_quizzes, generate_single_quiz

st.set_page_config(page_title="Data Science & ML Bootcamp", layout="wide", initial_sidebar_state="collapsed")
st.markdown(get_custom_css(), unsafe_allow_html=True)

# 메인 페이지 헤더 (아이콘 + 제목)
st.markdown(f'''
<div class="custom-header" style="justify-content: flex-start; gap: 1rem;">
    <img src="data:image/jpeg;base64,{img_b64}" style="width: 45px; height: 45px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <div style="display: flex; flex-direction: column;">
        <h2 style="margin: 0 !important; font-size: 1.5rem !important; font-weight: 800 !important; color: #0f172a;">
            Data Science & ML Bootcamp
        </h2>
        <span style="font-size: 0.85rem; font-weight: 500; color: #64748b;">Python, Pandas, Scikit-learn을 활용한 데이터 분석 및 머신러닝 실전 훈련</span>
    </div>
</div>
''', unsafe_allow_html=True)

tabs = st.tabs(["📚 학습 모드 (Study)", "🎯 실전 모의고사 (Exam)", "🏆 명예의 전당"])

with tabs[0]:
    remove_timer()
    
    if 's_total_solved' not in st.session_state:
        st.session_state.s_total_solved = 0
        st.session_state.s_total_correct = 0
        st.session_state.s_current_q = generate_single_quiz()
        st.session_state.s_attempts = 0
        st.session_state.s_show_exp = False
        st.session_state.s_correct = False

    acc = (st.session_state.s_total_correct / st.session_state.s_total_solved * 100) if st.session_state.s_total_solved > 0 else 0
    
    # 상단 HUD (우측 작게 배치)
    st.markdown(f'''
    <div class="hud-container">
        <div class="hud-badge">✅ 누적 완료: <span>{{st.session_state.s_total_solved}}</span> 개</div>
        <div class="hud-badge">🎯 1트 정답률: <span>{{acc:.1f}}</span> %</div>
    </div>
    ''', unsafe_allow_html=True)
    
    q = st.session_state.s_current_q
    
    with st.container(border=True):
        st.markdown(f"**Q. {{q['topic']}}** " + ("(주관식 ⌨️)" if q['type'] == 'text' else "(객관식 🖱️)"))
        st.markdown(f"{{q['question']}}")
        
        if q['type'] == 'radio':
            user_ans = st.radio("보기 선택", options=q['choices'], label_visibility="hidden", key=f"s_ans_endless", index=None)
        else:
            user_ans = st.text_input("직접 타이핑하여 코드를 완성하세요", placeholder="코드를 입력하세요", label_visibility="hidden", key=f"s_ans_endless")

    if not st.session_state.s_show_exp:
        if st.button("제출 및 채점", type="primary", key="btn_study_submit", use_container_width=True):
            if not user_ans:
                st.warning("답안을 입력하거나 보기를 선택해 주세요.")
            else:
                if q['type'] == 'radio':
                    is_correct = (user_ans == q['expected'])
                else:
                    is_correct = q['check'](user_ans)

                if is_correct:
                    st.session_state.s_correct = True
                    st.session_state.s_show_exp = True
                    st.session_state.s_total_solved += 1
                    if st.session_state.s_attempts == 0:
                        st.session_state.s_total_correct += 1
                else:
                    st.session_state.s_attempts += 1
                    if st.session_state.s_attempts >= 3:
                        st.session_state.s_correct = False
                        st.session_state.s_show_exp = True
                        st.session_state.s_total_solved += 1
            st.rerun()
            
        if st.session_state.s_attempts > 0 and not st.session_state.s_show_exp:
            st.error(f"❌ 오답입니다. (남은 기회: {{3 - st.session_state.s_attempts}}번)")
    else:
        if st.session_state.s_correct:
            st.success("✅ 정답입니다!")
        else:
            st.error("❌ 3회 오답. 해설 공개.")
            
        with st.expander("해설 및 모범 답안", expanded=True):
            st.code(q['expected'], language='python')
            st.markdown(q['explanation'])
            
        if st.button("⏭️ 다음 문제 (Endless)", type="primary", key="btn_study_next", use_container_width=True):
            st.session_state.s_current_q = generate_single_quiz()
            st.session_state.s_attempts = 0
            st.session_state.s_show_exp = False
            st.session_state.s_correct = False
            st.rerun()

with tabs[1]:
    if 'exam_state' not in st.session_state:
        st.session_state.exam_state = 'landing'
        st.session_state.e_quizzes = generate_exam_quizzes()
        st.session_state.e_score = 0
        st.session_state.e_user_answers = []
        st.session_state.exam_name = ""
        st.session_state.exam_start_time = 0
        st.session_state.exam_end_time = 0

    if st.session_state.exam_state == 'landing':
        remove_timer()
        with st.container(border=True):
            st.markdown('''
            <div style="text-align: center; padding: 1rem;">
                <h3 style="margin-bottom:0.5rem; color:#0f172a;">🚨 실전 모의고사</h3>
                <p style="color: #64748b; font-size:0.9rem;">20문항 (객관식 18, 주관식 2) | 제한 시간 40분</p>
            </div>
            ''', unsafe_allow_html=True)
            
            candidate_name = st.text_input("수험자 이름(ID):", placeholder="홍길동", label_visibility="collapsed")
            
            if st.button("▶️ 모의고사 응시 시작", type="primary", use_container_width=True):
                if candidate_name.strip():
                    st.session_state.exam_name = candidate_name.strip()
                    st.session_state.e_quizzes = generate_exam_quizzes()
                    st.session_state.exam_start_time = time.time()
                    st.session_state.exam_state = 'running'
                    st.rerun()
                else:
                    st.warning("이름을 입력하세요.")

    elif st.session_state.exam_state == 'running':
        inject_timer(2400, st.session_state.exam_start_time)
        st.markdown(f"수험자: **{{st.session_state.exam_name}}** 님")
        
        with st.form("exam_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.e_quizzes):
                st.markdown(f"**Q{{i+1:02d}}. {{q['topic']}}** " + ("(주관식 ⌨️)" if q['type'] == 'text' else "(객관식 🖱️)"))
                st.markdown(f"{{q['question']}}")
                
                if q['type'] == 'radio':
                    ans = st.radio(f"보기 {{i+1}}", options=q['choices'], label_visibility="hidden", key=f"exam_ans_{{i}}", index=None)
                else:
                    ans = st.text_input(f"답안 {{i+1}}", placeholder="코드를 직접 타이핑하세요", label_visibility="hidden", key=f"exam_ans_{{i}}")
                    
                user_answers.append(ans)
                st.markdown("---")
            
            if st.form_submit_button("최종 답안 제출", type="primary", use_container_width=True):
                st.session_state.exam_end_time = time.time()
                score = 0
                for i, q in enumerate(st.session_state.e_quizzes):
                    if user_answers[i]:
                        if q['type'] == 'radio':
                            if user_answers[i] == q['expected']:
                                score += 1
                        else:
                            if q['check'](user_answers[i]):
                                score += 1
                st.session_state.e_score = score
                st.session_state.e_user_answers = user_answers
                save_score(st.session_state.exam_name, st.session_state.e_score)
                st.session_state.exam_state = 'finished'
                st.rerun()

    elif st.session_state.exam_state == 'finished':
        remove_timer()
        st.balloons()
        elapsed_sec = int(st.session_state.exam_end_time - st.session_state.exam_start_time)
        m, s = divmod(elapsed_sec, 60)
        
        st.success("🎊 시험이 종료되었습니다.")
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label="수험자", value=st.session_state.exam_name)
        col2.metric(label="점수", value=f"{{st.session_state.e_score}}/20")
        col3.metric(label="시간", value=f"{{m}}분 {{s}}초")
        
        with st.expander("상세 성적표 보기"):
            for i, q in enumerate(st.session_state.e_quizzes):
                u_ans = st.session_state.e_user_answers[i]
                if not u_ans:
                    is_cor = False
                elif q['type'] == 'radio':
                    is_cor = (u_ans == q['expected'])
                else:
                    is_cor = q['check'](u_ans)
                    
                css_class = "report-correct" if is_cor else "report-wrong"
                st.markdown(f'''<div class="{{css_class}}">
                    <strong>Q{{i+1:02d}}. {{q['topic']}}</strong><br>
                    내 답: <code>{{u_ans if u_ans else "미입력"}}</code><br>
                    정답: <code>{{q['expected']}}</code>
                </div>''', unsafe_allow_html=True)
            
        if st.button("🔄 새로운 모의고사 응시", use_container_width=True):
            st.session_state.exam_state = 'landing'
            st.session_state.e_score = 0
            st.session_state.e_user_answers = []
            st.rerun()

with tabs[2]:
    remove_timer()
    lb = load_leaderboard()
    if not lb:
        st.info("기록이 없습니다.")
    else:
        df_lb = pd.DataFrame(lb)
        df_lb.index = df_lb.index + 1
        if 'created_at' in df_lb.columns:
            df_lb['created_at'] = pd.to_datetime(df_lb['created_at']).dt.strftime('%Y-%m-%d %H:%M')
            df_lb = df_lb[['name', 'score', 'created_at']]
        else:
            df_lb = df_lb[['name', 'score', 'date']]
        df_lb.columns = ['수험자', '스코어', '일시']
        st.dataframe(df_lb, use_container_width=True)
"""

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_content)
