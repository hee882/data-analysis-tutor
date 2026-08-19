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
    st.title("🧪 Machine Learning Lab")
    st.markdown("인터랙티브하게 머신러닝 모델의 동작 방식을 실험해보세요!")

    tab1, tab2, tab3 = st.tabs(["분류 (Classification)", "회귀 (Regression)", "데이터 탐색 (EDA)"])

    with tab1:
        st.header("꽃의 종류 분류하기 (Iris Dataset)")
        st.markdown("K-Nearest Neighbors (KNN) 알고리즘을 사용하여 붓꽃의 종류를 분류합니다.")
        
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
            
            run_btn = st.button("모델 훈련 및 평가 (분류)", type="primary")

        with col2:
            if run_btn:
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
        st.header("팁 금액 예측하기 (Tips Dataset)")
        st.markdown("단순 선형 회귀 (Linear Regression)를 사용하여 팁 금액을 예측합니다.")
        
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
            
            reg_run_btn = st.button("모델 훈련 및 평가 (회귀)", type="primary")

        with col2:
            if reg_run_btn:
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
        st.header("상호작용 데이터 탐색 (Pairplot)")
        st.markdown("선택한 데이터셋의 변수 간 관계를 시각적으로 확인해보세요.")
        
        dataset_name = st.radio("데이터셋 선택", ["iris", "tips"])
        
        if dataset_name == "iris":
            df_eda = sns.load_dataset('iris')
            hue_opts = [None] + df_eda.columns.tolist()
            hue_col = st.selectbox("색상(Hue) 기준 변수", hue_opts, index=hue_opts.index('species'))
        else:
            df_eda = sns.load_dataset('tips')
            hue_opts = [None] + df_eda.columns.tolist()
            hue_col = st.selectbox("색상(Hue) 기준 변수", hue_opts, index=hue_opts.index('time') if 'time' in hue_opts else 0)
            
        if st.button("Pairplot 생성"):
            with st.spinner("그래프 생성 중..."):
                fig_pair = sns.pairplot(df_eda, hue=hue_col)
                st.pyplot(fig_pair.fig)
