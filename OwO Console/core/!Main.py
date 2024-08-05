import json, math, random, os, time, hashlib, threading, multiprocessing, datetime, base64, json, math, random, os, time, hashlib, threading, datetime
from file import phrases, actvar, gamblevar
try:
    import requests, psutil, pytz
    from blessed import Terminal
    from notifypy import Notify
except ModuleNotFoundError  :
    print("Please Run: ! Create venv and Install lib.bat")

    time.sleep(2)
    exit()

# Get the current working directory
current_dir = os.getcwd()

# Join the current directory with the filename
file_config = os.path.join(current_dir, 'data\\setting_config.json')
file_cache = os.path.join(current_dir, 'data\\cache.json')
file_update = os.path.join(current_dir, 'core\\!Update.py')
#Call cfg.json file 
with open(file_config, 'r', encoding='utf-8') as a:
    cfgs = json.load(a)
    a.close()
def token_decode(token):
    token_id = token.split(".")[0]
    padding_length = 4 - (len(token_id) % 4)
    if padding_length < 4:
        token_id += "=" * padding_length
    userid = base64.b64decode(token_id).decode("utf-8")
    return userid

def boolean_conv(str_value):
  if str_value == "main" or "extra":
      return str_value
  else:
    return str_value.lower() == "true"

def P_str_int_conv(str_value):
  if isinstance(str_value, str):
    try:
      converted_value = int(float(str_value))
      if converted_value < 0:
        return "0"
      else:
        return str(converted_value)
    except ValueError:
      return "0"
  elif isinstance(str_value, bool):
    return "0"
  else:
    return 0
red = Terminal().red
green = Terminal().green
blue = Terminal().blue
yellow = Terminal().yellow
magenta = Terminal().magenta

"""▄▀█ █▀▀ █▀▀ █▀▀ █▀ █▀   ▀█▀ █░█ █▀▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
   █▀█ █▄▄ █▄▄ ██▄ ▄█ ▄█   ░█░ █▀█ ██▄   ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█"""
print("Checking Setting")
try:
    setting               = cfgs["settings"]
    prefix                = str(setting['owo_prefix'])
    bot_prefix            = str(setting['control_prefix'])
    slash_command         = boolean_conv(setting['slash_command'])
    sayowo                = boolean_conv(setting['sayowo'])
    pray                  = boolean_conv(setting['pray'])
    curse                 = boolean_conv(setting['curse'])
    hunt                  = boolean_conv(setting['hunt'])
    battle                = boolean_conv(setting['battle'])
    autoquest             = boolean_conv(setting['autoquest'])
    extratokencheck       = boolean_conv(setting['extratoken'])
    randommess            = boolean_conv(setting['randommess'])
    banbypass             = boolean_conv(setting['banbypass'])
    #========================================================================================================================
    inventory             = setting['inventory']
    inventorycheck        = boolean_conv(inventory['inventorycheck'])
    gemcheck              = boolean_conv(inventory['gemcheck'])
    lootboxcheck          = boolean_conv(inventory['lootboxcheck'])
    fabledlootboxcheck    = boolean_conv(inventory['fabledlootboxcheck'])
    cratecheck            = boolean_conv(inventory['cratecheck'])
    #========================================================================================================================
    animals               = setting['animals']
    ani_enable            = boolean_conv(animals['enable'])
    ani_type              = str(animals['type'])
    animaltype            = animals['animaltype']
    common                = boolean_conv(animaltype['common'])
    uncommon              = boolean_conv(animaltype['uncommon'])
    rare                  = boolean_conv(animaltype['rare'])
    epic                  = boolean_conv(animaltype['epic'])
    mythical              = boolean_conv(animaltype['mythical'])
    patreon               = boolean_conv(animaltype['patreon'])
    cpatreon              = boolean_conv(animaltype['cpatreon'])
    legendary             = boolean_conv(animaltype['legendary'])
    gem                   = boolean_conv(animaltype['gem'])
    bot                   = boolean_conv(animaltype['bot'])
    distorted             = boolean_conv(animaltype['distorted'])
    fabled                = boolean_conv(animaltype['fabled'])
    special               = boolean_conv(animaltype['special'])
    hidden                = boolean_conv(animaltype['hidden'])
    #========================================================================================================================
    upgradeautohunt       = setting['upgradeautohunt']
    upg_enable            = boolean_conv(upgradeautohunt['enable'])
    upg_type              = str(upgradeautohunt['upgtype'])
    #========================================================================================================================
    gamble                = setting['gamble']

    coinflip              = gamble['coinflip']
    coinflip_enable       = boolean_conv(coinflip['enable'])
    coinflip_amount       = P_str_int_conv(coinflip['amount'])

    slots                 = gamble['slots']
    slots_enable          = boolean_conv(slots['enable'])
    slots_amount          = P_str_int_conv(slots['amount'])
    #========================================================================================================================
    main                  = cfgs['main']
    main_token            = str(main['token'])
    main_id               = str(token_decode(main_token))
    main_serverid         = str(main['serverid'])
    main_channelid        = str(main['channelid'])
    main_questchannelid   = str(main['questchannelid'])
    main_dmchannelid      = str(main['owo_dmschannelid'])

    extra                 = cfgs['extra']
    extra_token           = str(extra['token'])
    extra_id              = str(token_decode(extra_token))
    extra_serverid        = str(extra['serverid'])
    extra_channelid       = str(extra['channelid'])
    extra_questchannelid  = str(extra['questchannelid'])
    extra_dmchannelid     = str(extra['owo_dmschannelid'])

    #========================================================================================================================
except (IndexError, KeyError) as e:
    print("Check your setting_config.json there some missing")
    time.sleep(1)
    os._exit(0)
time.sleep(1.5)
notification = Notify()
process = psutil.Process()
quest = True
etoken = False
pray_curse = True
battle_hunt = True
active_bot = True
capcha_flag = False
task_bot_active = True
captcha_notification = False
if (extra_token == main_token):
    extratokencheck = False

version = "v1-0.2.e04c023b"

"""███╗░░░███╗░█████╗░██╗███╗░░██╗  ██████╗░███████╗███████╗
   ████╗░████║██╔══██╗██║████╗░██║  ██╔══██╗██╔════╝██╔════╝
   ██╔████╔██║███████║██║██╔██╗██║  ██║░░██║█████╗░░█████╗░░
   ██║╚██╔╝██║██╔══██║██║██║╚████║  ██║░░██║██╔══╝░░██╔══╝░░
   ██║░╚═╝░██║██║░░██║██║██║░╚███║  ██████╔╝███████╗██║░░░░░
   ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░░░░"""
def load_cache():
    try:
        with open(file_cache, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError , FileNotFoundError):
        data = {}
    return data
#========================================================================================================================
def save_cache(data):
    with open(file_cache, "w") as f:
        json.dump(data, f, indent=4)
