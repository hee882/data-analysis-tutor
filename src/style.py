def get_custom_css(mode="bootcamp_day1_4"):
    if mode == "comprehensive":
        bg_color = "#f3f4f6"
        gradient = """
        radial-gradient(at 80% 0%, hsla(280, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(30, 100%, 60%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(350, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(200, 100%, 60%, 0.15) 0px, transparent 50%) !important;
        """
        active_color = "#8b5cf6"
    else:
        bg_color = "#f1f5f9"
        gradient = """
        radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, hsla(340, 100%, 76%, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 100%, hsla(242, 100%, 70%, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 0%, hsla(343, 100%, 76%, 0.15) 0px, transparent 50%) !important;
        """
        active_color = "#3b82f6"

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
header, footer, #MainMenu {{ display: none !important; }}

/* -------------------------------------------------------------
   HUD CONTAINER (Stats)
------------------------------------------------------------- */
.hud-container {{
    display: flex;
    flex-wrap: nowrap !important;
    white-space: nowrap !important;
    justify-content: flex-end;
    gap: 0.8rem;
    margin-bottom: 1rem;
}}
.hud-badge {{
    background: rgba(255, 255, 255, 0.8) !important;
    white-space: nowrap !important;
    min-width: max-content !important;
    word-break: keep-all !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(0,0,0,0.1) !important;
    padding: 0.4rem 1rem !important;
    border-radius: 99px !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    color: #475569 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
}}
.hud-badge span {{
    color: {active_color} !important;
    font-size: 1.05rem !important;
}}

/* -------------------------------------------------------------
   MODERN SCROLLBAR (Sleek & Clean)
------------------------------------------------------------- */
::-webkit-scrollbar {{
    width: 6px;
    height: 6px;
}}
::-webkit-scrollbar-track {{
    background: transparent;
}}
::-webkit-scrollbar-thumb {{
    background: rgba(100, 116, 139, 0.3);
    border-radius: 10px;
}}
::-webkit-scrollbar-thumb:hover {{
    background: rgba(100, 116, 139, 0.5);
}}

/* Firefox scrollbar support */
* {{
    scrollbar-width: thin;
    scrollbar-color: rgba(100, 116, 139, 0.3) transparent;
}}

/* -------------------------------------------------------------
   LAYOUT
------------------------------------------------------------- */
.block-container {{
    padding: 2rem 3rem !important;
    max-width: 1400px !important;
    margin: 0 auto !important;
    overflow: visible !important;
}}
div[data-testid="stVerticalBlock"] {{ gap: 1rem !important; }}

