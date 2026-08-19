def get_custom_css():
    return '''
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div, input, button {
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.02em !important;
}

.stApp { background-color: #f8fafc; }
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
    display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1px solid #e2e8f0;
}
.custom-header h2 { margin: 0 !important; font-size: 1.6rem !important; font-weight: 800 !important; }
.custom-header span { font-size: 0.85rem; font-weight: 600; color: #3b82f6; background-color: #eff6ff; padding: 0.3rem 0.8rem; border-radius: 99px; }

[data-baseweb="tab-list"] {
    gap: 2rem; margin-bottom: 2rem; border-bottom: 2px solid #f1f5f9; display: flex; flex-wrap: wrap;
}
[data-baseweb="tab"] { font-size: 1.05rem !important; font-weight: 600 !important; color: #94a3b8 !important; padding-bottom: 0.8rem !important; padding-top: 0 !important; transition: color 0.2s ease; }
[aria-selected="true"] { color: #0f172a !important; border-bottom: 3px solid #0f172a !important; }
[data-baseweb="tab-panel"] { min-height: 60vh !important; }

[data-testid="stVerticalBlockBorderWrapper"], .exam-card {
    background-color: #ffffff; border-radius: 16px; box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.04) !important;
    border: 1px solid #e2e8f0 !important; padding: 2.5rem !important; margin-bottom: 2.5rem; transition: transform 0.2s ease, box-shadow 0.2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover { box-shadow: 0 10px 30px -4px rgba(15, 23, 42, 0.08) !important; }

div[data-baseweb="input"] { border-radius: 10px !important; border: 1px solid #cbd5e1 !important; background-color: #f8fafc !important; transition: all 0.2s ease !important; }
div[data-baseweb="input"]:focus-within { border-color: #3b82f6 !important; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important; background-color: #ffffff !important; }
input { color: #0f172a !important; font-weight: 500 !important; font-size: 1.05rem !important; }

.stButton > button { background-color: #0f172a !important; color: #ffffff !important; border: none !important; border-radius: 10px !important; padding: 0.6rem 1.5rem !important; font-size: 1.05rem !important; font-weight: 600 !important; width: 100%; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important; }
.stButton > button:hover { background-color: #1e293b !important; transform: translateY(-2px); box-shadow: 0 8px 16px -4px rgba(15, 23, 42, 0.25) !important; }
.stButton > button:active { transform: translateY(0); box-shadow: none !important; }
[data-testid="stButton"] button:not(:disabled) { background-color: #f1f5f9 !important; color: #334155 !important; border: 1px solid #e2e8f0 !important; box-shadow: none !important; }
[data-testid="stButton"] button:not(:disabled):hover { background-color: #e2e8f0 !important; border-color: #cbd5e1 !important; }
[data-testid="stButton"] button[kind="primary"] { background-color: #3b82f6 !important; color: white !important; border: none !important; }
[data-testid="stButton"] button[kind="primary"]:hover { background-color: #2563eb !important; box-shadow: 0 8px 16px -4px rgba(59, 130, 246, 0.3) !important; }

.stProgress > div > div > div > div { background-color: #3b82f6 !important; border-radius: 99px !important; }
[data-testid="stAlert"] { border-radius: 12px; border: none !important; box-shadow: 0 2px 8px rgba(0,0,0,0.02) !important; }
code { font-family: 'JetBrains Mono', 'D2Coding', monospace !important; font-size: 0.95rem !important; color: #0284c7 !important; background-color: #f0f9ff !important; padding: 0.2rem 0.4rem !important; border-radius: 6px !important; border: 1px solid #e0f2fe; }

.report-correct { border-left: 4px solid #10b981 !important; background-color: #f0fdf4; padding: 1.2rem; border-radius: 0 8px 8px 0; margin-bottom: 1rem; }
.report-wrong { border-left: 4px solid #ef4444 !important; background-color: #fef2f2; padding: 1.2rem; border-radius: 0 8px 8px 0; margin-bottom: 1rem; }

.landing-box { text-align: center; padding: 3rem 1rem; }
.landing-box h3 { font-size: 2rem !important; color: #0f172a !important; }
.landing-box .stats { display: flex; justify-content: center; gap: 3rem; margin: 2rem 0; }
.landing-box .stat-item { background: #f1f5f9; padding: 1.5rem; border-radius: 16px; min-width: 150px; }
.landing-box .stat-item strong { display: block; font-size: 2rem; color: #2563eb; margin-bottom: 0.5rem; }

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
}
</style>
    '''