#========================================================================================================================
def add_user(user_ids):
    caches = load_cache()
    if user_ids not in caches:
        caches[user_ids] = {
            "daily": "ready",
            "quest": "ready",
            "day_daily": "2000-01-01",
            "day_quest": "2000-01-01",
            "id_captcha_dm": "0000000000000000000000",
            "id_captcha": {
                "id_1": "0000000000000000000000",
                "id_2": "0000000000000000000000",
                "id_3": "0000000000000000000000",
                "id_4": "0000000000000000000000",
                "id_5": "0000000000000000000000",
                "id_6": "0000000000000000000000",
                "id_7": "0000000000000000000000",
                "id_8": "0000000000000000000000",
                "id_9": "0000000000000000000000",
                "id_10": "0000000000000000000000"
            },
            "id_activate": {
                "id_1": "0000000000000000000000",
                "id_2": "0000000000000000000000",
                "id_3": "0000000000000000000000",
                "id_4": "0000000000000000000000",
                "id_5": "0000000000000000000000",
                "id_6": "0000000000000000000000",
                "id_7": "0000000000000000000000",
                "id_8": "0000000000000000000000",
                "id_9": "0000000000000000000000",
                "id_10": "0000000000000000000000"
            },
            "id_quest_battle":{
                "id_1": "0000000000000000000000",
                "id_2": "0000000000000000000000",
                "id_3": "0000000000000000000000",
                "id_4": "0000000000000000000000",
                "id_5": "0000000000000000000000",
                "id_6": "0000000000000000000000",
                "id_7": "0000000000000000000000",
                "id_8": "0000000000000000000000",
                "id_9": "0000000000000000000000",
                "id_10": "0000000000000000000000"
            }
        }
    save_cache(caches)
#========================================================================================================================
def install_update():
    update = requests.get(
        "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Update.py"
    )
    with open(file_update, "wb") as fu:
        fu.write(update.content)
        fu.close()

#========================================================================================================================
def checkversion():
    response = requests.get('https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/data/version')
    versions = response.text.strip()
    if versions != version:
        print("New version detected")
        time.sleep(3)
        os._exit(0)
#========================================================================================================================
def notification_def(tokentype):
    notification = Notify()
    noti_count = 11
    while noti_count > -1:
        if captcha_notification == True:
            noti_count = noti_count - 1
            if noti_count > 0:
                noti_count_str = str(noti_count)
                notification.title = f"[{tokentype}] Captcha Detected!"
                notification.message = f"SOLVE CAPTCHA AND RESTART BOT\nyou only have {noti_count_str}min left"
                notification.icon = "data/owo.ico"
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f"[{tokentype}]") +
                    red(f" Time left {noti_count} Min! ⚠️")
                )
                notification.send()
            else:
                noti_count_str = str(noti_count)
                notification.title = f"[{tokentype}] Captcha Detected!"
                notification.message = f"You are Banned by OwO"
                notification.icon = "data/owo.ico"
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f"[{tokentype}]") +
                    red(f" Time left {noti_count} Min! ⚠️")
                )
                notification.send()
                time.sleep(3)
                os._exit(0)
        else:
            break
        time.sleep(60)
#========================================================================================================================
def rantime():
    rdt = random.randint(1, 5) + round(random.uniform(0, 1), 3)
    return rdt
#========================================================================================================================
def rantime_2():
    rdt = random.randint(5, 30) + round(random.uniform(0, 1), 3)
    return rdt
#========================================================================================================================
def nonce():
    rannonce = 1098393848631590 + math.floor(round(random.uniform(0, 1), 3) * 9999)
    return rannonce
#========================================================================================================================
def autoseed(token):
    seed = hashlib.sha256(f"seedaccess-entropyverror-apiv10.{token}".encode()).digest()
    return seed
#========================================================================================================================
def generate_random_128bit_hex():
  "Tạo một chuỗi hexa ngẫu nhiên 128-bit."
  random_bytes = os.urandom(16)  # 16 byte = 128 bit
  return random_bytes.hex()
#========================================================================================================================
def bot_owo(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": "owo",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" OwO ✅ ")    
        )
#========================================================================================================================
def bot_hunt(token, timehunt, tokentype, channelid, session_id, serverid):
    if slash_command:
        requests.post(
            f"https://discord.com/api/v9/interactions",
            headers={"authorization": token},
            json={
                "type": 2,
                "application_id": "408785106942164992",
                "guild_id": serverid,
                "channel_id": channelid,
                "session_id": session_id,
                "data": {
                    "version": "872969405326323743",
                    "id": "789914703878946847",
                    "name": "hunt",
                    "type": 1,
                    "options": [],
                    "application_command": {
                        "id": "789914703878946847",
                        "type": 1,
                        "application_id": "408785106942164992",
                        "version": "872969405326323743",
                        "name": "hunt",
                        "description": "Hunt for some animals!",
                        "integration_types": [
                            0
                        ],
                        "global_popularity_rank": 1,
                        "options": [],
                        "description_localized": "Hunt for some animals!",
                        "name_localized": "hunt"
                    },
                    "attachments": []
                },
                "nonce": nonce(),
                "analytics_location": "slash_ui"
            }
        )
        pass
    else:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "h",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" Hunt ✅ (" + str(timehunt) + " ms)")    
        )
#========================================================================================================================
def bot_battle(token, timebattle, tokentype, channelid, session_id, serverid):
    if slash_command:
        requests.post(
            f"https://discord.com/api/v9/interactions",
            headers={"authorization": token},
            json = {
                "type": 2,
                "application_id": "408785106942164992",
                "guild_id": serverid,
                "channel_id": channelid,
                "session_id": session_id,
                "data": {
                    "version": "953950078974963724",
                    "id": "953950078974963723",
                    "name": "battle",
                    "type": 1,
                    "options": [],
                    "application_command": {
                        "id": "953950078974963723",
                        "type": 1,
                        "application_id": "408785106942164992",
                        "version": "953950078974963724",
                        "name": "battle",
                        "description": "Fight with your team of animals!",
                        "options": [
                            {
                                "type": 6,
                                "name": "user",
                                "description": "Fight a friend.",
                                "description_localized": "Fight a friend.",
                                "name_localized": "user"
                            }
                        ],
                        "integration_types": [
                            0
                        ],
                        "global_popularity_rank": 2,
                        "description_localized": "Fight with your team of animals!",
                        "name_localized": "battle"
                    },
                    "attachments": []
                },
                "nonce": nonce(),
                "analytics_location": "slash_ui"
        },
    )
    else:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "b",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +     
        blue(" Battle ✅ (" + str(timebattle) + " ms)")    
        )   
#========================================================================================================================
def get_ran_mess():
    grm = random.randint(0, (len(phrases)-1))
    return phrases[grm]
#========================================================================================================================
def get_ran_act():
    gra = random.randint(0, (len(actvar)-1))
    return actvar[gra]
#========================================================================================================================
def get_ran_gamble():
    gra = random.randint(0, (len(gamblevar)-1))
    return gamblevar[gra]
#========================================================================================================================
def ran_message(token, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": get_ran_mess(),        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
#========================================================================================================================
def bot_animals(token, tokentype, channelid, ani_type):
    animalcheck = False
    animaltypes = ""
    ranks = [
        "common",
        "uncommon",
        "rare",
        "epic",
        "mythical",
        "patreon",
        "cpatreon",
        "legendary",
        "gem",
        "bot",
        "distorted",
        "fabled",
        "special",
        "hidden",
    ]
    rank = ["c","u","r","e","m","p","cp","l","g","b","d","f","s","h",
    ]
    for e, a in zip(ranks,rank):
        if animaltype["all"]:
            animaltypes = "all"
            break
        else:
            if animaltype[e]:
                animaltypes += f"{a} "

    if ani_type == "sacrifice" or ani_type == "sell" or ani_type == "sac":
        animalcheck = True

    if animalcheck:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": f"owo {ani_type} {animaltypes}",
                "nonce": nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        print( 
            red(f"{time.strftime('%H:%M:%S')} ") + 
            magenta(f"[{tokentype}] ") +
            blue(f"Animals ✅ / Type: {ani_type}"))
    else:
        print(
            red(f"{time.strftime('%H:%M:%S')} ") + 
            magenta(f"[{tokentype}] ") + 
            blue(f"[{tokentype}] Animals ❌ / Error: Incorrect Type"))
#========================================================================================================================
def bot_pray(token, tokentype, channelid, pray):
    global pray_curse
    if pray_curse:
        ct = None
        if pray:
            if (tokentype == "Extra Token") :
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif pray == "main":
            if (tokentype == "Extra Token"):
                ct = prefix + "pray <@" + main_id + ">"
                bt = "Pray to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif pray == "extra":
            if (tokentype == "Extra Token"):
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "pray <@" + extra_id + ">"
                bt = "Pray to extra"
        else:
            ct = ""
            bt = ""
                
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}] ") +
            yellow( bt +"✅")
        )
