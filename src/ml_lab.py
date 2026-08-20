import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, mean_absolute_error, mean_squared_error, r2_score

def render_ml_lab():
    st.markdown("<p style='color: #64748b; font-size: 0.95rem; margin-bottom: 0.5rem;'>🧪 <strong>머신러닝 실험실:</strong> 데이터를 조작하며 분류, 회귀, EDA의 원리를 시각적으로 학습합니다.</p>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["분류 (Classification)", "회귀 (Regression)", "데이터 탐색 (EDA)"])

    with tab1:
        st.subheader("🌷 꽃의 종류 분류하기 (Iris Dataset)")
        st.markdown("K-Nearest Neighbors (KNN) 알고리즘을 사용하여 붓꽃의 종류를 분류합니다.")

        st.info('''
**🧠 K-Nearest Neighbors (KNN) 알고리즘이란?**  
가장 직관적인 분류 알고리즘 중 하나입니다. 새로운 데이터가 주어졌을 때, 기존 데이터 중 가장 가까운 **K개의 이웃**을 찾아 그 이웃들이 가장 많이 속한 클래스(종류)로 예측합니다.
* **K 값 (n_neighbors)**: 몇 명의 이웃을 참고할지 결정합니다. 너무 작으면 과대적합(Outlier에 민감), 너무 크면 과소적합(경계가 흐려짐)이 발생할 수 있습니다.
* **특징 스케일링(StandardScaler)**: KNN은 거리를 기반으로 작동하므로, 각 특성(꽃받침 길이, 꽃잎 너비 등)의 단위가 다르면 왜곡이 발생합니다. 스케일러로 단위를 맞춰주는 것이 중요합니다.
''')

        
        iris = sns.load_dataset('iris')
        with st.expander("데이터셋 보기"):
            st.dataframe(iris.head(10))

        features = iris.columns[:-1].tolist()
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("모델 설정")
            selected_features = st.multiselect("학습에 사용할 특징(Feature) 선택", features, default=features)
            k_value = st.slider("K 값 (n_neighbors)", 1, 30, 5)
            test_size = st.slider("테스트 데이터 비율 (test_size)", 0.1, 0.5, 0.2, 0.05)
            use_scaler = st.toggle("StandardScaler 적용 (특징 스케일링)", value=True)
            
            

        with col2:
            if True: # Instant update
                if not selected_features:
                    st.warning("최소 1개의 특징(Feature)을 선택해주세요.")
                else:
                    X = iris[selected_features]
                    y = iris['species']

                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
                    
                    if use_scaler:
                        scaler = StandardScaler()
                        X_train = scaler.fit_transform(X_train)
                        X_test = scaler.transform(X_test)
                    
                    # Model training
                    knn = KNeighborsClassifier(n_neighbors=k_value)
                    knn.fit(X_train, y_train)
                    y_pred = knn.predict(X_test)
                    
                    # Metrics
                    acc = accuracy_score(y_test, y_pred)
                    
                    st.subheader("평가 결과")
                    st.metric(label="정확도 (Accuracy)", value=f"{acc:.4f}")
                    
                    # Confusion Matrix
                    cm = confusion_matrix(y_test, y_pred)
                    fig_cm, ax_cm = plt.subplots(figsize=(5, 4))
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=knn.classes_, yticklabels=knn.classes_, ax=ax_cm)
                    ax_cm.set_xlabel('Predicted')
                    ax_cm.set_ylabel('True')
                    st.pyplot(fig_cm)
                    
                    st.markdown("**분류 보고서 (Classification Report)**")
                    report = classification_report(y_test, y_pred, output_dict=True)
                    st.dataframe(pd.DataFrame(report).transpose())
                    
                    # K Value comparison
                    st.markdown("**K값에 따른 정확도 변화 (교차 검증)**")
                    k_range = range(1, 31)
                    cv_scores = []
                    
                    X_scaled = X
                    if use_scaler:
                         X_scaled = StandardScaler().fit_transform(X)
                         
                    for k in k_range:
                        knn_temp = KNeighborsClassifier(n_neighbors=k)
                        scores = cross_val_score(knn_temp, X_scaled, y, cv=5, scoring='accuracy')
                        cv_scores.append(scores.mean())
                        
                    fig_k, ax_k = plt.subplots(figsize=(8, 4))
                    ax_k.plot(k_range, cv_scores, marker='o', linestyle='dashed', color='red')
                    ax_k.set_xlabel('K Value')
                    ax_k.set_ylabel('Cross-Validated Accuracy')
                    ax_k.set_title('Optimal K Selection')
                    st.pyplot(fig_k)

    with tab2:
        st.subheader("💰 팁 금액 예측하기 (Tips Dataset)")
        st.markdown("단순 선형 회귀 (Linear Regression)를 사용하여 팁 금액을 예측합니다.")

        st.info('''
**📈 단순 선형 회귀 (Linear Regression)란?**  
독립 변수(X)와 종속 변수(y) 사이의 관계를 가장 잘 설명하는 **하나의 직선(y = wx + b)**을 찾는 알고리즘입니다.
* **R² Score (결정계수)**: 모델이 데이터를 얼마나 잘 설명하는지 나타냅니다. 1에 가까울수록 완벽한 예측을 의미하며, 0에 가까우면 평균으로 예측하는 것과 같음을 의미합니다.
* **MAE (평균 절대 오차)**: 실제값과 예측값의 차이를 절댓값으로 변환해 평균을 낸 것입니다. 직관적인 오차 규모를 보여줍니다.
* **RMSE (평균 제곱근 오차)**: 오차를 제곱하여 평균 낸 뒤 루트를 씌웁니다. 큰 오차에 대해 더 높은 패널티를 부여합니다.
''')

        
        tips = sns.load_dataset('tips')
        with st.expander("데이터셋 보기"):
            st.dataframe(tips.head(10))
            
        numeric_cols = tips.select_dtypes(include=[np.number]).columns.tolist()
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("모델 설정")
            x_col = st.selectbox("독립 변수 (X)", numeric_cols, index=0)
            y_col = st.selectbox("종속 변수 (y, 예측 대상)", numeric_cols, index=1 if len(numeric_cols)>1 else 0)
            reg_test_size = st.slider("테스트 데이터 비율", 0.1, 0.5, 0.2, 0.05, key='reg_test_size')
            
            

        with col2:
            if True: # Instant update
                if x_col == y_col:
                    st.warning("독립 변수와 종속 변수를 다르게 설정해주세요.")
                else:
                    X = tips[[x_col]]
                    y = tips[y_col]
                    
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=reg_test_size, random_state=42)
                    
                    lr = LinearRegression()
                    lr.fit(X_train, y_train)
                    y_pred = lr.predict(X_test)
                    
                    # Metrics
                    r2 = r2_score(y_test, y_pred)
                    mae = mean_absolute_error(y_test, y_pred)
                    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                    
                    st.subheader("평가 결과")
                    m1, m2, m3 = st.columns(3)
                    m1.metric("R² Score", f"{r2:.4f}")
                    m2.metric("MAE", f"{mae:.4f}")
                    m3.metric("RMSE", f"{rmse:.4f}")
                    
                    # Plot
                    fig_reg, ax_reg = plt.subplots(figsize=(8, 5))
                    ax_reg.scatter(X_test, y_test, color='blue', label='Actual data')
                    ax_reg.plot(X_test, y_pred, color='red', linewidth=2, label='Regression line')
                    ax_reg.set_xlabel(x_col)
                    ax_reg.set_ylabel(y_col)
                    ax_reg.legend()
                    st.pyplot(fig_reg)
                    
    with tab3:
        st.subheader("📊 상호작용 데이터 탐색 (동적 시각화)")
        st.markdown("데이터의 형태(범주형/수치형)에 따라 적합한 시각화 라이브러리(Seaborn) 함수를 선택하고 코드를 확인해보세요.")
        
        col_ds, col_plot = st.columns(2)
        with col_ds:
            dataset_name = st.selectbox("데이터셋 선택", ["iris", "tips", "titanic"])
        
        df_eda = sns.load_dataset(dataset_name)
        
        cat_cols = df_eda.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
        num_cols = df_eda.select_dtypes(include=['float64', 'int64']).columns.tolist()
        all_cols = df_eda.columns.tolist()
        
        with col_plot:
            plot_type = st.selectbox("시각화 함수 선택", ["sns.pairplot", "sns.scatterplot", "sns.boxplot", "sns.barplot", "sns.countplot", "sns.histplot"])

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
            st.info("💡 pairplot은 데이터셋 내의 모든 수치형 변수 쌍의 관계를 한눈에 보여줍니다.")
            code_str = f"sns.pairplot(df, hue={repr(hue_col)})"
        elif plot_type == "sns.scatterplot":
            st.info("💡 scatterplot(산점도)은 두 수치형(Numerical) 변수 간의 관계(상관성)를 확인하는 데 적합합니다.")
            code_str = f"sns.scatterplot(data=df, x='{x_col}', y='{y_col}', hue={repr(hue_col)})"
        elif plot_type in ["sns.boxplot", "sns.barplot"]:
            func_name = plot_type.split('.')[1]
            st.info(f"💡 {func_name}은 범주형(Categorical) 그룹별 수치형(Numerical) 변수의 분포나 평균을 비교할 때 유용합니다.")
            code_str = f"{plot_type}(data=df, x='{x_col}', y='{y_col}', hue={repr(hue_col)})"
        elif plot_type == "sns.countplot":
            st.info("💡 countplot은 단일 범주형(Categorical) 변수의 데이터 개수(빈도)를 세어 막대 그래프로 나타냅니다.")
            code_str = f"sns.countplot(data=df, x='{x_col}', hue={repr(hue_col)})"
        elif plot_type == "sns.histplot":
            st.info("💡 histplot은 단일 수치형(Numerical) 변수의 분포를 히스토그램으로 나타냅니다.")
            code_str = f"sns.histplot(data=df, x='{x_col}', hue={repr(hue_col)}, kde=True)"

        st.markdown("**💻 실행된 Python 코드 (Seaborn):**")
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
