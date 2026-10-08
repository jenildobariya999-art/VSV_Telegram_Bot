# Panel — saare bots ek server par (TBC jaisa UI)

Phone-first dark UI (Home, Bots, Errors, Settings, More). Ek hi process mein 100-200+ bots.

## Kya-kya hai
- **Home:** active users, commands run, total/working bots, 24h activity chart, most active bots
- **Bots:** search, filter, pin, export, Start/Stop; "+" se tokens add (ek line = ek token), "⋮" se Start/Stop all
- **Bot > Intro | Commands | Search | Mini App | Manage | Admin | Settings**
  - Commands: search, naya, edit, delete, syntax-check (✓), select+delete (🗑), export (</>)
  - Editor: line numbers, **suggestions** (`Bot.sendmsg` likho -> `Bot.sendMessage`), Enter/Tab se pura snippet, Tab se agle blank par, Ctrl+Space se list
  - Search: saare commands ke code mein dhundo (Aa / |ab| / .*), History, **Replace All** (jo replace syntax tod de wo skip hota hai)
  - Admin: Analytics (users 24h/7d/30d, new, blocked, commands lines), Users (balance edit), Broadcasts, Bot Data
  - Manage/Settings: restart, import/export, token change, error alert Telegram ID, delete
- **Errors:** command chalane par jo error aaye wo seedha dikhta hai: command, **line number**, error aur code ka tukda.
  Bell par laal dot, command list mein laal dot, editor mein us line par highlight.
  Bot Settings mein apna Telegram ID daalo to error aate hi bot tumhe message bhej deta hai.

## Import / Export
- Import: `.json` (kai formats samajhta hai), `.txt` (`=== /name ===`), `.py`; saath mein bot data bhi (JSON mein `bot_data` ho to)
- Export: bot JSON (commands + data), commands .txt, saare bots ZIP, full backup (More)
- ZIP import: file ke naam mein bot ka @username ho

## Setup (VPS, Ubuntu 24.04)
    sudo mkdir -p /opt/tbcbot && cd /opt/tbcbot          # zip yahin unzip karo
    sudo apt install -y python3 python3-venv
    python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
    cp .env.example .env && nano .env                    # PANEL_PASSWORD badlo (lamba!)
    ./venv/bin/python tbc_panel.py                       # test; browser: http://SERVER_IP:2222
    sudo cp tbcpanel.service /etc/systemd/system/ && sudo systemctl daemon-reload
    sudo systemctl enable --now tbcpanel                 # 24/7
    journalctl -u tbcpanel -f                            # live logs
Termux: `pip install flask requests waitress`, same .env, `python tbc_panel.py`, phone browser mein http://localhost:2222

## HTTPS (zaroori hai agar internet par khola)
Panel se code chalta hai (editor = server par code execution), isliye:
1. Lamba password rakho. 2. HTTPS lagao. Sabse aasan Caddy:
       sudo apt install -y caddy
       echo 'panel.yourdomain.com { reverse_proxy localhost:2222 }' | sudo tee /etc/caddy/Caddyfile && sudo systemctl restart caddy
   (domain ka A record VPS IP par). Phir .env mein PUBLIC_URL=https://panel.yourdomain.com
3. Firewall: sudo ufw allow 22,80,443/tcp && sudo ufw enable   (2222 band; Caddy se hi access)

## 220 bots shift karne ka tareeka
1. TBC par har bot Stop karo (ek token par ek hi jagah chal sakta hai).
2. Panel > Bots > "Add bots": saare tokens paste karo.
3. Har bot ke commands TBC se export karke ek ZIP banao, file ka naam mein bot ka @username ho.
4. Panel > "Bulk import commands (ZIP)".
5. Bots Start karo. Users/balance ka purana data TBC se nahi aata (README.md dekho).

## Limits
- RAM andaza: ~1-2 GB 170+ bots ke liye. Zyada traffic ho to WORKERS_PER_BOT badhao.
- libs.tbcads (TBC ads) yahan nahi hota. Webhooks ke liye PUBLIC_URL zaroori.
