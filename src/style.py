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
   LAYOUT
------------------------------------------------------------- */
.block-container {{ 
    padding: 1rem 1rem 6rem 1rem !important; 
    max-width: 650px !important; 
    margin: 0 auto 0 10% !important;
    overflow-x: hidden !important;
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

/* 글로벌 스위처 (Toggle) 중앙 정렬 */
div[data-testid="stToggle"] {{
    display: flex !important; justify-content: center !important; margin-bottom: 1rem !important;
}}
div[data-testid="stToggle"] label {{ color: {active_color} !important; font-weight: 700 !important; }}

/* -------------------------------------------------------------
   TAB BAR (PC: Floating, Mobile: Docked)
------------------------------------------------------------- */
[data-baseweb="tab-list"] {{
    position: fixed !important; bottom: 1.5rem !important; left: 50% !important; transform: translateX(-50%) !important;
    width: 90% !important; max-width: 500px !important;
    background: rgba(255, 255, 255, 0.8) !important; backdrop-filter: blur(24px) saturate(200%) !important; -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
    border: 1px solid rgba(255, 255, 255, 0.9) !important; border-radius: 99px !important;
    padding: 0.4rem !important; margin: 0 !important; z-index: 9999 !important;
    display: flex !important; justify-content: space-between !important; gap: 0.2rem !important;
    box-shadow: 0 12px 32px rgba(0,0,0,0.1), inset 0 2px 4px rgba(255,255,255,1) !important;
}}
[data-baseweb="tab"] {{ 
    flex: 1 !important; border-radius: 99px !important; font-size: 0.95rem !important; font-weight: 700 !important; 
    padding: 0.6rem 0 !important; color: #64748b !important; background: transparent !important; border: none !important;
}}
[aria-selected="true"] {{ background: {active_color} !important; color: #ffffff !important; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important; border: none !important; }}
[aria-selected="false"]:hover {{ background: rgba(255, 255, 255, 0.5) !important; color: #0f172a !important; }}

/* -------------------------------------------------------------
   TAB TRANSITION ANIMATION
------------------------------------------------------------- */
[data-baseweb="tab-panel"] {{ animation: tabSlideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards !important; opacity: 0; }}
@keyframes tabSlideUp {{ 0% {{ opacity: 0; transform: translateY(20px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}

/* -------------------------------------------------------------
   MAIN CONTENT CARDS (Real Glassmorphism)
------------------------------------------------------------- */
[data-testid="stVerticalBlockBorderWrapper"], .stForm {{
    background: rgba(255, 255, 255, 0.8) !important; backdrop-filter: blur(48px) saturate(160%) !important; -webkit-backdrop-filter: blur(48px) saturate(160%) !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important; border-radius: 24px !important;
    box-shadow: 0 32px 64px rgba(0, 0, 0, 0.08), inset 0 2px 6px rgba(255, 255, 255, 0.6) !important;
    padding: 1.5rem !important; margin-bottom: 0.5rem !important; text-align: left !important;
}}

/* -------------------------------------------------------------
   RADIO BUTTONS (Strictly Vertical Options for Exams)
------------------------------------------------------------- */
div[role="radiogroup"] {{
    display: flex !important; flex-direction: column !important; align-items: stretch !important;
    gap: 0.6rem !important; margin-top: 0.5rem !important; width: 100% !important;
}}
div[role="radiogroup"] > label {{
    background: rgba(255, 255, 255, 0.6) !important; backdrop-filter: blur(12px) !important; border: 1px solid rgba(255, 255, 255, 0.9) !important;
    border-radius: 14px !important; padding: 0.8rem 1rem !important; width: 100% !important; min-height: 3.5rem !important;
    display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: flex-start !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02) !important; transition: all 0.2s ease !important; margin: 0 !important;
}}
div[role="radiogroup"] > label:hover {{ background: rgba(255, 255, 255, 0.95) !important; border-color: #cbd5e1 !important; transform: scale(1.01) !important; box-shadow: 0 8px 20px rgba(0,0,0,0.06) !important; }}
div[role="radiogroup"] > label[data-checked="true"] {{ border-color: {active_color} !important; background: #ffffff !important; box-shadow: 0 0 0 2px {active_color}, 0 8px 20px rgba(0,0,0,0.1) !important; transform: scale(1.01) !important; }}
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
   DESKTOP EXPLANATION BOX (Right Side)
------------------------------------------------------------- */
.floating-exp {{ 
    position: fixed; 
    top: 15%; 
    right: 3rem; 
    width: 450px; 
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

/* -------------------------------------------------------------
   MOBILE EXTREME OPTIMIZATION (??)
------------------------------------------------------------- */
@media screen and (max-width: 768px) {{
    .block-container {{ padding: 0.5rem 0.8rem 4rem 0.8rem !important; margin: 0 auto !important; }}
    
    .custom-header {{ flex-direction: row !important; align-items: center !important; justify-content: flex-start !important; gap: 0.5rem !important; margin-bottom: 0.5rem !important; padding: 0 !important; text-align: left !important; }}
    .header-top-row {{ margin: 0 !important; gap: 0.5rem !important; justify-content: flex-start !important; }}
    .header-logo {{ width: 28px !important; height: 28px !important; border-radius: 6px !important; }}
    .header-title {{ font-size: 1.1rem !important; }}
    .header-subtitle {{ display: none !important; }}
    
    div[data-testid="stToggle"] {{ margin-bottom: 0.5rem !important; justify-content: flex-start !important; }}
    
    [data-testid="stVerticalBlockBorderWrapper"], .stForm {{ padding: 1rem 1rem !important; border-radius: 16px !important; margin-bottom: 0.5rem !important; }}
    
    div[role="radiogroup"] > label {{ padding: 0.6rem 0.8rem !important; min-height: 2.8rem !important; border-radius: 10px !important; margin-bottom: 0 !important; }}
    div[role="radiogroup"] > label > div:nth-child(2) {{ font-size: 0.9rem !important; line-height: 1.3 !important; }}
    
    .hud-container {{ margin-bottom: 0.5rem !important; justify-content: flex-start !important; gap: 0.4rem !important; }}
    .hud-badge {{ padding: 0.2rem 0.5rem !important; font-size: 0.75rem !important; }}
    
    [data-baseweb="tab-list"] {{ 
        bottom: 0 !important; width: 100% !important; border-radius: 0 !important; border-top: 1px solid rgba(0,0,0,0.1) !important;
        padding: 0.3rem 0.2rem 1rem 0.2rem !important; max-width: none !important;
    }}
    [data-baseweb="tab"] {{ font-size: 0.85rem !important; padding: 0.4rem 0 !important; }}
    [aria-selected="true"] {{ border-radius: 8px !important; box-shadow: none !important; background: transparent !important; color: {active_color} !important; border-bottom: 3px solid {active_color} !important; }}
    
    .floating-exp {{ position: static; width: 100%; margin-top: 1rem !important; animation: none; box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 1rem !important; border-radius: 16px !important; }}
}}
</style>
"""
 
