import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
import contextlib
import traceback

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, r2_score, mean_absolute_error, mean_squared_error

def render_ml_lab():
    st.markdown("<p style='color: #64748b; font-size: 0.95rem; margin-bottom: 0.5rem;'>💡 <strong>데이터 & ML 랩</strong>: 시각화와 머신러닝 알고리즘을 테스트하거나, <strong>직접 파이썬 코드를 작성하고 실행</strong>해볼 수 있습니다.</p>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 기초 탐색 & 시각화 (EDA)", "🤖 예측 모델링 (ML)", "⌨️ 인터랙티브 코딩 샌드박스"])

    with tab1:
        st.subheader("🔍 상호작용형 데이터 탐색")
        st.markdown("데이터의 형태에 따라 적합한 시각화(Seaborn) 함수를 선택하고 동작 원리를 확인하세요.")
        
        col_ds, col_plot = st.columns(2)
        with col_ds:
            dataset_name = st.selectbox("데이터셋 선택", ["iris", "tips", "titanic", "penguins"], key="eda_ds")
        
        df_eda = sns.load_dataset(dataset_name).dropna()
        
        cat_cols = df_eda.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
        num_cols = df_eda.select_dtypes(include=['float64', 'int64']).columns.tolist()
        all_cols = df_eda.columns.tolist()
        
        with col_plot:
            plot_type = st.selectbox("시각화 함수 선택", ["sns.scatterplot", "sns.histplot", "sns.boxplot", "sns.barplot", "sns.countplot", "sns.pairplot"], key="eda_plot")

        st.markdown("---")
        
        col_opt1, col_opt2 = st.columns(2)
        with col_opt1:
            hue_col = st.selectbox("색상(Hue) 기준 변수 (선택)", [None] + cat_cols, index=0)
            
        x_col, y_col = None, None
        code_str = ""
        
        with col_opt2:
            if plot_type == "sns.scatterplot":
                x_col = st.selectbox("X축 (수치형)", num_cols, index=0)
                y_col = st.selectbox("Y축 (수치형)", num_cols, index=1 if len(num_cols) > 1 else 0)
            elif plot_type in ["sns.boxplot", "sns.barplot"]:
                x_col = st.selectbox("X축 (범주형 권장)", all_cols, index=all_cols.index(cat_cols[0]) if cat_cols else 0)
                y_col = st.selectbox("Y축 (수치형)", num_cols, index=0)
            elif plot_type == "sns.countplot":
                x_col = st.selectbox("X축 (범주형 권장)", all_cols, index=all_cols.index(cat_cols[0]) if cat_cols else 0)
            elif plot_type == "sns.histplot":
                x_col = st.selectbox("X축 (수치형)", num_cols, index=0)

        # Set code and text
        if plot_type == "sns.pairplot":
            st.info("💡 pairplot은 데이터셋 내의 모든 수치형 변수들 간의 관계를 한눈에 보여줍니다.")
            code_str = f"sns.pairplot(df, hue={repr(hue_col)})"
        elif plot_type == "sns.scatterplot":
            st.info("💡 scatterplot(산점도)은 두 수치형(Numerical) 변수 간의 관계(상관성)를 확인하는 데 적합합니다.")
            code_str = f"sns.scatterplot(data=df, x='{x_col}', y='{y_col}', hue={repr(hue_col)})"
        elif plot_type in ["sns.boxplot", "sns.barplot"]:
            func_name = plot_type.split('.')[1]
            st.info(f"💡 {func_name}은 범주형(Categorical) 그룹별 수치형(Numerical) 변수의 분포나 평균을 비교할 때 사용합니다.")
            code_str = f"{plot_type}(data=df, x='{x_col}', y='{y_col}', hue={repr(hue_col)})"
        elif plot_type == "sns.countplot":
            st.info("💡 countplot은 단일 범주형(Categorical) 변수의 차이와 개수(빈도)를 세어 막대 그래프로 나타냅니다.")
            code_str = f"sns.countplot(data=df, x='{x_col}', hue={repr(hue_col)})"
        elif plot_type == "sns.histplot":
            st.info("💡 histplot은 단일 수치형(Numerical) 변수의 분포를 히스토그램으로 나타냅니다.")
            code_str = f"sns.histplot(data=df, x='{x_col}', hue={repr(hue_col)}, kde=True)"

        st.markdown("**👉 실행된 Python 코드 (Seaborn):**")
        st.code(code_str, language='python')
        
        with st.spinner("그래프 생성 중..."):
            try:
                if plot_type == "sns.pairplot":
                    fig_pair = sns.pairplot(df_eda, hue=hue_col)
                    st.pyplot(fig_pair.fig)
                else:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    if plot_type == "sns.scatterplot":
                        sns.scatterplot(data=df_eda, x=x_col, y=y_col, hue=hue_col, ax=ax)
                    elif plot_type == "sns.boxplot":
                        sns.boxplot(data=df_eda, x=x_col, y=y_col, hue=hue_col, ax=ax)
                    elif plot_type == "sns.barplot":
                        sns.barplot(data=df_eda, x=x_col, y=y_col, hue=hue_col, ax=ax)
                    elif plot_type == "sns.countplot":
                        sns.countplot(data=df_eda, x=x_col, hue=hue_col, ax=ax)
                    elif plot_type == "sns.histplot":
                        sns.histplot(data=df_eda, x=x_col, hue=hue_col, kde=True, ax=ax)
                    st.pyplot(fig)
            except Exception as e:
                st.error(f"시각화 중 에러가 발생했습니다: {e}")

    with tab2:
        st.subheader("🤖 알고리즘 실험 (Classification & Regression)")
        task_type = st.radio("머신러닝 태스크 선택", ["분류 (Classification) - 붓꽃 종 예측", "회귀 (Regression) - 팁 금액 예측"], horizontal=True)
        st.markdown("---")
        
        if "분류" in task_type:
            st.info('''
**💡 K-Nearest Neighbors (KNN) 알고리즘이란?**  
가장 직관적인 분류 알고리즘 중 하나입니다. 새로운 데이터가 주어졌을 때, 기존 데이터 중 가장 가까운 **K개의 이웃**을 찾아 그 이웃들이 가장 많이 속한 클래스(종류)로 예측합니다.
* **K 값(n_neighbors)**: 몇 명의 이웃을 참고할지 결정합니다. 너무 작으면 과대적합, 너무 크면 과소적합이 발생할 수 있습니다.
''')
            iris = sns.load_dataset('iris')
            with st.expander("데이터셋 미리보기 (Iris)"):
                st.dataframe(iris.head())
            features = iris.columns[:-1].tolist()
            
            c1, c2 = st.columns([1, 2])
            with c1:
                st.subheader("모델 하이퍼파라미터")
                selected_features = st.multiselect("학습에 사용할 특징(Feature) 선택", features, default=features)
                k_val = st.slider("K 값 (이웃 수)", 1, 15, 3, 1)
                test_size = st.slider("테스트 데이터 비율", 0.1, 0.5, 0.2, 0.05)
                
            with c2:
                if len(selected_features) == 0:
                    st.warning("최소 1개 이상의 특징을 선택해주세요.")
                else:
                    X = iris[selected_features]
                    y = iris['species']
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
                    
                    scaler = StandardScaler()
                    X_train_scaled = scaler.fit_transform(X_train)
                    X_test_scaled = scaler.transform(X_test)
                    
                    knn = KNeighborsClassifier(n_neighbors=k_val)
                    knn.fit(X_train_scaled, y_train)
                    y_pred = knn.predict(X_test_scaled)
                    
                    acc = accuracy_score(y_test, y_pred)
                    st.subheader(f"🎯 예측 정확도: {acc*100:.1f}%")
                    st.markdown("**오차 행렬 (Confusion Matrix)**")
                    cm = confusion_matrix(y_test, y_pred)
                    fig_c, ax_c = plt.subplots(figsize=(6, 4))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=knn.classes_, yticklabels=knn.classes_)
                    st.pyplot(fig_c)
                    
        else:
            st.info('''
**💡 단순 선형 회귀 모델 (Linear Regression)이란?**  
독립 변수(X)와 종속 변수(y) 사이의 관계를 가장 잘 설명하는 **하나의 직선(y = wx + b)**을 찾는 알고리즘입니다.
* **R² Score (결정계수)**: 모델이 데이터를 얼마나 잘 설명하는지 나타냅니다. 1에 가까울수록 완벽한 예측을 의미합니다.
''')
            tips = sns.load_dataset('tips')
            numeric_cols = tips.select_dtypes(include=[np.number]).columns.tolist()
            with st.expander("데이터셋 미리보기 (Tips)"):
                st.dataframe(tips.head())
            
            c1, c2 = st.columns([1, 2])
            with c1:
                st.subheader("모델 변수 설정")
                x_col = st.selectbox("독립 변수 (X)", numeric_cols, index=0)
                y_col = st.selectbox("종속 변수 (y, 예측 대상)", numeric_cols, index=1 if len(numeric_cols)>1 else 0)
                reg_test_size = st.slider("테스트 데이터 비율", 0.1, 0.5, 0.2, 0.05, key='reg_ts')
                
            with c2:
                if x_col == y_col:
                    st.warning("독립 변수와 종속 변수를 다르게 설정해주세요.")
                else:
                    X = tips[[x_col]]
                    y = tips[y_col]
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=reg_test_size, random_state=42)
                    
                    lr = LinearRegression()
                    lr.fit(X_train, y_train)
                    y_pred = lr.predict(X_test)
                    
                    r2 = r2_score(y_test, y_pred)
                    mae = mean_absolute_error(y_test, y_pred)
                    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                    
                    st.subheader("📈 회귀 성능 평가")
                    m1, m2, m3 = st.columns(3)
                    m1.metric("R² Score", f"{r2:.4f}")
                    m2.metric("MAE", f"{mae:.4f}")
                    m3.metric("RMSE", f"{rmse:.4f}")
                    
                    fig_r, ax_r = plt.subplots(figsize=(8, 5))
                    ax_r.scatter(X_test, y_test, color='blue', alpha=0.5, label='Actual data')
                    ax_r.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
                    ax_r.set_xlabel(x_col)
                    ax_r.set_ylabel(y_col)
                    ax_r.legend()
                    st.pyplot(fig_r)

    with tab3:
        st.subheader("⌨️ 인터랙티브 코딩 샌드박스 (Live Code Editor)")
        st.markdown('''
        이곳에서는 **실제 파이썬 코드(Pandas, Scikit-learn 등)를 직접 작성하고 실행**해볼 수 있습니다. 
        `print()` 출력결과나 DataFrame 형태, 심지어 `plt.show()`를 통한 그래프도 바로 아래 렌더링됩니다!
        ''')
        
        default_code = '''# 데이터셋 로드
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

# 예시 1: 데이터 살펴보기
print("데이터 형태:", df.shape)
print(df.head())

# 예시 2: 그룹별 평균 구하기
grouped = df.groupby('class', observed=False)['survived'].mean()
print("\\n클래스별 생존율:\\n", grouped)

# 예시 3: 그래프 출력하기
sns.barplot(data=df, x='class', y='survived')
plt.title('Survival Rate by Class')
plt.show()
'''
        
        user_code = st.text_area("파이썬 코드를 작성하세요", value=default_code, height=350, key="sandbox_code")
        
        if st.button("🚀 코드 실행 (Run)", type="primary"):
            st.markdown("### 🖥️ 실행 결과 (Output)")
            
            # Create a string buffer to capture stdout
            stdout_buffer = io.StringIO()
            
            # Setup execution environment
            local_env = {
                'pd': pd, 'np': np, 'sns': sns, 'plt': plt, 'st': st,
                'train_test_split': train_test_split, 'RandomForestClassifier': RandomForestClassifier,
                'accuracy_score': accuracy_score
            }
            
            # Clear previous plots
            plt.clf()
            
            # Catch outputs
            with st.container(border=True):
                with contextlib.redirect_stdout(stdout_buffer):
                    try:
                        # 실행 시 보안 경고 (로컬 앱이므로 exec 허용)
                        exec(user_code, globals(), local_env)
                        
                        # Print captured output
                        output = stdout_buffer.getvalue()
                        if output:
                            st.code(output, language='text')
                        else:
                            st.success("코드 실행 완료 (출력값 없음)")
                            
                        # If a matplotlib figure was generated but not explicitly st.pyplot()'d
                        if plt.gcf().get_axes():
                            st.pyplot(plt.gcf())
                            
                    except Exception as e:
                        st.error(f"❌ 에러 발생:\\n\\n{traceback.format_exc()}")
