def get_custom_css():
    return """
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div, input, button {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.02em !important;
}

/* 글래스모피즘 전역 배경 */
.stApp { 
    background-color: #f1f5f9 !important;
    background-image: 
        radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(340, 100%, 76%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(343, 100%, 76%, 0.15) 0px, transparent 50%) !important;
    background-attachment: fixed !important;
}

/* 폰트 및 라인하이트 최소화 */
p, li, span, label { color: #475569 !important; line-height: 1.4 !important; }
h1, h2, h3, h4, h5, strong { color: #0f172a !important; letter-spacing: -0.03em !important; margin-bottom: 0.2rem !important; }

/* 툴바 제거 및 여백 최소화 */
header, footer, #MainMenu { visibility: hidden !important; height: 0 !important; }
h1 { display: none; }
html, body { overflow: hidden !important; } /* 스크롤바 원천 차단 시도 */
.stApp > header { display: none !important; }

/* 메인 컨테이너 초박형 여백 (한 화면에 다 들어가게) */
.block-container { 
    padding-top: 1rem !important; 
    padding-bottom: 1rem !important; 
    max-width: 900px !important; 
    width: 95% !important;
    margin: 0 auto !important;
    height: 100vh !important;
    overflow-y: auto !important; /* 내용이 넘칠 때만 내부 스크롤 */
}
div[data-testid="stVerticalBlock"] { gap: 0.5rem !important; }

/* 초박형 커스텀 헤더 */
.custom-header {
    background-color: transparent; padding: 0.5rem 0 0.5rem 0; margin-bottom: 0.5rem;
    display: flex; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.4);
}
.custom-header h2 { margin: 0 !important; font-size: 1.3rem !important; font-weight: 800 !important; }
.custom-header span { font-size: 0.75rem; font-weight: 600; color: #3b82f6; background-color: rgba(255,255,255,0.6); padding: 0.2rem 0.6rem; border-radius: 99px; backdrop-filter: blur(4px); }

/* 탭 높이 및 여백 축소 */
[data-baseweb="tab-list"] { gap: 1.5rem; margin-bottom: 1rem; border-bottom: 2px solid rgba(255,255,255,0.4); display: flex; flex-wrap: wrap; }
[data-baseweb="tab"] { font-size: 1rem !important; font-weight: 600 !important; color: #64748b !important; padding-bottom: 0.5rem !important; padding-top: 0 !important; transition: color 0.2s ease; background: transparent !important; }
[aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #0f172a !important; }

/* 유리 패널 여백 최소화 */
[data-testid="stVerticalBlockBorderWrapper"], .exam-card {
    background: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.7) !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 16px 0 rgba(31, 38, 135, 0.05) !important;
    padding: 1.2rem !important; margin-bottom: 1rem;
}

/* 라디오 타일형 객관식 여백 최소화 */
div[role="radiogroup"] { gap: 0.5rem !important; margin-top: 0.5rem; margin-bottom: 0.5rem; }
div[role="radiogroup"] > label {
    background: rgba(255, 255, 255, 0.3) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 12px !important;
    padding: 0.8rem 1.2rem !important;
    width: 100% !important;
    cursor: pointer !important;
    margin-bottom: 0 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important;
}
div[role="radiogroup"] > label:hover { background: rgba(255, 255, 255, 0.6) !important; border-color: rgba(255,255,255,0.9) !important; transform: translateY(-1px); }
div[role="radiogroup"] > label[data-checked="true"] { border-color: #3b82f6 !important; background: rgba(255, 255, 255, 0.85) !important; }
div[role="radiogroup"] > label > div:first-child { display: none !important; }
div[role="radiogroup"] > label > div:nth-child(2) {
    font-family: 'JetBrains Mono', 'D2Coding', monospace !important;
    font-size: 1rem !important;
    color: #1e293b !important;
    font-weight: 600 !important;
    margin-left: 0 !important;
}

/* 버튼 사이즈 및 여백 축소 */
.stButton > button { background-color: rgba(15, 23, 42, 0.85) !important; color: #ffffff !important; border-radius: 10px !important; padding: 0.4rem 1rem !important; font-size: 1rem !important; width: 100%; margin-top: 0.5rem !important; }
[data-testid="stButton"] button[kind="primary"] { background-color: rgba(59, 130, 246, 0.85) !important; }

/* 상태 대시보드 HUD */
.hud-box {
    background: rgba(255,255,255,0.4); padding: 0.8rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.5); text-align: center; margin-bottom: 0.5rem;
}
.hud-title { font-size: 1rem; color: #3b82f6; font-weight: 700; margin-bottom: 0.2rem; }
.hud-value { font-size: 1.5rem; font-weight: 800; color: #0f172a; }

/* 모바일 전용 */
@media screen and (max-width: 768px) {
    .block-container { padding: 0.5rem !important; }
    .custom-header { flex-direction: row; }
    [data-testid="stVerticalBlockBorderWrapper"], .exam-card { padding: 1rem !important; }
    div[role="radiogroup"] > label { padding: 0.8rem !important; }
}
</style>
"""