#========================================================================================================================
def bot_curse(token, tokentype, channelid, curse):
    global pray_curse
    if pray_curse:
        ct = None
        if curse:
            if (tokentype == "Extra Token") :
                ct = prefix + "curse"
                bt = "Curse"
            else:
                ct = prefix + "curse"
                bt = "Curse"
        elif curse == "main":
            if (tokentype == "Extra Token"):
                ct = prefix + "curse <@" + main_id + ">"
                bt = "Curse to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif curse == "extra":
            if (tokentype == "Extra Token"):
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "curse <@" + extra_id + ">"
                bt = "Curse to extra"
        else:
            ct = " "
            bt = " "
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}] ") +
            yellow( bt + "✅")
        )
#========================================================================================================================
def cookie(token, tokentype, channelid):
    if (tokentype == "Extra Token"):
        ct = prefix + "cookie <@"+ main_id + ">"
    else :
        if extratokencheck:
            ct = prefix + "cookie <@"+ extra_id +">"
        else:
            ct = prefix + "cookie <@408785106942164992>"
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": ct,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Cookie ✅")
    )
#========================================================================================================================
def daily(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "daily",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Daily ✅")
    )
#========================================================================================================================
def bot_coinflip(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "cf " + coinflip_amount,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Gamble / CoinFlip ✅ / Amount: " +
                coinflip_amount)
    )
#========================================================================================================================
def bot_slots(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "s " + slots_amount,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Gamble / slots ✅ / Amount: " +
                slots_amount)
    )
#========================================================================================================================
def upgradeall(token, tokentype, channelid):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "upg " + upg_type + " all",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}]") +
        yellow(" Upgrade AutoHunt ✅ ")
    )
"""▒█▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 ▒█░░░ ░▀░ █▀▀ ▀▀█▀▀ 
   ▒█░▒█ █░░█ █▀▀ ▀▀█ ░░█░░ 　 █▄▄█ █░░█ █░░█ 　 ▒█░░░ ▀█▀ ▀▀█ ░░█░░ 
   ░▀▀█▄ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░"""
def dailycount(userid):
    with open(file_cache, 'r', encoding='utf-8') as c:
        data = json.load(c)
        c.close()
    base_time = datetime.time(7, 0, 0)
    day_base = datetime.datetime.strptime(data[userid]["day_daily"], "%Y-%m-%d").date()
    base_datetime = datetime.datetime.combine(day_base, base_time)
    base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
    now_utc = datetime.datetime.now(pytz.utc)
    if ((base_datetime_utc < now_utc) and (data[userid]["daily"] == "done")):
        data[userid]["daily"] = "ready"
        with open(file_cache, "w", encoding='utf-8') as s:
            json.dump(data, s, indent=4)
            s.close()
            dailycheckers = "ready"
    elif data[userid]["daily"] == "ready":
        dailycheckers = "ready"
    else:
        dailycheckers = "done"
    return dailycheckers
def checklist(token, tokentype, channelid, userid):
    if dailycount(userid) == "ready":
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": f"{prefix}cl",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")+
            magenta(f"[{tokentype}] ") +
            blue(f"Sending Checklist📜...")
        )
        time.sleep(0.5)
        while True:
            response = requests.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1",
                headers={"authorization": token},
            )
            try:
                body = response.json()
                author = body[0]["author"]
                id = author["id"]
                if ((id == "408785106942164992") and
                    ("Checklist" in body[0]["embeds"][0]["author"]["name"])):
                    embeds = body[0]["embeds"]
                    cont = embeds[0]["description"]
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")+
                        magenta(f"[{tokentype}] ")+
                        blue(f"Getting Checklist🔎...")
                        )
                    print(green(f"{cont}"))
                    if "☑️ 🎉" in cont:
                        with open(file_cache, "r", encoding='utf-8') as d:
                            data = json.load(d)
                            d.close()
                        now_utc = datetime.datetime.now(pytz.utc)
                        data[userid]["day_daily"] = now_utc.strftime("%Y-%m-%d")
                        data[userid]["daily"] = "done"
                        with open(file_cache, "w", encoding='utf-8') as e:
                            json.dump(data, e, indent=4)
                            e.close()

                        return "checklist completed"
                    elif "⬛ 🎁" in cont:
                        daily(token, tokentype, channelid)
                    elif "⬛ 🍪" in cont:
                        cookie(token, tokentype, channelid)
                    elif "⬛ 📝" in cont:
                        print(
                            magenta((f"[{tokentype}] ") +
                            blue(f"YOUR DAILY VOTE IS AVAILABLE!"))
                        )
                    break
                else:
                    continue
            except (KeyError, json.JSONDecodeError) as e:
                if isinstance(e, IndexError) and str(e) == "list index out of range":
                    print(red("Unable to get Checklist❗"))
                    return
                else:
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                        magenta(f"[{tokentype}] ") +
                        red("Unable to get Checklist❗")
                    )
            time.sleep(0.05)
#========================================================================================================================
def checkinv(token, channelid, tokentype):
    if gemcheck:
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token}
        )
        body = response.json()
        cont = body[0]['content']
        if "You found:" in cont or "and caught a" in cont:
            collection = ["alulu"]
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}]") +
                blue(" inventory checking 🔍")
            )
            if "gem1" not in cont:
                collection.append("huntgem")
            if "gem3" not in cont:
                collection.append("empgem")
            if "gem4" not in cont:
                collection.append("luckgem")
            if "gem1" in cont and "gem3" in cont and "gem4" in cont:
                getinv(token, channelid, tokentype, "nogem", ["nocollection"])
            else:
                getinv(token, channelid, tokentype, "gemvar", collection)
    else:
        print(
            f"{datetime.datetime.now().strftime('%H:%M:%S')} [{tokentype}] inventory checking 🔍"
        )
        getinv(token, channelid, tokentype, "nogem", ["nocollection"])
