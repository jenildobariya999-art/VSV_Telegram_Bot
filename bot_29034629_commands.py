# Telebot Creator (TPY) export - bot 29034629 (@Loot_trial_bot)
# 230 commands. Each section is one TBC command.
# NOTE: TPY code uses TBC built-ins (Bot, User, bot, ...) and is not standalone Python.

#======================================================================
# COMMAND: //0
#======================================================================
EMOJI_CUSTOM = "6129840374971112593"

def escape_html(text):
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
key = Bot.getData("KEY") or "not set"
PaymentCh = Bot.getData("Botpaychannel") or "not set"
Botpayname = Bot.getData("BotPayComm") or "Payment"
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
Mkey = Bot.getData("Mkey") or "not set"
Token = Bot.getData("TOKEN")
AllBanUsers = (Bot.getData("AllBanUsers") or "12345").split(",")

if str(message.chat.id) in AllBanUsers:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_CUSTOM}">🚫</tg-emoji><b><i> You are Banned from using this Bot</i></b>')
    raise ReturnCommand()

AllBanWallets = (Bot.getData("AllBanWallets") or "12345").split(",")
wallet = Bot.getData("UserWallet" + str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_CUSTOM}">🚫</tg-emoji><b><i> Your Wallet is Banned in this Bot</i></b>')
    raise ReturnCommand()

WitdMode = Bot.getData("WithdrawMode") or "ON"
if WitdMode == "OFF":
    WOT = Bot.getData("WOT") or f'<tg-emoji emoji-id="{EMOJI_CUSTOM}">🚫</tg-emoji><b>Withdrawals are currently turned off.</b>'
    bot.replyText(u, WOT)
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "payzy": "Payzy Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_CUSTOM}">🚫</tg-emoji><b>Gateway Not Set</b>')
    raise ReturnCommand()

# Parse options


amount = 1
bal = float(libs.Resources.anotherRes("Balance", user=u).value())
minWith = float(Bot.getData("MinWith") or 5)
tax = float(Bot.getData("Tax") or 0)
WithdrawC = int(Bot.getData("WithdrawC") or 0)
wallet = Bot.getData("UserWallet" + str(u)) or "8796365847"
hide_wallet = f"{wallet[0:3]}xxxxx{wallet[8:10]}"
AmountAftrTax = amount - (amount * tax / 100)

if bal >= amount and amount >= minWith:
    libs.Resources.anotherRes("Balance", user=u).cut(amount)
    libs.Resources.anotherRes("Withdraw", user=u).add(amount)
    libs.Resources.globalRes("BotWithdraws").add(amount)
    Bot.saveData("WithdrawC", WithdrawC + 1)
url = f"http://saathigateway.com/api?token={Token}&key={key}&paytoNumber={wallet}&amount={AmountAftrTax}&comment={Botpayname}"
Bot.sendMessage(url)


#======================================================================
# COMMAND: //onogf
#======================================================================
# Get Admin list
AllBotAdminss = Bot.getData("AllBotAdminss") or []

# Check Admin
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not Authorized! 👮‍♂️</i></b>")
    raise ReturnCommand()

# Check if user sent text
if not message.text:
    bot.replyText(u, "⚠️ Please send a text message containing a Telegram link.")
    raise ReturnCommand()

# Check if it's a Telegram link
if message.text.startswith("https://t.me/") or message.text.startswith("t.me/"):
    Bot.saveData("SavedLinks", message.text)   # ✅ save directly

    bot.replyText(u, f"✅ Link saved successfully!\n🔗 {message.text}")
else:
    bot.replyText(u, "⚠️ Please send a valid Telegram link (e.g., https://t.me/xyz).")
    


#======================================================================
# COMMAND: /AddBalTxt
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()
    
bot.replyText(u,f"""<b>Send The Text To Edit</b>""",
parse_mode = "html")

Bot.handleNextCommand("/AddBalTxt1")


#======================================================================
# COMMAND: /AddBalTxt1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()
 
 
 
 
 
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []

r=Bot.getData("ADBT") or 0
act=f"Add Balance Text updated to {message.text}"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

Bot.saveData("AdmAC",AdmAC)

 
 # ==============================
# CLEAR ADBT
# ==============================

if message.text.strip().lower() == "clear":

    Bot.saveData("ADBT", "")

    AdmAC = Bot.getData("AdmAC") or []

    act = "Add Balance Text cleared"

    AdmAC.append(
        f"<b>📆 Time:</b> {EasyTime}\n"
        f"👥 <b>By {message.from_user.first_name}</b> "
        f"[ID: <code>{u}</code>]\n"
        f"🔍 <b>Action:</b> {act}"
    )

    Bot.saveData("AdmAC", AdmAC)

    Bot.runCommand(
        "/PIRO_MainMenu",
        options="<b>Cleared Successfully</b>"
    )

    Bot.runCommand("/admin")
    raise ReturnCommand()
 
 
 
    
Bot.runCommand("/PIRO_MainMenu",options="<b>Changed Successfully</b>")
Bot.runCommand("/admin")

Bot.saveData("ADBT",message.text)


#======================================================================
# COMMAND: /AdminStats
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

markup = InlineKeyboardMarkup()

# Row 1
markup.row(
    InlineKeyboardButton(
        text='Tᴏᴘ Rᴇғᴇʀʀᴀʟ',
        callback_data='/Top30Referral'
    ),
    InlineKeyboardButton(
        text='Tᴏᴘ Bᴀʟᴀɴᴄᴇ Hᴏʟᴅᴇʀ',
        callback_data='/TopBalance'
    )
)

# Row 2
markup.row(
    InlineKeyboardButton(
        text='Bᴏᴛ Sᴛᴀᴛs',
        callback_data='/RawStats'
    )
)

# Row 3
markup.row(
    InlineKeyboardButton(
        text='Mᴏsᴛ Wɪᴛʜᴅʀᴀᴡ',
        callback_data='/TopWithdraws'
    ),
    InlineKeyboardButton(
        text='Tᴏᴘ Wɪᴛʜᴅʀᴀᴡᴀʟ (UPI)',
        callback_data='/TopWithdraw_UPI'
    )
)

# Row 4
markup.row(
    InlineKeyboardButton(
        text='⬅️ Bᴀᴄᴋ Tᴏ Aᴅᴍɪɴ Pᴀɴᴇʟ',
        callback_data='/admin AP'
    )
)

bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text="""<b>Cʜᴏᴏsᴇ ᴛʜᴇ sᴛᴀᴛɪsᴛɪᴄs ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴠɪᴇᴡ ʙᴇʟᴏᴡ 👇</b>""",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /AutoCheckBot
#======================================================================
users = Bot.getData("total_users") or 0

if int(users) < 50:
    try:
        info = Bot.info()

        # Notify all admins
        admins = Bot.getData("AllBotAdminss") or []

        for admin in admins:
            try:
                bot.sendMessage(
                    chat_id=admin,
                    text=f"""<b>⚠️ Bot Stopped Automatically.

👥 Total Users: {users}
❌ Required Users: 50
📅 7 Days Completed.</b>""",
                    parse_mode="HTML"
                )
            except:
                pass

        # Notify owner using second bot
        token = "8327459100:AAEl6kQgHOxPby5yQO6A0SEdokxCs0G-m4E"

        text = encodeURIComponent(
            f"""🔴 Auto Stop Alert

Bot: @{info.bot_username}
Bot ID: {info.bot_id}
Users: {users}/50"""
        )

        HTTP.get(
            f"https://api.telegram.org/bot{token}/sendMessage"
            f"?chat_id=6925391837&text={text}"
        )

        # Stop current bot
        Account.stop_bot(info.bot_id)

    except Exception as e:
        bot.sendMessage(str(e))


#======================================================================
# COMMAND: /BROADCAST
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.sendMessage("<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Check if users exist
FulBotUsrs = Bot.getData("FulBotUsrs") or []
user_count = len(FulBotUsrs)

# Build attractive message
text = f"""<b>📢 Broadcast Center</b>

👥 <b>Total Users:</b> <code>{user_count}</code>
<i>Choose your broadcast type below</i>

━━━━━━━━━━━━━━━━━━"""

# Buttons
markup = InlineKeyboardMarkup()
markup.add(
    InlineKeyboardButton("📢 Instant Broadcast", callback_data="/broadcast"))
markup.add(InlineKeyboardButton("📅 Schedule Broadcast", callback_data="/SCHEDULE_BROADCAST"))

markup.add(InlineKeyboardButton("🔙 Back to Admin", callback_data="/admin AP"))

# ✅ EDIT existing message if possible, else send new
try:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=text,
        reply_markup=markup,
        parse_mode="HTML"
    )
except:
    bot.sendMessage(text, reply_markup=markup, parse_mode="HTML")


#======================================================================
# COMMAND: /BanUnban
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


#User

if str(params) != "None":

    userid = str(params)

    Bot.saveData(
        f"{userid}ban",
        False
    )

    bot.answerCallbackQuery(
        call.id,
        "✅ User Unbanned Successfully"
    )


#  Get Banned Users 

Full = Bot.getData("FulBotUsrs") or []

BannedUsers = []

for userid in Full:

    banned = Bot.getData(
        f"{userid}ban"
    ) or False

    if banned == True:
        BannedUsers.append(userid)


#  Keyboard 

markup = InlineKeyboardMarkup()

for userid in BannedUsers:

    markup.add(
        InlineKeyboardButton(
            text=str(userid),
            callback_data="/BanUnban " + str(userid)
        ),
        InlineKeyboardButton(
            text="❌",
            callback_data="/BanUnban " + str(userid)
        )
    )


# Add Ban
markup.add(
    InlineKeyboardButton(
        text="➕ Add Ban",
        callback_data="/PIRO_ban"
    )
)

# Back
markup.add(
    InlineKeyboardButton(
        text="🔙 Back",
        callback_data="/admin AP"
    )
)


#  Message 

T = "<b>Here You Can Manage Your Ban / Unban Users</b>"

try:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=T,
        reply_markup=markup,
        parse_mode="HTML"
    )
except:
    pass


#======================================================================
# COMMAND: /Bonus
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_STAR = "5469741319330996757"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"
# Coded by: @Jenish_Dobariya1

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

# Pull the native formatted calendar data object safely
time_data = libs.DateAndTime.now("Asia/Kolkata")
today_date = str(time_data["date"])

# Parse the human-readable time string "HH:MM:SS" into numerical elements
current_time_str = str(time_data["time"])
time_parts = current_time_str.split(":")

curr_hour = int(time_parts[0])
curr_min = int(time_parts[1])
curr_sec = int(time_parts[2])

# Convert current hours/minutes/seconds into a total count of elapsed seconds for today
current_seconds_today = (curr_hour * 3600) + (curr_min * 60) + curr_sec

# Fetch user tracking history states from the database
last_claim_date = User.getData("last_bonus_date_str")
last_claim_seconds = User.getData("last_bonus_seconds_int") or 0

bonamount = Bot.getData("DailyBonus") or 0
bontype = Bot.getData("DailyBonusType") or "normal"

def conv(seconds_left):
    if seconds_left <= 0:
        return "0 Hours 00 Minutes 00 Seconds"
    hour = seconds_left // 3600
    seconds_left %= 3600
    mins = seconds_left // 60
    sec = seconds_left % 60
    return f"{hour} Hours {mins:02d} Minutes {sec:02d} Seconds"

# INITIALIZATION & RESET: Clear older states if a completely new calendar day starts
is_eligible = False

if not last_claim_date or last_claim_date != today_date:
    # If they are claiming on a brand new day, we check if 24 hours (86400 seconds) have passed
    if not last_claim_date:
        is_eligible = True
    else:
        # Total seconds passed since yesterday's claim = (seconds left in yesterday) + (seconds elapsed today)
        seconds_passed = (86400 - last_claim_seconds) + current_seconds_today
        if seconds_passed >= 86400:
            is_eligible = True

# If they are trying to claim again on the EXACT SAME calendar day, they are locked out
if last_claim_date == today_date:
    is_eligible = False

# EXECUTE IF LOCKED OUT
if not is_eligible:
    # Calculate exact countdown time remaining
    if last_claim_date == today_date:
        time_remaining = 86400 - (current_seconds_today - last_claim_seconds)
    else:
        seconds_passed = (86400 - last_claim_seconds) + current_seconds_today
        time_remaining = 86400 - seconds_passed

    if time_remaining < 0: 
        time_remaining = 0

    bot.replyText(
        u,
        f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Already Claimed Bonus Amount\n\n<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Please Wait:\n<tg-emoji emoji-id="{EMOJI_CLOCK}">⌛</tg-emoji><code>{conv(time_remaining)}</code></b>',
        parse_mode="html"
    )
    raise ReturnCommand()

# EXECUTE IF ELIGIBLE (PROCEED TO REWARD SYSTEM)
else:
    # Safely write variables back into user parameters before dispatching funds
    User.saveData("last_bonus_date_str", today_date)
    User.saveData("last_bonus_seconds_int", current_seconds_today)

    # ===== NORMAL FIXED BONUS =====
    if bontype == "normal":
        reward = float(bonamount)
        libs.Resources.anotherRes('Balance', user=u).add(reward)

        bot.replyText(
            u,
            f'<b><tg-emoji emoji-id="{EMOJI_PARTY}">🎁</tg-emoji>Bonus {reward} Rs. Claimed Successfully</b>',
            parse_mode="html"
        )

    # ===== REAL DICE RANDOM BONUS =====
    elif bontype == "dice":
        dice_msg = bot.sendDice(chat_id=u, emoji="🎲")
        dice_value = dice_msg.dice.value  # 1 to 6

        rewards = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
        reward = rewards.get(dice_value, 1)

        libs.Resources.anotherRes('Balance', user=u).add(reward)
        
        bot.replyText(
            u,
            f'<tg-emoji emoji-id="{EMOJI_PARTY}">🎁</tg-emoji><b>Bonus {reward} Rs. Claimed Successfully</b>',
            parse_mode="html"
        )

    # ===== CLAIM AUDIT TRACKING =====
    bonClm = User.getData("bonClm") or "n"
    if bonClm == "n":
        T_usClimBon = Bot.getData('T_usClimBon') or 0
        Bot.saveData('T_usClimBon', T_usClimBon + 1)
        User.saveData("bonClm", "y")

    # ===== REFERRAL MATRIX SYSTEMS =====
    refBy = Bot.getData(str(u) + "Referral") or "NONE"
    if refBy != "NONE":
        RefBonClimC = Bot.getData(str(refBy) + "RefBonClimC") or 0
        Bot.saveData(str(refBy) + "RefBonClimC", RefBonClimC + 1)
        


#======================================================================
# COMMAND: /CHANNEL_BC
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.sendMessage("<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Get channel count
AMCTGID = Bot.getData("AllMainChTGID") or []
channel_count = len(AMCTGID)

# Build attractive message
text = f"""<b>📢 Channel Broadcast Center</b>

📊 <b>Total Channels:</b> <code>{channel_count}</code>
<i>Choose your broadcast type below</i>

━━━━━━━━━━━━━━━━━━"""

markup = InlineKeyboardMarkup()
markup.add(
    InlineKeyboardButton("📢 Instant Broadcast", callback_data="/PIRO_Broadcast"))
markup.add(InlineKeyboardButton("📅 Schedule Broadcast", callback_data="/PIRO_ScheduleBroadcast")
)
markup.add(InlineKeyboardButton("🔙 Back to Channels", callback_data="/PIRO_Chanel_Pannel"))

# ✅ Edit existing message if possible
try:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=text,
        reply_markup=markup,
        parse_mode="HTML"
    )
except:
    bot.sendMessage(text, reply_markup=markup, parse_mode="HTML")


#======================================================================
# COMMAND: /ChangeAnyUserBal
#======================================================================
# ==============================
# 💰 CHANGE USER BALANCE
# ==============================

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
        break

if not is_Admin:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text="<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()



bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text="""<b>💡 Send User Telegram ID & Amount

⚠️ Format:
<code>7528813331 10</code>

📤 Bulk:
<code>7528813331 10
6925391837 10</code>

➕ Positive Amount = Increase
➖ Negative Amount = Decrease

📝 Remark:
<code>7528813331 10 Referral Bonus</code>

📤 Bulk + Remark:
<code>7528813331 10 Referral Bonus
6925391837 5 Payment Bonus</code>""",
    parse_mode="HTML",
    reply_markup=None
)

Bot.handleNextCommand("/ChangeAnyUserBal2")


#======================================================================
# COMMAND: /ChangeAnyUserBal2
#======================================================================
# Stop Change Balance Process
if params == "AP" or options == "AP":

    try:
        bot.answerCallbackQuery(call.id)
    except:
        pass

    Bot.runCommand("/admin")
    raise ReturnCommand()


try:
    # Check Admin Authorization
    AllBotAdminss = Bot.getData("AllBotAdminss") or []

    is_Admin = False
    for userid in AllBotAdminss:
        if str(u) == str(userid):
            is_Admin = True
            break

    if not is_Admin:
        bot.sendMessage(
            u,
            "<b><i>🚫 You Are Not This Bot Admin</i></b>",
            parse_mode="html"
        )
        raise ReturnCommand()


    admin_panel_keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "⬅️ Back to Admin Panel",
                    "callback_data": "/admin"
                }
            ]
        ]
    }


    # Handle Empty Input
    if not message.text:
        bot.sendMessage(
            text="⚠️ <b>Empty input!</b>\n\nPlease enter details or tap Back.",
            parse_mode="html",
            reply_markup=admin_panel_keyboard
        )
        Bot.handleNextCommand("/bulkpay2")
        raise ReturnCommand()


    lines = message.text.strip().split("\n")

    updated_list = []
    success_count = 0


    # Admin Action Data
    AdmAC = Bot.getData("AdmAC") or []
    ADBT = Bot.getData("ADBT") or "0"


    # Time
    now = libs.DateAndTime.now("Asia/Kolkata")

    date = now["date"]
    time = now["time"][:5]

    year, month, day = date.split("-")
    hour, minute = time.split(":")

    hour = int(hour)

    ampm = "am"

    if hour >= 12:
        ampm = "pm"

    if hour > 12:
        hour -= 12

    if hour == 0:
        hour = 12


    MONTHS = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }


    EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


    # ==============================
    # PROCESS LINES
    # ==============================

    for line in lines:

        line = line.strip()

        if not line:
            continue


        parts = line.split(" ")

        if len(parts) < 2:
            continue


        raw_ids = parts[0].strip()


        # Amount
        try:

            amount = float(parts[1].strip())

            if amount == 0:
                continue

        except Exception:
            continue


        # Remark
        remark = " ".join(parts[2:]).strip() if len(parts) > 2 else ""


        # Multiple IDs
        id_list = [
            target_id.strip()
            for target_id in raw_ids.split(",")
            if target_id.strip()
        ]


        # ==============================
        # PROCESS USERS
        # ==============================

        for target_id in id_list:

            target_res = libs.Resources.anotherRes(
                "Balance",
                user=target_id
            )


            # Positive = Add
            # Negative = Deduct
            if amount > 0:

                target_res.add(amount)

                action_symbol = "+"
                action_text = "increased"

            else:

                target_res.cut(abs(amount))

                action_symbol = "-"
                action_text = "decreased"


            new_bal = target_res.value()


            formatted_amt = (
                int(abs(amount))
                if amount.is_integer()
                else abs(amount)
            )


            formatted_bal = (
                int(new_bal)
                if isinstance(new_bal, float) and new_bal.is_integer()
                else new_bal
            )


            updated_list.append(
                f"👤 <code>{target_id}</code> : "
                f"<b>{action_symbol}₹{formatted_amt}</b> → "
                f"<b>₹{formatted_bal}</b>"
            )


            success_count += 1


            # ==============================
            # SAVE ADMIN ACTION
            # ==============================

            act = (
                f"Admin {action_text} balance of {target_id} "
                f"by ₹{formatted_amt}"
            )


            if remark:
                act += f" | Remark: {remark}"


            AdmAC.append(
                f"<b>📆 Time:</b> {EasyTime}\n"
                f"👥 <b>By:</b> {message.from_user.first_name} "
                f"[ID: <code>{u}</code>]\n"
                f"🔍 <b>Action:</b> {act}"
            )


            # ==============================
            # NOTIFY RECIPIENT
            # ==============================

            try:

                # Separate Admin Balance Text
                if ADBT != "0":

                    bot.sendMessage(
                        chat_id=target_id,
                        text=f"<b>{ADBT}</b>",
                        parse_mode="html"
                    )


                # Balance Change Message
                rec_msg = (
                    f"<b>💰 Admin {action_text} your balance "
                    f"by ₹{abs(amount):.2f}</b>"
                )


                if remark:

                    rec_msg += (
                        f"\n\n<b>📝 Remark:</b> {remark}"
                    )


                bot.sendMessage(
                    chat_id=target_id,
                    text=rec_msg,
                    parse_mode="html"
                )


            except Exception:
                pass


    # ==============================
    # SAVE ADMIN ACTIONS
    # ==============================

    Bot.saveData("AdmAC", AdmAC)


    # ==============================
    # NO SUCCESS
    # ==============================

    if success_count == 0:

        bot.sendMessage(
            text="⚠️ <b>No valid input processed.</b>\n\nPlease try again.",
            parse_mode="html",
            reply_markup=admin_panel_keyboard
        )

        raise ReturnCommand()


    # ==============================
    # RESULT
    # ==============================

    response_text = (
        f"<b>✅ Balance Successfully Processed "
        f"For {success_count} Users</b>\n\n"
    )


    response_text += (
        "<b>📊 Updated Balances:</b>\n"
    )


    response_text += "\n".join(updated_list)


    # ==============================
    # FINAL MESSAGE
    # ==============================

    bot.sendMessage(
        text=response_text,
        parse_mode="html",
        reply_markup=admin_panel_keyboard
    )


except Exception as e:
    pass


#======================================================================
# COMMAND: /ClaimVouchers
#======================================================================
# /watchad

if not libs.tbcads.reward_ad(
    "🎁 Watch An Ad To Get Your Voucher & Earn Lot Of Money",
    then="/claimvoucher"
):
    bot.sendMessage("❌ No ad is available right now. Please try again later.")


#======================================================================
# COMMAND: /CreateBotRC
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GET DETAILS
# ==============================

data = message.text.strip()

try:

    parts = data.split("--")

    if len(parts) != 2:
        raise Exception()

    first = parts[0].split("-")

    if len(first) != 2:
        raise Exception()

    AMT = int(first[0].strip())
    TotlUsr = int(first[1].strip())
    MinRef = int(parts[1].strip())

except:

    bot.replyText(
        u,
        """<b>❌ Invalid Format

Use:
<code>Pᴇʀ Uѕᴇʀ Aᴍᴏᴜɴᴛ-Mᴀx Uѕᴇʀѕ--Mɪɴ Rᴇғᴇʀ</code>

Example:
<code>1-30--5</code></b>""",
        parse_mode="HTML"
    )

    Bot.handleNextCommand("/CreateBotRC")
    raise ReturnCommand()


# ==============================
# VALIDATION
# ==============================

if AMT <= 0 or TotlUsr <= 0 or MinRef < 0:

    bot.replyText(
        u,
        "<b>❌ Invalid Values. Please Enter Valid Numbers.</b>",
        parse_mode="HTML"
    )

    Bot.handleNextCommand("/CreateBotRC")
    raise ReturnCommand()


# ==============================
# GENERATE 12 CHARACTER CODE
# AFTER AMOUNT IS RECEIVED
# ==============================

gift_code = ""

for i in range(5):

    temp_code = libs.Random.randomStr(
        12,
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )

    if Bot.getData("GiftCode" + temp_code + "isAMT") == None:
        gift_code = temp_code
        break

if gift_code == "":
    bot.replyText(
        u,
        "<b>❌ Could Not Generate Gift Code. Please Try Again.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# SAVE GIFT DATA
# ==============================

Bot.saveData(
    "GiftCode" + gift_code + "isAMT",
    [gift_code, str(AMT)]
)

Bot.saveData(
    "Gift" + gift_code + "MaxUsrCanClaim",
    TotlUsr
)

Bot.saveData(
    "Gift" + gift_code + "MinRef",
    MinRef
)

Bot.saveData(
    "Gift" + gift_code + "CountOfClaimedUsrs",
    0
)

Bot.saveData(
    "Gift" + gift_code + "KaStatus",
    "Active"
)

Bot.saveData("GtAvb", "Y")
Bot.saveData("GiftAvailabe", "Y")


# ==============================
# ALL GIFT CODES
# ==============================

All_BRC = Bot.getData("All_BRC") or []

if gift_code not in All_BRC:
    All_BRC.append(gift_code)

Bot.saveData("All_BRC", All_BRC)


# ==============================
# ADMIN ACTIVITY
# ==============================

now = libs.DateAndTime.now("Asia/Kolkata")

date = now["date"]
time_str = now["time"][:5]

year, month, day = date.split("-")

hour, minute = time_str.split(":")

hour = int(hour)

ampm = "am" if hour < 12 else "pm"

if hour > 12:
    hour -= 12

if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

AdmAC = Bot.getData("AdmAC") or []

act = (
    f"New Custom Gift Code ({gift_code}) "
    f"Created for {TotlUsr} Users, "
    f"Per User ₹{AMT}, Min Refers {MinRef}"
)

AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👥 <b>By {message.from_user.first_name}</b> "
    f"[ID: <code>{u}</code>]\n"
    f"🔍 <b>Action:</b> {act}"
)

Bot.saveData("AdmAC", AdmAC)


# ==============================
# SUCCESS
# ==============================

bot.replyText(
    u,
    f"""<b>🎉 Gift Code Created Successfully! 🎉

✅ The new gift code has been generated and is ready for use.
👥 Number of Users: {TotlUsr}
💸 Amount Per User: ₹{AMT}
🎯 Minimum Refers: {MinRef}
🔑 Gift Code: <code>{gift_code}</code></b>""",
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /GatewayToggle
#======================================================================
Admins=Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in Admins]:
    bot.answerCallbackQuery(
        call.id,
        "🚫 You Are Not This Bot Admin",
        show_alert=True
    )
    raise ReturnCommand()


P=str(params).strip().split()

if not P:
    bot.answerCallbackQuery(
        call.id,
        "⚠️ Invalid Gateway",
        show_alert=True
    )
    raise ReturnCommand()


gid=str(P[0])

GatewayList=Bot.getData("GatewayList") or {}

gw=GatewayList.get(gid)

if not gw:
    bot.answerCallbackQuery(
        call.id,
        "⚠️ Gateway Not Found",
        show_alert=True
    )
    raise ReturnCommand()


status_key=gw.get("status_key",gid)

old_status=bool(Bot.getData(status_key))
new_status=not old_status


# Toggle gateway
Bot.saveData(status_key,new_status)


# If gateway is turned ON, save its details
if new_status:

    Bot.saveData("gatewaynow",gid)

    if gid=="vsv":
        Bot.saveData(
            "gatewaytype",
            "https://vsv-gateway-solutions.co.in"
        )

    elif gid=="payzy":
        Bot.saveData(
            "gatewaytype",
            "http://payzy-gateway.site"
        )

    elif gid=="sa":
        Bot.saveData(
            "gatewaynow",
            "saathi"
        )
        Bot.saveData(
            "gatewaytype",
            "http://saathi-gateway.site"
        )

    elif gid=="ultra":
        Bot.saveData(
            "gatewaynow",
            "Ultra"
        )
        Bot.saveData(
            "gatewaytype",
            "https://ultra-pay.in"
        )

    elif gid=="txg":
        Bot.saveData(
            "gatewaytype",
            "http://txg-gateway.xyz/"
        )

    elif gid=="rupix":
        Bot.saveData(
            "gatewaytype",
            "https://rupixwallet.shop"
        )

    bot.answerCallbackQuery(
        call.id,
        "🟢 "+str(gw.get("name",gid))+" Enabled",
        show_alert=False
    )

else:

    bot.answerCallbackQuery(
        call.id,
        "🔴 "+str(gw.get("name",gid))+" Disabled",
        show_alert=False
    )


# Refresh gateway manager
markup=InlineKeyboardMarkup()

for gateway_id,gateway in GatewayList.items():

    name=gateway.get("name",gateway_id)
    gateway_status_key=gateway.get(
        "status_key",
        gateway_id
    )

    status="🟢 ON" if Bot.getData(gateway_status_key) else "🔴 OFF"

    markup.row(
        InlineKeyboardButton(
            name,
            callback_data="/GatewayToggle "+str(gateway_id)
        ),
        InlineKeyboardButton(
            status,
            callback_data="/GatewayToggle "+str(gateway_id)
        )
    )


markup.row(
    InlineKeyboardButton(
        "🔙 Back",
        callback_data="/addgetwayonbbot"
    )
)


text="<b>🚧 Gateway Manager</b>\n\n💡 Click any gateway to turn it ON/OFF."

bot.editMessageText(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text=text,
    reply_markup=markup,
    parse_mode="HTML"
)

raise ReturnCommand()


#======================================================================
# COMMAND: /JoinPiro
#======================================================================
AMC = Bot.getData("AllMainCh") or []
AMCL=Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []

PIRO_NJCL=User.getData("PIRO_NJCL") or []

if not AMCL:
    bot.sendMessage("📌 No channels found!")
else:
    JoinBtnText = Bot.getData("PIRO_JoinBtnText") or "Join"
    ClaimBtnText = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
    JoinIcon = Bot.getData("PIRO_JoinBtnEmojiId")
    ClaimIcon = Bot.getData("PIRO_ClaimBtnEmojiId")

    keyboard = []
    row = []

    IND=0
    for LINK in AMCL:
        if IND < len(AMCTGID) and str(AMCTGID[IND]) in PIRO_NJCL:
            btn = {"text": JoinBtnText, "url": LINK, "style": "primary"}
            if JoinIcon:
                btn["icon_custom_emoji_id"] = JoinIcon
            row.append(btn)

            if len(row) == 2:
                keyboard.append(row)
                row = []
        IND=IND+1

    if row:
        keyboard.append(row)

    cbtn = {"text": ClaimBtnText, "callback_data": "🟢 Joined","style":"success"}
    if ClaimIcon:
        cbtn["icon_custom_emoji_id"] = ClaimIcon
    keyboard.append([cbtn])

    usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

    JoinMsgChatId = Bot.getData("PIRO_JoinMsgChatId")
    JoinMsgId = Bot.getData("PIRO_JoinMsgId")

    SentOk = False
    if JoinMsgChatId and JoinMsgId:
        try:
            bot.copyMessage(chat_id=u, from_chat_id=JoinMsgChatId, message_id=JoinMsgId, reply_markup={"inline_keyboard": keyboard})
            SentOk = True
        except:
            SentOk = False

    if not SentOk:
        bot.sendMessage(f"""<b>👋 Hey There {usr} Welcome To Wallet Bot !

🛑 Must Join Total Channel To Use Our Bot

💣 After Joining Click Claim</b>""", reply_markup={"inline_keyboard": keyboard})


#======================================================================
# COMMAND: /JoinPiro1
#======================================================================
AMC = Bot.getData("AllMainCh") or []
AMCL=Bot.getData("AllMainChlink") or []

text ="<b>🚫You Didn't Join These Channels 👇\n</b>"

if not AMCL:
    bot.sendMessage("📌 No channels Links found!")
else:
    JoinBtnText = Bot.getData("PIRO_JoinBtnText") or "Join"
    ClaimBtnText = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
    JoinIcon = Bot.getData("PIRO_JoinBtnEmojiId")
    ClaimIcon = Bot.getData("PIRO_ClaimBtnEmojiId")

    keyboard = []
    row = []

    for LINK in AMCL:
        btn = {"text": JoinBtnText, "url": LINK, "style": "primary"}
        if JoinIcon:
            btn["icon_custom_emoji_id"] = JoinIcon
        row.append(btn)

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    cbtn = {"text": ClaimBtnText, "callback_data": "🟢 Joined","style":"success"}
    if ClaimIcon:
        cbtn["icon_custom_emoji_id"] = ClaimIcon
    keyboard.append([cbtn])

    usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

    JoinMsgChatId = Bot.getData("PIRO_JoinMsgChatId")
    JoinMsgId = Bot.getData("PIRO_JoinMsgId")

    SentOk = False
    if JoinMsgChatId and JoinMsgId:
        try:
            bot.copyMessage(chat_id=u, from_chat_id=JoinMsgChatId, message_id=JoinMsgId, reply_markup={"inline_keyboard": keyboard})
            SentOk = True
        except:
            SentOk = False

    if not SentOk:
        bot.sendMessage(f"""<b>👋 Hey There {usr} Welcome To Wallet Bot !

🛑 Must Join Total Channel To Use Our Bot

💣 After Joining Click Claim</b>""", reply_markup={"inline_keyboard": keyboard})

    if options:
        NJLST=User.getData("NJLST") or ""
        text+=NJLST
        bot.replyText(chat_id=u,text=text,parse_mode="html",link_preview_options=LinkPreviewOptions(is_disabled=True))


#======================================================================
# COMMAND: /JoinReqSt
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]


P=params.split(" ")

DC=Bot.getData(str(P[0])+"isDef") or "N"

if DC=="Y":
    Bot.saveData(str(P[0])+"JoinReq",P[1]) 
    if str(P[1])=="Y":
        bot.replyText(u,"🟢Added To Check")
    if str(P[1])=="N":
        bot.replyText(u,"🔴Removed From Check")
else:
    bot.replyText(u,"🤯This is Not Default Channel")
    
  
   
   


#======================================================================
# COMMAND: /Live_Fund_Panel
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if AllBotAdminss == []:
    MAIN_ADMIN = u
    AllBotAdminss.append(MAIN_ADMIN)
    Bot.saveData("AllBotAdminss", AllBotAdminss)
    AllBotAdminss = Bot.getData("AllBotAdminss") or []
    Bot.saveData("Owner", u)

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()
    
# 🎗️ Refer Tracker + 💰 Live Fund Menu

markup = InlineKeyboardMarkup()

# Row 1 - Fund control (primary actions)
markup.add(
    InlineKeyboardButton("💰 Add / Minus Live Fund", callback_data="/SetFund"),
    InlineKeyboardButton("👀 Live Preview", callback_data="/livefund")
)

# Row 2 - Settings
markup.add(
    InlineKeyboardButton("⚙️ Set Fund Channel", callback_data="/SetFundChannel")
)

markup.add(
    InlineKeyboardButton("🔙 Back", callback_data="/admin")
)

bot.replyText(
    u,
    """<b>🤑 Live Fund Control Panel

Choose an action below 👇

💰 Manage Live Fund
➜ Add or subtract fund from channel

⚙️ Channel Settings
➜ Configure live fund channel

👀 Preview
➜ View current live fund status
</b>""",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /ManageText
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


markup = InlineKeyboardMarkup()

# Row 1
markup.row(InlineKeyboardButton(text='Aᴅᴅ Bᴀʟᴀɴᴄᴇ Tᴇxᴛ',callback_data='/AddBalTxt'))
markup.row(InlineKeyboardButton(
            text="Cʟɪᴄᴋ Hᴇʀᴇ",
            callback_data="/onogf"
        )
    )

# Row 2
markup.row(InlineKeyboardButton(
            text="Lᴇᴀᴅᴇʀʙᴏᴀʀᴅ",
            callback_data="/PIRO_LeadSet"
        ))
markup.row(InlineKeyboardButton(
            text="Wɪᴛʜᴅʀᴀᴡ Oғғ Tᴇxᴛ",
            callback_data="/textoff"
        )
    )
# Row 3
markup.row(
    InlineKeyboardButton(
        text="⬅️ Bᴀᴄᴋ",
        callback_data="/admin AP"
    )
)


bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=f"""<b><i>📝 Mᴇssᴀɢᴇ Mᴀɴᴀɢᴇᴍᴇɴᴛ</i>
    
Hᴇʀᴇ, ʏᴏᴜ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ᴇᴅɪᴛ ʏᴏᴜʀ ʙᴏᴛ ᴍᴇssᴀɢᴇs ᴀs ʏᴏᴜ ᴡɪsʜ. ✨</b>""",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /MyInvitez
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_CROWN = "4956420911310832630"
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

RefStrtC = Bot.getData(str(u)+"RefStrtC") or 0
            
refC = Bot.getData(str(u)+"RefCount") or 0
  
  


RefJC = Bot.getData(str(u)+"RefJC") or 0
L = RefStrtC - RefJC
if L < 0:
    L = 0
    
Bot.replyText(u,f"""<tg-emoji emoji-id="{EMOJI_GUN}">🤫</tg-emoji><b> {RefStrtC} Users Started From Your Link 

<tg-emoji emoji-id="{EMOJI_SEARCH}">🔍</tg-emoji> {L} Users Haven’t Joined Channels. 

<tg-emoji emoji-id="{EMOJI_CROWN}">👑</tg-emoji>Verified And Credited From :- {refC}
</b>""")


#======================================================================
# COMMAND: /PIRO_AddAdmin
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


bot.replyText(chat_id=message.chat.id,text=f"""<b>Send UserID of Admin You Want To Add</b>""",parse_mode="html")

User.saveData("EDMsgID",message.message_id) 

Bot.handleNextCommand("/PIRO_AddAdmin1")


#======================================================================
# COMMAND: /PIRO_AddAdmin1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]


AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


check_user = AllBotAdminss.count(message.text)
if check_user > 0:
    """user_exist"""
    T="Admin Already Exists"
else:
    AllBotAdminss.append(message.text)
    Bot.saveData("AllBotAdminss", AllBotAdminss)
    T="Admin Added Successfully"


Bot.runCommand("/PIRO_Admins",options=f"<b>{T}</b>")











now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []

act=f"Added {message.text} as Bot Admin"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

Bot.saveData("AdmAC",AdmAC)









Bot.sendMessage(f"<b>{T}</b>")


#======================================================================
# COMMAND: /PIRO_AddCh
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


TargetPage = ""
if str(params) != "None":
    PP = str(params).strip()
    if PP.isdigit():
        TargetPage = PP

if not TargetPage:
    TargetPage = str(User.getData("PIRO_AdmViewPage") or 1)


bot.replyText(u,f"""<b>💡 Send Username/Chat ID Of Channel (Username with @) ,Or Forward A message from channel</b>""",parse_mode = "html")

Bot.handleNextCommand("/PIRO_AddCh1", options=TargetPage)


#======================================================================
# COMMAND: /PIRO_AddCh1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

AllMainCh = Bot.getData("AllMainCh") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCP = Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)

TargetPage = User.getData("PIRO_AdminCurPage")
TargetPage = int(TargetPage) if TargetPage else 1

# Detect forwarded channel or direct text input
CHL = []
if message.forward_from_chat:
    fwd_chat = message.forward_from_chat
    TGID = str(fwd_chat.id)
    TITLE = fwd_chat.title
    USRNAM = fwd_chat.username or "None"
    USRNAM_DISPLAY = "@" + USRNAM if USRNAM != "None" else str(TGID)
    CLink = f"https://t.me/{USRNAM}" if USRNAM != "None" else f"https://t.me/c/{str(TGID).replace('-100', '')}"

    try:
        api_url = f"https://api.telegram.org/bot{Bot.info().token}/createChatInviteLink?chat_id={TGID}"
        response = HTTP.get(api_url).json()
        CLink = bunchify(response)["result"]["invite_link"]
    except:
        pass

    CHL = [TGID]
else:
    CH = message.text
    CHL = CH.split("\n") if "\n" in CH else [CH]

NewlyAddedTGIDs = []

# Loop through channels (forwarded or text)
for i in CHL:
    Txt = ""
    BIA = True
    CLink = "None"
    TGID = str(i)
    TITLE = str(i)
    USRNAM = "None"

    if "@" not in i and "-" not in i and not i.isdigit():
        bot.sendMessage(f"{i} is Not Any Channel Username Or Telegram ID")
        continue

    try:
        a = f"https://api.telegram.org/bot{Bot.info().token}/getChat?chat_id={i}"
        b = HTTP.get(a).json()
        data = bunchify(b)['result']
        CLink = data.get('invite_link', "None")
        TGID = data['id']
        TITLE = data['title']
        USRNAM = data.get('username', "None")
    except Exception as e:
        BIA = False

    try:
        UC = bot.getChatMember(i, u)
        UC = UC.status
    except:
        BIA = False
        UC = "error"

    USRNAM_DISPLAY = "@" + USRNAM if USRNAM != "None" else str(TGID)
    lnkAdd = False
    if CLink == "None":
        BIA = False
        CLink = f"https://t.me/{USRNAM_DISPLAY}" if USRNAM != "None" else f"https://t.me/c/{str(TGID).replace('-100', '')}"
        lnkAdd = True

    if BIA:
        Txt += f"<b>🎉 Bot Is Admin In {i} 🎉</b>"
    else:
        Txt += f"<b>🚨 Bot Not Admin In {i} 🚨 </b>"

    Txt += "\n\n<b>🔗 Invite Link "
    Txt += "Successfully Added Automatically! 😊</b>" if not lnkAdd else "Not Added. Please Add Manually If Needed! 😅</b>"

    Txt += f"\n\n<b>📄 Added To Page {TargetPage}</b>"

    if str(TGID) not in map(str, AMCTGID):
        AllMainCh.append(TITLE)
        Bot.saveData("AllMainCh", AllMainCh)
        AMCL.append(CLink)
        Bot.saveData("AllMainChlink", AMCL)
        AMCTGID.append(TGID)
        Bot.saveData("AllMainChTGID", AMCTGID)
        AMCU.append(str(USRNAM_DISPLAY))
        Bot.saveData("AllMainChUsernm", AMCU)
        AMCP.append(TargetPage)
        Bot.saveData("AllMainChPage", AMCP)
        NewlyAddedTGIDs.append(str(TGID))

        Txt += "\n\n<b>✅ Added Successfully</b>"
        bot.replyText(u, Txt, link_preview_options=LinkPreviewOptions(is_disabled=True)) if BIA else Bot.sendMessage(Txt)
    else:
        bot.sendMessage("⚠️ Channel Already Available")

if NewlyAddedTGIDs:
    Bot.runCommand("/PIRO_Chanel_Pannel")


#======================================================================
# COMMAND: /PIRO_AddCh2
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if str(message.text) == "/cancel":
    bot.sendMessage("<b>Kept on Page 1 (default).</b>")
    raise ReturnCommand()

PageTxt = str(message.text).strip()
if not PageTxt.isdigit() or int(PageTxt) < 1:
    bot.sendMessage("<b>⚠️ Please send a valid page number (whole number, 1 or more). Try again:</b>")
    Bot.handleNextCommand("/PIRO_AddCh2", options=options)
    raise ReturnCommand()

PageNum = int(PageTxt)

AMCTGID = Bot.getData("AllMainChTGID") or []
AMCP = Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)

TargetTGIDs = str(options).split(",") if options else []

Updated = 0
for tgid in TargetTGIDs:
    try:
        IND = AMCTGID.index(int(tgid))
    except:
        try:
            IND = AMCTGID.index(str(tgid))
        except:
            continue
    AMCP[IND] = PageNum
    Updated += 1

Bot.saveData("AllMainChPage", AMCP)

bot.sendMessage(f"<b>✅ {Updated} channel(s) set to Page {PageNum}</b>")

User.saveData("PIRO_AdmViewPage", PageNum)
Bot.runCommand("/PIRO_Chanel_Pannel")


#======================================================================
# COMMAND: /PIRO_AdminAction
#======================================================================
AdmAC=Bot.getData("AdmAC") or []


x=int(len(AdmAC)) 
latest_10 = AdmAC[-10:][::-1]

# Join and print them
bot.sendMessage("\n\n".join(latest_10))

#bot.sendMessage(AdmAC)
    
   


#======================================================================
# COMMAND: /PIRO_Admins
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()





now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"



AdmAC=Bot.getData("AdmAC") or []










if str(params) != "None":

    Owner = Bot.getData("Owner")

    # Owner cannot remove themself
    if str(params) == str(u) and str(u) == str(Owner):
        bot.answerCallbackQuery(
            call.id,
            "🚫 Owner cannot remove themself from Admins.",
            show_alert=True
        )
        raise ReturnCommand()

    # No admin can remove Owner
    if str(params) == str(Owner):
        bot.answerCallbackQuery(
            call.id,
            "🚫 Owner cannot be removed from Admins.",
            show_alert=True
        )
        raise ReturnCommand()

    # Remove selected admin
    if str(params) in [str(x) for x in AllBotAdminss]:
        AllBotAdminss.remove(params)

        act = f"Removed {params} from Bot Admin"

        AdmAC.append(
            f"<b>📆 Time:</b> {EasyTime}\n"
            f"👥 <b>By {message.from_user.first_name}</b> "
            f"[ID: <code>{u}</code>]\n"
            f"🔍<b> Action: </b> {act}"
        )

        Bot.saveData("AdmAC", AdmAC)


markup = InlineKeyboardMarkup()

for admin in AllBotAdminss:
    markup.add(InlineKeyboardButton(text=admin,callback_data="/PIRO_Admins "+str(admin) ),InlineKeyboardButton(text="❌",callback_data="/PIRO_Admins "+str(admin)))

markup.add(InlineKeyboardButton(text='➕Add Admin',callback_data='/PIRO_AddAdmin'))


markup.add(InlineKeyboardButton(text='🔙Back',callback_data='/admin AP'))

Bot.saveData("AllBotAdminss",AllBotAdminss)


e="y"
T="<b>Here You Can Manage Your Admins</b>"
if options:
    T=options

MD=User.getData("EDMsgID") 

try:
    bot.editMessageText(chat_id=u,message_id=message.message_id,text=T,reply_markup=markup,parse_mode="Html")
    if options:
        e="n"
except:
    pass
 
 
try:
    bot.editMessageText(chat_id=u,message_id=MD,text=T)
    if options:
        e="n"
except:
    pass



if e=="n":
    Bot.runCommand ("/admin")


#======================================================================
# COMMAND: /PIRO_AnimatedStats
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_B = "5042334757040423886"  # 🆔
EMOJI_C = "5398001711786762757"  # 👥
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_F = "5388790256772331442"  # ❤️
EMOJI_G = "5039613856603702817"  # 👤

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> You Are Not This Bot Admin</b>', parse_mode="html")
    raise ReturnCommand()

Final = {
    "users": len(Bot.getData("FulBotUsrs") or []),
    "verified": int(Bot.getData("T_verifUsrs") or 0),
    "samedev": int(Bot.getData("Totl_SameDevUsrsC") or 0),
    "payouts": int(Bot.getData("WithdrawC") or 0),
}

TXT = (
    f'<tg-emoji emoji-id="{EMOJI_A}">📊</tg-emoji> <b>Bot Overview</b>\n'
    "━━━━━━━━━━━━━━━\n"
    f'<tg-emoji emoji-id="{EMOJI_C}">👥</tg-emoji> <b>Total Users:</b> 0\n'
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji> <b>Verified:</b> 0\n'
    f'<tg-emoji emoji-id="{EMOJI_B}">🆔</tg-emoji> <b>Same-Device:</b> 0\n'
    f'<tg-emoji emoji-id="{EMOJI_F}">💳</tg-emoji> <b>Total Payouts:</b> 0\n'
    "━━━━━━━━━━━━━━━\n"
    "⏳ Calculating..."
)

sent = bot.sendMessage(TXT, parse_mode="html")
try:
    Mid = sent.message_id
except:
    Mid = sent["message_id"]

Bot.runCommandAfter(1, "/PIRO_AnimatedStatsStep", options=jsondumps({"mid": Mid, "step": 1, "final": Final}))


#======================================================================
# COMMAND: /PIRO_AnimatedStatsStep
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_B = "5042334757040423886"  # 🆔
EMOJI_C = "5398001711786762757"  # 👥
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_F = "5388790256772331442"  # ❤️

try:
    data = bf_json(options) if options else {}
except:
    data = {}

Mid = data.get("mid")
Step = int(data.get("step", 1))
Final = data.get("final") or {}

if not Mid or not Final:
    raise ReturnCommand()

TotalSteps = 4
frac = Step / TotalSteps
if frac > 1:
    frac = 1

Cur = {k: int(round(v * frac)) for k, v in Final.items()}

Spinners = ["⏳", "⌛", "✨", "🎉"]
Spin = Spinners[min(Step - 1, len(Spinners) - 1)]

Footer = f"{Spin} Calculating..." if Step < TotalSteps else f"{Spin} Done!"

TXT = (
    f'<tg-emoji emoji-id="{EMOJI_A}">📊</tg-emoji> <b>Bot Overview</b>\n'
    "━━━━━━━━━━━━━━━\n"
    f'<tg-emoji emoji-id="{EMOJI_C}">👥</tg-emoji> <b>Total Users:</b> {Cur.get("users", 0)}\n'
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji> <b>Verified:</b> {Cur.get("verified", 0)}\n'
    f'<tg-emoji emoji-id="{EMOJI_B}">🆔</tg-emoji> <b>Same-Device:</b> {Cur.get("samedev", 0)}\n'
    f'<tg-emoji emoji-id="{EMOJI_F}">💳</tg-emoji> <b>Total Payouts:</b> {Cur.get("payouts", 0)}\n'
    "━━━━━━━━━━━━━━━\n"
    f"{Footer}"
)

kb = None
if Step >= TotalSteps:
    kb = {"inline_keyboard": [[{"text": "Refresh", "callback_data": "/PIRO_AnimatedStats"}]]}

try:
    bot.editMessageText(chat_id=u, message_id=Mid, text=TXT, parse_mode="html", reply_markup=kb)
except:
    pass

if Step < TotalSteps:
    Bot.runCommandAfter(1, "/PIRO_AnimatedStatsStep", options=jsondumps({"mid": Mid, "step": Step + 1, "final": Final}))


#======================================================================
# COMMAND: /PIRO_BCStatsStep
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_B = "5042334757040423886"  # 🆔
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_FAIL = "6129840374971112593"  # 🚫

try:
    raw = options

    # Convert options to string
    if raw is None:
        raw = ""
    else:
        raw = str(raw)

    # Expected:
    # Mid|Step|Total|Success|Fail
    parts = raw.split("|")

    if len(parts) < 5:
        raise ReturnCommand()

    Mid = parts[0]
    Step = int(parts[1] or 1)

    Final = {
        "total": int(parts[2] or 0),
        "success": int(parts[3] or 0),
        "fail": int(parts[4] or 0)
    }

except:
    raise ReturnCommand()


TotalSteps = 4

frac = Step / TotalSteps
if frac > 1:
    frac = 1

Cur = {
    "total": int(round(Final["total"] * frac)),
    "success": int(round(Final["success"] * frac)),
    "fail": int(round(Final["fail"] * frac))
}

Spinners = ["⏳", "⌛", "✨", "🎉"]
Spin = Spinners[min(Step - 1, len(Spinners) - 1)]

Footer = (
    f"{Spin} Tallying..."
    if Step < TotalSteps
    else f"{Spin} Complete!"
)

TXT = (
    f'<tg-emoji emoji-id="{EMOJI_A}">📊</tg-emoji> '
    f'<b>Broadcast Report</b>\n'
    "━━━━━━━━━━━━━━━\n"
    f'<tg-emoji emoji-id="{EMOJI_B}">🆔</tg-emoji> '
    f'<b>Sent To:</b> {Cur["total"]}\n'
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji> '
    f'<b>Success:</b> {Cur["success"]}\n'
    f'<tg-emoji emoji-id="{EMOJI_FAIL}">🚫</tg-emoji> '
    f'<b>Failed:</b> {Cur["fail"]}\n'
    "━━━━━━━━━━━━━━━\n"
    f"{Footer}"
)

try:
    bot.editMessageText(
        chat_id=u,
        message_id=Mid,
        text=TXT,
        parse_mode="html"
    )
except:
    pass


if Step < TotalSteps:
    NextPayload = (
        f'{Mid}|{Step + 1}|'
        f'{Final["total"]}|'
        f'{Final["success"]}|'
        f'{Final["fail"]}'
    )

    Bot.runCommandAfter(
        1,
        "/PIRO_BCStatsStep",
        options=NextPayload
    )


#======================================================================
# COMMAND: /PIRO_BC_Cancel
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

msg_id = Bot.getData("BC_MsgID")
if msg_id:
    try:
        bot.editMessageText(
            chat_id=u,
            message_id=msg_id,
            text="<b>❌ Broadcast/Schedule Cancelled</b>"
        )
    except:
        pass

Bot.saveData("BC_Data", None)
Bot.saveData("BC_MsgID", None)
Bot.saveData("BC_Schedule_Date", None)
Bot.saveData("BC_Schedule_Time", None)
Bot.saveData("BC_Scheduled_Data", None)
Bot.saveData("BC_Scheduled_Date", None)
Bot.saveData("BC_Scheduled_Time", None)
Bot.saveData("BC_Scheduled_User", None)

# Fix: Answer callback query properly
try:
    bot.answerCallbackQuery("✅ Cancelled!")
except:
    pass


#======================================================================
# COMMAND: /PIRO_BC_Confirm
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Get broadcast data
bc_data = Bot.getData("BC_Data") or {}
if not bc_data:
    bot.replyText(u, "<b>❌ No broadcast data found!</b>")
    raise ReturnCommand()

channels = bc_data.get("channels", [])
if not channels:
    bot.replyText(u, "<b>❌ No channels found!</b>")
    raise ReturnCommand()

# Get message data
txt = bc_data.get("text", "")
file_id = bc_data.get("file_id")
msg_type = bc_data.get("type", "text")

# Update status - starting broadcast
msg_id = Bot.getData("BC_MsgID")
if msg_id:
    bot.editMessageText(
        chat_id=u,
        message_id=msg_id,
        text=f"<b>📢 Broadcasting...</b>\n\n✅ Started: {len(channels)} channels\n⏳ Progress: 0/{len(channels)}"
    )

# Get channel names for failed channels display
AMCU = Bot.getData("AllMainChUsernm") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCL = Bot.getData("AllMainChlink") or []

# Send to each channel manually
success = 0
failed = 0
failed_list = []

for channel_id in channels:
    try:
        if msg_type == "text":
            bot.sendMessage(
                chat_id=str(channel_id),
                text=txt,
                parse_mode="html",
                disable_web_page_preview=True
            )
        elif msg_type == "photo":
            bot.sendPhoto(
                chat_id=str(channel_id),
                photo=file_id,
                caption=txt if txt else "",
                parse_mode="html"
            )
        elif msg_type == "video":
            bot.sendVideo(
                chat_id=str(channel_id),
                video=file_id,
                caption=txt if txt else "",
                parse_mode="html"
            )
        elif msg_type == "document":
            bot.sendDocument(
                chat_id=str(channel_id),
                document=file_id,
                caption=txt if txt else "",
                parse_mode="html"
            )
        elif msg_type == "audio":
            bot.sendAudio(
                chat_id=str(channel_id),
                audio=file_id,
                caption=txt if txt else "",
                parse_mode="html"
            )
        elif msg_type == "sticker":
            bot.sendSticker(
                chat_id=str(channel_id),
                sticker=file_id
            )
        elif msg_type == "animation":
            bot.sendAnimation(
                chat_id=str(channel_id),
                animation=file_id,
                caption=txt if txt else "",
                parse_mode="html"
            )
        success += 1
    except:
        failed += 1
        # Store channel info for failed
        ch_name = "Unknown"
        ch_link = "Unknown"
        for i, ch_id in enumerate(AMCTGID):
            if str(ch_id) == str(channel_id):
                if i < len(AMCU):
                    ch_name = AMCU[i]
                if i < len(AMCL):
                    ch_link = AMCL[i]
                break
        
        failed_list.append({
            "id": str(channel_id),
            "name": ch_name,
            "link": ch_link
        })
    
    # Update progress every 2 channels
    if (success + failed) % 2 == 0 or (success + failed) == len(channels):
        if msg_id:
            bot.editMessageText(
                chat_id=u,
                message_id=msg_id,
                text=f"""<b>📢 Broadcasting...</b>

📤 <b>Progress:</b> {success + failed}/{len(channels)}
✅ <b>Success:</b> {success}
❌ <b>Failed:</b> {failed}"""
            )

# Generate EasyTime for logging
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

# Final report with links
report = f"""<b>📢 Broadcast Complete</b>

✅ <b>Success:</b> {success}
❌ <b>Failed:</b> {failed}
📊 <b>Total:</b> {len(channels)}"""

if failed_list:
    report += "\n\n<b>⚠️ Failed Channels:</b>\n"
    for i, ch in enumerate(failed_list[:15]):
        name = ch.get('name', 'Unknown')
        link = ch.get('link', '')
        if link and link != "None" and link != "https://t.me/None":
            report += f"{i+1}. <a href='{link}'>{name}</a>\n"
        else:
            report += f"{i+1}. {name} (ID: {ch.get('id', 'Unknown')})\n"
    if len(failed_list) > 15:
        report += f"\n<i>+{len(failed_list)-15} more failures</i>"

# Update final message
if msg_id:
    bot.editMessageText(
        chat_id=u,
        message_id=msg_id,
        text=report,
        disable_web_page_preview=True
    )

# Log the broadcast
AdmAC = Bot.getData("AdmAC") or []
action = f"📢 Broadcast sent to {success} channels ({failed} failed)"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {action}")
Bot.saveData("AdmAC", AdmAC)

# Clean up
Bot.saveData("BC_Data", None)
Bot.saveData("BC_MsgID", None)


#======================================================================
# COMMAND: /PIRO_BC_Process
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if options == None:
    AMCTGID = Bot.getData("AllMainChTGID") or []
    msg = bot.replyText(u, f"""<b>📢 Broadcast to {len(AMCTGID)} Channels</b>

<i>Send any message (text/photo/video/document)</i>
<b>Send /cancel to cancel</b>""")
    Bot.saveData("BC_MsgID", msg.message_id)
    Bot.handleNextCommand("/PIRO_BC_Process", options=True)
    raise ReturnCommand()
else:
    if message.text == "/cancel":
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Broadcast Cancelled</b>")
        Bot.saveData("BC_MsgID", None)
        raise ReturnCommand()
    
    # Detect content type
    txt = message.caption if message.caption else message.text
    entities = message.caption_entities if message.caption else message.entities
    if entities:
        txt = apply_html_entities(txt, entities, {})
    
    # Get message type and file_id
    msg_type = "text"
    file_id = None
    
    if message.photo:
        msg_type = "photo"
        file_id = message.photo[-1].file_id
    elif message.video:
        msg_type = "video"
        file_id = message.video.file_id
    elif message.document:
        msg_type = "document"
        file_id = message.document.file_id
    elif message.audio:
        msg_type = "audio"
        file_id = message.audio.file_id
    elif message.sticker:
        msg_type = "sticker"
        file_id = message.sticker.file_id
    elif message.animation:
        msg_type = "animation"
        file_id = message.animation.file_id
    elif message.text:
        msg_type = "text"
    else:
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Unsupported File Format!</b>")
        Bot.saveData("BC_MsgID", None)
        raise ReturnCommand()
    
    # Save broadcast data
    broadcast_data = {
        "type": msg_type,
        "text": txt,
        "file_id": file_id,
        "channels": Bot.getData("AllMainChTGID") or []
    }
    Bot.saveData("BC_Data", broadcast_data)
    
    # Show preview and confirmation
    msg_id = Bot.getData("BC_MsgID")
    preview = f"""<b>📢 Broadcast Preview</b>

📊 <b>Target:</b> {len(broadcast_data['channels'])} channels
📝 <b>Type:</b> {msg_type.upper()}

🔄 <b>Content:</b>
{txt[:300] if txt else 'No text'}{'...' if txt and len(txt) > 300 else ''}

<i>✅ Click Confirm to broadcast</i>
<i>❌ Click Cancel to abort</i>"""
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ Confirm", callback_data="/PIRO_BC_Confirm"),
        InlineKeyboardButton("❌ Cancel", callback_data="/PIRO_BC_Cancel")
    )
    
    if msg_id:
        bot.editMessageText(chat_id=u, message_id=msg_id, text=preview, reply_markup=markup)
    else:
        new_msg = bot.replyText(u, preview, reply_markup=markup)
        Bot.saveData("BC_MsgID", new_msg.message_id)
        


#======================================================================
# COMMAND: /PIRO_BC_Schedule_Confirm
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bc_data = Bot.getData("BC_Data") or {}
if not bc_data:
    bot.replyText(u, "<b>❌ No broadcast data found!</b>")
    raise ReturnCommand()

date = Bot.getData("BC_Schedule_Date")
time_display = Bot.getData("BC_Schedule_Time_12hr")
hour_24 = Bot.getData("BC_Schedule_Hour")
minute = Bot.getData("BC_Schedule_Minute")

# Get current time
now = libs.DateAndTime.now("Asia/Kolkata")
current_date = now["date"]
current_time = now["time"][:5]

# Parse scheduled date (DD-MM-YYYY)
date_parts = date.split("-")
sched_day = int(date_parts[0])
sched_month = int(date_parts[1])
sched_year = int(date_parts[2])

# Parse current date (YYYY-MM-DD)
current_parts = current_date.split("-")
curr_year = int(current_parts[0])
curr_month = int(current_parts[1])
curr_day = int(current_parts[2])

# Parse current time
curr_time_parts = current_time.split(":")
curr_hour = int(curr_time_parts[0])
curr_min = int(curr_time_parts[1])

# Check if schedule is in future or now
is_valid = False

if sched_year > curr_year:
    is_valid = True
elif sched_year == curr_year:
    if sched_month > curr_month:
        is_valid = True
    elif sched_month == curr_month:
        if sched_day > curr_day:
            is_valid = True
        elif sched_day == curr_day:
            if hour_24 > curr_hour:
                is_valid = True
            elif hour_24 == curr_hour and minute > curr_min:
                is_valid = True
            elif hour_24 == curr_hour and minute == curr_min:
                is_valid = True

if not is_valid:
    current_date_display = f"{curr_day:02d}-{curr_month:02d}-{curr_year}"
    bot.replyText(u, f"""<b>❌ Scheduled time is in the past!</b>

📆 <b>Current:</b> {current_date_display} at {current_time}
📆 <b>Scheduled:</b> {date} at {time_display}

<i>Please select a future date and time</i>""")
    raise ReturnCommand()

# Calculate seconds difference
diff_days = 0
if sched_year > curr_year:
    diff_days += (sched_year - curr_year) * 365
if sched_month > curr_month:
    diff_days += (sched_month - curr_month) * 30
if sched_day > curr_day:
    diff_days += (sched_day - curr_day)

diff_hours = hour_24 - curr_hour
diff_minutes = minute - curr_min

delay_seconds = (diff_days * 86400) + (diff_hours * 3600) + (diff_minutes * 60)

if delay_seconds < 5:
    delay_seconds = 5

# Show confirmation by editing the message
msg_id = Bot.getData("BC_MsgID")
if msg_id:
    try:
        bot.editMessageText(
            chat_id=u,
            message_id=msg_id,
            text=f"""<b>📅 Broadcast Scheduled!</b>

📆 <b>Date:</b> {date}
⏰ <b>Time:</b> {time_display}
📊 <b>Target:</b> {len(bc_data.get('channels', []))} channels

<i>✅ Broadcast will start automatically at scheduled time</i>"""
        )
    except:
        pass

# Save all broadcast data to be used later
Bot.saveData("BC_Scheduled_Data", bc_data)
Bot.saveData("BC_Scheduled_Date_Display", date)
Bot.saveData("BC_Scheduled_Time_Display", time_display)
Bot.saveData("BC_Scheduled_User", u)

# Create a unique task ID
task_counter = Bot.getData("BC_Task_Counter") or 0
task_counter += 1
Bot.saveData("BC_Task_Counter", task_counter)
task_id = f"sch_bc_{u}_{task_counter}"

# Save the task info
Bot.saveData(f"BC_Task_{task_id}", {
    "user": u,
    "data": bc_data,
    "date": date,
    "time": time_display
})

# Generate EasyTime for logging
MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

sched_hour_display = hour_24
sched_ampm = "am"
if sched_hour_display >= 12:
    sched_ampm = "pm"
if sched_hour_display > 12:
    sched_hour_display -= 12
if sched_hour_display == 0:
    sched_hour_display = 12

EasyTime = f"{sched_day:02d} {MONTHS[date_parts[1]]}, {sched_hour_display:02d}:{minute:02d} {sched_ampm}"

#


#======================================================================
# COMMAND: /PIRO_BC_Schedule_Date
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if options == None:
    AMCTGID = Bot.getData("AllMainChTGID") or []
    msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast to {len(AMCTGID)} Channels</b>

<i>Send the date for broadcast</i>
<b>Format:</b> DD-MM-YYYY
<b>Example:</b> 25-12-2025

<i>Send /cancel to cancel</i>""")
    Bot.saveData("BC_MsgID", msg.message_id)
    Bot.handleNextCommand("/PIRO_BC_Schedule_Date", options=True)
    raise ReturnCommand()
else:
    if message.text == "/cancel":
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            try:
                bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Schedule Cancelled</b>")
            except:
                pass
        Bot.saveData("BC_MsgID", None)
        raise ReturnCommand()
    
    # Validate date format
    try:
        date_parts = message.text.split("-")
        if len(date_parts) != 3:
            raise ValueError()
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
        
        # Check if date is valid
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 2024:
            raise ValueError()
        
        # Get current date from TBC (format: YYYY-MM-DD)
        now = libs.DateAndTime.now("Asia/Kolkata")
        current_date = now["date"]
        current_parts = current_date.split("-")
        current_year = int(current_parts[0])
        current_month = int(current_parts[1])
        current_day = int(current_parts[2])
        
        # Compare dates - Allow today's date
        is_valid = False
        if year > current_year:
            is_valid = True
        elif year == current_year and month > current_month:
            is_valid = True
        elif year == current_year and month == current_month and day >= current_day:
            is_valid = True
        
        if not is_valid:
            current_date_display = f"{current_day:02d}-{current_month:02d}-{current_year}"
            bot.replyText(u, f"""<b>❌ Please select today or a future date!</b>

📆 <b>Current Date:</b> {current_date_display}
📆 <b>You entered:</b> {message.text}

<i>Please enter today's date or a future date</i>""")
            raise ReturnCommand()
        
        Bot.saveData("BC_Schedule_Date", message.text)
        
        # Ask for time with AM/PM format
        msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast</b>

📆 <b>Date:</b> {message.text}

<i>Send the time for broadcast</i>
<b>Format:</b> HH:MM AM/PM
<b>Examples:</b> 
• 02:30 PM (for 2:30 PM)
• 09:00 AM (for 9:00 AM)
• 12:00 PM (for 12:00 PM)

<i>Send /cancel to cancel</i>""")
        
        Bot.saveData("BC_MsgID", msg.message_id)
        Bot.handleNextCommand("/PIRO_BC_Schedule_Time", options=True)
        
    except:
        bot.replyText(u, """<b>❌ Invalid date format!</b>

<b>Use:</b> DD-MM-YYYY
<b>Example:</b> 25-12-2025

<i>Please send date in correct format</i>""")
        raise ReturnCommand()


#======================================================================
# COMMAND: /PIRO_BC_Schedule_Execute
#======================================================================
# No admin check - runs automatically via Bot.runCommandAfter()

# Get task ID from options
task_id = options
task_data = Bot.getData(f"BC_Task_{task_id}") or {}

if not task_data:
    raise ReturnCommand()

# Get data from task
u = task_data.get("user")
bc_data = task_data.get("data", {})
date = task_data.get("date", "Unknown")
time = task_data.get("time", "Unknown")

channels = bc_data.get("channels", [])
txt = bc_data.get("text", "")
file_id = bc_data.get("file_id")
msg_type = bc_data.get("type", "text")

if not channels:
    bot.replyText(u, "<b>❌ No channels found!</b>")
    raise ReturnCommand()

# Send notification
bot.replyText(u, f"""<b>📢 Scheduled Broadcast Started!</b>

📆 <b>Scheduled:</b> {date} at {time}
📊 <b>Target:</b> {len(channels)} channels
📝 <b>Type:</b> {msg_type.upper()}

<i>⏳ Broadcasting in progress...</i>""")

# Get channel names for failed display
AMCU = Bot.getData("AllMainChUsernm") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCL = Bot.getData("AllMainChlink") or []

# Send to channels
success = 0
failed = 0
failed_list = []

for channel_id in channels:
    try:
        if msg_type == "text":
            bot.sendMessage(chat_id=str(channel_id), text=txt, parse_mode="html", disable_web_page_preview=True)
        elif msg_type == "photo":
            bot.sendPhoto(chat_id=str(channel_id), photo=file_id, caption=txt if txt else "", parse_mode="html")
        elif msg_type == "video":
            bot.sendVideo(chat_id=str(channel_id), video=file_id, caption=txt if txt else "", parse_mode="html")
        elif msg_type == "document":
            bot.sendDocument(chat_id=str(channel_id), document=file_id, caption=txt if txt else "", parse_mode="html")
        elif msg_type == "audio":
            bot.sendAudio(chat_id=str(channel_id), audio=file_id, caption=txt if txt else "", parse_mode="html")
        elif msg_type == "sticker":
            bot.sendSticker(chat_id=str(channel_id), sticker=file_id)
        elif msg_type == "animation":
            bot.sendAnimation(chat_id=str(channel_id), animation=file_id, caption=txt if txt else "", parse_mode="html")
        success += 1
    except:
        failed += 1
        # Get channel name
        ch_name = str(channel_id)
        ch_link = ""
        for i, ch_id in enumerate(AMCTGID):
            if str(ch_id) == str(channel_id):
                if i < len(AMCU):
                    ch_name = AMCU[i]
                if i < len(AMCL):
                    ch_link = AMCL[i]
                break
        failed_list.append({
            "name": ch_name,
            "link": ch_link
        })

# Generate EasyTime
now = libs.DateAndTime.now("Asia/Kolkata")
date_now = now["date"]  
time_now = now["time"][:5] 
year, month, day = date_now.split("-")
hour, minute = time_now.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

#


#======================================================================
# COMMAND: /PIRO_BC_Schedule_Message
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if options == None:
    date = Bot.getData("BC_Schedule_Date") or "DD-MM-YYYY"
    time_display = Bot.getData("BC_Schedule_Time_12hr") or "HH:MM AM/PM"
    msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast</b>

📆 <b>Date:</b> {date}
⏰ <b>Time:</b> {time_display}

<i>Now send your message (text/photo/video/document)</i>
<b>Send /cancel to cancel</b>""")
    Bot.saveData("BC_MsgID", msg.message_id)
    Bot.handleNextCommand("/PIRO_BC_Schedule_Message", options=True)
    raise ReturnCommand()
else:
    if message.text == "/cancel":
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            try:
                bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Schedule Cancelled</b>")
            except:
                pass
        Bot.saveData("BC_MsgID", None)
        Bot.saveData("BC_Schedule_Date", None)
        Bot.saveData("BC_Schedule_Time_12hr", None)
        Bot.saveData("BC_Schedule_Time_24hr", None)
        Bot.saveData("BC_Schedule_Hour", None)
        Bot.saveData("BC_Schedule_Minute", None)
        raise ReturnCommand()
    
    # Detect content type
    txt = message.caption if message.caption else message.text
    entities = message.caption_entities if message.caption else message.entities
    if entities:
        txt = apply_html_entities(txt, entities, {})
    
    # Get message type and file_id
    msg_type = "text"
    file_id = None
    
    if message.photo:
        msg_type = "photo"
        file_id = message.photo[-1].file_id
    elif message.video:
        msg_type = "video"
        file_id = message.video.file_id
    elif message.document:
        msg_type = "document"
        file_id = message.document.file_id
    elif message.audio:
        msg_type = "audio"
        file_id = message.audio.file_id
    elif message.sticker:
        msg_type = "sticker"
        file_id = message.sticker.file_id
    elif message.animation:
        msg_type = "animation"
        file_id = message.animation.file_id
    elif message.text:
        msg_type = "text"
    else:
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            try:
                bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Unsupported File Format!</b>")
            except:
                pass
        Bot.saveData("BC_MsgID", None)
        Bot.saveData("BC_Schedule_Date", None)
        Bot.saveData("BC_Schedule_Time_12hr", None)
        Bot.saveData("BC_Schedule_Time_24hr", None)
        Bot.saveData("BC_Schedule_Hour", None)
        Bot.saveData("BC_Schedule_Minute", None)
        raise ReturnCommand()
    
    # Save scheduled broadcast data
    broadcast_data = {
        "type": msg_type,
        "text": txt,
        "file_id": file_id,
        "channels": Bot.getData("AllMainChTGID") or []
    }
    Bot.saveData("BC_Data", broadcast_data)
    
    date = Bot.getData("BC_Schedule_Date")
    time_display = Bot.getData("BC_Schedule_Time_12hr")
    
    # Show confirmation
    msg_id = Bot.getData("BC_MsgID")
    preview = f"""<b>📅 Schedule Broadcast Confirmation</b>

📆 <b>Date:</b> {date}
⏰ <b>Time:</b> {time_display}
📊 <b>Target:</b> {len(broadcast_data['channels'])} channels
📝 <b>Type:</b> {msg_type.upper()}

🔄 <b>Content:</b>
{txt[:300] if txt else 'No text'}{'...' if txt and len(txt) > 300 else ''}

<i>✅ Click Confirm to schedule</i>
<i>❌ Click Cancel to abort</i>"""
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ Schedule", callback_data="/PIRO_BC_Schedule_Confirm"),
        InlineKeyboardButton("❌ Cancel", callback_data="/PIRO_BC_Cancel")
    )
    
    if msg_id:
        try:
            bot.editMessageText(chat_id=u, message_id=msg_id, text=preview, reply_markup=markup)
        except:
            new_msg = bot.replyText(u, preview, reply_markup=markup)
            Bot.saveData("BC_MsgID", new_msg.message_id)
    else:
        new_msg = bot.replyText(u, preview, reply_markup=markup)
        Bot.saveData("BC_MsgID", new_msg.message_id)


#======================================================================
# COMMAND: /PIRO_BC_Schedule_Time
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if options == None:
    date = Bot.getData("BC_Schedule_Date") or "DD-MM-YYYY"
    msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast</b>

📆 <b>Date:</b> {date}

<i>Send the time for broadcast</i>
<b>Format:</b> HH:MM AM/PM
<b>Examples:</b> 
• 02:30 PM (for 2:30 PM)
• 09:00 AM (for 9:00 AM)
• 12:00 PM (for 12:00 PM)
• 8:34 PM (for 8:34 PM)

<i>Send /cancel to cancel</i>""")
    Bot.saveData("BC_MsgID", msg.message_id)
    Bot.handleNextCommand("/PIRO_BC_Schedule_Time", options=True)
    raise ReturnCommand()
else:
    # This runs when user sends the time
    if message.text == "/cancel":
        msg_id = Bot.getData("BC_MsgID")
        if msg_id:
            try:
                bot.editMessageText(chat_id=u, message_id=msg_id, text="<b>❌ Schedule Cancelled</b>")
            except:
                pass
        Bot.saveData("BC_MsgID", None)
        Bot.saveData("BC_Schedule_Date", None)
        raise ReturnCommand()
    
    # Validate time format (HH:MM AM/PM or H:MM AM/PM)
    try:
        user_input = message.text
        
        # Check if message has AM/PM
        if "AM" not in user_input.upper() and "PM" not in user_input.upper():
            bot.replyText(u, """<b>❌ Invalid time format!</b>

<b>Use:</b> HH:MM AM/PM
<b>Examples:</b> 
• 02:30 PM (for 2:30 PM)
• 09:00 AM (for 9:00 AM)
• 12:00 PM (for 12:00 PM)
• 8:34 PM (for 8:34 PM)

<i>Please send time in correct format</i>""")
            raise ReturnCommand()
        
        # Split by space to get time and AM/PM
        parts = user_input.upper().split(" ")
        if len(parts) != 2:
            bot.replyText(u, """<b>❌ Invalid format!</b>
Please use format: HH:MM AM/PM
Example: 02:30 PM""")
            raise ReturnCommand()
        
        time_str = parts[0].strip()
        ampm_str = parts[1].strip()
        
        if ampm_str not in ["AM", "PM"]:
            bot.replyText(u, "<b>❌ Invalid AM/PM! Use AM or PM</b>")
            raise ReturnCommand()
        
        # Split time by colon
        time_components = time_str.split(":")
        if len(time_components) != 2:
            bot.replyText(u, "<b>❌ Invalid time format! Use HH:MM</b>")
            raise ReturnCommand()
        
        hour = int(time_components[0].strip())
        minute = int(time_components[1].strip())
        
        if hour < 1 or hour > 12:
            bot.replyText(u, "<b>❌ Hour must be between 1-12</b>")
            raise ReturnCommand()
        if minute < 0 or minute > 59:
            bot.replyText(u, "<b>❌ Minute must be between 0-59</b>")
            raise ReturnCommand()
        
        # Convert to 24-hour format for storage
        if ampm_str == "PM" and hour != 12:
            hour_24 = hour + 12
        elif ampm_str == "AM" and hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
        
        # Format the display time with leading zero if needed
        display_time = f"{hour:02d}:{minute:02d} {ampm_str}"
        
        # Store both formats
        Bot.saveData("BC_Schedule_Time_12hr", display_time)
        Bot.saveData("BC_Schedule_Time_24hr", f"{hour_24:02d}:{minute:02d}")
        Bot.saveData("BC_Schedule_Hour", hour_24)
        Bot.saveData("BC_Schedule_Minute", minute)
        
        # Check if time is in future (if date is today)
        date = Bot.getData("BC_Schedule_Date")
        now = libs.DateAndTime.now("Asia/Kolkata")
        current_date = now["date"]
        current_time = now["time"][:5]
        
        # Parse stored date (DD-MM-YYYY)
        date_parts = date.split("-")
        sched_day = int(date_parts[0])
        sched_month = int(date_parts[1])
        sched_year = int(date_parts[2])
        
        # Parse current date (YYYY-MM-DD)
        curr_parts = current_date.split("-")
        curr_year = int(curr_parts[0])
        curr_month = int(curr_parts[1])
        curr_day = int(curr_parts[2])
        
        # Check if scheduled date is today
        is_today = (sched_year == curr_year and sched_month == curr_month and sched_day == curr_day)
        
        if is_today:
            curr_hour = int(current_time.split(":")[0])
            curr_min = int(current_time.split(":")[1])
            
            if hour_24 < curr_hour or (hour_24 == curr_hour and minute <= curr_min):
                bot.replyText(u, f"""<b>❌ Please select a future time!</b>

⏰ <b>Current Time:</b> {current_time}
⏰ <b>You entered:</b> {display_time}

<i>Please enter a time after current time</i>""")
                raise ReturnCommand()
        
        # Ask for message
        date = Bot.getData("BC_Schedule_Date")
        time_display = Bot.getData("BC_Schedule_Time_12hr")
        
        msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast</b>

📆 <b>Date:</b> {date}
⏰ <b>Time:</b> {time_display}

<i>Now send your message (text/photo/video/document)</i>
<b>Send /cancel to cancel</b>""")
        
        Bot.saveData("BC_MsgID", msg.message_id)
        Bot.handleNextCommand("/PIRO_BC_Schedule_Message", options=True)
        
    except ValueError:
        bot.replyText(u, """<b>❌ Invalid time format!</b>

<b>Use:</b> HH:MM AM/PM
<b>Examples:</b> 
• 02:30 PM (for 2:30 PM)
• 09:00 AM (for 9:00 AM)
• 12:00 PM (for 12:00 PM)
• 8:34 PM (for 8:34 PM)

<i>Please send time in correct format</i>""")
        raise ReturnCommand()
    except:
        bot.replyText(u, """<b>❌ Invalid time format!</b>

<b>Use:</b> HH:MM AM/PM
<b>Examples:</b> 
• 02:30 PM (for 2:30 PM)
• 09:00 AM (for 9:00 AM)
• 12:00 PM (for 12:00 PM)
• 8:34 PM (for 8:34 PM)

<i>Please send time in correct format</i>""")
        raise ReturnCommand()


#======================================================================
# COMMAND: /PIRO_Broadcast
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Get all channels
AMCTGID = Bot.getData("AllMainChTGID") or []
if not AMCTGID:
    bot.replyText(u, "<b>❌ No Channels Added Yet!</b>")
    raise ReturnCommand()

# Ask for message
msg = bot.replyText(u, f"""<b>📢 Broadcast to {len(AMCTGID)} Channels</b>

<i>Send any message (text/photo/video/document)</i>
<b>Send /cancel to cancel</b>""")

Bot.saveData("BC_MsgID", msg.message_id)
Bot.handleNextCommand("/PIRO_BC_Process", options=True)


#======================================================================
# COMMAND: /PIRO_ChLinks
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

AMCL=Bot.getData("AllMainChlink") or []

Links=""
for L in AMCL:
    Links=f"{Links}\n{L}"

if Links!="":
    bot.sendMessage(Links)
else:
    bot.sendMessage("No Links Found")


#======================================================================
# COMMAND: /PIRO_Chanel_Pannel
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]
# Page-wise panel: next/prev nav + auto-add-to-current-page

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


OWNER=Bot.getData("Owner") or "1294066842"

AMC = Bot.getData("AllMainCh") or []
AMCL=Bot.getData("AllMainChlink") or []
AMCU=Bot.getData("AllMainChUsernm") or []
AMCTGID=Bot.getData("AllMainChTGID") or []

AMCP=Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)

# Self-heal any array-length drift so a bad delete/add can never crash the panel
for _pad in range(len(AMCTGID) - len(AMC)):
    AMC.append("Unknown")
for _pad in range(len(AMCTGID) - len(AMCU)):
    AMCU.append("Unknown")
for _pad in range(len(AMCTGID) - len(AMCL)):
    AMCL.append("https://t.me/" + str(AMCTGID[len(AMCL)]))

StoredPageCount = Bot.getData("AllMainChPageCount") or 1
MaxChPage = max(AMCP) if AMCTGID else 1
TotalPages = max(int(StoredPageCount), int(MaxChPage), 1)

AdminCurPage = User.getData("PIRO_AdminCurPage")
if AdminCurPage is None:
    AdminCurPage = 1
else:
    AdminCurPage = int(AdminCurPage)
if AdminCurPage < 1:
    AdminCurPage = 1
if AdminCurPage > TotalPages:
    AdminCurPage = TotalPages


now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []


if str(params) != "None":
    P = str(params).split(" ")

    if P[0] == "page":
        if P[1] == "next":
            AdminCurPage = min(AdminCurPage + 1, TotalPages)
        elif P[1] == "prev":
            AdminCurPage = max(AdminCurPage - 1, 1)
        elif P[1] == "addnew":
            TotalPages = TotalPages + 1
            Bot.saveData("AllMainChPageCount", TotalPages)
            AdminCurPage = TotalPages
        User.saveData("PIRO_AdminCurPage", AdminCurPage)

    if P[0] == "DelSocial":
        SocialLinks = Bot.getData("AllSocialLinks") or []

        try:
            ind = int(P[1])
            SocialLinks.pop(ind)
            Bot.saveData("AllSocialLinks", SocialLinks)
        except:
            pass

    MMM = InlineKeyboardMarkup()
    MMM.add(
        InlineKeyboardButton(
            text='🟢CHECK',
            callback_data=f'/JoinReqSt {P[1]} Y'
        ),
        InlineKeyboardButton(
            text='🔴NO CHECK',
            callback_data=f'/JoinReqSt {P[1]} N'
        )
    )

    DC = Bot.getData(str(P[1]) + "isDef") or "N"

    if P[0]=="setLink":
        
        if DC=="Y" and str(u)!=OWNER:
            bot.replyText(u,"<b>😖This is a Permanent Channel</b>")
            raise ReturnCommand()
        
        bot.replyText(u,"<b>Send Invite Link For Channel\n\nSend /cancel To Cancel\n\nYou Can Also Send Public Channel Link (t.me) Here To Reset If You Have Done Wrong</b>")
        Bot.handleNextCommand("/PIRO_Chanel_Pannel1",options=str(P[1])) 
        raise ReturnCommand()

    if P[0]=="setPage":
        bot.replyText(u,"<b>📄 Send the new page number for this channel (e.g. 1, 2, 3)\n\nSend /cancel To Cancel</b>")
        Bot.handleNextCommand("/PIRO_Chanel_PannelSetPage",options=str(P[1]))
        raise ReturnCommand()

    if P[0]=="delete":
        if DC=="Y" and str(u)!=OWNER:
            bot.replyText(u,"<b>😖This is a Permanent Channel</b>")
            raise ReturnCommand()
        
        try:
            IND=AMCTGID.index(int(P[1]))
        except:
            IND=AMCTGID.index(str(P[1]))
        
        try:
            AMCTGID.pop(IND)
            AMCU.pop(IND)
            AMCL.pop(IND)
            AMC.pop(IND)
            try:
                AMCP.pop(IND)
            except:
                pass
        except:
            pass
        
        act=f"Channel ({P[1]}) Removed "
        AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")
        Bot.saveData("AdmAC",AdmAC)
        
        
        bot.replyText(u,"<b>Channel Removed Successfully</b>")
        
        
    if P[0]=="UP":
        try:
            IND=AMCTGID.index(int(P[1]))
        except:
            IND=AMCTGID.index(str(P[1]))
        
        ThisPg = AMCP[IND]
        SwapIdx = None
        for j in range(IND - 1, -1, -1):
            if AMCP[j] == ThisPg:
                SwapIdx = j
                break
        
        if SwapIdx is not None:
            t=AMCTGID[IND]; AMCTGID[IND]=AMCTGID[SwapIdx]; AMCTGID[SwapIdx]=t
            t=AMCU[IND]; AMCU[IND]=AMCU[SwapIdx]; AMCU[SwapIdx]=t
            t=AMCL[IND]; AMCL[IND]=AMCL[SwapIdx]; AMCL[SwapIdx]=t
            t=AMC[IND]; AMC[IND]=AMC[SwapIdx]; AMC[SwapIdx]=t
        
    if P[0]=="DOWN":
        try:
            IND=AMCTGID.index(int(P[1]))
        except:
            IND=AMCTGID.index(str(P[1]))
        
        ThisPg = AMCP[IND]
        SwapIdx = None
        for j in range(IND + 1, len(AMCTGID)):
            if AMCP[j] == ThisPg:
                SwapIdx = j
                break
        
        if SwapIdx is not None:
            t=AMCTGID[IND]; AMCTGID[IND]=AMCTGID[SwapIdx]; AMCTGID[SwapIdx]=t
            t=AMCU[IND]; AMCU[IND]=AMCU[SwapIdx]; AMCU[SwapIdx]=t
            t=AMCL[IND]; AMCL[IND]=AMCL[SwapIdx]; AMCL[SwapIdx]=t
            t=AMC[IND]; AMC[IND]=AMC[SwapIdx]; AMC[SwapIdx]=t
    
    if P[0]=="info":
       
        try:
            IND=AMCTGID.index(int(P[1]))
        except:
            IND=AMCTGID.index(str(P[1]))
        
        L=AMCL[IND]
        if str(L)=="https://t.me/"+str(AMCTGID[IND]):
            L=" none "
        
        if DC=="Y":
            bot.replyText(u, f"<b>💡Channel Info\n\n🆔Chat ID/Chat Username :- {AMCU[IND]}\n📄Page :- {AMCP[IND]}\n🖇Private Chat Link :- {L}</b>", disable_web_page_preview=True,reply_markup=MMM)
        else:
            bot.replyText(u, f"<b>💡Channel Info\n\n🆔Chat ID/Chat Username :- {AMCU[IND]}\n📄Page :- {AMCP[IND]}\n🖇Private Chat Link :- {L}</b>", disable_web_page_preview=True)
            
        raise ReturnCommand()


    Bot.saveData("AllMainCh",AMC) 
    Bot.saveData("AllMainChlink",AMCL) 
    Bot.saveData("AllMainChUsernm",AMCU) 
    Bot.saveData("AllMainChTGID",AMCTGID) 
    Bot.saveData("AllMainChPage",AMCP) 


# Save which page admin is currently viewing (so newly added channels attach here)
User.saveData("PIRO_AdminCurPage", AdminCurPage)

keyboard = []
IND=0
for ch_tgid in AMCTGID:
    if AMCP[IND] != AdminCurPage:
        IND = IND + 1
        continue
    
    ch=str(AMCU[IND]) 
    
    keyboard.append([
    {"text": ch, "callback_data": "/PIRO_Chanel_Pannel setLink "+str(ch_tgid)},
    {"text": "❌", "callback_data": "/PIRO_Chanel_Pannel delete "+str(ch_tgid)},
    {"text": "🔼", "callback_data": "/PIRO_Chanel_Pannel UP "+str(ch_tgid)},
    {"text": "🔽", "callback_data": "/PIRO_Chanel_Pannel DOWN "+str(ch_tgid)},
    {"text": "👀", "callback_data": "/PIRO_Chanel_Pannel info "+str(ch_tgid)}])

    IND=IND+1

# Page navigation row
NavRow = []
if AdminCurPage > 1:
    NavRow.append({"text": "◀ Prev", "callback_data": "/PIRO_Chanel_Pannel page prev"})
else:
    NavRow.append({"text": "▪️", "callback_data": "/PIRO_Chanel_Pannel noop"})

NavRow.append({"text": f"📄 Page {AdminCurPage}/{TotalPages}", "callback_data": "/PIRO_Chanel_Pannel noop"})

if AdminCurPage < TotalPages:
    NavRow.append({"text": "Next ▶", "callback_data": "/PIRO_Chanel_Pannel page next"})
else:
    NavRow.append({"text": "➕ New Page", "callback_data": "/PIRO_Chanel_Pannel page addnew"})

keyboard.append(NavRow)

keyboard.append([{"text": f"➕Add Channel To Page {AdminCurPage}", "callback_data": "/PIRO_AddCh"}])

keyboard.append([
    {"text": "✏️ Edit Join Message", "callback_data": "/PIRO_SetJoinMsg"}
])
keyboard.append([
    {"text": "✏️ Edit Extra Message (below join)", "callback_data": "/PIRO_SetJoinMsg2"}
])
keyboard.append([
    {"text": "🔘 Join Button (Text + Emoji)", "callback_data": "/PIRO_SetJoinBtnTxt"}
])
keyboard.append([
    {"text": "🔘 Claim Button (Text + Emoji)", "callback_data": "/PIRO_SetClaimBtnTxt"}
])

keyboard.append([{"text": "📡 Channel Broadcast", "callback_data": "/CHANNEL_BC"}])

keyboard.append([
    {"text": "➕ Add Social Link", "callback_data": "/social"}
])

SocialLinks = Bot.getData("AllSocialLinks") or []

for i, item in enumerate(SocialLinks):
    keyboard.append([
        {"text": "🌐 " + item["name"], "url": item["url"]},
        {"text": "❌", "callback_data": "/PIRO_Chanel_Pannel DelSocial " + str(i)}
    ])

keyboard.append([{"text": "🔙Back", "callback_data": "/admin AP"}])


TXT=f"""<b>Here You Can Manage Your Channels\n\nViewing Page {AdminCurPage} of {TotalPages}. Use ◀ Prev / Next ▶ to switch pages.\nAny channel you add now will be added to Page {AdminCurPage}.\nClick a channel name to set its invite link.</b>"""


try:
    bot.editMessageText(chat_id=u, message_id=message.message_id,text=TXT,reply_markup={"inline_keyboard": keyboard})
except:
    try:
        bot.sendMessage(TXT, reply_markup={"inline_keyboard": keyboard})
    except:
        pass


#======================================================================
# COMMAND: /PIRO_Chanel_Pannel1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()



if str(message.text)=="/cancel":
    bot.sendMessage("canceled")
    raise ReturnCommand()
    
    
AMC = Bot.getData("AllMainCh") or []
AMCL=Bot.getData("AllMainChlink") or []
AMCU=Bot.getData("AllMainChUsernm") or []

AMCTGID=Bot.getData("AllMainChTGID") or []
        

try:
    IND=AMCTGID.index(int(options))
except:
    IND=AMCTGID.index(str(options))
    
      
   
   
   
 
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []

act=f"Invite Link ({AMCL[IND]}) changed to ({message.text}) in Bot Channel ({AMCTGID[IND]})"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

Bot.saveData("AdmAC",AdmAC)
  
   
   
   
   
   
   
   
AMCL[IND]=str(message.text) 
Bot.saveData("AllMainChlink",AMCL) 
    
   
bot.replyText(u, f"<b> Invite Link Updated for {AMCU[IND]} {AMCTGID[IND]} </b>", disable_web_page_preview=True)

Bot.runCommand("/PIRO_Chanel_Pannel")


#======================================================================
# COMMAND: /PIRO_Chanel_PannelSetPage
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if str(message.text) == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

PageTxt = str(message.text).strip()
if not PageTxt.isdigit() or int(PageTxt) < 1:
    bot.sendMessage("<b>⚠️ Please send a valid whole number page (1 or more). Try again, or /cancel:</b>")
    Bot.handleNextCommand("/PIRO_Chanel_PannelSetPage")
    raise ReturnCommand()

PageNum = int(PageTxt)

User.saveData("PIRO_AdmViewPage", PageNum)

bot.replyText(u, f"<b>✅ Now Viewing Page {PageNum}</b>")
Bot.runCommand("/PIRO_Chanel_Pannel")


#======================================================================
# COMMAND: /PIRO_DebugPages
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 Not Admin</b>")
    raise ReturnCommand()

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCP = Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)

Lines = [f"Total channels: {len(AMCTGID)}"]
IND = 0
for i in AMCTGID:
    try:
        UC = bot.getChatMember(i, u).status
    except Exception as e:
        UC = f"error:{str(e)[:60]}"
    Lines.append(f"{IND}: id={i} ({type(i).__name__}) user={AMCU[IND] if IND<len(AMCU) else '?'} page={AMCP[IND]} my_status={UC}")
    IND += 1

bot.sendMessage("<pre>" + "\n".join(Lines) + "</pre>")


#======================================================================
# COMMAND: /PIRO_JoinGate
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_PIN = "6129434968713076807"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_HEART = "5388790256772331442"
# Shared page-wise join gate (FAST: cached 1 minute; old join message only deleted on Joined tap).
# Caller stores the target command in User data "PIRO_GateTarget".

if message.chat.type != "private":
    raise ReturnCommand()

Target = User.getData("PIRO_GateTarget") or "/PIRO_MainMenu"

usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

BotAdmins = Bot.getData("AllBotAdminss") or []
BOTID = int(Bot.info().token.split(":")[0])

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCO = Bot.getData("AllMainChOptional") or []
AMCP = Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)
for _pad in range(len(AMCTGID) - len(AMCU)):
    AMCU.append("Unknown")
for _pad in range(len(AMCTGID) - len(AMCL)):
    AMCL.append("https://t.me/" + str(AMCTGID[len(AMCL)]))

ALL_PAGES = sorted(set(AMCP)) if AMCTGID else []
CurPage = ALL_PAGES[0] if ALL_PAGES else 1

# ---- verified-channel cache (valid for the current MINUTE only) ----
_now = libs.DateAndTime.now("Asia/Kolkata")
Stamp = str(_now["date"]) + " " + str(_now["time"])[:5]
OKids = []
try:
    _c = User.getData("PIRO_OK")
    if _c and _c.get("s") == Stamp:
        OKids = list(_c.get("ids") or [])
except:
    OKids = []

joinSTAT = "JOIND"
PIRO_NJCL = []
FoundIdx = None
CacheDirty = False

for PageIdx in range(0, len(ALL_PAGES)):
    ThisPage = ALL_PAGES[PageIdx]
    NotJoinedThisPage = []

    IND = 0
    for i in AMCTGID:
        if AMCP[IND] != ThisPage:
            IND += 1
            continue

        sid = str(i)
        if sid in OKids:
            IND += 1
            continue

        UC = "error"
        ERR = ""
        try:
            UC = bot.getChatMember(i, u).status
        except Exception as e:
            UC = "error"
            ERR = str(e)[:150]

        if UC == "member" or UC == "administrator" or UC == "creator":
            OKids.append(sid)
            CacheDirty = True

        elif UC == "left" or UC == "kicked":
            ReqRec = Bot.getData(sid + "JoinRRof" + str(u)) or "N"
            JR = Bot.getData(sid + "JoinReq") or "Y"
            if ReqRec != "Y" and JR == "Y" and (not AMCO or IND >= len(AMCO) or AMCO[IND] != "O"):
                NotJoinedThisPage.append(sid)

        elif UC == "error":
            BotIsAdm = False
            try:
                BS = bot.getChatMember(i, BOTID).status
                if BS == "administrator" or BS == "creator":
                    BotIsAdm = True
            except:
                BotIsAdm = False

            if not BotIsAdm:
                if Bot.getData("PIRO_NAsent" + sid) != "Y":
                    Bot.saveData("PIRO_NAsent" + sid, "Y")
                    for admin in BotAdmins:
                        try:
                            bot.replyText(admin, f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️\n\n✨ Only admins see this reminder (sent once per channel). 😊</b>")
                        except:
                            pass
            else:
                Bot.deleteData("PIRO_NAsent" + sid)
                if Bot.getData("PIRO_ERRsent" + sid) != "Y":
                    Bot.saveData("PIRO_ERRsent" + sid, "Y")
                    for admin in BotAdmins:
                        try:
                            bot.replyText(admin, f"<b>ℹ️ Bot IS admin in {AMCU[IND]}, but a member check failed:</b>\n<code>{ERR}</code>\n<i>(sent once per channel, only admins see this)</i>")
                        except:
                            pass

        IND += 1

    if NotJoinedThisPage:
        joinSTAT = "NOTJOIN"
        PIRO_NJCL = NotJoinedThisPage
        FoundIdx = PageIdx
        break

if CacheDirty:
    User.saveData("PIRO_OK", {"s": Stamp, "ids": OKids})

if FoundIdx is not None:
    CurPage = ALL_PAGES[FoundIdx]
elif ALL_PAGES:
    CurPage = ALL_PAGES[-1]

User.saveData("PIRO_CurPage", CurPage)
User.saveData("PIRO_NJCL", PIRO_NJCL)

if joinSTAT == "JOIND":
    Bot.runCommand(Target)
    raise ReturnCommand()

# NOTE: old join message is intentionally NOT deleted here anymore.
# It is only deleted when the user actually taps the Joined button (faster gate).

JoinBtnText = Bot.getData("PIRO_JoinBtnText") or "Join"
ClaimBtnText = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
JoinIcon = Bot.getData("PIRO_JoinBtnEmojiId")
ClaimIcon = Bot.getData("PIRO_ClaimBtnEmojiId")

keyboard = []
row = []
IND = 0
for i in AMCTGID:
    if str(i) in PIRO_NJCL:
        btn = {"text": JoinBtnText, "url": AMCL[IND], "style": "primary"}
        if JoinIcon:
            btn["icon_custom_emoji_id"] = JoinIcon
        row.append(btn)
        if len(row) == 2:
            keyboard.append(row)
            row = []
    IND += 1
if row:
    keyboard.append(row)

SocialLinks = Bot.getData("AllSocialLinks") or []
if SocialLinks:
    row = []
    for s in SocialLinks:
        row.append({"text": f"{s['name']}", "url": s['url'], "style": "primary"})
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

cbtn = {"text": ClaimBtnText, "callback_data": "🟢 Joined", "style": "success"}
if ClaimIcon:
    cbtn["icon_custom_emoji_id"] = ClaimIcon
keyboard.append([cbtn])

JoinMsgChatId = Bot.getData("PIRO_JoinMsgChatId")
JoinMsgId = Bot.getData("PIRO_JoinMsgId")

SentOk = False
if JoinMsgChatId and JoinMsgId:
    try:
        Sent = bot.copyMessage(chat_id=u, from_chat_id=JoinMsgChatId, message_id=JoinMsgId, reply_markup={"inline_keyboard": keyboard})
        try:
            Mid = Sent.message_id
        except:
            Mid = Sent["message_id"]
        User.saveData("PIRO_ltmg", Mid)
        SentOk = True
    except:
        SentOk = False

if not SentOk:
    msg = bot.sendMessage(
    f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""",
        reply_markup={"inline_keyboard": keyboard},
        disable_web_page_preview=True
    )
    User.saveData("PIRO_ltmg", msg["message_id"])

Ex1 = Bot.getData("PIRO_JoinMsg2ChatId")
Ex2 = Bot.getData("PIRO_JoinMsg2Id")
if Ex1 and Ex2:
    try:
        S2 = bot.copyMessage(chat_id=u, from_chat_id=Ex1, message_id=Ex2)
        try:
            M2 = S2.message_id
        except:
            M2 = S2["message_id"]
        User.saveData("PIRO_ltmg2", M2)
    except:
        pass


#======================================================================
# COMMAND: /PIRO_LeadSet
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()



markup = InlineKeyboardMarkup()

markup.add(InlineKeyboardButton(text='Leaderboard Text',callback_data='/PIRO_LeadSet Text'))

markup.add(InlineKeyboardButton(text='Ban From Leaderboard',callback_data='/PIRO_LeadSet Ban'))

markup.add(InlineKeyboardButton(text='UnBan From Leaderboard',callback_data='/PIRO_LeadSet UnBan'))


markup.add(InlineKeyboardButton(text='Leaderboard Size',callback_data='/PIRO_LeadSet Size'))

markup.add(InlineKeyboardButton(text='🔙Back',callback_data='/admin AP'))


if str(params) !="None":
    P=params.split(" ")
    if P[0]=="Text":
        bot.replyText(u,f"""<b>Send New Leaderboard Text</b>""",parse_mode = "html")
        
    if P[0]=="Ban":
        bot.replyText(u,f"""<b>Send UserId to Ban From Leaderboard</b>""",parse_mode = "html")
        
    if P[0]=="UnBan":
        bot.replyText(u,f"""<b>Send UserId to UnBan From Leaderboard</b>""",parse_mode = "html")
        
    if P[0]=="Size":
        bot.replyText(u,f"""<b>Send The Numbers Of Winners to Show In Leaderboard</b>""",parse_mode = "html")
        
    Bot.handleNextCommand("/PIRO_LeadSet1",options=P[0])
    raise ReturnCommand()



TXT=f"""<b>Here You Can Modify Leaderboard Specifications </b>"""

try:
    bot.editMessageText(chat_id=u, message_id=message.message_id,text=TXT,reply_markup=markup)
except:
    pass


#======================================================================
# COMMAND: /PIRO_LeadSet1
#======================================================================
op=options

if message.text == "Cancel":
    raise ReturnCommand()
    


now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []



 





if op=="Text":
    bot.replyText(u,f"""<b>Leaderboard has been changed</b>""",parse_mode = "html")
    Bot.saveData("LdrbrdTxt",message.text)
    
    act=f"Leaderboard Text updated to {message.text}"
    AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

    Bot.saveData("AdmAC",AdmAC)
    raise ReturnCommand()

if op=="Ban":
    bot.replyText(u,f"""<b>{message.text} Banned From Leaderboard</b>""",parse_mode = "html")
    Bot.saveData("LdrbrdBanUsr",message.text)
    
    act=f"Banned {message.text} from Leaderboard"
    AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

    Bot.saveData("AdmAC",AdmAC)
    raise ReturnCommand()

if op=="UnBan":
    bot.replyText(u,f"""<b>{message.text} Unbanned From Leaderboard</b>""",parse_mode = "html")
    Bot.deleteData("LdrbrdBanUsr")
    act=f"UnBanned {message.text} from Leaderboard"
    AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

    Bot.saveData("AdmAC",AdmAC)    
    raise ReturnCommand()

if op=="Size":
    bot.replyText(u,f"""<b>Leaderboard Size Changed to {message.text}</b>""",parse_mode = "html")
    Bot.saveData("LdrbrdSize",message.text)
    act=f"Leaderboard Size Updated To {message.text} "
    AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

    Bot.saveData("AdmAC",AdmAC)
    raise ReturnCommand()


#======================================================================
# COMMAND: /PIRO_MainMenu
#======================================================================
EMOJI_PARTY = "6224161941305169199"
EMOJI_STAR = "5469741319330996757"
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5193085063998224234"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_PAISA = "6287207173537666597"
EMOJI_CLOCK = "6231214251835397322"
EMOJI_POTL = "5375296873982604963"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CROWN = "4956420911310832630"
EMOJI_POTLI = "6278489025581944577"
EMOJI_MST = "6278337731063975777"
EMOJI_BANK = "5332455502917949981"


# --- Referral & First-time check ---
dn = User.getData("dn") or "n"
if dn == "n":
    refBy = Bot.getData(str(u) + "Referral") or "None"
    RefJC = Bot.getData(str(refBy) + "RefJC") or 0
    Bot.saveData(str(refBy) + "RefJC", RefJC + 1)
    User.saveData("dn", "y")
# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShown") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/claimvoucher"
    )

    if AdResult:
        User.saveData("TBC_AdShown", "Y")
        raise ReturnCommand()
# ============================================================
# 📱 CONTACT VERIFICATION FIRST
# ============================================================

VerifySystemStatus = Bot.getData(
    "VerifySystemStatus"
) or "OFF"


if VerifySystemStatus == "ON":

    if not User.getData("is_verified"):

        Bot.runCommand(
            "/shareprofile"
        )

        raise ReturnCommand()


# ============================================================
# 🔐 CAPTCHA + MANUAL APPROVAL VERIFICATION
# ============================================================

iisApproved = Bot.getData(
    str(u) + "ManualAproval"
) or "N"

UsrPhVerif = User.getData(
    "PhVerification"
)


Captcha = Bot.getData(
    "CaptchaMode"
) or "ON"


verify = User.getData(
    "verify"
)


if Captcha == "ON":

    if verify != "ok":

        # ✅ Phone verified OR manually approved = allow
        if UsrPhVerif == "Verified" or iisApproved == "Y":
            pass

        else:
            Bot.runCommand(
                "/PIRO_Verification"
            )

            raise ReturnCommand()
# --- Menu Function ---
def PIRO_Menu():
    # --- Get saved link ---
    saved_link = Bot.getData("SavedLinks")

    # --- Get owner ID (save once with: Bot.saveData("Owner", 123456789)) ---
    owner_id = Bot.getData("Owner")

    # --- Decide final link ---
    if saved_link:
        final_link = saved_link
    elif owner_id:
        final_link = f"tg://openmessage?user_id={owner_id}"
    else:
        final_link = "https://t.me/"   # fallback if nothing set

    # --- Welcome text ---
    HHT = (
        f'<tg-emoji emoji-id="{EMOJI_STAR
        }">🏡</tg-emoji><b>Welcome To Refer Earn Bot!</b>\n\n'
        f"<b>How to Earn → </b> <b><a href='{final_link}'>[ CLICK HERE ]</a></b>")
        
    if options:   # override if a custom message is passed
        HHT = options

    # --- Keyboard menu ---
    keyboard = {
    "keyboard": [
        [
            {
                "text": "Balance",
                "icon_custom_emoji_id": EMOJI_POTL
            },
            {
                "text": "Refer Earn",
                "icon_custom_emoji_id": EMOJI_TIE
            }
        ],
        [
            {
                "text": "Bonus",
                "icon_custom_emoji_id": EMOJI_GIFT
            },
            {
                "text": "Withdraw",
                "icon_custom_emoji_id": EMOJI_MST
            }
        ],
        [
            {
                "text": "Payout Method",
                "icon_custom_emoji_id": EMOJI_BANK
            }
        ]
    ],
    "resize_keyboard": True
}
    bot.sendMessage(
        HHT,
        chat_id=message.chat.id,
        reply_markup=keyboard,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShown") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/start"
    )

    if AdResult:
        User.saveData("TBC_AdShown", "Y")
        raise ReturnCommand()
# --- Show Menu ---
PIRO_Menu()

# --- Referral Logic ---
is_invited = User.getData("is_invited")
ref = Bot.getData(str(u) + "Referral") or "None"
perRef = Bot.getData("PerRefer") or "0"   # string format support

if is_invited is None:
    if ref != "None":
        sameDev = Bot.getData(str(u) + "sameDev") or "no"
        if sameDev == "no":
            RefCount = Bot.getData(str(ref) + "RefCount") or 0
            Bot.saveData(str(ref) + "RefCount", int(RefCount + 1))

            usr = f"""<a href="tg://user?id={str(u)}">{str(u)}</a>"""

            # --- Decide Referral Bonus ---
            bonus = 0
            if "-" in str(perRef):
                try:
                    start, end = map(int, perRef.split("-"))
                    # ✅ Built-in random (no import)
                    bonus = libs.Random.randomInt(start,end)
                except:
                    bonus = 0
            else:
                try:
                    bonus = int(perRef)
                except:
                    bonus = 0

            # --- Add bonus to referrer ---
            if bonus > -1:
                libs.Resources.anotherRes('Balance', user=ref).add(bonus)
                try:
                    bot.replyText(
                        chat_id=ref,
                        text=f"""<tg-emoji emoji-id="{EMOJI_PARTY}">🤑</tg-emoji><b>{usr} Got Invited By Your Url: +{bonus} Rs </b>""",
                        parse_mode="HTML"
                    )
                except:
                    pass

    # --- Count verified users ---
    T_verifUsrs = Bot.getData('T_verifUsrs') or 0
    Bot.saveData('T_verifUsrs', T_verifUsrs + 1)

    User.saveData("is_invited", True)


#======================================================================
# COMMAND: /PIRO_PayoutMenu
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_DOWN = "5470177992950946662"
EMOJI_TI = "5375152498656961898"

# ----------- WALLET / UPI MENU (opened only after the join gate passes) -----------
# coded by @Jenish_Dobariya1

wallet = Bot.getData("UserWallet" + str(u)) or "Not Linked"
upi = Bot.getData("UserUPI" + str(u)) or "Not Linked"

WalletStatus = Bot.getData("WalletWithdraw") or "ON"
UpiStatus = Bot.getData("UpiWithdraw") or "ON"

if WalletStatus == "OFF" and UpiStatus == "OFF":
    bot.replyText(u, f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji>All Withdrawal Methods Are Currently Disabled</b>')
    raise ReturnCommand()

text = f'<b><tg-emoji emoji-id="{EMOJI_TI}">💳</tg-emoji> Choose Desired Payment Method From Below <tg-emoji emoji-id="{EMOJI_DOWN}">👇</tg-emoji>\n\n'
buttons = []
row = []

if WalletStatus == "ON":
    text += f"Your Current Wallet - <code>{wallet}</code>\n"
    row.append({"text": "Link Wallet", "callback_data": "Link Wallet"})

if UpiStatus == "ON":
    text += f"Your Current UPI - <code>{upi}</code>\n"
    row.append({"text": "Link UPI", "callback_data": "link_upi"})

text += "</b>"
if row:
    buttons.append(row)

bot.replyText(
    u,
    text,
    parse_mode="html",
    reply_markup={"inline_keyboard": buttons}
)


#======================================================================
# COMMAND: /PIRO_RC_Pannel
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(userid) for userid in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GIFT CODES
# ==============================

All_BRC = Bot.getData("All_BRC") or []

All_BRC = [str(RC) for RC in All_BRC]

markup = InlineKeyboardMarkup()


# ==============================
# NO GIFT CODES
# ==============================

if not All_BRC:

    markup.add(
        InlineKeyboardButton(
            text="➕ Cʀᴇᴀᴛᴇ Nᴇᴡ Gɪғᴛ Cᴏᴅᴇ",
            callback_data="/creating_NwRC"
        )
    )

else:

    # ==============================
    # GIFT CODE LIST
    # ==============================

    for RC in All_BRC:

        Status = Bot.getData(
            "Gift" + RC + "KaStatus"
        ) or "Active"

        StatusEmoji = "🟢" if Status == "Active" else "🔴"


        markup.row(
            InlineKeyboardButton(
                text=RC,
                callback_data="/RC_Change info_" + RC
            ),

            InlineKeyboardButton(
                text="🗑",
                callback_data="/RC_Change delete_" + RC
            ),

            InlineKeyboardButton(
                text=StatusEmoji,
                callback_data="/RC_Change " + StatusEmoji + "_" + RC
            )
        )


    # ==============================
    # CREATE NEW
    # ==============================

    markup.add(
        InlineKeyboardButton(
            text="➕ Cʀᴇᴀᴛᴇ Nᴇᴡ",
            callback_data="/creating_NwRC"
        )
    )


# ==============================
# CLAIMED TEXT
# ==============================

markup.add(
    InlineKeyboardButton(
        text="📝 Cʟᴀɪᴍᴇᴅ Tᴇxᴛ",
        callback_data="/RC_claimedText"
    )
)


# ==============================
# BACK
# ==============================

markup.add(
    InlineKeyboardButton(
        text="🔙 Bᴀᴄᴋ",
        callback_data="/admin AP"
    )
)


# ==============================
# PANEL TEXT
# ==============================

TXT = f"""<b>🎁 Gɪғᴛ Cᴏᴅᴇ Mᴀɴᴀɢᴇʀ

📊 Tᴏᴛᴀʟ Gɪғᴛ Cᴏᴅᴇs: {len(All_BRC)}

👇 Sᴇʟᴇᴄᴛ A Gɪғᴛ Cᴏᴅᴇ Tᴏ Mᴀɴᴀɢᴇ Iᴛ.</b>"""


# ==============================
# EDIT CURRENT MESSAGE
# ==============================

try:

    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

except:

    bot.replyText(
        u,
        TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )


raise ReturnCommand()


#======================================================================
# COMMAND: /PIRO_ResetMe
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

# Forget that this account is a "returning" user, so /start treats you as brand new again
Bot.deleteData("UserID" + str(u))
User.deleteData("bot_user")
Bot.deleteData(str(u) + "Referral")

FulUsrs = Bot.getData("FulBotUsrs") or []
if u in FulUsrs:
    FulUsrs.remove(u)
    Bot.saveData("FulBotUsrs", FulUsrs)

T_usrs = Bot.getData("total_users")
if T_usrs:
    Bot.saveData("total_users", max(0, int(T_usrs) - 1))

# Also clear your own channel-join test state so /start re-checks everything fresh
User.deleteData("PIRO_CurPage")
User.deleteData("PIRO_OK")
User.deleteData("PIRO_NJCL")
User.deleteData("PIRO_ltmg")
User.deleteData("PIRO_ltmg2")

bot.replyText(u, "<b>♻️ Your account has been reset. Send /start now — it will behave like your very first time (new-user notification + channel-join flow both fresh).</b>")


#======================================================================
# COMMAND: /PIRO_ScheduleBroadcast
#======================================================================
# Admin Check
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

AMCTGID = Bot.getData("AllMainChTGID") or []
if not AMCTGID:
    bot.replyText(u, "<b>❌ No Channels Added Yet!</b>")
    raise ReturnCommand()

# Ask for date
msg = bot.replyText(u, f"""<b>📅 Schedule Broadcast to {len(AMCTGID)} Channels</b>

<i>Send the date for broadcast</i>
<b>Format:</b> DD-MM-YYYY
<b>Example:</b> 25-12-2025

<i>Send /cancel to cancel</i>""")

Bot.saveData("BC_MsgID", msg.message_id)
Bot.handleNextCommand("/PIRO_BC_Schedule_Date", options=True)


#======================================================================
# COMMAND: /PIRO_SetClaimBtnEmoji
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

CurId = Bot.getData("PIRO_ClaimBtnEmojiId")

bot.replyText(
    u,
    f"<b>🎭 Current Claim button icon_custom_emoji_id:</b> {CurId or 'not set'}\n\n"
    "<b>Send a message containing ONLY the custom/premium emoji you want as the Claim button's icon "
    "(paste it from Telegram's premium emoji picker). Send /cancel to cancel, /reset_default to remove it.</b>"
)
Bot.handleNextCommand("/PIRO_SetClaimBtnEmojiSave")


#======================================================================
# COMMAND: /PIRO_SetClaimBtnEmojiSave
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

Txt = str(message.text or "").strip()

if Txt == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if Txt == "/reset_default":
    Bot.deleteData("PIRO_ClaimBtnEmojiId")
    bot.sendMessage("<b>♻️ Claim button icon removed.</b>")
    raise ReturnCommand()

FoundId = None
Ents = message.entities or []
for e in Ents:
    if e.type == "custom_emoji":
        FoundId = e.custom_emoji_id
        break

if not FoundId:
    bot.sendMessage("<b>⚠️ I couldn't find a custom/premium emoji in that message. Make sure you pasted an actual premium emoji (not a regular one), then try again, or /cancel.</b>")
    Bot.handleNextCommand("/PIRO_SetClaimBtnEmojiSave")
    raise ReturnCommand()

Bot.saveData("PIRO_ClaimBtnEmojiId", str(FoundId))
bot.sendMessage(f"<b>✅ Claim button icon_custom_emoji_id saved: {FoundId}</b>")


#======================================================================
# COMMAND: /PIRO_SetClaimBtnTxt
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

CurClaim = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
CurIcon = Bot.getData("PIRO_ClaimBtnEmojiId") or "none"

bot.replyText(
    u,
    f"<b>🔘 Current Claim button:</b> {CurClaim}  (icon id: {CurIcon})\n\n"
    "<b>Send the new Claim button text together with its emoji, in one message.</b>\n"
    "• Premium emoji anywhere in the message = saved automatically as the button icon (shown in front)\n"
    "• Normal emoji written at the end is moved to the front automatically\n"
    "• If there is more than one page, \"(Page X/Y)\" is added automatically\n\n"
    "Send /cancel to cancel, /reset_default to reset."
)
Bot.handleNextCommand("/PIRO_SetClaimBtnTxtSave")


#======================================================================
# COMMAND: /PIRO_SetClaimBtnTxtSave
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

Full = str(message.text or "")
Txt = Full.strip()

if Txt == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if Txt == "/reset_default":
    Bot.deleteData("PIRO_ClaimBtnText")
    Bot.deleteData("PIRO_ClaimBtnEmojiId")
    bot.sendMessage("<b>♻️ Claim button reset to default (🔒 Claim, no icon).</b>")
    raise ReturnCommand()

# 1) Premium emoji -> becomes the button icon (shown in front), removed from text
Icon = None
Cut = []
for e in (message.entities or []):
    if e.type == "custom_emoji":
        if Icon is None:
            Icon = str(e.custom_emoji_id)
        Cut.append((e.offset, e.length))

if Cut:
    Res = ""
    p = 0
    for ch in Full:
        w = 2 if ord(ch) > 65535 else 1
        inside = False
        for (o, l) in Cut:
            if p >= o and p < o + l:
                inside = True
        if not inside:
            Res += ch
        p += w
    Txt = Res.strip()

# 2) Regular emoji written at the END gets moved to the FRONT
tokens = Txt.split()
last = -1
for idx, t in enumerate(tokens):
    if len([c for c in t if c.isalnum()]) > 0:
        last = idx

if last >= 0:
    body = tokens[:last + 1]
    tail = tokens[last + 1:]
    w = body[-1]
    cut = len(w)
    for k in range(len(w) - 1, -1, -1):
        c = w[k]
        if c.isalnum():
            break
        if ord(c) >= 8592 or ord(c) == 8205:
            cut = k
        else:
            break
    glued = w[cut:]
    body[-1] = w[:cut]
    frontparts = [x for x in ([glued] + tail) if x]
    Txt = " ".join(frontparts + body).strip()

if not Txt and Icon:
    Bot.saveData("PIRO_ClaimBtnEmojiId", Icon)
    bot.sendMessage("<b>✅ Claim button icon saved (text unchanged).</b>")
    raise ReturnCommand()

if not Txt or len(Txt) > 30:
    bot.sendMessage("<b>⚠️ Please send text between 1 and 30 characters.</b>")
    Bot.handleNextCommand("/PIRO_SetClaimBtnTxtSave")
    raise ReturnCommand()

Bot.saveData("PIRO_ClaimBtnText", Txt)
IconMsg = ""
if Icon:
    Bot.saveData("PIRO_ClaimBtnEmojiId", Icon)
    IconMsg = f"\n🎭 Premium emoji saved as icon (id {Icon})"

bot.sendMessage(f"<b>✅ Claim button text: {Txt}</b>{IconMsg}")


#======================================================================
# COMMAND: /PIRO_SetJoinBtnEmoji
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

CurId = Bot.getData("PIRO_JoinBtnEmojiId")

bot.replyText(
    u,
    f"<b>🎭 Current Join button icon_custom_emoji_id:</b> {CurId or 'not set'}\n\n"
    "<b>Send a message containing ONLY the custom/premium emoji you want as the Join button's icon "
    "(paste it from Telegram's premium emoji picker). Send /cancel to cancel, /reset_default to remove it.</b>\n\n"
    "<i>Note: Telegram's official Bot API does not document icon support for buttons, so this may or may not visually show — but I'll wire it in exactly as requested.</i>"
)
Bot.handleNextCommand("/PIRO_SetJoinBtnEmojiSave")


#======================================================================
# COMMAND: /PIRO_SetJoinBtnEmojiSave
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

Txt = str(message.text or "").strip()

if Txt == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if Txt == "/reset_default":
    Bot.deleteData("PIRO_JoinBtnEmojiId")
    bot.sendMessage("<b>♻️ Join button icon removed.</b>")
    raise ReturnCommand()

FoundId = None
Ents = message.entities or []
for e in Ents:
    if e.type == "custom_emoji":
        FoundId = e.custom_emoji_id
        break

if not FoundId:
    bot.sendMessage("<b>⚠️ I couldn't find a custom/premium emoji in that message. Make sure you pasted an actual premium emoji (not a regular one), then try again, or /cancel.</b>")
    Bot.handleNextCommand("/PIRO_SetJoinBtnEmojiSave")
    raise ReturnCommand()

Bot.saveData("PIRO_JoinBtnEmojiId", str(FoundId))
bot.sendMessage(f"<b>✅ Join button icon_custom_emoji_id saved: {FoundId}</b>")


#======================================================================
# COMMAND: /PIRO_SetJoinBtnTxt
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

CurJoin = Bot.getData("PIRO_JoinBtnText") or "Join"
CurIcon = Bot.getData("PIRO_JoinBtnEmojiId") or "none"

bot.replyText(
    u,
    f"<b>🔘 Current Join button:</b> {CurJoin}  (icon id: {CurIcon})\n\n"
    "<b>Send the new Join button text together with its emoji, in one message.</b>\n"
    "• Premium emoji anywhere in the message = saved automatically as the button icon (shown in front)\n"
    "• Normal emoji written at the end is moved to the front automatically\n\n"
    "Example: <code>Join Now 🔥</code> becomes <code>🔥 Join Now</code>\n"
    "Send /cancel to cancel, /reset_default to reset."
)
Bot.handleNextCommand("/PIRO_SetJoinBtnTxtSave")


#======================================================================
# COMMAND: /PIRO_SetJoinBtnTxtSave
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

Full = str(message.text or "")
Txt = Full.strip()

if Txt == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if Txt == "/reset_default":
    Bot.deleteData("PIRO_JoinBtnText")
    Bot.deleteData("PIRO_JoinBtnEmojiId")
    bot.sendMessage("<b>♻️ Join button reset to default (Join, no icon).</b>")
    raise ReturnCommand()

# 1) Premium emoji -> becomes the button icon (shown in front), removed from text
Icon = None
Cut = []
for e in (message.entities or []):
    if e.type == "custom_emoji":
        if Icon is None:
            Icon = str(e.custom_emoji_id)
        Cut.append((e.offset, e.length))

if Cut:
    Res = ""
    p = 0
    for ch in Full:
        w = 2 if ord(ch) > 65535 else 1
        inside = False
        for (o, l) in Cut:
            if p >= o and p < o + l:
                inside = True
        if not inside:
            Res += ch
        p += w
    Txt = Res.strip()

# 2) Regular emoji written at the END gets moved to the FRONT
tokens = Txt.split()
last = -1
for idx, t in enumerate(tokens):
    if len([c for c in t if c.isalnum()]) > 0:
        last = idx

if last >= 0:
    body = tokens[:last + 1]
    tail = tokens[last + 1:]
    w = body[-1]
    cut = len(w)
    for k in range(len(w) - 1, -1, -1):
        c = w[k]
        if c.isalnum():
            break
        if ord(c) >= 8592 or ord(c) == 8205:
            cut = k
        else:
            break
    glued = w[cut:]
    body[-1] = w[:cut]
    frontparts = [x for x in ([glued] + tail) if x]
    Txt = " ".join(frontparts + body).strip()

if not Txt and Icon:
    Bot.saveData("PIRO_JoinBtnEmojiId", Icon)
    bot.sendMessage("<b>✅ Join button icon saved (text unchanged).</b>")
    raise ReturnCommand()

if not Txt or len(Txt) > 30:
    bot.sendMessage("<b>⚠️ Please send text between 1 and 30 characters.</b>")
    Bot.handleNextCommand("/PIRO_SetJoinBtnTxtSave")
    raise ReturnCommand()

Bot.saveData("PIRO_JoinBtnText", Txt)
IconMsg = ""
if Icon:
    Bot.saveData("PIRO_JoinBtnEmojiId", Icon)
    IconMsg = f"\n🎭 Premium emoji saved as icon (id {Icon})"

bot.sendMessage(f"<b>✅ Join button text: {Txt}</b>{IconMsg}")


#======================================================================
# COMMAND: /PIRO_SetJoinMsg
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

bot.replyText(
    u,
    "<b>✏️ Send the message you want users to see on the Join screen.\n\n"
    "Format it however you like using Telegram's own formatting (bold, italic, links, emoji) "
    "— no HTML needed. You can also forward a message here to copy it exactly. "
    "Photos/stickers with captions work too.\n\n"
    "Send /cancel to cancel, or /reset_default to go back to the built-in default message.</b>"
)
Bot.handleNextCommand("/PIRO_SetJoinMsgSave")


#======================================================================
# COMMAND: /PIRO_SetJoinMsg2
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

bot.replyText(
    u,
    "<b>✏️ Send the EXTRA message that should come together with the channel join message.</b>\n\n"
    "Format it normally in Telegram (bold, italic, links, premium emoji, photo with caption etc.) — no HTML needed. "
    "You can also forward a message to copy it exactly.\n\n"
    "It is sent right after the join message, and when the user taps Joined it is deleted and sent again along with the next join message.\n\n"
    "Send /cancel to cancel, or /reset_default to remove the extra message."
)
Bot.handleNextCommand("/PIRO_SetJoinMsg2Save")


#======================================================================
# COMMAND: /PIRO_SetJoinMsg2Save
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

TxtIn = str(message.text or message.caption or "")

if TxtIn.strip() == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if TxtIn.strip() == "/reset_default":
    Bot.deleteData("PIRO_JoinMsg2ChatId")
    Bot.deleteData("PIRO_JoinMsg2Id")
    bot.sendMessage("<b>♻️ Extra message removed.</b>")
    raise ReturnCommand()

Bot.saveData("PIRO_JoinMsg2ChatId", message.chat.id)
Bot.saveData("PIRO_JoinMsg2Id", message.message_id)

bot.sendMessage("<b>✅ Saved! This extra message will come along with the join message:</b>")

try:
    bot.copyMessage(chat_id=u, from_chat_id=message.chat.id, message_id=message.message_id)
except Exception as e:
    bot.sendMessage(f"<b>⚠️ Saved, but couldn't preview it: {str(e)[:150]}</b>")


#======================================================================
# COMMAND: /PIRO_SetJoinMsgSave
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>")
    raise ReturnCommand()

TxtIn = str(message.text or message.caption or "")

if TxtIn.strip() == "/cancel":
    bot.sendMessage("<b>Cancelled</b>")
    raise ReturnCommand()

if TxtIn.strip() == "/reset_default":
    Bot.deleteData("PIRO_JoinMsgChatId")
    Bot.deleteData("PIRO_JoinMsgId")
    bot.sendMessage("<b>♻️ Reset — the built-in default Join message will be used again.</b>")
    raise ReturnCommand()

Bot.saveData("PIRO_JoinMsgChatId", message.chat.id)
Bot.saveData("PIRO_JoinMsgId", message.message_id)

bot.sendMessage("<b>✅ Saved! This is exactly how it will look to users (buttons will be added automatically):</b>")

try:
    bot.copyMessage(chat_id=u, from_chat_id=message.chat.id, message_id=message.message_id)
except Exception as e:
    bot.sendMessage(f"<b>⚠️ Saved, but couldn't preview it: {str(e)[:150]}</b>")


#======================================================================
# COMMAND: /PIRO_Verification
#======================================================================
EMOJI_PARTY = "6224161941305169199"
EMOJI_STAR = "5469741319330996757"
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5193085063998224234"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_PAISA = "6287207173537666597"
EMOJI_CLOCK = "6231214251835397322"
EMOJI_POTL = "5375296873982604963"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CROWN = "4956420911310832630"
EMOJI_POTLI = "6278489025581944577"
EMOJI_MST = "6278337731063975777"
EMOJI_BANK = "5332455502917949981"

EMOJI_FAILED = EMOJI_FAIL
EMOJI_SECURE = "5197288647275071607"
EMOJI_BULLET = "5458603043203327669"


BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShownV") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/claimvoucher"
    )

    if AdResult:
        User.saveData("TBC_AdShownV", "Y")
        raise ReturnCommand()
Captcha = Bot.getData("CaptchaMode") or "ON"

if Captcha == "OFF":

    # ================= REFERRAL CREDIT =================
    User.deleteData("verify")   # ✅ Yeh line important hai

    # Ab menu dikhao
    saved_link = Bot.getData("SavedLinks")
    owner_id = Bot.getData("Owner")
    if saved_link:
        final_link = saved_link
    elif owner_id:
        final_link = f"tg://openmessage?user_id={owner_id}"
    else:
        final_link = "https://t.me/"

    HHT = (
        f'<tg-emoji emoji-id="{EMOJI_STAR
        }">🏡</tg-emoji><b> Welcome To Refer Earn Bot!</b>\n\n'
        f"<b>How to Earn → </b> <b><a href='{final_link}'>[ CLICK HERE ]</a></b>")

    keyboard = {
    "keyboard": [
        [
            {
                "text": "Balance",
                "icon_custom_emoji_id": EMOJI_POTL
            },
            {
                "text": "Refer Earn",
                "icon_custom_emoji_id": EMOJI_TIE
            }
        ],
        [
            {
                "text": "Bonus",
                "icon_custom_emoji_id": EMOJI_GIFT
            },
            {
                "text": "Withdraw",
                "icon_custom_emoji_id": EMOJI_MST
            }
        ],
        [
            {
                "text": "Payout Method",
                "icon_custom_emoji_id": EMOJI_BANK
            }
        ]
    ],
    "resize_keyboard": True
}

    bot.sendMessage(
        HHT,
        chat_id=message.chat.id,
        reply_markup=keyboard,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

    raise ReturnCommand()

# ================= VERIFY STATUS =================
verify = User.getData("verify")

if verify == "ok":
    # Agar verify "ok" hai toh menu dikhao
    saved_link = Bot.getData("SavedLinks")
    owner_id = Bot.getData("Owner")
    if saved_link:
        final_link = saved_link
    elif owner_id:
        final_link = f"tg://openmessage?user_id={owner_id}"
    else:
        final_link = "https://t.me/"

    HHT = (
        f'<tg-emoji emoji-id="{EMOJI_STAR
        }">🏡</tg-emoji><b> Welcome To Refer Earn Bot!</b>\n\n'
        f"<b>How to Earn → </b> <b><a href='{final_link}'>[ CLICK HERE ]</a></b>")
    keyboard = {
    "keyboard": [
        [
            {
                "text": "Balance",
                "icon_custom_emoji_id": EMOJI_POTL
            },
            {
                "text": "Refer Earn",
                "icon_custom_emoji_id": EMOJI_TIE
            }
        ],
        [
            {
                "text": "Bonus",
                "icon_custom_emoji_id": EMOJI_GIFT
            },
            {
                "text": "Withdraw",
                "icon_custom_emoji_id": EMOJI_MST
            }
        ],
        [
            {
                "text": "Payout Method",
                "icon_custom_emoji_id": EMOJI_BANK
            }
        ]
    ],
    "resize_keyboard": True
}

    bot.sendMessage(
        HHT,
        chat_id=message.chat.id,
        reply_markup=keyboard,
        parse_mode="HTML",
        disable_web_page_preview=True
    )

    raise ReturnCommand()




# ================= HASH GENERATE =================
random_hash = User.getData(
    "user_hash"
)

if random_hash is None:

    chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
    )

    random_hash = ""

    for i in range(32):

        random_hash += libs.Random.randomWeightedChoice(
            chars,
            [1] * len(chars)
        )

    User.saveData(
        "user_hash",
        random_hash
    )


# ================= BOT USERNAME =================
me = HTTP.get(
    "https://api.telegram.org/bot"
    + bot_token +
    "/getMe"
).json()

BOT_USERNAME = me["result"]["username"]


# ================= WEBHOOK URL =================
webhook = libs.Webhook.getUrlFor(
    command="/onWebhook",
    user_id=u
)

webhook_encoded = rawurlencode(
    webhook
)


# ================= WEBAPP URL =================
WEBAPP_URL = (
    "https://verification-page-six.vercel.app/"
    f"?botusername={BOT_USERNAME}"
    f"&webhook={webhook_encoded}"
    f"&hash={random_hash}"
)

# ================= SEND VERIFY =================
EMOJI_BULLET = "5458603043203327669"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_TELEGRAM = "6082461220634368541"

bot.sendMessage(
    f"""<tg-emoji emoji-id="{EMOJI_SECURE}">🔐</tg-emoji><b>Verify Your Self To Continue Bot.</b>
""",

    parse_mode="HTML",

    reply_markup={
        "inline_keyboard": [
            [
                {
                    "text": "Verify Now",
                    "web_app": {
                        "url": WEBAPP_URL
                    },
                    "style": "primary",
                    "icon_custom_emoji_id": EMOJI_BULLET
                }
            ]
        ]
    }
)

raise ReturnCommand()


#======================================================================
# COMMAND: /PIRO_Verification0
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, "<b>🙇‍♂️ Bot Is Currently Off</b>")
    raise ReturnCommand()


verify = User.getData("verifyYYY")
if verify:
  bot.sendMessage("🙄Already verified")
  raise ReturnCommand()

webhook = libs.Webhook.getUrlFor(command="/onWebhook", user_id=u)

BOTID = str(bot.info().token).split(":")[0]

webPage="https://api.jobians.top/telegram/verify?webhookUrl="+str(encodeURIComponent(webhook))+"&botId="+BOTID

keys = [[InlineKeyboardButton(text='Verify', web_app=webPage)]]
button = InlineKeyboardMarkup(keys)

bot.sendMessage("<b>🔐 Verify Yourself To Start Bot</b>", reply_markup=button)


#======================================================================
# COMMAND: /PIRO_ban
#======================================================================
# 12'07'25"00'06'18  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()



bot.replyText(u,"<b>📢 Send User Telegram ID to Ban in Bot:</b>""",parse_mode = "html")

Bot.handleNextCommand("/PIRO_ban1")


#======================================================================
# COMMAND: /PIRO_ban1
#======================================================================
# 12'07'25"00'06'18  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

 
bot.replyText(u,f"""<b> Banned Success: {message.text} </b>""",parse_mode = "html")

Bot.saveData(f"{message.text}ban",True)


#======================================================================
# COMMAND: /PIRO_broadcast1
#======================================================================
# 19'4'25 00'11'10 v:1'0'0 [√]
# Broadcast capture: extracts the message content regardless of forward status,
# so admin can later choose Instant Clean Send or Origin-Tagged Send independently.

EMOJI_G = "5039613856603702817"  # 👤

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> You Are Not This Bot Admin</b>', parse_mode="html")
    raise ReturnCommand()

if message.text == "/cancel":
    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> Cancelled</b>', parse_mode="html")
    raise ReturnCommand()

is_forwarded = False
try:
    if message.forward_from or message.forward_from_chat or message.forward_date:
        is_forwarded = True
except:
    is_forwarded = False

direct_function = None
direct_kwargs = {}

if message.photo:
    direct_function = "send_photo"
    direct_kwargs = {"photo": message.photo[-1].file_id}
    if message.caption:
        direct_kwargs["caption"] = message.caption
        try:
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
        except:
            pass

elif message.video:
    direct_function = "send_video"
    direct_kwargs = {"video": message.video.file_id}
    if message.caption:
        direct_kwargs["caption"] = message.caption
        try:
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
        except:
            pass

elif message.document:
    direct_function = "send_document"
    direct_kwargs = {"document": message.document.file_id}
    if message.caption:
        direct_kwargs["caption"] = message.caption
        try:
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
        except:
            pass

elif message.audio:
    direct_function = "send_audio"
    direct_kwargs = {"audio": message.audio.file_id}
    try:
        if message.caption:
            direct_kwargs["caption"] = message.caption
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
    except:
        pass

elif message.voice:
    direct_function = "send_voice"
    direct_kwargs = {"voice": message.voice.file_id}
    try:
        if message.caption:
            direct_kwargs["caption"] = message.caption
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
    except:
        pass

elif message.animation:
    direct_function = "send_animation"
    direct_kwargs = {"animation": message.animation.file_id}
    try:
        if message.caption:
            direct_kwargs["caption"] = message.caption
            if message.caption_entities:
                direct_kwargs["caption_entities"] = message.caption_entities
    except:
        pass

elif message.sticker:
    direct_function = "send_sticker"
    direct_kwargs = {"sticker": message.sticker.file_id}

elif message.contact:
    direct_function = "send_contact"
    direct_kwargs = {
        "phone_number": message.contact.phone_number,
        "first_name": message.contact.first_name or "Contact"
    }
    try:
        if message.contact.last_name:
            direct_kwargs["last_name"] = message.contact.last_name
    except:
        pass

elif message.text:
    direct_function = "send_message"
    direct_kwargs = {"text": message.text}
    try:
        if message.entities:
            direct_kwargs["entities"] = message.entities
    except:
        pass

else:
    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">⚠️</tg-emoji><b> Unsupported Message Type!</b>', parse_mode="html")
    raise ReturnCommand()

broadcast_data = {
    "direct_function": direct_function,
    "direct_kwargs": direct_kwargs,
    "is_forwarded": is_forwarded,
    "from_chat_id": message.chat.id,
    "message_id": message.message_id,
    "mode": "forward" if is_forwarded else "direct",
    "button_rows": [],
    "awaiting_buttons": False
}

User.saveData("broadcast_data", broadcast_data)
User.deleteData("broadcast_confirm_msgid")

# Show a live preview of exactly what was captured (once)
try:
    if is_forwarded:
        bot.forwardMessage(chat_id=u, from_chat_id=message.chat.id, message_id=message.message_id)
    elif direct_function == "send_message":
        bot.sendMessage(text=direct_kwargs.get("text", ""), entities=direct_kwargs.get("entities"))
    elif direct_function == "send_photo":
        bot.sendPhoto(photo=direct_kwargs.get("photo"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_video":
        bot.sendVideo(video=direct_kwargs.get("video"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_document":
        bot.sendDocument(document=direct_kwargs.get("document"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_audio":
        bot.sendAudio(audio=direct_kwargs.get("audio"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_voice":
        bot.sendVoice(voice=direct_kwargs.get("voice"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_animation":
        bot.sendAnimation(animation=direct_kwargs.get("animation"), caption=direct_kwargs.get("caption"), caption_entities=direct_kwargs.get("caption_entities"))
    elif direct_function == "send_sticker":
        bot.sendSticker(sticker=direct_kwargs.get("sticker"))
    elif direct_function == "send_contact":
        bot.sendContact(phone_number=direct_kwargs.get("phone_number"), first_name=direct_kwargs.get("first_name"), last_name=direct_kwargs.get("last_name"))
except Exception as e:
    bot.sendMessage(f"<b>⚠️ Couldn't render preview ({str(e)[:120]})</b>")

Bot.runCommand("/PIRO_broadcast1c")


#======================================================================
# COMMAND: /PIRO_broadcast1_btnbulk
#======================================================================
EMOJI_G = "5039613856603702817"  # 👤
EMOJI_E = "6129434968713076807"  # 📌

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    raise ReturnCommand()

data = User.getData("broadcast_data")

# Authoritative guard: only act if broadcast_data exists AND we explicitly flagged
# ourselves as waiting for button text. This protects against any stray/old wait
# firing (e.g. after Back or Cancel), regardless of platform wait behavior.
if not data or not data.get("awaiting_buttons"):
    # If what got swallowed was actually a real command (e.g. "/start"), forward it
    # on properly instead of silently dropping it.
    Txt0 = str(message.text or "").strip()
    if Txt0.startswith("/"):
        parts = Txt0.split(" ", 1)
        cmd = parts[0]
        opt = parts[1] if len(parts) > 1 else None
        try:
            Bot.runCommand(cmd, options=opt)
        except:
            pass
    raise ReturnCommand()

Txt = str(message.text or "").strip()
StoredMid = User.getData("broadcast_confirm_msgid")

# Keep the chat clean — remove the admin's own typed message
try:
    bot.deleteMessage(message.chat.id, message.message_id)
except:
    pass

if Txt == "/cancel":
    data["awaiting_buttons"] = False
    User.saveData("broadcast_data", data)
    Bot.runCommand("/PIRO_broadcast1c")
    raise ReturnCommand()

Lines = [ln.strip() for ln in Txt.split("\n") if ln.strip()]

BackKb = {"inline_keyboard": [[{"text": "Back", "callback_data": "/PIRO_broadcast1c back", "icon_custom_emoji_id": EMOJI_G}]]}

if not Lines:
    if StoredMid:
        try:
            bot.editMessageText(chat_id=u, message_id=StoredMid, text=f'<tg-emoji emoji-id="{EMOJI_E}">⚠️</tg-emoji><b> Send at least one line, or tap Back.</b>', parse_mode="html", reply_markup=BackKb)
        except:
            bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_E}">⚠️</tg-emoji><b> Send at least one line, or tap Back.</b>', parse_mode="html", reply_markup=BackKb)
    Bot.handleNextCommand("/PIRO_broadcast1_btnbulk")
    raise ReturnCommand()

Rows = []
BadLine = None

for line in Lines:
    parts = [p.strip() for p in line.split("&&")]
    row = []
    for p in parts:
        if " - " not in p:
            BadLine = line
            break
        label, link = p.split(" - ", 1)
        label = label.strip()
        link = link.strip()
        if not label or not (link.startswith("http://") or link.startswith("https://") or link.startswith("tg://")):
            BadLine = line
            break
        row.append({"text": label[:30], "url": link})
    if BadLine:
        break
    Rows.append(row)

if BadLine:
    ErrTxt = (
        f'<tg-emoji emoji-id="{EMOJI_E}">⚠️</tg-emoji><b> This line isn\'t right:</b>\n<code>{BadLine}</code>\n\n'
        "<b>Use: Label - https://link.com</b>\nTry again, or tap Back."
    )
    if StoredMid:
        try:
            bot.editMessageText(chat_id=u, message_id=StoredMid, text=ErrTxt, parse_mode="html", reply_markup=BackKb)
        except:
            bot.sendMessage(ErrTxt, parse_mode="html", reply_markup=BackKb)
    else:
        bot.sendMessage(ErrTxt, parse_mode="html", reply_markup=BackKb)
    Bot.handleNextCommand("/PIRO_broadcast1_btnbulk")
    raise ReturnCommand()

data["button_rows"] = Rows
data["awaiting_buttons"] = False
User.saveData("broadcast_data", data)

Bot.runCommand("/PIRO_broadcast1c")


#======================================================================
# COMMAND: /PIRO_broadcast1c
#======================================================================
# Confirm-broadcast interactive card: delivery-style toggle, add/clear buttons, confirm/cancel.
# Everything happens by EDITING the same message — minimal new messages sent.
# Each panel is locked to its own message_id, so a stale/old panel's buttons can never
# act on a newer broadcast session.
#
# IMPORTANT (button-wait safety): we cannot reliably "cancel" a pending handleNextCommand
# wait from a button tap. So instead, broadcast_data carries its own explicit
# "awaiting_buttons" flag. /PIRO_broadcast1_btnbulk ONLY acts on incoming text when this
# flag is True — regardless of whether some old wait happens to still be pointing at it.
# Tapping Back always clears this flag, so a stray later wait firing becomes a harmless no-op.

EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_B = "5042334757040423886"  # 🆔
EMOJI_C = "5398001711786762757"  # 👥
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_E = "6129434968713076807"  # 📌
EMOJI_F = "5388790256772331442"  # ❤️
EMOJI_G = "5039613856603702817"  # 👤

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in map(str, AllBotAdminss)
if not is_Admin:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> You Are Not This Bot Admin</b>', parse_mode="html")
    raise ReturnCommand()

data = User.getData("broadcast_data")
if not data:
    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">⚠️</tg-emoji><b> Broadcast data not found. Please start again with /broadcast.</b>', parse_mode="html")
    raise ReturnCommand()

P = str(params) if params else ""
StoredMid = User.getData("broadcast_confirm_msgid")
TargetMid = StoredMid or message.message_id

if P and StoredMid and message.message_id != StoredMid:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">⚠️</tg-emoji><b> This broadcast session has expired. Use /broadcast to start a new one.</b>', parse_mode="html")
    raise ReturnCommand()

if P == "cancel":
    User.deleteData("broadcast_data")
    User.deleteData("broadcast_confirm_msgid")
    try:
        bot.editMessageText(chat_id=u, message_id=TargetMid, text=f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> Broadcast Cancelled</b>', parse_mode="html", reply_markup=None)
    except:
        bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> Broadcast Cancelled</b>', parse_mode="html")
    raise ReturnCommand()

if P == "back":
    data["awaiting_buttons"] = False
    User.saveData("broadcast_data", data)

if P == "mode direct":
    if data.get("mode") == "direct":
        try:
            bot.answerCallbackQuery(callback_query_id=message.id, text="✅ Direct is already selected", show_alert=False)
        except:
            pass
        raise ReturnCommand()
    data["mode"] = "direct"
    User.saveData("broadcast_data", data)

elif P == "mode forward":
    if data.get("mode") == "forward":
        try:
            bot.answerCallbackQuery(callback_query_id=message.id, text="✅ Forward is already selected", show_alert=False)
        except:
            pass
        raise ReturnCommand()
    data["mode"] = "forward"
    User.saveData("broadcast_data", data)

elif P == "clearbtns":
    data["button_rows"] = []
    User.saveData("broadcast_data", data)

elif P == "addbtn":
    data["awaiting_buttons"] = True
    User.saveData("broadcast_data", data)

    InstrTxt = (
        f'<tg-emoji emoji-id="{EMOJI_E}">🧩</tg-emoji><b> Add Buttons</b>\n'
        "━━━━━━━━━━━━━━━\n\n"
        "Format: <code>Label - link</code>\n\n"
        "🔹 <b>One button</b>\n"
        "<code>Visit Site - https://example.com</code>\n\n"
        "🔹 <b>Multiple rows</b> — one per line\n"
        "<code>Join Channel - https://t.me/YourChannel\n"
        "Get Support - https://t.me/YourSupport</code>\n\n"
        "🔹 <b>Same row</b> — join with <code>&amp;&amp;</code>\n"
        "<code>Join - https://t.me/A &amp;&amp; Support - https://t.me/B</code>\n\n"
        "🔹 <b>Mix both</b>\n"
        "<code>Join - https://t.me/A &amp;&amp; Support - https://t.me/B\n"
        "Website - https://example.com</code>\n\n"
        "━━━━━━━━━━━━━━━\n"
        "Send your buttons now, or tap Back."
    )
    BackKb = {"inline_keyboard": [[{"text": "Back", "callback_data": "/PIRO_broadcast1c back", "icon_custom_emoji_id": EMOJI_G}]]}
    try:
        bot.editMessageText(chat_id=u, message_id=TargetMid, text=InstrTxt, parse_mode="html", reply_markup=BackKb)
    except:
        sent = bot.sendMessage(InstrTxt, parse_mode="html", reply_markup=BackKb)
        try:
            TargetMid = sent.message_id
        except:
            TargetMid = sent["message_id"]
        User.saveData("broadcast_confirm_msgid", TargetMid)
    Bot.handleNextCommand("/PIRO_broadcast1_btnbulk")
    raise ReturnCommand()

elif P == "confirm":
    try:
        bot.editMessageText(chat_id=u, message_id=TargetMid, text=f'<tg-emoji emoji-id="{EMOJI_A}">🎉</tg-emoji><b> Sending your broadcast...</b>', parse_mode="html", reply_markup=None)
    except:
        pass
    Bot.runCommand("/PIRO_broadcast2")
    raise ReturnCommand()

TYPE_LABELS = {
    "send_message": "Text",
    "send_photo": "Photo",
    "send_video": "Video",
    "send_document": "Document",
    "send_audio": "Audio",
    "send_voice": "Voice Note",
    "send_sticker": "Sticker",
    "send_animation": "GIF",
    "send_contact": "Contact Card",
}

TypeLabel = TYPE_LABELS.get(data.get("direct_function"), "Unknown")
Mode = data.get("mode", "direct")
Rows = data.get("button_rows") or []
BtnCount = sum(len(r) for r in Rows)

if Mode == "direct":
    ModeLine = "🚀 <b>Direct</b> — clean message, no tag"
else:
    ModeLine = "🔁 <b>Forward</b> — shows 'Forwarded from' tag"

if BtnCount:
    BtnLine = f"✅ <b>{BtnCount}</b> button(s) in <b>{len(Rows)}</b> row(s)"
    if Mode == "forward":
        BtnLine += "\n   <i>(won't show — forwards can't carry buttons)</i>"
else:
    BtnLine = "— None yet —"

FulUsrs = Bot.getData("FulBotUsrs") or []

TXT = (
    f'<tg-emoji emoji-id="{EMOJI_A}">📣</tg-emoji> <b>Broadcast Panel</b>\n'
    "━━━━━━━━━━━━━━━\n"
    f'<tg-emoji emoji-id="{EMOJI_B}">🆔</tg-emoji> <b>Content</b> ⟶ {TypeLabel}\n'
    f'<tg-emoji emoji-id="{EMOJI_C}">👥</tg-emoji> <b>Delivery</b> ⟶ {ModeLine}\n'
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji> <b>Buttons</b> ⟶ {BtnLine}\n'
    "━━━━━━━━━━━━━━━\n\n"
    f'<tg-emoji emoji-id="{EMOJI_F}">❤️</tg-emoji> <b>Ready to go out?</b>\n'
    f"<blockquote>This will reach <b>{len(FulUsrs)}</b> user(s) once you confirm.</blockquote>"
)

keyboard = []

keyboard.append([
    {"text": ("Direct ✅" if Mode == "direct" else "Direct"), "callback_data": "/PIRO_broadcast1c mode direct", "icon_custom_emoji_id": EMOJI_D},
    {"text": ("Forward ✅" if Mode == "forward" else "Forward"), "callback_data": "/PIRO_broadcast1c mode forward", "icon_custom_emoji_id": EMOJI_C}
])

if BtnCount:
    keyboard.append([
        {"text": "Add More", "callback_data": "/PIRO_broadcast1c addbtn", "icon_custom_emoji_id": EMOJI_E},
        {"text": "Clear Buttons", "callback_data": "/PIRO_broadcast1c clearbtns", "icon_custom_emoji_id": EMOJI_G}
    ])
else:
    keyboard.append([{"text": "Add Buttons", "callback_data": "/PIRO_broadcast1c addbtn", "icon_custom_emoji_id": EMOJI_E}])

keyboard.append([
    {"text": "Confirm & Send", "callback_data": "/PIRO_broadcast1c confirm", "icon_custom_emoji_id": EMOJI_A},
    {"text": "Cancel", "callback_data": "/PIRO_broadcast1c cancel", "icon_custom_emoji_id": EMOJI_G}
])

Edited = False
if StoredMid:
    try:
        bot.editMessageText(chat_id=u, message_id=StoredMid, text=TXT, parse_mode="html", reply_markup={"inline_keyboard": keyboard})
        Edited = True
    except:
        Edited = False

if not Edited and P:
    try:
        bot.answerCallbackQuery(callback_query_id=message.id, text="Already up to date", show_alert=False)
    except:
        pass

if not Edited and not P:
    sent = bot.sendMessage(TXT, parse_mode="html", reply_markup={"inline_keyboard": keyboard})
    try:
        Mid = sent.message_id
    except:
        Mid = sent["message_id"]
    User.saveData("broadcast_confirm_msgid", Mid)


#======================================================================
# COMMAND: /PIRO_broadcast2
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_G = "5039613856603702817"  # 👤

# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
        break

if not is_Admin:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> You Are Not This Bot Admin</b>', parse_mode="html")
    raise ReturnCommand()

data = User.getData("broadcast_data")

if not data:
    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">⚠️</tg-emoji><b> Nothing to send. Start again with /broadcast.</b>', parse_mode="html")
    raise ReturnCommand()

# Generate webhook callback URL to trigger /PIRO_broadcast3 upon completion
url = libs.Webhook.getUrlFor("/PIRO_broadcast3", u)

try:
    Mode = data.get("mode", "direct")

    if Mode == "forward":
        func = "forward_message"
        kwargs = {
            "from_chat_id": data.get("from_chat_id"),
            "message_id": data.get("message_id"),
        }
    else:
        func = data.get("direct_function")
        kwargs = dict(data.get("direct_kwargs") or {})
        Rows = data.get("button_rows") or []
        if Rows:
            kwargs["reply_markup"] = {"inline_keyboard": Rows}

    # Launch mass broadcast task using function safelist
    task = Bot.broadcast(function=func, callback_url=url, **kwargs)

    if task.get("status") != "success":
        bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">❌</tg-emoji><b> Broadcast failed:</b>\n\n<code>{task}</code>', parse_mode="html")
        raise ReturnCommand()

    broadcast_id = task.get("broadcast_id")
    User.saveData("active_broadcast_id", broadcast_id)
    User.deleteData("broadcast_data")
    User.deleteData("broadcast_confirm_msgid")
    User.deleteData("broadcast_pending_btn_text")

    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_A}">🚀</tg-emoji><b> Broadcast started!</b>', parse_mode="html")

except Exception as e:
    bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_G}">❌</tg-emoji><b> Error:</b>\n\n<code>{str(e)}</code>', parse_mode="html")


#======================================================================
# COMMAND: /PIRO_broadcast3
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_G = "5039613856603702817"  # 👤

try:
    # Parse webhook options payload delivered upon completion
    if hasattr(options, "json") and options.json:
        data = bunchify(options.json)
    elif isinstance(options, dict):
        data = options
    else:
        data = {}

    total = int(data.get("total", 0) or 0)
    success = int(data.get("total_success", 0) or 0)
    fail = int(data.get("total_errors", 0) or 0)

    TXT = (
        f'<tg-emoji emoji-id="{EMOJI_A}">📊</tg-emoji> <b>Broadcast Report</b>\n'
        "━━━━━━━━━━━━━━━\n"
        f"🆔 <b>Sent To:</b> 0\n"
        f"✅ <b>Success:</b> 0\n"
        f"🚫 <b>Failed:</b> 0\n"
        "━━━━━━━━━━━━━━━\n"
        "⏳ Tallying..."
    )

    sent = bot.sendMessage(TXT, parse_mode="html")
    try:
        Mid = sent.message_id
    except:
        Mid = sent["message_id"]

    Payload = f"{Mid}|1|{total}|{success}|{fail}"
    Bot.runCommandAfter(1, "/PIRO_BCStatsStep", options=Payload)
    User.deleteData("active_broadcast_id")

except Exception as e:
    bot.sendMessage(text=f'<tg-emoji emoji-id="{EMOJI_G}">⚠️</tg-emoji><b> Error reading result:</b>\n\n<code>{str(e)}</code>', parse_mode="html")


#======================================================================
# COMMAND: /PIRO_unban
#======================================================================
# 12'07'25"00'06'18  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()



bot.replyText(u,"<b>📢 Send User Telegram ID to Unban in Bot:</b>""",parse_mode = "html")

Bot.handleNextCommand("/PIRO_unban1")


#======================================================================
# COMMAND: /PIRO_unban1
#======================================================================
# 12'07'25"00'06'18  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


bot.replyText(u,f"""<b> Unanned Success: {message.text} </b>""",parse_mode = "html")

Bot.saveData(f"{message.text}ban",False)


#======================================================================
# COMMAND: /PIRO_withdraw
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6278294652541996868"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_HEART = "5388790256772331442"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"

# coded by @Jenish_Dobariya1

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Bot Is Currently Off</b>', parse_mode="HTML")
    raise ReturnCommand()

# --- ULTRA-STRICT SYSTEM CHECK ---
W_Mode = Bot.getData("WalletWithdrawMode")
W_With = Bot.getData("WalletWithdraw")

check_mode = str(W_Mode).strip().upper() if W_Mode is not None else "NONE"
check_with = str(W_With).strip().upper() if W_With is not None else "NONE"

if check_mode == "OFF" or check_mode == "FALSE" or check_with == "OFF" or check_with == "FALSE":
    custom_text = Bot.getData("WOT") or f'<tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji><b> allet Withdrawal Method Is Currently Disabled</b>'
    bot.replyText(u, custom_text, parse_mode="HTML")
    raise ReturnCommand()
    
    
PaymentCh = Bot.getData("Botpaychannel") or "not set"
if PaymentCh == "not set":
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='⚙️ Set Payout Channel', callback_data='/SetBotPayChann'))
    
    # Professional message
    msg = (
        f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> No Payout Channel Added!</b>\n\n'
        "<i>Current status: Not set. Please set the payout channel "
        "to enable withdrawals for your users.</i>"
    )
    
    bot.replyText(u, msg, reply_markup=markup, parse_mode="HTML")
    raise ReturnCommand()
# Referral Verification System
refC = Bot.getData(str(u) + "RefCount") or 0
refN = Bot.getData("SetMinRef") or 0
ChkR = int(refN) - int(refC)

markup = InlineKeyboardMarkup()
if int(refN) > 0 and int(refC) < int(refN):
    markup.add(InlineKeyboardButton(text=f"You need only {ChkR} refer(s) 🎯", callback_data="Invite Earn 🤑"))
else:
    markup.add(InlineKeyboardButton(text="Set Wallet 💳", callback_data="Link Wallet"))

# Balance & Wallet Validations
wall = Bot.getData("UserWallet" + str(u))
bal = libs.Resources.anotherRes('Balance', user=u).value()
Mini_Withdraw = Bot.getData("MinWith") or 1

if bal is None:
    bal = 0.0

if float(bal) < float(Mini_Withdraw):
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_WARN}">🤑</tg-emoji><b> You need minimum {Mini_Withdraw} balance to withdraw</b>', parse_mode="HTML")
    raise ReturnCommand()

if wall is None:
    bot.replyText(u, "<b>⚙️ Please set your Wallet first to continue!</b>", parse_mode="HTML", reply_markup=markup)
    raise ReturnCommand()

if int(refN) > 0 and int(refC) < int(refN):
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>You need only {ChkR} more verified refer(s) to unlock withdraw.\n\n👉 Click below to complete & withdraw instantly in your Wallet ✓</b>', parse_mode="HTML", reply_markup=markup)
    raise ReturnCommand()

# Input prompt triggers
bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_MONEY}">💰</tg-emoji><b> Send Total Amount You Wish To Withdraw</b>', parse_mode="HTML")
Bot.handleNextCommand("/PIRO_withdraw1", options="View")


#======================================================================
# COMMAND: /PIRO_withdraw1
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6278294652541996868"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_STAT = "6001546944470587024"
EMOJI_WALLET = "5472363448404809929"
EMOJI_SIREN = "6129532640564354033"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_NUMBER = "5264895611517300926"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"
# coded by @Jenish_Dobariya1

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>', parse_mode="HTML")
    raise ReturnCommand()

# --- ULTRA-STRICT SYSTEM STATUS CHECK ---
W_Mode = Bot.getData("WalletWithdrawMode")
W_With = Bot.getData("WalletWithdraw")

check_mode = str(W_Mode).strip().upper() if W_Mode is not None else "NONE"
check_with = str(W_With).strip().upper() if W_With is not None else "NONE"

if check_mode == "OFF" or check_mode == "FALSE" or check_with == "OFF" or check_with == "FALSE":
    custom_text = Bot.getData("WOT") or f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Wallet Withdrawal Method Is Currently Disabled</b>'
    bot.replyText(u, custom_text, parse_mode="HTML")
    raise ReturnCommand()
    

# Master Gateway Matrix Mapping
gateway_master = {
    "sa": {"name": "Saathi", "cmd": "/PIRO_withdrawsa", "url": "http://saathigateway.com"},
    "vsv": {"name": "VSV", "cmd": "/PIRO_withdrawVsvw", "url": "https://vsv-gateway-solutions.co.in"},
    "payzy": {"name": "Payzy", "cmd": "/PIRO_withdrawpayzy", "url": "https://payzy-gateway.site"},
    "ultra": {"name": "Ultra", "cmd": "/PIRO_withdrawu", "url": "https://ultra-pay.in"},
    "txg": {"name": "TXG", "cmd":"/PIRO_withdrawTXG", "url":"http://txg-gateway.xyz"},
    "rupix": {"name": "Rupix", "cmd":"/PIRO_withdrawRupix", "url":"https://rupixwallet.shop"},

}

# --- PARSE INPUT AMOUNT CONTROL ---
is_callback = False
if options == "View":
    amount_input = message.text if message.text else msg
else:
    if params and "_" in str(params):
        try:
            amount_input = params.split("_")[1]
            is_callback = True
        except:
            amount_input = params
    else:
        amount_input = params

try:
    amount = float(amount_input)
except:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Only Numeric Values Are Allowed</b>', parse_mode="HTML")
    raise ReturnCommand()

# Global Business Limits & Balance Validations
wallet = Bot.getData("UserWallet" + str(u)) or "Not Linked"
minWith = float(Bot.getData("MinWith") or 5)
maxWith = float(Bot.getData("MaxWith") or 10)
bal = float(libs.Resources.anotherRes('Balance', user=u).value() or 0)

if amount < minWith:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji><b>Minimum Withdraw Limit:</b> <code>{minWith}</code>', parse_mode="HTML")
    raise ReturnCommand()

if amount > bal:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Withdraw Amount Exceeds Your Balance</b>:', parse_mode="HTML")
    raise ReturnCommand()

if amount > maxWith:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">⚠️</tg-emoji><b>Maximum Withdraw Limit:</b> <code>{maxWith}</code>', parse_mode="HTML")
    raise ReturnCommand()


# ================== VIEW STATE: SHOW ACTIVE OPTIONS ==================
if options == "View" or not is_callback:
    try:
        bot.deleteMessage(u)
    except:
        pass

    markup = InlineKeyboardMarkup()
    has_active_gateway = False
    row_buttons = []

    # 2-Column Responsive Layout Generation System
    for key, info in gateway_master.items():
        if Bot.getData(key) == True: 
            has_active_gateway = True
            row_buttons.append(InlineKeyboardButton(text=info['name'], callback_data=f"/PIRO_withdraw1 {key}_{amount}"))
            
            if len(row_buttons) == 2:
                markup.row(*row_buttons)
                row_buttons = []
                
    if row_buttons: 
        markup.row(*row_buttons)

    markup.add(InlineKeyboardButton(text='❌ Cancel Transaction', callback_data='/delete'))

    if not has_active_gateway:
        bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>NoActive Payment Options Available Right Now.</b>', parse_mode="HTML")
        raise ReturnCommand()

    VIEWmessage = f"""<tg-emoji emoji-id="{EMOJI_SUCCESS}">💸</tg-emoji><b> Withdrawal Details</b>

<tg-emoji emoji-id="{EMOJI_WALLET}">📊</tg-emoji><b>Amount ›</b> <code>{amount}</code>
<tg-emoji emoji-id="{EMOJI_NUMBER}">📱</tg-emoji><b>Target Wallet:</b> <code>{wallet}</code>"""

    bot.replyText(u, text=VIEWmessage, reply_markup=markup, parse_mode="HTML", disable_web_page_preview=True)
    raise ReturnCommand()


# ================== EXECUTION STATE: VERIFIED CALLBACK ONLY ==================
if is_callback and params:
    click_status = User.getData(f"clickd{message.message_id}") or "n"
    if click_status == "n":
        User.saveData(f"clickd{message.message_id}", "y")
    else:
        try:
            bot.answerCallbackQuery(call.id, "🔴 Don't Spam Actions")
        except:
            pass
        raise ReturnCommand()

    selected_gw_key = params.split("_")[0]
    gw_data = gateway_master.get(selected_gw_key)

    # Strict Validation
    if not gw_data or Bot.getData(selected_gw_key) != True:
        bot.replyText(u, "<b>❌ Selected Gateway is currently inactive or invalid!</b>", parse_mode="HTML")
        raise ReturnCommand()

    # --- DELETE THE GATEWAY CHOOSE MESSAGE INSTANTLY ---
    try:
        bot.deleteMessage(u, message.message_id)
    except:
        pass

    Bot.saveData("gatewaynow", selected_gw_key)

    # --- ANIMATED PROCESSING ENGINE (NO IMPORTS) ---
    try:
        # Initial Message with Selected Gateway Info
        M = bot.sendMessage(u, f"⚙️ <b>Selected Gateway:</b> <code>{gw_data['name']}</code>\n⏳ <b>Connecting Secure Server...</b>", parse_mode="HTML")
        msg_id = M.message_id
        chat_id = u

        colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
        total_slots = 8

        boot_lines = [
            "🔐 Securing API Encrypted Tunnel",
            "📡 Initializing Gateway Handshake",
            "💳 Fetching User Wallet Address",
            "🪙 Checking Liquidity Node Balance",
            "⚡ Formatting Instant Payout Packet",
            "🚀 Transmitting Fund Dispatch Request"
        ]

        for stage in range(1, 11):
            percent = stage * 10
            filled = int((percent / 100) * total_slots)

            color = colors[(stage - 1) % len(colors)]
            bar = (color * filled) + ("⬜" * (total_slots - filled))

            dots = "." * (stage % 4)
            boot_text = boot_lines[(stage - 1) % len(boot_lines)]

            try:
                bot.editMessageText(
                    chat_id=chat_id,
                    message_id=msg_id,
                    text=(
                        f"⚙️ <b>Selected Gateway:</b> <code>{gw_data['name']}</code>\n"
                        "━━━━━━━━━━━━━━━━━━\n"
                        "💸 <b>Processing Withdrawal" + dots + "</b>\n\n"
                        "📡 <b>Action:</b> " + boot_text + "\n\n"
                        + bar + "  " + str(percent) + "%"
                    ),
                    parse_mode="HTML"
                )
            except:
                pass

            for _ in range(250000):
                pass

        # Final Success State Text
        bot.editMessageText(
            chat_id=chat_id,
            message_id=msg_id,
            text=f"⚙️ <b>Selected Gateway:</b> <code>{gw_data['name']}</code>\n\n✅ <b>Gateway Handshake Successful!</b>\n💰 <i>Routing fund packet to your linked wallet...</i>",
            parse_mode="HTML"
        )

    except Exception as e:
        M = bot.sendMessage(u, f"⚙️ <b>Selected Gateway:</b> <code>{gw_data['name']}</code>\n<b>⏳ Processing your wallet withdrawal request...</b>", parse_mode="HTML")

    # --- BACKEND EXECUTION ROUTE ---
    op = f"{M.message_id}_{amount}"
    Bot.runCommand(gw_data["cmd"], options=op)
    
    


#======================================================================
# COMMAND: /PIRO_withdraw1_UPI
#======================================================================
# coded by @Jenish_Dobariya1
BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, "<b>🙇‍♂️ Bot Is Currently Off</b>", parse_mode="HTML")
    raise ReturnCommand()

# 🛡️ LIVE ADMIN CHECK: Agar UPI OFF hai toh ye screen show hi na ho
UpiStatus = Bot.getData("UpiWithdrawMode") or Bot.getData("UpiWithdraw") or "ON"
if str(UpiStatus).upper() == "OFF":
    bot.replyText(u, "<b>🛑 UPI Withdrawals are temporarily disabled by the Admin.</b>", parse_mode="HTML")
    raise ReturnCommand()

# coded by @Jenish_Dobariya1
gateway = Bot.getData("gatewaynow") or "Not Set"
gateway_map = {
    "Rjwallet": "/PIRO_withdrawRJw",
    "full2sms": "/PIRO_withdrawF2sw",
    "Tgwallet": "/PIRO_withdrawTGw",
    "vsv": "/PIRO_withdrawVsvw",
    "lifafawala": "/PIRO_withdrawLw",
    "Fxl": "/PIRO_withdrawFxlw",
    "info": "/PIRO_withdrawinw",
    "RDX": "/PIRO_withdrawrw",
    "X": "/PIRO_withdrawXw",
    "e": "/PIRO_withdrawe",
    "sa": "/PIRO_withdrawsa",
    "ultra": "/PIRO_withdrawu",
    "payzy": "/payzy_withdraw",
    "unio": "/PIRO_withdrawunio"
}
gateway_command = gateway_map.get(gateway)
if not gateway_command:
    bot.replyText(u, "<b>⛔ No Payout Gateway Configured</b>\n\n<i>Contact Admin to Enable Withdrawals</i>", parse_mode="HTML")
    raise ReturnCommand()

# 🏦 UPI DATA ONLY
wallet = Bot.getData("UserUPI" + str(u)) or "Not Linked"
TotWith = Bot.getData("TotalWith") or 0
BFWithrw = Bot.getData("BFWithrw") or 0
minWith = float(Bot.getData("MinWith1") or 5)
maxWith = float(Bot.getData("MaxWith1") or 10)
tax = float(Bot.getData("Tax1") or 0)

bal = libs.Resources.anotherRes('Balance', user=u).value()
amount_input = params or msg
try:
    amount = float(amount_input)
except:
    bot.replyText(u, "<b>⛔ Only Numeric Values Are Allowed ⛔</b>", parse_mode="HTML")
    raise ReturnCommand()

# Validation Checks
if amount < minWith:
    bot.replyText(u, f"<b>⚠️ Minimum Withdraw Limit:</b> <code>{minWith}</code>", parse_mode="HTML")
    raise ReturnCommand()

if amount > bal:
    bot.replyText(u, "<b>🚫 Withdraw Amount Exceeds Your Balance</b>", parse_mode="HTML")
    raise ReturnCommand()

if amount > maxWith:
    bot.replyText(u, f"<b>⚠️ Maximum Withdraw Limit:</b> <code>{maxWith}</code>", parse_mode="HTML")
    raise ReturnCommand()

if options != "View":
    try:
        bot.deleteMessage(u, message.message_id)
    except:
        pass

# 🏦 SIRF UPI APPROVE KA BUTTON SHOW HOGA
markup = InlineKeyboardMarkup()
markup.add(
    InlineKeyboardButton(text='🏦 Approve UPI Withdraw', callback_data='/PIRO_withdraw1_UPI ' + str(amount)),
    InlineKeyboardButton(text='❌ Cancel Request', callback_data='/delete')
)

VIEWmessage = f"""<b>💸 UPI Withdrawal Confirmation</b>\n\n━━━━━━━━━━━━━━━\n💰 <b>Amount:</b> <code>{amount} INR</code>\n🏦 <b>UPI ID:</b> <code>{wallet}</code>\n📦 <b>Gateway:</b> <code>UPI AUTO-PAY</code>\n━━━━━━━━━━━━━━━\n\n<i>Confirm your transaction below to proceed.</i>\n"""

if options == "View":
    bot.replyText(u, text=VIEWmessage, reply_markup=markup, parse_mode="HTML")
    raise ReturnCommand()

if str(params) != "None":
    click_status = User.getData(f"clickd{message.message_id}") or "n"
    if click_status == "n":
        User.saveData(f"clickd{message.message_id}", "y")
    else:
        try:
            bot.answerCallbackQuery(call.id, "🔴 Don't Spam Actions")
        except:
            pass
        raise ReturnCommand()

    WITHmessageTOuser = "<b>⏳ Processing your UPI withdrawal request...</b>"
    M = bot.sendMessage(WITHmessageTOuser, parse_mode="HTML")
    op = f"{M.message_id}_{amount}"
    Bot.runCommand("Process_UPI", options=op)


#======================================================================
# COMMAND: /PIRO_withdrawRupix
#======================================================================
def escape_html(text):
    if not text:
        return ""
    return text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

PaymentCh=Bot.getData("Botpaychannel") or "not set"
Botpayname=Bot.getData("BotPayComm") or "Payment"
current_gateway=Bot.getData("gatewaynow")
KEY=Bot.getData(f"KEY_{current_gateway}") or "not set"

AllBanUsers=(Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u,"<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets=(Bot.getData("AllBanWallets") or "12345").split(",")
wallet=Bot.getData("UserWallet"+str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u,"<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode=Bot.getData("WithdrawMode") or "ON"
if WitdMode=="OFF":
    WOT=Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u,WOT)
    raise ReturnCommand()

Gatewaysett0=Bot.getData("gatewaynow") or "Not Set"
if Gatewaysett0=="Not Set":
    bot.replyText(u,"<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

P=options.split("_")
MD=int(P[0])
amount=float(P[1])

bal=float(libs.Resources.anotherRes("Balance",user=u).value())
minWith=float(Bot.getData("MinWith") or 5)
tax=float(Bot.getData("rupixtax") or 0)
WithdrawC=int(Bot.getData("WithdrawC") or 0)

wallet=Bot.getData("UserWallet"+str(u)) or "1234567890"
hide_wallet=f"{wallet[0:3]}*****{wallet[-3:]}"
AmountAftrTax=amount-tax

if bal<amount:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text="<b>❌ Withdrawal Failed\n\nReason : Insufficient Balance</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

if amount<minWith:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=f"<b>❌ Withdrawal Failed\n\nReason : Minimum withdrawal is ₹{minWith}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

libs.Resources.anotherRes("Balance",user=u).cut(amount)
Bot.saveData("WithdrawC",WithdrawC+1)

refunded=False

try:
    url=f"https://rupixwallet.shop/api/v1/wallet/transfer?key={KEY}&wallet={wallet}&amount={AmountAftrTax}&comment={Botpayname}"
    response=HTTP.get(url)
    data=response.json()

    if not isinstance(data,dict):
        data={}

    status=str(data.get("status") or data.get("Status") or data.get("state") or "")
    success=data.get("success") is True or status.lower()=="success"

    error_code=str(
        data.get("error_code")
        or data.get("errorCode")
        or data.get("code")
        or "UNKNOWN"
    )

    gateway_message=str(
        data.get("gateway_message")
        or data.get("gatewayMessage")
        or data.get("message")
        or data.get("msg")
        or data.get("error")
        or data.get("reason")
        or data.get("description")
        or "Unknown error"
    )

    error_code=escape_html(error_code)
    status=escape_html(status)
    gateway_message=escape_html(gateway_message)

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    if success:

        WITHmessage=(
            "<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n"
            "✔️ Please Check Your Rupix Wallet Account!</b>"
        )

        channel_msg=(
            "<b>✅ New Withdrawal Processed ✅</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Rupix Wallet Response: "
            f"<code>{{'status': 'success', 'message': '{gateway_message}', "
            f"'code': 'PPT_200'}}</code></b>"
        )

        # ==========================
        # LIVE FUND DEDUCT
        # ==========================

        try:
            fund=float(Bot.getData("LiveFund") or 0)

            newfund=fund-amount

            if newfund<0:
                newfund=0

            Bot.saveData("LiveFund",newfund)

            channel1=Bot.getData("LiveFundChannel1")
            channel2=Bot.getData("LiveFundChannel2")

            msgid1=Bot.getData("LiveFundMsgID1")
            msgid2=Bot.getData("LiveFundMsgID2")

            try:
                bot_name=Bot.info().username
            except:
                bot_name="Bot"


            # ==========================
            # LIVE FUND TEXT
            # ==========================

            live_text=(
                "<b>✅ Total Remaining Fund In @"
                +str(bot_name)
                +" >> ₹"
                +str(round(newfund,2))
                +"\n\n🚀 This Is A High Fund And Long Term Running Bot With Huge Funds"
                +"\n\n💰💰 Loot As Much As You Can 😎🙏"
                +"\n\n😍 Specially Powered By"
                +"\n@"
                +str(bot_name)
                +" !!</b>"
            )


            # ==========================
            # FUND BUTTON
            # ==========================

            live_button={
                "inline_keyboard":[
                    [
                        {
                            "text":"💰 Fund ₹"+str(round(newfund,2)),
                            "url":"https://t.me/"+str(bot_name)
                        }
                    ]
                ]
            }


            # ==========================
            # CHANNEL 1 UPDATE
            # ==========================

            if channel1 and msgid1:

                try:

                    bot.editMessageText(
                        chat_id=channel1,
                        message_id=int(msgid1),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


            # ==========================
            # CHANNEL 2 UPDATE
            # ==========================

            if channel2 and msgid2:

                try:

                    bot.editMessageText(
                        chat_id=channel2,
                        message_id=int(msgid2),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


        except:
            pass


        # ==========================
        # PAYMENT CHANNEL LOG
        # ==========================

        bot.replyText(
            PaymentCh,
            channel_msg,
            parse_mode="HTML"
        )

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=WITHmessage,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        libs.Resources.anotherRes("Withdraw",user=u).add(amount)
        libs.Resources.globalRes("BotWithdraws").add(amount)

    else:

        libs.Resources.anotherRes("Balance",user=u).add(amount)
        refunded=True

        balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

        channel_msg=(
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Rupix Wallet Response: "
            f"<code>{{'status': 'failed', 'message': '{gateway_message}', "
            f"'code': 'PPT_000'}}</code></b>"
        )

        bot.replyText(PaymentCh,channel_msg,parse_mode="HTML")

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=(
                "<b>❌ Withdrawal Failed\n\n"
                f"⚠️ Reason : <code>{gateway_message}</code></b>"
            ),
            parse_mode="HTML"
        )

except Exception as e:

    if not refunded:
        libs.Resources.anotherRes("Balance",user=u).add(amount)

    error_msg=escape_html(str(e))

    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=(
            "<b>❌ Withdrawal Failed\n\n"
            f"⚠️ Reason : <code>Timeout Or Invalid Response</code></b>"
        ),
        parse_mode="HTML"
    )

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    bot.replyText(
        PaymentCh,
        (
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Rupix Wallet Response: "
            f"<code>{{'status': 'failed', 'message': 'Timeout Or Invalid Response', 'code': 'ERROR'}}</code></b>"
        ),
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /PIRO_withdrawTXG
#======================================================================
def escape_html(text):
    if not text:
        return ""
    return text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

PaymentCh=Bot.getData("Botpaychannel") or "not set"
Botpayname=Bot.getData("BotPayComm") or "Payment"
current_gateway=Bot.getData("gatewaynow")
KEY=Bot.getData(f"KEY_{current_gateway}") or "not set"
secret = Bot.getData("SECRETKEY") or "not set"
API = Bot.getData(f"API_{current_gateway}") or "not set"
AllBanUsers=(Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u,"<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets=(Bot.getData("AllBanWallets") or "12345").split(",")
wallet=Bot.getData("UserWallet"+str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u,"<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode=Bot.getData("WithdrawMode") or "ON"
if WitdMode=="OFF":
    WOT=Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u,WOT)
    raise ReturnCommand()

Gatewaysett0=Bot.getData("gatewaynow") or "Not Set"
if Gatewaysett0=="Not Set":
    bot.replyText(u,"<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

P=options.split("_")
MD=int(P[0])
amount=float(P[1])

bal=float(libs.Resources.anotherRes("Balance",user=u).value())
minWith=float(Bot.getData("MinWith") or 5)
tax=float(Bot.getData("txgtax") or 0)
WithdrawC=int(Bot.getData("WithdrawC") or 0)

wallet=Bot.getData("UserWallet"+str(u)) or "1234567890"
hide_wallet=f"{wallet[0:3]}*****{wallet[-3:]}"
AmountAftrTax=amount-tax

if bal<amount:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text="<b>❌ Withdrawal Failed\n\nReason : Insufficient Balance</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

if amount<minWith:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=f"<b>❌ Withdrawal Failed\n\nReason : Minimum withdrawal is ₹{minWith}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

libs.Resources.anotherRes("Balance",user=u).cut(amount)
Bot.saveData("WithdrawC",WithdrawC+1)

refunded=False

try:
    url=f"https://txg-gateway.xyz/client/api/send.php?api_key={KEY}&secret_pin={secret}&toUser={wallet}&amount={AmountAftrTax}&remark={Botpayname}"
    response=HTTP.get(url)
    data=response.json()

    if not isinstance(data,dict):
        data={}

    status=str(data.get("status") or data.get("Status") or data.get("state") or "")
    success=data.get("success") is True or status.lower()=="success"

    error_code=str(
        data.get("error_code")
        or data.get("errorCode")
        or data.get("code")
        or "UNKNOWN"
    )

    gateway_message=str(
        data.get("gateway_message")
        or data.get("gatewayMessage")
        or data.get("message")
        or data.get("msg")
        or data.get("error")
        or data.get("reason")
        or data.get("description")
        or "Unknown error"
    )

    error_code=escape_html(error_code)
    status=escape_html(status)
    gateway_message=escape_html(gateway_message)

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    if success:

        WITHmessage=(
            "<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n"
            "✔️ Please Check Your TXG Wallet Account!</b>"
        )

        channel_msg=(
            "<b>✅ New Withdrawal Processed ✅</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ TXG Wallet Response: "
            f"<code>{{'status': 'success', 'message': '{gateway_message}', "
            f"'code': 'PPT_200'}}</code></b>"
        )

        # ==========================
        # LIVE FUND DEDUCT
        # ==========================

        try:
            fund=float(Bot.getData("LiveFund") or 0)

            newfund=fund-amount

            if newfund<0:
                newfund=0

            Bot.saveData("LiveFund",newfund)

            channel1=Bot.getData("LiveFundChannel1")
            channel2=Bot.getData("LiveFundChannel2")

            msgid1=Bot.getData("LiveFundMsgID1")
            msgid2=Bot.getData("LiveFundMsgID2")

            try:
                bot_name=Bot.info().username
            except:
                bot_name="Bot"


            # ==========================
            # LIVE FUND TEXT
            # ==========================

            live_text=(
                "<b>✅ Total Remaining Fund In @"
                +str(bot_name)
                +" >> ₹"
                +str(round(newfund,2))
                +"\n\n🚀 This Is A High Fund And Long Term Running Bot With Huge Funds"
                +"\n\n💰💰 Loot As Much As You Can 😎🙏"
                +"\n\n😍 Specially Powered By"
                +"\n@"
                +str(bot_name)
                +" !!</b>"
            )


            # ==========================
            # FUND BUTTON
            # ==========================

            live_button={
                "inline_keyboard":[
                    [
                        {
                            "text":"💰 Fund ₹"+str(round(newfund,2)),
                            "url":"https://t.me/"+str(bot_name)
                        }
                    ]
                ]
            }


            # ==========================
            # CHANNEL 1 UPDATE
            # ==========================

            if channel1 and msgid1:

                try:

                    bot.editMessageText(
                        chat_id=channel1,
                        message_id=int(msgid1),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


            # ==========================
            # CHANNEL 2 UPDATE
            # ==========================

            if channel2 and msgid2:

                try:

                    bot.editMessageText(
                        chat_id=channel2,
                        message_id=int(msgid2),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


        except:
            pass


        # ==========================
        # PAYMENT CHANNEL LOG
        # ==========================

        bot.replyText(
            PaymentCh,
            channel_msg,
            parse_mode="HTML"
        )

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=WITHmessage,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        libs.Resources.anotherRes("Withdraw",user=u).add(amount)
        libs.Resources.globalRes("BotWithdraws").add(amount)

    else:

        libs.Resources.anotherRes("Balance",user=u).add(amount)
        refunded=True

        balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

        channel_msg=(
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ TXG Wallet Response: "
            f"<code>{{'status': 'failed', 'message': '{gateway_message}', "
            f"'code': 'PPT_000'}}</code></b>"
        )

        bot.replyText(PaymentCh,channel_msg,parse_mode="HTML")

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=(
                "<b>❌ Withdrawal Failed\n\n"
                f"⚠️ Reason : <code>{gateway_message}</code></b>"
            ),
            parse_mode="HTML"
        )
except Exception as e:

    if not refunded:
        libs.Resources.anotherRes("Balance",user=u).add(amount)

    error_msg=escape_html(str(e))

    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=(
            "<b>❌ Withdrawal Failed\n\n"
            f"⚠️ Reason : <code>Timeout Or Gateway Error</code></b>"
        ),
        parse_mode="HTML"
    )

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    bot.replyText(
        PaymentCh,
        (
            "<b>❗New Withdrawal Failed &amp; Refunded</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ TXG Wallet Response: "
            f"<code>{{'status': 'failed', 'message': 'Timeout Or Invalid Response', 'code': 'ERROR'}}</code></b>"
        ),
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /PIRO_withdrawVsvUPI
#======================================================================
# --- Manual HTML Escaper ---
def escape_html(text):
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PaymentCh = Bot.getData("Botpaychannel") or "not set"
Botpayname = Bot.getData("BotPayComm") or "Payment"
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
Mkey = Bot.getData("MKEY") or "not set"
Token = Bot.getData("TOKEN")
AllBanUsers = (Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u, "<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets = (Bot.getData("AllBanWallets") or "12345").split(",")
wallet = Bot.getData("UserWallet" + str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u, "<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode = Bot.getData("WithdrawMode") or "ON"
if WitdMode == "OFF":
    WOT = Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u, WOT)
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv1": "VSV Wallet",
    "payzy1": "Payzy Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

# Parse options
P = options.split("_")
MD = int(P[0])
amount = float(P[1])
bal = float(libs.Resources.anotherRes("Balance", user=u).value())
minWith = float(Bot.getData("MinWith1") or 5)
tax = float(Bot.getData("Tax2") or 0)
WithdrawC = int(Bot.getData("WithdrawC") or 0)
wallet = Bot.getData("UserUPI" + str(u)) or "1234567890"
hide_wallet = f"{wallet[0:3]}xxxxx{wallet[8:10]}"
AmountAftrTax = amount - (amount * tax / 100)

if bal >= amount and amount >= minWith:
    libs.Resources.anotherRes("Balance", user=u).cut(amount)
    libs.Resources.anotherRes("Withdraw", user=u).add(amount)
    libs.Resources.globalRes("BotWithdraws").add(amount)
    Bot.saveData("WithdrawC", WithdrawC + 1)

    try:
        url=f"https://vsv-gateway-solutions.co.in/Api/upi.php?token={Bot.getData('TOKEN2')}&upi_id={wallet}&amount={AmountAftrTax}&comment=Withdraw"
        response = HTTP.get(url)
        data = response.json()
        status = data.get("status", "")
        message_text = escape_html(data.get("message", "No message"))  # escape before use
        usr = f"""<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>"""
        balance0010 = float(libs.Resources.anotherRes("Balance", user=u).value())

        WITHmessage = f"""<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n✔️ Please Check Your <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Account</b>"""
        WITHmessage01 = f"""<b>✅ New Withdrawal Requested ✅\n\n🟢 User : {usr}\n🚀 Amount : {amount}  ( FEES - {tax}%)\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>{message_text}</code>\n\n✌️ Current Balance : <code>{balance0010}</code>Rs\n\n🔴 Bot: @{Bot.info().username}</b>"""

        if status == "success":
            bot.replyText(PaymentCh, WITHmessage01, parse_mode="html")
            bot.editMessageText(chat_id=u, message_id=MD, text=WITHmessage, parse_mode="html", disable_web_page_preview=True)
            libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        else:
            # Refund back on failure
            libs.Resources.anotherRes("Balance", user=u).add(amount)
            bot.editMessageText(chat_id=u, message_id=MD, text=(
                "<b>❌ Withdrawal Failed 🔥🚀\n\n"
                "⚠️ Reason: Invalid or incorrect wallet number.\n"
                "💡 Please double-check and try again!</b>"), parse_mode="HTML")
            
            # Notify payment channel about failure
            bot.replyText(PaymentCh, f"""<b>❌ Withdrawal Failed ❌\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>{message_text}</code>\n\n🔴 Bot: @{Bot.info().username}</b>""", parse_mode="html")

    except Exception as e:
        # Refund user balance on error/timeout
        libs.Resources.anotherRes("Balance", user=u).add(amount)
        error_msg = escape_html(str(e))  # escape before sending
        usr = f"""<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>"""

        # Timeout or generic error
        if "timeout" in error_msg.lower():
            user_msg = "<b>⏳ Withdrawal Timeout! The gateway did not respond in time. Please try again later.</b>"
            channel_msg = f"""<b>⏳ Withdrawal Timeout ⏳\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : Gateway Timeout\n\n🔴 Bot: @{Bot.info().username}</b>"""
        else:
            user_msg = f"<b>⚠️ Error occurred:</b>"
            channel_msg = f"""<b>⚠️ Withdrawal Error ⚠️\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>Failed</code>\n\n🔴 Bot: @{Bot.info().username}</b>"""

        bot.replyText(u, user_msg, parse_mode="html")
        bot.replyText(PaymentCh, channel_msg, parse_mode="html")
        


#======================================================================
# COMMAND: /PIRO_withdrawVsvw
#======================================================================
def escape_html(text):
    if not text:
        return ""
    return text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

PaymentCh=Bot.getData("Botpaychannel") or "not set"
Botpayname=Bot.getData("BotPayComm") or "Payment"
current_gateway=Bot.getData("gatewaynow")
KEY=Bot.getData(f"KEY_{current_gateway}") or "not set"
current_gateway = Bot.getData("gatewaynow")
Token = Bot.getData(f"TOKEN_{current_gateway}") or "not set"
AllBanUsers=(Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u,"<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets=(Bot.getData("AllBanWallets") or "12345").split(",")
wallet=Bot.getData("UserWallet"+str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u,"<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode=Bot.getData("WithdrawMode") or "ON"
if WitdMode=="OFF":
    WOT=Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u,WOT)
    raise ReturnCommand()

Gatewaysett0=Bot.getData("gatewaynow") or "Not Set"
if Gatewaysett0=="Not Set":
    bot.replyText(u,"<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

P=options.split("_")
MD=int(P[0])
amount=float(P[1])

bal=float(libs.Resources.anotherRes("Balance",user=u).value())
minWith=float(Bot.getData("MinWith") or 5)
tax=float(Bot.getData("vsvtax") or 0)
WithdrawC=int(Bot.getData("WithdrawC") or 0)

wallet=Bot.getData("UserWallet"+str(u)) or "1234567890"
hide_wallet=f"{wallet[0:3]}*****{wallet[-3:]}"
AmountAftrTax=amount-tax

if bal<amount:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text="<b>❌ Withdrawal Failed\n\nReason : Insufficient Balance</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

if amount<minWith:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=f"<b>❌ Withdrawal Failed\n\nReason : Minimum withdrawal is ₹{minWith}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

libs.Resources.anotherRes("Balance",user=u).cut(amount)
Bot.saveData("WithdrawC",WithdrawC+1)

refunded=False

try:
    url=f"https://vsv-gateway-solutions.co.in/Api/api.php?token={Token}&paytm={wallet}&amount={AmountAftrTax}&comment={Botpayname}"
    response=HTTP.get(url)
    data=response.json()

    if not isinstance(data,dict):
        data={}

    status=str(data.get("status") or data.get("Status") or data.get("state") or "")
    success=data.get("success") is True or status.lower()=="success"

    error_code=str(
        data.get("error_code")
        or data.get("errorCode")
        or data.get("code")
        or "UNKNOWN"
    )

    gateway_message=str(
        data.get("gateway_message")
        or data.get("gatewayMessage")
        or data.get("message")
        or data.get("msg")
        or data.get("error")
        or data.get("reason")
        or data.get("description")
        or "Unknown error"
    )

    error_code=escape_html(error_code)
    status=escape_html(status)
    gateway_message=escape_html(gateway_message)

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    if success:

        WITHmessage=(
            "<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n"
            "✔️ Please Check Your VSV Wallet Account!</b>"
        )

        channel_msg=(
            "<b>✅ New Withdrawal Processed ✅</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ VSV Wallet Response: "
            f"<code>{{'status': 'success', 'message': '{gateway_message}', "
            f"'code': 'PPT_200'}}</code></b>"
        )

        # ==========================
        # LIVE FUND DEDUCT
        # ==========================

        try:
            fund=float(Bot.getData("LiveFund") or 0)

            newfund=fund-amount

            if newfund<0:
                newfund=0

            Bot.saveData("LiveFund",newfund)

            channel1=Bot.getData("LiveFundChannel1")
            channel2=Bot.getData("LiveFundChannel2")

            msgid1=Bot.getData("LiveFundMsgID1")
            msgid2=Bot.getData("LiveFundMsgID2")

            try:
                bot_name=Bot.info().username
            except:
                bot_name="Bot"


            # ==========================
            # LIVE FUND TEXT
            # ==========================

            live_text=(
                "<b>✅ Total Remaining Fund In @"
                +str(bot_name)
                +" >> ₹"
                +str(round(newfund,2))
                +"\n\n🚀 This Is A High Fund And Long Term Running Bot With Huge Funds"
                +"\n\n💰💰 Loot As Much As You Can 😎🙏"
                +"\n\n😍 Specially Powered By"
                +"\n@"
                +str(bot_name)
                +" !!</b>"
            )


            # ==========================
            # FUND BUTTON
            # ==========================

            live_button={
                "inline_keyboard":[
                    [
                        {
                            "text":"💰 Fund ₹"+str(round(newfund,2)),
                            "url":"https://t.me/"+str(bot_name)
                        }
                    ]
                ]
            }


            # ==========================
            # CHANNEL 1 UPDATE
            # ==========================

            if channel1 and msgid1:

                try:

                    bot.editMessageText(
                        chat_id=channel1,
                        message_id=int(msgid1),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


            # ==========================
            # CHANNEL 2 UPDATE
            # ==========================

            if channel2 and msgid2:

                try:

                    bot.editMessageText(
                        chat_id=channel2,
                        message_id=int(msgid2),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


        except:
            pass


        # ==========================
        # PAYMENT CHANNEL LOG
        # ==========================

        bot.replyText(
            PaymentCh,
            channel_msg,
            parse_mode="HTML"
        )

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=WITHmessage,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        libs.Resources.anotherRes("Withdraw",user=u).add(amount)
        libs.Resources.globalRes("BotWithdraws").add(amount)

    else:

        libs.Resources.anotherRes("Balance",user=u).add(amount)
        refunded=True

        balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

        channel_msg=(
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ VSV Wallet Response: "
            f"<code>{{'status': 'failed', 'message': '{gateway_message}', "
            f"'code': 'PPT_000'}}</code></b>"
        )

        bot.replyText(PaymentCh,channel_msg,parse_mode="HTML")

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=(
                "<b>❌ Withdrawal Failed\n\n"
                f"⚠️ Reason : <code>{gateway_message}</code></b>"
            ),
            parse_mode="HTML"
        )

except Exception as e:

    if not refunded:
        libs.Resources.anotherRes("Balance",user=u).add(amount)

    error_msg=escape_html(str(e))

    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=(
            "<b>❌ Withdrawal Failed\n\n"
            f"⚠️ Reason : <code>Timeout Or Invalid Response</code></b>"
        ),
        parse_mode="HTML"
    )

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    bot.replyText(
        PaymentCh,
        (
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ VSV Wallet Response: "
            f"<code>{{'status': 'failed', 'message': 'Timeout or Invalid Response', 'code': 'ERROR'}}</code></b>"
        ),
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /PIRO_withdraw_upi
#======================================================================
# coded by @Jenish_Dobariya1
# Sahi variables define karein (MinWith1 aur MaxWith1 use karein)
minWith = float(Bot.getData("MinWith1") or 5)
maxWith = float(Bot.getData("MaxWith1") or 10)

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, "<b>🙇‍♂️ Bot Is Currently Off</b>", parse_mode="HTML")
    raise ReturnCommand()

Upi = Bot.getData("UpiWithdraw") or "ON"
if Upi == "OFF":
    txt = Bot.getData("UpiOffText") or "<b>⛔ UPI Withdraw Temporarily Disabled</b>"
    bot.replyText(u, txt, parse_mode="HTML")
    raise ReturnCommand()
    
markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton(text="Set UPI 💳", callback_data="link_upi"))

PaymentCh = Bot.getData("Botpaychannel") or "not set"

if PaymentCh == "not set":
    # Button create karna taki admin turant set kar sake
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='⚙️ Set Payout Channel', callback_data='/SetBotPayChann'))
    
    # Professional message
    msg = (
        "<b>⛔ No Payout Channel Added!</b>\n\n"
        "<i>Current status: Not set. Please set the payout channel "
        "to enable withdrawals for your users.</i>"
    )
    
    bot.replyText(u, msg, reply_markup=markup, parse_mode="HTML")
    raise ReturnCommand()


refC = Bot.getData(str(u)+"RefCount") or 0
refN = Bot.getData("SetMinRef1") or 0
ChkR = int(refN) - int(refC)

if int(refN) > 0 and int(refC) < int(refN):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=f"You need only {ChkR} refer(s) 🎯", callback_data="Invite Earn 🤑"))
else:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Set UPI 💳", callback_data="link_upi"))

def withdraw():
    upi_id = Bot.getData("UserUPI"+str(u))
    bal = float(libs.Resources.anotherRes('Balance', user=u).value() or 0)

    # Balance check: Agar user ka balance minimum withdrawal limit se kam hai
    if bal < minWith:
        bot.replyText(u, f"<b>🤑 You need a minimum of {minWith} balance to withdraw.</b>", parse_mode="HTML")
        return

    # UPI Check
    if upi_id is None:
        bot.replyText(u, "<b>⚙️ Please set your UPI first to continue!</b>", parse_mode="HTML", reply_markup=markup)
        raise ReturnCommand()

    # Referral Check
    if int(refN) > 0 and int(refC) < int(refN):
        bot.replyText(u, f"<b>🎯 You need {ChkR} more verified refer(s) to unlock withdraw.\n\n👉 Click below to complete & withdraw instantly in your UPI ✓</b>", parse_mode="HTML", reply_markup=markup)
        raise ReturnCommand()

    # Amount puchne se pehle user ko limit dikhayein
    bot.replyText(u, f"<b>💰 Send Total Amount You Wish To Withdraw\n\n📌 Limits: {minWith} - {maxWith}</b>", parse_mode="HTML")
    Bot.handleNextCommand("/PIRO_withdraw1_UPI", options="View")

withdraw()


#======================================================================
# COMMAND: /PIRO_withdrawpayzy
#======================================================================
def escape_html(text):
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PaymentCh = Bot.getData("Botpaychannel") or "not set"
Botpayname = Bot.getData("BotPayComm") or "Payment"
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
Mkey = Bot.getData("API") or "not set"

# Withdrawal command ke andar:
current_gateway = Bot.getData("gatewaynow")
# Dynamic key fetch karein
Token = Bot.getData(f"TOKEN_{current_gateway}") or "not set"

AllBanUsers = (Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u, "<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets = (Bot.getData("AllBanWallets") or "12345").split(",")
wallet = Bot.getData("UserWallet" + str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u, "<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode = Bot.getData("WithdrawMode") or "ON"
if WitdMode == "OFF":
    WOT = Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u, WOT)
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

# 🚫 Ultra Wallet removed from here
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "X": "X lifafa",
    "payzy": "Payzy Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
current_gateway = Bot.getData("gatewaynow")
KEY = Bot.getData(f"KEY_{current_gateway}") or "not set"

Num = Bot.getData("NUM") or "not set"
Key = Bot.getData("KEY") or "not set"

# Parse options
P = options.split("_")
MD = int(P[0])
amount = float(P[1])
bal = float(libs.Resources.anotherRes("Balance", user=u).value())
minWith = float(Bot.getData("MinWith") or 5)
tax = float(Bot.getData("payzytax") or 0)
WithdrawC = int(Bot.getData("WithdrawC") or 0)
wallet = Bot.getData("UserWallet" + str(u)) or "1234567890"
hide_wallet = f"{wallet[0:3]}xxxxx{wallet[8:10]}"
AmountAftrTax = amount - tax

if bal<amount:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text="<b>❌ Withdrawal Failed\n\nReason : Insufficient Balance</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

if amount<minWith:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=f"<b>❌ Withdrawal Failed\n\nReason : Minimum withdrawal is ₹{minWith}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

libs.Resources.anotherRes("Balance",user=u).cut(amount)
Bot.saveData("WithdrawC",WithdrawC+1)

refunded=False

try:
    url=f"https://payzy-gateway.site/api/transfer?token={Token}&number={wallet}&amount={AmountAftrTax}"
    response=HTTP.get(url)
    data=response.json()

    if not isinstance(data,dict):
        data={}

    status=str(data.get("status") or data.get("Status") or data.get("state") or "")
    success=data.get("success") is True or status.lower()=="success"

    error_code=str(
        data.get("error_code")
        or data.get("errorCode")
        or data.get("code")
        or "UNKNOWN"
    )

    gateway_message=str(
        data.get("gateway_message")
        or data.get("gatewayMessage")
        or data.get("message")
        or data.get("msg")
        or data.get("error")
        or data.get("reason")
        or data.get("description")
        or "Unknown error"
    )

    error_code=escape_html(error_code)
    status=escape_html(status)
    gateway_message=escape_html(gateway_message)

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    if success:

        WITHmessage=(
            "<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n"
            "✔️ Please Check Your Payzy Wallet Account!</b>"
        )

        channel_msg=(
            "<b>✅ New Withdrawal Processed ✅</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Payzy Wallet Response: "
            f"<code>{{'status': 'success', 'message': '{gateway_message}', "
            f"'code': 'PPT_200'}}</code></b>"
        )

        # ==========================
        # LIVE FUND DEDUCT
        # ==========================

        try:
            fund=float(Bot.getData("LiveFund") or 0)

            newfund=fund-amount

            if newfund<0:
                newfund=0

            Bot.saveData("LiveFund",newfund)

            channel1=Bot.getData("LiveFundChannel1")
            channel2=Bot.getData("LiveFundChannel2")

            msgid1=Bot.getData("LiveFundMsgID1")
            msgid2=Bot.getData("LiveFundMsgID2")

            try:
                bot_name=Bot.info().username
            except:
                bot_name="Bot"


            # ==========================
            # LIVE FUND TEXT
            # ==========================

            live_text=(
                "<b>✅ Total Remaining Fund In @"
                +str(bot_name)
                +" >> ₹"
                +str(round(newfund,2))
                +"\n\n🚀 This Is A High Fund And Long Term Running Bot With Huge Funds"
                +"\n\n💰💰 Loot As Much As You Can 😎🙏"
                +"\n\n😍 Specially Powered By"
                +"\n@"
                +str(bot_name)
                +" !!</b>"
            )


            # ==========================
            # FUND BUTTON
            # ==========================

            live_button={
                "inline_keyboard":[
                    [
                        {
                            "text":"💰 Fund ₹"+str(round(newfund,2)),
                            "url":"https://t.me/"+str(bot_name)
                        }
                    ]
                ]
            }


            # ==========================
            # CHANNEL 1 UPDATE
            # ==========================

            if channel1 and msgid1:

                try:

                    bot.editMessageText(
                        chat_id=channel1,
                        message_id=int(msgid1),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


            # ==========================
            # CHANNEL 2 UPDATE
            # ==========================

            if channel2 and msgid2:

                try:

                    bot.editMessageText(
                        chat_id=channel2,
                        message_id=int(msgid2),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


        except:
            pass


        # ==========================
        # PAYMENT CHANNEL LOG
        # ==========================

        bot.replyText(
            PaymentCh,
            channel_msg,
            parse_mode="HTML"
        )

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=WITHmessage,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        libs.Resources.anotherRes("Withdraw",user=u).add(amount)
        libs.Resources.globalRes("BotWithdraws").add(amount)

    else:

        libs.Resources.anotherRes("Balance",user=u).add(amount)
        refunded=True

        balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

        channel_msg=(
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Payzy Wallet Response: "
            f"<code>{{'status': 'failed', 'message': '{gateway_message}', "
            f"'code': 'PPT_000'}}</code></b>"
        )

        bot.replyText(PaymentCh,channel_msg,parse_mode="HTML")

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=(
                "<b>❌ Withdrawal Failed\n\n"
                f"⚠️ Reason : <code>{gateway_message}</code></b>"
            ),
            parse_mode="HTML"
        )

except Exception as e:

    if not refunded:
        libs.Resources.anotherRes("Balance",user=u).add(amount)

    error_msg=escape_html(str(e))

    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=(
            "<b>❌ Withdrawal Failed\n\n"
            f"⚠️ Reason : <code>{error_msg}</code></b>"
        ),
        parse_mode="HTML"
    )

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    bot.replyText(
        PaymentCh,
        (
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Payzy Wallet Response: "
            f"<code>{{'status': 'failed', 'message': 'Timeout Or Invalid Response', 'code': 'ERROR'}}</code></b>"
        ),
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /PIRO_withdrawu
#======================================================================
def escape_html(text):
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PaymentCh = Bot.getData("Botpaychannel") or "not set"
Botpayname = Bot.getData("BotPayComm") or "Payment"
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
Mkey = Bot.getData("API") or "not set"
# Withdrawal command ke andar:
current_gateway = Bot.getData("gatewaynow")
# Dynamic key fetch karein
Token = Bot.getData(f"TOKEN_{current_gateway}") or "not set"

AllBanUsers = (Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u, "<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets = (Bot.getData("AllBanWallets") or "12345").split(",")
wallet = Bot.getData("UserWallet" + str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u, "<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode = Bot.getData("WithdrawMode") or "ON"
if WitdMode == "OFF":
    WOT = Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u, WOT)
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "X": "X lifafa",
    "ultra": "Ultra Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
# Withdrawal script ke andar:
current_gateway = Bot.getData("gatewaynow")
KEY = Bot.getData(f"KEY_{current_gateway}") or "not set"

Num = Bot.getData("NUM") or "not set"
Key = Bot.getData("KEY") or "not set"
# Parse options
P = options.split("_")
MD = int(P[0])
amount = float(P[1])
bal = float(libs.Resources.anotherRes("Balance", user=u).value())
minWith = float(Bot.getData("MinWith") or 5)
tax = float(Bot.getData("ultratax") or 0)
WithdrawC = int(Bot.getData("WithdrawC") or 0)
wallet = Bot.getData("UserWallet" + str(u)) or "1234567890"
hide_wallet = f"{wallet[0:3]}xxxxx{wallet[8:10]}"
AmountAftrTax = amount - tax

if bal<amount:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text="<b>❌ Withdrawal Failed\n\nReason : Insufficient Balance</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

if amount<minWith:
    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=f"<b>❌ Withdrawal Failed\n\nReason : Minimum withdrawal is ₹{minWith}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

libs.Resources.anotherRes("Balance",user=u).cut(amount)
Bot.saveData("WithdrawC",WithdrawC+1)

refunded=False

try:
    url=f"https://ultra-pay.in/APIs/api?token={Token}&key={KEY}&paytoNumber={wallet}&amount={AmountAftrTax}&comment={Botpayname}"
    response=HTTP.get(url)
    data=response.json()

    if not isinstance(data,dict):
        data={}

    status=str(data.get("status") or data.get("Status") or data.get("state") or "")
    success=data.get("success") is True or status.lower()=="success"

    error_code=str(
        data.get("error_code")
        or data.get("errorCode")
        or data.get("code")
        or "UNKNOWN"
    )

    gateway_message=str(
        data.get("gateway_message")
        or data.get("gatewayMessage")
        or data.get("message")
        or data.get("msg")
        or data.get("error")
        or data.get("reason")
        or data.get("description")
        or "Unknown error"
    )

    error_code=escape_html(error_code)
    status=escape_html(status)
    gateway_message=escape_html(gateway_message)

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    if success:

        WITHmessage=(
            "<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n"
            "✔️ Please Check Your Ultra Wallet Account!</b>"
        )

        channel_msg=(
            "<b>✅ New Withdrawal Processed ✅</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Ultra Wallet Response: "
            f"<code>{{'status': 'success', 'message': '{gateway_message}', "
            f"'code': 'PPT_200'}}</code></b>"
        )

        # ==========================
        # LIVE FUND DEDUCT
        # ==========================

        try:
            fund=float(Bot.getData("LiveFund") or 0)

            newfund=fund-amount

            if newfund<0:
                newfund=0

            Bot.saveData("LiveFund",newfund)

            channel1=Bot.getData("LiveFundChannel1")
            channel2=Bot.getData("LiveFundChannel2")

            msgid1=Bot.getData("LiveFundMsgID1")
            msgid2=Bot.getData("LiveFundMsgID2")

            try:
                bot_name=Bot.info().username
            except:
                bot_name="Bot"


            # ==========================
            # LIVE FUND TEXT
            # ==========================

            live_text=(
                "<b>✅ Total Remaining Fund In @"
                +str(bot_name)
                +" >> ₹"
                +str(round(newfund,2))
                +"\n\n🚀 This Is A High Fund And Long Term Running Bot With Huge Funds"
                +"\n\n💰💰 Loot As Much As You Can 😎🙏"
                +"\n\n😍 Specially Powered By"
                +"\n@"
                +str(bot_name)
                +" !!</b>"
            )


            # ==========================
            # FUND BUTTON
            # ==========================

            live_button={
                "inline_keyboard":[
                    [
                        {
                            "text":"💰 Fund ₹"+str(round(newfund,2)),
                            "url":"https://t.me/"+str(bot_name)
                        }
                    ]
                ]
            }


            # ==========================
            # CHANNEL 1 UPDATE
            # ==========================

            if channel1 and msgid1:

                try:

                    bot.editMessageText(
                        chat_id=channel1,
                        message_id=int(msgid1),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


            # ==========================
            # CHANNEL 2 UPDATE
            # ==========================

            if channel2 and msgid2:

                try:

                    bot.editMessageText(
                        chat_id=channel2,
                        message_id=int(msgid2),
                        text=live_text,
                        parse_mode="HTML",
                        reply_markup=live_button
                    )

                except:
                    pass


        except:
            pass


        # ==========================
        # PAYMENT CHANNEL LOG
        # ==========================

        bot.replyText(
            PaymentCh,
            channel_msg,
            parse_mode="HTML"
        )

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=WITHmessage,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

        libs.Resources.globalRes("BotWithdrawsuccess").add(amount)
        libs.Resources.anotherRes("Withdraw",user=u).add(amount)
        libs.Resources.globalRes("BotWithdraws").add(amount)

    else:

        libs.Resources.anotherRes("Balance",user=u).add(amount)
        refunded=True

        balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

        channel_msg=(
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Ultra Wallet Response: "
            f"<code>{{'status': 'failed', 'message': '{gateway_message}', "
            f"'code': 'PPT_000'}}</code></b>"
        )

        bot.replyText(PaymentCh,channel_msg,parse_mode="HTML")

        bot.editMessageText(
            chat_id=u,
            message_id=MD,
            text=(
                "<b>❌ Withdrawal Failed\n\n"
                f"⚠️ Reason : <code>{gateway_message}</code></b>"
            ),
            parse_mode="HTML"
        )

except Exception as e:

    if not refunded:
        libs.Resources.anotherRes("Balance",user=u).add(amount)

    error_msg=escape_html(str(e))

    bot.editMessageText(
        chat_id=u,
        message_id=MD,
        text=(
            "<b>❌ Withdrawal Failed\n\n"
            f"⚠️ Reason : <code>Timeout Or Invalid Response</code></b>"
        ),
        parse_mode="HTML"
    )

    usr=f'<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>'
    balance_now=float(libs.Resources.anotherRes("Balance",user=u).value())

    bot.replyText(
        PaymentCh,
        (
            "<b>❌ New Withdrawal Failed &amp; Refunded ❌</b>\n\n"
            f"<b>🟢 User : {usr}</b>\n"
            f"<b>🤑 Remaining Balance :- {balance_now}</b>\n\n"
            f"<b>🚀 Amount : {amount} INR (-)</b>\n"
            f"<b>⛔ Address : <code>{hide_wallet}</code></b>\n\n"
            f"<b>🤖 Bot: @{Bot.info().username}</b>\n\n"
            f"<b>⚠️ Ultra Wallet Response: "
            f"<code>{{'status': 'failed', 'message': 'Timeout Or Invalid Response', 'code': 'ERROR'}}</code></b>"
        ),
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /Payzywalletsele
#======================================================================
# Command name :+ /Payzywallet

# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# --- MINIMAL CHANGE START: Multiple Selection Logic ---
# Baaki gateways ko False karne ki jagah, sirf VSV ka status toggle (invert) hoga
current_payzy_status = Bot.getData("payzy")
new_payzy_status = False if current_payzy_status else True
Bot.saveData("payzy", new_payzy_status)

# Current global gateway configuration (Aapki dynamic requirements ke liye)
if new_payzy_status:
    Bot.saveData("gatewaynow", "payzy")
    Bot.saveData("gatewaytype", "http://payzy-gateway.site")
# Sabhi gateways ka latest status database se check karne ke liye helper function
def get_status(key):
    return "✅" if Bot.getData(key) else "❌"

# Sabhi gateways ka live status fetch karna
rj = get_status("rj")
info = get_status("info")
vsv = get_status("vsv")
payzy = get_status("payzy")
fxl = get_status("Fxl")
tg = get_status("Tgwallet")
RDX = get_status("RDX")
X = get_status("X")
E = get_status("e")
sa = get_status("sa")
ultra = get_status("ultra")
unio = get_status("unio")
# --- MINIMAL CHANGE END ---

# Inline Keyboard (Ab yeh static cross/check ki jagah dynamic live status dikhaega)
markup = {
    "inline_keyboard": [
        [
            {"text": "Infotech Wallet", "callback_data": "/none"},
            {"text": info, "callback_data": "/inwalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": vsv, "callback_data": "/Vsvwalletsele0"}
        ],
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": payzy, "callback_data": "/Payzywalletsele"}
        ],
        [
            {"text": "FXL Wallet", "callback_data": "/none"},
            {"text": fxl, "callback_data": "/Fxlwalletsele0"}
        ],
        [
            {"text": "TG Wallet", "callback_data": "/none"},
            {"text": tg, "callback_data": "/Tgwalletsele0"}
        ],
        [
            {"text": "RDX Wallet", "callback_data": "/none"},
            {"text": RDX, "callback_data": "/RDXwalletsele0"}
        ],
        [
            {"text": "X Wallet", "callback_data": "/none"},
            {"text": X, "callback_data": "/Xwalletsele0"}
        ],
        [
            {"text": "RJ Wallet", "callback_data": "/none"},
            {"text": rj, "callback_data": "/rjwalletsele0"}
        ],
        [
            {"text": "E Wallet", "callback_data": "/none"},
            {"text": E, "callback_data": "/ewalletsele0"}
        ],
        [
            {"text": "Saathi Gateway", "callback_data": "/none"},
            {"text": sa, "callback_data": "/sawalletsele0"}
        ],
        [
            {"text": "Ultra Wallet", "callback_data": "/none"},
            {"text": ultra, "callback_data": "/ultrawalletsele0"}
        ],
        [
            {"text": "Unio Wallet", "callback_data": "/none"},
            {"text": unio, "callback_data": "/uniowalletsele0"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
status_text = "Active ✅" if new_payzy_status else "Inactive ❌"
bot.replyText(u, f"<b><i>🔄 Payzy Wallet is {status_text} Now!</i></b>")


#======================================================================
# COMMAND: /Perfom_Stats
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


markup = InlineKeyboardMarkup()

markup.add(InlineKeyboardButton(text=' 🏆Leaderboard',callback_data='/TopReferral'))

markup.add(InlineKeyboardButton(text=' Top Bal',callback_data='/TopBalance'),InlineKeyboardButton(text='Raw Stats',callback_data='/RawStats'))

markup.add(InlineKeyboardButton(text=' Most Withdrawals (UPI) ',callback_data='/TopWithdraw_UPI'))

markup.add(InlineKeyboardButton(text=' Top Promoters',callback_data='/TopWithdraws'))

markup.add(InlineKeyboardButton(text='Added Links',callback_data='/PIRO_ChLinks'))


markup.add(InlineKeyboardButton(text=' Add Balance Text',callback_data='/AddBalTxt'))

markup.add(InlineKeyboardButton(text='🔙Back',callback_data='/admin AP'))


TXT="<b>📊 Here You Can View Leaderboard & Metrics 🏆</b>"
try:
    bot.editMessageText(chat_id=u, message_id=message.message_id,text=TXT,reply_markup=markup)
except:
    pass
        
#bot.replyText(u,TXT,reply_markup=markup)


#======================================================================
# COMMAND: /RC_Change
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Owner_Here
# [ DM TO BUY ANY BOTS & CODES ]

# ==============================
# ADMIN CHECK
# ==============================

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# CALLBACK DATA
# ==============================

P = []

if params:
    P = str(params).split("_")

if options:
    P = str(options).split("_")


if len(P) < 2:
    bot.replyText(
        u,
        "<b>❌ Invalid Gift Code Action</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


ACTION = str(P[0])
RC = str(P[1]).strip()


# ==============================
# ALL CODES
# ==============================

All_BRC = Bot.getData("All_BRC") or []
All_BRC = [str(x) for x in All_BRC]


if RC not in All_BRC:

    try:
        bot.answerCallbackQuery(
            callback_query_id=call.id,
            text="❌ Gift Code Not Found",
            show_alert=True
        )
    except:
        pass

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


# ==============================
# INFO
# ==============================

if ACTION == "info":

    ABC = Bot.getData(
        "GiftCode" + RC + "isAMT"
    )

    if not ABC or len(ABC) < 2:
        Bot.runCommand("/PIRO_RC_Pannel")
        raise ReturnCommand()


    MxC = Bot.getData(
        "Gift" + RC + "MaxUsrCanClaim"
    ) or 0

    C = Bot.getData(
        "Gift" + RC + "CountOfClaimedUsrs"
    ) or 0

    MinRef = Bot.getData(
        "Gift" + RC + "MinRef"
    ) or 0

    Status = Bot.getData(
        "Gift" + RC + "KaStatus"
    ) or "Active"


    if Status == "Active":
        StatusText = "🟢 Aᴄᴛɪᴠᴇ"
        StatusCallback = "🟢"
    else:
        StatusText = "🔴 Dᴇᴀᴄᴛɪᴠᴇ"
        StatusCallback = "🔴"


    markup = InlineKeyboardMarkup()


    markup.add(
        InlineKeyboardButton(
            text="✏️ Rᴇɴᴀᴍᴇ Gɪғᴛ Cᴏᴅᴇ",
            callback_data="/RC_Edit Rename_" + RC
        )
    )


    markup.add(
        InlineKeyboardButton(
            text="👥 Eᴅɪᴛ Tᴏᴛᴀʟ Uѕᴇʀѕ",
            callback_data="/RC_Edit MxUsr_" + RC
        )
    )


    markup.add(
        InlineKeyboardButton(
            text="💸 Eᴅɪᴛ Aᴍᴏᴜɴᴛ",
            callback_data="/RC_Edit Amt_" + RC
        )
    )


    markup.add(
        InlineKeyboardButton(
            text="🎯 Eᴅɪᴛ Mɪɴ. Rᴇғᴇʀ",
            callback_data="/RC_Edit MinRef_" + RC
        )
    )


    markup.add(
    InlineKeyboardButton(
        text="👥 Cʟᴀɪᴍᴇᴅ Uѕᴇʀѕ",
        callback_data="/RC_ClaimedUsers " + RC
    )
)

    markup.add(
        InlineKeyboardButton(
            text="🔙 Bᴀᴄᴋ",
            callback_data="/PIRO_RC_Pannel"
        )
    )


    TXT = f"""<b>🎁 Gɪғᴛ Cᴏᴅᴇ Iɴғᴏ

🔑 Cᴏᴅᴇ: <code>{RC}</code>

📤 Cʟᴀɪᴍᴇᴅ: {C} / {MxC}
💸 Pᴇʀ Uѕᴇʀ: ₹{ABC[1]}
🎯 Mɪɴ. Rᴇғᴇʀ: {MinRef}
📊 Sᴛᴀᴛᴜs: {StatusText}</b>"""


    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

    raise ReturnCommand()


# ==============================
# DELETE
# ==============================

# ==============================
# DELETE
# ==============================

if ACTION == "delete":

    RC = str(P[1]).strip()

    All_BRC = Bot.getData("All_BRC") or []
    All_BRC = [str(x) for x in All_BRC]

    # ==============================
    # CHECK CODE EXISTS
    # ==============================

    if RC not in All_BRC:

        try:
            bot.answerCallbackQuery(
                call.id,
                "❌ Gift Code Already Deleted",
                show_alert=True
            )
        except:
            pass

        raise ReturnCommand()


    # ==============================
    # GET CLAIMED USERS BEFORE DELETE
    # ==============================

    ClaimedUsers = Bot.getData(
        "UsrsClaimedBotRC" + RC
    ) or []


    # ==============================
    # DELETE FROM ALL_BRC
    # ==============================

    New_BRC = []

    for CODE in All_BRC:

        if str(CODE) != RC:
            New_BRC.append(str(CODE))

    Bot.saveData("All_BRC", New_BRC)


    # ==============================
    # DELETE GIFT CODE DATA
    # ==============================

    Bot.deleteData(
        "GiftCode" + RC + "isAMT"
    )

    Bot.deleteData(
        "Gift" + RC + "MaxUsrCanClaim"
    )

    Bot.deleteData(
        "Gift" + RC + "CountOfClaimedUsrs"
    )

    Bot.deleteData(
        "Gift" + RC + "MinRef"
    )

    Bot.deleteData(
        "Gift" + RC + "KaStatus"
    )


    # ==============================
    # DELETE CLAIMED USER STATUSES
    # ==============================

    for user_id in ClaimedUsers:

        try:

            Bot.deleteData(
                str(user_id) + "Gift" + RC + "stat"
            )

        except:
            pass


    # Delete claimed users list
    Bot.deleteData(
        "UsrsClaimedBotRC" + RC
    )


    # ==============================
    # ADMIN ACTIVITY
    # ==============================

    AdmAC = Bot.getData("AdmAC") or []

    now = libs.DateAndTime.now("Asia/Kolkata")

    date = now["date"]
    time = now["time"][:5]

    year, month, day = date.split("-")

    hour, minute = time.split(":")

    hour = int(hour)

    ampm = "am"

    if hour >= 12:
        ampm = "pm"

    if hour > 12:
        hour -= 12

    if hour == 0:
        hour = 12

    MONTHS = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }

    EasyTime = (
        f"{int(day)} {MONTHS[month]}, "
        f"{hour:02}:{minute} {ampm}"
    )

    act = f"Gift Code ({RC}) Deleted Permanently"

    AdmAC.append(
        f"""<b>📆 Time:</b> {EasyTime}
👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]
🔍 <b>Action:</b> {act}"""
    )

    Bot.saveData("AdmAC", AdmAC)


    # ==============================
    # REAL-TIME PANEL UPDATE
    # ==============================

    markup = InlineKeyboardMarkup()


    if not New_BRC:

        markup.add(
            InlineKeyboardButton(
                text="➕ Cʀᴇᴀᴛᴇ Nᴇᴡ",
                callback_data="/creating_NwRC"
            )
        )

    else:

        for CODE in New_BRC:

            CODE = str(CODE)

            Status = Bot.getData(
                "Gift" + CODE + "KaStatus"
            ) or "Active"

            Emoji = "🟢" if Status == "Active" else "🔴"

            markup.row(
                InlineKeyboardButton(
                    text=CODE,
                    callback_data="/RC_Change info_" + CODE
                ),

                InlineKeyboardButton(
                    text="🗑",
                    callback_data="/RC_Change delete_" + CODE
                ),

                InlineKeyboardButton(
                    text=Emoji,
                    callback_data="/RC_Change " + Emoji + "_" + CODE
                )
            )


        markup.add(
            InlineKeyboardButton(
                text="➕ Cʀᴇᴀᴛᴇ Nᴇᴡ",
                callback_data="/creating_NwRC"
            )
        )


    # Claimed Text MUST remain permanent
    markup.add(
        InlineKeyboardButton(
            text="📝 Cʟᴀɪᴍᴇᴅ Tᴇxᴛ",
            callback_data="/RC_claimedText"
        )
    )


    markup.add(
        InlineKeyboardButton(
            text="🔙 Bᴀᴄᴋ",
            callback_data="/admin AP"
        )
    )


    TXT = f"""<b>🎁 Gɪғᴛ Cᴏᴅᴇ Mᴀɴᴀɢᴇʀ

📊 Tᴏᴛᴀʟ Gɪғᴛ Cᴏᴅᴇs: {len(New_BRC)}

👇 Sᴇʟᴇᴄᴛ A Gɪғᴛ Cᴏᴅᴇ Tᴏ Mᴀɴᴀɢᴇ Iᴛ.</b>"""


    # ==============================
    # EDIT SAME MESSAGE
    # ==============================

    try:

        bot.editMessageText(
            chat_id=u,
            message_id=message.message_id,
            text=TXT,
            reply_markup=markup,
            parse_mode="HTML"
        )

    except:

        try:

            bot.replyText(
                u,
                TXT,
                reply_markup=markup,
                parse_mode="HTML"
            )

        except:
            pass


    raise ReturnCommand()


# ==============================
# ACTIVATE
# ==============================

if ACTION == "🔴":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Active"
    )

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


# ==============================
# DEACTIVATE
# ==============================

if ACTION == "🟢":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Deactive"
    )

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


raise ReturnCommand()


#======================================================================
# COMMAND: /RC_ClaimedUsers
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GET GIFT CODE
# ==============================

RC = str(params).strip()

if RC.startswith("/RC_ClaimedUsers"):
    RC = RC.replace("/RC_ClaimedUsers", "", 1).strip()

RC = RC.strip("_ ")


# ==============================
# CHECK CODE
# ==============================

All_BRC = Bot.getData("All_BRC") or []
All_BRC = [str(x) for x in All_BRC]

if RC not in All_BRC:
    bot.replyText(
        u,
        "<b>❌ This Gift Code Does Not Exist.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GET CLAIMED USERS
# ==============================

ClaimedUsers = Bot.getData(
    "UsrsClaimedBotRC" + RC
) or []


# Remove duplicate users
CleanUsers = []

for user_id in ClaimedUsers:

    user_id = str(user_id)

    if user_id not in CleanUsers:
        CleanUsers.append(user_id)

ClaimedUsers = CleanUsers


# ==============================
# NO CLAIMED USERS
# ==============================

if not ClaimedUsers:

    TXT = f"""<b>👥 Claimed Users

🎁 Gift Code: <code>{RC}</code>

📊 Total Claimed: 0

🤷‍♂️ No User Has Claimed This Gift Code Yet.</b>"""


# ==============================
# CLAIMED USERS
# ==============================

else:

    TXT = f"""<b>👥 Claimed Users

🎁 Gift Code: <code>{RC}</code>
📊 Total Claimed: {len(ClaimedUsers)}

━━━━━━━━━━━━━━</b>

"""

    count = 0

    for user_id in ClaimedUsers:

        count += 1
        user_id = str(user_id)

        # ==============================
        # GET USER NAME
        # ==============================

        first_name = "User"

        try:
            chat_info = bot.getChat(user_id)

            if chat_info:
                first_name = str(
                    chat_info.first_name or "User"
                )

        except:
            pass

        # Escape HTML characters
        first_name = (
            first_name
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

        TXT += (
            f'<b>{count}.</b> '
            f'<a href="tg://user?id={user_id}">'
            f'👤 {first_name}</a> '
            f'<b>[{user_id}]</b>\n'
        )

# ==============================
# BACK BUTTON
# ==============================

markup = InlineKeyboardMarkup()

markup.add(
    InlineKeyboardButton(
        text="🔙 Back",
        callback_data="/PIRO_RC_Pannel"
    )
)


# ==============================
# DISPLAY
# ==============================

try:

    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

except:

    bot.replyText(
        u,
        TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

raise ReturnCommand()


#======================================================================
# COMMAND: /RC_Edit
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Owner_Here

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GET PARAMETERS
# ==============================

P = str(params or "").split("_")

if len(P) < 2:
    raise ReturnCommand()

EDIT = P[0]
RC = str(P[1]).strip()


# ==============================
# CHECK CODE STILL EXISTS
# ==============================

All_BRC = Bot.getData("All_BRC") or []
All_BRC = [str(x) for x in All_BRC]

if RC not in All_BRC:

    bot.replyText(
        u,
        "<b>❌ This Gift Code No Longer Exists.</b>",
        parse_mode="HTML"
    )

    raise ReturnCommand()


# ==============================
# MAX USERS
# ==============================

if EDIT == "MxUsr":

    bot.replyText(
        u,
        f"""<b>👥 Edit Total Users

🎁 Gift Code: <code>{RC}</code>

Send The New Maximum User Limit:</b>""",
        parse_mode="HTML"
    )

    Bot.handleNextCommand(
        "/RC_Edit1",
        options="MxUsr_" + RC
    )

    raise ReturnCommand()


# ==============================
# AMOUNT
# ==============================

if EDIT == "Amt":

    bot.replyText(
        u,
        f"""<b>💸 Edit Amount

🎁 Gift Code: <code>{RC}</code>

Send The New Amount:</b>""",
        parse_mode="HTML"
    )

    Bot.handleNextCommand(
        "/RC_Edit1",
        options="Amt_" + RC
    )

    raise ReturnCommand()


# ==============================
# MINIMUM REFERRALS
# ==============================

if EDIT == "MinRef":

    bot.replyText(
        u,
        f"""<b>🎯 Edit Minimum Referrals

🎁 Gift Code: <code>{RC}</code>

Send The New Minimum Verified Refers:</b>""",
        parse_mode="HTML"
    )

    Bot.handleNextCommand(
        "/RC_Edit1",
        options="MinRef_" + RC
    )

    raise ReturnCommand()


# ==============================
# RENAME
# ==============================

if EDIT == "Rename":

    bot.replyText(
        u,
        f"""<b>✏️ Rename Gift Code

Current Code:
<code>{RC}</code>

Send The New Code Name:</b>""",
        parse_mode="HTML"
    )

    Bot.handleNextCommand(
        "/RC_Edit1",
        options="Rename_" + RC
    )

    raise ReturnCommand()


# ==============================
# ACTIVE / INACTIVE
# ==============================

if EDIT == "🟢Active":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Deactive"
    )

    Bot.runCommand("/PIRO_RC_Pannel")

    raise ReturnCommand()


if EDIT == "🔴Not Active":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Active"
    )

    Bot.runCommand("/PIRO_RC_Pannel")

    raise ReturnCommand()


# ==============================
# ALSO SUPPORT SIMPLE EMOJIS
# ==============================

if EDIT == "🟢":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Deactive"
    )

    Bot.runCommand("/PIRO_RC_Pannel")

    raise ReturnCommand()


if EDIT == "🔴":

    Bot.saveData(
        "Gift" + RC + "KaStatus",
        "Active"
    )

    Bot.runCommand("/PIRO_RC_Pannel")

    raise ReturnCommand()


raise ReturnCommand()


#======================================================================
# COMMAND: /RC_Edit1
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Owner_Here

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


P = str(options).split("_")

if len(P) < 2:
    raise ReturnCommand()

EDIT = P[0]
RC = str(P[1])


# ==============================
# CHECK CODE
# ==============================

All_BRC = Bot.getData("All_BRC") or []
All_BRC = [str(x) for x in All_BRC]

if RC not in All_BRC:

    bot.replyText(
        u,
        "<b>❌ This Gift Code Was Deleted.</b>",
        parse_mode="HTML"
    )

    raise ReturnCommand()


VALUE = str(message.text).strip()


# ==============================
# MAX USERS
# ==============================

if EDIT == "MxUsr":

    if not VALUE.isdigit() or int(VALUE) <= 0:
        bot.replyText(
            u,
            "<b>❌ Enter A Valid User Limit.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()

    OLD = Bot.getData(
        "Gift" + RC + "MaxUsrCanClaim"
    ) or 0

    Bot.saveData(
        "Gift" + RC + "MaxUsrCanClaim",
        int(VALUE)
    )

    bot.replyText(
        u,
        f"""<b>✅ User Limit Updated

🎁 Gift Code: <code>{RC}</code>
👥 New Limit: {VALUE}</b>""",
        parse_mode="HTML"
    )

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


# ==============================
# AMOUNT
# ==============================

if EDIT == "Amt":

    try:
        AMT = float(VALUE)
    except:
        bot.replyText(
            u,
            "<b>❌ Enter A Valid Amount.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    if AMT <= 0:
        bot.replyText(
            u,
            "<b>❌ Amount Must Be Greater Than 0.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    OLD = Bot.getData(
        "GiftCode" + RC + "isAMT"
    ) or [RC, 0]

    Bot.saveData(
        "GiftCode" + RC + "isAMT",
        [RC, str(VALUE)]
    )

    bot.replyText(
        u,
        f"""<b>✅ Amount Updated

🎁 Gift Code: <code>{RC}</code>
💸 New Amount: ₹{VALUE}</b>""",
        parse_mode="HTML"
    )

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


# ==============================
# MINIMUM REFERRALS
# ==============================

if EDIT == "MinRef":

    if not VALUE.isdigit() or int(VALUE) < 0:
        bot.replyText(
            u,
            "<b>❌ Enter A Valid Referral Number.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    Bot.saveData(
        "Gift" + RC + "MinRef",
        int(VALUE)
    )

    bot.replyText(
        u,
        f"""<b>✅ Minimum Referrals Updated

🎁 Gift Code: <code>{RC}</code>
🎯 New Min. Refers: {VALUE}</b>""",
        parse_mode="HTML"
    )

    Bot.runCommand("/PIRO_RC_Pannel")
    raise ReturnCommand()


# ==============================
# RENAME
# ==============================

# ==============================
# RENAME GIFT CODE
# ==============================

if EDIT == "Rename":

    NewRC = str(message.text).strip()

    if len(NewRC) < 1 or len(NewRC) > 50:
        bot.replyText(
            u,
            "<b>❌ Gift Code Name Must Be 1–50 Characters.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    if NewRC == RC:

        bot.replyText(
            u,
            "<b>❌ New Name Is Same As Current Name.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    if NewRC in All_BRC:

        bot.replyText(
            u,
            "<b>❌ This Gift Code Name Already Exists.</b>",
            parse_mode="HTML"
        )
        raise ReturnCommand()


    # ==============================
    # GET OLD DATA
    # ==============================

    ABC = Bot.getData(
        "GiftCode" + RC + "isAMT"
    ) or [RC, 0]

    MaxUsr = Bot.getData(
        "Gift" + RC + "MaxUsrCanClaim"
    ) or 0

    Claimed = Bot.getData(
        "Gift" + RC + "CountOfClaimedUsrs"
    ) or 0

    MinRef = Bot.getData(
        "Gift" + RC + "MinRef"
    ) or 0

    Status = Bot.getData(
        "Gift" + RC + "KaStatus"
    ) or "Active"

    ClaimedUsers = Bot.getData(
        "UsrsClaimedBotRC" + RC
    ) or []


    # ==============================
    # SAVE NEW CODE DATA
    # ==============================

    Bot.saveData(
        "GiftCode" + NewRC + "isAMT",
        [NewRC, str(ABC[1])]
    )

    Bot.saveData(
        "Gift" + NewRC + "MaxUsrCanClaim",
        MaxUsr
    )

    Bot.saveData(
        "Gift" + NewRC + "CountOfClaimedUsrs",
        Claimed
    )

    Bot.saveData(
        "Gift" + NewRC + "MinRef",
        MinRef
    )

    Bot.saveData(
        "Gift" + NewRC + "KaStatus",
        Status
    )

    Bot.saveData(
        "UsrsClaimedBotRC" + NewRC,
        ClaimedUsers
    )


    # ==============================
    # MOVE USER CLAIM STATUS
    # ==============================

    for user_id in ClaimedUsers:

        old_key = (
            str(user_id)
            + "Gift"
            + RC
            + "stat"
        )

        new_key = (
            str(user_id)
            + "Gift"
            + NewRC
            + "stat"
        )

        old_status = Bot.getData(old_key)

        if old_status is not None:

            Bot.saveData(
                new_key,
                old_status
            )

            Bot.deleteData(old_key)


    # ==============================
    # UPDATE ALL_BRC
    # ==============================

    NewList = []

    for CODE in All_BRC:

        if str(CODE) == RC:
            NewList.append(NewRC)
        else:
            NewList.append(str(CODE))

    Bot.saveData(
        "All_BRC",
        NewList
    )


    # ==============================
    # DELETE OLD MAIN DATA
    # ==============================

    Bot.deleteData(
        "GiftCode" + RC + "isAMT"
    )

    Bot.deleteData(
        "Gift" + RC + "MaxUsrCanClaim"
    )

    Bot.deleteData(
        "Gift" + RC + "CountOfClaimedUsrs"
    )

    Bot.deleteData(
        "Gift" + RC + "MinRef"
    )

    Bot.deleteData(
        "Gift" + RC + "KaStatus"
    )

    Bot.deleteData(
        "UsrsClaimedBotRC" + RC
    )


    # ==============================
    # SUCCESS
    # ==============================

    bot.replyText(
        u,
        f"""<b>✅ Gift Code Renamed Successfully

🎁 Old Name:
{RC}

🎁 New Name:
{NewRC}

👥 Claimed Users: {Claimed}
🎯 Minimum Refers: {MinRef}
💸 Amount: ₹{ABC[1]}
📊 User Limit: {MaxUsr}</b>""",
        parse_mode="HTML"
    )

    Bot.runCommand("/PIRO_RC_Pannel")

    raise ReturnCommand()


#======================================================================
# COMMAND: /RC_SaveMinRef
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    raise ReturnCommand()

RC = str(options).strip()
NewMinRef = message.text.strip()

if not NewMinRef.isdigit():
    bot.replyText(
        u,
        "<b>❌ Please Send A Valid Number.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

NewMinRef = int(NewMinRef)

if NewMinRef < 0:
    bot.replyText(
        u,
        "<b>❌ Minimum Referrals Cannot Be Negative.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

Bot.saveData(
    "Gift" + RC + "MinRef",
    NewMinRef
)

Bot.runCommand("/PIRO_RC_Pannel")
raise ReturnCommand()


#======================================================================
# COMMAND: /RC_SaveRename
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    raise ReturnCommand()

OldRC = str(options).strip()
NewRC = message.text.strip().upper()

if not NewRC.isalnum() or len(NewRC) < 3:
    bot.replyText(
        u,
        "<b>❌ Invalid Gift Code Name.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

All_BRC = Bot.getData("All_BRC") or []
All_BRC = [str(x) for x in All_BRC]

if NewRC in All_BRC and NewRC != OldRC:
    bot.replyText(
        u,
        "<b>❌ This Gift Code Already Exists.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# COPY EXISTING DATA
# ==============================

ABC = Bot.getData(
    "GiftCode" + OldRC + "isAMT"
)

if not ABC:
    raise ReturnCommand()


MaxUsr = Bot.getData(
    "Gift" + OldRC + "MaxUsrCanClaim"
) or 0

Claimed = Bot.getData(
    "Gift" + OldRC + "CountOfClaimedUsrs"
) or 0

MinRef = Bot.getData(
    "Gift" + OldRC + "MinRef"
) or 0

Status = Bot.getData(
    "Gift" + OldRC + "KaStatus"
) or "Active"


Bot.saveData(
    "GiftCode" + NewRC + "isAMT",
    [NewRC, str(ABC[1])]
)

Bot.saveData(
    "Gift" + NewRC + "MaxUsrCanClaim",
    MaxUsr
)

Bot.saveData(
    "Gift" + NewRC + "CountOfClaimedUsrs",
    Claimed
)

Bot.saveData(
    "Gift" + NewRC + "MinRef",
    MinRef
)

Bot.saveData(
    "Gift" + NewRC + "KaStatus",
    Status
)


# ==============================
# REPLACE IN ALL CODES
# ==============================

NewList = []

for code in All_BRC:

    if str(code) == OldRC:
        NewList.append(NewRC)
    else:
        NewList.append(str(code))

Bot.saveData(
    "All_BRC",
    NewList
)


# ==============================
# REMOVE OLD DATA
# ==============================

Bot.deleteData("GiftCode" + OldRC + "isAMT")
Bot.deleteData("Gift" + OldRC + "MaxUsrCanClaim")
Bot.deleteData("Gift" + OldRC + "CountOfClaimedUsrs")
Bot.deleteData("Gift" + OldRC + "MinRef")
Bot.deleteData("Gift" + OldRC + "KaStatus")


Bot.runCommand("/PIRO_RC_Pannel")
raise ReturnCommand()


#======================================================================
# COMMAND: /RC_claimedText
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Owner_Here
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(userid) for userid in AllBotAdminss]:
    bot.replyText(
        u,
        "<b>🚫 You Are Not This Bot Admin</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


keyboard = ReplyKeyboardMarkup(True)
keyboard.row("⛔ Cancel")

bot.replyText(
    u,
    """Send The Text To Edit

💡 Tip: You can use {Bonus} in your text, and it will automatically be replaced with the redeem code amount!""",
    parse_mode="HTML",
    reply_markup=keyboard
)

Bot.handleNextCommand("/RC_claimedText1")

raise ReturnCommand()


#======================================================================
# COMMAND: /RC_claimedText1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# CANCEL
# ==============================

if message.text == "⛔ Cancel":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options="<b>⛔ Cancelled Successfully</b>"
    )

    raise ReturnCommand()


# ==============================
# SAVE CLAIM TEXT
# ==============================

Bot.saveData("RCT", message.text)


# ==============================
# ADMIN ACTIVITY
# ==============================

now = libs.DateAndTime.now("Asia/Kolkata")

date = now["date"]
time = now["time"][:5]

year, month, day = date.split("-")
hour, minute = time.split(":")

hour = int(hour)

ampm = "am"

if hour >= 12:
    ampm = "pm"

if hour > 12:
    hour -= 12

if hour == 0:
    hour = 12


MONTHS = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

EasyTime = (
    f"{int(day)} {MONTHS[month]}, "
    f"{hour:02}:{minute} {ampm}"
)


AdmAC = Bot.getData("AdmAC") or []

act = f"Code Claim Text updated to {message.text}"

AdmAC.append(
    f"""<b>📆 Time:</b> {EasyTime}
👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]
🔍 <b>Action:</b> {act}"""
)

Bot.saveData("AdmAC", AdmAC)


Bot.runCommand(
    "/PIRO_MainMenu",
    options="<b>✅ Claim Text Updated Successfully</b>"
)

Bot.runCommand("/admin")

raise ReturnCommand()


#======================================================================
# COMMAND: /RawStats
#======================================================================
EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_B = "5042334757040423886"  # 🆔
EMOJI_C = "5398001711786762757"  # 👥
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_F = "5388790256772331442"  # ❤️

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


FulUsrs = Bot.getData("FulBotUsrs") or []
T_verifUsrs = Bot.getData("T_verifUsrs") or 0
Totl_SameDevUsrsC = Bot.getData("Totl_SameDevUsrsC") or 0
WithdrawC = Bot.getData("WithdrawC") or 0

markup = InlineKeyboardMarkup()

markup.row(
    InlineKeyboardButton(text="✨ Animated View", callback_data="/PIRO_AnimatedStats")
)
markup.row(
    InlineKeyboardButton(text="Sᴛᴀᴛɪsᴛɪᴄs", callback_data="📊 Statistics1")
)
markup.row(
    InlineKeyboardButton(text="Vᴇʀɪғɪᴇᴅ Sᴛᴀᴛs", callback_data="/verifiedStats"),
    InlineKeyboardButton(text="Pᴇʀғᴏʀᴍᴀɴᴄᴇ & Sᴛᴀᴛɪsᴛɪᴄs", callback_data="/Perfom_Stats")
)
markup.row(
    InlineKeyboardButton(text="⬅️ Bᴀᴄᴋ", callback_data="/AdminStats")
)

TXT = (
    f'<tg-emoji emoji-id="{EMOJI_A}">📊</tg-emoji><b> Bot Overview</b>\n'
    "━━━━━━━━━━━━━━━\n\n"
    f'<tg-emoji emoji-id="{EMOJI_C}">👥</tg-emoji><b> Total Users:</b> {len(FulUsrs)}\n'
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji><b> Verified:</b> {T_verifUsrs}\n'
    f'<tg-emoji emoji-id="{EMOJI_B}">🆔</tg-emoji><b> Same-Device (Allowed):</b> {Totl_SameDevUsrsC}\n'
    f'<tg-emoji emoji-id="{EMOJI_F}">💳</tg-emoji><b> Total Payouts:</b> {WithdrawC}\n\n'
    "━━━━━━━━━━━━━━━\n"
    "<i>More data will be added soon</i>"
)

bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=TXT,
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /RedeemBotRC
#======================================================================
EMOJI_ALERT = "6289507480711992374"
EMOJI_MONEY = "6082586710988820084"
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

  
Av=Bot.getData("GiftAvailabe") or "N"
if str(Av)=="Y":

    keyboard=ReplyKeyboardMarkup(True)
    keyboard.row("Cancel")
    bot.replyText(chat_id=u,text=f'<tg-emoji emoji-id="{EMOJI_MONEY}">💸</tg-emoji><b>Send Gift Code To Claim Reward!</b>',reply_markup=keyboard,parse_mode="Html")

    Bot.handleNextCommand("/RedeemBotRC1")
else:
    bot.replyText(u,f'<tg-emoji emoji-id="{EMOJI_ALERT}">😢</tg-emoji><b>No Gifts Created By Admin.</b>')


#======================================================================
# COMMAND: /RedeemBotRC1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Jenish_Dobariya1
EMOJI_FAILED="6129840374971112593"
EMOJI_PARTY = "6224161941305169199"
EMOJI_STAR = "5469741319330996757"
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5193085063998224234"
EMOJI_MONEY = "5472030678633684592"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_DOWN = "5470177992950946662"
EMOJI_PAISA = "6287207173537666597"
EMOJI_STAT = "5042290883949495533"
EMOJI_CLOCK = "6231214251835397322"
EMOJI_POTL = "5375296873982604963"
EMOJI_TARGET = "6287439449664000621"
EMOJI_USER = "5879770735999717115"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CROWN = "4956420911310832630"
EMOJI_POTLI = "6278489025581944577"
EMOJI_MST = "6278337731063975777"
EMOJI_BANK = "5332455502917949981"

AllBotAdminss = Bot.getData("AllBotAdminss") or []


# ==============================
# USER INPUT
# ==============================

user_input_code = str(message.text).strip()


# ==============================
# CANCEL
# ==============================

if user_input_code.lower() == "cancel":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji>Cancelled</b>'
    )

    raise ReturnCommand()


# ==============================
# CHECK GIFT SYSTEM
# ==============================

Av = Bot.getData("GiftAvailabe") or "N"

if Av != "Y":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> No Gift Codes Available At The Moment.\n\n'
                "Check Back Later!</b>"
    )

    raise ReturnCommand()


# ==============================
# GET GIFT CODE
# ==============================

ABC = Bot.getData(
    "GiftCode" + user_input_code + "isAMT"
)


if not ABC:

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Invalid Redeem Code! \n\n'
                f'<tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji> Make sure you`ve entered the correct code.</b>'
    )

    raise ReturnCommand()


# ==============================
# ACTUAL SAVED CODE
# ==============================

RC = str(ABC[0])


# ==============================
# STATUS
# ==============================

st = Bot.getData(
    "Gift" + RC + "KaStatus"
) or "Active"


if st != "Active":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Redeem Code Inactive

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Gift Code: <code>{RC}</code>

<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> This gift code is currently unavailable.</b>"""
    )

    raise ReturnCommand()


# ==============================
# ALREADY CLAIMED
# ==============================

Stat = Bot.getData(
    str(u) + "Gift" + RC + "stat"
)


if Stat == "claimed":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Code Already Used

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Gift Code: <code>{RC}</code>

You've already claimed this code.

<tg-emoji emoji-id="{EMOJI_SEARCH}">🔍</tg-emoji> Try a different one.</b>"""
    )

    raise ReturnCommand()


# ==============================
# CLAIM COUNT
# ==============================

C = Bot.getData(
    "Gift" + RC + "CountOfClaimedUsrs"
) or 0

MxC = Bot.getData(
    "Gift" + RC + "MaxUsrCanClaim"
) or 0


if int(C) >= int(MxC):

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Gift Code Fully Claimed

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Gift Code: <code>{RC}</code>

<tg-emoji emoji-id="{EMOJI_USER}">👤</tg-emoji> Claim Limit: {MxC}
<tg-emoji emoji-id="{EMOJI_SUCCESS}">✅</tg-emoji> Already Claimed: {C}

<tg-emoji emoji-id="{EMOJI_SEARCH}">🔍</tg-emoji> Try a different code.</b>"""
    )

    raise ReturnCommand()


# ==============================
# MINIMUM REFERRAL CHECK
# ==============================

MinRef = Bot.getData(
    "Gift" + RC + "MinRef"
) or 0

UserRefCount = Bot.getData(
    str(u) + "RefCount"
) or 0


if int(UserRefCount) < int(MinRef):

    NeedRef = int(MinRef) - int(UserRefCount)

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> You Cannot Claim This Gift Code

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Gift Code: <code>{RC}</code>

<tg-emoji emoji-id="{EMOJI_TARGET}">🎯</tg-emoji> Required Refers: {MinRef}
<tg-emoji emoji-id="{EMOJI_SUCCESS}">🎁</tg-emoji> Your Verified Refers: {UserRefCount}

<tg-emoji emoji-id="{EMOJI_STAT}">📊</tg-emoji> You Need {NeedRef} More Verified Refer(s) To Claim This Gift.</b>"""
    )

    raise ReturnCommand()


# ==============================
# CLAIM CONFIRMATION
# ==============================




bot.sendMessage(
    f"""<b><tg-emoji emoji-id="{EMOJI_MONEY}">💸</tg-emoji> Claim Confirmation 
    
<tg-emoji emoji-id="{EMOJI_DONE}">✅</tg-emoji> You're About To Claim ₹{ABC[1]}.

Confirm your action and claim your reward now.

<tg-emoji emoji-id="{EMOJI_DOWN}">👇🏻</tg-emoji> Click Proceed To Complete Claim</b>""",
    reply_markup={
        "inline_keyboard": [
            [
                {"text": "Proceed", "callback_data": "/RedeemBotRC2",
                "icon_custom_emoji_id": EMOJI_SUCCESS,
                "style": "success"
                }
            ]
        ]
    }
)


# ==============================
# SAVE CODE FOR STEP 2
# ==============================

User.saveData(
    "InpBGRC",
    RC
)


#======================================================================
# COMMAND: /RedeemBotRC2
#======================================================================
EMOJI_FAILED="6129840374971112593"
EMOJI_PARTY = "6224161941305169199"
EMOJI_STAR = "5469741319330996757"
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5193085063998224234"
EMOJI_MONEY = "5472030678633684592"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_DOWN = "5470177992950946662"
EMOJI_PAISA = "6287207173537666597"
EMOJI_STAT = "5042290883949495533"
EMOJI_CLOCK = "6231214251835397322"
EMOJI_POTL = "5375296873982604963"
EMOJI_TARGET = "6287439449664000621"
EMOJI_USER = "5879770735999717115"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CROWN = "4956420911310832630"
EMOJI_POTLI = "6278489025581944577"
EMOJI_MST = "6278337731063975777"
EMOJI_BANK = "5332455502917949981"
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Jenish_Dobariya1 

try:
    bot.deleteMessage(u, message.message_id)
except:
    pass


RRC = User.getData("InpBGRC")

UsrsClaimedBotRC = Bot.getData(
    "UsrsClaimedBotRC" + str(RRC)
) or []


Botpaychannel = Bot.getData("Botpaychannel")

ABC = Bot.getData(
    "GiftCode" + str(RRC) + "isAMT"
)


# ==============================
# INVALID CODE
# ==============================

if not ABC or len(ABC) < 2:
    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Invalid Gift Code</b>'
    )
    raise ReturnCommand()


Stat = Bot.getData(
    f"{u}Gift{ABC[0]}stat"
)

C = Bot.getData(
    f"Gift{ABC[0]}CountOfClaimedUsrs"
) or 0

MxC = Bot.getData(
    f"Gift{ABC[0]}MaxUsrCanClaim"
) or 0


# ==============================
# ALREADY CLAIMED
# ==============================

if Stat == "claimed":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Code Used\n\nYou already used this code!</b>'
    )

    raise ReturnCommand()


# ==============================
# CODE STATUS
# ==============================

RC = ABC[0]

st = Bot.getData(
    f"Gift{RC}KaStatus"
) or "Active"

if st != "Active":

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Redeem Code Expired <tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji></b>'
    )

    raise ReturnCommand()


# ==============================
# MAX CLAIM CHECK
# ==============================

if int(C) >= int(MxC):

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> This Code Is Expired ❌</b>'
    )

    raise ReturnCommand()


# ==============================
# MINIMUM REFERRAL CHECK
# ==============================

MinRef = Bot.getData(
    "Gift" + str(ABC[0]) + "MinRef"
) or 0

UserRefCount = Bot.getData(
    str(u) + "RefCount"
) or 0


if int(UserRefCount) < int(MinRef):

    NeedRef = int(MinRef) - int(UserRefCount)

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Minimum Referral Requirement Not Met

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Gift Code: <code>{ABC[0]}</code>

<tg-emoji emoji-id="{EMOJI_TARGET}">🎯</tg-emoji> Required Refers: {MinRef}
<tg-emoji emoji-id="{EMOJI_SUCCESS}">✅</tg-emoji>Your Verified Refers: {UserRefCount}

<tg-emoji emoji-id="{EMOJI_STAT}">📊</tg-emoji> You Need {NeedRef} More Verified Refer(s).</b>"""
    )

    raise ReturnCommand()


# ==============================
# CLAIM GIFT
# ==============================

amount = int(ABC[1])

libs.Resources.anotherRes(
    'Balance',
    user=u
).add(amount)


Bot.saveData(
    f"{u}Gift{ABC[0]}stat",
    "claimed"
)

Bot.saveData(
    f"Gift{ABC[0]}CountOfClaimedUsrs",
    int(C) + 1
)


# ==============================
# SAVE CLAIMED USER
# ==============================

if str(u) not in [str(x) for x in UsrsClaimedBotRC]:

    UsrsClaimedBotRC.append(u)

    Bot.saveData(
        "UsrsClaimedBotRC" + str(RRC),
        UsrsClaimedBotRC
    )

# ==============================
# CLAIM SUCCESS TEXT
# ==============================

GGT = Bot.getData("RCT")

if not GGT:
    GGT = f'<tg-emoji emoji-id="{EMOJI_PARTY}">🎉</tg-emoji> Congratulations! You Have Successfully Claimed The Gift Code Of {{Bonus}}'

BonusText = f"₹{amount}"

GGT = str(GGT).replace(
    "{Bonus}",
    BonusText
)


Bot.runCommand(
    "/PIRO_MainMenu",
    options=f"<b>{GGT}</b>"
)

# ==============================
# DATE & TIME
# ==============================

datetime = libs.DateAndTime.now("Asia/Kolkata")

date = datetime["date"]
time = datetime["time"]


# ==============================
# PAYOUT CHANNEL LOG
# ==============================

if Botpaychannel:

    try:

        Bot.replyText(
            Botpaychannel,
            f"""
<b>New User Claimed Gift Code 🎁</b>

🔹 <b>User :</b> <a href="tg://user?id={u}">{message.from_user.first_name}</a>
🔹 <b>ID:</b> <code>{u}</code>
🔸 <b>Code :</b> <code>{RRC}</code>
🔸 <b>Amount:</b> <b>₹{amount:,}</b>
📆 <b>Date :</b> {date}
⏱ <b>Time:</b> {time}
🤖 <i>Bot: @{Bot.info().username}</i>
""",
            parse_mode="HTML"
        )

    except Exception as e:

        Bot.log(
            f"Error sending to Botpaychannel: {e}"
        )


raise ReturnCommand()


#======================================================================
# COMMAND: /ReferTracker
#======================================================================
bot.replyText(
    u,
    "<b>Send the user id (number) you want to check</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/ReferTrackerCheck")


#======================================================================
# COMMAND: /ReferTrackerCheck
#======================================================================
uid = message.text.strip()

# Check user started bot or not
UserStarted = Bot.getData("UserID" + str(uid))

if UserStarted == None:
    bot.replyText(
        u,
        "<b>❌ This User Has Not Started The Bot Yet!</b>",
        parse_mode="html"
    )
    raise ReturnCommand()


ref = Bot.getData(str(uid)+"Referral") or "None"
sameDev = Bot.getData(str(uid)+"sameDev") or "no"
is_invited = User.getData("is_invited")


# Default
credit = "NO ❌"


if ref == "None":
    invited = "—"
    note = "This User Was Not Referred By Anyone."

else:
    ref = str(ref)

    if len(ref) > 5:
        invited = ref[:2] + "xxxxx" + ref[-3:]
    else:
        invited = ref
        

    if sameDev == "yes":
        note = "Same Device Detected. Referral Bonus Not Available."
        credit = "NO ❌"

    elif is_invited:
        note = "This User Was Referred Successfully."
        credit = "YES ✅"

    else:
        note = "Referral Failed. Bonus Not Credited."
        credit = "NO ❌"



bot.replyText(
    u,
    f"""<b>👥 User ==> <code>{uid}</code>
💰 Invited By ==> {invited}
❓ Invite Credited ==> {credit}
⚠️ Note ==> {note}
</b>""",
    parse_mode="html"
)


#======================================================================
# COMMAND: /ResetAllBalance
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()

AllUsers = Bot.getData("FulBotUsrs") or []

total_balance = 0

for user_id in AllUsers:
    try:
        balance = libs.Resources.anotherRes(
            "Balance",
            user=str(user_id)
        ).value() or 0

        total_balance += float(balance)

    except:
        pass


markup = {
    "inline_keyboard": [
        [
            {
                "text": "✅ Confirm Reset",
                "callback_data": "/ResetAllBalanceConfirm"
            },
            {
                "text": "❌ Cancel",
                "callback_data": "/admin"
            }
        ]
    ]
}


bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text=f"""<b>⚠️ RESET ALL BALANCES</b>

━━━━━━━━━━━━━━━━━━

👥 <b>Total Users:</b> {len(AllUsers)}
💰 <b>Total Bot Balance:</b> ₹{total_balance:.2f}

⚠️ <i>This will only reset Balance.
Other user data will remain safe.</i>

━━━━━━━━━━━━━━━━━━

<b>Are you sure you want to continue?</b>""",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /ResetAllBalanceConfirm
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()


# ==============================
# USERS
# ==============================

AllUsers = Bot.getData("FulBotUsrs") or []


# ==============================
# REPORT BOT
# ==============================

token = "8327459100:AAEl6kQgHOxPby5yQO6A0SEdokxCs0G-m4E"
report_chat_id = "6925391837"


# ==============================
# COLLECT BALANCE DATA
# ==============================

total_balance = 0
success = 0
report_lines = []


for user_id in AllUsers:

    try:

        user_id = str(user_id)

        balance = libs.Resources.anotherRes(
            "Balance",
            user=user_id
        )

        current = balance.value() or 0
        current = float(current)

        total_balance += current

        if current != 0:

            report_lines.append(
                f"👤 User ID: <code>{user_id}</code>\n"
                f"💰 Balance: ₹{current:.2f}"
            )

        success += 1

    except:
        pass


# ==============================
# FETCH BOT USERNAME
# ==============================
bot_username = Bot.info().username 


# ==============================
# REPORT TEXT
# ==============================

report_text = f"""<b>📊 BALANCE RESET HISTORY</b>

━━━━━━━━━━━━━━━━━━

👤 <b>Reset By Admin:</b> <code>{u}</code>
🤖 <b>Bot Username:</b> @{bot_username}

👥 <b>Total Users:</b> {len(AllUsers)}
💰 <b>Total Balance Before Reset:</b> ₹{total_balance:.2f}

━━━━━━━━━━━━━━━━━━

"""



if report_lines:

    report_text += "\n\n".join(report_lines)

else:

    report_text += "💰 No user had a balance."


# ==============================
# SEND REPORT THROUGH REPORT BOT
# ==============================

try:

    HTTP.get(
        f"https://api.telegram.org/bot{token}/sendMessage"
        f"?chat_id={report_chat_id}"
        f"&parse_mode=HTML"
        f"&text={report_text}"
    )

except:
    pass


# ==============================
# RESET ALL BALANCES
# ==============================

reset_count = 0


for user_id in AllUsers:

    try:

        user_id = str(user_id)

        balance = libs.Resources.anotherRes(
            "Balance",
            user=user_id
        )

        current = balance.value() or 0

        if current != 0:
            balance.cut(current)

        reset_count += 1

    except:
        pass


# ==============================
# FINAL RESULT
# ==============================

bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,

    text=f"""<b>✅ BALANCE RESET COMPLETE</b>

━━━━━━━━━━━━━━━━━━

👥 <b>Users Reset:</b> {reset_count}
💰 <b>New Balance:</b> ₹0

━━━━━━━━━━━━━━━━━━

<i>All other user data remains unchanged.</i>""",

    parse_mode="HTML",

    reply_markup={
        "inline_keyboard": [
            [
                {
                    "text": "🔙 Admin Panel",
                    "callback_data": "/admin"
                }
            ]
        ]
    }
)


#======================================================================
# COMMAND: /SCHEDULE_BROADCAST
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.sendMessage("<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Get all users
FulBotUsrs = Bot.getData("FulBotUsrs") or []
if not FulBotUsrs:
    bot.sendMessage("<b>❌ No users found in bot!</b>")
    raise ReturnCommand()

bot.sendMessage(f"""<b>📅 Schedule Broadcast to {len(FulBotUsrs)} Users</b>

<i>Send date & time in one line:</i>
<code>DD-MM-YYYY HH:MM AM/PM</code>
<b>Example:</b> <code>25-12-2025 02:30 PM</code>

<i>Send /cancel to cancel</i>""")

Bot.handleNextCommand("/SCHEDULE_SET_TIME")


#======================================================================
# COMMAND: /SCHEDULE_EXECUTE
#======================================================================
# No admin check – runs automatically

task_id = options
task_data = Bot.getData(f"BC_Task_{task_id}") or {}
if not task_data:
    raise ReturnCommand()

u = task_data.get("user")
bc_data = task_data.get("data", {})
txt = bc_data.get("text", "")
file_id = bc_data.get("file_id")
msg_type = bc_data.get("type", "text")

# ✅ Get latest user list at execution time
users = Bot.getData("FulBotUsrs") or []

if not users:
    bot.sendMessage("<b>❌ No users to broadcast!</b>")
    raise ReturnCommand()

# Send to all users
success = 0
failed = 0
failed_list = []

for user_id in users:
    try:
        if msg_type == "text":
            bot.sendMessage(chat_id=str(user_id), text=txt, parse_mode="html", disable_web_page_preview=True)
        elif msg_type == "photo":
            bot.sendPhoto(chat_id=str(user_id), photo=file_id, caption=txt, parse_mode="html")
        elif msg_type == "video":
            bot.sendVideo(chat_id=str(user_id), video=file_id, caption=txt, parse_mode="html")
        elif msg_type == "document":
            bot.sendDocument(chat_id=str(user_id), document=file_id, caption=txt, parse_mode="html")
        elif msg_type == "audio":
            bot.sendAudio(chat_id=str(user_id), audio=file_id, caption=txt, parse_mode="html")
        elif msg_type == "sticker":
            bot.sendSticker(chat_id=str(user_id), sticker=file_id)
        elif msg_type == "animation":
            bot.sendAnimation(chat_id=str(user_id), animation=file_id, caption=txt, parse_mode="html")
        success += 1
    except:
        failed += 1
        failed_list.append(str(user_id))

# Report to admin
report = f"""<b>📢 Scheduled Broadcast Complete</b>
✅ Success: {success}
❌ Failed: {failed}
📊 Total: {len(users)}"""
if failed_list:
    report += "\n\n<b>⚠️ Failed Users:</b>\n" + "\n".join(failed_list[:10])

bot.sendMessage(report, disable_web_page_preview=True)

# Cleanup task data
Bot.saveData(f"BC_Task_{task_id}", None)


#======================================================================
# COMMAND: /SCHEDULE_SET_MESSAGE
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.sendMessage("<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if message.text == "/cancel":
    bot.sendMessage("<b>❌ Cancelled</b>")
    Bot.saveData("BC_Schedule_Date", None)
    Bot.saveData("BC_Schedule_Time_12hr", None)
    Bot.saveData("BC_Schedule_Hour", None)
    Bot.saveData("BC_Schedule_Minute", None)
    raise ReturnCommand()

# Detect content
txt = message.caption if message.caption else message.text
entities = message.caption_entities if message.caption else message.entities
if entities:
    txt = apply_html_entities(txt, entities, {})

msg_type = "text"
file_id = None
if message.photo:
    msg_type = "photo"
    file_id = message.photo[-1].file_id
elif message.video:
    msg_type = "video"
    file_id = message.video.file_id
elif message.document:
    msg_type = "document"
    file_id = message.document.file_id
elif message.audio:
    msg_type = "audio"
    file_id = message.audio.file_id
elif message.sticker:
    msg_type = "sticker"
    file_id = message.sticker.file_id
elif message.animation:
    msg_type = "animation"
    file_id = message.animation.file_id
elif message.text:
    msg_type = "text"
else:
    bot.sendMessage("<b>❌ Unsupported file!</b>")
    raise ReturnCommand()

# ✅ Store only a flag, not the user list (to include new users later)
bc_data = {
    "type": msg_type,
    "text": txt,
    "file_id": file_id,
    "target": "all_users"   # Fetch latest users at execution
}
Bot.saveData("BC_Data", bc_data)

# Calculate delay
date_str = Bot.getData("BC_Schedule_Date")
time_12hr = Bot.getData("BC_Schedule_Time_12hr")
hour24 = Bot.getData("BC_Schedule_Hour")
minute = Bot.getData("BC_Schedule_Minute")

now = libs.DateAndTime.now("Asia/Kolkata")
cur_d = now["date"].split("-")
cur_y, cur_m, cur_d = map(int, cur_d)
cur_h, cur_min = map(int, now["time"].split(":")[:2])

d, m, y = map(int, date_str.split("-"))
diff_days = (y - cur_y) * 365 + (m - cur_m) * 30 + (d - cur_d)
diff_sec = diff_days * 86400 + (hour24 - cur_h) * 3600 + (minute - cur_min) * 60
if diff_sec < 5:
    diff_sec = 5

# Create task
task_counter = Bot.getData("BC_Task_Counter") or 0
task_counter += 1
Bot.saveData("BC_Task_Counter", task_counter)
task_id = f"sch_{u}_{task_counter}"
Bot.saveData(f"BC_Task_{task_id}", {"user": u, "data": bc_data, "date": date_str, "time": time_12hr})

# Schedule
Bot.runCommandAfter(diff_sec, "/SCHEDULE_EXECUTE", options=task_id)

# Show confirmation with current user count (new users will be included later)
current_users = Bot.getData("FulBotUsrs") or []
bot.sendMessage(f"""<b>✅ Broadcast Scheduled!</b>

📆 {date_str} at {time_12hr}
👥 {len(current_users)} users (will include new users at execution)
📝 {msg_type.upper()}

<i>Will run automatically.</i>""")

# Cleanup temp
Bot.saveData("BC_Schedule_Date", None)
Bot.saveData("BC_Schedule_Time_12hr", None)
Bot.saveData("BC_Schedule_Hour", None)
Bot.saveData("BC_Schedule_Minute", None)
Bot.saveData("BC_Data", None)


#======================================================================
# COMMAND: /SCHEDULE_SET_TIME
#======================================================================
# Admin Check
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
if is_Admin != True:
    bot.sendMessage("<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if message.text == "/cancel":
    bot.sendMessage("<b>❌ Cancelled</b>")
    raise ReturnCommand()

# Parse: "25-12-2025 02:30 PM"
parts = message.text.strip().split(" ")
if len(parts) < 3:
    bot.sendMessage("<b>❌ Invalid! Use: DD-MM-YYYY HH:MM AM/PM</b>")
    raise ReturnCommand()

date_str = parts[0]
time_str = parts[1]
ampm = parts[2].upper()

# Validate date
try:
    d, m, y = map(int, date_str.split("-"))
    if d<1 or d>31 or m<1 or m>12 or y<2024: raise ValueError
except:
    bot.sendMessage("<b>❌ Invalid date! Use DD-MM-YYYY</b>")
    raise ReturnCommand()

# Validate time
try:
    h, mn = map(int, time_str.split(":"))
    if h<1 or h>12 or mn<0 or mn>59: raise ValueError
    if ampm not in ["AM","PM"]: raise ValueError
except:
    bot.sendMessage("<b>❌ Invalid time! Use HH:MM AM/PM</b>")
    raise ReturnCommand()

# Convert to 24hr
if ampm == "PM" and h != 12:
    h24 = h + 12
elif ampm == "AM" and h == 12:
    h24 = 0
else:
    h24 = h

# Check future
now = libs.DateAndTime.now("Asia/Kolkata")
cur_d = now["date"].split("-")
cur_y, cur_m, cur_d = map(int, cur_d)
cur_h, cur_min = map(int, now["time"].split(":")[:2])

is_future = False
if y > cur_y:
    is_future = True
elif y == cur_y and m > cur_m:
    is_future = True
elif y == cur_y and m == cur_m and d > cur_d:
    is_future = True
elif y == cur_y and m == cur_m and d == cur_d:
    if h24 > cur_h or (h24 == cur_h and mn > cur_min):
        is_future = True

if not is_future:
    bot.sendMessage("<b>❌ Scheduled time is in the past! Choose a future time.</b>")
    raise ReturnCommand()

# Store
Bot.saveData("BC_Schedule_Date", f"{d:02d}-{m:02d}-{y}")
Bot.saveData("BC_Schedule_Time_12hr", f"{h:02d}:{mn:02d} {ampm}")
Bot.saveData("BC_Schedule_Hour", h24)
Bot.saveData("BC_Schedule_Minute", mn)

bot.sendMessage(f"""<b>📅 Schedule Broadcast</b>

📆 Date: {d:02d}-{m:02d}-{y}
⏰ Time: {h:02d}:{mn:02d} {ampm}

<i>Now send your message (text/photo/video/document)</i>
<i>Send /cancel to cancel</i>""")

Bot.handleNextCommand("/SCHEDULE_SET_MESSAGE")


#======================================================================
# COMMAND: /SaveFundChannel
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()


channels = message.text.strip().split(",")


if len(channels) > 2:

    bot.replyText(
        u,
        "<b>❌ Maximum 2 Channels Allowed</b>",
        parse_mode="html"
    )

    raise ReturnCommand()


channel1 = channels[0].strip()

channel2 = None

if len(channels) == 2:
    channel2 = channels[1].strip()


fund = float(
    Bot.getData("LiveFund") or 0
)

bot_name = Bot.info().username


# =========================
# CHANNEL 1
# =========================

try:

    post1 = bot.sendMessage(
        chat_id=channel1,
        text=f"""<b>✅ Total Remaining Fund In @{bot_name} >> ₹{fund:.2f}

🚀 This Is A High Fund And Long
Term Running Bot With Huge Funds

💰💰 Loot As Much As You Can 😎🙏

😍 Specially Powered By
{channel1} !!

</b>""",
        parse_mode="html",
        reply_markup={
            "inline_keyboard": [
                [
                    {
                        "text": f"💰 Fund ₹{fund:.2f}",
                        "url": f"https://t.me/{bot_name}"
                    }
                ]
            ]
        }
    )


    bot.pinChatMessage(
        chat_id=channel1,
        message_id=post1.message_id
    )


    Bot.saveData(
        "LiveFundChannel1",
        channel1
    )


    Bot.saveData(
        "LiveFundMsgID1",
        post1.message_id
    )


except Exception as e:

    bot.replyText(
        u,
        f"""<b>❌ Channel 1 Failed

Error:
{e}</b>""",
        parse_mode="html"
    )

    raise ReturnCommand()


# =========================
# CHANNEL 2
# =========================

if channel2:

    try:

        post2 = bot.sendMessage(
            chat_id=channel2,
            text=f"""<b>✅ Total Remaining Fund In @{bot_name} >> ₹{fund:.2f}

🚀 This Is A High Fund And Long
Term Running Bot With Huge Funds

💰💰 Loot As Much As You Can 😎🙏

😍 Specially Powered By
{channel2} !!

</b>""",
            parse_mode="html",
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": f"💰 Fund ₹{fund:.2f}",
                            "url": f"https://t.me/{bot_name}"
                        }
                    ]
                ]
            }
        )


        bot.pinChatMessage(
            chat_id=channel2,
            message_id=post2.message_id
        )


        Bot.saveData(
            "LiveFundChannel2",
            channel2
        )


        Bot.saveData(
            "LiveFundMsgID2",
            post2.message_id
        )


    except Exception as e:

        bot.replyText(
            u,
            f"""<b>❌ Channel 2 Failed

Error:
{e}</b>""",
            parse_mode="html"
        )

        raise ReturnCommand()


else:

    # Clear old second channel data
    Bot.saveData(
        "LiveFundChannel2",
        None
    )

    Bot.saveData(
        "LiveFundMsgID2",
        None
    )


# =========================
# SUCCESS
# =========================

bot.replyText(
    u,
    f"""<b>✅ Live Fund Post Created & Pinned

📢 Channel 1:
{channel1}

📢 Channel 2:
{channel2 if channel2 else "Not Set"}

💰 Fund:
₹{fund:.2f}
</b>""",
    parse_mode="html"
)


#======================================================================
# COMMAND: /SetAllLimits
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in list(map(str, AllBotAdminss)):
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


text = message.text.strip()

wallet_data = None
upi_data = None

try:
    # -----------------------------
    # EXTRACT WALLET
    # -----------------------------
    lower_text = text.lower()

    if "wallet:" in lower_text:
        wallet_part = lower_text.split("wallet:", 1)[1]

        if "upi:" in wallet_part:
            wallet_part = wallet_part.split("upi:", 1)[0]

        wallet_part = wallet_part.strip().replace(" ", "")

        w_min, w_max, w_ref = map(int, wallet_part.split("-"))

        if w_min < 0 or w_max < 0 or w_ref < 0:
            raise Exception()

        if w_min > w_max:
            raise Exception()

        wallet_data = (w_min, w_max, w_ref)


    # -----------------------------
    # EXTRACT UPI
    # -----------------------------
    if "upi:" in lower_text:
        upi_part = lower_text.split("upi:", 1)[1]

        if "wallet:" in upi_part:
            upi_part = upi_part.split("wallet:", 1)[0]

        upi_part = upi_part.strip().replace(" ", "")

        u_min, u_max, u_ref = map(int, upi_part.split("-"))

        if u_min < 0 or u_max < 0 or u_ref < 0:
            raise Exception()

        if u_min > u_max:
            raise Exception()

        upi_data = (u_min, u_max, u_ref)


    # At least one setting required
    if wallet_data is None and upi_data is None:
        raise Exception()


except:
    bot.replyText(
        u,
        """<b>❌ Invalid Format!</b>

Use:

<code>Wallet:10-100-5</code>
<code>UPI:10-264-0</code>

Or update both:

<code>Wallet:10-100-5 UPI:10-264-0</code>

<b>Format:</b>
Min - Max - Min Referrals""",
        parse_mode="html"
    )
    raise ReturnCommand()


# -----------------------------
# OLD VALUES
# -----------------------------
old_w_min = Bot.getData("MinWith") or 0
old_w_max = Bot.getData("MaxWith") or 0
old_w_ref = Bot.getData("SetMinRef") or 0

old_u_min = Bot.getData("MinWith1") or 0
old_u_max = Bot.getData("MaxWith1") or 0
old_u_ref = Bot.getData("SetMinRef1") or 0


# -----------------------------
# SAVE VALUES
# -----------------------------
if wallet_data:
    w_min, w_max, w_ref = wallet_data

    Bot.saveData("MinWith", w_min)
    Bot.saveData("MaxWith", w_max)
    Bot.saveData("SetMinRef", w_ref)


if upi_data:
    u_min, u_max, u_ref = upi_data

    Bot.saveData("MinWith1", u_min)
    Bot.saveData("MaxWith1", u_max)
    Bot.saveData("SetMinRef1", u_ref)


# -----------------------------
# TIME
# -----------------------------
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]
time = now["time"][:5]

y, m, d = date.split("-")
h, mi = time.split(":")

h = int(h)

ampm = "am"

if h >= 12:
    ampm = "pm"

if h > 12:
    h -= 12

if h == 0:
    h = 12


MONTHS = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

EasyTime = f"{int(d)} {MONTHS[m]}, {h:02}:{mi} {ampm}"


# -----------------------------
# ADMIN ACTIVITY
# -----------------------------
AdmAC = Bot.getData("AdmAC") or []

actions = []

if wallet_data:
    actions.append(
        f"Wallet: {old_w_min}-{old_w_max}-{old_w_ref} → "
        f"{w_min}-{w_max}-{w_ref}"
    )

if upi_data:
    actions.append(
        f"UPI: {old_u_min}-{old_u_max}-{old_u_ref} → "
        f"{u_min}-{u_max}-{u_ref}"
    )

AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👤 <b>By {message.from_user.first_name}</b> "
    f"[ID: <code>{u}</code>]\n"
    f"🔧 <b>Action:</b>\n" +
    "\n".join(actions)
)

Bot.saveData("AdmAC", AdmAC)


# -----------------------------
# SUCCESS MESSAGE
# -----------------------------

# ONLY WALLET
if wallet_data and not upi_data:

    bot.replyText(
        u,
        f"""<b>✅ Wɪᴛʜᴅʀᴀᴡ Sᴇᴛᴛɪɴɢs Uᴘᴅᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!

💳 Wᴀʟʟᴇᴛ Wɪᴛʜᴅʀᴀᴡ
• Mɪɴ: ₹{w_min}
• Mᴀx: ₹{w_max}
• Min. Rᴇғᴇʀʀᴀʟs: {w_ref}</b>""",
        parse_mode="html"
    )


# ONLY UPI
elif upi_data and not wallet_data:

    bot.replyText(
        u,
        f"""<b>✅ Wɪᴛʜᴅʀᴀᴡ Sᴇᴛᴛɪɴɢs Uᴘᴅᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!

💳 Uᴘɪ Wɪᴛʜᴅʀᴀᴡ
• Mɪɴ: ₹{u_min}
• Mᴀx: ₹{u_max}
• Min. Rᴇғᴇʀʀᴀʟs: {u_ref}</b>""",
        parse_mode="html"
    )


# BOTH
else:

    bot.replyText(
        u,
        f"""<b>✅ Wɪᴛʜᴅʀᴀᴡ Sᴇᴛᴛɪɴɢs Uᴘᴅᴀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!

💳 Wᴀʟʟᴇᴛ Wɪᴛʜᴅʀᴀᴡ
• Mɪɴ: ₹{w_min}
• Mᴀx: ₹{w_max}
• Min. Rᴇғᴇʀʀᴀʟs: {w_ref}

💳 Uᴘɪ Wɪᴛʜᴅʀᴀᴡ
• Mɪɴ: ₹{u_min}
• Mᴀx: ₹{u_max}
• Min. Rᴇғᴇʀʀᴀʟs: {u_ref}</b>""",
        parse_mode="html"
    )


Bot.runCommand("/admin")


#======================================================================
# COMMAND: /SetBonusAmont
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.replyText(
    u,
    """<b>📢 Send Amount For Daily Bonus

👉 Send number = Normal Bonus
🎲 Send 'Dice' = Dice Bonus Mode</b>""",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBonusAmont1")


#======================================================================
# COMMAND: /SetBonusAmont1
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

msg = message.text.strip()

# ===== TIME SYSTEM =====
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 

year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)

ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan","02": "Feb","03": "Mar","04": "Apr",
    "05": "May","06": "Jun","07": "Jul","08": "Aug",
    "09": "Sep","10": "Oct","11": "Nov","12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

# ===== ADMIN LOG =====
AdmAC = Bot.getData("AdmAC") or []

# ===== CHECK MODE =====
if msg.lower() == "dice":
    
    Bot.saveData("DailyBonusType", "dice")
    
    act = "Bonus Mode updated to 🎲 Dice Bonus"
    
    bot.replyText(
        u,
        "<b>🎲 Dice Bonus Mode Activated</b>",
        parse_mode="html"
    )

else:
    try:
        amount = float(msg)
    except:
        bot.replyText(u, "<b>❌ Invalid Input! Send number or 'Dice'</b>", parse_mode="html")
        raise ReturnCommand()

    Bot.saveData("DailyBonus", amount)
    Bot.saveData("DailyBonusType", "normal")
    
    act = f"Bonus Amount set to {amount} Rs."

    bot.replyText(
        u,
        f"<b>✅ Bonus Amount Updated To {amount} Rs.</b>",
        parse_mode="html"
    )

# ===== SAVE ADMIN LOG =====
AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n"
    f"🔍 <b>Action:</b> {act}"
)

Bot.saveData("AdmAC", AdmAC)

Bot.runCommand("/admin")


#======================================================================
# COMMAND: /SetBotGatewayKey
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss")
if AllBotAdminss is None:
    push = []
else:
    push = AllBotAdminss

is_Admin = False
for userid in push:
    if str(message.chat.id) == str(userid):
        is_Admin = True

if not is_Admin:
    bot.replyText(message.chat.id, "<b>🚫 You Are Not Bot Admin</b>", parse_mode="HTML")
    raise ReturnCommand()

# ================== ALL GATEWAYS MASTER CONFIG ==================
gateway_config = {
    "vsv": {"name": "VSV Wallet", "cmd": "/Set_Key_Token"},
    "payzy": {"name": "Payzy Wallet", "cmd": "/Set_Key_Token"},
    "ultra": {"name": "Ultra Wallet", "cmd": "/Set_Key_Tk"},
    "sa": {"name": "Saathi Gateway", "cmd": "/Set_Key_Tk"},
    "rupix": {"name": "Rupix Wallet", "cmd": "/Set_Key_Tk"},  
    "txg": {"name": "TXG Wallet", "cmd": "/Set_Key_Secret"},  
}

markup = InlineKeyboardMarkup()
has_active_gateway = False

# Loop chalakar check karenge kaun-kaun se gateways ON hain
for db_key, data in gateway_config.items():
    # Agar gateway database mein ON (True) hai, sirf tabhi button dikhega
    if Bot.getData(db_key) == True:
        has_active_gateway = True
        action_cb = f"{data['cmd']} {db_key}"
        
        markup.row(
            InlineKeyboardButton(text=data["name"], callback_data='/none'),
            InlineKeyboardButton(text="Set Keys ⚙️", callback_data=action_cb)
        )

# Back Button
markup.add(InlineKeyboardButton(text="🔙 Exit", callback_data='/addgetwayonbbot'))

# UI Text Handling based on active gateways
if has_active_gateway:
    page_text = "<b>⚙️ ACTIVE GATEWAYS CONFIGURATION</b>\n\n<i>Select any active gateway to configure its specific credentials.</i>"
else:
    page_text = "<b>⚠️ NO ACTIVE GATEWAYS FOUND!</b>\n\n<i>Pehle main menu se kisi gateway ko ON karein, tabhi woh yahan show hoga.</i>"

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=page_text,
    parse_mode="HTML",
    reply_markup=markup,
    disable_web_page_preview=True
)


#======================================================================
# COMMAND: /SetBotGatewayKeyKey1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_map = {
    "vsv": "VSV Wallet",
    "txg":"TXG Wallet",
    "ultra":"Ultra Wallet",
    "rupix":"Rupix Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()


Bot.saveData(f"KEY_{Gatewaysett0}", msg)


markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

bot.replyText(
    u,
    f"<b>✅ {Gatewaysett20} Payout API Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeyapi1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Wallet"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_map = {
    "vsv": "VSV Wallet",
    "txg":"TXG Wallet",
    "ultra":"Ultra Wallet",
    "rupix":"Rupix Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Wallet")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()


Bot.saveData("SECRETKEY", msg)


markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

bot.replyText(
    u,
    f"<b>✅ {Gatewaysett20} Payout API Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeyguid
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your GUID :</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeyguid1")


#======================================================================
# COMMAND: /SetBotGatewayKeyguid1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "info": "Infotech "
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()


Bot.saveData("GUID", msg)


markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

bot.replyText(
    u,
    f"<b>✅ <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Payout GUID Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeykey
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Key:</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeyKey1")


#======================================================================
# COMMAND: /SetBotGatewayKeymeyy
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your MKEY :</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeymeyy1")


#======================================================================
# COMMAND: /SetBotGatewayKeymeyy1
#======================================================================
# Check if user is an admin
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Fetch gateway configuration
Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

# Define human-readable gateway names
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "info": "Infotech"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

# If gateway is not set, block further steps
if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

# Save the input MID
Bot.saveData("MKEY", msg)

# Build inline markup
markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

# Show confirmation message
bot.replyText(
    u,
    f"<b>✅ <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Payout MKEY Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeymii
#======================================================================



#======================================================================
# COMMAND: /SetBotGatewayKeymiid
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Mid :</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeymiid1")


#======================================================================
# COMMAND: /SetBotGatewayKeymiid1
#======================================================================
# Check if user is an admin
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Fetch gateway configuration
Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

# Define human-readable gateway names
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "info": "Infotech"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

# If gateway is not set, block further steps
if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

# Save the input MID
Bot.saveData("MID", msg)

# Build inline markup
markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

# Show confirmation message
bot.replyText(
    u,
    f"<b>✅ <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Payout MID Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeynum
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Number:</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeynum1")


#======================================================================
# COMMAND: /SetBotGatewayKeynum1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "RDX": "RDX"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()


Bot.saveData("NUM", msg)


markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/SetBotGatewayKey"}]
    ]
}

bot.replyText(
    u,
    f"<b>✅ <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Payout NUMBER Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotGatewayKeysapi
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Secret Key:</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeyapi1")


#======================================================================
# COMMAND: /SetBotGatewayKeytokken
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Token :</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotGatewayKeytokken1")


#======================================================================
# COMMAND: /SetBotGatewayKeytokken1
#======================================================================
# Get admin list
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

# Check admin permission
is_Admin = str(message.chat.id) in [str(userid) for userid in push]
if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Get gateway settings
Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

# Define gateway readable names
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet",
    "payzy": "Payzy Wallet",
    "RDX": "RDX wallet",
    "e": "E Wallet",
    "sa": "Saathi Wallet",
    "ultra": "Ultra Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

# Block if not set
if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

# Handle token-based gateways
token_based = ["Rjwallet", "vsv", "payzy", "Tgwallet", "lifafawala", "RDX", "e", "sa", "ultra"]

if Gatewaysett0 in token_based:
    # 1. Gateway ke naam ke saath unique key banayein (e.g., TOKEN_ultra)
    token_key = f"TOKEN_{Gatewaysett0}"
    
    # 2. Us specific gateway ka token save karein
    Bot.saveData(token_key, msg)
    
    markup = {
        "inline_keyboard": [
            [{"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}]
        ]
    }
    
    bot.replyText(u,
        f"<b>✅ {Gatewaysett20} Token Saved!</b>\n\n"
        f"<code>{msg}</code>",
        reply_markup=markup,
        parse_mode="html",
        disable_web_page_preview=True
    )
    raise ReturnCommand()
    


#======================================================================
# COMMAND: /SetBotPayChann
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your PayChannel Username\n\nSend <code>Clear</code> To Remove Current Payout Channel</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotPayChann1")


#======================================================================
# COMMAND: /SetBotPayChann1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


CH = msg.strip()

# --- Clear Logic Start ---
if CH.lower() == "clear":
    Bot.saveData("Botpaychannel", "not set")
    markup = {"inline_keyboard": [[{"text": "🔙 Back", "callback_data": "/admin"}]]}
    bot.replyText(u, "<b>🗑 Payout Channel has been cleared successfully!</b>", reply_markup=markup, parse_mode="HTML")
    raise ReturnCommand()
# --- Clear Logic End ---

if "@" not in CH and "-" not in CH:
    bot.sendMessage(f"{CH} is not a valid channel username or Telegram ID")
    raise ReturnCommand()

# ... (Aapka baki ka purana code niche waisa hi rahega) ...


Txt = ""
BIA = True
CLink = "None"
TGID = str(CH)
TITLE = str(CH)
USRNAM = "None"

try:
    url = f'https://api.telegram.org/bot{Bot.info().token}/getChat?chat_id={CH}'
    b = HTTP.get(url).json()
    result = bunchify(b)['result']
    CLink = result.invite_link if "invite_link" in result else "None"
    TGID = result.id
    TITLE = result.title
    USRNAM = result.username if "username" in result else "None"
except:
    BIA = False

try:
    member = bot.getChatMember(CH, u)
    UC = member.status
except:
    BIA = False
    UC = "error"

if USRNAM == "None":
    USRNAM = str(TGID)
else:
    USRNAM = "@" + USRNAM

if CLink == "None":
    CLink = f"https://t.me/{str(TGID)}"
    Txt += f"<b>🚨 Bot Not Admin In {CH} 🚨</b>\n\n<b>🔗 Channel Link Not Found.</b>"
    BIA = False
else:
    Txt += f"<b>{'🎉 Bot Is Admin In' if BIA else '🚨 Bot Not Admin In'} {CH}</b>\n\n<b>🔗 Channel Link Successfully Added Automatically!</b>"


if BIA:
    Bot.saveData("Botpaychannel", msg)
    Txt += f"\n\n<b>✅ New Payout Channel Added: {CH}</b>"
else:
    Txt += f"\n\n<b>❌ Channel Not Added Because Bot Is Not Admin</b>"

markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/admin"}]
    ]
}

bot.replyText(
    u,
    Txt,
    reply_markup=markup,
    disable_web_page_preview=True
)


#======================================================================
# COMMAND: /SetBotPayComm0
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []

is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🔰 Send Your Payment Comment :</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SetBotPayComm01")


#======================================================================
# COMMAND: /SetBotPayComm01
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")
push = AllBotAdminss if AllBotAdminss else []
is_Admin = str(message.chat.id) in [str(userid) for userid in push]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv": "VSV Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()


Bot.saveData("BotPayComm", msg)


markup = {
    "inline_keyboard": [
        [{"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}]
    ]
}

bot.replyText(
    u,
    f"<b>✅ Bot Payout Comment Set : {msg}</b>",
    reply_markup=markup,
    disable_web_page_preview=True
)

raise ReturnCommand()


#======================================================================
# COMMAND: /SetBotUPIkey
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss")

if AllBotAdminss is None:
    push = []
else:
    push = AllBotAdminss

is_Admin = False
for userid in push:
    if str(message.chat.id) == str(userid):
        is_Admin = True

if not is_Admin:
    bot.replyText(
        message.chat.id,
        "<b>🚫 You Are Not Bot Admin</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ================== GATEWAY INFO ==================

Gatewaysett0 = Bot.getData("gatewaynow") or "not set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"

gateway_names = {
    "payzy1": "💎 Payzy Wallet",
    "vsv1": "🏦 VSV Wallet"
}

Gatewaysett20 = gateway_names.get(Gatewaysett0, "❌ Not Set")

if Gatewaysett0 == "not set":
    bot.replyText(
        message.chat.id,
        "<b>⚠️ Gateway Not Selected</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()
    
# ================== STATUS CHECK ==================

Token = Bot.getData("TOKEN")
CheckToken = "🟢" if Token else "🔴"

# ================== CATEGORY ==================

vsv = ["vsv1"]
payzy = ["payzy1"]

markup = InlineKeyboardMarkup()

# Header Row
markup.add(
    InlineKeyboardButton(text=Gatewaysett20, callback_data='/none'),
    InlineKeyboardButton(text="⚙️ ACTIVE", callback_data='/none')
)


# ================== BUTTON LOGIC ==================

if Gatewaysett0 in vsv:
    markup.add(
        InlineKeyboardButton(
            text=f"{CheckToken} Set Token",
            callback_data='/selegetwayonbbo1t'
        )
    )

elif Gatewaysett0 in payzy:
    markup.add(
        InlineKeyboardButton(
            text=f"{CheckToken} Set Token",
            callback_data='/payzy_token'
        ))
        


# Back Button
markup.add(
    InlineKeyboardButton(
        text="🔙 Back",
        callback_data='/addgetwayonbbot'
    )
)


# ================== FINAL MESSAGE ==================

bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"""
<b>⚙️ SET GATEWAY DETAILS</b>

🏦 <b>Gateway:</b>
<a href="{Gatewaysett011}">{Gatewaysett20}</a>

<i> Warning ⚠️:- Set Your Token Real</i>

<b>Select Option Below To Set Credentials.</b>
""",
    parse_mode="HTML",
    reply_markup=markup,
    disable_web_page_preview=True
)


#======================================================================
# COMMAND: /SetFund
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()


bot.replyText(
u,
"""<b>Send Fund Change

Example:
+500
-200
</b>""",
parse_mode="html"
)

Bot.handleNextCommand("/SetFund2")


#======================================================================
# COMMAND: /SetFund2
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()


old = float(Bot.getData("LiveFund") or 0)

change = float(message.text)

new = old + change


Bot.saveData(
"LiveFund",
new
)


channel1 = Bot.getData("LiveFundChannel1")
channel2 = Bot.getData("LiveFundChannel2")

msgid1 = Bot.getData("LiveFundMsgID1")
msgid2 = Bot.getData("LiveFundMsgID2")

bot_name = Bot.info().username


# Channel 1
if channel1 and msgid1:

    try:

        bot.editMessageText(
            chat_id=channel1,
            message_id=msgid1,
            text=f"""<b>✅ Total Remaining Fund In @{bot_name} >> ₹{new:.2f}

🚀 This Is A High Fund And Long
Term Running Bot With Huge Funds

💰💰 Loot As Much As You Can 😎🙏

😍 Specially Powered By
{channel1} !!

</b>""",
            parse_mode="html",
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": f"💰 Fund ₹{new:.2f}",
                            "url": f"https://t.me/{bot_name}"
                        }
                    ]
                ]
            }
        )

    except:
        pass


# Channel 2
if channel2 and msgid2:

    try:

        bot.editMessageText(
            chat_id=channel2,
            message_id=msgid2,
            text=f"""<b>✅ Total Remaining Fund In @{bot_name} >> ₹{new:.2f}

🚀 This Is A High Fund And Long
Term Running Bot With Huge Funds

💰💰 Loot As Much As You Can 😎🙏

😍 Specially Powered By
{channel2} !!

</b>""",
            parse_mode="html",
            reply_markup={
                "inline_keyboard": [
                    [
                        {
                            "text": f"💰 Fund ₹{new:.2f}",
                            "url": f"https://t.me/{bot_name}"
                        }
                    ]
                ]
            }
        )

    except:
        pass



bot.replyText(
u,
f"""<b>✅ Fund Updated

Old:
₹{old}

New:
₹{new}
</b>""",
parse_mode="html"
)


#======================================================================
# COMMAND: /SetFundChannel
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()


bot.replyText(
    u,
    "<b>📢 Send Channel Username(s)\n\n"
    "1 Channel:\n"
    "@MyChannel\n\n"
    "2 Channels:\n"
    "@Channel1,@Channel2</b>",
    parse_mode="html"
)

Bot.handleNextCommand("/SaveFundChannel")


#======================================================================
# COMMAND: /SetMinRef
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


mMr=Bot.getData("SetMinRef") or 0
bot.replyText(u,f"""<b>✔️Current Set To {mMr}

⚙️Send New Amount Of Refers Needed To Withdraw</b>""",
parse_mode = "html")

Bot.handleNextCommand("/SetMinRef1")


#======================================================================
# COMMAND: /SetMinRef1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []


r=Bot.getData("SetMinRef") or 0
act=f"Min Refers to Withdraw ({r}) updated to {message.text}"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

Bot.saveData("AdmAC",AdmAC)

 

    
Bot.saveData("SetMinRef",message.text) 

bot.replyText(u,f"""<b>✔️Now {message.text} Verified Refers Needed to Make Withdrawal</b>""",parse_mode = "html")

    


#======================================================================
# COMMAND: /SetMinWithAmont
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in list(map(str, AllBotAdminss)):
    bot.answerCallbackQuery(
        call.id,
        "🚫 You Are Not This Bot Admin"
    )
    raise ReturnCommand()


bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text="""<b>Send Withdraw Limits</b>

<b>Wallet:</b>
<code>Wallet:10-100-5</code>

<b>UPI:</b>
<code>UPI:10-264-0</code>

<b>Both:</b>
<code>Wallet:10-100-5 UPI:10-264-0</code>

<b>Format:</b>
<code>Type:Min-Max-Min Refer</code>""",
    parse_mode="html"
)

Bot.handleNextCommand("/SetAllLimits")


#======================================================================
# COMMAND: /SetPerReferAmont
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()




bot.replyText(
    u,
    "<b>💸 Referral Reward Setup\n\n"
    "✨ Send the <u>amount per refer</u>:\n\n"
    "🔢 Example (random range): <code>1-3</code>\n"
    "💰 Example (fixed amount): <code>1</code>\n\n"
    "⚡ Choose wisely & send now!</b>",
    parse_mode="html"
)


Bot.handleNextCommand("/SetPerReferAmont1")


#======================================================================
# COMMAND: /SetPerReferAmont1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# ---------------- Time ----------------
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

# ---------------- Validation ----------------
text = message.text.strip()

if text.isdigit():
    # ✅ Case 1: Single number
    Bot.saveData("PerRefer", text)
    act = f"Refer Amount updated to {text}"
    bot.replyText(u, f"<b>Refer Amount Updated To {text} Rs.</b>", parse_mode="html")

elif "-" in text:
    parts = text.split("-")
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        min_val, max_val = int(parts[0]), int(parts[1])
        if min_val <= max_val:
            Bot.saveData("PerRefer", text)
            act = f"Refer Range updated to {min_val}-{max_val}"
            bot.replyText(u, f"<b>Refer Amount Range Updated To {min_val}-{max_val} Rs.</b>", parse_mode="html")
        else:
            bot.replyText(u, "⚠️ Minimum refer must be less than or equal to Maximum refer.")
            raise ReturnCommand()
    else:
        bot.replyText(u, "❌ Please enter in correct format: <b>min-max</b> (e.g., 1-3)", parse_mode="html")
        raise ReturnCommand()
else:
    bot.replyText(u, "❌ Please use only numbers or format <b>min-max</b>", parse_mode="html")
    raise ReturnCommand()

# ---------------- Save Action Log ----------------
AdmAC = Bot.getData("AdmAC") or []
AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n"
    f"🔍 <b>Action:</b> {act}"
)
Bot.saveData("AdmAC", AdmAC)

Bot.runCommand("/admin")


#======================================================================
# COMMAND: /SetPerupiAmont1
#======================================================================
# coded by @Jenish_Dobariya1

# ----------- ADMIN CHECK -----------
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


# ----------- TIME FORMAT -----------
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 

year, month, day = date.split("-")
hour, minute = time.split(":")

hour = int(hour)
ampm = "am"

if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


# ----------- INPUT VALIDATION -----------
text = message.text.strip()

token = None
tax = 0

# Case 1: Token-Tax (जैसे: TVJZCUHK-15)
if "-" in text:
    parts = text.split("-")

    if len(parts) != 2 or not parts[0] or not parts[1].isdigit():
        bot.replyText(u, "❌ Invalid format. Use: <b>TVJZCUHK-15</b>", parse_mode="html")
        raise ReturnCommand()

    token = parts[0]
    tax = int(parts[1])

# Case 2: Only Token (बिना टैक्स के, टैक्स = 0)
else:
    token = text
    tax = 0


# ----------- VALIDATE TOKEN LENGTH -----------
# 6-डिजिट वाली पुरानी एरर को हटाने के लिए नियम को लचीला बनाया गया है
if len(token) < 4:
    bot.replyText(u, "❌ Token is too short! Please enter a valid gateway token.", parse_mode="html")
    raise ReturnCommand()


# ----------- SAVE DATA -----------
Bot.saveData("Token1", token)
Bot.saveData("Tax1", tax)

# आपके पूरे विड्रॉल सिस्टम के साथ तालमेल बिठाने के लिए ग्लोबल वेरिएबल्स भी अपडेट किए
Bot.saveData("BotGatewayKey", token)
Bot.saveData("Tax", float(tax))

act = f"Token = {token}, Tax = {tax}%"


# ----------- RESPONSE -----------
bot.replyText(
    u,
    f"<b>✅ Saved Successfully</b>\n\n🔑 Token: <code>{token}</code>\n💸 Tax: {tax}%",
    parse_mode="html"
)


# ----------- SAVE ADMIN ACTION LOG -----------
AdmAC = Bot.getData("AdmAC") or []

AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👤 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n"
    f"⚙️ <b>Action:</b> {act}"
)

Bot.saveData("AdmAC", AdmAC)


# ----------- BACK TO ADMIN PANEL -----------
Bot.runCommand("/admin")


#======================================================================
# COMMAND: /SetTaxAmont
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(userid) for userid in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

bot.replyText(
    u,
    """<b>⚖️ Gateway Tax Setup</b>

Send Gateway Name & Tax ₹

<b>Format:</b>
<code>VSV 5</code>

<b>Example:</b>
<code>Ultra 3</code>
<code>Payzy 4</code>
<code>TXG 2.5</code>
<code>Rupix 6</code>""",
    parse_mode="HTML"
)

Bot.handleNextCommand("/SetTaxAmont1")


#======================================================================
# COMMAND: /SetTaxAmont1
#======================================================================
AllBotAdminss=Bot.getData("AllBotAdminss") or []

if str(u) not in [str(userid) for userid in AllBotAdminss]:
    bot.replyText(u,"<b><i>🚫 You Are Not This Bot Admin</i></b>",parse_mode="HTML")
    raise ReturnCommand()

text=str(message.text).strip()
parts=text.split()

if not parts or len(parts)%2!=0:
    bot.replyText(u,"""<b>❌ Invalid Format</b>

<code>VSV 5</code>
<code>VSV 5 Ultra 3 Payzy 2 TXG 4 Rupix 1</code>""",parse_mode="HTML")
    Bot.handleNextCommand("/SetTaxAmont1")
    raise ReturnCommand()

gateway_keys={
    "vsv":"vsvtax",
    "ultra":"ultratax",
    "ultrapay":"ultratax",
    "payzy":"payzytax",
    "txg":"txgtax",
    "rupix":"rupixtax"
}

gateway_names={
    "vsv":"VSV",
    "ultra":"Ultra Pay",
    "ultrapay":"Ultra Pay",
    "payzy":"Payzy",
    "txg":"TXG",
    "rupix":"Rupix"
}

saved=[]
errors=[]

for i in range(0,len(parts),2):
    gateway=str(parts[i]).strip().lower()
    tax_text=str(parts[i+1]).strip()

    tax_key=gateway_keys.get(gateway)

    if not tax_key:
        errors.append("<code>"+str(parts[i])+"</code> - Invalid Gateway")
        continue

    try:
        tax=float(tax_text)
    except:
        errors.append("<code>"+str(parts[i])+"</code> - Invalid Tax")
        continue

    if tax<0:
        errors.append("<code>"+str(parts[i])+"</code> - Tax cannot be below 0%")
        continue

    if tax>100:
        errors.append("<code>"+str(parts[i])+"</code> - Tax cannot exceed 100%")
        continue

    Bot.saveData(tax_key,tax)

    if tax==int(tax):
        tax_display=str(int(tax))
    else:
        tax_display=str(tax)

    gateway_name=gateway_names.get(gateway,gateway)

    saved.append("🏦 <b>"+gateway_name+"</b> → <b>"+tax_display+"₹</b>")


if not saved and errors:
    bot.replyText(u,"<b>❌ No Tax Updated</b>\n\n"+"\n".join(errors),parse_mode="HTML")
    Bot.handleNextCommand("/SetTaxAmont1")
    raise ReturnCommand()


now=libs.DateAndTime.now("Asia/Kolkata")
date=now["date"]
time=now["time"][:5]

year,month,day=date.split("-")
hour,minute=time.split(":")
hour=int(hour)

ampm="am"

if hour>=12:
    ampm="pm"

if hour>12:
    hour-=12

if hour==0:
    hour=12

MONTHS={
    "01":"Jan","02":"Feb","03":"Mar",
    "04":"Apr","05":"May","06":"Jun",
    "07":"Jul","08":"Aug","09":"Sep",
    "10":"Oct","11":"Nov","12":"Dec"
}

EasyTime=f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"

AdmAC=Bot.getData("AdmAC") or []

act="Gateway Tax Updated\n"+"\n".join(saved)

AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n"
    f"🔍 <b>Action:</b> {act}"
)

Bot.saveData("AdmAC",AdmAC)

msg="<b>✅ Gateway Tax Updated</b>\n\n"+"\n".join(saved)

if errors:
    msg+="\n\n<b>⚠️ Errors:</b>\n"+"\n".join(errors)

bot.replyText(u,msg,parse_mode="HTML")

raise ReturnCommand()


#======================================================================
# COMMAND: /Set_Key_Default
#======================================================================
# coded by @Jenish_Dobariya1
if not params: raise ReturnCommand()
gw_key = str(params).strip()
Bot.saveData("gatewaynow", gw_key)

# Dynamic Unique Status Check
GUID = Bot.getData("GUID_" + gw_key)
CheckGUID = "🟢" if GUID else "🔴"
MIDD = Bot.getData("MID_" + gw_key)
CheckMIDD = "🟢" if MIDD else "🔴"
MKEY = Bot.getData("MKEY_" + gw_key)
CheckMKEY = "🟢" if MKEY else "🔴"

markup = InlineKeyboardMarkup()
markup.row(
    InlineKeyboardButton(text=f"{CheckGUID} Set GUID", callback_data='/SetBotGatewayKeyguid'),
    InlineKeyboardButton(text=f"{CheckMIDD} Set MID", callback_data='/SetBotGatewayKeymiid')
)
markup.add(InlineKeyboardButton(text=f"{CheckMKEY} Set MKEY", callback_data='/SetBotGatewayKeymeyy'))
markup.add(InlineKeyboardButton(text="🔙 Back to List", callback_data='/SetBotGatewayKey'))

# ================== GATEWAY MAPPING ==================
gateway_names = {
    "vsv": "🏦 VSV Wallet",
    "Tgwallet": "🤖 TG Wallet",
    "lifafawala": "🎁 LifafaWala",
    "VIP": "👑 VIP Wallet",
    "e": "📤 E Wallet"
}

# Agar list me naam na mile to fallback ke liye key ko hi uppercase me dikha dega
full_gateway_name = gateway_names.get(gw_key, gw_key.upper())

# ================== FINAL MESSAGE ==================
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"<b>⚙️ TOKEN BASED SETUP</b>\n\n🏦 <b>Active Gateway:</b> {full_gateway_name}\n\n<i>Set Your Gateway Token 👇🏻👇🏻</i>",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /Set_Key_Number
#======================================================================
# coded by @Jenish_Dobariya1
if not params: raise ReturnCommand()
gw_key = str(params).strip()
Bot.saveData("gatewaynow", gw_key)

# Dynamic Unique Status Check
MY = Bot.getData("API_" + gw_key)
CheckM = "🟢" if MY else "🔴"
NUM = Bot.getData("NUM_" + gw_key)
CheckNUM = "🟢" if NUM else "🔴"
KEY = Bot.getData("KEY_" + gw_key)
CheckKEY = "🟢" if KEY else "🔴"

markup = InlineKeyboardMarkup()
markup.row(
    InlineKeyboardButton(text=f"{CheckM} Set API", callback_data='/SetBotGatewayKeytokken'),
    InlineKeyboardButton(text=f"{CheckNUM} Set Number", callback_data='/SetBotGatewayKeynum')
)
markup.add(InlineKeyboardButton(text=f"{CheckKEY} Set Key", callback_data='/SetBotGatewayKeykey'))
markup.add(InlineKeyboardButton(text="🔙 Back to List", callback_data='/SetBotGatewayKey'))

# ================== GATEWAY MAPPING ==================
gateway_names = {
    "vsv": "🏦 VSV Wallet",
    "Tgwallet": "🤖 TG Wallet",
    "lifafawala": "🎁 LifafaWala",
    "VIP": "👑 VIP Wallet",
    "e": "📤 E Wallet"
}

# Agar list me naam na mile to fallback ke liye key ko hi uppercase me dikha dega
full_gateway_name = gateway_names.get(gw_key, gw_key.upper())

# ================== FINAL MESSAGE ==================
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"<b>⚙️ TOKEN BASED SETUP</b>\n\n🏦 <b>Active Gateway:</b> {full_gateway_name}\n\n<i>Set Your Gateway Token 👇🏻👇🏻</i>",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /Set_Key_Secret
#======================================================================
# coded by @Jenish_Dobariya1
if not params: raise ReturnCommand()
gw_key = str(params).strip()
Bot.saveData("gatewaynow", gw_key)

# Dynamic Unique Status Check
MY = Bot.getData("SECRETKEY")
CheckM = "🟢" if MY else "🔴"
KEY = Bot.getData("KEY_" + gw_key)
CheckKEY = "🟢" if KEY else "🔴"

markup = InlineKeyboardMarkup()
markup.add(InlineKeyboardButton(text=f"{CheckM} Set API Secret", callback_data='/SetBotGatewayKeysapi'))
markup.add(InlineKeyboardButton(text=f"{CheckKEY} Set API Key", callback_data='/SetBotGatewayKeykey'))
markup.add(InlineKeyboardButton(text="🔙 Back to List", callback_data='/SetBotGatewayKey'))

# ================== GATEWAY MAPPING ==================
gateway_names = {
    "vsv": "🏦 VSV Wallet",
    "Tgwallet": "🤖 TG Wallet",
    "lifafawala": "🎁 LifafaWala",
    "VIP": "👑 VIP Wallet",
    "e": "📤 E Wallet"
}

# Agar list me naam na mile to fallback ke liye key ko hi uppercase me dikha dega
full_gateway_name = gateway_names.get(gw_key, gw_key.upper())

# ================== FINAL MESSAGE ==================
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"<b>⚙️ TOKEN BASED SETUP</b>\n\n🏦 <b>Active Gateway:</b> {full_gateway_name}\n\n<i>Set Your Gateway Token 👇🏻👇🏻</i>",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /Set_Key_Tk
#======================================================================
# coded by @Jenish_Dobariya1

if not params:
    raise ReturnCommand()

gw_key = str(params).strip()
Bot.saveData("gatewaynow", gw_key)

# ================== DYNAMIC STATUS CHECK ==================
KEY = Bot.getData("KEY_" + gw_key)
CheckKEY = "🟢" if KEY else "🔴"

Token = Bot.getData("TOKEN_" + gw_key)
CheckToken = "🟢" if Token else "🔴"

markup = InlineKeyboardMarkup()

# ================== GATEWAY SETUP BUTTONS ==================
# KEY ONLY GATEWAYS
if gw_key in ["unio", "rupix"]:

    markup.add(
        InlineKeyboardButton(
            text=f"{CheckKEY} Set Key",
            callback_data="/SetBotGatewayKeykey"
        )
    )

# KEY + TOKEN GATEWAYS
else:

    markup.add(
        InlineKeyboardButton(
            text=f"{CheckKEY} Set Key",
            callback_data="/SetBotGatewayKeykey"
        )
    )

    markup.add(
        InlineKeyboardButton(
            text=f"{CheckToken} Set Token",
            callback_data="/SetBotGatewayKeytokken"
        )
    )

markup.add(
    InlineKeyboardButton(
        text="🔙 Back to List",
        callback_data="/SetBotGatewayKey"
    )
)

# ================== GATEWAY MAPPING ==================
gateway_names = {
    "vsv": "🏦 VSV Wallet",
    "Tgwallet": "🤖 TG Wallet",
    "lifafawala": "🎁 LifafaWala",
    "VIP": "👑 VIP Wallet",
    "e": "📤 E Wallet",
    "unio": "💳 Unio",
    "aura": "✨ Aura"
}

full_gateway_name = gateway_names.get(
    gw_key,
    gw_key.upper()
)

# ================== SETUP TEXT ==================
if gw_key in ["unio", "aura"]:
    setup_text = "Set Your Gateway Key 👇🏻👇🏻"
else:
    setup_text = "Set Your Gateway Key & Token 👇🏻👇🏻"

# ================== FINAL MESSAGE ==================
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"""
<b>⚙️ TOKEN BASED SETUP</b>

🏦 <b>Active Gateway:</b> {full_gateway_name}

<i>{setup_text}</i>
""",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /Set_Key_Token
#======================================================================
# coded by @Jenish_Dobariya1
if not params: raise ReturnCommand()
gw_key = str(params).strip()
Bot.saveData("gatewaynow", gw_key)

# Dynamic Unique Status Check
Token = Bot.getData("TOKEN_" + gw_key)
CheckToken = "🟢" if Token else "🔴"

markup = InlineKeyboardMarkup()
# Button dabaane par value isi unique gateway ke database path me save hogi
markup.add(InlineKeyboardButton(text=f"{CheckToken} Set Token", callback_data='/SetBotGatewayKeytokken'))
markup.add(InlineKeyboardButton(text="🔙 Back to List", callback_data='/SetBotGatewayKey'))

# ================== GATEWAY MAPPING ==================
gateway_names = {
    "vsv": "🏦 VSV Wallet",
    "Tgwallet": "🤖 TG Wallet",
    "lifafawala": "🎁 LifafaWala",
    "VIP": "👑 VIP Wallet",
    "e": "📤 E Wallet",
    "payzy": "💀 Payzy Wallet"
}

# Agar list me naam na mile to fallback ke liye key ko hi uppercase me dikha dega
full_gateway_name = gateway_names.get(gw_key, gw_key.upper())

# ================== FINAL MESSAGE ==================
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text=f"<b>⚙️ TOKEN BASED SETUP</b>\n\n🏦 <b>Active Gateway:</b> {full_gateway_name}\n\n<i>Set Your Gateway Token 👇🏻👇🏻</i>",
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /TalkUser
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()

bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text="""<b>💬 TALK WITH USER</b>
━━━━━━━━━━━━━━━━━━
🆔 <b>Send User ID & Message</b>

<i>Example:</i> <code>6925391837 Hello!! How Are You?</code>

❌ Send <code>cancel</code> to cancel.""",
    parse_mode="HTML"
)

Bot.handleNextCommand("/TalkUser2")


#======================================================================
# COMMAND: /TalkUser2
#======================================================================
admins = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, admins):
    raise ReturnCommand()

data = message.text.split(" ", 1)

# Cancel
if message.text.strip().lower() == "cancel":
    Bot.runCommand("/admin")
    raise ReturnCommand()

if len(data) < 2:
    bot.sendMessage(
        chat_id=u,
        text="""<b>❌ INVALID FORMAT</b>
━━━━━━━━━━━━━━━━━━

Use:
<code>UserID Message</code>

Example:
<code>123456789 Hello, how can I help you?</code>""",
        parse_mode="HTML"
    )

    raise ReturnCommand()

user_id = data[0]
text = data[1]

if not user_id.lstrip("-").isdigit():
    bot.sendMessage(
        chat_id=u,
        text="<b>❌ Invalid User ID!</b>",
        parse_mode="HTML"
    )

    Bot.handleNextCommand("/TalkUser2")
    raise ReturnCommand()

try:

    bot.sendMessage(
        chat_id=user_id,
        text=f"""<b>💬 MESSAGE FROM ADMIN</b>

━━━━━━━━━━━━━━━━━━

{text}

━━━━━━━━━━━━━━━━━━""",
        parse_mode="HTML"
    )

    bot.sendMessage(
        chat_id=u,
        text=f"""<b>✅ MESSAGE SENT</b>
━━━━━━━━━━━━━━━━━━

🆔 <b>User:</b> <code>{user_id}</code>

💬 <b>Message:</b> {text}

━━━━━━━━━━━━━━━━━━""",
        parse_mode="HTML",
        reply_markup={
            "inline_keyboard": [
                [
                    {
                        "text": "💬 Send Another",
                        "callback_data": "/TalkUser"
                    },
                    {
                        "text": "🔙 Admin Panel",
                        "callback_data": "/admin"
                    }
                ]
            ]
        }
    )

except:

    bot.sendMessage(
        chat_id=u,
        text=f"""<b>❌ MESSAGE FAILED</b>

━━━━━━━━━━━━━━━━━━

🆔 User: <code>{user_id}</code>

<i>The user may have blocked the bot or the ID may be invalid.</i>""",
        parse_mode="HTML",
        reply_markup={
            "inline_keyboard": [
                [
                    {
                        "text": "🔄 Try Again",
                        "callback_data": "/TalkUser"
                    },
                    {
                        "text": "🔙 Back",
                        "callback_data": "/admin"
                    }
                ]
            ]
        }
    )


#======================================================================
# COMMAND: /ToggleSameUPI
#======================================================================
# coded by @Jenish_Dobariya1

# ================== ADMIN CHECK ==================

Admins = Bot.getData("AllBotAdminss") or []

if not isinstance(Admins, list):
    Admins = [Admins]

if str(message.chat.id) not in list(map(str, Admins)):
    bot.answerCallbackQuery(
        callback_query_id=call.id,
        text="🚫 Access Denied",
        show_alert=True
    )
    raise ReturnCommand()


# ================== TOGGLE ==================

SameUPI = Bot.getData("SameUPI") or "ON"

if SameUPI == "ON":
    NewStatus = "OFF"
    AlertText = "♻️ Same UPI Disabled"
else:
    NewStatus = "ON"
    AlertText = "♻️ Same UPI Enabled"

Bot.saveData("SameUPI", NewStatus)


# ================== CALLBACK ALERT ==================

try:
    bot.answerCallbackQuery(
        callback_query_id=call.id,
        text=AlertText,
        show_alert=False
    )
except:
    pass


# ================== LOAD DATA ==================

Botpayname = Bot.getData("Botpayname") or "Payment"
SameWallet = Bot.getData("SameWallet") or "ON"

if SameWallet not in ["ON", "OFF"]:
    SameWallet = "ON"
    Bot.saveData("SameWallet", SameWallet)


# ================== STATUS ==================

if SameWallet == "ON":
    WalletStatus = "🟢 ON"
    WalletDesc = "Multiple users can use the same wallet"
else:
    WalletStatus = "🔴 OFF"
    WalletDesc = "One wallet can be linked to only one user"


if NewStatus == "ON":
    UPIStatus = "🟢 ON"
    UPIDesc = "Multiple users can use the same UPI"
else:
    UPIStatus = "🔴 OFF"
    UPIDesc = "One UPI can be linked to only one user"


# ================== KEYBOARD ==================

markup = InlineKeyboardMarkup()

markup.add(
    InlineKeyboardButton(
        text='🌐 Select Gateway (Wallet)',
        callback_data='/selegetwayonbbot'
    ),
    InlineKeyboardButton(
        text='🔑 Set Payout Keys',
        callback_data='/SetBotGatewayKey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'✨ Payment Message: {Botpayname}',
        callback_data='/SetBotPayComm0'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same Wallet: {WalletStatus}',
        callback_data='/ToggleSameWallet'
    )
)

markup.add(
    InlineKeyboardButton(
        text='🌐 Add Gateway (UPI)',
        callback_data='/test'
    ),
    InlineKeyboardButton(
        text='Set UPI Gateway Keys 🔐',
        callback_data='/SetBotUPIkey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same UPI: {UPIStatus}',
        callback_data='/ToggleSameUPI'
    )
)

markup.add(
    InlineKeyboardButton(
        text='🔙 Back To Admin Panel',
        callback_data='/admin'
    )
)


# ================== MESSAGE ==================

text = f"""
<b>╔══════════════════════╗
        🛠 ADMIN SETTINGS
╚══════════════════════╝</b>

👤 <b>Admin:</b> {call.from_user.first_name}
🆔 <b>Chat ID:</b> {call.message.chat.id}

━━━━━━━━━━━━━━━━━━━
<b>💳 WALLET SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> Wallet Gateway
♻️ <b>Same Wallet:</b> {WalletStatus}

<i>💡 {WalletDesc}</i>

━━━━━━━━━━━━━━━━━━━
<b>💸 UPI SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> UPI Gateway
♻️ <b>Same UPI:</b> {UPIStatus}

<i>💡 {UPIDesc}</i>

━━━━━━━━━━━━━━━━━━━
⚙️ <b>Manage Gateway & Payment Settings</b>
━━━━━━━━━━━━━━━━━━━
"""


# ================== EDIT ==================

try:
    bot.editMessageText(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="HTML",
        reply_markup=markup
    )
except:
    pass


#======================================================================
# COMMAND: /ToggleSameWallet
#======================================================================
# coded by @Jenish_Dobariya1

# ================== ADMIN CHECK ==================

Admins = Bot.getData("AllBotAdminss") or []

if not isinstance(Admins, list):
    Admins = [Admins]

if str(message.chat.id) not in list(map(str, Admins)):
    bot.answerCallbackQuery(
        callback_query_id=call.id,
        text="🚫 Access Denied",
        show_alert=True
    )
    raise ReturnCommand()


# ================== TOGGLE ==================

SameWallet = Bot.getData("SameWallet") or "ON"

if SameWallet == "ON":
    NewStatus = "OFF"
    AlertText = "♻️ Same Wallet Disabled"
else:
    NewStatus = "ON"
    AlertText = "♻️ Same Wallet Enabled"

Bot.saveData("SameWallet", NewStatus)


# ================== CALLBACK ALERT ==================

try:
    bot.answerCallbackQuery(
        callback_query_id=call.id,
        text=AlertText,
        show_alert=False
    )
except:
    pass


# ================== LOAD DATA ==================

Botpayname = Bot.getData("Botpayname") or "Payment"
SameUPI = Bot.getData("SameUPI") or "ON"

if SameUPI not in ["ON", "OFF"]:
    SameUPI = "ON"
    Bot.saveData("SameUPI", SameUPI)


# ================== STATUS ==================

if NewStatus == "ON":
    WalletStatus = "🟢 ON"
    WalletDesc = "Multiple users can use the same wallet"
else:
    WalletStatus = "🔴 OFF"
    WalletDesc = "One wallet can be linked to only one user"


if SameUPI == "ON":
    UPIStatus = "🟢 ON"
    UPIDesc = "Multiple users can use the same UPI"
else:
    UPIStatus = "🔴 OFF"
    UPIDesc = "One UPI can be linked to only one user"


# ================== KEYBOARD ==================

markup = InlineKeyboardMarkup()

markup.add(
    InlineKeyboardButton(
        text='🌐 Select Gateway (Wallet)',
        callback_data='/selegetwayonbbot'
    ),
    InlineKeyboardButton(
        text='🔑 Set Payout Keys',
        callback_data='/SetBotGatewayKey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'✨ Payment Message: {Botpayname}',
        callback_data='/SetBotPayComm0'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same Wallet: {WalletStatus}',
        callback_data='/ToggleSameWallet'
    )
)

markup.add(
    InlineKeyboardButton(
        text='🌐 Add Gateway (UPI)',
        callback_data='/test'
    ),
    InlineKeyboardButton(
        text='Set UPI Gateway Keys 🔐',
        callback_data='/SetBotUPIkey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same UPI: {UPIStatus}',
        callback_data='/ToggleSameUPI'
    )
)

markup.add(
    InlineKeyboardButton(
        text='🔙 Back To Admin Panel',
        callback_data='/admin'
    )
)


# ================== MESSAGE ==================

text = f"""
<b>╔══════════════════════╗
        🛠 ADMIN SETTINGS
╚══════════════════════╝</b>

👤 <b>Admin:</b> {call.from_user.first_name}
🆔 <b>Chat ID:</b> {call.message.chat.id}

━━━━━━━━━━━━━━━━━━━
<b>💳 WALLET SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> Wallet Gateway
♻️ <b>Same Wallet:</b> {WalletStatus}

<i>💡 {WalletDesc}</i>

━━━━━━━━━━━━━━━━━━━
<b>💸 UPI SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> UPI Gateway
♻️ <b>Same UPI:</b> {UPIStatus}

<i>💡 {UPIDesc}</i>

━━━━━━━━━━━━━━━━━━━
⚙️ <b>Manage Gateway & Payment Settings</b>
━━━━━━━━━━━━━━━━━━━
"""


# ================== EDIT ==================

try:
    bot.editMessageText(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        parse_mode="HTML",
        reply_markup=markup
    )
except:
    pass


#======================================================================
# COMMAND: /ToggleUpi
#======================================================================
# coded by @Jenish_Dobariya1
current = Bot.getData("UpiWithdrawMode") or "ON"

if str(current).upper() == "ON":
    Bot.saveData("UpiWithdrawMode", "OFF")
    Bot.saveData("UpiWithdraw", "OFF") # Backup security
else:
    Bot.saveData("UpiWithdrawMode", "ON")
    Bot.saveData("UpiWithdraw", "ON") # Backup security

# Screen ko turant refresh karein
Bot.runCommand("/WithdrawStatus")


#======================================================================
# COMMAND: /ToggleWallet
#======================================================================
# coded by @Jenish_Dobariya1
current = Bot.getData("WalletWithdrawMode") or "ON"

if str(current).upper() == "ON":
    Bot.saveData("WalletWithdrawMode", "OFF")
    Bot.saveData("WalletWithdraw", "OFF") # Purane checks ke liye backup
else:
    Bot.saveData("WalletWithdrawMode", "ON")
    Bot.saveData("WalletWithdraw", "ON") # Purane checks ke liye backup

# Screen ko turant refresh karein
Bot.runCommand("/WithdrawStatus")


#======================================================================
# COMMAND: /Top30Referral
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# TOP 30 REFERRAL LEADERBOARD
# 10 USERS PER PAGE

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
        break


Full = Bot.getData("FulBotUsrs")

if not Full:

    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text="⬅️ Back",
            callback_data="/AdminStats"
        )
    )

    bot.editMessageText(
        chat_id=u,
        message_id=call.message.message_id,
        text="<b>😳 No Top Users Available</b>",
        parse_mode="HTML",
        reply_markup=markup
    )

    raise ReturnCommand()


# =========================
# GET PAGE NUMBER
# =========================

page = 1

try:
    if len(params) > 0:
        page = int(params[0])
except:
    page = 1

if page < 1:
    page = 1


# =========================
# GET REFERRAL DATA
# =========================

FullUsrsRefC = []

for i in Full:

    c = Bot.getData(str(i) + "RefCount")

    if c is None:
        c = 0

    try:
        c = int(c)
    except:
        c = 0

    if c > 0:
        FullUsrsRefC.append((i, c))


# Highest referrals first
FullUsrsRefC.sort(
    key=lambda x: x[1],
    reverse=True
)


# =========================
# TOP 30 ONLY
# =========================

top_users = FullUsrsRefC[:30]


# =========================
# PAGINATION
# =========================

per_page = 10

total_users = len(top_users)

total_pages = (total_users + per_page - 1) // per_page

if total_pages < 1:
    total_pages = 1

if page > total_pages:
    page = total_pages

start = (page - 1) * per_page
end = start + per_page

page_users = top_users[start:end]

# =========================
# MESSAGE
# =========================

m = (
    f"<b>🏆 Top 30 Users With Most Refers</b>\n"
    f"<i>Page {page}/{total_pages}</i>\n\n"
)


# =========================
# RANK EMOJIS
# =========================

dec = [
    "🥇", "🥈", "🥉",
    "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟",
    "11", "12", "13", "14", "15",
    "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25",
    "26", "27", "28", "29", "30"
]


# =========================
# SHOW USERS
# =========================

for index, (user_id, ref_count) in enumerate(page_users):

    rank = start + index

    UID = str(user_id)

    hide_wallet = (
        UID[0:2] + "*****" + UID[-3:]
        if len(UID) >= 5
        else "*****"
    )

    if is_Admin:

        usr = (
            f'<a href="tg://user?id={user_id}">'
            f'{user_id}</a>'
        )

    else:

        usr = (
            f"<b>{hide_wallet}</b>"
        )


    m += (
        f"{dec[rank]} <b>Top {rank + 1}</b>\n"
        f"   User ID: {usr}\n"
        f"   Verified Referrals: <b>{ref_count}</b>\n\n"
    )


# =========================
# PAGINATION BUTTONS
# =========================

markup = InlineKeyboardMarkup()


if page > 1:

    markup.row(
        InlineKeyboardButton(
            text="⬅️ Previous",
            callback_data=f"/Top30Referral {page - 1}"
        ),
        InlineKeyboardButton(
            text=f"{page}/{total_pages}",
            callback_data="noop"
        )
    )


if page < total_pages:

    if page == 1:

        markup.row(
            InlineKeyboardButton(
                text=f"{page}/{total_pages}",
                callback_data="noop"
            ),
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"/Top30Referral {page + 1}"
            )
        )

    else:

        markup.row(
            InlineKeyboardButton(
                text="Next ➡️",
                callback_data=f"/Top30Referral {page + 1}"
            )
        )


markup.row(
    InlineKeyboardButton(
        text="⬅️ Back",
        callback_data="/AdminStats"
    )
)


# =========================
# EDIT MESSAGE
# =========================

bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=m,
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /TopBalance
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# TOP 30 BALANCE LEADERBOARD
# 10 USERS PER PAGE - SINGLE COMMAND

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False

for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True
        break

if not is_Admin:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


Full = Bot.getData("FulBotUsrs") or []

if not Full:

    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text="⬅️ Back",
            callback_data="/AdminStats"
        )
    )

    bot.editMessageText(
        chat_id=u,
        message_id=call.message.message_id,
        text="<b>😳 No Top Users Available</b>",
        parse_mode="HTML",
        reply_markup=markup
    )

    raise ReturnCommand()


# =========================
# GET PAGE
# =========================

page = 1

try:
    data = call.data or ""

    if " " in data:
        page = int(data.split(" ")[1])

except:
    page = 1


# =========================
# GET BALANCE DATA
# =========================

FullUsrsBalC = []

for user_id in Full:

    bal = libs.Resources.anotherRes(
        "Balance",
        user=user_id
    ).value()

    if bal is None:
        bal = 0

    try:
        bal = float(bal)
    except:
        bal = 0

    if bal > 0:
        FullUsrsBalC.append(
            (user_id, bal)
        )


# Highest balance first
FullUsrsBalC.sort(
    key=lambda x: x[1],
    reverse=True
)


# =========================
# TOP 30 ONLY
# =========================

top_users = FullUsrsBalC[:30]


# =========================
# PAGE SYSTEM
# =========================

per_page = 10

total_users = len(top_users)

total_pages = (
    (total_users + per_page - 1)
    // per_page
)

if total_pages < 1:
    total_pages = 1

if page < 1:
    page = 1

if page > total_pages:
    page = total_pages


start = (page - 1) * per_page
end = start + per_page

page_users = top_users[start:end]


# =========================
# MESSAGE
# =========================

m = (
    "<b>😍 Top Users With Most Balance :</b>\n"
    f"<i>Page {page}/{total_pages}</i>\n\n"
)


medals = [
    "🥇", "🥈", "🥉",
    "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟",
    "11", "12", "13", "14", "15",
    "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25",
    "26", "27", "28", "29", "30"
]


for index, (user_id, bal) in enumerate(page_users):

    rank = start + index

    usr = (
        f'<b><a href="tg://user?id={user_id}">'
        f'{user_id}</a></b>'
    )

    m += (
        f"{medals[rank]} {usr} - ₹ {bal:g}\n"
    )


# =========================
# BUTTONS
# =========================

markup = InlineKeyboardMarkup()


if page > 1:

    markup.row(
        InlineKeyboardButton(
            text="⬅️ Previous",
            callback_data=f"/TopBalance {page - 1}"
        ),
        InlineKeyboardButton(
            text=f"📄 {page}/{total_pages}",
            callback_data="noop"
        )
    )


elif page == 1:

    markup.row(
        InlineKeyboardButton(
            text=f"📄 {page}/{total_pages}",
            callback_data="noop"
        )
    )


if page < total_pages:

    markup.row(
        InlineKeyboardButton(
            text="Next ➡️",
            callback_data=f"/TopBalance {page + 1}"
        ))


markup.row(
    InlineKeyboardButton(
        text="⬅️ Back",
        callback_data="/AdminStats"
    )
)


# =========================
# EDIT MESSAGE
# =========================

bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=m,
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: /TopReferral
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss")
if AllBotAdminss==None:
    push = []
else:
    push = AllBotAdminss

is_Admin = False
for userid in push:
    if str(u) == str(userid):
        is_Admin = True




Full = Bot.getData("FulBotUsrs")

m = "<b>😍Top Users With Most Refers :\n\n</b>"

if not Full:  
    bot.sendMessage("<b>😳 No Top Users Available</b>")
    raise ReturnCommand()

FullUsrsRefC = []

for i in Full:
    c = Bot.getData(str(i) + "RefCount")
    if c is None:
        c = 0
    FullUsrsRefC.append((i, c))  

FullUsrsRefC.sort(key=lambda x: x[1], reverse=True)

s=Bot.getData("LdrbrdSize") or 5

top_users = FullUsrsRefC[:int(s)]

dec = ["🥇", "🥈", "🥉", "4⃣", "5⃣","6️⃣","7️⃣","8️⃣️","9️⃣","🔟"]

n = 0
for user_id, ref_count in top_users:
    
    if ref_count > 0 and Bot.getData("LdrbrdBanUsr") != user_id:
        UID = str(user_id)
        hide_wallet = f"{UID[0:2]}*****{UID[7:10]}"
        usr = "<b>"+UID[:3] +"****" +UID[-2:]+"</b>"

        if is_Admin==True:
            usr = f'<b><a href="tg://user?id={user_id}">{user_id}</a></b>'
        
        m += f"{dec[n]} <b>Top {n+1}:</b>\n   User ID: {hide_wallet}\n   Verified Referrals: {ref_count}\n\n"
        n += 1




bot.sendMessage(f"<b>{m}</b>")
ss=Bot.getData("LdrbrdTxt") or "0"
if ss!="0":
    bot.sendMessage(f"<b>{ss}</b>")


#======================================================================
# COMMAND: /TopWithdraw_UPI
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


Full = Bot.getData("FulBotUsrs") or []

if not Full:
    bot.sendMessage(
        chat_id=u,
        text="<b>😳 No Top UPI Available</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


m = "<b>😍 Top UPI With Most Withdrawals :</b>\n\n"

users = []

for i in Full:
    try:
        count = libs.Resources.anotherRes(
            "Withdraw_UPI",
            user=i
        ).value() or 0

        users.append((i, float(count)))

    except:
        pass


users.sort(
    key=lambda x: x[1],
    reverse=True
)


n = 0

for user_id, amount in users[:10]:

    if amount > 0:

        upi = Bot.getData(
            "UserUPI" + str(user_id)
        ) or "~~~"

        n += 1

        m += (
            f"\n<b>Top {n}</b>"
            f"\nUPI ID: <code>{upi}</code>"
            f"\nTOTAL Amount: {amount}"
            f"\n────────────"
        )


if n == 0:
    m = "<b>😳 No Top UPI Available</b>"

bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text=m,
    parse_mode="HTML",
    reply_markup={
    "inline_keyboard": [
        [
            {
                "text": "Top Withdrawal (Wallet)",
                "callback_data": "/TopWithdraw_Wallet"
            }
        ],
        [
            {
                "text": "⬅️ Back To Admin Panel",
                "callback_data": "/admin"
            }
        ]
    ]
})


#======================================================================
# COMMAND: /TopWithdraw_Wallet
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 

# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here


AllBotAdminss = Bot.getData("AllBotAdminss") or []


if str(u) not in [str(x) for x in AllBotAdminss]:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()


Full = Bot.getData("FulBotUsrs") or []


if not Full:
    bot.sendMessage(
        chat_id=u,
        text="<b>😳 No Top Wallet Available</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()



FullUsrsWithdrwC = []


for i in Full:

    try:
        c = libs.Resources.anotherRes(
            "Withdraw_Wallet",
            user=i
        ).value() or 0

        FullUsrsWithdrwC.append(
            (i, float(c))
        )

    except:
        pass



FullUsrsWithdrwC.sort(
    key=lambda x: x[1],
    reverse=True
)


top_users = FullUsrsWithdrwC[:10]


m = "<b>😍 Top Wallet With Most Withdrawals :</b>\n\n"


n = 0


for user_id, Wbal in top_users:

    if Wbal > 0:

        Wallet = Bot.getData(
            "UserWallet" + str(user_id)
        ) or "~~~"


        n += 1

        m += (
            f"<b>Top {n}</b>\n"
            f"Wallet Address: <code>{Wallet}</code>\n"
            f"TOTAL amount: {Wbal}\n"
            f"────────────\n"
        )


if n == 0:
    m = "<b>😳 No Top Wallet Available</b>"



bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text=m,
    parse_mode="HTML",
    reply_markup={
    "inline_keyboard": [
        [
            {
                "text": "Top Withdrawal (UPI)",
                "callback_data": "/TopWithdraw_UPI"
            }
        ],
        [
            {
                "text": "⬅️ Back To Admin Panel",
                "callback_data": "/admin"
            }
        ]
    ]
})


#======================================================================
# COMMAND: /TopWithdraws
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="html"
    )
    raise ReturnCommand()


Full = Bot.getData("FulBotUsrs")

m = "<b>😍 Top Users With Most Withdrawals:\n\n</b>"

if not Full:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text="<b>😳 No Top Withdrawals Available</b>",
        parse_mode="html"
    )
    raise ReturnCommand()


FullUsrsWithdrwC = []

for i in Full:
    c = libs.Resources.anotherRes('Withdraw', user=i).value()

    if c is None:
        c = 0

    FullUsrsWithdrwC.append((i, c))


FullUsrsWithdrwC.sort(key=lambda x: x[1], reverse=True)

top_users = FullUsrsWithdrwC[:10]

medals = [
    "🥇",
    "🥈",
    "🥉",
    "4⃣",
    "5⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
    "🔟"
]

n = 0

for user_id, Wbal in top_users:

    if Wbal > 0:

        usr = f'<b><a href="tg://user?id={user_id}">{user_id}</a></b>'

        refC = Bot.getData(str(user_id) + "RefCount") or 0

        m += f"""\
{medals[n]} Top {n+1}:
User ID: {usr}
Verified Refers: {refC}
TOTAL amount: {Wbal}
------------
"""

        n += 1


# If no user has any withdrawal
if n == 0:
    m = "<b>😳 No Top Withdrawals Available</b>"


# Edit existing message instead of sending a new one
bot.editMessageText(
    chat_id=u,
    message_id=message.message_id,
    text=m,
    parse_mode="html",
    reply_markup={
        "inline_keyboard": [
            [
                {
                    "text": "‹ Bᴀᴄᴋ",
                    "callback_data": "/AdminStats"
                }
            ]
        ]
    }
)


#======================================================================
# COMMAND: /TransferOwnership
#======================================================================
owner = Bot.getData("Owner")

if str(u) != str(owner):
    bot.replyText(
        u,
        "<b>🚫 Only the bot owner can transfer ownership.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

bot.replyText(
    u,
    "<b>👤 Send the Telegram ID of the new owner.</b>\n\n",
    parse_mode="HTML"
)

Bot.handleNextCommand("/TransferOwnership_Save")


#======================================================================
# COMMAND: /TransferOwnership_Save
#======================================================================
owner = Bot.getData("Owner")

if str(u) != str(owner):
    raise ReturnCommand()

new_owner = message.text.strip()

if not new_owner.isdigit():
    bot.replyText(
        u,
        "<b>❌ Please send a valid Telegram User ID.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

# Cannot transfer to yourself
if str(new_owner) == str(owner):
    bot.replyText(
        u,
        "<b>❌ You are already the owner of this bot.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

# User must have started the bot
users = Bot.getData("FulBotUsrs") or []

if str(new_owner) not in [str(x) for x in users]:
    bot.replyText(
        u,
        "<b>❌ This user hasn't started the bot yet.\n\nAsk them to start the bot first, then try again.</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

# Add to admin list if missing
admins = Bot.getData("AllBotAdminss") or []

if str(new_owner) not in [str(x) for x in admins]:
    admins.append(str(new_owner))
    Bot.saveData("AllBotAdminss", admins)

old_owner = owner
Bot.saveData("Owner", str(new_owner))

bot.replyText(
    u,
    f"""<b>✅ Ownership transferred successfully.

👤 Old Owner:
<code>{old_owner}</code>

👑 New Owner:
<code>{new_owner}</code></b>""",
    parse_mode="HTML"
)

# Notify new owner (ignore errors)
try:
    bot.sendMessage(
        chat_id=new_owner,
        text="<b>👑 Congratulations!\n\nYou are now the owner of this bot.</b>",
        parse_mode="HTML"
    )
except:
    pass


#======================================================================
# COMMAND: /UPIOFF_Text
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

keyboard = ReplyKeyboardMarkup(True)
keyboard.row("⛔ Cancel")

bot.replyText(
    u,
    """<b>💡 Please Send Your UPI Withdraw Mode Off Message

⚠️ Send '<code>Clear</code>' To Remove The Withdraw Mode Off Message</b>""",
    parse_mode="HTML",
    reply_markup=keyboard
)

Bot.handleNextCommand("/UPIOFF_Text1")


#======================================================================
# COMMAND: /UPIOFF_Text1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if message.text == "⛔ Cancel":
    Bot.runCommand("/PIRO_MainMenu", options="<b>⛔ Cancelled Successfully</b>")
    Bot.runCommand("/admin")
    raise ReturnCommand()
    
if message.text.lower() == "clear":
    Bot.saveData("UpiOffText", "")
    
    Bot.runCommand(
        "/PIRO_MainMenu",
        options="<b>✅ UPI OFF Text Cleared Successfully</b>"
    )
    raise ReturnCommand()

Bot.saveData("UpiOffText", message.text)

Bot.runCommand(
    "/PIRO_MainMenu",
    options="<b>✅ UPI OFF Text Changed Successfully</b>"
)    

Bot.saveData("UpiOffText", message.text)


#======================================================================
# COMMAND: /UserKiSabDetails
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

bot.replyText( chat_id = message.chat.id,
    text = f"""<b>💡 Send User Telegram Id To View Details</b>""",
parse_mode = "html")

Bot.handleNextCommand("/UserKiSabDetails1")


#======================================================================
# COMMAND: /UserKiSabDetails1
#======================================================================
# ==============================
# USER DETAILS
# ==============================

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, AllBotAdminss):
    bot.replyText(u, "<b>🚫 You Are Not This Bot Admin</b>", parse_mode="HTML")
    raise ReturnCommand()


# ==============================
# GET USER ID
# ==============================

UID = str(message.text).strip()

if not UID.isdigit():
    bot.replyText(
        u,
        "<b>❌ Invalid User ID</b>\n\n"
        "💡 Please send a numeric Telegram User ID.",
        parse_mode="HTML"
    )
    raise ReturnCommand()

UID = UID.strip()
uid = UID
# Save selected user permanently for buttons
Bot.saveData("ViewingUser_" + str(u), UID)

ref = Bot.getData(str(uid)+"Referral") or "None"
sameDev = Bot.getData(str(uid)+"sameDev") or "no"
is_invited = User.getData("is_invited")

# ==============================
# USER DATA
# ==============================
# ==============================
# REFERRED BY
# ==============================

ref = Bot.getData(str(UID) + "Referral") or "None"

if ref == "None":
    invited = "🤖 Auto Started"
else:
    ref = str(ref)
    invited = f'<a href="tg://user?id={ref}">{ref}</a>'
        
balance = libs.Resources.anotherRes(
    "Balance",
    user=UID
).value() or 0

withdraw = libs.Resources.anotherRes(
    "Withdraw",
    user=UID
).value() or 0

RefStrtC = Bot.getData(UID + "RefStrtC") or 0
refC = Bot.getData(UID + "RefCount") or 0
RefSameDevC = Bot.getData(UID + "RefSameDevC") or 0
RefBonClimC = Bot.getData(UID + "RefBonClimC") or 0
RefWalletLnkC = Bot.getData(UID + "RefWalletLnkC") or 0

pending = int(RefStrtC) - int(refC)

if pending < 0:
    pending = 0


# ==============================
# WALLET
# ==============================

wallet = Bot.getData("UserWallet" + UID) or "Not Linked"


# ==============================
# USER DETAILS TEXT
# ==============================

TXT = f"""<b>👤 Uѕᴇʀ Dᴇᴛᴀɪʟѕ

Usᴇʀ ID: <a href="tg://user?id={UID}">{UID}</a>
Bᴀʟᴀɴᴄᴇ: ₹{balance}
Tᴏᴛᴀʟ Wɪᴛʜᴅʀᴀᴡɴ: ₹{withdraw}
Tᴏᴛᴀʟ Rᴇғᴇʀs: {RefStrtC}
Vᴇʀɪғɪᴇᴅ Rᴇғᴇʀs: {refC}
Bʟᴏᴄᴋᴇᴅ Rᴇғᴇʀs (Sᴀᴍᴇ Dᴇᴠɪᴄᴇ): {RefSameDevC}
Pᴇɴᴅɪɴɢ Rᴇғᴇʀs: {RefStrtC - refC}
Rᴇғᴇʀʀᴀʟs Wɪᴛʜ Wᴀʟʟᴇᴛ Lɪɴᴋ: {RefWalletLnkC}
Rᴇғᴇʀʀᴀʟs Wɪᴛʜ Cʟᴀɪᴍᴇᴅ Bᴏɴᴜs: {RefBonClimC}
Wᴀʟʟᴇᴛ: {wallet}

Rᴇғᴇʀʀᴇᴅ Bʏ: {invited}"""


# ==============================
# BUTTONS
# ==============================

markup = InlineKeyboardMarkup()

markup.add(
    InlineKeyboardButton(
        text="👥 Rᴇғᴇʀʀᴀʟs",
        callback_data="/UserReferrals"
    ))

markup.add(
    InlineKeyboardButton(
        text="🔙 Bᴀᴄᴋ",
        callback_data="/admin"
    )
)


# ==============================
# SEND DETAILS
# ==============================

bot.replyText(
    u,
    TXT,
    reply_markup=markup,
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /UserReferrals
#======================================================================
# ==============================
# /UserReferrals
# ==============================

AllBotAdminss = Bot.getData("AllBotAdminss") or []

if str(u) not in map(str, AllBotAdminss):
    bot.replyText(
        u,
        "<b>🚫 You Are Not This Bot Admin</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# GET UID + PAGE
# ==============================

UID = ""
page = 1

if params and str(params) not in ["None", ""]:
    parts = str(params).strip().split()

    if len(parts) >= 1:
        UID = parts[0]

    if len(parts) >= 2:
        try:
            page = int(parts[1])
        except:
            page = 1

if not UID:
    UID = str(
        Bot.getData("ViewingUser_" + str(u)) or ""
    ).strip()

if UID.startswith("/UserReferrals"):
    UID = UID.replace("/UserReferrals", "", 1).strip()

    parts = UID.split()

    if len(parts) >= 1:
        UID = parts[0]

    if len(parts) >= 2:
        try:
            page = int(parts[1])
        except:
            page = 1


# ==============================
# VALIDATE UID
# ==============================

if not UID.isdigit():
    bot.replyText(
        u,
        "<b>❌ Invalid User ID</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

Bot.saveData("ViewingUser_" + str(u), UID)

if page < 1:
    page = 1


# ==============================
# FIND ALL REFERRED USERS
# ==============================

AllUsers = Bot.getData("FulBotUsrs") or []

InvitedUsers = []

for user_id in AllUsers:

    user_id = str(user_id)

    user_ref = Bot.getData(
        user_id + "Referral"
    ) or "None"

    if str(user_ref) == str(UID):

        if user_id not in InvitedUsers:
            InvitedUsers.append(user_id)


# ==============================
# PAGE SYSTEM
# ==============================

PER_PAGE = 10

TotalUsers = len(InvitedUsers)

TotalPages = (TotalUsers + PER_PAGE - 1) // PER_PAGE

if TotalPages < 1:
    TotalPages = 1

if page > TotalPages:
    page = TotalPages

Start = (page - 1) * PER_PAGE
End = Start + PER_PAGE

PageUsers = InvitedUsers[Start:End]


# ==============================
# DISPLAY
# ==============================

TXT = f"""<b>👥 Uѕᴇʀ Rᴇғᴇʀʀᴀʟѕ

🆔 Rᴇғᴇʀʀᴇʀ ID: <code>{UID}</code>
📊 Tᴏᴛᴀʟ Iɴᴠɪᴛᴇᴅ: {TotalUsers}
📄 Pᴀɢᴇ: {page}/{TotalPages}</b>

"""

if TotalUsers == 0:

    TXT += "<b>🤷‍♂️ Tʜɪs Uѕᴇʀ Hᴀs Nᴏᴛ Iɴᴠɪᴛᴇᴅ Aɴʏᴏɴᴇ.</b>"

else:

    number = Start + 1

for invited_id in PageUsers:

    try:
        chat_info = bot.getChat(invited_id)
        first_name = chat_info.first_name or "Unknown"
    except:
        first_name = "Unknown"

    TXT += (
        f'<b>{number}. '
        f'<a href="tg://user?id={invited_id}">{first_name}</a> '
        f'[<code>{invited_id}</code>]</b>\n'
    )

    number += 1

# ==============================
# BUTTONS
# ==============================

markup = InlineKeyboardMarkup()

nav = []

if page > 1:
    nav.append(
        InlineKeyboardButton(
            text="⬅️ Pʀᴇᴠ",
            callback_data="/UserReferrals " + UID + " " + str(page - 1)
        )
    )

if page < TotalPages:
    nav.append(
        InlineKeyboardButton(
            text="Nᴇxᴛ ➡️",
            callback_data="/UserReferrals " + UID + " " + str(page + 1)
        )
    )

if nav:
    markup.row(*nav)

markup.add(
    InlineKeyboardButton(
        text="🔙 Bᴀᴄᴋ",
        callback_data="/admin"
    )
)


# ==============================
# DISPLAY
# ==============================

try:

    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

except:

    bot.replyText(
        u,
        TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

raise ReturnCommand()


#======================================================================
# COMMAND: /Vsvwalletsele0
#======================================================================
# Command name :+ /Vsvwalletsele0

# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# --- MINIMAL CHANGE START: Multiple Selection Logic ---
# Baaki gateways ko False karne ki jagah, sirf VSV ka status toggle (invert) hoga
current_vsv_status = Bot.getData("vsv")
new_vsv_status = False if current_vsv_status else True
Bot.saveData("vsv", new_vsv_status)

# Current global gateway configuration (Aapki dynamic requirements ke liye)
if new_vsv_status:
    Bot.saveData("gatewaynow", "vsv")
    Bot.saveData("gatewaytype", "https://vsv-gateway-solutions.co.in")

# Sabhi gateways ka latest status database se check karne ke liye helper function
def get_status(key):
    return "✅" if Bot.getData(key) else "❌"

# Sabhi gateways ka live status fetch karna
rj = get_status("rj")
info = get_status("info")
vsv = get_status("vsv")
payzy = get_status("payzy")
fxl = get_status("Fxl")
tg = get_status("Tgwallet")
RDX = get_status("RDX")
X = get_status("X")
E = get_status("e")
sa = get_status("sa")
ultra = get_status("ultra")
unio = get_status("unio")
# --- MINIMAL CHANGE END ---

# Inline Keyboard (Ab yeh static cross/check ki jagah dynamic live status dikhaega)
markup = {
    "inline_keyboard": [
        [
            {"text": "Infotech Wallet", "callback_data": "/none"},
            {"text": info, "callback_data": "/inwalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": vsv, "callback_data": "/Vsvwalletsele0"}
        ],
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": payzy, "callback_data": "/Payzywalletsele"}
        ],
        [
            {"text": "FXL Wallet", "callback_data": "/none"},
            {"text": fxl, "callback_data": "/Fxlwalletsele0"}
        ],
        [
            {"text": "TG Wallet", "callback_data": "/none"},
            {"text": tg, "callback_data": "/Tgwalletsele0"}
        ],
        [
            {"text": "RDX Wallet", "callback_data": "/none"},
            {"text": RDX, "callback_data": "/RDXwalletsele0"}
        ],
        [
            {"text": "X Wallet", "callback_data": "/none"},
            {"text": X, "callback_data": "/Xwalletsele0"}
        ],
        [
            {"text": "RJ Wallet", "callback_data": "/none"},
            {"text": rj, "callback_data": "/rjwalletsele0"}
        ],
        [
            {"text": "E Wallet", "callback_data": "/none"},
            {"text": E, "callback_data": "/ewalletsele0"}
        ],
        [
            {"text": "Saathi Gateway", "callback_data": "/none"},
            {"text": sa, "callback_data": "/sawalletsele0"}
        ],
        [
            {"text": "Ultra Wallet", "callback_data": "/none"},
            {"text": ultra, "callback_data": "/ultrawalletsele0"}
        ],
        [
            {"text": "Unio Wallet", "callback_data": "/none"},
            {"text": unio, "callback_data": "/uniowalletsele0"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
status_text = "Active ✅" if new_vsv_status else "Inactive ❌"
bot.replyText(u, f"<b><i>🔄 Vsv Wallet is {status_text} Now!</i></b>")


#======================================================================
# COMMAND: /Vsvwalletsele1
#======================================================================
# /rjwallet_activate

# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Activate RJ Wallet and deactivate others
Bot.saveData("vsv1", True)
Bot.saveData("payzy1", False)

# Save current gateway details
Bot.saveData("gatewaynow", "vsv1")
Bot.saveData("gatewaytype", "https://vsv-gateway-solutions.co.in")

# UI Symbols
check = "✅"
cross = "❌"

# Inline Keyboard
markup = {
    "inline_keyboard": [
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": cross, "callback_data": "/payzywalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": check, "callback_data": "/Vsvwalletsele0"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
bot.replyText(u, "<b><i>✅ Vsv Wallet  Autopay Upi Active Now!</i></b>")


#======================================================================
# COMMAND: /WalletOFF_Text
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

keyboard = ReplyKeyboardMarkup(True)
keyboard.row("⛔ Cancel")

bot.replyText(
    u,
    """<b>💡 Please Send Your Wallet Withdraw Mode Off Message

⚠️ Send '<code>Clear</code>' To Remove The Withdraw Mode Off Message</b>""",
    parse_mode="HTML",
    reply_markup=keyboard
)

Bot.handleNextCommand("/WalletOFF_Text1")


#======================================================================
# COMMAND: /WalletOFF_Text1
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if message.text == "⛔ Cancel":
    Bot.runCommand("/PIRO_MainMenu", options="<b>⛔ Cancelled Successfully</b>")
    Bot.runCommand("/admin")
    raise ReturnCommand()

if message.text.lower() == "clear":
    Bot.saveData("WalletOffText", "")

    Bot.runCommand(
        "/PIRO_MainMenu",
        options="<b>✅ Wallet OFF Text Cleared Successfully</b>"
    )
    raise ReturnCommand()

Bot.saveData("WalletOffText", message.text)

Bot.runCommand(
    "/PIRO_MainMenu",
    options="<b>✅ Wallet OFF Text Changed Successfully</b>"
)


#======================================================================
# COMMAND: /WithdrawStatus
#======================================================================
# coded by @Jenish_Dobariya1
Wallet = Bot.getData("WalletWithdrawMode") or "ON"
Upi = Bot.getData("UpiWithdrawMode") or "ON"

markup = {
 "inline_keyboard":[
  [{"text":f"💳 Wallet : {Wallet}","callback_data":"/ToggleWallet"}],
  [{"text":f"🏦 UPI : {Upi}","callback_data":"/ToggleUpi"}],
  [{"text":"🔙 Back","callback_data":"/admin"}]
 ]
}

bot.editMessageText(
 chat_id=u,
 message_id=message.message_id,
 text="<b>⚙️ Withdraw Settings</b>",
 reply_markup=markup,
 parse_mode="HTML"
)


#======================================================================
# COMMAND: /WithdrwOFF_Text
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


keyboard=ReplyKeyboardMarkup(True)
keyboard.row("⛔ Cancel")



bot.replyText(u,"<b> Send The Text To Edit</b>""",parse_mode = "html",reply_markup=keyboard)



Bot.handleNextCommand("/WithdrwOFF_Text1")


#======================================================================
# COMMAND: /WithdrwOFF_Text1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

if message.text=="⛔ Cancel":
    Bot.runCommand("/PIRO_MainMenu",options="<b>⛔ Cancelled Succesfully</b>""") 
    Bot.runCommand("/admin")
    raise ReturnCommand()
    
Bot.runCommand("/PIRO_MainMenu",options="<b>Changed Successfully</b>""") 

Bot.saveData("WOT",message.text)


#======================================================================
# COMMAND: /addgetwayonbbot
#======================================================================
# coded by @Jenish_Dobariya1

# ================== ADMIN CHECK ==================

Admins = Bot.getData("AllBotAdminss") or []

if not isinstance(Admins, list):
    Admins = [Admins]

is_Admin = False

for userid in Admins:
    if str(message.chat.id) == str(userid):
        is_Admin = True
        break

if not is_Admin:
    bot.replyText(
        message.chat.id,
        f"<b>🚫 Access Denied\n\n🆔 Your Chat ID : {message.chat.id}</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ================== FETCH DATA ==================

Botpayname = Bot.getData("Botpayname") or "Payment"

SameWallet = Bot.getData("SameWallet") or "ON"
SameUPI = Bot.getData("SameUPI") or "ON"

# Safety check
if SameWallet not in ["ON", "OFF"]:
    SameWallet = "ON"
    Bot.saveData("SameWallet", SameWallet)

if SameUPI not in ["ON", "OFF"]:
    SameUPI = "ON"
    Bot.saveData("SameUPI", SameUPI)


# ================== STATUS ==================

if SameWallet == "ON":
    WalletStatus = "🟢 ON"
    WalletDesc = "Multiple users can use the same wallet"
else:
    WalletStatus = "🔴 OFF"
    WalletDesc = "One wallet can be linked to only one user"


if SameUPI == "ON":
    UPIStatus = "🟢 ON"
    UPIDesc = "Multiple users can use the same UPI"
else:
    UPIStatus = "🔴 OFF"
    UPIDesc = "One UPI can be linked to only one user"


# ================== INLINE KEYBOARD ==================

markup = InlineKeyboardMarkup()


# -------- WALLET --------

markup.add(
    InlineKeyboardButton(
        text='🌐 Select Gateway (Wallet)',
        callback_data='/selegetwayonbbot'
    ),
    InlineKeyboardButton(
        text='🔑 Set Payout Keys',
        callback_data='/SetBotGatewayKey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'✨ Payment Message: {Botpayname}',
        callback_data='/SetBotPayComm0'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same Wallet: {WalletStatus}',
        callback_data='/ToggleSameWallet'
    )
)


# -------- UPI --------

markup.add(
    InlineKeyboardButton(
        text='🌐 Add Gateway (UPI)',
        callback_data='/test'
    ),
    InlineKeyboardButton(
        text='Set UPI Gateway Keys 🔐',
        callback_data='/SetBotUPIkey'
    )
)

markup.add(
    InlineKeyboardButton(
        text=f'♻️ Same UPI: {UPIStatus}',
        callback_data='/ToggleSameUPI'
    )
)


# -------- BACK --------

markup.add(
    InlineKeyboardButton(
        text='🔙 Back To Admin Panel',
        callback_data='/admin'
    )
)


# ================== MESSAGE TEXT ==================

text = f"""
<b>╔══════════════════════╗
        🛠 ADMIN SETTINGS
╚══════════════════════╝</b>

👤 <b>Admin:</b> {message.from_user.first_name}
🆔 <b>Chat ID:</b> {message.chat.id}

━━━━━━━━━━━━━━━━━━━
<b>💳 WALLET SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> Wallet Gateway
♻️ <b>Same Wallet:</b> {WalletStatus}

<i>💡 {WalletDesc}</i>

━━━━━━━━━━━━━━━━━━━
<b>💸 UPI SETTINGS</b>
━━━━━━━━━━━━━━━━━━━

🌐 <b>Gateway:</b> UPI Gateway
♻️ <b>Same UPI:</b> {UPIStatus}

<i>💡 {UPIDesc}</i>

━━━━━━━━━━━━━━━━━━━
⚙️ <b>Manage Gateway & Payment Settings</b>
━━━━━━━━━━━━━━━━━━━
"""


# ================== SAFE EDIT ==================

try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=text,
        parse_mode="HTML",
        reply_markup=markup
    )
except:
    bot.replyText(
        message.chat.id,
        text,
        parse_mode="HTML",
        reply_markup=markup
    )


#======================================================================
# COMMAND: /admin
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if AllBotAdminss == []:
    MAIN_ADMIN = u
    AllBotAdminss.append(MAIN_ADMIN)
    Bot.saveData("AllBotAdminss", AllBotAdminss)

    AllBotAdminss = Bot.getData("AllBotAdminss") or []
    Bot.saveData("Owner", u)

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>"
    )
    raise ReturnCommand()



Owner = Bot.getData("Owner") or None

# Owner always has all permissions
is_Owner = str(u) == str(Owner)

Permissions = Bot.getData("AdminPermissions") or {}


DEFAULT_OFF_PERMISSIONS = [
    "permission",
    "reset_balance",
]


def HasPermission(key):

    # Owner always has everything
    if is_Owner:
        return True

    # If permission was manually saved, use saved value
    if key in Permissions:
        return Permissions[key]

    # New permissions listed here are OFF by default
    if key in DEFAULT_OFF_PERMISSIONS:
        return False

    # All other permissions are ON by default
    return True

now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]
time = now["time"][:5]

year, month, day = date.split("-")
hour, minute = time.split(":")

hour = int(hour)

ampm = "am"

if hour >= 12:
    ampm = "pm"

if hour > 12:
    hour -= 12

if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


# ==============================
# DATA
# ==============================

AdmAC = Bot.getData("AdmAC") or []

perRef = Bot.getData("PerRefer") or 0
daiBon = Bot.getData("DailyBonus") or 0

minWit = Bot.getData("MinWith") or 0
maxWit = Bot.getData("MaxWith") or 0

upi_minWit = Bot.getData("MinWith1") or 0
upi_maxWit = Bot.getData("MaxWith1") or 0

minWit1 = Bot.getData("MinWith1") or 0
maxWit1 = Bot.getData("MaxWith1") or 0
SetMinRef1 = Bot.getData("SetMinRef1") or 0
tax = Bot.getData("Tax") or 0

PayOutChannel = Bot.getData("Botpaychannel") or "🚫 Not Set"

MinRef = Bot.getData("MinRefToWithdrw") or 0
SetMinRef = Bot.getData("SetMinRef") or 0

Owner = Bot.getData("Owner") or None

ownerid = f"tg://openmessage?user_id={Owner}"
owner = f"<a href='{ownerid}'>{Owner}</a>"

GatewayList={
    "vsv":{"name":"Vsv Wallet","status_key":"vsv","tax_key":"vsvtax"},
    "payzy":{"name":"Payzy Wallet","status_key":"payzy","tax_key":"payzytax"},
    "sa":{"name":"Saathi Gateway","status_key":"sa","tax_key":"satax"},
    "ultra":{"name":"Ultra Wallet","status_key":"ultra","tax_key":"ultratax"},
    "txg":{"name":"TXG Wallet","status_key":"txg","tax_key":"txgtax"},
    "rupix":{"name":"Rupix Wallet","status_key":"rupix","tax_key":"rupixtax"}
}

tax_lines=[]

for gid,gw in GatewayList.items():
    status_key=gw.get("status_key")
    tax_key=gw.get("tax_key")

    if Bot.getData(status_key):
        tax=Bot.getData(tax_key) or 0
        name=gw.get("name",gid)
        tax_lines.append(f"🧾 {name} Tax: ₹{tax}")

gateway_tax_text="\n".join(tax_lines) or "🧾 Tax: Not Set"
# ==============================
# BOT MODE
# ==============================

if "BotMode" in str(params):

    P = params.split(" ")

    mode = "ON" if P[1].upper() == "ON" else "OFF"

    Bot.saveData("BotMode", mode)

    act = f"🤖 Bot Mode Turned {mode}"

    AdmAC.append(
        f"<b>📆 Time:</b> {EasyTime}\n"
        f"👥 <b>By {message.from_user.first_name}</b> "
        f"[ID: <code>{u}</code>]\n"
        f"🔍<b> Action: </b> {act}"
    )

    Bot.saveData("AdmAC", AdmAC)


BOT_MODE = Bot.getData("BotMode") or "ON"

botSta = "🟢 On" if BOT_MODE == "ON" else "🔴 Off"

botStatChngeBut = (
    "BotMode OFF"
    if BOT_MODE == "ON"
    else "BotMode ON"
)


# ==============================
# NEW USER NOTIFICATION
# ==============================

NewUserNotification = Bot.getData(
    "NewUserNotification"
) or "ON"


if "NewUserNotification" in str(params):

    P = params.split(" ")

    mode = "ON" if P[1].upper() == "ON" else "OFF"

    Bot.saveData(
        "NewUserNotification",
        mode
    )

    NewUserNotification = mode

    act = f"🔔 New User Notification Turned {mode}"

    AdmAC.append(
        f"<b>📆 Time:</b> {EasyTime}\n"
        f"👥 <b>By {message.from_user.first_name}</b> "
        f"[ID: <code>{u}</code>]\n"
        f"🔍 <b>Action:</b> {act}"
    )

    Bot.saveData("AdmAC", AdmAC)


NewUserNotification = Bot.getData(
    "NewUserNotification"
) or "ON"


NewUserSta = (
    "🟢 On"
    if NewUserNotification == "ON"
    else "🔴 Off"
)


NewUserStatChngeBut = (
    "NewUserNotification OFF"
    if NewUserNotification == "ON"
    else "NewUserNotification ON"
)


# ==============================
# WITHDRAW MODE
# ==============================

if "WithdrawMode" in str(params):

    P = params.split(" ")

    mode = "ON" if P[1].upper() == "ON" else "OFF"

    Bot.saveData("WithdrawMode", mode)

    act = f"💸 Withdraws Turned {mode}"

    AdmAC.append(
        f"<b>📆 Time:</b> {EasyTime}\n"
        f"👥 <b>By {message.from_user.first_name}</b> "
        f"[ID: <code>{u}</code>]\n"
        f"🔍<b> Action: </b> {act}"
    )

    Bot.saveData("AdmAC", AdmAC)


WITHD_MODE = Bot.getData("WithdrawMode") or "ON"

witSta = (
    "🟢 On"
    if WITHD_MODE == "ON"
    else "🔴 Off"
)

witStatChngeBut = (
    "WithdrawMode OFF"
    if WITHD_MODE == "ON"
    else "WithdrawMode ON"
)


# ==============================
# VERIFICATION SYSTEM
# ==============================

current_verif_mode = int(
    Bot.getData("VerifModeSystem") or 0
)


if "ToggleVerifMode" in str(params):

    current_verif_mode = (
        current_verif_mode + 1
    ) % 4

    Bot.saveData(
        "VerifModeSystem",
        current_verif_mode
    )

    contact_status = (
        "ON"
        if current_verif_mode in [1, 3]
        else "OFF"
    )

    captcha_status = (
        "ON"
        if current_verif_mode in [2, 3]
        else "OFF"
    )

    Bot.saveData(
        "VerifySystemStatus",
        contact_status
    )

    Bot.saveData(
        "CaptchaMode",
        captcha_status
    )

    mode_labels = {
        0: "ALL OFF ❌",
        1: "CONTACT ONLY 📱",
        2: "CAPTCHA ONLY 🔐",
        3: "BOTH ON 🛡"
    }

    act = (
        f"⚙ Verification Mode Changed To: "
        f"{mode_labels[current_verif_mode]}"
    )

    AdmAC.append(
        f"<b>📆 Time:</b> {EasyTime}\n"
        f"👥 <b>By {message.from_user.first_name}</b> "
        f"[ID: <code>{u}</code>]\n"
        f"🔍<b> Action: </b> {act}"
    )

    Bot.saveData("AdmAC", AdmAC)


verif_display_text = {
    0: "🔴 All Off",
    1: "📱 Contact On",
    2: "🔐 Captcha On",
    3: "🛡 Both On"
}

verif_status_label = verif_display_text.get(
    current_verif_mode,
    "🔴 All Off"
)


# ==============================
# NEW USER MODE
# ==============================

NewU = Bot.getData("NewU") or "ON"

NewSta = (
    "🟢 On"
    if NewU == "ON"
    else "🔴 Off"
)

NewStatChngeBut = (
    "NewU OFF"
    if NewU == "ON"
    else "NewU ON"
)


# ==============================
# MENU
# ==============================

markup = InlineKeyboardMarkup()


# MANAGE ADMIN PERMISSION
if HasPermission("permission"):
    markup.add(
        InlineKeyboardButton(
            text="🧑‍💼 Mᴀɴᴀɢᴇ Aᴅᴍɪɴ Pᴇʀᴍɪssɪᴏɴ",
            callback_data="/permission"
        )
    )


# TRANSFER + TAX
buttons = []

if HasPermission("transfer_owner"):
    buttons.append(
        InlineKeyboardButton(
            text="👑 Tʀᴀɴsғᴇʀ Oᴡɴᴇʀsʜɪᴘ",
            callback_data="/TransferOwnership"
        )
    )

if HasPermission("tax"):
    buttons.append(
        InlineKeyboardButton(
            text=f"⚖️ Tᴀx",
            callback_data="/SetTaxAmont"
        )
    )

if buttons:
    markup.add(*buttons)


# VERIFICATION
if HasPermission("verification"):
    markup.add(
        InlineKeyboardButton(
            text="🛡 Vᴇʀɪғɪᴄᴀᴛɪᴏɴ: " + verif_status_label,
            callback_data="/admin ToggleVerifMode"
        )
    )


# ADMINS + BAN
buttons = []

if HasPermission("admins"):
    buttons.append(
        InlineKeyboardButton(
            text="👮 Mᴀɴᴀɢᴇ Aᴅᴍɪɴs",
            callback_data="/PIRO_Admins"
        )
    )

if HasPermission("ban_unban"):
    buttons.append(
        InlineKeyboardButton(
            text="⛔ Mᴀɴᴀɢᴇ Bᴀɴ Usᴇʀs",
            callback_data="/BanUnban"
        )
    )

if buttons:
    markup.add(*buttons)


# PAYOUT CHANNEL
if HasPermission("payout_channel"):
    markup.add(
        InlineKeyboardButton(
            text="💳 Sᴇᴛ Pᴀʏᴏᴜᴛ Cʜᴀɴɴᴇʟ",
            callback_data="/SetBotPayChann"
        )
    )


# WITHDRAW + BOT STATUS
buttons = []

if HasPermission("withdraw"):
    buttons.append(
        InlineKeyboardButton(
            text="💸 Wɪᴛʜᴅʀᴀᴡ Sᴛᴀᴛᴜs",
            callback_data="/WithdrawStatus"
        )
    )

if HasPermission("bot_status"):
    buttons.append(
        InlineKeyboardButton(
            text="🤖 Bᴏᴛ Sᴛᴀᴛᴜs: " + botSta,
            callback_data="/admin " + botStatChngeBut
        )
    )

if buttons:
    markup.add(*buttons)


# ADD BALANCE
if HasPermission("balance"):
    markup.add(
        InlineKeyboardButton(
            text="➕ Aᴅᴅ Bᴀʟᴀɴᴄᴇ",
            callback_data="/ChangeAnyUserBal"
        )
    )


# VERIFY USER + MANAGE TEXT
buttons = []

if HasPermission("verify_user"):
    buttons.append(
        InlineKeyboardButton(
            text="🙇🏻‍♂️ Vᴇʀɪғʏ Usᴇʀ",
            callback_data="/manualVerifKro"
        )
    )

if HasPermission("manage_text"):
    buttons.append(
        InlineKeyboardButton(
            text="🚀 Mᴀɴᴀɢᴇ Tᴇxᴛ",
            callback_data="/ManageText"
        )
    )

if buttons:
    markup.add(*buttons)


# CHANNELS
if HasPermission("channels"):
    markup.add(
        InlineKeyboardButton(
            text="⚡ Mᴀɴᴀɢᴇ Cʜᴀɴɴᴇʟs",
            callback_data="/PIRO_Chanel_Pannel"
        )
    )


# RESET + BROADCAST
buttons = []

if HasPermission("reset_balance"):
    buttons.append(
        InlineKeyboardButton(
            text="⚠️ Rᴇsᴇᴛ Bᴀʟᴀɴᴄᴇ",
            callback_data="/ResetAllBalance"
        )
    )

if HasPermission("broadcast"):
    buttons.append(
        InlineKeyboardButton(
            text="🎙️ Bʀᴏᴀᴅᴄᴀsᴛ",
            callback_data="/BROADCAST"
        )
    )

if buttons:
    markup.add(*buttons)


# WITHDRAWAL LIMITS
if HasPermission("withdraw_limits"):
    markup.add(
    InlineKeyboardButton(
        text=f"📉 Wᴀʟʟᴇᴛ: ₹{minWit}-{maxWit}-{SetMinRef} | Uᴘɪ: ₹{minWit1}-{maxWit1}-{SetMinRef1}",
        callback_data="/SetMinWithAmont"
    )
)


# REFER + BONUS
buttons = []

if HasPermission("refer"):
    buttons.append(
        InlineKeyboardButton(
            text=f"👥 Pᴇʀ Rᴇғᴇʀ ~ ₹{perRef}",
            callback_data="/SetPerReferAmont"
        )
    )

if HasPermission("bonus"):
    buttons.append(
        InlineKeyboardButton(
            text=f"🎁 Bᴏɴᴜs ~ ₹{daiBon}",
            callback_data="/SetBonusAmont"
        )
    )

if buttons:
    markup.add(*buttons)


# STATISTICS
if HasPermission("statistics"):
    markup.add(
        InlineKeyboardButton(
            text="📊 Sᴛᴀᴛɪsᴛɪᴄs",
            callback_data="/AdminStats"
        )
    )


# TALK + USER DETAILS
buttons = []

if HasPermission("talk_user"):
    buttons.append(
        InlineKeyboardButton(
            text="💬 Tᴀʟᴋ Wɪᴛʜ Usᴇʀ",
            callback_data="/TalkUser"
        )
    )

if HasPermission("user_details"):
    buttons.append(
        InlineKeyboardButton(
            text="ℹ️ Usᴇʀ Dᴇᴛᴀɪʟs",
            callback_data="/UserKiSabDetails"
        )
    )

if buttons:
    markup.add(*buttons)


# ADMIN ACTIONS
if HasPermission("admin_actions"):
    markup.add(
        InlineKeyboardButton(
            text="📝 Rᴇᴄᴇɴᴛ Aᴅᴍɪɴ Aᴄᴛɪᴏɴs",
            callback_data="/PIRO_AdminAction"
        )
    )


# LEADERBOARD + CLICK HERE
buttons = []

if HasPermission("leaderboard"):
    buttons.append(
        InlineKeyboardButton(
            text="🥇 Lᴇᴀᴅᴇʀʙᴏᴀʀᴅ",
            callback_data="/PIRO_LeadSet"
        )
    )

if HasPermission("click_here"):
    buttons.append(
        InlineKeyboardButton(
            text="🤖 Cʟɪᴄᴋ Hᴇʀᴇ",
            callback_data="/onogf"
        )
    )

if buttons:
    markup.add(*buttons)


# NEW USER NOTIFICATION
if HasPermission("new_user_notification"):
    markup.add(
        InlineKeyboardButton(
            text="🔔 Nᴇᴡ Usᴇʀ Nᴏᴛɪғɪᴄᴀᴛɪᴏɴ: " + NewUserSta,
            callback_data="/admin " + NewUserStatChngeBut
        )
    )


# GIFT + WITHDRAW OFF TEXT
buttons = []

if HasPermission("gift_codes"):
    buttons.append(
        InlineKeyboardButton(
            text="🎟 Gɪғᴛ Cᴏᴅᴇs",
            callback_data="/PIRO_RC_Pannel"
        )
    )

if HasPermission("withdraw_off_text"):
    buttons.append(
        InlineKeyboardButton(
            text="📴 Wɪᴛʜᴅʀᴀᴡ Oғғ Tᴇxᴛ",
            callback_data="/textoff"
        )
    )

if buttons:
    markup.add(*buttons)


# GATEWAY
if HasPermission("gateway"):
    markup.add(
        InlineKeyboardButton(
            text="🌐 Gᴀᴛᴇᴡᴀʏ Sᴇᴛᴜᴘ",
            callback_data="/addgetwayonbbot"
        )
    )

if HasPermission("gateway"):
    markup.add(
        InlineKeyboardButton(
            text="💰 Bᴏᴛ Fᴜɴᴅ",
            callback_data="/Live_Fund_Panel"
        )
    )
    

# ==============================
# ADMIN TEXT
# ==============================

TXT = f"""<b>👋🏻 Hᴇʟʟᴏ </b> <code>{message.from_user.first_name}</code>

<b>👑 Mᴀɪɴ Oᴡɴᴇʀ: {owner}

   🤖 Bᴏᴛ Sᴛᴀᴛᴜs: {botSta}
   💸 Wɪᴛʜᴅʀᴀᴡᴀʟ Sᴛᴀᴛᴜs: {witSta}
   🛡️ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ Mᴏᴅᴇ: {verif_status_label}
   📢 Pᴀʏᴏᴜᴛ Cʜᴀɴɴᴇʟ: {PayOutChannel}
   🎫 Mɪɴɪᴍᴜᴍ Wɪᴛʜᴅʀᴀᴡᴀʟ(Wᴀʟʟᴇᴛ): ₹{minWit}
   🎟️ Mᴀxɪᴍᴜᴍ Wɪᴛʜᴅʀᴀᴡᴀʟ(Wᴀʟʟᴇᴛ): ₹{maxWit}
   🎫 Mɪɴɪᴍᴜᴍ Wɪᴛʜᴅʀᴀᴡᴀʟ(UPI): ₹{minWit1}
   🎟️ Mᴀxɪᴍᴜᴍ Wɪᴛʜᴅʀᴀᴡᴀʟ(UPI): ₹{maxWit1}
   👥 Pᴇʀ Rᴇғᴇʀ: ₹{perRef}
   🎯 Mɪɴ. Rᴇғᴇʀ Fᴏʀ Wɪᴛʜᴅʀᴀᴡ: {SetMinRef}
   🎁 Dᴀɪʟʏ Bᴏɴᴜs: ₹{daiBon}
   {gateway_tax_text}</b>

<i>🧭 Sᴇʟᴇᴄᴛ A Sᴇᴛᴛɪɴɢ Bᴇʟᴏᴡ Tᴏ Mᴀɴᴀɢᴇ Yᴏᴜʀ Bᴏᴛ.</i>"""


# ==============================
# COMMAND HANDLING
# ==============================

if str(message.text) == "/admin":

    bot.replyText(
        u,
        TXT,
        reply_markup=markup,
        parse_mode="HTML"
    )

    raise ReturnCommand()


if (
    params
    or params != None
    or options == "AP"
    or params == "AP"
):

    try:

        bot.editMessageText(
            chat_id=u,
            message_id=message.message_id,
            text=TXT,
            reply_markup=markup,
            parse_mode="HTML"
        )

    except:
        pass

    raise ReturnCommand()


bot.replyText(
    u,
    TXT,
    reply_markup=markup,
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /botfund
#======================================================================
EMOJI_GIFT = "5193085063998224234"
EMOJI_LIVE = "4990298741463319592"

live_fund = float(Bot.getData("LiveFund") or 0)
total_fund = float(Bot.getData("TotalFund") or live_fund)

bot.sendMessage(
    chat_id=u,
    text=f"""<b><tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji> Total Fund Of The Bot >> ₹1,000

<tg-emoji emoji-id="{EMOJI_LIVE}">✅</tg-emoji>Remaining Fund >> ₹{live_fund:.2f}</b>""",
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /broadcast
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

EMOJI_A = "6224161941305169199"  # 🎉
EMOJI_D = "6082398290773546707"  # ✅
EMOJI_G = "5039613856603702817"  # 👤

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_G}">🚫</tg-emoji><b> You Are Not This Bot Admin</b>')
    raise ReturnCommand()

bot.sendMessage(
    f'<tg-emoji emoji-id="{EMOJI_A}">📣</tg-emoji><b> New Broadcast</b>\n'
    "━━━━━━━━━━━━━━━\n\n"
    "<b>Step 1 — Send your message</b>\n"
    "Type it like a normal chat. Bold, italic, links, spoilers — all work, no HTML needed.\n\n"
    f'<tg-emoji emoji-id="{EMOJI_D}">✅</tg-emoji><b> Accepted:</b> Text, Photo, Video, Audio, Document, Sticker, GIF, Voice, Contact\n\n'
    "<b>Step 2 — Pick how it's sent</b>\n"
    "🚀 Direct — clean, no tag\n"
    "🔁 Forward — shows 'Forwarded from'\n\n"
    "━━━━━━━━━━━━━━━\n"
    "👇 Send your message below",
    parse_mode="html"
)

Bot.handleNextCommand("/PIRO_broadcast1")


#======================================================================
# COMMAND: /claimvoucher
#======================================================================
# /claimvoucher

if not libs.tbcads.claim():
    raise ReturnCommand

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
voucher = ""

for i in range(32):
    voucher += chars[libs.Random.randomInt(0, 35)]

bot.sendMessage(
    "🎉 <b>Voucher Unlocked!</b>\n\n"
    "🎟️ <code>" + voucher + "</code>\n\n"
    "✅ Ad verified successfully!"
)


#======================================================================
# COMMAND: /cooltimw
#======================================================================
Bot.sendMessage("⏳ <b>Please enter the cooldown time (in minutes)</b>\n\n🕐 Example: <code>30</code>", "html")
Bot.handleNextCommand("/setcool")


#======================================================================
# COMMAND: /creating_NwRC
#======================================================================
# 19'4'25   00'11'10  v:2'0'0 [√]
# CODED BY: @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


bot.replyText(
    u,
    """<b>💸 Sᴇɴᴅ Dᴇᴛᴀɪʟs Iɴ Tʜɪs Fᴏʀᴍᴀᴛ:
    
<code>Pᴇʀ Uѕᴇʀ Aᴍᴏᴜɴᴛ-Mᴀx Uѕᴇʀѕ--Mɪɴ Rᴇғᴇʀ</code>

💡 E.xᴀᴍᴘʟᴇ:
<code>1-30--5</code></b>""",
    parse_mode="HTML"
)

Bot.handleNextCommand("/CreateBotRC")


#======================================================================
# COMMAND: /creating_NwRC1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Jenish_Dobariya1 

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

gift_name = options # पिछली स्टेप से कोड का नाम यहाँ आया
max_users = message.text.strip()

bot.replyText(u, f"<b>Okay! {max_users} Users Can Claim The Code: <code>{gift_name}</code></b>\n\n💸 Send the amount each user will receive upon redeeming.", parse_mode="html")

# ये अगली कमांड (/CreateBotRC) को दोनों डेटा ट्रांसफर करेगा
Bot.handleNextCommand("/CreateBotRC", options=f"{gift_name}_{max_users}")


#======================================================================
# COMMAND: /creating_NwRC_Step2
#======================================================================
# CODED BY: @Jenish_Dobariya1 

AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

gift_name = message.text.strip().upper() # नाम को UPPERCASE में सेव करेगा ताकि यूज़र आसानी से टाइप कर सकें

bot.replyText(u, f"<b>Code Name Set To: <code>{gift_name}</code></b>\n\n🔢 Enter the Maximum Number Of Users That Can Redeem This Code.", parse_mode="html")
Bot.handleNextCommand("/creating_NwRC1", options=gift_name)


#======================================================================
# COMMAND: /delete
#======================================================================
EMOJI_FAILED = "6188201202337977430"

try:
    bot.deleteMessage(u,message.message_id)
except:
    pass
bot.sendMessage(f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Payout Request Canceled<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> </b>')


#======================================================================
# COMMAND: /handler_special_updates
#======================================================================
if update_type == "my_chat_member":
    chat = message.chat
    new_status = message.new_chat_member.status
    
    #proceed if bot gt add in channel
    if chat.type == "channel" and new_status == "administrator":
        chat_id = chat.id
        chat_username = chat.username
        L="link..."
        
        AllBotAdminss = Bot.getData("AllBotAdminss") or []
 
        lnkFound=True
        try:
            L=bot.exportChatInviteLink(message.chat.id)
        except:
            lnkFound=False
         
        if lnkFound==False or str(L)=="None": 
            for A in AllBotAdminss:
                try:
                    bot.replyText(A,f"<b>🚫 Can't Add Invite Link To  {message.chat.id} Because Admin Detected, But No Permission To Invite Users. 😊</b>",parse_mode="HTML",disable_web_page_preview=True)
                except:
                    pass
            raise ReturnCommand()
              
        AMC = Bot.getData("AllMainCh") or []
        AMCL=Bot.getData("AllMainChlink") or []
        AMCU=Bot.getData("AllMainChUsernm") or []

        AMCTGID=Bot.getData("AllMainChTGID") or []
        
        try:
            try:
                IND=AMCTGID.index(int(message.chat.id))
            except:
                IND=AMCTGID.index(str(message.chat.id))
            AMCL[IND]=L
            Bot.saveData("AllMainChlink",AMCL) 
        except:
            raise ReturnCommand()
        
        
       
        for A in AllBotAdminss:
            try:
                bot.replyText(A,f"<b>🎉 Bot Is Admin In {AMCU[IND]} 🎉\n\n🔗 Invite Link Successfully Added Automatically! 😊</b>",parse_mode="HTML",disable_web_page_preview=True)
        
                bot.replyText(A,f"<b>🔗 Invite Link {L} Added To {AMCU[IND]} Because Admin With Invite Users Permissions Was Detected. 😊</b>",parse_mode="HTML",disable_web_page_preview=True)

            except:
                pass




if update_type == "chat_join_request":
    user_id = message.from_user.id
    
    Bot.saveData(str(message.chat.id)+"JoinRRof"+str(user_id),"Y")
    


#======================================================================
# COMMAND: /info
#======================================================================
EMOJI_JENISH = "6264839164248727584"

# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here
# [ DM TO BUY ANY BOTS & CODES ]

text = '<a href="http://t.me/Jenil_AutoMakerbot">AutoPay Maker [Jenil]</a>'

bot.replyText(
    u,
    f'<b>Developed By {text} <tg-emoji emoji-id="{EMOJI_JENISH}">🔍</tg-emoji></b>',
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /livefund
#======================================================================
channel = Bot.getData("LiveFundChannel") or "@YourChannel"

fund = Bot.getData("LiveFund") or 0
fund = Bot.getData("LiveFund") or 0
bot_name = Bot.info().username

bot.sendMessage(
f"""<b>✅ Total Remaining Fund In @{bot_name} >> ₹{fund:.2f}

🚀 This Is A High Fund And Long
Term Running Bot With Huge Funds

💰💰 Loot As Much As You Can 😎🙏

😍 Specially Powered By
{channel} !!

</b>""",
        parse_mode="html",
        reply_markup={
    "inline_keyboard": [
        [
            {
                "text": f"💰 Fund ₹{fund:.2f}",
                "url": f"https://t.me/{bot_name}"
            }
        ]
    ]
})


#======================================================================
# COMMAND: /manualVerifKro
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


bot.replyText(u,"<b>💡 Send User Telegram Id To Approve</b>""",parse_mode = "html")

Bot.handleNextCommand("/manualVerifKro1")


#======================================================================
# COMMAND: /manualVerifKro1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()


now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 
year, month, day = date.split("-")
hour, minute = time.split(":")
hour = int(hour)
ampm = "am"
if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr","05": "May", "06": "Jun", "07": "Jul", "08": "Aug","09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


AdmAC=Bot.getData("AdmAC") or []



USE=message.text
try:
    bot.replyText(USE,f"""<b>You Are Verified By Admin

Now You Can Use The Bot

Press /start</b>""",parse_mode = "html")

    bot.replyText(USE,f"""<b>User Can Use Bot Now</b>""",parse_mode = "html")
    Bot.saveData(str(USE) +"ManualAproval","Y")
except:
    bot.replyText(u,f"""<b>Invalid Value</b>""",parse_mode = "html")


act=f"Verified to {message.text}"
AdmAC.append(f"<b>📆 Time:</b> {EasyTime}\n👥 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n🔍<b> Action: </b> {act}")

Bot.saveData("AdmAC",AdmAC)

 
 


#======================================================================
# COMMAND: /onWebhook
#======================================================================
EMOJI_WARN = "5447644880824181073"
EMOJI_GIFT = "5203996991054432397"
EMOJI_SUCCESS = "6203820727083208720"
EMOJI_FAILED = "6129840374971112593"
EMOJI_CELE = "6129758753412619088"
EMOJI_PARTY = "6224161941305169199"
# ================= VALIDATION =================
if options is None:
    raise ReturnCommand()

if options.json is None:
    raise ReturnCommand()


# ================= RESPONSE =================
res = options.json

# ================= FINGERPRINT =================
fp = str(
    res.get("fingerprint", "")
).strip()

botusername = str(
    res.get("botusername", "")
).strip()

fp = str(
    res.get("fingerprint", "")
).strip()

if fp == "":

    bot.sendMessage(
        f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji>Fingerprint Missing'
)

    raise ReturnCommand()


# ================= SAME DEVICE CHECK =================

used_device = Bot.getData(
    "FP_" + fp
)

if used_device is not None:

    Bot.saveData(
        str(u) + "sameDev",
        "yes"
    )

    User.saveData(
        "verify",
        "ok"
    )

    User.saveData(
        "PhVerification",
        "Verified"
    )

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""
<b><tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji>Same Device Detected

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji>Referral Bonus Not Available.

<tg-emoji emoji-id="{EMOJI_CELE}">🥳</tg-emoji>But You Can Still Use The Bot.</b>
"""
    )

    raise ReturnCommand()


# ================= SAVE NEW DEVICE =================

Bot.saveData(
    "FP_" + fp,
    str(u)
)

botusername = str(
    res.get("botusername", "")
).strip()

User.saveData(
    "fingerprint",
    fp
)

User.saveData(
    "botusername",
    botusername
)

Bot.saveData(
    "FP_" + fp,
    str(u)
)

status = str(
    res.get("status", "")
).lower().strip()

message_txt = str(
    res.get("message", "")
).strip()


# ================= VERIFIED =================
if (
    status == "pass"
    and message_txt == "Verified Successfully"
):

    User.saveData(
        "verify",
        "ok"
    )

    User.saveData(
        "PhVerification",
        "Verified"
    )

    bot.sendMessage(
        f"""
<tg-emoji emoji-id="{EMOJI_PARTY}">🎉</tg-emoji><b>Verification Successful!

<tg-emoji emoji-id="{EMOJI_SUCCESS}">✅</tg-emoji>Welcome To Wallet Bot.</b>
""",
        parse_mode="HTML"
    )

    Bot.runCommand(
        "/PIRO_MainMenu"
    )

    raise ReturnCommand()


# ================= ALREADY VERIFIED =================
elif (
    status == "pass"
    and message_txt == "Already Verified"
):

    User.saveData(
        "verify",
        "ok"
    )

    User.saveData(
        "PhVerification",
        "Verified"
    )

    Bot.runCommand(
        "/PIRO_MainMenu"
    )

    raise ReturnCommand()


# ================= VPN DETECTED =================
elif (
    status == "fail"
    and "VPN" in message_txt
):

    bot.sendMessage(
        f"""
<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>VPN Detected

<tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji>Disable VPN
And Try Again.</b>
""",
        parse_mode="HTML"
    )

    raise ReturnCommand()


# ================= SAME DEVICE =================
elif (
    status == "fail"
    and "Device already used" in message_txt
):

    Bot.saveData(
        str(u) + "sameDev",
        "yes"
    )

    User.saveData(
        "verify",
        "ok"
    )

    User.saveData(
        "PhVerification",
        "Verified"
    )

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f"""
<b><tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji>Same Device Detected

<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji>Referral Bonus Not Available.

<tg-emoji emoji-id="{EMOJI_CELE}">🥳</tg-emoji>But You Can Still Use The Bot.</b>
"""
    )

    raise ReturnCommand()


# ================= FAILED =================
else:

    User.saveData(
        "verify",
        "pending"
    )

    bot.sendMessage(
        f"""
<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Verification Failed

🔄 Please Try Again.</b>
""",
        parse_mode="HTML"
    )

    Bot.runCommand(
        "/PIRO_Verification"
    )

    raise ReturnCommand()


#======================================================================
# COMMAND: /onogf
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not Authorized! 👮‍♂️</i></b>")
    raise ReturnCommand()

Bot.sendMessage("✨📌 Send <b>Click Here</b> link for menu text 🔗📲")
Bot.handleNextCommand("//onogf")


#======================================================================
# COMMAND: /payzy_token
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()




bot.replyText(
    u,
    "<b>💸 UPI Gateway Setup Payzy Wallet\n\n"
    "✨ Send the <u>Token(Payzy) & Tax in percentage</u>:\n\n"
    "🔢 Example : <code>Token--15</code>\n"
    "⚡ Choose wisely & send now!</b>",
    parse_mode="html"
)


Bot.handleNextCommand("/payzy_upi")


#======================================================================
# COMMAND: /payzy_upi
#======================================================================
# coded by @Jenish_Dobariya1

# ----------- ADMIN CHECK -----------
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# ----------- TIME FORMAT -----------
now = libs.DateAndTime.now("Asia/Kolkata")
date = now["date"]  
time = now["time"][:5] 

year, month, day = date.split("-")
hour, minute = time.split(":")

hour = int(hour)
ampm = "am"

if hour >= 12:
    ampm = "pm"
if hour > 12:
    hour -= 12
if hour == 0:
    hour = 12

MONTHS = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

EasyTime = f"{int(day)} {MONTHS[month]}, {hour:02}:{minute} {ampm}"


# ----------- INPUT VALIDATION -----------
text = message.text.strip()

token2 = None
tax2 = 0

# Case 1: Token-Tax (जैसे: TVJZCUHK-15)
if "--" in text:
    parts = text.split("--")

    if len(parts) != 2 or not parts[0] or not parts[1].isdigit():
        bot.replyText(u, "❌ Invalid format. Use: <b>Your Token-15</b>", parse_mode="html")
        raise ReturnCommand()

    token2 = parts[0]
    tax2 = int(parts[1])

# Case 2: Only Token (बिना टैक्स के, टैक्स = 0)
else:
    token2 = text
    tax2 = 0



# ----------- SAVE DATA -----------
Bot.saveData("Token2", token2)
Bot.saveData("Tax2", tax2)

# आपके पूरे विड्रॉल सिस्टम के साथ तालमेल बिठाने के लिए ग्लोबल वेरिएबल्स भी अपडेट किए
Bot.saveData("BotGatewayKeyp", token2)
Bot.saveData("Tax", float(tax2))

act = f"Token = {token2}, Tax = {tax2}%"


# ----------- RESPONSE -----------
bot.replyText(
    u,
    f"<b>✅ Saved Successfully</b>\n\n🔑 Token: <code>{token2}</code>\n💸 Tax: {tax2}%",
    parse_mode="html"
)


# ----------- SAVE ADMIN ACTION LOG -----------
AdmAC = Bot.getData("AdmAC") or []

AdmAC.append(
    f"<b>📆 Time:</b> {EasyTime}\n"
    f"👤 <b>By {message.from_user.first_name}</b> [ID: <code>{u}</code>]\n"
    f"⚙️ <b>Action:</b> {act}"
)

Bot.saveData("AdmAC", AdmAC)


# ----------- BACK TO ADMIN PANEL -----------
Bot.runCommand("/admin")


#======================================================================
# COMMAND: /payzywalletsele0
#======================================================================
# /rjwallet_activate

# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# Activate RJ Wallet and deactivate others
Bot.saveData("vsv1", False)
Bot.saveData("payzy1", True)

# Save current gateway details
Bot.saveData("gatewaynow", "payzy1")
Bot.saveData("gatewaytype", "https://payzy-gateway.site")

# UI Symbols
check = "✅"
cross = "❌"

# Inline Keyboard
markup = {
    "inline_keyboard": [
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": check, "callback_data": "/payzywalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": cross, "callback_data": "/Vsvwalletsele1"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
bot.replyText(u, "<b><i>✅ Payzy Wallet  Autopay Upi Is Active Now!</i></b>")


#======================================================================
# COMMAND: /permission
#======================================================================
# ==============================
# ADMIN PERMISSION PANEL
# ==============================

Owner = Bot.getData("Owner") or None

if str(u) != str(Owner):
    bot.replyText(
        u,
        "<b>🚫 Only Bot Owner Can Manage Permissions</b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ==============================
# PERMISSIONS
# ==============================

Permissions = Bot.getData("AdminPermissions") or {}


# ==============================
# TOGGLE PERMISSION
# ==============================

if str(params) != "None" and str(params) != "":
    permission = str(params)

    current = Permissions.get(permission, True)
    Permissions[permission] = not current

    Bot.saveData("AdminPermissions", Permissions)


# Reload
Permissions = Bot.getData("AdminPermissions") or {}


# ==============================
# STATUS
# ==============================

DEFAULT_OFF_PERMISSIONS = [
    "permission",
    "reset_balance",
]

def P(key):
    if key in Permissions:
        return "✅" if Permissions[key] else "❌"

    if key in DEFAULT_OFF_PERMISSIONS:
        return "❌"

    return "✅"

# ==============================
# MENU
# ==============================

markup = InlineKeyboardMarkup()


markup.add(
    InlineKeyboardButton(
        text="🧑‍💼 Mᴀɴᴀɢᴇ Aᴅᴍɪɴ Pᴇʀᴍɪssɪᴏɴ " + P("permission"),
        callback_data="/permission permission"
    )
)


markup.add(
    InlineKeyboardButton(
        text="👑 Tʀᴀɴsғᴇʀ Oᴡɴᴇʀsʜɪᴘ " + P("transfer_owner"),
        callback_data="/permission transfer_owner"
    ),
    InlineKeyboardButton(
        text="⚖️ Tᴀx ~ " + str(Bot.getData("Tax") or 0) + "% " + P("tax"),
        callback_data="/permission tax"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🛡 Vᴇʀɪғɪᴄᴀᴛɪᴏɴ " + P("verification"),
        callback_data="/permission verification"
    )
)


markup.add(
    InlineKeyboardButton(
        text="👮 Mᴀɴᴀɢᴇ Aᴅᴍɪɴs " + P("admins"),
        callback_data="/permission admins"
    ),
    InlineKeyboardButton(
        text="⛔ Mᴀɴᴀɢᴇ Bᴀɴ Usᴇʀs " + P("ban_unban"),
        callback_data="/permission ban_unban"
    )
)


markup.add(
    InlineKeyboardButton(
        text="💳 Sᴇᴛ Pᴀʏᴏᴜᴛ Cʜᴀɴɴᴇʟ " + P("payout_channel"),
        callback_data="/permission payout_channel"
    )
)


markup.add(
    InlineKeyboardButton(
        text="💸 Wɪᴛʜᴅʀᴀᴡ: " + P("withdraw"),
        callback_data="/permission withdraw"
    ),
    InlineKeyboardButton(
        text="🤖 Bᴏᴛ Sᴛᴀᴛᴜs: " + P("bot_status"),
        callback_data="/permission bot_status"
    )
)


markup.add(
    InlineKeyboardButton(
        text="➕ Aᴅᴅ Bᴀʟᴀɴᴄᴇ " + P("balance"),
        callback_data="/permission balance"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🙇🏻‍♂️ Vᴇʀɪғʏ Usᴇʀ " + P("verify_user"),
        callback_data="/permission verify_user"
    ),
    InlineKeyboardButton(
        text="🚀 Mᴀɴᴀɢᴇ Tᴇxᴛ " + P("manage_text"),
        callback_data="/permission manage_text"
    )
)


markup.add(
    InlineKeyboardButton(
        text="⚡ Mᴀɴᴀɢᴇ Cʜᴀɴɴᴇʟs " + P("channels"),
        callback_data="/permission channels"
    )
)


markup.add(
    InlineKeyboardButton(
        text="⚠️ Rᴇsᴇᴛ Bᴀʟᴀɴᴄᴇ " + P("reset_balance"),
        callback_data="/permission reset_balance"
    ),
    InlineKeyboardButton(
        text="🎙️ Bʀᴏᴀᴅᴄᴀsᴛ " + P("broadcast"),
        callback_data="/permission broadcast"
    )
)


markup.add(
    InlineKeyboardButton(
        text="📉 Wɪᴛʜᴅʀᴀᴡᴀʟ Lɪᴍɪᴛs " + P("withdraw_limits"),
        callback_data="/permission withdraw_limits"
    )
)


markup.add(
    InlineKeyboardButton(
        text="👥 Pᴇʀ Rᴇғᴇʀ ~ " + P("refer"),
        callback_data="/permission refer"
    ),
    InlineKeyboardButton(
        text="🎁 Bᴏɴᴜs ~ " + P("bonus"),
        callback_data="/permission bonus"
    )
)


markup.add(
    InlineKeyboardButton(
        text="📊 Sᴛᴀᴛɪsᴛɪᴄs " + P("statistics"),
        callback_data="/permission statistics"
    )
)


markup.add(
    InlineKeyboardButton(
        text="💬 Tᴀʟᴋ Wɪᴛʜ Usᴇʀ " + P("talk_user"),
        callback_data="/permission talk_user"
    ),
    InlineKeyboardButton(
        text="ℹ️ Usᴇʀ Dᴇᴛᴀɪʟs " + P("user_details"),
        callback_data="/permission user_details"
    )
)


markup.add(
    InlineKeyboardButton(
        text="📝 Rᴇᴄᴇɴᴛ Aᴅᴍɪɴ Aᴄᴛɪᴏɴs " + P("admin_actions"),
        callback_data="/permission admin_actions"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🥇 Lᴇᴀᴅᴇʀʙᴏᴀʀᴅ " + P("leaderboard"),
        callback_data="/permission leaderboard"
    ),
    InlineKeyboardButton(
        text="🤖 Cʟɪᴄᴋ Hᴇʀᴇ " + P("click_here"),
        callback_data="/permission click_here"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🔔 Nᴇᴡ Usᴇʀ Nᴏᴛɪғɪᴄᴀᴛɪᴏɴ " + P("new_user_notification"),
        callback_data="/permission new_user_notification"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🎟 Gɪғᴛ Cᴏᴅᴇs " + P("gift_codes"),
        callback_data="/permission gift_codes"
    ),
    InlineKeyboardButton(
        text="📴 Wɪᴛʜᴅʀᴀᴡ Oғғ Tᴇxᴛ " + P("withdraw_off_text"),
        callback_data="/permission withdraw_off_text"
    )
)


markup.add(
    InlineKeyboardButton(
        text="🌐 Gᴀᴛᴇᴡᴀʏ Sᴇᴛᴜᴘ " + P("gateway"),
        callback_data="/permission gateway"
    )
)
markup.add(
    InlineKeyboardButton(
        text="💰 Bᴏᴛ Fᴜɴᴅ " + P("botfund"),
        callback_data="/permission botfund"
    )
)

markup.add(
    InlineKeyboardButton(
        text="🔙 Bᴀᴄᴋ",
        callback_data="/admin AP"
    )
)


# ==============================
# TEXT
# ==============================

T = """<b>🧑‍💼 Aᴅᴍɪɴ Pᴇʀᴍɪssɪᴏɴ</b>

<i>Manage permissions for all bot admins.</i>

<b>✅</b> Permission Given
<b>❌</b> Permission Disabled

<i>Tap any button to change its permission.</i>"""


# ==============================
# FULL EDIT MESSAGE
# ==============================

try:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=T,
        reply_markup=markup,
        parse_mode="HTML"
    )
except:
    bot.replyText(
        u,
        T,
        reply_markup=markup,
        parse_mode="HTML"
    )


#======================================================================
# COMMAND: /savesocial
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not Authorized!</b>")
    raise ReturnCommand()

txt = message.text.strip()

# Expecting format: Name - Link
if "-" not in txt:
    bot.sendMessage("❌ Invalid format!\n\nUse: <b>Name - https://link</b>")
    raise ReturnCommand()

parts = txt.split("-", 1)
name = parts[0].strip()
link = parts[1].strip()

if not link.startswith("http"):
    bot.sendMessage("❌ Invalid link format! Must start with http/https")
    raise ReturnCommand()

# Load existing links
SocialLinks = Bot.getData("AllSocialLinks") or []

# Add new one
SocialLinks.append({"name": name, "url": link})

# Save back
Bot.saveData("AllSocialLinks", SocialLinks)

bot.sendMessage(f"✅ Added Social Link:\n\n<b>{name}</b> → {link}")


#======================================================================
# COMMAND: /sawalletsele0
#======================================================================
# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# --- MULTIPLE SELECTION LOGIC START ---
# Baaki gateways ko bina chhede, sirf "sa" ka status toggle (ON/OFF) hoga
current_sa_status = Bot.getData("sa")
new_sa_status = False if current_sa_status else True
Bot.saveData("sa", new_sa_status)

# Agar Saathi Gateway active hua hai, toh uski details save karein
if new_sa_status:
    Bot.saveData("gatewaynow", "sa")
    Bot.saveData("gatewaytype", "http://saathigateway.com/")

# Sabhi gateways ka live status database se fetch karne ke liye helper function
def get_status(key):
    return "✅" if Bot.getData(key) else "❌"

# Har ek gateway ka current status check karna
rj = get_status("rj")
info = get_status("info")
vsv = get_status("vsv")
payzy = get_status("payzy")
fxl = get_status("Fxl")
tg = get_status("Tgwallet")
RDX = get_status("RDX")
X = get_status("X")
E = get_status("e")
sa = get_status("sa")
ultra = get_status("ultra")
unio = get_status("unio")
# --- MULTIPLE SELECTION LOGIC END ---

# Inline Keyboard (Ab yeh hamesha database se live status uthaega)
markup = {
    "inline_keyboard": [
        [
            {"text": "Infotech Wallet", "callback_data": "/none"},
            {"text": info, "callback_data": "/inwalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": vsv, "callback_data": "/Vsvwalletsele0"}
        ],
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": payzy, "callback_data": "/Payzywalletsele"}
        ],
        [
            {"text": "FXL Wallet", "callback_data": "/none"},
            {"text": fxl, "callback_data": "/Fxlwalletsele0"}
        ],
        [
            {"text": "TG Wallet", "callback_data": "/none"},
            {"text": tg, "callback_data": "/Tgwalletsele0"}
        ],
        [
            {"text": "RDX Wallet", "callback_data": "/none"},
            {"text": RDX, "callback_data": "/RDXwalletsele0"}
        ],
        [
            {"text": "X Wallet", "callback_data": "/none"},
            {"text": X, "callback_data": "/Xwalletsele0"}
        ],
        [
            {"text": "RJ Wallet", "callback_data": "/none"},
            {"text": rj, "callback_data": "/rjwalletsele0"}
        ],
        [
            {"text": "E Wallet", "callback_data": "/none"},
            {"text": E, "callback_data": "/ewalletsele0"}
        ],
        [
            {"text": "Saathi Gateway", "callback_data": "/none"},
            {"text": sa, "callback_data": "/sawalletsele0"}
        ],
        [
            {"text": "Ultra Wallet", "callback_data": "/none"},
            {"text": ultra, "callback_data": "/ultrawalletsele0"}
        ],
        [
            {"text": "Unio Wallet", "callback_data": "/none"},
            {"text": unio, "callback_data": "/uniowalletsele0"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
status_text = "Active ✅" if new_sa_status else "Inactive ❌"
bot.replyText(u, f"<b><i>🔄 Saathi Gateway is {status_text} Now!</i></b>")


#======================================================================
# COMMAND: /selegetwayonbbo1t
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()




bot.replyText(
    u,
    "<b>💸 UPI Gateway Setup VSV\n\n"
    "✨ Send the <u>Token(VSV) & Tax in percentage</u>:\n\n"
    "🔢 Example : <code>Token-15</code>\n"
    "⚡ Choose wisely & send now!</b>",
    parse_mode="html"
)


Bot.handleNextCommand("/SetPerupiAmont1")


#======================================================================
# COMMAND: /selegetwayonbbot
#======================================================================
Admins=Bot.getData("AllBotAdminss") or []

if str(u) not in [str(x) for x in Admins]:
    bot.replyText(u,"<b><i>🚫 You Are Not This Bot Admin</i></b>",parse_mode="HTML")
    raise ReturnCommand()

GatewayList={
    "vsv":{"name":"Vsv Wallet","status_key":"vsv"},
    "payzy":{"name":"Payzy Wallet","status_key":"payzy"},
    "ultra":{"name":"Ultra Wallet","status_key":"ultra"},
    "txg":{"name":"TXG Wallet","status_key":"txg"},
    "rupix":{"name":"Rupix Wallet","status_key":"rupix"}
}

Bot.saveData("GatewayList",GatewayList)

markup=InlineKeyboardMarkup()

for gid,gw in GatewayList.items():
    name=gw.get("name",gid)
    status_key=gw.get("status_key",gid)
    status="🟢 ON" if Bot.getData(status_key) else "🔴 OFF"

    markup.row(
        InlineKeyboardButton(name,callback_data="/GatewayToggle "+str(gid)),
        InlineKeyboardButton(status,callback_data="/GatewayToggle "+str(gid))
    )

markup.row(
    InlineKeyboardButton("🔙 Back",callback_data="/addgetwayonbbot")
)

text="<b>🚧 Gateway Manager</b>\n\n💡 Click any gateway to turn it ON/OFF."

try:
    bot.editMessageText(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=text,
        reply_markup=markup,
        parse_mode="HTML"
    )
except:
    try:
        bot.editMessageText(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=text,
            reply_markup=markup,
            parse_mode="HTML"
        )
    except:
        bot.replyText(u,text,reply_markup=markup,parse_mode="HTML")

raise ReturnCommand()


#======================================================================
# COMMAND: /setcool
#======================================================================
def save_cooltime(minutes):
    try:
        minutes = int(minutes)
        if minutes <= 0:
            minutes = 1   # minimum 1 minute to avoid 0 or negative
        Bot.setData("Cooltime", minutes)
        return f"✅ Cooltime updated to {minutes} minutes"
    except:
        return "❌ Invalid value. Please enter a number"
        


#======================================================================
# COMMAND: /setwallet
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_PAISA = "6287207173537666597"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_WALLET = "5472363448404809929"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"

# coded by @Jenish_Dobariya1

WalletStatus = Bot.getData("WalletWithdraw") or "ON"
if WalletStatus == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji><b> Wallet Withdraw Temporarily Disabled</b>', parse_mode="HTML")
    raise ReturnCommand()
    
# --- Cancel Operation Flow ---
if str(message.text) == "Cancel":
    Bot.runCommand("/PIRO_MainMenu")
    raise ReturnCommand()

# --- Anti-Fraud Verification Block (1 Wallet = 1 Account Only) ---
all_users = Bot.getData("AllUsers") or []
wallet_in_use = False
input_wallet = str(message.text).strip()

for user_id in all_users:
    if str(user_id) == str(u):
        continue # Apne hi purane data ko verification me skip karega
    
    saved_wallet = Bot.getData("UserWallet" + str(user_id))
    if str(saved_wallet) == input_wallet:
        wallet_in_use = True
        break

if wallet_in_use:
    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji> This Wallet Number Is Already Linked To Another User!</b>\n\n💡 Please enter a different one.'
    )
    raise ReturnCommand()

# --- String Type Validation Check (Strict 10-Digit Rules) ---
if input_wallet.isdigit() and len(input_wallet) == 10:
    Bot.saveData("UserWallet" + str(u), input_wallet)

    # Automatically map entry into registry
    if str(u) not in map(str, all_users):
        all_users.append(str(u))
        Bot.saveData("AllUsers", all_users)

    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<tg-emoji emoji-id="{EMOJI_SUCCESS}">✅</tg-emoji><b> Your Wallet Number Has Been Successfully Updated To:\n\n<tg-emoji emoji-id="{EMOJI_WALLET}">👉🏻</tg-emoji> Wallet : </b><code>{input_wallet}</code>'
    )

    # --- Referral Metrics Tracking System ---
    upLnk = User.getData("upLnk") or "n"
    if upLnk == "n":
        T_usLnkWallet = Bot.getData('T_usLnkWallet') or 0
        Bot.saveData('T_usLnkWallet', int(T_usLnkWallet) + 1)
        User.saveData("upLnk", "y")

        refBy = Bot.getData(str(u) + "Referral") or "NONE"
        if refBy != "NONE":
            RefWalletLnkC = Bot.getData(str(refBy) + "RefWalletLnkC") or 0
            Bot.saveData(str(refBy) + "RefWalletLnkC", int(RefWalletLnkC) + 1)

else:
    Bot.runCommand(
        "/PIRO_MainMenu",
        options=f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji> Invalid Wallet Number!</b>\n\n💡 It must be a 10-digit number only.'
    )
    raise ReturnCommand()
    


#======================================================================
# COMMAND: /setwallet1
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_PAISA = "6287207173537666597"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_WALLET = "5264895611517300926"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"


# coded by @Jenish_Dobariya1

# ================== UPI WITHDRAW STATUS ==================

UpiStatus = Bot.getData("UpiWithdraw") or "ON"

if UpiStatus == "OFF":
    bot.replyText(
        u,
        f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> UPI Withdraw Temporarily Disabled</b>',
        parse_mode="HTML"
    )
    raise ReturnCommand()


# ================== CANCEL ==================

if str(message.text) == "Cancel":
    Bot.runCommand("/PIRO_MainMenu")
    raise ReturnCommand()


# ================== UPI INPUT ==================

input_upi = str(message.text).strip()


# ================== UPI VALIDATION ==================

if "@" not in input_upi or len(input_upi) < 5:
    Bot.runCommand(
        "/PIRO_MainMenu",
        options=(
            f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji> Invalid UPI ID!</b>\n\n<tg-emoji emoji-id="{EMOJI_WALLET}">💳</tg-emoji><b> Send Correct UPI</b>'
        )
    )
    raise ReturnCommand()


# ================== LOAD SETTINGS ==================

SameUPI = Bot.getData("SameUPI") or "ON"

# Safety check
if SameUPI not in ["ON", "OFF"]:
    SameUPI = "ON"
    Bot.saveData("SameUPI", SameUPI)


# ================== LOAD USERS ==================

all_users = Bot.getData("AllUsers") or []


# ================== SAME UPI PROTECTION ==================
# ON  = Multiple users can use the same UPI
# OFF = One UPI can be linked to only one user

if SameUPI == "OFF":

    for user_id in all_users:

        # Skip current user's own UPI
        if str(user_id) == str(u):
            continue

        saved_upi = Bot.getData(
            "UserUPI" + str(user_id)
        )

        if str(saved_upi).strip().lower() == input_upi.lower():

            Bot.runCommand(
                "/PIRO_MainMenu",
                options=(
                    f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji>This UPI ID Is Already Linked '
                    "To Another User!</b>\n\n"
                    "💡 Please use a different UPI ID."
                )
            )
            raise ReturnCommand()


# ================== SAVE UPI ==================

Bot.saveData(
    "UserUPI" + str(u),
    input_upi
)


# ================== REGISTER USER ==================

if str(u) not in list(map(str, all_users)):

    all_users.append(str(u))

    Bot.saveData(
        "AllUsers",
        all_users
    )


# ================== SUCCESS ==================

Bot.runCommand(
    "/PIRO_MainMenu",
    options=(
        f'<b><tg-emoji emoji-id="{EMOJI_SUCCESS}">✅</tg-emoji>UPI Linked Successfully!</b>\n\n'
        f'<tg-emoji emoji-id="{EMOJI_WALLET}">💳</tg-emoji> <b>UPI:</b> <code>{input_upi}</code>'
    )
)


# ================== UPI LINK TRACKING ==================

upi_link_status = User.getData("upLnk") or "n"

if upi_link_status == "n":

    total_linked = Bot.getData(
        "T_usLnkUpi"
    ) or 0

    Bot.saveData(
        "T_usLnkUpi",
        int(total_linked) + 1
    )

    User.saveData(
        "upLnk",
        "y"
    )


    # ================== REFERRAL TRACKING ==================

    ref_by = Bot.getData(
        str(u) + "Referral"
    ) or "NONE"

    if ref_by != "NONE":

        ref_link_count = Bot.getData(
            str(ref_by) + "RefUpiLnkC"
        ) or 0

        Bot.saveData(
            str(ref_by) + "RefUpiLnkC",
            int(ref_link_count) + 1
        )


#======================================================================
# COMMAND: /shareprofile
#======================================================================
try:

    # ============================================================
    # 🛑 CHECK CONTACT VERIFICATION SYSTEM
    # ============================================================

    VerifySystemStatus = Bot.getData(
        "VerifySystemStatus"
    ) or "OFF"


    # If Contact Verification is OFF
    if VerifySystemStatus != "ON":

        Bot.runCommand(
            "/PIRO_MainMenu"
        )

        raise ReturnCommand()


    # ============================================================
    # 📱 INCOMING CONTACT
    # ============================================================

    contact = message.contact


    if contact:

        phone_number = contact.phone_number
        user_id = contact.user_id
        current_sender_id = message.from_user.id


        # ========================================================
        # 🔐 SECURITY CHECK
        # ========================================================

        if user_id and str(user_id) != str(current_sender_id):

            bot.sendMessage(
                "❌ <b>Verification Failed!</b>\n\n"
                "Aapko apna khud ka number share karna hoga.",
                parse_mode="HTML"
            )

            Bot.handleNextCommand(
                "/shareprofile"
            )

            raise ReturnCommand()


        # ========================================================
        # ✅ SAVE CONTACT VERIFICATION
        # ========================================================

        User.saveData(
            "user_phone",
            str(phone_number)
        )

        User.saveData(
            "is_verified",
            True
        )


        # ========================================================
        # 🔐 CAPTCHA CHECK
        # ========================================================

        Captcha = Bot.getData(
            "CaptchaMode"
        ) or "ON"


        if Captcha == "ON":

            verify = User.getData(
                "verify"
            )


            if verify != "ok":

                # 🧹 DELETE CONTACT MESSAGE
                try:

                    current_msg_id = message.message_id

                    bot.deleteMessage(
                        chat_id=current_sender_id,
                        message_id=current_msg_id
                    )

                    bot.deleteMessage(
                        chat_id=current_sender_id,
                        message_id=current_msg_id - 1
                    )

                except:

                    pass


                # 🚀 GO TO MAIN MENU
                # MainMenu will send user to CAPTCHA
                Bot.runCommand(
                    "/PIRO_MainMenu"
                )

                raise ReturnCommand()


        # ========================================================
        # 🧹 DELETE CONTACT MESSAGES
        # ========================================================

        try:

            current_msg_id = message.message_id

            bot.deleteMessage(
                chat_id=current_sender_id,
                message_id=current_msg_id
            )

            bot.deleteMessage(
                chat_id=current_sender_id,
                message_id=current_msg_id - 1
            )

        except:

            pass


        # ========================================================
        # 🚀 ALL VERIFICATION PASSED
        # ========================================================

        Bot.runCommand(
            "/PIRO_MainMenu"
        )

        raise ReturnCommand()


    # ============================================================
    # 📱 INITIAL CONTACT PROMPT
    # ============================================================

    reply_markup = {
        "keyboard": [
            [
                {
                    "text": "📱 Share Profile",
                    "request_contact": True
                }
            ]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }


    bot.sendMessage(
        "<b>🔒 Please Verify Your Profile To Avoid Fake Accounts\n\n"
        "⚠️ Your Profile Is Not Shared With Anyone & Is Safe !!</b>",
        parse_mode="HTML",
        reply_markup=reply_markup
    )


    # ============================================================
    # 🔁 HANDLE NEXT CONTACT
    # ============================================================

    Bot.handleNextCommand(
        "/shareprofile"
    )

    raise ReturnCommand()


except Exception as e:

    if type(e).__name__ != "ReturnCommand":

        pass


#======================================================================
# COMMAND: /social
#======================================================================
# --- Command: /addsocial ---
AllBotAdminss = Bot.getData("AllBotAdminss") or []
is_Admin = str(u) in [str(userid) for userid in AllBotAdminss]

if not is_Admin:
    bot.replyText(u, "<b>🚫 You Are Not Authorized!</b>")
    raise ReturnCommand()

# Ask admin for input
bot.sendMessage("📌 Send Social Media in this format:\n\n<b>ButtonName - https://link.com</b>")
Bot.handleNextCommand("/savesocial")


#======================================================================
# COMMAND: /start
#======================================================================
EMOJI_FAILED="6129840374971112593"
EMOJI_PIN="6129434968713076807"
EMOJI_SUCCESS="6082398290773546707"
EMOJI_HEART="5388790256772331442"

# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]
# Page-wise channel join (FAST: cache 1 min, delete only on Joined)
# A sent join request counts as joined — admin approval is not required.

if message.chat.type!="private": raise returnCommand()

AllBotAdminss=Bot.getData("AllBotAdminss") or []
if AllBotAdminss==[]:
    MAIN_ADMIN=u
    AllBotAdminss.append(MAIN_ADMIN)
    Bot.saveData("AllBotAdminss",AllBotAdminss)
    Bot.saveData("Owner",u)
    AllBotAdminss=Bot.getData("AllBotAdminss") or []

BotMode=Bot.getData("BotMode") or "ON"
if BotMode=="OFF":
    bot.replyText(u,f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

if Bot.getData("Bot7DayTimer")!="STARTED":
    Bot.saveData("Bot7DayTimer","STARTED")
    Bot.runCommandAfter(604800,"/AutoCheckBot")

referalID=None
if params!=None: referalID=Bot.getData(str(params)+"GetTgIDbyRefLetters")

FulUsrs=Bot.getData("FulBotUsrs") or []
refer=params

if params!=None:
    A=params
    if str(A[slice(3)])=="ref": refer=referalID

if params==None: refer="@not_referred"

Neww=Bot.getData("UserID"+str(u))
if Neww==None:
    Bot.saveData("UserID"+str(u),"done")
    FulUsrs.append(u)
    Bot.saveData("FulBotUsrs",FulUsrs)
    RefStrtC=Bot.getData(str(refer)+"RefStrtC") or 0
    Bot.saveData(str(refer)+"RefStrtC",RefStrtC+1)

already=User.getData("bot_user")

if already==None:
    Bot.saveData(str(u)+"Referral",refer)

    NewUserNotification=Bot.getData("NewUserNotification") or "ON"

    if NewUserNotification=="ON":

        if refer=="@not_referred":
            invited_text="🤖 Auto Started"
        else:
            invited_text=f'<a href="tg://user?id={refer}">{refer}</a>'

        safe_name=str(message.from_user.first_name or "Trying to fetch").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

        notify_text=f"""
<b><tg-emoji emoji-id="6224161941305169199">🎉</tg-emoji> New User Joined!</b>

<tg-emoji emoji-id="5039613856603702817">👤</tg-emoji> <b>User:</b> <a href="tg://user?id={u}">{safe_name}</a>
<tg-emoji emoji-id="5042334757040423886">🆔</tg-emoji> <b>User ID:</b> <code>{u}</code>
<tg-emoji emoji-id="5398001711786762757">👥</tg-emoji> <b>Invited By:</b> {invited_text}
"""

        for admin in AllBotAdminss:
            try: bot.replyText(admin,notify_text,parse_mode="HTML")
            except: pass

    User.saveData("bot_user",True)

    T_usrs=Bot.getData("total_users")
    if T_usrs==None: Bot.saveData("total_users",1)
    else: Bot.saveData("total_users",int(T_usrs)+1)

BotAdmins=Bot.getData("AllBotAdminss") or [str(u)]
BOTID=int(Bot.info().token.split(":")[0])

AMC=Bot.getData("AllMainCh") or []
AMCU=Bot.getData("AllMainChUsernm") or []
AMCL=Bot.getData("AllMainChlink") or []
AMCTGID=Bot.getData("AllMainChTGID") or []
AMCP=Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)
for _pad in range(len(AMCTGID) - len(AMCU)):
    AMCU.append("Unknown")
for _pad in range(len(AMCTGID) - len(AMCL)):
    AMCL.append("https://t.me/" + str(AMCTGID[len(AMCL)]))

ALL_PAGES=sorted(set(AMCP)) if AMCTGID else []
CurPage=ALL_PAGES[0] if ALL_PAGES else 1

# ---- verified-channel cache (valid for the current MINUTE only) ----
_now = libs.DateAndTime.now("Asia/Kolkata")
Stamp = str(_now["date"]) + " " + str(_now["time"])[:5]
OKids = []
try:
    _c = User.getData("PIRO_OK")
    if _c and _c.get("s") == Stamp:
        OKids = list(_c.get("ids") or [])
except:
    OKids = []

joinSTAT="JOIND"
PIRO_NJCL=[]
FoundIdx=None

# Always start from the FIRST page, so pages come strictly 1 -> 2 -> 3
for PageIdx in range(0, len(ALL_PAGES)):
    ThisPage=ALL_PAGES[PageIdx]
    NotJoinedThisPage=[]

    IND=0
    for i in AMCTGID:
        if AMCP[IND]!=ThisPage:
            IND+=1
            continue

        sid=str(i)
        if sid in OKids:
            IND+=1
            continue

        UC="error"
        ERR=""
        try:
            UC=bot.getChatMember(i,u).status
        except Exception as e:
            UC="error"
            ERR=str(e)[:150]

        if UC=="member" or UC=="administrator" or UC=="creator":
            OKids.append(sid)

        elif UC=="left" or UC=="kicked":
            # A sent join request also counts as joined (no approval wait needed)
            ReqRec=Bot.getData(sid+"JoinRRof"+str(u)) or "N"
            if ReqRec=="N":
                NotJoinedThisPage.append(sid)

        elif UC=="error":
            DC=Bot.getData(sid+"isDef") or "Y"
            JR=Bot.getData(sid+"JoinReq") or "Y"
            if JR=="Y" and DC!="Y":
                BotIsAdm=False
                try:
                    BS=bot.getChatMember(i,BOTID).status
                    if BS=="administrator" or BS=="creator":
                        BotIsAdm=True
                except:
                    BotIsAdm=False

                if not BotIsAdm:
                    if Bot.getData("PIRO_NAsent"+sid)!="Y":
                        Bot.saveData("PIRO_NAsent"+sid,"Y")
                        for admin in BotAdmins:
                            try: bot.replyText(admin,f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️\n\n✨ Only admins see this reminder (sent once per channel). 😊</b>")
                            except: pass
                else:
                    Bot.deleteData("PIRO_NAsent"+sid)
                    if Bot.getData("PIRO_ERRsent"+sid)!="Y":
                        Bot.saveData("PIRO_ERRsent"+sid,"Y")
                        for admin in BotAdmins:
                            try: bot.replyText(admin,f"<b>ℹ️ Bot IS admin in {AMCU[IND]}, but a member check failed:</b>\n<code>{ERR}</code>\n<i>(sent once per channel, only admins see this)</i>")
                            except: pass

        IND+=1

    if NotJoinedThisPage:
        joinSTAT="NOTJOIN"
        PIRO_NJCL=NotJoinedThisPage
        FoundIdx=PageIdx
        break

User.saveData("PIRO_OK",{"s":Stamp,"ids":OKids})

if FoundIdx is not None:
    CurPage=ALL_PAGES[FoundIdx]
elif ALL_PAGES:
    CurPage=ALL_PAGES[-1]

User.saveData("PIRO_CurPage",CurPage)
User.saveData("PIRO_NJCL",PIRO_NJCL)

Captcha=Bot.getData("CaptchaMode") or "ON"

if joinSTAT=="JOIND":
    if Captcha=="OFF": User.saveData("PhVerification","verify")
    Bot.runCommand("/PIRO_MainMenu")
    raise ReturnCommand()

# NOTE: old join message is intentionally NOT deleted here anymore.
# It is only deleted when the user actually taps the Joined button (faster /start & gates).

JoinBtnText = Bot.getData("PIRO_JoinBtnText") or "Join"
ClaimBtnText = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
JoinIcon = Bot.getData("PIRO_JoinBtnEmojiId")
ClaimIcon = Bot.getData("PIRO_ClaimBtnEmojiId")

keyboard=[]
row=[]
IND=0

for i in AMCTGID:
    if str(i) in PIRO_NJCL:
        btn={"text":JoinBtnText,"url":AMCL[IND],"style":"primary"}
        if JoinIcon: btn["icon_custom_emoji_id"]=JoinIcon
        row.append(btn)
        if len(row)==2:
            keyboard.append(row)
            row=[]
    IND+=1

if row: keyboard.append(row)

SocialLinks=Bot.getData("AllSocialLinks") or []

if SocialLinks:
    row=[]
    for s in SocialLinks:
        row.append({"text":f"{s['name']}","url":s['url'],"style":"primary"})
        if len(row)==2:
            keyboard.append(row)
            row=[]
    if row: keyboard.append(row)

cbtn={"text":ClaimBtnText,"callback_data":"🟢 Joined","style":"success"}
if ClaimIcon: cbtn["icon_custom_emoji_id"]=ClaimIcon
keyboard.append([cbtn])

usr=f'<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>'

JoinMsgChatId = Bot.getData("PIRO_JoinMsgChatId")
JoinMsgId = Bot.getData("PIRO_JoinMsgId")

SentOk = False
if JoinMsgChatId and JoinMsgId:
    try:
        Sent = bot.copyMessage(chat_id=u, from_chat_id=JoinMsgChatId, message_id=JoinMsgId, reply_markup={"inline_keyboard":keyboard})
        try:
            Mid = Sent.message_id
        except:
            Mid = Sent["message_id"]
        User.saveData("PIRO_ltmg", Mid)
        SentOk = True
    except:
        SentOk = False

if not SentOk:
    PIRO=bot.sendMessage(
        f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""",
        reply_markup={"inline_keyboard":keyboard}
    )

    User.saveData("PIRO_ltmg",PIRO.message_id)

# Extra message shown below the join message (admin-editable)
Ex1 = Bot.getData("PIRO_JoinMsg2ChatId")
Ex2 = Bot.getData("PIRO_JoinMsg2Id")
if Ex1 and Ex2:
    try:
        S2 = bot.copyMessage(chat_id=u, from_chat_id=Ex1, message_id=Ex2)
        try:
            M2 = S2.message_id
        except:
            M2 = S2["message_id"]
        User.saveData("PIRO_ltmg2", M2)
    except:
        pass


#======================================================================
# COMMAND: /test
#======================================================================
# /gateway_status_checker

# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
if str(u) not in list(map(str, Admins)):
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

def get_status(key):
    return "✅" if Bot.getData(key) else "❌"

# Gateway status indicators

payzy = get_status("payzy")
vsv = get_status("vsv")

# Inline Keyboard
markup = {
    "inline_keyboard": [
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": payzy, "callback_data": "/payzywalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": vsv, "callback_data": "/Vsvwalletsele1"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Displaying or Editing the message
bot.editMessageText(
    chat_id=message.chat.id,
    message_id=message.message_id,
    text="<b>🚧 Choose The Gateways</b>",
    reply_markup=markup
)


#======================================================================
# COMMAND: /textoff
#======================================================================
AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(
        u,
        "<b><i>🚫 You Are Not This Bot Admin</i></b>",
        parse_mode="HTML"
    )
    raise ReturnCommand()

off_markup = InlineKeyboardMarkup()

off_markup.add(
    InlineKeyboardButton(
        text="🏧 UPI Withdraw Off Text",
        callback_data="/UPIOFF_Text"
    )
)

off_markup.add(
    InlineKeyboardButton(
        text="👜 Wallet Withdraw Off Text",
        callback_data="/WalletOFF_Text"
    )
)

off_markup.add(
    InlineKeyboardButton(
        text="🔙 Back To Admin",
        callback_data="/admin"
    )
)

off_txt = """<b>⚙️ Withdraw Off Text Management

Choose an option below 👇

🏧 UPI Withdraw Off Text
👜 Wallet Withdraw Off Text

Here you can set custom messages shown when withdrawals are disabled.</b>"""

try:
    bot.editMessageText(
        chat_id=u,
        message_id=message.message_id,
        text=off_txt,
        reply_markup=off_markup,
        parse_mode="HTML"
    )
except:
    bot.replyText(
        u,
        off_txt,
        parse_mode="HTML",
        reply_markup=off_markup
    )

raise ReturnCommand()


#======================================================================
# COMMAND: /toggle_all_modes
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []
if str(u) not in [str(uid) for uid in AllBotAdminss]:
    raise ReturnCommand()

# वर्तमान मोड को चक्र (Loop) में आगे बढ़ाना
current_mode = Bot.getData("MasterWithdrawMode") or "both_on"

if current_mode == "both_on":
    next_mode = "wallet_on"
    Bot.saveData("WalletWithdrawMode", "ON")
    Bot.saveData("UpiWithdrawMode", "OFF")
    alert_msg = "💼 Wallet Only Enabled!"

elif current_mode == "wallet_on":
    next_mode = "upi_on"
    Bot.saveData("WalletWithdrawMode", "OFF")
    Bot.saveData("UpiWithdrawMode", "ON")
    alert_msg = "🏦 UPI Only Enabled!"

elif current_mode == "upi_on":
    next_mode = "both_off"
    Bot.saveData("WalletWithdrawMode", "OFF")
    Bot.saveData("UpiWithdrawMode", "OFF")
    alert_msg = "🔴 All Withdrawals Stopped!"

else:
    next_mode = "both_on"
    Bot.saveData("WalletWithdrawMode", "ON")
    Bot.saveData("UpiWithdrawMode", "ON")
    alert_msg = "🟢 Both Systems Activated!"

# नए मोड को डेटाबेस में सेव करना
Bot.saveData("MasterWithdrawMode", next_mode)

# स्क्रीन पर एक छोटा सा पॉप-अप अलर्ट दिखाना (यह नया पेज नहीं खोलेगा)
try:
    bot.answerCallbackQuery(call.id, alert_msg, show_alert=False)
except:
    pass

# 🔄 उसी समय एडमिन पैनल को उसी जगह रिफ्रेश करना ताकि नया नाम तुरंत दिखने लगे
Bot.runCommand("/admin")


#======================================================================
# COMMAND: /toggle_upi
#======================================================================
# Coded by: @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []
if str(u) not in [str(uid) for uid in AllBotAdminss]:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# स्टेटस बदलना
current = Bot.getData("UpiWithdrawMode") or "ON"
new_status = "OFF" if current == "ON" else "ON"
Bot.saveData("UpiWithdrawMode", new_status)

bot.replyText(
    u, 
    f"<b>🏦 UPI Withdrawal Status Updated!</b>\n\n━━━━━━━━━━━━━━━━━━━━\n"
    f"📌 <b>Current Status:</b> <code>{new_status}</code>\n"
    f"━━━━━━━━━━━━━━━━━━━━\n"
    f"<i>👉 To change it again, run <code>/toggle_upi</code></i>", 
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /toggle_wallet
#======================================================================
# Coded by: @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []
if str(u) not in [str(uid) for uid in AllBotAdminss]:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# पुराने वेरिएबल को बिना डिस्टर्ब किए स्टेटस बदलना
current = Bot.getData("WalletWithdrawMode") or "ON"
new_status = "OFF" if current == "ON" else "ON"
Bot.saveData("WalletWithdrawMode", new_status)

bot.replyText(
    u, 
    f"<b>💼 Wallet Withdrawal Status Updated!</b>\n\n━━━━━━━━━━━━━━━━━━━━\n"
    f"📌 <b>Current Status:</b> <code>{new_status}</code>\n"
    f"━━━━━━━━━━━━━━━━━━━━\n"
    f"<i>👉 To change it again, run <code>/toggle_wallet</code></i>", 
    parse_mode="HTML"
)


#======================================================================
# COMMAND: /toggle_wd_status
#======================================================================
# coded by @Jenish_Dobariya1

AllBotAdminss = Bot.getData("AllBotAdminss") or []
if str(u) not in [str(uid) for uid in AllBotAdminss]:
    raise ReturnCommand()

# वर्तमान मोड को चक्र (Loop) में आगे बढ़ाना
current_mode = Bot.getData("MasterWithdrawMode") or "both_on"

if current_mode == "both_on":
    next_mode = "wallet_on"
    Bot.saveData("WalletWithdrawMode", "ON")
    Bot.saveData("UpiWithdrawMode", "OFF")
    alert_msg = "💼 Wallet Only Enabled!"

elif current_mode == "wallet_on":
    next_mode = "upi_on"
    Bot.saveData("WalletWithdrawMode", "OFF")
    Bot.saveData("UpiWithdrawMode", "ON")
    alert_msg = "🏦 UPI Only Enabled!"

elif current_mode == "upi_on":
    next_mode = "both_off"
    Bot.saveData("WalletWithdrawMode", "OFF")
    Bot.saveData("UpiWithdrawMode", "OFF")
    alert_msg = "🔴 All Withdrawals Stopped!"

else:
    next_mode = "both_on"
    Bot.saveData("WalletWithdrawMode", "ON")
    Bot.saveData("UpiWithdrawMode", "ON")
    alert_msg = "🟢 Both Systems Activated!"

# नए मोड को डेटाबेस में सेव करना
Bot.saveData("MasterWithdrawMode", next_mode)

# स्क्रीन पर एक छोटा सा पॉप-अप अलर्ट दिखाना
try:
    bot.answerCallbackQuery(call.id, alert_msg, show_alert=False)
except:
    pass

# 🔄 एडमिन पैनल को उसी समय रिफ्रेश करना
Bot.runCommand("/admin")


#======================================================================
# COMMAND: /ultrawalletsele0
#======================================================================
# Admin Verification
Admins = Bot.getData("AllBotAdminss") or []
is_Admin = False

for admin_id in Admins:
    if str(u) == str(admin_id):
        is_Admin = True

if not is_Admin:
    bot.replyText(u, "<b><i>🚫 You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()

# --- MULTIPLE SELECTION LOGIC START ---
# Baaki gateways ko bina chhede, sirf "ultra" ka status toggle (ON/OFF) hoga
current_ultra_status = Bot.getData("ultra")
new_ultra_status = False if current_ultra_status else True
Bot.saveData("ultra", new_ultra_status)

# Agar Ultra active hua hai, toh uski details save karein
if new_ultra_status:
    Bot.saveData("gatewaynow", "ultra")
    Bot.saveData("gatewaytype", "https://ultra-pay.in/")

# Sabhi gateways ka live status database se fetch karne ke liye helper function
def get_status(key):
    return "✅" if Bot.getData(key) else "❌"

# Har ek gateway ka current status check karna
rj = get_status("rj")
info = get_status("info")
vsv = get_status("vsv")
payzy = get_status("payzy")
fxl = get_status("Fxl")
tg = get_status("Tgwallet")
RDX = get_status("RDX")
X = get_status("X")
E = get_status("e")
sa = get_status("sa")
ultra = get_status("ultra")
unio = get_status("unio")
# --- MULTIPLE SELECTION LOGIC END ---

# Inline Keyboard (Ab yeh hamesha database se latest status cross/check uthaega)
markup = {
    "inline_keyboard": [
        [
            {"text": "Infotech Wallet", "callback_data": "/none"},
            {"text": info, "callback_data": "/inwalletsele0"}
        ],
        [
            {"text": "Vsv Wallet", "callback_data": "/none"},
            {"text": vsv, "callback_data": "/Vsvwalletsele0"}
        ],
        [
            {"text": "Payzy Wallet", "callback_data": "/none"},
            {"text": payzy, "callback_data": "/Payzywalletsele"}
        ],
        [
            {"text": "FXL Wallet", "callback_data": "/none"},
            {"text": fxl, "callback_data": "/Fxlwalletsele0"}
        ],
        [
            {"text": "TG Wallet", "callback_data": "/none"},
            {"text": tg, "callback_data": "/Tgwalletsele0"}
        ],
        [
            {"text": "RDX Wallet", "callback_data": "/none"},
            {"text": RDX, "callback_data": "/RDXwalletsele0"}
        ],
        [
            {"text": "X Wallet", "callback_data": "/none"},
            {"text": X, "callback_data": "/Xwalletsele0"}
        ],
        [
            {"text": "RJ Wallet", "callback_data": "/none"},
            {"text": rj, "callback_data": "/rjwalletsele0"}
        ],
        [
            {"text": "E Wallet", "callback_data": "/none"},
            {"text": E, "callback_data": "/ewalletsele0"}
        ],
        [
            {"text": "Saathi Gateway", "callback_data": "/none"},
            {"text": sa, "callback_data": "/sawalletsele0"}
        ],
        [
            {"text": "Ultra Wallet", "callback_data": "/none"},
            {"text": ultra, "callback_data": "/ultrawalletsele0"}
        ],
        [
            {"text": "Unio Wallet", "callback_data": "/none"},
            {"text": unio, "callback_data": "/uniowalletsele0"}
        ],
        [
            {"text": "🔙 Back", "callback_data": "/addgetwayonbbot"}
        ]
    ]
}

# Update UI
try:
    bot.editMessageText(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text="<b>🚧 Choose The Gateways</b>",
        reply_markup=markup
    )
except:
    pass

# Confirmation message
status_text = "Active ✅" if new_ultra_status else "Inactive ❌"
bot.replyText(u, f"<b><i>🔄 Ultra Wallet is {status_text} Now!</i></b>")


#======================================================================
# COMMAND: /verifiedStats
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

AllBotAdminss = Bot.getData("AllBotAdminss") or []

is_Admin = False
for userid in AllBotAdminss:
    if str(u) == str(userid):
        is_Admin = True

if is_Admin != True:
    bot.replyText(u, "<b><i>🚫You Are Not This Bot Admin</i></b>")
    raise ReturnCommand()
    
T_usLnkWallet=Bot.getData('T_usLnkWallet') or 0

T_usLnkUpi = int(Bot.getData("T_usLnkUpi") or 0)

T_usClimBon=Bot.getData('T_usClimBon') or 0
        
T_verifUsrs=Bot.getData('T_verifUsrs') or 0

FulUsrs=Bot.getData("FulBotUsrs") or []

m = f"""<b>👍Total Verified Users In Bot : {T_verifUsrs} Users

👍Total Users Claimed Bonus : {T_usClimBon} Users

👍Total Users Linked Wallet : {T_usLnkWallet} Users

📍 Powered By - @Jenish_Dobariya1 </b>"""

markup = InlineKeyboardMarkup()

markup.row(
    InlineKeyboardButton(
        text="⬅️ Back",
        callback_data="/AdminStats"
    )
)

bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=m,
    parse_mode="HTML",
    reply_markup=markup
)


#======================================================================
# COMMAND: @
#======================================================================
EMOJI_PARTY = "6224161941305169199"
EMOJI_BALL = "5039613856603702817"
EMOJI_DONE = "5398001711786762757"
EMOJI_PAISA = "5042334757040423886"
EMOJI_FAILED = "6129840374971112593"
EMOJI_WARN = "5447644880824181073"

if message.update_type == "chat_join_request":
    Bot.saveData(f"{message.chat.id}JoinRRof{u}", "Y")

if message.chat.type != "private":
    raise returnCommand()

PIRO_ban = Bot.getData(f"{u}ban") or False

if PIRO_ban:
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> You\'re banned in this bot</b>')
    raise returnCommand()


#======================================================================
# COMMAND: Balance
#======================================================================
EMOJI_FAILED = "6129840374971112593"

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Bot Is Currently Off</b>')
    raise ReturnCommand()

# Page-wise join check, then open the balance screen
User.saveData("PIRO_GateTarget", "💴 Account1")
Bot.runCommand("/PIRO_JoinGate")


#======================================================================
# COMMAND: Bonus
#======================================================================
EMOJI_FAILED = "6129840374971112593"

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

# Page-wise join check, then open the bonus screen
User.saveData("PIRO_GateTarget", "🎁 Bonus1")
Bot.runCommand("/PIRO_JoinGate")


#======================================================================
# COMMAND: Link UPI
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_PIN = "6129434968713076807"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_HEART = "5388790256772331442"

# coded by @Jenish_Dobariya1
WitdMode = Bot.getData("WithdrawMode") or "ON"
if WitdMode == "OFF":
    WOT = Bot.getData("WOT") or "<b>⛔ Withdrawal Is Off</b>"
    bot.replyText(u, WOT)
    raise ReturnCommand()
    
if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, "<b>🙇‍♂️ Bot Is Currently Off</b>")
    raise ReturnCommand()

BotAdmins = Bot.getData("AllBotAdminss") or [str(u)]

joinSTAT = "JOIND"
# Gateway setting UPI par set rakhein
Gatewaysett011 = Bot.getData("gatewaytype") or "Not Set"

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []

User.deleteData("PIRO_NJCL")
PIRO_NJCL = []

BINA = False
IND = 0

for i in AMCTGID:
    try:
        UC = bot.getChatMember(i, u)
        UC = UC.status
    except:
        UC = "error"

    ReqRec = Bot.getData(str(i) + "JoinRRof" + str(u)) or "N"

    if UC == "left" and ReqRec == "N":
        joinSTAT = "NOTJOIN"
        PIRO_NJCL.append(str(i))

    DC = Bot.getData(str(i) + "isDef") or "Y"
    JR = Bot.getData(str(i) + "JoinReq") or "Y"

    if UC == "error" and JR == "Y":
        if DC == "Y":
            continue
        for admin in BotAdmins:
            try:
                bot.replyText(admin, f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️\n\n✨ Don't worry, this message is only for admins as a reminder. 😊</b>")
            except:
                pass
        BINA = True

    IND += 1

User.saveData("PIRO_NJCL", PIRO_NJCL)

if BINA:
    raise ReturnCommand()

if joinSTAT == "JOIND":
     pass 
else:
    if not AMCL:
        bot.sendMessage("📌 No channels found!")
    else:
        keyboard = []
        row = []
        IND = 0
        for LINK in AMCL:
            if str(AMCTGID[IND]) in PIRO_NJCL:
                row.append({"text": "Join", "url": LINK,"style":"primary"})
                if len(row) == 2:
                    keyboard.append(row)
                    row = []
            IND += 1
        if row:
            keyboard.append(row)
        keyboard.append([{"text": "🔒 Claim", "callback_data": "🟢 Joined","style":"success"}])
        usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""
        PIRO = bot.sendMessage(f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""", reply_markup={"inline_keyboard": keyboard})

User.saveData("PIRO_ltmg", PIRO.message_id)

raise ReturnCommand()
# ----------- GET UPI DATA -----------
upi = Bot.getData("UserUPI" + str(u)) or "Not Linked"
UpiStatus = Bot.getData("UpiWithdraw") or "ON"

if UpiStatus == "OFF":
    bot.replyText(
        u,
        "<b>⛔ UPI Withdrawal Is Currently Disabled</b>",
        parse_mode="html"
    )
    raise ReturnCommand()

text = f"<b>🏦 Your Current UPI - <code>{upi}</code>\n\nClick Below To Link/Update UPI 👇</b>"

buttons = [[
    InlineKeyboardButton("🏦 Link UPI", callback_data="link_upi")
]]

keyboard = InlineKeyboardMarkup(buttons)

bot.replyText(
    u,
    text,
    parse_mode="html",
    reply_markup=keyboard
)


#======================================================================
# COMMAND: Link Wallet
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_SIRE = "5316709465616031741"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
UNIVERSE = "5447410659077661506"
EMOJI_DOWN = "6280368546220349439"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"
EMOJI_SIREN = "5395695537687123235"

# coded by @Jenish_Dobariya1

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>', parse_mode="HTML")
    raise ReturnCommand()

BotAdmins = Bot.getData("AllBotAdminss") or [str(u)]
joinSTAT = "JOIND"

# --- SYSTEM INTEGRITY CHECK ---
AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []

User.deleteData("PIRO_NJCL")
PIRO_NJCL = []
BINA = False
IND = 0

for i in AMCTGID:
    try:
        UC = bot.getChatMember(i, u)
        UC = UC.status
    except:
        UC = "error"

    ReqRec = Bot.getData(str(i) + "JoinRRof" + str(u)) or "N"

    if UC == "left" and ReqRec == "N":
        joinSTAT = "NOTJOIN"
        PIRO_NJCL.append(str(i))

    DC = Bot.getData(str(i) + "isDef") or "Y"
    JR = Bot.getData(str(i) + "JoinReq") or "Y"

    if UC == "error" and JR == "Y":
        if DC == "Y":
            continue
        for admin in BotAdmins:
            try:
                bot.replyText(admin, f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️\n\n✨ Reminder for Admin only.</b>", parse_mode="HTML")
            except:
                pass
        BINA = True
    IND += 1

User.saveData("PIRO_NJCL", PIRO_NJCL)

if BINA:
    raise ReturnCommand()

# --- FORCED CHANNEL JOIN LOGIC ---
# --- FORCED CHANNEL JOIN LOGIC ---
if joinSTAT != "JOIND":
    if not AMCL:
        bot.sendMessage("📌 No channels found!")
    else:
        keyboard = []
        row = []
        IND = 0

        for LINK in AMCL:
            if str(AMCTGID[IND]) in PIRO_NJCL:
                row.append({"text": "Join", "url": LINK,"style":"primary"})
                if len(row) == 2:
                    keyboard.append(row)
                    row = []
            IND += 1

        if row:
            keyboard.append(row)

        keyboard.append([{"text": "Claim", "callback_data": "🟢 Joined","style":"success","icon_custom_emoji_id":"5296369303661067030"}])
        usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

        try:
            PIRO = bot.sendMessage(f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""", reply_markup={"inline_keyboard": keyboard}, parse_mode="HTML")
            
            # This will only execute if the message sent successfully
            User.saveData("PIRO_ltmg", PIRO.message_id)
            
        except Exception as e:
            # Fallback safe assignment if the send fails
            PIRO = None
            print(f"Error sending message: {e}")

        raise ReturnCommand()
        


# --- STRICT WITHDRAWAL OFF CHECK ---
# --- STRICT WITHDRAWAL OFF CHECK FOR LINK WALLET ONLY ---
W_Mode = Bot.getData("WalletWithdrawMode") or Bot.getData("WithdrawMode") or "ON"
current_status = str(W_Mode).strip().upper()

if current_status == "OFF" or current_status == "FALSE":
    # Link wallet ke liye fixed alert text jo aapne manga:
    bot.replyText(u, f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji>Wallet Withdrawal off link your wallet after on</b>', parse_mode="HTML")
    raise ReturnCommand()
    

# --- MULTI-GATEWAY ACTIVE DETECTION SYSTEM ---
gateway_names_map = {
    "sa": "https://saathigateway.com",
    "vsv": "http://vsv-gateway-solutions.co.in",
    "payzy": "https://payzy-gateway.site",
    "ultra": "https://ultra-pay.in",
    "txg":"http://txg-gateway.xyz",
    "rupix":"https://rupixwallet.shop"
}

active_gateways_list = []

for key, gateway in gateway_names_map.items():
    if Bot.getData(key) == True:
        if str(gateway).startswith(("http://", "https://")):
            active_gateways_list.append(
                f'<a href="{gateway}"><b>{gateway}</b></a>'
            )
        else:
            active_gateways_list.append(
                f"<b>{gateway}</b>"
            )

if not active_gateways_list:
    gateway_display = "<b>Admin Not Connected Any Gateway 🚨</b>"
else:
    gateway_display = "\n".join(active_gateways_list)

# --- CHOOSE WALLET INPUT INTERFACE ---
keyboard = {
    "keyboard": [
        [
            {
                "text": "Cancel",
                "style": "primary",
                "icon_custom_emoji_id": EMOJI_FAIL
            }
        ]
    ],
    "resize_keyboard": True
}

bot.replyText(
    u,
    text=f"""<b><tg-emoji emoji-id="{EMOJI_SIRE}">✨</tg-emoji> Send Your Wallet Number To Link Wallet.</b>

<tg-emoji emoji-id="{UNIVERSE}">🔗</tg-emoji><b> Supported Gateways <tg-emoji emoji-id="{EMOJI_DOWN}">👇</tg-emoji>
<b>{gateway_display}</b>""",
    parse_mode="HTML",
    reply_markup=keyboard
)
Bot.handleNextCommand("/setwallet")


#======================================================================
# COMMAND: Payout Method
#======================================================================
EMOJI_FAILED = "6129840374971112593"

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Bot Is Currently Off</b>')
    raise ReturnCommand()

# Page-wise join check, then open the payout method menu
User.saveData("PIRO_GateTarget", "/PIRO_PayoutMenu")
Bot.runCommand("/PIRO_JoinGate")


#======================================================================
# COMMAND: Process_UPI
#======================================================================
# --- Manual HTML Escaper ---
def escape_html(text):
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

PaymentCh = Bot.getData("Botpaychannel") or "not set"
Botpayname = Bot.getData("BotPayComm") or "Payment"
GUID = Bot.getData("GUID") or "not set"
MID = Bot.getData("MID") or "not set"
Mkey = Bot.getData("MKEY") or "not set"
Token = Bot.getData("TOKEN")
AllBanUsers = (Bot.getData("AllBanUsers") or "12345").split(",")
if str(message.chat.id) in AllBanUsers:
    bot.replyText(u, "<b><i>🚫 You are Banned in this Bot</i></b>")
    raise ReturnCommand()

AllBanWallets = (Bot.getData("AllBanWallets") or "12345").split(",")
wallet = Bot.getData("UserWallet" + str(u))
if wallet and wallet in AllBanWallets:
    bot.replyText(u, "<b><i>🚫 Your Wallet is Banned in this Bot</i></b>")
    raise ReturnCommand()

WitdMode = Bot.getData("WithdrawMode") or "ON"
Gatewaysett0 = Bot.getData("gatewaynow") or "Not Set"
Gatewaysett011 = Bot.getData("gatewaytype") or "https://RJWallet.in/"
gateway_map = {
    "Rjwallet": "RJ Wallet",
    "full2sms": "F2S Wallet",
    "Tgwallet": "TG Wallet",
    "Fxl": "FXL Wallet",
    "lifafawala": "LifafaWala Wallet",
    "vsv1": "VSV Wallet"
}
Gatewaysett20 = gateway_map.get(Gatewaysett0, "Not Set")

if Gatewaysett0 == "Not Set":
    bot.replyText(u, "<b>⛔ Gateway Not Set</b>")
    raise ReturnCommand()

# Parse options
P = options.split("_")
MD = int(P[0])
amount = float(P[1])
bal = float(libs.Resources.anotherRes("Balance", user=u).value())
minWith = float(Bot.getData("MinWith1") or 5)
tax = float(Bot.getData("Tax1") or 0)
tax2 = float(Bot.getData("Tax2") or 0)
WithdrawC = int(Bot.getData("WithdrawC") or 0)
wallet = Bot.getData("UserUPI" + str(u)) or "1234567890"
hide_wallet = f"{wallet[0:3]}xxxxx{wallet[8:10]}"
AmountAftrTax = amount - (amount * tax / 100)
AmountAftrTax2 = amount - (amount * tax2 / 100)
token1 = Bot.getData("Token1")
token2 = Bot.getData("Token2")

if bal >= amount and amount >= minWith:
    libs.Resources.anotherRes("Balance", user=u).cut(amount)
    libs.Resources.anotherRes("Withdraw", user=u).add(amount)
    libs.Resources.globalRes("BotWithdraws").add(amount)
    Bot.saveData("WithdrawC", WithdrawC + 1)

    try:
        # 1. Fetch Active Gateway & its specific credentials
        active_gw = Bot.getData("gatewaynow") or "not set"
        token = Bot.getData(f"TOKEN_{active_gw}") # Dynamically fetch token for current gateway
        
        # 2. Gateway API Router
        if active_gw == "vsv1":
            url = f"https://vsv-gateway-solutions.co.in/Api/upi.php?token={token1}&upi_id={wallet}&amount={AmountAftrTax}&comment=Withdraw"
        elif active_gw == "payzy1":
            url = f"https://payzy-gateway.site/api/upi/?token={token2}&upi={wallet}&amount={AmountAftrTax2}"
        # Aap yahan aur gateways elif karke add kar sakte hain...
        else:
            raise Exception("Gateway URL not configured")

        # 3. API Execution
        response = HTTP.get(url, timeout=10)
        data = response.json()
        
        # ... (Baaki success/failure ka logic waisa hi rahega)

        response = HTTP.get(url)
        data = response.json()
        status = data.get("status", "")
        message_text = escape_html(data.get("message", "No message"))  # escape before use
        usr = f"""<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>"""
        balance0010 = float(libs.Resources.anotherRes("Balance", user=u).value())

        WITHmessage = f"""<b>🎁 Your Withdrawal Successfully Processed 🔥🚀\n\n✔️ Please Check Your <a href='{Gatewaysett011}'>{Gatewaysett20}</a> Account</b>"""
        WITHmessage01 = f"""<b>✅ New Withdrawal Requested ✅\n\n🟢 User : {usr}\n🚀 Amount : {amount}  ( FEES - {tax}%)\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>{message_text}</code>\n\n✌️ Current Balance : <code>{balance0010}</code>Rs\n\n🔴 Bot: @{Bot.info().username}</b>"""

        if status == "success":

           bot.replyText(PaymentCh, WITHmessage01, parse_mode="html")

           bot.editMessageText(
              chat_id=u,
              message_id=MD,
              text=WITHmessage,
              parse_mode="html",
              disable_web_page_preview=True
    )

           libs.Resources.globalRes("BotWithdrawsuccess").add(amount)

    # ✅ Add UPI Top Withdrawal Count Only On Success
           old_upi_w = libs.Resources.anotherRes(
           'Withdraw_UPI',
          user=u
        ).value() or 0

           libs.Resources.anotherRes(
        'Withdraw_UPI',
            user=u
        ).set(old_upi_w + amount)
        
        else:
            # Refund back on failure
            libs.Resources.anotherRes("Balance", user=u).add(amount)
            bot.editMessageText(chat_id=u, message_id=MD, text=(
                "<b>❌ Withdrawal Failed 🔥🚀\n\n"
                "⚠️ Reason: Invalid or incorrect wallet number.\n"
                "💡 Please double-check and try again!</b>"), parse_mode="HTML")
            
            # Notify payment channel about failure
            bot.replyText(PaymentCh, f"""<b>❌ Withdrawal Failed ❌\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>{message_text}</code>\n\n🔴 Bot: @{Bot.info().username}</b>""", parse_mode="html")

    except Exception as e:
        # Refund user balance on error/timeout
        libs.Resources.anotherRes("Balance", user=u).add(amount)
        error_msg = escape_html(str(e))  # escape before sending
        usr = f"""<a href="tg://user?id={message.chat.id}">{message.chat.id}</a>"""

        # Timeout or generic error
        if "timeout" in error_msg.lower():
            user_msg = "<b>⏳ Withdrawal Timeout! The gateway did not respond in time. Please try again later.</b>"
            channel_msg = f"""<b>⏳ Withdrawal Timeout ⏳\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : Gateway Timeout\n\n🔴 Bot: @{Bot.info().username}</b>"""
        else:
            user_msg = f"<b>⚠️ Error occurred:</b>"
            channel_msg = f"""<b>⚠️ Withdrawal Error ⚠️\n\n🟢 User : {usr}\n🚀 Amount : {amount}\n⛔ Address : <code>{hide_wallet}</code>\n⚠️ Status : <code>Failed</code>\n\n🔴 Bot: @{Bot.info().username}</b>"""

        bot.replyText(u, user_msg, parse_mode="html")
        bot.replyText(PaymentCh, channel_msg, parse_mode="html")
        
        


#======================================================================
# COMMAND: Refer Earn
#======================================================================
EMOJI_FAILED = "6129840374971112593"

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

# Page-wise join check, then open the referral screen
User.saveData("PIRO_GateTarget", "👫Referral1")
Bot.runCommand("/PIRO_JoinGate")


#======================================================================
# COMMAND: Withdraw
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_PIN = "6129434968713076807"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_WARN = "5447644880824181073"
EMOJI_STAR = "5469741319330996757"
EMOJI_PAISA = "6278337731063975777"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_HEART = "5388790256772331442"
EMOJI_DONE = "5021905410089550576"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_DOWN = "5470177992950946662"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"
# coded by @Jenish_Dobariya1

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(u, f'<b><tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji>Bot Is Currently Off</b>')
    raise ReturnCommand()

BotAdmins = Bot.getData("AllBotAdminss") or [str(u)]

joinSTAT = "JOIND"

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []

User.deleteData("PIRO_NJCL")
PIRO_NJCL = []

BINA = False
IND = 0

for i in AMCTGID:
    try:
        UC = bot.getChatMember(i, u)
        UC = UC.status
    except:
        UC = "error"

    ReqRec = Bot.getData(str(i) + "JoinRRof" + str(u)) or "N"

    if UC == "left" and ReqRec == "N":
        joinSTAT = "NOTJOIN"
        PIRO_NJCL.append(str(i))

    DC = Bot.getData(str(i) + "isDef") or "Y"
    JR = Bot.getData(str(i) + "JoinReq") or "Y"

    if UC == "error" and JR == "Y":
        if DC == "Y":
            continue
        for admin in BotAdmins:
            try:
                bot.replyText(admin, f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️</b>")
            except:
                pass
        BINA = True

    IND += 1

User.saveData("PIRO_NJCL", PIRO_NJCL)

if BINA:
    raise ReturnCommand()


# ✅ IF JOINED → SHOW WITHDRAW OPTIONS WITH LIVE ACCOUNT INFO
if joinSTAT == "JOIND":

    # Admin Settings read karein (Loop Status Toggle)
    WalletStatus = Bot.getData("WalletWithdrawMode") or Bot.getData("WalletWithdraw") or "ON"
    UpiStatus = Bot.getData("UpiWithdrawMode") or Bot.getData("UpiWithdraw") or "ON"

    # User ka live Data read karein
    wallet_data = Bot.getData("UserWallet" + str(u)) or "Not Linked"
    upi_data = Bot.getData("UserUPI" + str(u)) or "Not Linked"

    # Agar dono method disabled hain
    if str(WalletStatus).upper() == "OFF" and str(UpiStatus).upper() == "OFF":
        bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">⛔</tg-emoji><b>All Withdrawal Methods Are Currently Disabled</b>', parse_mode="HTML")
        raise ReturnCommand()

    # Dynamic Message tayar karna
    text = f'<b><tg-emoji emoji-id="{EMOJI_PAISA}">💸</tg-emoji> Choose Withdrawal Method From Below <tg-emoji emoji-id="{EMOJI_DOWN}">👇</tg-emoji>\n\n'
    buttons = []

    if str(WalletStatus).upper() == "ON":
        text += f"Your Current Wallet - <code>{wallet_data}</code>\n"
        buttons.append([
            InlineKeyboardButton("Wallet Withdraw", callback_data="/PIRO_withdraw")
        ])

    if str(UpiStatus).upper() == "ON":
        text += f"Your Current UPI - <code>{upi_data}</code>\n"
        buttons.append([
            InlineKeyboardButton("UPI Withdraw", callback_data="/PIRO_withdraw_upi")
        ])

    text += "</b>"

    bot.replyText(
        u,
        text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )
    raise ReturnCommand()

    
# ❌ NOT JOINED → SHOW JOIN UI
if not AMCL:
    bot.sendMessage("📌 No channels found!")
else:
    keyboard = []
    row = []
    IND = 0

    for LINK in AMCL:
        if str(AMCTGID[IND]) in PIRO_NJCL:
            row.append({"text": "Join", "url": LINK,"style":"primary"})
            if len(row) == 2:
                keyboard.append(row)
                row = []
        IND += 1

    if row:
        keyboard.append(row)

    keyboard.append([{"text": "🔒 Claim", "callback_data": "🟢 Joined","style":"success"}])

    usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

    PIRO = bot.sendMessage(f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""", reply_markup={"inline_keyboard": keyboard})

User.saveData("PIRO_ltmg", PIRO.message_id)

raise ReturnCommand()


#======================================================================
# COMMAND: link_upi
#======================================================================
# 
EMOJI_FAIL = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_STAR = "5469741319330996757"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
EMOJI_PARTY = "6224161941305169199"

EMOJI_USER = "6129840374971112593"
EMOJI_BULLET = "6129488844782836766"
EMOJI_SUCCESS = "6293907090591192968"
EMOJI_HEART = "5388790256772331442"
EMOJI_PIN = "6129434968713076807"
EMOJI_WARN = "5447644880824181073"

if message.chat.type != "private":
    raise ReturnCommand()

BotMode = Bot.getData("BotMode")
if BotMode == "OFF":
    bot.replyText(
        u,
        f'<b><tg-emoji emoji-id="{EMOJI_FAIL}">🙇‍♂️</tg-emoji> Bot Is Currently Off</b>'
    )
    raise ReturnCommand()

BotAdmins = Bot.getData("AllBotAdminss") or [str(u)]

joinSTAT = "JOIND"
Gatewaysett011 = Bot.getData("gatewaytype") or "Not Set"
gatewaynow = Bot.getData("gatewaynow") or "RJ WALLET"

if Gatewaysett011 == "Not Set":
    bot.replyText(
        u,
        f'<b><tg-emoji emoji-id="{EMOJI_FAIL}">⛔</tg-emoji> Gateway Not Set</b>'
    )
    raise ReturnCommand()

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []

User.deleteData("PIRO_NJCL")
PIRO_NJCL = []

BINA = False
IND = 0

for i in AMCTGID:
    try:
        UC = bot.getChatMember(i, u)
        UC = UC.status
    except:
        UC = "error"

    ReqRec = Bot.getData(str(i) + "JoinRRof" + str(u)) or "N"

    if UC == "left" and ReqRec == "N":
        joinSTAT = "NOTJOIN"
        PIRO_NJCL.append(str(i))

    DC = Bot.getData(str(i) + "isDef") or "Y"
    JR = Bot.getData(str(i) + "JoinReq") or "Y"

    if UC == "error" and JR == "Y":
        if DC == "Y":
            continue
        for admin in BotAdmins:
            try:
                bot.replyText(
                    admin,
                    f'<b><tg-emoji emoji-id="{EMOJI_USER}">👀</tg-emoji> Bot Is Not Admin In {AMCU[IND]}! <tg-emoji emoji-id="{EMOJI_WARN}">⚠️</tg-emoji></b>'
                )
            except:
                pass
        BINA = True

    IND += 1

User.saveData("PIRO_NJCL", PIRO_NJCL)

if BINA:
    raise ReturnCommand()

if joinSTAT != "JOIND":

    if not AMCL:
        bot.sendMessage(
            f'<tg-emoji emoji-id="{EMOJI_PIN}">📌</tg-emoji> No channels found!'
        )

    else:
        keyboard = []
        row = []
        IND = 0

        for LINK in AMCL:
            if str(AMCTGID[IND]) in PIRO_NJCL:
                row.append({
                    "text": "Join",
                    "url": LINK,
                    "style": "primary",
                    "icon_custom_emoji_id": EMOJI_BULLET
                })

                if len(row) == 2:
                    keyboard.append(row)
                    row = []

            IND += 1

        if row:
            keyboard.append(row)

        keyboard.append([
            {
                "text": "Claim",
                "callback_data": "🟢 Joined",
                "style": "primary",
                "icon_custom_emoji_id": EMOJI_SUCCESS
            }
        ])

        usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

        PIRO = bot.sendMessage(
            f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""",
            reply_markup={"inline_keyboard": keyboard}
        )

        if PIRO:
            User.saveData("PIRO_ltmg", PIRO.message_id)

    raise ReturnCommand()


keyboard = {
    "keyboard": [
        [
            {
                "text": "Cancel",
                "style": "primary",
                "icon_custom_emoji_id": EMOJI_FAIL
            }
        ]
    ],
    "resize_keyboard": True
}

bot.replyText(
    u,
    f'<b><tg-emoji emoji-id="{EMOJI_TIE}">💸</tg-emoji> Send Your UPI Where You Want Withdrawal</b>',
    parse_mode="HTML",
    reply_markup=keyboard
)

Bot.handleNextCommand("/setwallet1")


#======================================================================
# COMMAND: payzy_withdraw
#======================================================================
#


#======================================================================
# COMMAND: 🎁 Bonus1
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5203996991054432397"
EMOJI_MONEY = "6089081350080434641"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_STAR = "5469741319330996757"
EMOJI_SEARCH = "6195146353434169614"
EMOJI_DONE = "5021905410089550576"
EMOJI_CLOCK = "5316615057939897832"
EMOJI_CROWN = "4956420911310832630"
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]
BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShownB") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/claimvoucher"
    )

    if AdResult:
        User.saveData("TBC_AdShownB", "Y")
        raise ReturnCommand()
# Initialize your markup object correctly (case-sensitive)
# --- KEYBOARD ARRAY WITH PREMIUM EMOJIS ---
keyboard = [
    # Row 1: Daily Bonus
    [
        {
            "text": "Daily Bonus",
            "callback_data": "/Bonus",
            "icon_custom_emoji_id": EMOJI_CLOCK
        }
    ],
    # Row 2: Gift Code
    [
        {
            "text": "Gift Code",
            "callback_data": "/RedeemBotRC",
            "icon_custom_emoji_id": EMOJI_GIFT
        }
    ]
]

# --- SENDING MESSAGE ---
bot.replyText(
    u, 
    text=f'<b><tg-emoji emoji-id="{EMOJI_STAR}">✨</tg-emoji> Choose One:</b>', 
    reply_markup={"inline_keyboard": keyboard},
    parse_mode="HTML"
)


#======================================================================
# COMMAND: 👫Referral1
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GIFT = "5193085063998224234"
EMOJI_MONEY = "5316709465616031741"
EMOJI_TROPHY = "6156436440260549720"
EMOJI_TIE = "5375203677487248777"
EMOJI_GUN = "6129488844782836766"
EMOJI_DONE = "6294071751047385584"
EMOJI_TI = "5346123450358444391"

BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b> Bot Is Currently Off</b>')
    raise ReturnCommand()

# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShownR") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/claimvoucher"
    )

    if AdResult:
        User.saveData("TBC_AdShownR", "Y")
        raise ReturnCommand()
PER_REF=Bot.getData("PerRefer") or 0
per_refer = PER_REF
  
get_bot = Bot.info().username 
RL=f"https://t.me/{get_bot}?start={u}"


msg = f"""<tg-emoji emoji-id="{EMOJI_GIFT}">🎁</tg-emoji><b> Per Refer Rs.{per_refer} Upi Cash
  
<tg-emoji emoji-id="{EMOJI_TI}">💰</tg-emoji> Your Refferal Link: {RL}
    
Share With Your Friend's & Family And Earn Refer Bonus Easily <tg-emoji emoji-id="{EMOJI_MONEY}">🤑</tg-emoji></b>"""

# --- BUTTON LAYOUT WITH PREMIUM EMOJIS ---
keyboard = [
    [
        {
            "text": "My Invites", 
            "callback_data": "/MyInvitez",
            "icon_custom_emoji_id": EMOJI_DONE
        },
        {
            "text": "Leaderboard", 
            "callback_data": "/TopReferral",
            "icon_custom_emoji_id": EMOJI_TROPHY
        }
    ],
    [
        {
            "text": "Refer Tracker",
            "callback_data": "/ReferTracker",
            "icon_custom_emoji_id": EMOJI_TIE
        }
    ]
]

# --- SENDING MESSAGE ---
bot.replyText(
    u,
    msg,
    parse_mode="HTML",
    reply_markup={"inline_keyboard": keyboard},
    disable_web_page_preview=True
)


#======================================================================
# COMMAND: 💴 Account1
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_GUN = "6305222293601653735"
EMOJI_MONEY = "5375296873982604963"
EMOJI_FUND = "5021905410089550576"
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, f'<tg-emoji emoji-id="{EMOJI_FAILED}">🚫</tg-emoji><b>Bot Is Currently Off</b>')
    raise ReturnCommand()
# --- TBC Rewarded Ad: Show Only Once ---
AdShown = User.getData("TBC_AdShownA") or "N"

if AdShown != "Y":
    AdResult = libs.tbcads.reward_ad(
        "Watch a short ad to continue",
        then="/claimvoucher"
    )

    if AdResult:
        User.saveData("TBC_AdShownA", "Y")
        raise ReturnCommand()
balance = libs.Resources.anotherRes('Balance',user=u).value()

def Convert_To_TWO_DP(x):
    f = "{:.2f}".format(x)
    return f

msg = f"""<tg-emoji emoji-id="{EMOJI_MONEY}">🤑</tg-emoji><b> Balance: ₹{Convert_To_TWO_DP(balance)}
  
<tg-emoji emoji-id="{EMOJI_GUN}">💰</tg-emoji> Use 'Withdraw' button to withdraw your balance to Wallet</b>"""

bot.replyText(
    u,
    msg,
    parse_mode="HTML",
    reply_markup={
        "inline_keyboard": [
            [
                {"text": "Bot Fund", "callback_data": "/botfund",            "icon_custom_emoji_id": EMOJI_FUND
                }
            ]
        ]
    }
)


#======================================================================
# COMMAND: 📊 Statistics1
#======================================================================
# 19'4'25   00'11'10  v:1'0'0 [√]
# CODED BY: @Owner_Here 
# [ DM TO BUY ANY BOTS & CODES ]

BotMode=Bot.getData("BotMode")
if BotMode=="OFF":
    bot.replyText(u, "<b>🙇‍♂️ Bot Is Currently Off</b>")
    raise ReturnCommand()


Tusrs=Bot.getData('total_users') or 0

wit=libs.Resources.globalRes('BotWithdraws').value()

FulUsrs=Bot.getData("FulBotUsrs") or []
T_verifUsrs=Bot.getData('T_verifUsrs') or 0


markup = InlineKeyboardMarkup()

markup.row(
    InlineKeyboardButton(
        text="⬅️ Back",
        callback_data="/RawStats"
    )
)


bot.editMessageText(
    chat_id=u,
    message_id=call.message.message_id,
    text=f"""<b>👍Total Members In Bot: {len(FulUsrs)} Users

👍Total Verified Users In Bot : {T_verifUsrs} Users

👍Total Payouts In Bot : {wit} INR

📍 Powered By - @Jenish_Dobariya1

</b>""",
    parse_mode="html",
    reply_markup=markup
)


#======================================================================
# COMMAND: 🟢 Joined
#======================================================================
EMOJI_FAILED = "6129840374971112593"
EMOJI_PIN = "6129434968713076807"
EMOJI_SUCCESS = "6082398290773546707"
EMOJI_HEART = "5388790256772331442"
# --- JOINING CHECK (page-wise, always starts from page 1, FAST: cached for 1 minute only) ---

PIRO_ltmg = User.getData("PIRO_ltmg")
try:
    bot.deleteMessage(message.chat.id, PIRO_ltmg)
except:
    pass
PIRO_ltmg2 = User.getData("PIRO_ltmg2")
try:
    bot.deleteMessage(message.chat.id, PIRO_ltmg2)
except:
    pass

usr = f"""<a href="tg://user?id={str(u)}">{message.from_user.first_name}</a>"""

BotAdmins = Bot.getData("AllBotAdminss") or []
BOTID = int(Bot.info().token.split(":")[0])

AMC = Bot.getData("AllMainCh") or []
AMCU = Bot.getData("AllMainChUsernm") or []
AMCL = Bot.getData("AllMainChlink") or []
AMCTGID = Bot.getData("AllMainChTGID") or []
AMCO = Bot.getData("AllMainChOptional") or []
AMCP = Bot.getData("AllMainChPage") or []
for _pad in range(len(AMCTGID) - len(AMCP)):
    AMCP.append(1)
for _pad in range(len(AMCTGID) - len(AMC)):
    AMC.append("Channel")
for _pad in range(len(AMCTGID) - len(AMCU)):
    AMCU.append("Unknown")
for _pad in range(len(AMCTGID) - len(AMCL)):
    AMCL.append("https://t.me/" + str(AMCTGID[len(AMCL)]))

ALL_PAGES = sorted(set(AMCP)) if AMCTGID else []
CurPage = ALL_PAGES[0] if ALL_PAGES else 1

# ---- verified-channel cache (valid for the current MINUTE only) ----
_now = libs.DateAndTime.now("Asia/Kolkata")
Stamp = str(_now["date"]) + " " + str(_now["time"])[:5]
OKids = []
try:
    _c = User.getData("PIRO_OK")
    if _c and _c.get("s") == Stamp:
        OKids = list(_c.get("ids") or [])
except:
    OKids = []

joinSTAT = "JOIND"
PIRO_NJCL = []
FoundIdx = None
CacheDirty = False

for PageIdx in range(0, len(ALL_PAGES)):
    ThisPage = ALL_PAGES[PageIdx]
    NotJoinedThisPage = []

    IND = 0
    for i in AMCTGID:
        if AMCP[IND] != ThisPage:
            IND += 1
            continue

        sid = str(i)
        if sid in OKids:
            IND += 1
            continue

        UC = "error"
        ERR = ""
        try:
            UC = bot.getChatMember(i, u).status
        except Exception as e:
            UC = "error"
            ERR = str(e)[:150]

        if UC == "member" or UC == "administrator" or UC == "creator":
            OKids.append(sid)
            CacheDirty = True

        elif UC == "left" or UC == "kicked":
            ReqRec = Bot.getData(sid + "JoinRRof" + str(u)) or ""
            JR = Bot.getData(sid + "JoinReq") or "Y"
            if ReqRec != "Y" and JR == "Y" and (not AMCO or IND >= len(AMCO) or AMCO[IND] != "O"):
                NotJoinedThisPage.append(sid)

        elif UC == "error":
            BotIsAdm = False
            try:
                BS = bot.getChatMember(i, BOTID).status
                if BS == "administrator" or BS == "creator":
                    BotIsAdm = True
            except:
                BotIsAdm = False

            if not BotIsAdm:
                if Bot.getData("PIRO_NAsent" + sid) != "Y":
                    Bot.saveData("PIRO_NAsent" + sid, "Y")
                    for admin in BotAdmins:
                        try:
                            bot.replyText(admin, f"<b>👀 Bot Is Not Admin In {AMCU[IND]}! ⚠️\n\n✨ Only admins see this reminder (sent once per channel). 😊</b>")
                        except:
                            pass
            else:
                Bot.deleteData("PIRO_NAsent" + sid)
                if Bot.getData("PIRO_ERRsent" + sid) != "Y":
                    Bot.saveData("PIRO_ERRsent" + sid, "Y")
                    for admin in BotAdmins:
                        try:
                            bot.replyText(admin, f"<b>ℹ️ Bot IS admin in {AMCU[IND]}, but a member check failed:</b>\n<code>{ERR}</code>\n<i>(sent once per channel, only admins see this)</i>")
                        except:
                            pass

        IND += 1

    if NotJoinedThisPage:
        joinSTAT = "NOTJOIN"
        PIRO_NJCL = NotJoinedThisPage
        FoundIdx = PageIdx
        break

if CacheDirty:
    User.saveData("PIRO_OK", {"s": Stamp, "ids": OKids})

if FoundIdx is not None:
    CurPage = ALL_PAGES[FoundIdx]
elif ALL_PAGES:
    CurPage = ALL_PAGES[-1]

User.saveData("PIRO_CurPage", CurPage)

if joinSTAT == "JOIND":
    Bot.runCommand("/PIRO_MainMenu")
    raise ReturnCommand()

User.saveData("PIRO_NJCL", PIRO_NJCL)

JoinBtnText = Bot.getData("PIRO_JoinBtnText") or "Join"
ClaimBtnText = Bot.getData("PIRO_ClaimBtnText") or "🔒 Claim"
JoinIcon = Bot.getData("PIRO_JoinBtnEmojiId")
ClaimIcon = Bot.getData("PIRO_ClaimBtnEmojiId")

keyboard = []
row = []
IND = 0
for i in AMCTGID:
    if str(i) in PIRO_NJCL:
        btn = {"text": JoinBtnText, "url": AMCL[IND], "style": "primary"}
        if JoinIcon:
            btn["icon_custom_emoji_id"] = JoinIcon
        row.append(btn)
        if len(row) == 2:
            keyboard.append(row)
            row = []
    IND += 1
if row:
    keyboard.append(row)

SocialLinks = Bot.getData("AllSocialLinks") or []
if SocialLinks:
    row = []
    for s in SocialLinks:
        row.append({"text": f"{s['name']}", "url": s['url'], "style": "primary"})
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

cbtn = {"text": ClaimBtnText, "callback_data": "🟢 Joined", "style": "success"}
if ClaimIcon:
    cbtn["icon_custom_emoji_id"] = ClaimIcon
keyboard.append([cbtn])

JoinMsgChatId = Bot.getData("PIRO_JoinMsgChatId")
JoinMsgId = Bot.getData("PIRO_JoinMsgId")

SentOk = False
if JoinMsgChatId and JoinMsgId:
    try:
        Sent = bot.copyMessage(chat_id=u, from_chat_id=JoinMsgChatId, message_id=JoinMsgId, reply_markup={"inline_keyboard": keyboard})
        try:
            Mid = Sent.message_id
        except:
            Mid = Sent["message_id"]
        User.saveData("PIRO_ltmg", Mid)
        SentOk = True
    except:
        SentOk = False

if not SentOk:
    msg = bot.sendMessage(
    f"""<tg-emoji emoji-id="{EMOJI_HEART}">👋🏻</tg-emoji><b>Hey There {usr} Welcome To Wallet Bot !

<tg-emoji emoji-id="{EMOJI_PIN}">🛑</tg-emoji> Must Join All Channels To Use Our Bot

<tg-emoji emoji-id="{EMOJI_SUCCESS}">🚫</tg-emoji> After Joining Click Claim</b>""",
        reply_markup={"inline_keyboard": keyboard},
        disable_web_page_preview=True
    )

    User.saveData("PIRO_ltmg", msg["message_id"])

Ex1 = Bot.getData("PIRO_JoinMsg2ChatId")
Ex2 = Bot.getData("PIRO_JoinMsg2Id")
if Ex1 and Ex2:
    try:
        S2 = bot.copyMessage(chat_id=u, from_chat_id=Ex1, message_id=Ex2)
        try:
            M2 = S2.message_id
        except:
            M2 = S2["message_id"]
        User.saveData("PIRO_ltmg2", M2)
    except:
        pass

