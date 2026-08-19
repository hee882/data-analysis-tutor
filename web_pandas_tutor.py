import streamlit as st
import time
import pandas as pd
from datetime import datetime

# 모듈 임포트
from src.style import get_custom_css
from src.db import load_leaderboard, save_score
from src.timer import inject_timer, remove_timer
from src.questions import generate_exam_quizzes, generate_single_quiz

st.set_page_config(page_title="Data Analysis Tutor", layout="wide", initial_sidebar_state="collapsed")
st.markdown(get_custom_css(), unsafe_allow_html=True)

st.markdown('''
<div class="custom-header">
    <h2>📊 Data Science & ML Bootcamp</h2>
    <span>Lv.1 Basic & Advanced</span>
</div>
<p style="color: #64748b; font-size: 1.1rem !important; margin-bottom: 2rem;">
    Python, Numpy, Pandas부터 Scikit-learn, 데이터 시각화까지 데이터 분석 및 머신러닝 실전 역량 강화를 위한 실전 객관식/주관식 혼합 학습 시스템입니다.
</p>
''', unsafe_allow_html=True)

tabs = st.tabs(["📚 학습 모드 (Study)", "🎯 실전 모의고사 (Exam)", "🏆 명예의 전당"])

with tabs[0]:
    remove_timer()
    st.info("?? **???? ?? ??:** ???? ???? ???????. ??? ????? ??? ?? ?????. (?? 3? ??? ??)")
    
    if 's_total_solved' not in st.session_state:
        st.session_state.s_total_solved = 0
        st.session_state.s_total_correct = 0
        st.session_state.s_current_q = generate_single_quiz()
        st.session_state.s_attempts = 0
        st.session_state.s_show_exp = False
        st.session_state.s_correct = False

    acc = (st.session_state.s_total_correct / st.session_state.s_total_solved * 100) if st.session_state.s_total_solved > 0 else 0
    
    # ?? ???
    colA, colB = st.columns(2)
    with colA:
        st.markdown(f"<div style='background:rgba(255,255,255,0.4); padding:1rem; border-radius:12px; border:1px solid rgba(255,255,255,0.5);'><strong style='font-size:1.2rem; color:#3b82f6;'>? ?? ?? ?</strong><br><span style='font-size:1.8rem; font-weight:800;'>{st.session_state.s_total_solved}</span> ?</div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div style='background:rgba(255,255,255,0.4); padding:1rem; border-radius:12px; border:1px solid rgba(255,255,255,0.5);'><strong style='font-size:1.2rem; color:#10b981;'>?? ? ?? ???</strong><br><span style='font-size:1.8rem; font-weight:800;'>{acc:.1f}</span> %</div>", unsafe_allow_html=True)
    st.write("")
    
    q = st.session_state.s_current_q
    
    with st.container(border=True):
        st.subheader(f"Q. {q['topic']} " + ("(??? ??)" if q['type'] == 'text' else "(??? ???)"))
        st.write(q['question'])
        
        if q['type'] == 'radio':
            user_ans = st.radio("?? ??", options=q['choices'], label_visibility="hidden", key=f"s_ans_endless", index=None)
        else:
            user_ans = st.text_input("?? ????? ??? ?????", placeholder="??? ?????", label_visibility="hidden", key=f"s_ans_endless")

    if not st.session_state.s_show_exp:
        if st.button("?? ? ??", type="primary", key="btn_study_submit"):
            if not user_ans:
                st.warning("??? ????? ??? ??? ???.")
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
            st.error(f"? ?????. ?? ??? ???. (?? ??: {3 - st.session_state.s_attempts}?)")
    else:
        if st.session_state.s_correct:
            st.success("? ?????!")
        else:
            st.error("? 3? ???? ?? ??? ?????.")
            
        with st.expander("?? ? ?? ??", expanded=True):
            st.code(q['expected'], language='python')
            st.markdown(q['explanation'])
            
        if st.button("?? ?? ??? ?? ?? (Endless)", type="primary", key="btn_study_next"):
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
            <div class="landing-box">
                <h3>🚨 데이터 전처리 실전 모의고사</h3>
                <p style="color: #64748b; margin-top: 1rem;">본 모의고사는 실무 환경과 동일한 조건에서 역량을 평가하기 위해 시간 제한이 적용됩니다.<br><b>객관식 18문항, 주관식 2문항</b>이 출제됩니다.</p>
                <div class="stats">
                    <div class="stat-item"><strong>20</strong>문항 수</div>
                    <div class="stat-item"><strong>40</strong>제한 시간 (분)</div>
                    <div class="stat-item"><strong>100</strong>만점 점수</div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            candidate_name = st.text_input("수험자 이름(ID)을 입력하세요:", placeholder="홍길동")
            
            if st.button("▶️ 모의고사 응시 시작", type="primary"):
                if candidate_name.strip():
                    st.session_state.exam_name = candidate_name.strip()
                    st.session_state.e_quizzes = generate_exam_quizzes()
                    st.session_state.exam_start_time = time.time()
                    st.session_state.exam_state = 'running'
                    st.rerun()
                else:
                    st.warning("수험자 이름을 반드시 입력해야 시작할 수 있습니다.")

    elif st.session_state.exam_state == 'running':
        inject_timer(2400, st.session_state.exam_start_time)
        st.markdown(f"수험자: **{st.session_state.exam_name}** 님")
        st.markdown("---")
        
        with st.form("exam_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.e_quizzes):
                st.markdown(f"**Q{i+1:02d}. {q['topic']}** " + ("(주관식 ⌨️)" if q['type'] == 'text' else "(객관식 🖱️)"))
                st.markdown(f"{q['question']}")
                
                if q['type'] == 'radio':
                    ans = st.radio(f"보기 {i+1}", options=q['choices'], label_visibility="hidden", key=f"exam_ans_{i}", index=None)
                else:
                    ans = st.text_input(f"답안 {i+1}", placeholder="코드를 직접 타이핑하세요", label_visibility="hidden", key=f"exam_ans_{i}")
                    
                user_answers.append(ans)
                st.markdown("---")
            
            if st.form_submit_button("최종 답안 제출 및 채점하기", type="primary"):
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
        
        st.success("🎊 시험이 종료되었습니다. (리더보드 자동 등록 완료)")
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label="수험자", value=st.session_state.exam_name)
        col2.metric(label="최종 점수", value=f"{st.session_state.e_score} / 20")
        col3.metric(label="소요 시간", value=f"{m}분 {s}초")
        
        st.markdown("### 📊 상세 성적표 (Report Card)")
        for i, q in enumerate(st.session_state.e_quizzes):
            u_ans = st.session_state.e_user_answers[i]
            if not u_ans:
                is_cor = False
            elif q['type'] == 'radio':
                is_cor = (u_ans == q['expected'])
            else:
                is_cor = q['check'](u_ans)
                
            css_class = "report-correct" if is_cor else "report-wrong"
            st.markdown(f'''<div class="{css_class}">
                <strong>Q{i+1:02d}. {q['topic']}</strong><br>
                내 답안: <code>{u_ans if u_ans else "미입력"}</code><br>
                정답: <code>{q['expected']}</code>
            </div>''', unsafe_allow_html=True)
            
        if st.button("🔄 새로운 모의고사 다시 응시하기"):
            st.session_state.exam_state = 'landing'
            st.session_state.e_score = 0
            st.session_state.e_user_answers = []
            st.rerun()

with tabs[2]:
    remove_timer()
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
        df_lb.columns = ['수험자', '최종 스코어', '평가 일시']
        st.dataframe(df_lb, use_container_width=True)

st.markdown('''<div class="custom-footer">© 2026 Data Science & ML Bootcamp. All rights reserved.</div>''', unsafe_allow_html=True)

