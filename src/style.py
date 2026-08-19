def get_custom_css():
    return """
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div, input, button {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.02em !important;
}

/* 1. 글로벌 글래스모피즘 배경 (은은하게 조정) */
.stApp { 
    background-color: #f8fafc !important; 
    background-image: 
        radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.12) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(340, 100%, 76%, 0.12) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242, 100%, 70%, 0.12) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(343, 100%, 76%, 0.12) 0px, transparent 50%) !important;
    background-attachment: fixed !important;
}

p, li, span, label { color: #334155 !important; line-height: 1.5 !important; }
h1, h2, h3, h4, h5, strong { color: #0f172a !important; letter-spacing: -0.03em !important; margin-bottom: 0.3rem !important; }

/* 툴바 제거 및 여백 최소화 */
header, footer, #MainMenu { visibility: hidden !important; height: 0 !important; }
h1 { display: none; }
html, body { overflow: hidden !important; }
.stApp > header { display: none !important; }

/* 컨테이너 및 레이아웃 정렬 */
.block-container { 
    padding-top: 1.5rem !important; 
    padding-bottom: 1.5rem !important; 
    max-width: 860px !important; 
    width: 95% !important;
    margin: 0 auto !important;
    height: 100vh !important;
    overflow-y: auto !important;
}
div[data-testid="stVerticalBlock"] { gap: 1rem !important; }

/* 2. 초박형 커스텀 헤더 */
.custom-header {
    background-color: transparent; padding: 0.5rem 0 1rem 0; margin-bottom: 0.5rem;
    display: flex; align-items: center; border-bottom: 1px solid rgba(0,0,0,0.05);
}

/* 탭 간격 및 디자인 */
[data-baseweb="tab-list"] { gap: 2rem; margin-bottom: 1.5rem; border-bottom: 2px solid rgba(0,0,0,0.05); display: flex; flex-wrap: wrap; }
[data-baseweb="tab"] { font-size: 1.05rem !important; font-weight: 600 !important; color: #94a3b8 !important; padding-bottom: 0.8rem !important; padding-top: 0 !important; transition: all 0.3s ease; background: transparent !important; }
[aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #3b82f6 !important; }

/* 3. 메인 문제 카드 (유리 질감 + 그림자 + 패딩 최적화) */
[data-testid="stVerticalBlockBorderWrapper"], .exam-card {
    background: rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08), inset 0 0 0 1px rgba(255,255,255,0.5) !important;
    padding: 2rem 2.5rem !important; 
    margin-bottom: 1.5rem !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
/* 카드 내부의 요소들 간격 */
[data-testid="stVerticalBlockBorderWrapper"] p { margin-bottom: 1rem !important; font-size: 1.1rem !important; }

/* 4. 라디오 타일형 객관식 (호버/선택 액션 강화) */
div[role="radiogroup"] { gap: 0.8rem !important; margin-top: 1rem !important; margin-bottom: 1rem !important; }
div[role="radiogroup"] > label {
    background: rgba(255, 255, 255, 0.5) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.9) !important;
    border-radius: 14px !important;
    padding: 1rem 1.5rem !important;
    width: 100% !important;
    cursor: pointer !important;
    margin-bottom: 0 !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: flex !important;
    align-items: center !important;
}
/* 호버 효과 (떠오름 + 그림자 진해짐) */
div[role="radiogroup"] > label:hover { 
    background: rgba(255, 255, 255, 0.95) !important; 
    border-color: #cbd5e1 !important; 
    transform: scale(1.015) !important; 
    box-shadow: 0 8px 20px rgba(0,0,0,0.08) !important;
}
/* 선택되었을 때 효과 (파란색 테두리 + 강력한 강조 그림자) */
div[role="radiogroup"] > label[data-checked="true"] { 
    border-color: #3b82f6 !important; 
    background: #ffffff !important; 
    box-shadow: 0 0 0 2px #3b82f6, 0 8px 20px rgba(59, 130, 246, 0.15) !important; 
    transform: scale(1.01) !important;
}
div[role="radiogroup"] > label > div:first-child { display: none !important; } /* 기존 동그라미 제거 */
div[role="radiogroup"] > label > div:nth-child(2) {
    font-family: 'JetBrains Mono', 'D2Coding', monospace !important;
    font-size: 1.05rem !important;
    color: #1e293b !important;
    font-weight: 600 !important;
    margin-left: 0 !important;
}

/* 5. 제출 및 액션 버튼 (명확한 호버 스케일업 효과) */
.stButton > button { 
    background-color: rgba(15, 23, 42, 0.85) !important; 
    color: #ffffff !important; 
    border-radius: 12px !important; 
    padding: 0.6rem 1.2rem !important; 
    font-size: 1.05rem !important; 
    font-weight: 600 !important;
    width: 100%; 
    margin-top: 1rem !important; 
    border: none !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) scale(1.01) !important;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.25) !important;
    background-color: #0f172a !important;
}
[data-testid="stButton"] button[kind="primary"] { 
    background-color: rgba(59, 130, 246, 0.9) !important; 
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2) !important;
}
[data-testid="stButton"] button[kind="primary"]:hover {
    background-color: #2563eb !important;
    box-shadow: 0 6px 16px rgba(59, 130, 246, 0.35) !important;
}

/* 6. 주관식 입력창(Text Input) 스타일링 */
div[data-testid="stTextInput"] input {
    background: rgba(255, 255, 255, 0.6) !important;
    border: 2px solid rgba(255,255,255,0.8) !important;
    border-radius: 12px !important;
    padding: 1rem 1.2rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.1rem !important;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.02) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTextInput"] input:focus {
    background: #ffffff !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15), inset 0 2px 6px rgba(0,0,0,0.01) !important;
}

/* 7. 상태 대시보드 HUD 고급화 */
.hud-box {
    background: rgba(255,255,255,0.5); 
    padding: 1rem 1.2rem; 
    border-radius: 16px; 
    border: 1px solid rgba(255,255,255,0.9); 
    text-align: center; 
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04), inset 0 0 0 1px rgba(255,255,255,0.5);
    backdrop-filter: blur(12px);
}
.hud-title { font-size: 0.9rem; color: #475569; font-weight: 700; margin-bottom: 0.3rem; letter-spacing: 0.05em; text-transform: uppercase; }
.hud-value { font-size: 1.8rem; font-weight: 800; color: #0f172a; }

/* 모바일 전용 반응형 튜닝 */
@media screen and (max-width: 768px) {
    .block-container { padding: 0.5rem !important; }
    .custom-header { flex-direction: row; padding: 0.5rem 0; }
    [data-testid="stVerticalBlockBorderWrapper"], .exam-card { padding: 1.5rem 1rem !important; border-radius: 16px !important; }
    div[role="radiogroup"] > label { padding: 0.8rem 1rem !important; }
    .hud-box { padding: 0.8rem; margin-bottom: 1rem; }
    .hud-value { font-size: 1.5rem; }
}

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


/* ?? ??? ?? ?? ?? (??? p ?? ???? ??) */
.stButton > button p, .stButton > button span, .stButton > button div { color: #ffffff !important; }

/* 우측 둥둥 떠있는(Floating) 해설 카드 (PC 기준) */
.floating-exp {
    position: fixed;
    top: 20%;
    right: 3rem;
    width: 360px;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    box-shadow: 0 16px 40px rgba(31, 38, 135, 0.15), inset 0 0 0 1px rgba(255,255,255,0.5);
    padding: 1.5rem;
    z-index: 9999;
    animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideInRight {
    from { opacity: 0; transform: translateX(50px); }
    to { opacity: 1; transform: translateX(0); }
}

/* 모바일/태블릿: 화면이 좁아지면 원래대로 문제 하단에 배치되도록 자동 변환 */
@media screen and (max-width: 1400px) {
    .floating-exp {
        position: static;
        width: 100%;
        margin-top: 1rem;
        margin-bottom: 1rem;
        animation: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
}


/* ??? ?? ??? ?? ????? ? (Bottom Nav) */
@media screen and (max-width: 768px) {
    [data-baseweb="tab-list"] {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(24px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
        border-top: 1px solid rgba(0,0,0,0.08) !important;
        border-bottom: none !important;
        padding: 0.5rem 0.5rem 1rem 0.5rem !important; /* ??? ?? ?? ?? ?? */
        margin: 0 !important;
        z-index: 9999 !important;
        display: flex !important;
        justify-content: space-around !important;
        box-shadow: 0 -8px 24px rgba(0,0,0,0.06) !important;
        gap: 0 !important;
    }
    
    [data-baseweb="tab"] {
        flex: 1 !important;
        text-align: center !important;
        justify-content: center !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 0 !important;
        flex-direction: column !important;
    }
    
    [aria-selected="true"] {
        border-bottom: none !important;
        color: #3b82f6 !important;
        border-top: 3px solid #3b82f6 !important;
        background: rgba(59, 130, 246, 0.05) !important;
        border-radius: 8px 8px 0 0 !important;
    }
    
    [aria-selected="false"] {
        border-top: 3px solid transparent !important;
        border-bottom: none !important;
    }

    /* ?? ??? ???? ???? ??? ?? ???? ?? ?? ?? */
    .block-container {
        padding-bottom: 6rem !important;
    }
}

</style>
"""