/* -------------------------------------------------------------
   HEADER
------------------------------------------------------------- */
.custom-header {{
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 0; margin-bottom: 0.5rem; text-align: center;
}}
.header-top-row {{ display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 0.8rem; margin-bottom: 0.3rem; }}
.header-logo {{ width: 48px; height: 48px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); flex-shrink: 0; }}
.header-title {{ margin: 0 !important; font-size: 1.6rem !important; font-weight: 800 !important; color: #0f172a; line-height: 1.2 !important; }}
.header-subtitle {{ font-size: 0.9rem; font-weight: 500; color: #64748b; line-height: 1.4 !important; max-width: 80%; }}

/* 글로벌 스위처 (Toggle) 좌우 텍스트 추가 및 중앙 정렬 */
div[data-testid="stToggle"] {{
    position: absolute !important;
    top: 1.5rem !important;
    right: 2rem !important;
    display: flex !important; 
    justify-content: flex-end !important; 
    align-items: center !important; 
    margin: 0 !important;
    z-index: 100 !important;
}}
div[data-testid="stToggle"]::before {{
    content: "🌱 베이직 버전";
    margin-right: 0.8rem;
    font-weight: 700;
    font-size: 1.05rem;
    color: #64748b;
}}
div[data-testid="stToggle"] label {{ 
    color: {active_color} !important; font-weight: 700 !important; font-size: 1.05rem !important; 
}}

/* -------------------------------------------------------------
   TAB BAR (PC: Standard Header Style, Mobile: iOS Bottom Dock)
------------------------------------------------------------- */
[data-baseweb="tab-list"] {{
    position: relative !important;
    width: 100% !important;
    max-width: 100% !important;
    background: transparent !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    border: none !important;
    border-bottom: 1px solid rgba(0,0,0,0.1) !important;
    border-radius: 0 !important;
    padding: 0 !important;
    margin: 0 0 1rem 0 !important;
    display: flex !important;
    justify-content: space-between !important;
    gap: 0 !important;
    box-shadow: none !important;
    bottom: auto !important;
    left: auto !important;
    transform: none !important;
}}
[data-baseweb="tab"] {{
    flex: 1 !important;
    text-align: center !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    padding: 0.8rem 0 !important;
    background: transparent !important;
    color: #64748b !important;
    border: none !important;
    border-radius: 0 !important;
    /* Removed border */
}}
[aria-selected="true"] {{
    color: {active_color} !important;
    /* Removed border */
    background: transparent !important;
    box-shadow: none !important;
}}
[aria-selected="false"]:hover {{
    color: #1e293b !important;
    background: transparent !important;
}}


/* -------------------------------------------------------------
   SUB-TAB BAR (Depth 2: ML Lab Inner Tabs)
------------------------------------------------------------- */
[data-baseweb="tab-panel"] [data-baseweb="tab-list"] {{
    background: rgba(0,0,0,0.03) !important;
    border-radius: 12px !important;
    padding: 0.3rem !important;
    gap: 0.5rem !important;
    border-bottom: none !important;
    margin-bottom: 1.5rem !important;
    width: 100% !important;
    display: flex !important;
}}
[data-baseweb="tab-panel"] [data-baseweb="tab"] {{
    border-radius: 8px !important;
    border-bottom: none !important;
    font-size: 0.95rem !important;
    padding: 0.5rem 1rem !important;
    background: transparent !important;
}}
[data-baseweb="tab-panel"] [aria-selected="true"] {{
    background: #ffffff !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
    border-bottom: none !important;
}}

/* -------------------------------------------------------------
   TAB TRANSITION ANIMATION
------------------------------------------------------------- */
[data-baseweb="tab-panel"] {{ animation: tabSlideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; opacity: 0; }}
@keyframes tabSlideUp {{ 0% {{ opacity: 0; transform: translateY(20px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}

/* -------------------------------------------------------------
   MAIN CONTENT CARDS (Real Glassmorphism)
------------------------------------------------------------- */
[data-testid="stVerticalBlockBorderWrapper"], .stForm {{
    background: linear-gradient(135deg, rgba(248, 250, 252, 0.95), rgba(226, 232, 240, 0.8)) !important; 
    backdrop-filter: blur(48px) saturate(200%) !important; 
    -webkit-backdrop-filter: blur(48px) saturate(200%) !important;
    border: 1px solid rgba(148, 163, 184, 0.3) !important; 
    border-top: 5px solid #6366f1 !important;
    border-radius: 20px !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08), inset 0 2px 10px rgba(255, 255, 255, 1) !important;
    padding: 2rem !important; margin-bottom: 0.5rem !important; text-align: left !important;
    transition: all 0.3s ease !important;
}}
[data-testid="stVerticalBlockBorderWrapper"]:hover, .stForm:hover {{
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12), inset 0 2px 10px rgba(255, 255, 255, 1) !important;
    transform: translateY(-2px) !important;
}}

/* -------------------------------------------------------------
   RADIO BUTTONS (Strictly Vertical Options for Exams)
------------------------------------------------------------- */
div[role="radiogroup"] {{
    display: flex !important; flex-direction: column !important; align-items: stretch !important;
    gap: 0.6rem !important; margin-top: 0.5rem !important; width: 100% !important;
}}
div[role="radiogroup"] > label {{
    width: 100% !important;
    display: flex !important;
    background: rgba(248, 250, 252, 0.6) !important;
    border: 1px solid rgba(226, 232, 240, 0.8) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    margin-bottom: 0.5rem !important;
    transition: all 0.2s ease;
}}
div[role="radiogroup"] > label:hover {{
    background: rgba(241, 245, 249, 1) !important;
    border-color: #cbd5e1 !important;
}}
div[role="radiogroup"] > label:hover {{ background: rgba(255, 255, 255, 0.95) !important; border-color: #cbd5e1 !important; transform: scale(1.01) !important; box-shadow: 0 8px 20px rgba(0,0,0,0.06) !important; }}
div[role="radiogroup"] > label:has(input:checked) {{ border-color: {active_color} !important; background: #ffffff !important; box-shadow: 0 0 0 2px {active_color}, 0 8px 20px rgba(0,0,0,0.15) !important; font-weight: 800 !important; border: 2px solid {active_color} !important; transform: scale(1.01) !important; }}
div[role="radiogroup"] > label > div:first-child {{ display: none !important; }} 
div[role="radiogroup"] > label > div:nth-child(2) {{ font-family: 'JetBrains Mono', 'D2Coding', monospace !important; font-size: 1rem !important; color: #1e293b !important; font-weight: 600 !important; margin-left: 0 !important; text-align: left !important; width: 100% !important; }}

/* -------------------------------------------------------------
   BUTTONS
------------------------------------------------------------- */
.stButton > button {{ background-color: rgba(15, 23, 42, 0.85) !important; border-radius: 14px !important; padding: 0.6rem 1rem !important; font-size: 1.05rem !important; font-weight: 700 !important; width: 100%; border: none !important; box-shadow: 0 6px 16px rgba(15, 23, 42, 0.15) !important; transition: all 0.2s ease !important; }}
.stButton > button p, .stButton > button span, .stButton > button div {{ color: #ffffff !important; }}
.stButton > button:hover {{ transform: scale(1.01) !important; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.25) !important; background-color: #0f172a !important; }}
[data-testid="stButton"] button[kind="primary"] {{ background-color: {active_color} !important; box-shadow: 0 6px 16px rgba(0,0,0,0.2) !important; }}
[data-testid="stButton"] button[kind="primary"]:hover {{ filter: brightness(0.9); box-shadow: 0 8px 24px rgba(0,0,0,0.3) !important; }}



/* -------------------------------------------------------------
   RADIO BUTTON FULL WIDTH FIX (Prevent jumping)
------------------------------------------------------------- */
div[data-testid="stRadio"], div[data-testid="stRadio"] > div {{
    width: 100% !important;
}}

/* -------------------------------------------------------------
   SELECTBOX / DROPDOWN MENU FIX (Crisp resolution)
------------------------------------------------------------- */
div[data-baseweb="popover"], div[data-baseweb="popover"] * {{
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
}}
ul[role="listbox"] {{
    background-color: #ffffff !important;
    border: 1px solid rgba(0,0,0,0.1) !important;
    border-radius: 8px !important;
    box-shadow: 0 12px 40px rgba(0,0,0,0.12) !important;
}}
ul[role="listbox"] li {{
    font-family: 'Pretendard Variable', -apple-system, sans-serif !important;
    font-size: 0.95rem !important;
    color: #1e293b !important;
}}

/* -------------------------------------------------------------
   DESKTOP EXPLANATION BOX (Right Side)
------------------------------------------------------------- */
.floating-exp {{ 
    position: fixed; 
    top: 15%; 
    right: 2%; 
    width: 380px; 
    max-height: 80vh;
    overflow-y: auto;
    overflow-x: hidden;
    background: rgba(255, 255, 255, 0.85); 
    backdrop-filter: blur(32px) saturate(200%); 
    -webkit-backdrop-filter: blur(32px) saturate(200%);
    border: 1px solid rgba(255, 255, 255, 0.8); 
    border-radius: 24px; 
    box-shadow: 0 24px 64px rgba(31, 38, 135, 0.15), inset 0 1px 2px rgba(255,255,255,1); 
    padding: 2rem; 
    z-index: 9999; 
    text-align: left; 
    animation: slideInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1); 
}}

/* 태블릿 및 작은 모니터 환경 방어 (가로 스크롤 및 겹침 방지) */
@media screen and (max-width: 1250px) {{
    .floating-exp {{ 
        position: static !important; 
        width: 100% !important; 
        margin-top: 1.5rem !important; 
        animation: none !important; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important; 
        padding: 1.5rem !important; 
        border-radius: 16px !important; 
        max-height: none !important;
    }}
}}


/* -------------------------------------------------------------
   MOBILE EXTREME OPTIMIZATION
------------------------------------------------------------- */
@media screen and (max-width: 768px) {{
    /* 1. Forbidden Zone: 하단 여백을 6rem으로 강제하여 컨텐츠가 탭바에 안가려지게 함 */
    .block-container {{
    height: auto !important;
    max-height: none !important;
    overflow-y: auto !important;
    padding: 0.5rem 0.8rem 6rem 0.8rem !important; margin: 0 auto !important; }}
    
    [data-testid="stAppViewContainer"] {{
        overflow-y: auto !important;
    }}
    
    [data-testid="column"] {{
        max-height: none !important;
        overflow-y: visible !important;
    }}
    
    
    .custom-header {{ flex-direction: row !important; align-items: center !important; justify-content: flex-start !important; gap: 0.5rem !important; margin-bottom: 0.5rem !important; padding: 0 !important; text-align: left !important; }}
    .header-top-row {{ margin: 0 !important; gap: 0.5rem !important; justify-content: flex-start !important; }}
    .header-logo {{ width: 28px !important; height: 28px !important; border-radius: 6px !important; }}
    .header-title {{ font-size: 1.1rem !important; }}
    .header-subtitle {{ display: none !important; }}
    
    div[data-testid="stToggle"] {{ position: relative !important; top: 0 !important; right: 0 !important; margin-bottom: 0.5rem !important; justify-content: flex-start !important; }}
    div[data-testid="stToggle"]::before {{ font-size: 0.95rem; }}
    div[data-testid="stToggle"] label {{ font-size: 0.95rem !important; }}
    
    [data-testid="stVerticalBlockBorderWrapper"], .stForm {{
    background: linear-gradient(135deg, rgba(248, 250, 252, 0.95), rgba(226, 232, 240, 0.8)) !important; 
    backdrop-filter: blur(48px) saturate(200%) !important; 
    -webkit-backdrop-filter: blur(48px) saturate(200%) !important;
    border: 1px solid rgba(148, 163, 184, 0.3) !important; 
    border-top: 5px solid #6366f1 !important;
    border-radius: 20px !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.08), inset 0 2px 10px rgba(255, 255, 255, 1) !important;
    padding: 1rem !important; margin-bottom: 0.5rem !important; text-align: left !important;
    transition: all 0.3s ease !important;
}}
[data-testid="stVerticalBlockBorderWrapper"]:hover, .stForm:hover {{
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.12), inset 0 2px 10px rgba(255, 255, 255, 1) !important;
    transform: translateY(-2px) !important;
}}
    
    div[role="radiogroup"] > label {{ padding: 0.6rem 0.8rem !important; min-height: 2.8rem !important; border-radius: 10px !important; margin-bottom: 0 !important; }}
    div[role="radiogroup"] > label > div:nth-child(2) {{ font-size: 0.9rem !important; line-height: 1.3 !important; }}
    
    .hud-container {{
    flex-wrap: nowrap !important;
    white-space: nowrap !important; margin-bottom: 0.5rem !important; justify-content: flex-start !important; gap: 0.4rem !important; }}
    .hud-badge {{
    white-space: nowrap !important;
    min-width: max-content !important;
    word-break: keep-all !important; padding: 0.2rem 0.5rem !important; font-size: 0.75rem !important; }}
    
    /* 2. iOS Style Bottom Dock for Tabs */
    [data-baseweb="tab-list"] {{ 
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        max-width: 100vw !important;
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(24px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
        border-top: 1px solid rgba(0,0,0,0.1) !important;
        border-bottom: none !important;
        padding: 0.5rem 0.5rem calc(0.5rem + env(safe-area-inset-bottom)) 0.5rem !important;
        margin: 0 !important;
        display: flex !important;
        justify-content: space-around !important;
        gap: 0 !important;
        z-index: 99999 !important;
        box-shadow: 0 -4px 16px rgba(0,0,0,0.08) !important;
    }}
    
    [data-baseweb="tab"] {{ 
        flex: 1 !important;
        font-size: 0.8rem !important;
        font-weight: 700 !important;
        padding: 0.5rem 0 !important;
        border: none !important;
        border-bottom: none !important;
        background: transparent !important;
        border-radius: 12px !important;
    }}
    
    [aria-selected="true"] {{ 
        color: {active_color} !important; 
        border-bottom: none !important;
        background: rgba(0,0,0,0.04) !important; 
        box-shadow: none !important;
    }}
    
    [aria-selected="false"]:hover {{
        background: transparent !important;
    }}
    
    /* 3. Sub-tabs (Depth 2) Reset (Do NOT dock to bottom!) */
    [data-baseweb="tab-panel"] [data-baseweb="tab-list"] {{
        position: relative !important;
        bottom: auto !important;
        left: auto !important;
        width: 100% !important;
        background: rgba(0,0,0,0.03) !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        border-top: none !important;
        padding: 0.3rem !important;
        margin-bottom: 1.5rem !important;
        z-index: 1 !important;
        box-shadow: none !important;
        border-radius: 12px !important;
    }}
    
    [data-baseweb="tab-panel"] [data-baseweb="tab"] {{
        flex: 1 !important;
        font-size: 0.85rem !important;
        padding: 0.4rem !important;
        background: transparent !important;
        border-radius: 8px !important;
    }}
    [data-baseweb="tab-panel"] [aria-selected="true"] {{
        background: #ffffff !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
    }}
    
    .floating-exp {{ position: static; width: 100%; margin-top: 1rem !important; animation: none; box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 1rem !important; border-radius: 16px !important; }}
}}

/* 글로벌 가로 스크롤 완전 차단 (데스크탑 와이드 모니터 이슈 방어) 및 세로 스크롤바 시프트 방지 */
html, body, [data-testid="stAppViewContainer"], .main, .stApp, #root {{
    overflow-x: hidden !important;
}}
[data-testid="stAppViewContainer"] {{
    
}}


/* Native tab highlight restored */
[data-baseweb="tab-border"] {{ display: none !important; }}


[data-testid="column"]::-webkit-scrollbar {{
    display: none !important; /* Chrome/Safari */
}}

/* -------------------------------------------------------------
   FULL WIDTH OVERRIDE
------------------------------------------------------------- */

</style>



"""
 