#========================================================================================================================
def getinv(token, channelid, tokentype, gemc, collectc):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "inv",
            "tts": False,
            "flags": 0,
                },
    )
    time.sleep(3)
    response = requests.get(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token}
    )
    body = response.json()
    cont = body[0]['content']
    if gemc == "gemvar":
        empgem = ""
        empgemstatus = False
        luckgem = ""
        luckgemstatus = False
        huntgem = ""
        huntgemstatus = False
        specialgem = ""
        specialgemstatus = False
        gem = ""
        gemusebro = False

        if "huntgem" in collectc:
            if "`057`" in cont:
                huntgem = "57"
                huntgemstatus = True
            elif "`056`" in cont:
                huntgem = "56"
                huntgemstatus = True
            elif "`055`" in cont:
                huntgem = "55"
                huntgemstatus = True
            elif "`054`" in cont:
                huntgem = "54"
                huntgemstatus = True
            elif "`053`" in cont:
                huntgem = "53"
                huntgemstatus = True
            elif "`052`" in cont:
                huntgem = "52"
                huntgemstatus = True
            elif "`051`" in cont:
                huntgem = "51"
                huntgemstatus = True

        if "empgem" in collectc:
            if "`071`" in cont:
                empgem = "71"
                empgemstatus = True
            elif "`070`" in cont:
                empgem = "70"
                empgemstatus = True
            elif "`069`" in cont:
                empgem = "69"
                empgemstatus = True
            elif "`068`" in cont:
                empgem = "68"
                empgemstatus = True
            elif "`067`" in cont:
                empgem = "67"
                empgemstatus = True
            elif "`066`" in cont:
                empgem = "66"
                empgemstatus = True
            elif "`065`" in cont:
                empgem = "65"
                empgemstatus = True

        if "luckgem" in collectc:
            if "`078`" in cont:
                luckgem = "78"
                luckgemstatus = True
            elif "`077`" in cont:
                luckgem = "77"
                luckgemstatus = True
            elif "`076`" in cont:
                luckgem = "76"
                luckgemstatus = True
            elif "`075`" in cont:
                luckgem = "75"
                luckgemstatus = True
            elif "`074`" in cont:
                luckgem = "74"
                luckgemstatus = True
            elif "`073`" in cont:
                luckgem = "73"
                luckgemstatus = True
            elif "`072`" in cont:
                luckgem = "72"
                luckgemstatus = True

        if "specialgem" in collectc:
            if "`085`" in cont:
                specialgem = "85"
                specialgemstatus = True
            elif "`084`" in cont:
                specialgem = "84"
                specialgemstatus = True
            elif "`083`" in cont:
                specialgem = "83"
                specialgemstatus = True
            elif "`082`" in cont:
                specialgem = "82"
                specialgemstatus = True
            elif "`081`" in cont:
                specialgem = "81"
                specialgemstatus = True
            elif "`080`" in cont:
                specialgem = "80"
                specialgemstatus = True
            elif "`079`" in cont:
                specialgem = "79"
                specialgemstatus = True

        if huntgemstatus:
            gem += f" {huntgem}"
            gemusebro = True
        if empgemstatus:
            gem += f" {empgem}"
            gemusebro = True
        if luckgemstatus:
            gem += f" {luckgem}"
            gemusebro = True
        if specialgemstatus:
            gem += f" {specialgem}"
            gemusebro = True
        if gemusebro:
            gemuse(token, gem, channelid, tokentype)

    if lootboxcheck:
        if "`050`" in cont:
            time.sleep(2)
            boxuse(token, "lb all", channelid, tokentype)

    if fabledlootboxcheck:
        if "`049`" in cont:
            time.sleep(2)
            boxuse(token, "lootbox fabled all", channelid, tokentype)

    if cratecheck:
        if "`100`" in cont:
            time.sleep(2)
            boxuse(token, "wc all", channelid, tokentype)
#========================================================================================================================
def boxuse(token, box, channelid, tokentype):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + box,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta(f"[{tokentype}] ") +     
        yellow(box + " ✅")    
    )
#========================================================================================================================
def gemuse(token, gem, channelid, tokentype):
    requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": prefix + "use " + gem,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
        magenta(f" [{tokentype}]") + 
        yellow(" Gem ✅")
            )
#========================================================================================================================
def questprayme(tokenrd, useridst, channelid, pro1, pro2):
    np = (pro2 - pro1) + 1
    global quest, active_bot, pray_curse
    pray_curse = False
    for np in range (np, 0, -1):
        if active_bot:
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"pray <@{useridst}>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            t = rantime_2()
            time.sleep(300 + t)
            if np == 1:
                quest = True
                pray_curse = True
        else:
            break
#========================================================================================================================
def questcurseme(tokenrd, useridst, channelid, pro1, pro2):
    np = (pro2 - pro1) + 1
    global quest, active_bot, curse, pray_curse
    pray_curse = False
    for np in range (np, 0, -1):
        if active_bot:
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"curse <@{useridst}>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            t = rantime_2()
            time.sleep(300 + t)
            if np == 1:
                pray_curse = True
                quest = True
        else:
            break
#========================================================================================================================
def questbattlefriend(tokenst, tokenrd, useridst, channelid, pro1, pro2, session_id, session_id2, serverid):
    np = (pro2 - pro1) + 1
    def read_id(id_to_check):
        with open(file_cache, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Truy cập id_captcha bên trong dictionary cache
        id_captcha = data[useridst]["id_captcha"]

        for value in id_captcha.values():
            if value == id_to_check:
                return False
        return True
    def add_id_to_quest_battle(new_id):
        with open(file_cache, 'r') as read_data:
            data = json.load(read_data)
            read_data.close
        if useridst in data:
            id_quest_battle = data[useridst].setdefault("id_quest_battle", {})
            id_list = list(id_quest_battle.values())
            id_list.insert(0, new_id)
            id_list = id_list[:10]
            data[useridst]["id_quest_battle"] = {f"id_{i+1}": v for i, v in enumerate(id_list)}
            with open(file_cache, 'w') as write_data:
                json.dump(data, write_data, indent=4)
                write_data.close
    def get_id(token, channelid, userid):
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=10",
            headers={"authorization": token},
            ) 
        body = response.json()
        n = 0
        for bodycount in body:
            n += 1
            if (bodycount["author"]["id"] == "408785106942164992"):
                print(n)
                if((read_id(bodycount["id"])) and 
                    (bodycount["content"] == f"<@{userid}>") and 
                    (bodycount["embeds"][0]["description"] =="`owo ab` to accept the battle!\n`owo db` to decline the battle!")):
                    bodycount["id"]
                    add_id_to_quest_battle(bodycount["id"])
                    return bodycount["id"]
            else:
                continue
            return False
    for np in range (np, 0, -1):
        global quest, active_bot, battle_hunt
        battle_hunt = False
        if active_bot:
            if slash_command:
                requests.post(
                    f"https://discord.com/api/v9/interactions",
                    headers={"authorization": tokenrd},
                    json={
                        "type": 2,
                        "application_id": "408785106942164992",
                        "guild_id": serverid,
                        "channel_id": channelid,
                        "session_id": session_id,
                        "data": {
                            "version": "953950078974963724",
                            "id": "953950078974963723",
                            "name": "battle",
                            "type": 1,
                            "options": [
                                {
                                    "type": 6,
                                    "name": "user",
                                    "value": useridst
                                }
                            ],
                            "application_command": {
                                "id": "953950078974963723",
                                "type": 1,
                                "application_id": "408785106942164992",
                                "version": "953950078974963724",
                                "name": "battle",
                                "description": "Fight with your team of animals!",
                                "options": [
                                    {
                                        "type": 6,
                                        "name": "user",
                                        "description": "Fight a friend.",
                                        "description_localized": "Fight a friend.",
                                        "name_localized": "user"
                                    }
                                ],
                                "integration_types": [
                                    0
                                ],
                                "global_popularity_rank": 2,
                                "description_localized": "Fight with your team of animals!",
                                "name_localized": "battle"
                            },
                            "attachments": []
                        },
                        "nonce": nonce(),
                        "analytics_location": "slash_ui"
                    },
                )
                time.sleep(3)
                requests.post(
                    f"https://discord.com/api/v9/interactions",
                    headers={"authorization": tokenst},
                    json = {
                        "type": 3,
                        "nonce": nonce(),
                        "guild_id": serverid,
                        "channel_id": channelid,
                        "message_flags": 0,
                        "message_id": get_id(tokenst, channelid, useridst),
                        "application_id": "408785106942164992",
                        "session_id": session_id2,
                        "data": {
                            "component_type": 2,
                            "custom_id": "battle_accept"
                        }
                    },
                )
                t = rantime()
                time.sleep(15 + t)
                if np == 1:
                    time.sleep(5)
                    battle_hunt = True
                    quest = True
            else:
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenrd},
                json={
                    "content": prefix + f"b <@{useridst}>",        
                    'nonce': nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                time.sleep(3)
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenst},
                json={
                    "content": prefix + "ab",        
                    'nonce': nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = rantime()
                time.sleep(15 + t)
                if np == 1:
                    time.sleep(5)
                    battle_hunt = True
                    quest = True
        else:
            break
#========================================================================================================================
def questuseactionreceive(tokenrd, useridst, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    for np in range (np, 0, -1):
        if active_bot:
            
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenrd},
            json={
                "content": prefix + f"{get_ran_act()} <@"+ useridst +">",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            t = rantime()
            time.sleep(5 + t)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questuseactiongive(token, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    for np in range (np, 0, -1):
        if active_bot:
            
            requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + f"{get_ran_act()} <@408785106942164992>",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                    },
                )
            t = rantime()
            time.sleep(5 + t)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questgamble(token, channelid, pro1, pro2) :
    np = pro2 - pro1
    global quest
    for np in range (np, 0, -1):
        global active_bot
        if active_bot:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + get_ran_gamble(),        
                    'nonce': nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                )
            t = rantime()
            time.sleep(15 + t)
            if np == 1:
                quest = True
        else:
            break
