# TBC bot -> VPS (Python)

Files
- tbc_runtime.py  : runner that emulates Telebot Creator (Bot, bot, User, libs, HTTP, handleNextCommand, runCommandAfter, webhooks, broadcast)
- commands.json   : your 230 commands (TPY code, unchanged)
- bot_29034629_commands.py : same code as one readable .py (reference only)

## Setup (Ubuntu/Debian)
    sudo mkdir -p /opt/tbcbot && cd /opt/tbcbot      # upload all files here
    sudo apt install -y python3 python3-venv
    python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
    cp .env.example .env && nano .env                # put BOT_TOKEN
    ./venv/bin/python tbc_runtime.py                 # test run (Ctrl+C to stop)

Run 24/7
    sudo cp tbcbot.service /etc/systemd/system/
    sudo systemctl daemon-reload && sudo systemctl enable --now tbcbot
    journalctl -u tbcbot -f                          # live logs

Stop the bot on TBC first (only one thing can poll a token at a time).

## IMPORTANT: your data does NOT move automatically
TBC's stored data (balances, users, admins, settings) lives on TBC. This runner starts with an empty
database (bot_data.sqlite3). The first person to /start becomes owner/admin, like a fresh bot.
To keep old users/balances you must export them from TBC (Bot.getAllData / getBotUsersFile) and import them.

## Naya/updated command code TBC se lagana (commands.txt)
Agar TBC mein code change kiya hai, to us bot ke commands export karke is folder mein `commands.txt` naam se rakh do
(format: har command `=== /name ===` ke baad uska code). Runner start hote hi `commands.txt` ko `commands.json`
se pehle load karta hai (log mein "loaded N commands from commands.txt" dikhega). Bot restart karna padega:
    sudo systemctl restart tbcbot        (VPS)      |      tmux mein Ctrl+C phir python tbc_runtime.py (Termux)
Database (bot_data.sqlite3) alag file hai, wo delete/overwrite nahi hota.

## What differs from TBC
- libs.tbcads (TBC ads): not available -> always "no ad". Ad-gated steps will not show ads.
- Payment/verification webhooks (libs.Webhook): set PUBLIC_URL to a public https URL that forwards
  to WEBHOOK_PORT (nginx/caddy reverse proxy). Without it, webhook-based verification won't complete.
- Bot.broadcast: simple built-in sender (~20 msg/s) to everyone who has used the bot since migration.
- Account.stop_bot (auto-stop) does not exist here.

## Security note: hard-coded reporting to the original author
Your code contains a hard-coded other bot token (8327459100:...) and chat 6925391837 in
/AutoCheckBot (sends "Auto Stop Alert", then tries to stop your bot after 7 days if <50 users) and in
/ResetAllBalanceConfirm (sends a list of ALL user IDs and balances to that chat).
The runner BLOCKS outbound calls that match BLOCKED_OUTBOUND (default: that token and chat id) and logs
"BLOCKED outbound request". Edit/remove those lines in commands.json if you want them gone for good.
