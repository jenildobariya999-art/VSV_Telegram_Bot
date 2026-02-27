# utils.py
import sqlite3
import requests
from datetime import datetime
from config import VSV_TOKEN

# Initialize DB
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    balance REAL DEFAULT 0,
                    referral_code TEXT,
                    referred_by TEXT,
                    last_daily_bonus TEXT,
                    wallet TEXT
                )""")
    conn.commit()
    conn.close()

# Add user to DB
def add_user(user_id, username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users(user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()

# Get user info
def get_user(user_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

# Update user balance
def update_balance(user_id, new_balance):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET balance=? WHERE user_id=?", (new_balance, user_id))
    conn.commit()
    conn.close()

# Update last daily bonus date
def update_daily_bonus_date(user_id, date_str):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET last_daily_bonus=? WHERE user_id=?", (date_str, user_id))
    conn.commit()
    conn.close()

# VSV Payment function
def vsv_transfer(paytm_number, amount, comment):
    url = f"https://vsv-gateway-solutions.co.in/Api/api.php?token={VSV_TOKEN}&paytm={paytm_number}&amount={amount}&comment={comment}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}