#========================================================================================================================
def questsayowo(token, channelid, pro1, pro2):
    np = pro2 - pro1
    global quest, active_bot
    if not sayowo:
        for np in range(np, 0, -1):
            if active_bot:
                bot_owo(token, "OwO Quest", channelid)
                t = rantime()
                time.sleep(15 + t)
                if np == 1:
                    quest = True
            else:
                break
#========================================================================================================================
def doquest(questss,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid):
    global quest
    quests = questss
    print(quests)
    if (("Say 'owo'") in  quests):
        quest = False
        if not sayowo:
            do_questsayowo = threading.Thread(
                target=questsayowo, 
                args=(
                    tokenst,
                    channelid,
                    int(progress1), 
                    int(progress2)
                )
            )
            return do_questsayowo.start()
    elif (("Gamble") in quests and
            ((not slots_enable) or
            (not coinflip_enable) )):
            quest = False
            do_questgamble = threading.Thread(
                target=questgamble, 
                args=(
                    tokenst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questgamble.start()
    elif (("Use an action command on someone") in quests):
        quest = False
        do_questuseactiongive = threading.Thread(
            target=questuseactiongive, 
            args=(
                tokenst,
                channelid,
                int(progress1),
                int(progress2)
            )
        )
        return do_questuseactiongive.start()
    if extratokencheck:
        if (("Have a friend curse you" in quests )):
            quest = False
            do_questcurseme = threading.Thread(
                target=questcurseme,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questcurseme.start()
        elif (("Have a friend pray to you") in quests):
            quest = False
            do_questprayme = threading.Thread(
                target=questprayme,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questprayme.start()
        elif (("Battle with a friend") in quests):
                quest = False
                do_questbattlefriend = threading.Thread(
                    target=questbattlefriend,
                    args=(
                        tokenst, 
                        tokenrd,
                        main_id,
                        channelid,
                        int(progress1),
                        int(progress2),
                        generate_random_128bit_hex(),
                        generate_random_128bit_hex(),
                        serverid
                    )
                )
                return do_questbattlefriend.start()
        elif (("Have a friend use an action command on you") in quests):
            quest = False
            do_questuseactionreceive = threading.Thread(
                target=questuseactionreceive,
                args=(
                    tokenrd, 
                    useridst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questuseactionreceive.start()
        
def get_quest_1(cont, conts):
    try:
        aquests = cont[0]["description"].split("**1. ")[1].split("**")[0]
        aprogress1 = cont[0]["description"].split("Progress: [")[1].split("/")[0]
        aprogress2 = cont[0]["description"].split("/")[1].split("]")[0]

        avarlock_quest_ = "**1. "
        avarlock_quest__ = "]`"
        avarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        achecklockquest = cont[0]["description"].split("**1. ")[1].split("]")[0]
        ajoinvar1 = "".join([avarlock_quest_, achecklockquest, avarlock_quest__])
        ajoinvar2 = "\n".join([ajoinvar1, avarlock_quest___])

        if ajoinvar2 in conts:
            aquests = ""
            aprogress1 = ""
            aprogress2 = ""
            return aquests, aprogress1, aprogress2
        else:
            aquests = quest_filter(aquests)
            return aquests, aprogress1, aprogress2
    except IndexError:
        aquests = ""
        aprogress1 = ""
        aprogress2 = ""
        return aquests, aprogress1, aprogress2

def get_quest_2(cont, conts):
    try:
        bquests = cont[0]["description"].split("**2. ")[1].split("**")[0]
        bcheckquest1 = cont[0]["description"].split("**2. ")[1].split("Progress: [")[0]
        bvar1 = "Progress: ["
        bcheckquest11 = "".join([bcheckquest1, bvar1])
        bprogress1 = cont[0]["description"].split(bcheckquest11)[1].split("/")[0]
        bvar2 = "/"
        bcheckquest2 = "".join([bcheckquest11, bprogress1, bvar2])
        bprogress2 = cont[0]["description"].split(bcheckquest2)[1].split("]")[0]
        bquests = quest_filter(bquests)

        bvarlock_quest_ = "**2. "
        bvarlock_quest__ = "]`"
        bvarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        bchecklockquest = cont[0]["description"].split("**2. ")[1].split("]")[0]
        bjoinvar1 = "".join([bvarlock_quest_, bchecklockquest, bvarlock_quest__])
        bjoinvar2 = "\n".join([bjoinvar1, bvarlock_quest___])

        if bjoinvar2 in conts:
            bquests = ""
            bprogress1 = ""
            bprogress2 = ""
            return bquests, bprogress1, bprogress2
        else:
            bquests = quest_filter(bquests)
            return bquests, bprogress1, bprogress2
    except IndexError:
        bquests = ""
        bprogress1 = ""
        bprogress2 = ""
        return bquests, bprogress1, bprogress2

def get_quest_3(cont, conts):
    try:
        cquests = cont[0]["description"].split("**3. ")[1].split("**")[0]
        ccheckquest1 = cont[0]["description"].split("**3. ")[1].split("Progress: [")[0]
        cvar1 = "Progress: ["
        ccheckquest11 = "".join([ccheckquest1, cvar1])
        cprogress1 = cont[0]["description"].split(ccheckquest11)[1].split("/")[0]
        cvar2 = "/"
        ccheckquest2 = "".join([ccheckquest11, cprogress1, cvar2])
        cprogress2 = cont[0]["description"].split(ccheckquest2)[1].split("]")[0]
        cquests = quest_filter(cquests)

        cvarlock_quest_ = "**3. "
        cvarlock_quest__ = "]`"
        cvarlock_quest___ = "<:blank:427371936482328596>`‣ 🔒 Locked`"
        cchecklockquest = cont[0]["description"].split("**3. ")[1].split("]")[0]
        cjoinvar1 = "".join([cvarlock_quest_, cchecklockquest, cvarlock_quest__])
        cjoinvar2 = "\n".join([cjoinvar1, cvarlock_quest___])

        if cjoinvar2 in conts:
            cquests = ""
            cprogress1 = ""
            cprogress2 = ""
            return cquests, cprogress1, cprogress2
        else:
            cquests = quest_filter(cquests)
            return cquests, cprogress1, cprogress2
    except IndexError:
        cquests = ""
        cprogress1 = ""
        cprogress2 = ""
        return cquests, cprogress1, cprogress2

def quest_filter(quest):
    if "Say 'owo'" in quest:
        quest == "Say 'owo'"
    elif "Gamble" in quest:
        quest == "Gamble"
    elif "Use an action command on someone" in quest:
        quest == "Use an action command on someone"
    elif "Battle with a friend" in quest:
        quest == "Battle with a friend"
    elif "Have a friend curse you" in quest:
        quest == "Have a friend curse you"
    elif "Have a friend pray to you" in quest:
        quest == "Have a friend pray to you"
    elif "Have a friend use an action command on you" in quest:
        quest == "Have a friend use an action command on you"
    return quest
    
def timecount(userid):
    with open(file_cache, 'r', encoding='utf-8') as h:
        data = json.load(h)
        h.close()
    cache_store = data[userid]
    base_time = datetime.time(7, 0, 0)
    day_base = datetime.datetime.strptime(cache_store[f"day_quest"], "%Y-%m-%d").date()
    base_datetime = datetime.datetime.combine(day_base, base_time)
    base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
    now_utc = datetime.datetime.now(pytz.utc)
    if ((base_datetime_utc < now_utc) and (data[userid]["quest"] == "done")):
        data[userid]["quest"] = "ready"
        with open(file_cache, "w", encoding='utf-8') as i:
            json.dump(data, i, indent=4)
            i.close()
            questcheckers = "ready"
    elif data[userid]["quest"] == "ready":
        questcheckers = "ready"
    else:
        questcheckers = "done"

    return questcheckers
        
def getquests(tokenst,tokenrd,useridst,channelid, tokentype, serverid):
    questchecker = timecount(useridst)
    global quest, active_bot
    aquests = ""
    bquests = ""
    cquests = ""
    if (active_bot)and(questchecker == "ready"):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": tokenst},
            json={
                "content": f"{prefix}q",        
                'nonce': nonce(),
                "tts": False,
                "flags": 0,
                },
        )
        time.sleep(2)
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1",
            headers={"authorization": tokenst}
        )
        try:
            body = response.json()
            cont = body[0]["embeds"]
            conts = cont[0]["description"]
            time.sleep(2)
            if "You finished all of your quests!" in cont[0]['description']:
                with open(file_cache, "r", encoding='utf-8') as j:
                    data = json.load(j)
                    j.close()
                now_utc = datetime.datetime.now(pytz.utc) + datetime.timedelta(days=1)
                data[useridst]["day_quest"] = now_utc.strftime("%Y-%m-%d")
                data[useridst]["quest"] = "done"
                with open(file_cache, "w", encoding='utf-8') as k:
                    json.dump(data, k, indent=4)
                    k.close()

                print(red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f"[{tokentype}]") +
                    yellow(" You have already finished all of your quests!")
                )
            else:
                varquest1 = get_quest_1(cont,conts)
                aquests, aprogress1, aprogress2 = varquest1
                varquest2 = get_quest_2(cont, conts)
                bquests, bprogress1, bprogress2 = varquest2
                varquest3 = get_quest_3(cont, conts)
                cquests, cprogress1, cprogress2 = varquest3                
                if (aquests == bquests) and (aquests == cquests):
                    progress2 = max(aprogress2, bprogress2, cprogress2)
                    progress1 = min(aprogress1, bprogress1, cprogress1)
                    do_quest_1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid))
                    return do_quest_1.start()
                elif (((aquests == bquests) or (aquests == cquests)or(bquests == cquests)) and ((aquests != "") and (bquests != ""))):
                    if (aquests == bquests):
                        progress2 = max(aprogress2, bprogress2)
                        progress1 = min(aprogress1, bprogress1)
                        do_quest_2 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid))
                        do_quest_2.start
                        if cquests != "":
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in cquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_2_1= threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                                do_quest_2_1.start
                            else:
                                do_quest_2_2= threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                                do_quest_2_2.start
                    elif (cquests != ""):
                        if (aquests == cquests):
                            progress2 = max(aprogress2, cprogress2)
                            progress1 = min(aprogress1, cprogress1)
                            do_quest_3 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid))
                            do_quest_3.start
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_3_1 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                                do_quest_3_1.start
                            else:
                                do_quest_3_2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                                do_quest_3_2.start
                        elif (bquests == cquests):
                            progress2 = max(aprogress2, cprogress2)
                            progress1 = min(aprogress1, cprogress1)
                            do_quest_4 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid))
                            do_quest_4.start
                            if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                                progress = int(progress2) - int(progress1)
                                time.sleep(progress * 60 * 5)
                                do_quest_4_1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                                do_quest_4_1.start
                            else:
                                do_quest_4_2 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                                do_quest_4_2.start
                else:
                    if (("pray" or "curse") in aquests) and (("pray" or "curse") in bquests):
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                        do_quest1.start()
                        aprogress = int(aprogress2) - int(aprogress1)
                        if cquests != "":
                            do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                            do_quest3.start()
                            pass
                        time.sleep(aprogress * 60 * 5)
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                        do_quest2.start()
                    elif (("pray" or "curse") in aquests) and (("pray" or "curse") in cquests):
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                        do_quest1.start()
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                        do_quest2.start()
                        aprogress = int(aprogress2) - int(aprogress1)
                        time.sleep(aprogress * 60 * 5)
                        do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                        do_quest3.start()
                    elif (("pray" or "curse") in bquests) and (("pray" or "curse") in cquests):
                        do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                        do_quest2.start()
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                        do_quest1.start()
                        bprogress = int(bprogress2) - int(bprogress1)
                        time.sleep(bprogress * 60 * 5)
                        do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                        do_quest3.start()
                    else:
                        do_quest1 = threading.Thread(target=doquest, args=(aquests,tokenst,tokenrd,useridst,channelid,aprogress1,aprogress2, serverid))
                        do_quest1.start()
                        if bquests != "":
                            do_quest2 = threading.Thread(target=doquest, args=(bquests,tokenst,tokenrd,useridst,channelid,bprogress1,bprogress2, serverid))
                            do_quest2.start()
                        elif cquests != "":
                            do_quest3 = threading.Thread(target=doquest, args=(cquests,tokenst,tokenrd,useridst,channelid,cprogress1,cprogress2, serverid))
                            do_quest3.start()
        except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}] ") +
                red("Unable to check quest❗")
        )
    else:
        pass
