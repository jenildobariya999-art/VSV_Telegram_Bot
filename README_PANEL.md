# TBC-Lite panel — saare bots ek server par

Panel = apna chhota TBC. Ek hi process mein 100-200+ bots chalte hain, web dashboard se control hota hai.

## Kya milta hai
- Login (password), Dashboard (bots, running, users, active 24h, activity chart)
- Bots list: Start / Stop / Restart, search, filter
- Bahut saare tokens ek saath add (ek line = ek token), ya kisi bot ke commands copy karke naya bot
- Command editor (live: save karte hi chalu bot par lagu), naya/delete, syntax check
- Import / Export commands (TBC wala `=== /name ===` .txt, ya .py/.json), saare bots ke liye ZIP import
- Per-bot Logs (errors yahin dikhte hain), Data (Bot.getData keys dekho/edit/import)
- Har bot ka alag database: data/bots/<id>/data.sqlite3, commands: data/bots/<id>/commands.json

## Setup (VPS, Ubuntu 24.04)
    sudo mkdir -p /opt/tbcbot && cd /opt/tbcbot          # zip yahin unzip karo
    sudo apt install -y python3 python3-venv
    python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
    cp .env.example .env && nano .env                    # PANEL_PASSWORD badlo (lamba!)
    ./venv/bin/python tbc_panel.py                       # test; browser: http://SERVER_IP:8000
    sudo cp tbcpanel.service /etc/systemd/system/ && sudo systemctl daemon-reload
    sudo systemctl enable --now tbcpanel                 # 24/7
    journalctl -u tbcpanel -f                            # live logs
Termux: `pip install flask requests waitress`, same .env, `python tbc_panel.py`, phone browser mein http://localhost:8000

## HTTPS (zaroori hai agar internet par khola)
Panel se code chalta hai (editor = server par code execution), isliye:
1. Lamba password rakho. 2. HTTPS lagao. Sabse aasan Caddy:
       sudo apt install -y caddy
       echo 'panel.yourdomain.com { reverse_proxy localhost:8000 }' | sudo tee /etc/caddy/Caddyfile && sudo systemctl restart caddy
   (domain ka A record VPS IP par). Phir .env mein PUBLIC_URL=https://panel.yourdomain.com
3. Firewall: sudo ufw allow 22,80,443/tcp && sudo ufw enable   (8000 band; Caddy se hi access)

## 220 bots shift karne ka tareeka
1. TBC par har bot Stop karo (ek token par ek hi jagah chal sakta hai).
2. Panel > Bots > "Add bots": saare tokens paste karo.
3. Har bot ke commands TBC se export karke ek ZIP banao, file ka naam mein bot ka @username ho.
4. Panel > "Bulk import commands (ZIP)".
5. Bots Start karo. Users/balance ka purana data TBC se nahi aata (README.md dekho).

## Limits
- RAM andaza: ~1-2 GB 170+ bots ke liye. Zyada traffic ho to WORKERS_PER_BOT badhao.
- libs.tbcads (TBC ads) yahan nahi hota. Webhooks ke liye PUBLIC_URL zaroori.
