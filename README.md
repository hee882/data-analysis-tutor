# 🚀 Data Science & ML Bootcamp

<div align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/version-v1.0.0-success.svg?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License">
</div>



이 프로젝트는 파이썬 기반 데이터 분석 및 머신러닝의 풀스택 생태계(Python, Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn)를 마스터하기 위한 **실전형 모의고사 및 부트캠프 시스템**입니다. 

단순히 문법을 외우는 것을 넘어, 실무 현업에서 마주치는 실제 데이터를 어떻게 다룰 것인지, 그리고 치명적인 에러(Troubleshooting)를 어떻게 대처할 것인지를 훈련합니다.

---

## 🎯 핵심 타겟 커리큘럼 생태계 (Target Stack)
이 시스템은 특정 라이브러리에 국한되지 않으며, **데이터 사이언티스트/분석가**가 갖춰야 할 아래의 풀스택 도구들을 훈련시킵니다.
1. **Python Base:** 기초 프로그래밍 및 자료구조
2. **Numpy / Pandas:** 고성능 수치 연산 및 정형 데이터 랭글링(Data Wrangling)
3. **Matplotlib / Seaborn:** 데이터 시각화 및 탐색적 데이터 분석(EDA)
4. **Scikit-learn:** 머신러닝 모델링(전처리, 분할, 평가) 및 파이프라인 구축

---

## 🎲 설계 철학 및 출제 원리 (Design Philosophy)
본 프로젝트는 시스템의 확장성과 문제의 변별력을 유지하기 위해 아래의 **3대 철학**을 기반으로 설계되었습니다. 추후 코드를 수정하거나 문제 은행을 확장할 때, 반드시 이 원칙을 준수해야 합니다.

### 1. 상황 기반 난수화 (Scenario-based Randomization)
문제를 출제할 때 단순한 숫자(N)만 바꾸는 무의미한 난수화 방식을 금지합니다.
**현업에서 마주치는 요구사항, 에러 메시지, 절차적 맥락을 Dictionary Array(풀)로 구축**하여 무작위 추출(`random.choice`)해야 합니다.
- **파라미터 튜닝:** "교집합만 병합하라" vs "왼쪽 테이블 기준으로 병합하라" 등 상황을 난수화.
- **파이프라인 시퀀스:** "시계열 분석" vs "머신러닝 전처리" 등 분석 타겟을 바꾸어 정답 절차를 동적으로 변경.
- **장애 트러블슈팅:** `MemoryError`, `UnicodeDecodeError` 등 실무 에러 상황을 발생시키고 그에 맞는 파라미터(`chunksize`, `encoding`)를 묻는 방식.

### 2. 악랄하고 매력적인 오답 (Distractors) 생성
객관식 퀴즈의 생명은 '변별력'입니다. 무의미한 코드를 넣지 않고, **실무자들이 가장 흔히 헷갈리는 문법적 실수**를 분석하여 오답 보기를 생성합니다.
- `kind` 파라미터 대신 `type`으로 속이기 (`df.plot(type='bar')`)
- 최상위 함수와 객체 메서드의 혼동 유도 (`pd.barplot()` vs `df.plot.bar()`)
- 파라미터 축(Axis) 또는 순서를 교묘하게 바꾼 함정 보기 생성

### 3. 사용자 중심 UI/UX (Glassmorphism & Mobile-first)
학습자의 피로도를 낮추기 위해 **최신 프론트엔드 트렌드인 글래스모피즘(Glassmorphism)**과 **모바일 반응형 설계**를 적용했습니다.
- **모바일 환경 최적화:** 작은 화면에서 코드를 일일이 타이핑하는 고통을 없애기 위해 객관식(Radio Tile) 인터페이스 채택.
- **글래스모피즘 타일:** 구형 체크박스가 아닌, 반투명 유리 질감의 큼지막한 타일 형태 UI 채택 (터치 편의성 및 심미성 극대화).
- **긴장감 유발 룰렛:** 전체 20문제 중 시스템이 무작위로 **단 2문제를 주관식(타이핑 모드)으로 강제 전환**시켜 적절한 학습 긴장감을 유도.

---

## 🛠 아키텍처 및 폴더 구조
프로젝트가 커짐에 따라, 단일 파일의 비대화(Bloating)를 막기 위해 철저히 모듈화되어 있습니다.

```text
data-analysis-tutor/
│
├── web_pandas_tutor.py   # 앱의 메인 엔트리 (UI 라우팅, 모의고사 타이머 및 점수 렌더링)
├── DESIGN_PHILOSOPHY.md  # 설계 철학 상세 명세서
├── README.md             # 프로젝트 개요 문서
│
└── src/                  # 핵심 비즈니스 로직 모듈
    ├── questions.py      # (핵심) 문제 은행 팩토리 및 난수 출제 사이클 엔진
    ├── style.py          # 글래스모피즘(Glassmorphism) CSS 스타일링 주입 로직
    ├── db.py             # Supabase 연동 및 로컬 JSON 리더보드 저장소 관리
    └── timer.py          # JavaScript 기반의 라이브 모의고사 플로팅 타이머
```

---

## 🚀 실행 방법
이 프로젝트는 Streamlit을 기반으로 구동됩니다.

```bash
# 필요 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run web_pandas_tutor.py
```