#██████╗░██╗░░░██╗███╗░░██╗  ██████╗░░█████╗░████████╗
#██╔══██╗██║░░░██║████╗░██║  ██╔══██╗██╔══██╗╚══██╔══╝
#██████╔╝██║░░░██║██╔██╗██║  ██████╦╝██║░░██║░░░██║░░░
#██╔══██╗██║░░░██║██║╚████║  ██╔══██╗██║░░██║░░░██║░░░
#██║░░██║╚██████╔╝██║░╚███║  ██████╦╝╚█████╔╝░░░██║░░░
#╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
def bot_main():
    add_user(main_id)
    time.sleep(2)
    response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": main_token}
        )
    try:
            body = response.json()
            if (str(body) == "401: Unauthorized"):
                    print(red(f"Main Token / {str(body)}"))
                    time.sleep(5)
                    exit(0)
            else:
                print(blue(f"[Main  Token] User:{body["username"]}{body["discriminator"]}"))
                checklist(main_token, "Main Token", main_channelid, main_id)
                print(green("Main Token ✅"))
    except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta("[Main  Token]") +
                red(f"Error while checking Main Token! ⚠️")
            )
#========================================================================================================================
def bot_extra():
    global etoken
    if extratokencheck:
        add_user(extra_id)
        time.sleep(2)
        etoken = True
        response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": extra_token}
        )
        try:
                body = response.json()
                if (str(body) == "401: Unauthorized"):
                        print(red(f"Extra Token / {str(body)}"))
                        time.sleep(5)
                        exit(0)
                else:
                    print(blue(f"[Extra Token] User:{body["username"]} {body["discriminator"]}"))
                    checklist(extra_token, "Extra Token", extra_channelid, extra_id)
                    print(green("Extra Token ✅"))
        except (KeyError, json.JSONDecodeError) as e:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta("[Extra Token]") +
                    red(f"Error while checking Extra Token! ⚠️")
                )
    else:
        etoken = False
