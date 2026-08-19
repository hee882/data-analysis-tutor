import os
import json
import streamlit as st
from datetime import datetime
from supabase import create_client

def get_supabase_client():
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except Exception:
        return None

def load_leaderboard():
    supabase = get_supabase_client()
    if supabase:
        try:
            response = supabase.table('leaderboard').select('*').order('score', desc=True).execute()
            return response.data
        except Exception:
            return []
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_score(name, score, strategy="bootcamp_day1_4"):
    supabase = get_supabase_client()
    if supabase:
        try:
            supabase.table('leaderboard').insert({"name": f"{name}###{strategy}", "score": score}).execute()
            return True
        except Exception:
            return False
    lb = load_leaderboard()
    lb.append({"name": f"{name}###{strategy}", "score": score, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")})
    lb = sorted(lb, key=lambda x: x['score'], reverse=True)
    with open("leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(lb, f, ensure_ascii=False, indent=4)
    return True
