import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Pandas 실전 튜터", layout="wide")

st.title("🚀 HDAT-DA 대비 Pandas 실전 튜터")
st.markdown("데이터 분석 시험(HDAT-DA)에 자주 출제되는 Pandas 핵심 문법을 모의고사 형태로 훈련하는 대화형 웹 튜터입니다.")

# 퀴즈 데이터베이스
QUIZ_BANK = [
    {
        'topic': '데이터프레임 병합 (Merge)',
        'question': "두 개의 데이터프레임을 공통 컬럼(예: 'ID') 기준으로 병합하려고 합니다. SQL의 JOIN과 동일한 역할을 하는 Pandas 함수는?",
        'options': ["pd.concat()", "pd.merge()", "pd.append()", "df.groupby()"],
        'answer': "pd.merge()",
        'explanation': "`pd.merge(df1, df2, on='ID')`는 두 데이터프레임을 특정 컬럼 기준으로 가로로 병합할 때 사용됩니다."
    },
    {
        'topic': '결측치 처리 (Missing Values)',
        'question': "데이터프레임 `df`에서 결측치(NaN)가 하나라도 포함된 모든 '행(row)'을 삭제하는 올바른 코드는?",
        'options': ["df.fillna(0)", "df.dropna(axis=0)", "df.dropna(axis=1)", "df.drop(0)"],
        'answer': "df.dropna(axis=0)",
        'explanation': "`dropna(axis=0)`은 결측치가 있는 행(가로)을 삭제하며, `axis=1`은 열(세로)을 삭제합니다."
    },
    {
        'topic': '그룹화 및 집계 (Groupby)',
        'question': "데이터를 'Category' 컬럼 기준으로 그룹화하고, 'Price' 컬럼의 평균을 구하는 올바른 코드는?",
        'options': [
            "df.groupby('Category')['Price'].mean()", 
            "df.groupby('Price')['Category'].mean()", 
            "df.sort_values('Category').mean()", 
            "df['Price'].mean(groupby='Category')"
        ],
        'answer': "df.groupby('Category')['Price'].mean()",
        'explanation': "`groupby('기준컬럼')['계산할컬럼'].집계함수()` 형태가 Pandas 그룹화의 핵심 공식입니다."
    },
    {
        'topic': '조건부 필터링 (Boolean Indexing)',
        'question': "나이('Age')가 30 이상이면서 성별('Sex')이 'M'인 데이터만 추출하려고 합니다. 올바른 조건식은?",
        'options': [
            "df[(df['Age'] >= 30) and (df['Sex'] == 'M')]",
            "df[(df['Age'] >= 30) & (df['Sex'] == 'M')]",
            "df[df['Age'] >= 30 & df['Sex'] == 'M']",
            "df.filter(Age >= 30, Sex == 'M')"
        ],
        'answer': "df[(df['Age'] >= 30) & (df['Sex'] == 'M')]",
        'explanation': "Pandas 조건식에서 '그리고'는 `and` 대신 `&`를 사용해야 하며, 각 조건은 반드시 괄호 `()`로 묶어야 합니다."
    }
]

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = False

if st.session_state.current_q < len(QUIZ_BANK):
    q = QUIZ_BANK[st.session_state.current_q]
    
    st.subheader(f"Q{st.session_state.current_q + 1}. {q['topic']}")
    st.write(q['question'])
    
    choice = st.radio("정답을 선택하세요:", q['options'], key=f"q_{st.session_state.current_q}")
    
    if st.button("제출 및 정답 확인"):
        st.session_state.show_explanation = True
        if choice == q['answer']:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"❌ 오답입니다. (정답: {q['answer']})")
            
    if st.session_state.show_explanation:
        st.info(q['explanation'])
        if st.button("다음 문제로 넘어가기"):
            st.session_state.current_q += 1
            st.session_state.show_explanation = False
            st.rerun()

else:
    st.success(f"🎉 모든 퀴즈를 완료했습니다! 최종 점수: {st.session_state.score} / {len(QUIZ_BANK)}")
    if st.button("다시 시작하기"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.show_explanation = False
        st.rerun()

st.sidebar.title("👨‍🏫 HDAT-DA 과외 선생님")
st.sidebar.markdown("이 웹 튜터를 통해 시험 전 Pandas 기초 체력을 기르세요!")
st.sidebar.markdown("실전 모의고사 및 데이터 학습은 `universal_exam.py`를 활용하시면 됩니다.")