""" ▒█▀▀█ █▀▀█ █░░ █░░ 　 █░░ █▀▀█ █▀▀█ █▀▀█ 
    ▒█░░░ █▄▄█ █░░ █░░ 　 █░░ █░░█ █░░█ █░░█ 
    ▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀▀ █▀▀▀"""
#========================================================================================================================
def run__bot__hunt__and__battle(tokens, tokentypes, channelids, serverid):
    while True:
        global active_bot, battle_hunt
        if active_bot:
            timehunt = rantime()
            timebattle = timehunt + 1
            if (hunt):
                time.sleep(timehunt)
                timehunts = round(timehunt, 3)
                bot_hunt(tokens, timehunts, tokentypes, channelids, generate_random_128bit_hex(), serverid)
                if inventorycheck:
                    time.sleep(1)
                    checkinv(tokens, channelids, tokentypes)
            if (battle) and battle_hunt:
                time.sleep(timebattle + 5)
                timebattles = round(timebattle, 3)
                bot_battle(tokens, timebattles, tokentypes, channelids, generate_random_128bit_hex(), serverid) 
        else:
            break
        time.sleep(15)
#========================================================================================================================
def run__bot__animal(tokens, tokentypes, channelid, ani_types):
     while True:
        global active_bot
        if active_bot:
            if ani_enable:
                bot_animals(tokens, tokentypes, channelid, ani_types)
        else:
            break
        t = rantime()
        time.sleep(60 + t)
#========================================================================================================================
def run__bot__say__owo(tokens, tokentypes, channelids):
     while True:
        global active_bot
        if active_bot:
            if sayowo:
                owosay = rantime()
                if (owosay >= 3):
                    owosay - 3
                time.sleep(owosay)
                bot_owo(tokens, tokentypes, channelids)
        else:
            break
        t = rantime()
        time.sleep(15 + t)
#========================================================================================================================
def run__bot__pray(tokens, tokentypes, channelids, prays):
     while True:
        global active_bot
        if active_bot:
            bot_pray(tokens, tokentypes, channelids, prays)
        else:
            break
        t = rantime_2()
        time.sleep((5 * 60) + t)
#========================================================================================================================
def run__bot__curse(tokens, tokentypes, channelids, curses):
     while True:
        global active_bot
        if active_bot:
                bot_curse(tokens, tokentypes, channelids, curses)
        else:
            break
        t = rantime_2()
        time.sleep((5 * 60) + t)
#========================================================================================================================
def run__bot__upgrade(tokens, tokentypes, channelids):
     while True:
        global active_bot
        if active_bot:
            if ani_enable:
                upgradeall(tokens, tokentypes, channelids)
        else: 
            break
        t = rantime_2()
        time.sleep((10 * 60) + t)
#========================================================================================================================
def run__bot__gamble(tokens, tokentypes, channelids):
    while True:
        global active_bot
        if active_bot:
            if slots_enable:
                bot_slots(tokens, tokentypes, channelids)
        else:
            break
        t = rantime()
        time.sleep(15 + t)
"""░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░████████╗
    ██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
    ██║░░╚═╝███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║░░░██║░░░
    ██║░░██╗██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║░░░██║░░░
    ╚█████╔╝██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
    ░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░"""
def catpcha_recover(token, tokentype, channelid, dmchannelid, userid):
    time.sleep(2)
    run__bot__captcha_thread = threading.Thread(target=run__bot__captcha, args=(token, tokentype, channelid, dmchannelid, userid))
    run__bot__captcha_thread.start()
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta("[Captcha Bot]") +
        green(f"Captcha has been fixed! ⚠️")
    )
    pass
def run__bot__captcha(token, tokentype, channelid, dmchannelid, userid):
    def add_id_to_quest_battle(new_id):
        with open(file_cache, 'r') as read_data:
            data = json.load(read_data)
            read_data.close
        if userid in data:
            id_quest_battle = data[userid].setdefault("id_captcha", {})
            id_list = list(id_quest_battle.values())
            id_list.insert(0, new_id)
            id_list = id_list[:10]
            data[userid]["id_captcha"] = {f"id_{i+1}": v for i, v in enumerate(id_list)}
            with open(file_cache, 'w') as write_data:
                json.dump(data, write_data, indent=4)
                write_data.close
    def captcha_def():
        global active_bot, capcha_flag, task_bot_active, captcha_notification, main_thread, extra_thread
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}] ") +
            red(f"Chat Captcha! ❌")
        )
        active_bot = False
        task_bot_active = False
        captcha_notification = True
        capcha_flag = True
        main_thread.kill()
        extra_thread.kill()
        time.sleep(0.001)
        notification_def(tokentype)
    
    def read_id(id_to_check):
        with open(file_cache, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Truy cập id_captcha bên trong dictionary cache
        id_captcha = data[userid]["id_captcha"]

        for value in id_captcha.values():
            if value == id_to_check:
                return False
        return True

    while True:
        global capcha_flag
        try: 
            response = requests.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages?limit=10",
                headers={"authorization": token}
            )
            responsedm = requests.get(
                f"https://discord.com/api/v9/channels/{dmchannelid}/messages?limit=1",
                headers={"authorization": token}
            )
            if ((response.status_code == 200) and (responsedm.status_code == 200)):
                with open(file_cache, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    f.close
                id_captcha_dm = data[userid]["id_captcha_dm"]

                bodydm = responsedm.json()
                captcha_md= bodydm[0]["id"]
                contentmd = bodydm[0]["content"]
                if  (("Are you a real human?" in  contentmd) and 
                    (captcha_md != id_captcha_dm) and 
                    (capcha_flag == False)):
                    data[userid]["id_captcha_dm"] = captcha_md
                    with open(file_cache, "w", encoding="utf-8") as write_id_dm:
                        json.dump(data, write_id_dm, indent=4)
                        write_id_dm.close()
                    captcha_def()
                    
                body = response.json()
                for bodycount in body:
                    content = bodycount["content"]
                    idowo = bodycount["author"]["id"]
                    captcha_chat = bodycount["id"]
                    #(idowo == "408785106942164992") and 
                    if ((("captcha" in content) or 
                        (f"⚠️ **|** <@{userid}>" in content) or
                        (f"⚠️ **|**" in content)
                        ) and 
                        (read_id(captcha_chat)) and 
                        (capcha_flag == False)):
                        for bodycounts in body:
                            add_id_to_quest_battle(bodycounts["id"])
                        captcha_def()
                        break
            elif ((response.status_code == 401) or responsedm.status_code == 401):
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(" Captcha Bot") +
                    red(f" 401: Unauthorized! ⚠️")
                )
        except (KeyError, json.JSONDecodeError) as e:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta(f"[{tokentype}]") +
                red(f" Error while checking captcha! ⚠️")
            )
            catpcha_recover(token, tokentype, channelid, dmchannelid, userid)
            break
        time.sleep(0.5)
#========================================================================================================================
def dmprotectprouwu(token, channelid, tokentype):    
    try: 
        requests.post(
        f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token, "super-x": autoseed()},
        json={
            "content": "hi bro",        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                },
    )
    except (KeyError, json.JSONDecodeError) as e:
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
            magenta(f"[{tokentype}]") +
            red(" OwO dm channel id incorrect ❌ ")
        )
