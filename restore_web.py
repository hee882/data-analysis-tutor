import os
import base64

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
main_path = os.path.join(repo_path, 'web_pandas_tutor.py')
style_path = os.path.join(repo_path, 'src', 'style.py')
q_path = os.path.join(repo_path, 'src', 'questions.py')
img_path = r'C:\Users\user\.gemini\antigravity-cli\brain\40d9afaf-7f02-4b4e-8221-9a93704dd5d8\data_science_logo_1787121178349.jpg'

with open(img_path, 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# 1. web_pandas_tutor.py
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

# 플러그인 전략 선택기 (Sidebar)
with st.sidebar:
    st.markdown("### ⚙️ 학습 모드 설정")
    selected_mode = st.radio(
        "출제 범위 선택",
        options=["bootcamp_day1_4", "comprehensive"],
        format_func=lambda x: "🎓 Day 1~4 시험 대비" if x == "bootcamp_day1_4" else "🔥 종합 마스터 (전범위)",
        key="strategy_selector"
    )
    if selected_mode == "bootcamp_day1_4":
        st.caption("부트캠프 진도에 맞춘 핵심 모드")
    else:
        st.caption("데이터 분석 전 분야 딥다이브")

    if 'current_strategy' not in st.session_state or st.session_state.current_strategy != selected_mode:
        st.session_state.current_strategy = selected_mode
        # 전략이 바뀌면 문제 초기화
        st.session_state.s_current_q = generate_single_quiz(selected_mode)
        st.session_state.exam_state = 'landing'
        st.session_state.e_quizzes = generate_exam_quizzes(selected_mode)

# 메인 페이지 헤더 (중앙 정렬 로고 + 제목 + 부제)
st.markdown(f'''
<div class="custom-header">
    <div class="header-top-row">
        <img src="data:image/jpeg;base64,{img_b64}" class="header-logo">
        <h2 class="header-title">Data Science & ML Bootcamp</h2>
    </div>
    <div class="header-subtitle">Python, Pandas, Scikit-learn을 활용한 데이터 분석 및 머신러닝 실전 훈련</div>
</div>
''', unsafe_allow_html=True)

tabs = st.tabs(["📚 학습", "🚨 모의고사", "🏆 랭킹"])

with tabs[0]:
    remove_timer()
    
    if 's_total_solved' not in st.session_state:
        st.session_state.s_total_solved = 0
        st.session_state.s_total_correct = 0
        st.session_state.s_current_q = generate_single_quiz(st.session_state.current_strategy)
        st.session_state.s_attempts = 0
        st.session_state.s_show_exp = False
        st.session_state.s_correct = False

    acc = (st.session_state.s_total_correct / st.session_state.s_total_solved * 100) if st.session_state.s_total_solved > 0 else 0
    
    # 상단 HUD (우측 뱃지)
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
            
        exp_html = f'''
        <div class="floating-exp">
            <h4 style="margin-top:0; margin-bottom:0.8rem; color:#3b82f6;">💡 해설 및 모범 답안</h4>
            <div style="background:#1e293b; padding:1rem; border-radius:12px; margin-bottom:1rem; font-family:'JetBrains Mono', monospace; color:#e2e8f0; font-size:0.95rem; line-height:1.4;">
                {{q['expected']}}
            </div>
            <p style="font-weight:600; font-size:1rem; color:#334155; word-break:keep-all;">{{q['explanation']}}</p>
        </div>
        '''
        st.markdown(exp_html, unsafe_allow_html=True)
            
        if st.button("⏭️ 다음 문제 (Endless)", type="primary", key="btn_study_next", use_container_width=True):
            st.session_state.s_current_q = generate_single_quiz(st.session_state.current_strategy)
            st.session_state.s_attempts = 0
            st.session_state.s_show_exp = False
            st.session_state.s_correct = False
            st.rerun()

with tabs[1]:
    if 'exam_state' not in st.session_state:
        st.session_state.exam_state = 'landing'
        st.session_state.e_quizzes = generate_exam_quizzes(st.session_state.current_strategy)
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
                    st.session_state.e_quizzes = generate_exam_quizzes(st.session_state.current_strategy)
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
                save_score(st.session_state.exam_name, st.session_state.e_score, st.session_state.current_strategy)
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
    st.markdown("<h3 style='text-align: center; margin-bottom: 0.5rem;'>🏆 명예의 전당</h3>", unsafe_allow_html=True)
    
    # 리더보드 모드 스위처
    lb_mode = st.radio("리더보드 카테고리", ["bootcamp_day1_4", "comprehensive"], 
                       format_func=lambda x: "🎓 Day 1~4 (기초)" if x == "bootcamp_day1_4" else "🔥 종합 마스터", 
                       horizontal=True, label_visibility="collapsed")
    
    lb = load_leaderboard()
    
    # 파싱 및 필터링
    filtered_lb = []
    for row in lb:
        raw_name = row['name']
        if "###" in raw_name:
            parsed_name, strategy = raw_name.split("###", 1)
        else:
            parsed_name, strategy = raw_name, "bootcamp_day1_4" # 레거시 데이터 기본값
            
        if strategy == lb_mode:
            row['display_name'] = parsed_name
            filtered_lb.append(row)
            
    if not filtered_lb:
        st.info("해당 모드의 기록이 없습니다. 첫 번째 명예의 전당에 도전하세요!")
    else:
        df_lb = pd.DataFrame(filtered_lb)
        df_lb = df_lb.sort_values(by='score', ascending=False).reset_index(drop=True)
        
        html = '<div class="lb-container">'
        for i, row in df_lb.iterrows():
            rank = i + 1
            rank_class = f"lb-rank-{{rank}}" if rank <= 3 else ""
            rank_display = ["🥇", "🥈", "🥉"][rank-1] if rank <= 3 else f"{{rank}}"
            
            name = row['display_name']
            score = row['score']
            date = pd.to_datetime(row['created_at'] if 'created_at' in row else row['date']).strftime('%y.%m.%d %H:%M')
            
            html += f'''
            <div class="lb-row">
                <div class="lb-rank {{rank_class}}">{{rank_display}}</div>
                <div class="lb-name">{{name}}</div>
                <div class="lb-score">{{score}} / 20</div>
                <div class="lb-date">{{date}}</div>
            </div>
            '''
        html += '</div>'
        
        st.markdown(html, unsafe_allow_html=True)
"""
with open(main_path, 'w', encoding='utf-8') as f:
    f.write(main_content)

print("web_pandas_tutor.py restored!")
