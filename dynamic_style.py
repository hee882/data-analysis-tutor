import os

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
style_path = os.path.join(repo_path, 'src', 'style.py')

content = '''def get_custom_css(mode="bootcamp_day1_4"):
    # 모드에 따른 배경색/분위기 전환
    if mode == "comprehensive":
        # 종합 마스터 모드: 좀 더 다크/퍼플/오렌지 계열의 딥한(Deep) 느낌
        bg_color = "#f3f4f6"
        gradient = """
        radial-gradient(at 80% 0%, hsla(280, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(30, 100%, 60%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(350, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(200, 100%, 60%, 0.15) 0px, transparent 50%) !important;
        """
        active_color = "#8b5cf6" # 보라색 포인트
    else:
        # Day 1~4 모드: 기존의 청량하고 밝은 블루/핑크 느낌
        bg_color = "#f1f5f9"
        gradient = """
        radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(340, 100%, 76%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(343, 100%, 76%, 0.15) 0px, transparent 50%) !important;
        """
        active_color = "#3b82f6" # 파란색 포인트

    return f"""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

html, body, [class*="css"], .stMarkdown, .stText, p, li, h1, h2, h3, h4, h5, h6, label, div, input, button {{
    font-family: 'Pretendard Variable', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;
    letter-spacing: -0.02em !important;
    word-break: keep-all !important;
}}

.stApp {{ 
    background-color: {bg_color} !important; 
    background-image: {gradient};
    background-attachment: fixed !important;
    transition: background 0.5s ease !important;
}}

p, li, span, label {{ color: #334155 !important; line-height: 1.5 !important; }}
h1, h2, h3, h4, h5, strong {{ color: #0f172a !important; letter-spacing: -0.03em !important; margin-bottom: 0.3rem !important; }}

header, footer, #MainMenu {{ visibility: hidden !important; height: 0 !important; }}
h1 {{ display: none; }}
html, body {{ overflow: hidden !important; }}
.stApp > header {{ display: none !important; }}

/* -------------------------------------------------------------
   LAYOUT
------------------------------------------------------------- */
.block-container {{ 
    padding: 1rem 1rem 6rem 1rem !important; 
    max-width: 860px !important; 
    width: 100% !important;
    margin: 0 auto !important;
    height: 100vh !important;
    overflow-y: auto !important;
    box-sizing: border-box !important;
    scroll-behavior: smooth !important;
}}
div[data-testid="stVerticalBlock"] {{ gap: 1rem !important; }}

/* -------------------------------------------------------------
   HEADER & TOP TOGGLE
------------------------------------------------------------- */
.custom-header {{
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 0.5rem 0 0.5rem 0; margin-bottom: 0.5rem; text-align: center;
}}
.header-top-row {{ display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 0.8rem; margin-bottom: 0.6rem; }}
.header-logo {{ width: 54px; height: 54px; border-radius: 12px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); flex-shrink: 0; }}
.header-title {{ margin: 0 !important; font-size: 1.8rem !important; font-weight: 800 !important; color: #0f172a; line-height: 1.2 !important; }}
.header-subtitle {{ font-size: 0.95rem; font-weight: 500; color: #64748b; line-height: 1.4 !important; max-width: 80%; }}

/* 메인 글로벌 토글 (모드 스위처) */
div[data-testid="stRadio"] {{ margin-bottom: 1rem !important; }}
div[data-testid="stRadio"] > div[role="radiogroup"] {{
    flex-direction: row !important; justify-content: center !important; gap: 0 !important;
    background: rgba(255, 255, 255, 0.5) !important; border-radius: 14px !important; padding: 0.3rem !important;
    width: auto !important; margin: 0 auto !important; display: inline-flex !important;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.05) !important;
}}
div[data-testid="stRadio"] > div[role="radiogroup"] > label[data-baseweb="radio"] {{
    background: transparent !important; border: none !important; box-shadow: none !important;
    padding: 0.6rem 1.5rem !important; min-height: auto !important; border-radius: 10px !important; margin: 0 !important;
    transition: all 0.3s ease !important;
}}
div[data-testid="stRadio"] > div[role="radiogroup"] > label[data-baseweb="radio"][data-checked="true"] {{
    background: #ffffff !important; box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important; color: {active_color} !important;
}}

/* -------------------------------------------------------------
   TAB BAR (High-end Floating Pill Design)
------------------------------------------------------------- */
[data-baseweb="tab-list"] {{
    position: fixed !important; bottom: 1.5rem !important; left: 50% !important; transform: translateX(-50%) !important;
    width: 90% !important; max-width: 600px !important;
    background: rgba(255, 255, 255, 0.75) !important; backdrop-filter: blur(24px) saturate(200%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
    border: 1px solid rgba(255, 255, 255, 0.9) !important; border-radius: 99px !important;
    padding: 0.5rem !important; margin: 0 !important; z-index: 9999 !important;
    display: flex !important; justify-content: space-between !important; gap: 0.3rem !important;
    box-shadow: 0 12px 32px rgba(31, 38, 135, 0.15), inset 0 2px 4px rgba(255,255,255,1) !important;
}}
[data-baseweb="tab"] {{ 
    flex: 1 !important; border-radius: 99px !important; font-size: 0.95rem !important; font-weight: 700 !important; 
    padding: 0.8rem 0 !important; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important; color: #64748b !important; background: transparent !important; border: none !important; outline: none !important;
}}
[aria-selected="true"] {{ background: {active_color} !important; color: #ffffff !important; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important; border: none !important; }}
[aria-selected="false"]:hover {{ background: rgba(255, 255, 255, 0.6) !important; color: #0f172a !important; }}

/* -------------------------------------------------------------
   TAB TRANSITION ANIMATION
------------------------------------------------------------- */
[data-baseweb="tab-panel"] {{ animation: tabSlideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; opacity: 0; }}
@keyframes tabSlideUp {{ 0% {{ opacity: 0; transform: translateY(30px) scale(0.98); }} 100% {{ opacity: 1; transform: translateY(0) scale(1); }} }}

/* -------------------------------------------------------------
   MAIN CONTENT CARDS
------------------------------------------------------------- */
[data-testid="stVerticalBlockBorderWrapper"], .stForm {{
    background: rgba(255, 255, 255, 0.8) !important; backdrop-filter: blur(48px) saturate(160%) !important; -webkit-backdrop-filter: blur(48px) saturate(160%) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important; border-radius: 24px !important;
    box-shadow: 0 32px 64px rgba(0, 0, 0, 0.08), inset 0 2px 6px rgba(255, 255, 255, 0.6) !important;
    padding: 1.5rem 2rem !important; margin-bottom: 0.5rem !important; text-align: left !important; overflow: visible !important;
}}

/* RADIO BUTTONS */
.stRadio label[data-baseweb="radio"] {{
    background: rgba(255, 255, 255, 0.6) !important; backdrop-filter: blur(12px) !important; border: 1px solid rgba(255, 255, 255, 0.9) !important;
    border-radius: 16px !important; padding: 0.8rem 1.2rem !important; width: 100% !important; min-height: 3rem !important;
    box-sizing: border-box !important; cursor: pointer !important; margin-bottom: 0 !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important; transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: flex-start !important; text-align: left !important;
}}
.stRadio label[data-baseweb="radio"]:hover {{ background: rgba(255, 255, 255, 0.95) !important; border-color: #cbd5e1 !important; transform: scale(1.015) !important; box-shadow: 0 12px 24px rgba(0,0,0,0.08) !important; }}
.stRadio label[data-baseweb="radio"][data-checked="true"] {{ border-color: {active_color} !important; background: #ffffff !important; box-shadow: 0 0 0 2px {active_color}, 0 12px 24px rgba(0,0,0,0.15) !important; transform: scale(1.01) !important; }}
.stRadio label[data-baseweb="radio"] > div:first-child {{ display: none !important; }} 
.stRadio label[data-baseweb="radio"] > div:nth-child(2) {{ font-family: 'JetBrains Mono', 'D2Coding', monospace !important; font-size: 1.05rem !important; color: #1e293b !important; font-weight: 600 !important; margin-left: 0 !important; text-align: left !important; width: 100% !important; }}

/* -------------------------------------------------------------
   BUTTONS & INPUTS
------------------------------------------------------------- */
.stButton > button {{ background-color: rgba(15, 23, 42, 0.85) !important; border-radius: 16px !important; padding: 0.8rem 1.2rem !important; font-size: 1.1rem !important; font-weight: 700 !important; width: 100%; margin-top: 1rem !important; border: none !important; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.15) !important; transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important; }}
.stButton > button p, .stButton > button span, .stButton > button div {{ color: #ffffff !important; }}
.stButton > button:hover {{ transform: scale(1.01) !important; box-shadow: 0 12px 32px rgba(15, 23, 42, 0.25) !important; background-color: #0f172a !important; }}
[data-testid="stButton"] button[kind="primary"] {{ background-color: {active_color} !important; box-shadow: 0 8px 24px rgba(0,0,0,0.2) !important; }}
[data-testid="stButton"] button[kind="primary"]:hover {{ background-color: #2563eb !important; box-shadow: 0 12px 32px rgba(0,0,0,0.35) !important; }}

div[data-testid="stTextInput"] input {{ background: rgba(255, 255, 255, 0.7) !important; border: 2px solid rgba(255,255,255,0.9) !important; border-radius: 16px !important; padding: 1.2rem 1.5rem !important; font-family: 'JetBrains Mono', monospace !important; font-size: 1.1rem !important; box-shadow: inset 0 2px 6px rgba(0,0,0,0.02) !important; text-align: left !important; transition: all 0.3s ease !important; }}
div[data-testid="stTextInput"] input:focus {{ background: #ffffff !important; border-color: {active_color} !important; box-shadow: 0 0 0 4px rgba(0,0,0,0.15), inset 0 2px 6px rgba(0,0,0,0.01) !important; }}

/* -------------------------------------------------------------
   HUD & FLOATING EXP
------------------------------------------------------------- */
.hud-container {{ display: flex; justify-content: flex-end; align-items: center; gap: 0.8rem; margin-bottom: 1.5rem; flex-wrap: wrap; }}
.hud-badge {{ background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 1); padding: 0.5rem 1.2rem; border-radius: 99px; font-size: 0.9rem; font-weight: 700; color: #1e293b; box-shadow: 0 8px 24px rgba(0,0,0,0.06); display: flex; align-items: center; }}
.hud-badge span {{ color: {active_color}; font-weight: 800; margin-left: 0.4rem; font-size: 1rem; }}

.floating-exp {{ position: fixed; top: 20%; right: 3rem; width: 400px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(32px) saturate(200%); border: 1px solid rgba(255, 255, 255, 1); border-radius: 24px; box-shadow: 0 24px 64px rgba(31, 38, 135, 0.2), inset 0 1px 2px rgba(255,255,255,1); padding: 2rem; z-index: 9999; text-align: left; animation: slideInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1); }}
@keyframes slideInRight {{ from {{ opacity: 0; transform: translateX(100px); }} to {{ opacity: 1; transform: translateX(0); }} }}

/* -------------------------------------------------------------
   MOBILE RESPONSIVE
------------------------------------------------------------- */
@media screen and (max-width: 768px) {{
    .block-container {{ padding: 0.5rem 0.8rem 4rem 0.8rem !important; }}
    .custom-header {{ flex-direction: row !important; align-items: center !important; justify-content: flex-start !important; gap: 0.5rem !important; margin-bottom: 0.5rem !important; padding: 0 !important; text-align: left !important; }}
    .header-top-row {{ margin: 0 !important; gap: 0.5rem !important; justify-content: flex-start !important; }}
    .header-logo {{ width: 28px !important; height: 28px !important; border-radius: 6px !important; }}
    .header-title {{ font-size: 1.1rem !important; }}
    .header-subtitle {{ display: none !important; }}
    [data-testid="stVerticalBlockBorderWrapper"], .stForm {{ padding: 1rem 1rem !important; border-radius: 16px !important; margin-bottom: 0.5rem !important; }}
    .stRadio label[data-baseweb="radio"] {{ padding: 0.6rem 0.8rem !important; min-height: 2.8rem !important; border-radius: 10px !important; margin-bottom: 0.3rem !important; }}
    .stRadio label[data-baseweb="radio"] > div:nth-child(2) {{ font-size: 0.9rem !important; }}
    .hud-container {{ margin-bottom: 0.5rem !important; justify-content: flex-start !important; gap: 0.4rem !important; }}
    .hud-badge {{ padding: 0.2rem 0.5rem !important; font-size: 0.75rem !important; }}
    .hud-badge span {{ font-size: 0.85rem !important; }}
    [data-baseweb="tab-list"] {{ 
        bottom: 0 !important; width: 100% !important; border-radius: 0 !important; border-top: 1px solid rgba(0,0,0,0.1) !important;
        padding: 0.3rem 0.2rem 1rem 0.2rem !important;
    }}
    [data-baseweb="tab"] {{ font-size: 0.85rem !important; padding: 0.4rem 0 !important; color: #94a3b8 !important; }}
    [aria-selected="true"] {{ border-top: none !important; color: {active_color} !important; background: transparent !important; box-shadow: none !important; }}
    [aria-selected="true"]::before {{ content: ''; position: absolute; top: -3px; left: 20%; right: 20%; height: 3px; background: {active_color}; border-radius: 0 0 4px 4px; }}
    .floating-exp {{ padding: 1rem !important; margin-top: 1rem !important; }}
    
    /* 모바일 글로벌 토글 스케일 */
    div[data-testid="stRadio"] > div[role="radiogroup"] > label[data-baseweb="radio"] {{ padding: 0.4rem 0.8rem !important; font-size: 0.85rem !important; }}
}}

@media screen and (max-width: 1400px) and (min-width: 769px) {{
    .floating-exp {{ position: static; width: 100%; margin-top: 1.5rem; margin-bottom: 1rem; animation: none; box-shadow: 0 12px 32px rgba(0,0,0,0.1); }}
}}

/* -------------------------------------------------------------
   LEADERBOARD UI
------------------------------------------------------------- */
.lb-container {{ display: flex; flex-direction: column; gap: 0.8rem; margin-top: 0.5rem; }}
.lb-row {{
    display: flex; align-items: center; justify-content: space-between;
    background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.9);
    padding: 1rem 1.5rem; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); transition: transform 0.2s;
}}
.lb-row:hover {{ transform: scale(1.01); background: rgba(255, 255, 255, 0.9); box-shadow: 0 8px 20px rgba(0,0,0,0.06); }}
.lb-rank {{ font-size: 1.2rem; font-weight: 800; color: #cbd5e1; width: 40px; }}
.lb-rank-1 {{ color: #fbbf24; font-size: 1.5rem; }}
.lb-rank-2 {{ color: #94a3b8; font-size: 1.3rem; }}
.lb-rank-3 {{ color: #b45309; font-size: 1.2rem; }}
.lb-name {{ flex: 1; font-size: 1.1rem; font-weight: 700; color: #1e293b; margin-left: 1rem; }}
.lb-score {{ font-size: 1.2rem; font-weight: 800; color: {active_color}; background: rgba(0, 0, 0, 0.05); padding: 0.3rem 0.8rem; border-radius: 8px; }}
.lb-date {{ font-size: 0.85rem; color: #64748b; margin-left: 1rem; text-align: right; width: 130px; font-family: monospace; }}

@media screen and (max-width: 768px) {{
    .lb-row {{ padding: 0.8rem 1rem; }}
    .lb-date {{ display: none; }}
}}
</style>
"""
'''
with open(style_path, 'w', encoding='utf-8') as f:
    f.write(content)