#========================================================================================================================
def main_account():
    bot_main_thread = threading.Thread(target=bot_main)
    run__bot__hunt__and__battle_thread = threading.Thread(target=run__bot__hunt__and__battle, args=(main_token, "Main Token", main_channelid, main_serverid))
    run__bot__animal_thread = threading.Thread(target=run__bot__animal, args=(main_token, "Main Token", main_channelid, ani_type))
    run__bot__say__owo_thread = threading.Thread(target=run__bot__say__owo, args=(main_token, "Main Token", main_channelid))
    run__bot__pray_thread = threading.Thread(target=run__bot__pray, args=(main_token, "Main Token", main_channelid, pray))
    run__bot__curse_thread = threading.Thread(target=run__bot__curse, args=(main_token, "Main Token", main_channelid, curse))
    run__bot__upgrade_thread = threading.Thread(target=run__bot__upgrade, args=(main_token, "Main Token", main_channelid))
    run__bot__gamble_thread = threading.Thread(target=run__bot__gamble, args=(main_token, "Main Token", main_channelid))
    run__bot__getquests_thread = threading.Thread(target=getquests, args=(main_token, extra_token, main_id, main_questchannelid, "Main Token", main_serverid))
    bot_main_thread.start()
    time.sleep(10)
    if autoquest:
        time.sleep(2)
        run__bot__getquests_thread.start() 
    run__bot__say__owo_thread.start()
    run__bot__hunt__and__battle_thread.start()
    time.sleep(5)
    run__bot__pray_thread.start()
    run__bot__curse_thread.start()
    time.sleep(5)
    run__bot__upgrade_thread.start()
    run__bot__gamble_thread.start()
    run__bot__animal_thread.start()

def extra_account():
    global etoken
    if extratokencheck:
        bot_extra_thread = threading.Thread(target=bot_extra)
        bot_extra_thread.start()
        time.sleep(10)
        if etoken:
            extra__run__bot__hunt__and__battle_thread = threading.Thread(target=run__bot__hunt__and__battle, args=(extra_token, "Extra Token", extra_channelid, extra_serverid))
            extra__run__bot__animal_thread = threading.Thread(target=run__bot__animal, args=(extra_token, "Extra Token", extra_channelid, ani_type))
            extra__run__bot__say__owo_thread = threading.Thread(target=run__bot__say__owo, args=(extra_token, "Extra Token", extra_channelid))
            extra__run__bot__pray_thread = threading.Thread(target=run__bot__pray, args=(extra_token, "Extra Token", extra_channelid, pray))
            extra__run__bot__curse_thread = threading.Thread(target=run__bot__curse, args=(extra_token, "Extra Token", extra_channelid, curse))
            extra__run__bot__upgrade_thread = threading.Thread(target=run__bot__upgrade, args=(extra_token, "Extra Token", extra_channelid))
            extra__run__bot__gamble_thread = threading.Thread(target=run__bot__gamble, args=(extra_token, "Extra Token", extra_channelid))
            extra__run__bot__getquests_thread = threading.Thread(target=getquests, args=(extra_token, main_token, extra_id, extra_questchannelid, "Extra Token", extra_serverid))
            if autoquest:
                extra__run__bot__getquests_thread.start() 
            extra__run__bot__say__owo_thread.start()
            extra__run__bot__hunt__and__battle_thread.start()
            time.sleep(5)
            extra__run__bot__pray_thread.start()
            extra__run__bot__curse_thread.start()
            time.sleep(5)
            extra__run__bot__animal_thread.start()
            extra__run__bot__upgrade_thread.start()
            extra__run__bot__gamble_thread.start()

def controller_recover(token, channelid, userid):
    time.sleep(2)
    print(
        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
        magenta("Controller Bot") +
        green(f"Control has been fixed! ⚠️")
    )
    controller_thread1 = threading.Thread(target=controller, args=(token, channelid, userid))
    controller_thread1.start()

def controller(token, channelid, userid):
    def add_id_to_quest_battle(new_id):
        with open(file_cache, 'r') as read_data:
            data = json.load(read_data)
            read_data.close
        if userid in data:
            id_quest_battle = data[userid].setdefault("id_activate", {})
            id_list = list(id_quest_battle.values())
            id_list.insert(0, new_id)
            id_list = id_list[:10]
            data[userid]["id_activate"] = {f"id_{i+1}": v for i, v in enumerate(id_list)}
            with open(file_cache, 'w') as write_data:
                json.dump(data, write_data, indent=4)
                write_data.close
    def send_mess(messages):
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")+
            yellow(f"{messages}")
        )
        requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages",
        headers={"authorization": token},
        json={
            "content": messages,        
            'nonce': nonce(),
            "tts": False,
            "flags": 0,
                }
        )
    def read_id(id_to_check):
        with open(file_cache, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Truy cập id_captcha bên trong dictionary cache
        id_activate = data[userid]["id_activate"]

        for value in id_activate.values():
            if value == id_to_check:
                return False
        return True
    while True:
        global task_bot_active, active_bot, captcha_notification , main_thread, extra_thread, capcha_flag
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=10",
            headers={"authorization": token},
            ) 
        if response.status_code == 200:
            try:
                body = response.json()
                for bodycount in body:

                    id = bodycount["author"]["id"]
                    id_bot_message = bodycount["id"]
                    if (((id == main_id) or (id == extra_id)) and
                        (read_id(id_bot_message))):
                        content = bodycount["content"]
                        if (content == f"{bot_prefix}stop"):
                            if task_bot_active:
                                for bodycounts in body:
                                    add_id_to_quest_battle(bodycounts["id"])
                                active_bot = False
                                task_bot_active = False
                                
                                main_thread.kill()
                                extra_thread.kill()
                                time.sleep(2)
                                send_mess('Bot stopped!')
                            else:
                                send_mess('Bot already stopped!')
                        elif (content == f"{bot_prefix}run"):
                            if  not task_bot_active:
                                for bodycounts in body:
                                    add_id_to_quest_battle(bodycounts["id"])
                                main_thread = multiprocessing.Process(target=main_account)
                                extra_thread = multiprocessing.Process(target=extra_account)

                                main_thread.start()
                                extra_thread.start()
                                captcha_notification = False
                                
                                task_bot_active = True
                                capcha_flag = False
                                active_bot = True
                                time.sleep(2)
                                send_mess('Bot is Runing!')
                            else:
                                send_mess('Bot has already runned!')
            except json.JSONDecodeError as e:
                print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta("Controller Bot") +
                red(f" Error while Control! ⚠️")
                )
                controller_recover(token, channelid, userid)
                break
        elif response.status_code == 401:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                magenta("[Controller Bot]") +
                red(f" 401: Unauthorized! ⚠️")
            )
        time.sleep(0.5)

if __name__ == '__main__':

    checkversion()
    install_update()
    main_thread = multiprocessing.Process(target=main_account)
    extra_thread = multiprocessing.Process(target=extra_account)

    main_thread.start()
    time.sleep(0.1)
    extra_thread.start()
    time.sleep(2)
    run__bot__captcha_thread = threading.Thread(target=run__bot__captcha, args=(main_token, "Main Token", main_channelid, main_dmchannelid, main_id))
    controller_thread1 = threading.Thread(target=controller, args=(main_token, main_channelid, main_id))
    run__bot__captcha_thread.start()
    controller_thread1.start()

    if etoken:
        extra__run__bot__captcha_thread = threading.Thread(target=run__bot__captcha, args=(extra_token, "Extra Token", extra_channelid, extra_dmchannelid, extra_id))
        controller_thread2 = threading.Thread(target=controller, args=(extra_token, extra_channelid, extra_id))
        extra__run__bot__captcha_thread.start()
        controller_thread2.start()
    
    
    while True:
        """keep alive"""
        time.sleep(1)
