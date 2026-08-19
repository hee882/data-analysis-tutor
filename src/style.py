def get_custom_css():
    return '''
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div, input, button {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.02em !important;
}

/* ==========================================
   글래스모피즘(Glassmorphism) 전역 배경 설정
   ========================================== */
.stApp { 
    background-color: #f1f5f9 !important;
    background-image: 
        radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(340, 100%, 76%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(343, 100%, 76%, 0.15) 0px, transparent 50%) !important;
    background-attachment: fixed !important;
}

p, li, span, label { color: #475569 !important; line-height: 1.6 !important; }
h1, h2, h3, h4, h5, strong { color: #0f172a !important; letter-spacing: -0.03em !important; }

header, footer, #MainMenu { visibility: hidden !important; }
h1 { display: none; }
html, body { overflow-y: scroll !important; }

.block-container { 
    padding-top: 2rem !important; 
    padding-bottom: 4rem !important; 
    max-width: 1000px !important; 
    width: 85% !important;
    margin: 0 auto !important;
    min-height: 85vh !important;
}

.custom-header {
    background-color: transparent; padding: 1rem 0 2rem 0; margin-bottom: 2rem;
    display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid rgba(255,255,255,0.4);
}
.custom-header h2 { margin: 0 !important; font-size: 1.6rem !important; font-weight: 800 !important; }
.custom-header span { font-size: 0.85rem; font-weight: 600; color: #3b82f6; background-color: rgba(255,255,255,0.6); padding: 0.3rem 0.8rem; border-radius: 99px; backdrop-filter: blur(4px); }

[data-baseweb="tab-list"] {
    gap: 2rem; margin-bottom: 2rem; border-bottom: 2px solid rgba(255,255,255,0.4); display: flex; flex-wrap: wrap;
}
[data-baseweb="tab"] { font-size: 1.05rem !important; font-weight: 600 !important; color: #64748b !important; padding-bottom: 0.8rem !important; padding-top: 0 !important; transition: color 0.2s ease; background: transparent !important; }
[aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #0f172a !important; }
[data-baseweb="tab-panel"] { min-height: 60vh !important; }

/* ==========================================
   유리 패널 (Glass Panel) 디자인
   ========================================== */
[data-testid="stVerticalBlockBorderWrapper"], .exam-card {
    background: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.7) !important;
    border-radius: 24px !important;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05) !important;
    padding: 2.5rem !important; margin-bottom: 2.5rem; transition: transform 0.2s ease, box-shadow 0.2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover { box-shadow: 0 10px 40px 0 rgba(31, 38, 135, 0.08) !important; }

/* 입력창 글래스모피즘 */
div[data-baseweb="input"] { border-radius: 12px !important; border: 1px solid rgba(255,255,255,0.5) !important; background: rgba(255, 255, 255, 0.3) !important; backdrop-filter: blur(10px) !important; transition: all 0.2s ease !important; }
div[data-baseweb="input"]:focus-within { border-color: rgba(255,255,255,0.8) !important; box-shadow: 0 0 0 3px rgba(255,255,255,0.3) !important; background: rgba(255, 255, 255, 0.6) !important; }
input { color: #0f172a !important; font-weight: 500 !important; font-size: 1.05rem !important; }

/* 버튼 글래스모피즘 톤다운 */
.stButton > button { background-color: rgba(15, 23, 42, 0.85) !important; backdrop-filter: blur(4px); color: #ffffff !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 12px !important; padding: 0.6rem 1.5rem !important; font-size: 1.05rem !important; font-weight: 600 !important; width: 100%; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important; }
.stButton > button:hover { background-color: rgba(15, 23, 42, 1) !important; transform: translateY(-2px); box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.3) !important; }
.stButton > button:active { transform: translateY(0); box-shadow: none !important; }

[data-testid="stButton"] button:not(:disabled) { background-color: rgba(255,255,255,0.4) !important; color: #334155 !important; border: 1px solid rgba(255,255,255,0.6) !important; box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important; }
[data-testid="stButton"] button:not(:disabled):hover { background-color: rgba(255,255,255,0.7) !important; border-color: rgba(255,255,255,0.9) !important; }
[data-testid="stButton"] button[kind="primary"] { background-color: rgba(59, 130, 246, 0.85) !important; color: white !important; border: 1px solid rgba(255,255,255,0.2) !important; }
[data-testid="stButton"] button[kind="primary"]:hover { background-color: rgba(37, 99, 235, 1) !important; box-shadow: 0 8px 24px -4px rgba(59, 130, 246, 0.4) !important; }

.stProgress > div > div > div > div { background-color: #3b82f6 !important; border-radius: 99px !important; }
[data-testid="stAlert"] { border-radius: 16px; border: 1px solid rgba(255,255,255,0.6) !important; background: rgba(255,255,255,0.5) !important; backdrop-filter: blur(10px); box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important; }
code { font-family: 'JetBrains Mono', 'D2Coding', monospace !important; font-size: 0.95rem !important; color: #0284c7 !important; background-color: rgba(255,255,255,0.6) !important; padding: 0.2rem 0.4rem !important; border-radius: 6px !important; border: 1px solid rgba(255,255,255,0.8); }

.report-correct { border-left: 4px solid #10b981 !important; background: rgba(240, 253, 244, 0.6) !important; backdrop-filter: blur(8px); padding: 1.2rem; border-radius: 0 12px 12px 0; margin-bottom: 1rem; }
.report-wrong { border-left: 4px solid #ef4444 !important; background: rgba(254, 242, 242, 0.6) !important; backdrop-filter: blur(8px); padding: 1.2rem; border-radius: 0 12px 12px 0; margin-bottom: 1rem; }

.landing-box { text-align: center; padding: 3rem 1rem; }
.landing-box h3 { font-size: 2rem !important; color: #0f172a !important; }
.landing-box .stats { display: flex; justify-content: center; gap: 3rem; margin: 2rem 0; }
.landing-box .stat-item { background: rgba(255,255,255,0.4); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.6); padding: 1.5rem; border-radius: 20px; min-width: 150px; box-shadow: 0 4px 16px rgba(0,0,0,0.03); }
.landing-box .stat-item strong { display: block; font-size: 2rem; color: #2563eb; margin-bottom: 0.5rem; }

/* ==========================================
   객관식(Radio) 타일형 글래스모피즘
   ========================================== */
div[role="radiogroup"] { gap: 1.2rem !important; margin-top: 1rem; margin-bottom: 1.5rem; }
div[role="radiogroup"] > label {
    background: rgba(255, 255, 255, 0.3) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 16px !important;
    padding: 1.2rem 1.5rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.02) !important;
}
div[role="radiogroup"] > label:hover {
    border-color: rgba(255,255,255,0.9) !important;
    background: rgba(255, 255, 255, 0.6) !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(31, 38, 135, 0.08) !important;
}
div[role="radiogroup"] > label[data-checked="true"] {
    border-color: #3b82f6 !important;
    background: rgba(255, 255, 255, 0.85) !important;
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15) !important;
}
div[role="radiogroup"] > label > div:first-child { display: none !important; }
div[role="radiogroup"] > label > div:nth-child(2) {
    font-family: 'JetBrains Mono', 'D2Coding', monospace !important;
    font-size: 1.1rem !important;
    color: #1e293b !important;
    font-weight: 600 !important;
    margin-left: 0 !important;
}

@media screen and (max-width: 768px) {
    .block-container { width: 100% !important; padding: 1rem !important; }
    .custom-header { flex-direction: column; align-items: flex-start; gap: 0.8rem; padding-bottom: 1rem; }
    [data-testid="stVerticalBlockBorderWrapper"], .exam-card { padding: 1.5rem 1rem !important; }
    .landing-box h3 { font-size: 1.5rem !important; }
    .landing-box .stats { flex-direction: column; gap: 0.8rem !important; margin: 1rem 0 !important; }
    .landing-box .stat-item { padding: 1rem; min-width: auto; }
    h3 { font-size: 1.1rem !important; }
    p, .stRadio label span, code { font-size: 0.95rem !important; }
    .stButton > button { font-size: 0.95rem !important; padding: 0.5rem 1rem !important; }
    [data-baseweb="tab-list"] { gap: 0.5rem !important; display: flex !important; flex-wrap: wrap !important; }
    [data-baseweb="tab"] { font-size: 0.9rem !important; padding: 0 0.5rem !important; }
    div[role="radiogroup"] > label { padding: 1rem !important; }
    div[role="radiogroup"] > label > div:nth-child(2) { font-size: 1rem !important; }
}
</style>
    '''
