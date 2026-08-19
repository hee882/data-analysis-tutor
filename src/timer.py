import streamlit.components.v1 as components

def inject_timer(time_limit_sec, start_timestamp):
    html_code = f"""
    <script>
        const parentDoc = window.parent.document;
        let timerDiv = parentDoc.getElementById("live-exam-timer");
        if (!timerDiv) {{
            timerDiv = parentDoc.createElement("div");
            timerDiv.id = "live-exam-timer";
            timerDiv.style.cssText = "position: fixed; bottom: 30px; right: 30px; background-color: #1e293b; color: #f8fafc; padding: 12px 24px; border-radius: 12px; font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 800; z-index: 999999; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border: 2px solid #3b82f6; transition: all 0.3s ease;";
            parentDoc.body.appendChild(timerDiv);
            
            if (window.innerWidth <= 768) {{
                timerDiv.style.bottom = "15px";
                timerDiv.style.right = "15px";
                timerDiv.style.padding = "8px 16px";
                timerDiv.style.fontSize = "1.05rem";
                timerDiv.style.borderWidth = "1px";
            }}
        }}
        
        const startTime = {start_timestamp} * 1000;
        const timeLimit = {time_limit_sec} * 1000;
        
        if (window.timerInterval) clearInterval(window.timerInterval);
        
        window.timerInterval = setInterval(function() {{
            const now = new Date().getTime();
            const elapsed = now - startTime;
            const remaining = timeLimit - elapsed;
            
            if (remaining <= 0) {{
                clearInterval(window.timerInterval);
                timerDiv.innerHTML = "🚨 TIME UP";
                timerDiv.style.borderColor = "#ef4444";
                timerDiv.style.color = "#ef4444";
            }} else {{
                const m = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
                const s = Math.floor((remaining % (1000 * 60)) / 1000);
                timerDiv.innerHTML = "⏳ 남은 시간 " + (m < 10 ? "0"+m : m) + ":" + (s < 10 ? "0"+s : s);
                
                if (remaining < 300000) {{
                    timerDiv.style.borderColor = "#ef4444";
                    timerDiv.style.color = "#fca5a5";
                }}
            }}
        }}, 1000);
    </script>
    """
    components.html(html_code, height=0)

def remove_timer():
    html_code = """
    <script>
        const parentDoc = window.parent.document;
        let timerDiv = parentDoc.getElementById("live-exam-timer");
        if (timerDiv) timerDiv.remove();
        if (window.timerInterval) clearInterval(window.timerInterval);
    </script>
    """
    components.html(html_code, height=0)
