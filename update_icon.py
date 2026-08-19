with open('web_pandas_tutor.py', 'r', encoding='utf-8') as f:
    t = f.read()

t = t.replace('st.set_page_config(page_title="Data Science & ML Bootcamp", layout="wide", initial_sidebar_state="collapsed")',
              'st.set_page_config(page_title="Data Science & ML Bootcamp", page_icon="logo.jpeg", layout="wide", initial_sidebar_state="collapsed")')

with open('web_pandas_tutor.py', 'w', encoding='utf-8') as f:
    f.write(t)
