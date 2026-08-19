import streamlit as st
import time
import pandas as pd
from datetime import datetime

# ?? ???
from src.style import get_custom_css
from src.db import load_leaderboard, save_score
from src.timer import inject_timer, remove_timer
from src.questions import generate_exam_quizzes, generate_single_quiz

st.set_page_config(page_title="Data Science Bootcamp", layout="wide", initial_sidebar_state="collapsed")
st.markdown(get_custom_css(), unsafe_allow_html=True)

st.markdown("""
<div class="custom-header">
    <h2>?? Data Science & ML Bootcamp</h2>
    <span>Lv.1 Basic & Advanced</span>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["?? ?? ?? (Study)", "?? ?? ???? (Exam)", "?? ??? ??"])

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
    
    # ?? ??? (? ?? ?????)
    colA, colB = st.columns(2)
    with colA:
        st.markdown(f"<div class='hud-box'><div class='hud-title'>? ?? ??</div><div class='hud-value'>{st.session_state.s_total_solved} ?</div></div>", unsafe_allow_html=True)
    with colB:
        st.markdown(f"<div class='hud-box'><div class='hud-title' style='color:#10b981;'>?? 1? ???</div><div class='hud-value'>{acc:.1f} %</div></div>", unsafe_allow_html=True)
    
    q = st.session_state.s_current_q
    
    with st.container(border=True):
        st.markdown(f"**Q. {q['topic']}** " + ("(??? ??)" if q['type'] == 'text' else "(??? ???)"))
        st.markdown(f"{q['question']}")
        
        if q['type'] == 'radio':
            user_ans = st.radio("?? ??", options=q['choices'], label_visibility="hidden", key=f"s_ans_endless", index=None)
        else:
            user_ans = st.text_input("?? ????? ??? ?????", placeholder="??? ?????", label_visibility="hidden", key=f"s_ans_endless")

    if not st.session_state.s_show_exp:
        if st.button("?? ? ??", type="primary", key="btn_study_submit", use_container_width=True):
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
            st.error(f"? ?????. (?? ??: {3 - st.session_state.s_attempts}?)")
    else:
        if st.session_state.s_correct:
            st.success("? ?????!")
        else:
            st.error("? 3? ??. ?? ??.")
            
        with st.expander("?? ? ?? ??", expanded=True):
            st.code(q['expected'], language='python')
            st.markdown(q['explanation'])
            
        if st.button("?? ?? ?? (Endless)", type="primary", key="btn_study_next", use_container_width=True):
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
            st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h3 style="margin-bottom:0.5rem; color:#0f172a;">?? ?? ????</h3>
                <p style="color: #64748b; font-size:0.9rem;">20?? (??? 18, ??? 2) | ?? ?? 40?</p>
            </div>
            """, unsafe_allow_html=True)
            
            candidate_name = st.text_input("??? ??(ID):", placeholder="???", label_visibility="collapsed")
            
            if st.button("?? ???? ?? ??", type="primary", use_container_width=True):
                if candidate_name.strip():
                    st.session_state.exam_name = candidate_name.strip()
                    st.session_state.e_quizzes = generate_exam_quizzes()
                    st.session_state.exam_start_time = time.time()
                    st.session_state.exam_state = 'running'
                    st.rerun()
                else:
                    st.warning("??? ?????.")

    elif st.session_state.exam_state == 'running':
        inject_timer(2400, st.session_state.exam_start_time)
        st.markdown(f"???: **{st.session_state.exam_name}** ?")
        
        with st.form("exam_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.e_quizzes):
                st.markdown(f"**Q{i+1:02d}. {q['topic']}** " + ("(??? ??)" if q['type'] == 'text' else "(??? ???)"))
                st.markdown(f"{q['question']}")
                
                if q['type'] == 'radio':
                    ans = st.radio(f"?? {i+1}", options=q['choices'], label_visibility="hidden", key=f"exam_ans_{i}", index=None)
                else:
                    ans = st.text_input(f"?? {i+1}", placeholder="??? ?? ??????", label_visibility="hidden", key=f"exam_ans_{i}")
                    
                user_answers.append(ans)
                st.markdown("---")
            
            if st.form_submit_button("?? ?? ??", type="primary", use_container_width=True):
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
        
        st.success("?? ??? ???????.")
        
        col1, col2, col3 = st.columns(3)
        col1.metric(label="???", value=st.session_state.exam_name)
        col2.metric(label="??", value=f"{st.session_state.e_score}/20")
        col3.metric(label="??", value=f"{m}? {s}?")
        
        with st.expander("?? ??? ??"):
            for i, q in enumerate(st.session_state.e_quizzes):
                u_ans = st.session_state.e_user_answers[i]
                if not u_ans:
                    is_cor = False
                elif q['type'] == 'radio':
                    is_cor = (u_ans == q['expected'])
                else:
                    is_cor = q['check'](u_ans)
                    
                css_class = "report-correct" if is_cor else "report-wrong"
                st.markdown(f"""<div class="{css_class}">
                    <strong>Q{i+1:02d}. {q['topic']}</strong><br>
                    ? ?: <code>{u_ans if u_ans else "???"}</code><br>
                    ??: <code>{q['expected']}</code>
                </div>""", unsafe_allow_html=True)
            
        if st.button("?? ??? ???? ??", use_container_width=True):
            st.session_state.exam_state = 'landing'
            st.session_state.e_score = 0
            st.session_state.e_user_answers = []
            st.rerun()

with tabs[2]:
    remove_timer()
    lb = load_leaderboard()
    if not lb:
        st.info("??? ????.")
    else:
        df_lb = pd.DataFrame(lb)
        df_lb.index = df_lb.index + 1
        if 'created_at' in df_lb.columns:
            df_lb['created_at'] = pd.to_datetime(df_lb['created_at']).dt.strftime('%Y-%m-%d %H:%M')
            df_lb = df_lb[['name', 'score', 'created_at']]
        else:
            df_lb = df_lb[['name', 'score', 'date']]
        df_lb.columns = ['???', '???', '??']
        st.dataframe(df_lb, use_container_width=True)
