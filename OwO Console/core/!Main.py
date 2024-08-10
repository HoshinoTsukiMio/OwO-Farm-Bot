version = "v2-0.1.6806951a45f5"
import multiprocessing.queues
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
            if converted_value < 1:
                return "1"
            else:
                return str(converted_value)
        except ValueError:
            return "1"
    elif isinstance(str_value, bool):
        return "1"
    elif isinstance(str_value, float):
        try:
            converted_value = int(str_value)
            if converted_value < 1:
                return "1"
            else:
                return converted_value
        except ValueError:
            return "1"
    else:
        return str(str_value)
def str_int_conv(str_value):
    if isinstance(str_value, str):
        try:
            converted_value = int(float(str_value))
            if converted_value < 1:
                return 1
            else:
                return converted_value
        except ValueError:
            return 1
    elif isinstance(str_value, bool):
        return 1
    elif isinstance(str_value, float):
        try:
            converted_value = int(str_value)
            if converted_value < 1:
                return 1
            else:
                return converted_value
        except ValueError:
            return 1
    else:
        return str_value
red = Terminal().red
green = Terminal().green
blue = Terminal().blue
yellow = Terminal().yellow
magenta = Terminal().magenta

"""▄▀█ █▀▀ █▀▀ █▀▀ █▀ █▀   ▀█▀ █░█ █▀▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
   █▀█ █▄▄ █▄▄ ██▄ ▄█ ▄█   ░█░ █▀█ ██▄   ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█"""
try:
    setting               = cfgs["settings"]
    number_of_groups      = str_int_conv(setting['number_of_groups'])
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
except (IndexError, KeyError) as e:
    print("Check your setting_config.json there some missing")
    time.sleep(1)
    os._exit(0)
time.sleep(1.5)
notification = Notify()
process = psutil.Process()



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

"""███╗░░░███╗░█████╗░██╗███╗░░██╗  ██████╗░███████╗███████╗
   ████╗░████║██╔══██╗██║████╗░██║  ██╔══██╗██╔════╝██╔════╝
   ██╔████╔██║███████║██║██╔██╗██║  ██║░░██║█████╗░░█████╗░░
   ██║╚██╔╝██║██╔══██║██║██║╚████║  ██║░░██║██╔══╝░░██╔══╝░░
   ██║░╚═╝░██║██║░░██║██║██║░╚███║  ██████╔╝███████╗██║░░░░░
   ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░░░░"""
class API():
    def __init__(self):
        self.extratokencheck = extratokencheck
        self.main_process = None
        self.pray_curse = True
        self.battle_hunt = True
        self.quest = True
        self.active_bot = True
        self.capcha_flag = False
        self.task_bot_active = True
        self.captcha_notification = False
        self.pray = pray
        self.curse = curse
        if self.curse and self.pray:
            self.pray = True
            self.curse = False
    def load_cache(self):
        try:
            with open(file_cache, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError , FileNotFoundError):
            data = {}
        return data
    #========================================================================================================================
    def save_cache(self,data):
        with open(file_cache, "w") as f:
            json.dump(data, f, indent=4)
    #========================================================================================================================
    def add_user(self,user_ids):
        caches = self.load_cache()
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
        self.save_cache(caches)
    def read_id(self, id_to_check,userid, path):
        with open(file_cache, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Truy cập id_captcha bên trong dictionary cache
        id_captcha = data[userid][path]

        for value in id_captcha.values():
            if value == id_to_check:
                return False
        return True
    def add_id_to_cache(self, new_id, userid, path):
        with open(file_cache, 'r') as read_data:
            data = json.load(read_data)
        if userid in data:
            id_quest_battle = data[userid].setdefault(path, {})
            id_list = list(id_quest_battle.values())
            id_list.insert(0, new_id)
            id_list = id_list[:10]
            data[userid][path] = {f"id_{i+1}": v for i, v in enumerate(id_list)}
            with open(file_cache, 'w') as write_data:
                json.dump(data, write_data, indent=4)
                time.sleep(0.01)
                write_data.close()
    #========================================================================================================================
    def notification_def(self,username):
        notification = Notify()
        noti_count = 11
        while noti_count > -1:
            if self.captcha_notification == True:
                noti_count = noti_count - 1
                if noti_count > 0:
                    noti_count_str = str(noti_count)
                    notification.title = f"[{username}] Captcha Detected!"
                    notification.message = f"SOLVE CAPTCHA AND RESTART BOT\nyou only have {noti_count_str}min left"
                    notification.icon = "data/owo.ico"
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{username}]") +
                        red(f" Time left {noti_count} Min! ⚠️")
                    )
                    notification.send()
                else:
                    noti_count_str = str(noti_count)
                    notification.title = f"[{username}] Captcha Detected!"
                    notification.message = f"You are Banned by OwO"
                    notification.icon = "data/owo.ico"
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{username}]") +
                        red(f" Time left {noti_count} Min! ⚠️")
                    )
                    notification.send()
                    time.sleep(3)
                    os._exit(0)
            else:
                break
            time.sleep(60)
    #========================================================================================================================
    def rantime(self):
        rdt = random.randint(1, 5) + round(random.uniform(0, 1), 3)
        return rdt
    #========================================================================================================================
    def rantime_2(self):
        rdt = random.randint(5, 30) + round(random.uniform(0, 1), 3)
        return rdt
    #========================================================================================================================
    def nonce(self):
        rannonce = 1098393848631590 + math.floor(round(random.uniform(0, 1), 3) * 9999)
        return rannonce
    #========================================================================================================================
    def autoseed(self, token):
        seed = hashlib.sha256(f"seedaccess-entropyverror-apiv10.{token}".encode()).digest()
        return seed
    #========================================================================================================================
    def generate_random_128bit_hex(self):
        "Tạo một chuỗi hexa ngẫu nhiên 128-bit."
        random_bytes = os.urandom(16)  # 16 byte = 128 bit
        return random_bytes.hex()
    #========================================================================================================================
    def bot_owo(self,token,group, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": "owo",        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            blue(" OwO ✅")
        )
    #========================================================================================================================
    def bot_hunt(self, token, timehunt, group, tokentype, channelid, session_id, serverid):
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
                    "nonce": self.nonce(),
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
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
            )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            blue(" Hunt ✅ (" + str(timehunt) + " ms)")
        )
    #========================================================================================================================
    def bot_battle(self, token, timebattle, group, tokentype, channelid, session_id, serverid):
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
                    "nonce": self.nonce(),
                    "analytics_location": "slash_ui"
            },
        )
        else:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + "b",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
            )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            blue(" Battle ✅ (" + str(timebattle) + " ms)")
        )
    #========================================================================================================================
    def get_ran_mess(self):
        grm = random.randint(0, (len(phrases)-1))
        return phrases[grm]
    #========================================================================================================================
    def get_ran_act(self):
        gra = random.randint(0, (len(actvar)-1))
        return actvar[gra]
    #========================================================================================================================
    def get_ran_gamble(self):
        gra = random.randint(0, (len(gamblevar)-1))
        return gamblevar[gra]
    #========================================================================================================================
    def ran_message(self, token, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": self.get_ran_mess(),        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
    #========================================================================================================================
    def bot_animals(self, token,group, tokentype, channelid, ani_type):
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
                    "nonce": self.nonce(),
                    "tts": False,
                    "flags": 0,
                },
            )
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                blue(f" Animals ✅ / Type: {ani_type}")
            )
        else:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                blue(f" Animals ❌ / Error: Incorrect Type")
            )
    #========================================================================================================================
    def bot_pray(self, token, group, tokentype, channelid, pray):
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
                ct = prefix + "pray <@" + self.main_id + ">"
                bt = "Pray to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif pray == "extra":
            if (tokentype == "Extra Token"):
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "pray <@" + self.extra_id + ">"
                bt = "Pray to extra"
        else:
            ct = ""
            bt = ""
                
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow( f" {bt} ✅")
            )
    #========================================================================================================================
    def bot_curse(self, token, group, tokentype, channelid, curse):
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
                ct = prefix + "curse <@" + self.main_id + ">"
                bt = "Curse to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif curse == "extra":
            if (tokentype == "Extra Token"):
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "curse <@" + self.extra_id + ">"
                bt = "Curse to extra"
        else:
            ct = " "
            bt = " "
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow( f" {bt} ✅")
            )
    #========================================================================================================================
    def cookie(self, token, group, tokentype, channelid):
        if (tokentype == "Extra Token"):
            ct = prefix + "cookie <@"+ self.main_id + ">"
        else :
            if self.extratokencheck:
                ct = prefix + "cookie <@"+ self.extra_id +">"
            else:
                ct = prefix + "cookie <@408785106942164992>"
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" Cookie ✅")
            )
    #========================================================================================================================
    def daily(self, token, group, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "daily",        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" Daily ✅")
            )
    #========================================================================================================================
    def bot_coinflip(self, token, group, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "cf " + coinflip_amount,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" Gamble / CoinFlip ✅ / Amount: " + coinflip_amount)
            )
    #========================================================================================================================
    def bot_slots(self, token, group, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "s " + slots_amount,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" Gamble / slots ✅ / Amount: " + slots_amount)
            )
    #========================================================================================================================
    def upgradeall(self, token, group, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "upg " + upg_type + " all",        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" Upgrade AutoHunt ✅ ")
            )
    """▒█▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 ▒█░░░ ░▀░ █▀▀ ▀▀█▀▀ 
    ▒█░▒█ █░░█ █▀▀ ▀▀█ ░░█░░ 　 █▄▄█ █░░█ █░░█ 　 ▒█░░░ ▀█▀ ▀▀█ ░░█░░ 
    ░▀▀█▄ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░"""
    def dailycount(self, userid):
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
    def checklist(self, token, group, tokentype, channelid, userid):
        if self.dailycount(userid) == "ready":
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": f"{prefix}cl",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
            )
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                blue(f" Sending Checklist📜...")
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
                            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")+
                            magenta(f" [{group}]")+
                            magenta(f" [{tokentype}]")+
                            blue(f" Getting Checklist🔎...")
                            )
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
                            self.daily(token, group, tokentype, channelid)
                        elif "⬛ 🍪" in cont:
                            self.cookie(token, group, tokentype, channelid)
                        elif "⬛ 📝" in cont:
                            print(
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                                magenta(f" [{group}]") +
                                magenta(f" [{tokentype}]") +
                                blue(f" YOUR DAILY VOTE IS AVAILABLE!")
                                )
                        break
                    else:
                        continue
                except (KeyError, json.JSONDecodeError) as e:
                    if isinstance(e, IndexError) and str(e) == "list index out of range":
                        print(
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                                magenta(f" [{group}]") +
                                magenta(f" [{tokentype}]") +
                                red(" Unable to get Checklist❗")
                            )
                        return
                    else:
                        print(
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                                magenta(f" [{group}]") +
                                magenta(f" [{tokentype}]") +
                                red(" Unable to get Checklist❗")
                            )
                time.sleep(0.05)
    #========================================================================================================================
    def checkinv(self, token, channelid, group, tokentype):
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
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta(f" [{group}]") +
                    magenta(f" [{tokentype}]") +
                    blue(" inventory checking 🔍")
                )
                if "gem1" not in cont:
                    collection.append("huntgem")
                if "gem3" not in cont:
                    collection.append("empgem")
                if "gem4" not in cont:
                    collection.append("luckgem")
                if "gem1" in cont and "gem3" in cont and "gem4" in cont:
                    self.getinv(token, channelid, group, tokentype, "nogem", ["nocollection"])
                else:
                    self.getinv(token, channelid, group, tokentype, "gemvar", collection)
        else:
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                magenta(f" [{tokentype}]") +
                yellow(" inventory checking 🔍")
             )
            self.getinv(token, channelid, group, tokentype, "nogem", ["nocollection"])
    #========================================================================================================================
    def getinv(self, token, channelid, group, tokentype, gemc, collectc):
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
                self.gemuse(token, gem, channelid, group, tokentype)

        if lootboxcheck:
            if "`050`" in cont:
                time.sleep(2)
                self.boxuse(token, "lb all", channelid, group, tokentype)

        if fabledlootboxcheck:
            if "`049`" in cont:
                time.sleep(2)
                self.boxuse(token, "lootbox fabled all", channelid, group, tokentype)

        if cratecheck:
            if "`100`" in cont:
                time.sleep(2)
                self.boxuse(token, "wc all", channelid, group, tokentype)
    #========================================================================================================================
    def boxuse(self, token, box, channelid, group, tokentype):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + box,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            yellow(f" {box} ✅")
        )
    #========================================================================================================================
    def gemuse(self, token, gem, channelid, group, tokentype):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "use " + gem,        
                'nonce': self.nonce(),
                "tts": False,
                "flags": 0,
                    },
        )
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            yellow(" Gem ✅")
        )
    #========================================================================================================================
    def questprayme(self, tokenrd, useridst, channelid, pro1, pro2):
        np = (pro2 - pro1) + 1
        self.pray_curse = False
        for np in range (np, 0, -1):
            if self.active_bot:
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenrd},
                json={
                    "content": prefix + f"pray <@{useridst}>",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = self.rantime_2()
                time.sleep(300 + t)
                if np <= 1:
                    self.quest = True
                    self.pray_curse = True
    #========================================================================================================================
    def questcurseme(self, tokenrd, useridst, channelid, pro1, pro2):
        np = (pro2 - pro1) + 1
        self.pray_curse = False
        for np in range (np, 0, -1):
            if self.active_bot:
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenrd},
                json={
                    "content": prefix + f"curse <@{useridst}>",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = self.rantime_2()
                time.sleep(300 + t)
                if np <= 1:
                    self.pray_curse = True
                    self.quest = True
    #========================================================================================================================
    def questbattlefriend(self, tokenst, tokenrd, useridst, channelid, pro1, pro2, session_id, session_id2, serverid):
        np = (pro2 - pro1) + 1
        self.battle_hunt = False
        def get_id(token, channelid, userid):
            response = requests.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages?limit=10",
                headers={"authorization": token},
                ) 
            body = response.json()
            for bodycount in body:
                if (bodycount["author"]["id"] == "408785106942164992"):
                    if((self.read_id(bodycount["id"], useridst, "id_quest_battle")) and 
                        (bodycount["content"] == f"<@{userid}>") and 
                        (bodycount["embeds"][0]["description"] =="`owo ab` to accept the battle!\n`owo db` to decline the battle!")):
                        bodycount["id"]
                        self.add_id_to_cache(bodycount["id"], useridst, "id_quest_battle")
                        return bodycount["id"]
                else:
                    continue
                return False
        for np in range (np, 0, -1):
            if self.active_bot:
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
                            "nonce": self.nonce(),
                            "analytics_location": "slash_ui"
                        },
                    )
                    time.sleep(3)
                    requests.post(
                        f"https://discord.com/api/v9/interactions",
                        headers={"authorization": tokenst},
                        json = {
                            "type": 3,
                            "nonce": self.nonce(),
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
                    t = self.rantime()
                    time.sleep(15 + t)
                    if np <= 1:
                        self.battle_hunt = True
                        self.quest = True
                
                else:
                    requests.post(
                    f"https://discord.com/api/v9/channels/{channelid}/messages",
                    headers={"authorization": tokenrd},
                    json={
                        "content": prefix + f"b <@{useridst}>",        
                        'nonce': self.nonce(),
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
                        'nonce': self.nonce(),
                        "tts": False,
                        "flags": 0,
                            },
                        )
                    t = self.rantime()
                    time.sleep(15 + t)
                    if np <= 1:
                        time.sleep(5)
                        self.battle_hunt = True
                        self.quest = True
    #========================================================================================================================
    def questuseactionreceive(self,tokenrd, useridst, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range (np, 0, -1):
            if self.active_bot:
                
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenrd},
                json={
                    "content": prefix + f"{self.get_ran_act()} <@"+ useridst +">",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True
    #========================================================================================================================
    def questuseactionreceive(self, tokenrd, useridst, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range (np, 0, -1):
            if self.active_bot:
                
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenrd},
                json={
                    "content": prefix + f"{self.get_ran_act()} <@"+ useridst +">",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True
    #========================================================================================================================
    def questuseactiongive(self, token, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range (np, 0, -1):
            if self.active_bot:
                requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + f"{self.get_ran_act()} <@408785106942164992>",        
                    'nonce': self.nonce(),
                    "tts": False,
                    "flags": 0,
                        },
                    )
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True
    #========================================================================================================================
    def questgamble(self, token, channelid, pro1, pro2) :
        np = pro2 - pro1
        for np in range (np, 0, -1):
            if (self.active_bot and 
                ((not coinflip_enable) or 
                 (not slots_enable))):
                requests.post(
                    f"https://discord.com/api/v9/channels/{channelid}/messages",
                    headers={"authorization": token},
                    json={
                        "content": prefix + self.get_ran_gamble(),        
                        'nonce': self.nonce(),
                        "tts": False,
                        "flags": 0,
                            },
                    )
                t = self.rantime()
                time.sleep(15 + t)
                if np <= 1:
                    self.quest = True
    #========================================================================================================================
    def questsayowo(self, token, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if ((not sayowo) and 
                self.active_bot):
                self.bot_owo(token, "OwO Quest", channelid)
                t = self.rantime()
                time.sleep(15 + t)
                if np <= 1:
                    self.quest = True
    #========================================================================================================================
    def doquest(self, quests,tokenst,tokenrd,useridst,channelid,progress1,progress2, serverid):
        global quest
        if (("owo") in  quests):
            quest = False
            if not sayowo:
                do_questsayowo = threading.Thread(
                    target=self.questsayowo, 
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
                    target=self.questgamble, 
                    args=(
                        tokenst,
                        channelid,
                        int(progress1),
                        int(progress2)
                    )
                )
                return do_questgamble.start()
        elif (("action give") in quests):
            quest = False
            do_questuseactiongive = threading.Thread(
                target=self.questuseactiongive, 
                args=(
                    tokenst,
                    channelid,
                    int(progress1),
                    int(progress2)
                )
            )
            return do_questuseactiongive.start()
        if self.extratokencheck:
            if (("curse" in quests )):
                quest = False
                do_questcurseme = threading.Thread(
                    target=self.questcurseme,
                    args=(
                        tokenrd, 
                        useridst,
                        channelid,
                        int(progress1),
                        int(progress2)
                    )
                )
                return do_questcurseme.start()
            elif (("pray") in quests):
                quest = False
                do_questprayme = threading.Thread(
                    target=self.questprayme,
                    args=(
                        tokenrd, 
                        useridst,
                        channelid,
                        int(progress1),
                        int(progress2)
                    )
                )
                return do_questprayme.start()
            elif (("Battle") in quests):
                    quest = False
                    do_questbattlefriend = threading.Thread(
                        target=self.questbattlefriend,
                        args=(
                            tokenst, 
                            tokenrd,
                            useridst,
                            channelid,
                            int(progress1),
                            int(progress2),
                            self.generate_random_128bit_hex(),
                            self.generate_random_128bit_hex(),
                            serverid
                        )
                    )
                    return do_questbattlefriend.start()
            elif (("action recive") in quests):
                quest = False
                do_questuseactionreceive = threading.Thread(
                    target=self.questuseactionreceive,
                    args=(
                        tokenrd, 
                        useridst,
                        channelid,
                        int(progress1),
                        int(progress2)
                    )
                )
                return do_questuseactionreceive.start()
            
    def get_quest_1(self, cont, conts):
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
                aquests = self.quest_filter(aquests)
                return aquests, aprogress1, aprogress2
        except IndexError:
            aquests = ""
            aprogress1 = ""
            aprogress2 = ""
            return aquests, aprogress1, aprogress2

    def get_quest_2(self, cont, conts):
        try:
            bquests = cont[0]["description"].split("**2. ")[1].split("**")[0]
            bcheckquest1 = cont[0]["description"].split("**2. ")[1].split("Progress: [")[0]
            bvar1 = "Progress: ["
            bcheckquest11 = "".join([bcheckquest1, bvar1])
            bprogress1 = cont[0]["description"].split(bcheckquest11)[1].split("/")[0]
            bvar2 = "/"
            bcheckquest2 = "".join([bcheckquest11, bprogress1, bvar2])
            bprogress2 = cont[0]["description"].split(bcheckquest2)[1].split("]")[0]

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
                bquests = self.quest_filter(bquests)
                return bquests, bprogress1, bprogress2
        except IndexError:
            bquests = ""
            bprogress1 = ""
            bprogress2 = ""
            return bquests, bprogress1, bprogress2

    def get_quest_3(self, cont, conts):
        try:
            cquests = cont[0]["description"].split("**3. ")[1].split("**")[0]
            ccheckquest1 = cont[0]["description"].split("**3. ")[1].split("Progress: [")[0]
            cvar1 = "Progress: ["
            ccheckquest11 = "".join([ccheckquest1, cvar1])
            cprogress1 = cont[0]["description"].split(ccheckquest11)[1].split("/")[0]
            cvar2 = "/"
            ccheckquest2 = "".join([ccheckquest11, cprogress1, cvar2])
            cprogress2 = cont[0]["description"].split(ccheckquest2)[1].split("]")[0]

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
                cquests = self.quest_filter(cquests)
                return cquests, cprogress1, cprogress2
        except IndexError:
            cquests = ""
            cprogress1 = ""
            cprogress2 = ""
            return cquests, cprogress1, cprogress2

    def quest_filter(self, quest):
        quests = ""
        if "Say 'owo'" in quest:
            quests = "owo"
        elif "Gamble" in quest:
            quests = "Gamble"
        elif "1Use an action command on someone" in quest:
            quests = "action give"
        elif "Battle with a friend" in quest:
            quests = "Battle"
        elif "Have a friend curse you" in quest:
            quests = "curse"
        elif "Have a friend pray to you" in quest:
            quests = "pray"
        elif "Have a friend use an action command on you" in quest:
            quests = "action recive"
        return quests
        
    def timecount(self, userid):
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
            
    def getquests(self, tokenst,tokenrd,useridst,channelid, group, tokentype, serverid,):
        questchecker = self.timecount(useridst)
        aquests = ""
        bquests = ""
        cquests = ""
        if (self.active_bot)and(questchecker == "ready"):
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenst},
                json={
                    "content": f"{prefix}q",        
                    'nonce': self.nonce(),
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

                    print(red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{group}]") +
                        magenta(f" [{tokentype}]") +
                        yellow(" You have already finished all of your quests!")
                    )
                else:
                    varquest1 = self.get_quest_1(cont,conts)
                    aquests, aprogress1, aprogress2 = varquest1
                    varquest2 = self.get_quest_2(cont, conts)
                    bquests, bprogress1, bprogress2 = varquest2
                    varquest3 = self.get_quest_3(cont, conts)
                    cquests, cprogress1, cprogress2 = varquest3                
                    if (aquests == bquests) and (aquests == cquests):
                        progress2 = max(aprogress2, bprogress2, cprogress2)
                        progress1 = min(aprogress1, bprogress1, cprogress1)
                        do_quest_1 = threading.Thread(
                            target=self.doquest, 
                            args=(
                                aquests,
                                tokenst,
                                tokenrd,
                                useridst,
                                channelid,
                                progress1,
                                progress2, 
                                serverid
                            )
                        )
                        return do_quest_1.start()
                    elif (((aquests == bquests) or 
                           (aquests == cquests) or
                           (bquests == cquests)) and 
                           ((aquests != "") and 
                            (bquests != ""))):
                        if (aquests == bquests):
                            progress2 = max(aprogress2, bprogress2)
                            progress1 = min(aprogress1, bprogress1)
                            do_quest_2 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    aquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    progress1,
                                    progress2, 
                                    serverid
                                )
                            )
                            do_quest_2.start
                            if cquests != "":
                                if ((("pray" in aquests) or ("curse" in aquests)) and 
                                    (("pray" in cquests) or ("curse" in cquests))):
                                    progress = int(progress2) - int(progress1)
                                    time.sleep(progress * 60 * 5)
                                    do_quest_2_1= threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            cquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            cprogress1,
                                            cprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_2_1.start
                                else:
                                    do_quest_2_2= threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            cquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            cprogress1,
                                            cprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_2_2.start
                        elif (cquests != ""):
                            if (aquests == cquests):
                                progress2 = max(aprogress2, cprogress2)
                                progress1 = min(aprogress1, cprogress1)
                                do_quest_3 = threading.Thread(
                                    target=self.doquest, 
                                    args=(
                                        aquests,
                                        tokenst,
                                        tokenrd,
                                        useridst,
                                        channelid,
                                        progress1,
                                        progress2, 
                                        serverid
                                    )
                                )
                                do_quest_3.start
                                if ((("pray" in aquests) or ("curse" in aquests)) and 
                                    (("pray" in bquests) or ("curse" in bquests))):
                                    progress = int(progress2) - int(progress1)
                                    time.sleep(progress * 60 * 5)
                                    do_quest_3_1 = threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            bquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            bprogress1,
                                            bprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_3_1.start
                                else:
                                    do_quest_3_2 = threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            bquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            bprogress1,
                                            bprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_3_2.start
                            elif (bquests == cquests):
                                progress2 = max(aprogress2, cprogress2)
                                progress1 = min(aprogress1, cprogress1)
                                do_quest_4 = threading.Thread(
                                    target=self.doquest, 
                                    args=(
                                        bquests,
                                        tokenst,
                                        tokenrd,
                                        useridst,
                                        channelid,
                                        progress1,
                                        progress2, 
                                        serverid
                                        )
                                    )
                                do_quest_4.start
                                if ((("pray" in aquests) or ("curse" in aquests)) and 
                                    (("pray" in bquests) or ("curse" in bquests))):
                                    progress = int(progress2) - int(progress1)
                                    time.sleep(progress * 60 * 5)
                                    do_quest_4_1 = threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            aquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            aprogress1,
                                            aprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_4_1.start
                                else:
                                    do_quest_4_2 = threading.Thread(
                                        target=self.doquest, 
                                        args=(
                                            aquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            aprogress1,
                                            aprogress2, 
                                            serverid
                                        )
                                    )
                                    do_quest_4_2.start
                    else:
                        if ((("pray" in aquests) or ("curse" in aquests)) and 
                              (("pray" in bquests) or ("curse" in bquests))):
                            do_quest1 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    aquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    aprogress1,
                                    aprogress2, 
                                    serverid
                                )
                            )
                            do_quest1.start()
                            aprogress = int(aprogress2) - int(aprogress1)
                            if cquests != "":
                                do_quest3 = threading.Thread(
                                    target=self.doquest, 
                                    args=(
                                        cquests,
                                        tokenst,
                                        tokenrd,
                                        useridst,
                                        channelid,
                                        cprogress1,
                                        cprogress2, 
                                        serverid
                                    )
                                )
                                do_quest3.start()
                                pass
                            time.sleep(aprogress * 60 * 5)
                            do_quest2 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    bquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    bprogress1,
                                    bprogress2, 
                                    serverid
                                )
                            )
                            do_quest2.start()
                        elif ((("pray" in aquests) or ("curse" in aquests)) and 
                              (("pray" in cquests) or ("curse" in cquests))):
                            do_quest1 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    aquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    aprogress1,
                                    aprogress2, 
                                    serverid
                                )
                            )
                            do_quest1.start()
                            do_quest2 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    bquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    bprogress1,
                                    bprogress2, 
                                    serverid
                                )
                            )
                            do_quest2.start()
                            aprogress = int(aprogress2) - int(aprogress1)
                            time.sleep(aprogress * 60 * 5)
                            do_quest3 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    cquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    cprogress1,
                                    cprogress2, 
                                    serverid
                                )
                            )
                            do_quest3.start()
                        elif ((("pray" in bquests) or ("curse" in bquests)) and 
                              (("pray" in cquests) or ("curse" in cquests))):
                            do_quest2 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    bquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    bprogress1,
                                    bprogress2, 
                                    serverid
                                )
                            )
                            do_quest2.start()
                            do_quest1 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    aquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    aprogress1,
                                    aprogress2, 
                                    serverid
                                )
                            )
                            do_quest1.start()
                            bprogress = int(bprogress2) - int(bprogress1)
                            time.sleep(bprogress * 60 * 5)
                            do_quest3 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    cquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    cprogress1,
                                    cprogress2,
                                    serverid
                                )
                            )
                            do_quest3.start()
                        else:
                            do_quest1 = threading.Thread(
                                target=self.doquest, 
                                args=(
                                    aquests,
                                    tokenst,
                                    tokenrd,
                                    useridst,
                                    channelid,
                                    aprogress1,
                                    aprogress2, 
                                    serverid
                                )
                            )
                            do_quest1.start()
                            if bquests != "":
                                do_quest2 = threading.Thread(
                                    target=self.doquest, 
                                    args=(
                                        bquests,
                                        tokenst,
                                        tokenrd,
                                        useridst,
                                        channelid,
                                        bprogress1,
                                        bprogress2, 
                                        serverid
                                    )
                                )
                                do_quest2.start()
                            elif cquests != "":
                                do_quest3 = threading.Thread(
                                    target=self.doquest, 
                                    args=(
                                        cquests,
                                        tokenst,
                                        tokenrd,
                                        useridst,
                                        channelid,
                                        cprogress1,
                                        cprogress2, 
                                        serverid
                                    )
                                )
                                do_quest3.start()
            except (KeyError, json.JSONDecodeError) as e:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f" [{group}]") +
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
    def bot_main(self, group):
        self.add_user(self.main_id)
        response = requests.get(
                f"https://canary.discord.com/api/v9/users/@me",
                headers={"authorization": self.main_token}
            )
        try:
                body = response.json()
                if (str(body) == "401: Unauthorized"):
                        print(
                            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                            magenta(f" [{group}]") +
                            magenta(" [Main  Token]") +
                            red(f" / {str(body)}")
                        )
                        time.sleep(5)
                        exit(0)
                else:
                    print(blue(f"User: {body["username"]}"))
                    self.checklist(
                        self.main_token, 
                        group, 
                        "Main  Token", 
                        self.main_channelid, 
                        self.main_id)
        except (KeyError, json.JSONDecodeError) as e:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                    magenta(f" [{group}]") +
                    magenta(" [Main  Token]") +
                    red(f" Error while checking Main  Token! ⚠️")
                )
                time.sleep(5)
                exit(0)
    #========================================================================================================================
    def bot_extra(self, group):
        if self.extratokencheck:
            self.add_user(self.extra_id)
            response = requests.get(
                f"https://canary.discord.com/api/v9/users/@me",
                headers={"authorization": self.extra_token}
            )
            try:
                    body = response.json()
                    if (str(body) == "401: Unauthorized"):
                            print(
                            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                            magenta(f" [{group}]") +
                            magenta(" [Extra  Token]") +
                            red(f" / {str(body)}")
                        )
                            time.sleep(5)
                            exit(0)
                    else:
                        print(blue(f"User: {body["username"]}"))
                        self.checklist(
                            self.extra_token, 
                            group, 
                            "Extra Token", 
                            self.extra_channelid, 
                            self.extra_id
                        )
            except (KeyError, json.JSONDecodeError) as e:
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{group}]") +
                        magenta(" [Extra Token]") +
                        red(f" Error while checking Extra Token! ⚠️")
                    )
                    time.sleep(5)
                    exit(0)
    """ ▒█▀▀█ █▀▀█ █░░ █░░ 　 █░░ █▀▀█ █▀▀█ █▀▀█ 
        ▒█░░░ █▄▄█ █░░ █░░ 　 █░░ █░░█ █░░█ █░░█ 
        ▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀▀ █▀▀▀"""
    #========================================================================================================================
    def run__bot__hunt__and__battle(self, tokens, group, tokentypes, channelids, serverid):
        session_id = self.generate_random_128bit_hex()
        while True:
            if self.active_bot:
                timehunt = self.rantime()
                timebattle = timehunt + 1
                if (hunt):
                    time.sleep(timehunt)
                    timehunts = round(timehunt, 3)
                    self.bot_hunt(
                        tokens, 
                        timehunts, 
                        group, 
                        tokentypes, 
                        channelids, 
                        session_id, 
                        serverid
                    )
                    if inventorycheck:
                        time.sleep(1)
                        self.checkinv(
                            tokens, 
                            channelids, 
                            group, 
                            tokentypes
                        )
                if (battle) and self.battle_hunt:
                    time.sleep(timebattle + 5)
                    timebattles = round(timebattle, 3)
                    self.bot_battle(
                        tokens, 
                        timebattles, 
                        group, 
                        tokentypes, 
                        channelids, 
                        session_id, 
                        serverid
                    ) 
            time.sleep(15)
    #========================================================================================================================
    def run__bot__animal(self, tokens, group, tokentypes, channelid, ani_types):
        while True:
            if (self.active_bot and 
                ani_enable):
                self.bot_animals(
                    tokens, 
                    group, 
                    tokentypes, 
                    channelid, 
                    ani_types
                )
            t = self.rantime()
            time.sleep(60 + t)
    #========================================================================================================================
    def run__bot__say__owo(self, tokens, group, tokentypes, channelids):
        while True:
            if (self.active_bot and 
                sayowo):
                self.bot_owo(
                    tokens, 
                    group, 
                    tokentypes, 
                    channelids
                    )
            t = self.rantime()
            time.sleep(15 + t)
    #========================================================================================================================
    def run__bot__pray(self, tokens, group, tokentypes, channelids, prays):
        while True:
            if (self.active_bot and 
                self.pray_curse and 
                self.pray):
                self.bot_pray(
                    tokens, 
                    group, 
                    tokentypes, 
                    channelids, 
                    prays
                )
            t = self.rantime_2()
            time.sleep((5 * 60) + t)
    #========================================================================================================================
    def run__bot__curse(self,tokens, group, tokentypes, channelids, curses):
        while True:
            if (self.active_bot and 
                self.pray_curse and 
                self.curse):
                self.bot_curse(
                    tokens, 
                    group, 
                    tokentypes, 
                    channelids, 
                    curses
                )
            t = self.rantime_2()
            time.sleep((5 * 60) + t)
    #========================================================================================================================
    def run__bot__upgrade(self, tokens, group, tokentypes, channelids):
        while True:
            if (self.active_bot and 
                ani_enable):
                self.upgradeall(
                    tokens, 
                    group, 
                    tokentypes, 
                    channelids
                )
            t = self.rantime_2()
            time.sleep((10 * 60) + t)
    #========================================================================================================================
    def run__bot__gamble(self, tokens, group, tokentypes, channelids):
        while True:
            if self.active_bot:
                if slots_enable:
                    self.bot_slots(
                        tokens, 
                        group, 
                        tokentypes, 
                        channelids
                    )
                elif coinflip_enable:
                    self.bot_coinflip(
                        tokens, 
                        group, 
                        tokentypes, 
                        channelids
                    )
            t = self.rantime()
            time.sleep(15 + t)
    """░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░████████╗
        ██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
        ██║░░╚═╝███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║░░░██║░░░
        ██║░░██╗██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║░░░██║░░░
        ╚█████╔╝██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
        ░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░"""
    def catpcha_recover(self, token, group, tokentype, channelid, dmchannelid, userid):
        time.sleep(2)
        run__bot__captcha_thread = threading.Thread(
            target=self.run__bot__captcha, 
            args=(
                token, 
                group, 
                tokentype, 
                channelid, 
                dmchannelid, 
                userid
            )
        )
        run__bot__captcha_thread.start()
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            magenta(" [Captcha Bot]") +
            green(f" Captcha has been fixed! ⚠️")
        )
        pass
    def run__bot__captcha(self, token, group, tokentype, channelid, dmchannelid, userid):
        response = requests.get(
                f"https://canary.discord.com/api/v9/users/@me",
                headers={"authorization": token}
            )
        body = response.json()
        username = body["username"]
        while True:
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
                        f.close()
                    id_captcha_dm = data[userid]["id_captcha_dm"]
                    bodydm = responsedm.json()
                    captcha_md= bodydm[0]["id"]
                    contentmd = bodydm[0]["content"]
                    if  (("Are you a real human?" in  contentmd) and 
                        (captcha_md != id_captcha_dm)):
                        data[userid]["id_captcha_dm"] = captcha_md
                        with open(file_cache, "w", encoding="utf-8") as write_id_dm:
                            json.dump(data, write_id_dm, indent=4)
                            write_id_dm.close()
                        print(
                            red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                            magenta(f"[{tokentype}] ") +
                            red(f"Chat Captcha! ❌")
                        )
                        self.active_bot = False
                        self.task_bot_active = False
                        self.captcha_notification = True
                        if self.main_thread.is_alive():
                            self.main_thread.kill()
                        time.sleep(0.001)
                        notification_bot = threading.Thread(
                                target=self.notification_def, 
                                args=(username,),
                                name=(f"notification_{username}",
                                )
                            )
                        notification_bot.start()
                        notification_bot.join()
                    body = response.json()
                    for bodycount in body:
                        content = bodycount["content"]
                        idowo = bodycount["author"]["id"]
                        captcha_chat = bodycount["id"]
                        #(idowo == "408785106942164992") and 
                        if ((
                            ("captcha" in content) or 
                            (f"⚠️ **|** <@{userid}>" in content) or 
                            (f"⚠️ **|**" in content)) and 
                            (self.read_id(captcha_chat, userid, "id_captcha"))
                            ):
                            print(
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ") +
                                magenta(f"[{group}] ") +
                                magenta(f"[{tokentype}] ") +
                                red(f"Chat Captcha! ❌")
                            )
                            self.active_bot = False
                            self.task_bot_active = False
                            self.captcha_notification = True
                            if self.main_thread.is_alive():
                                self.main_thread.kill()
                            time.sleep(0.001)
                            for bodycounts in body:
                                self.add_id_to_cache(bodycounts["id"], userid, "id_captcha")
                            notification_bot = threading.Thread(
                                target=self.notification_def, 
                                args=(username,),
                                name=(f"notification_{username}",
                                )
                            )
                            notification_bot.start()
                            notification_bot.join()
                elif ((response.status_code == 401) or 
                      (responsedm.status_code == 401)):
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{group}]") +
                        magenta(f" [{tokentype}]") +
                        magenta(" [Captcha Bot]") +
                        red(f" 401: Unauthorized! ⚠️")
                    )
            except (KeyError, json.JSONDecodeError) as e:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta(f" [{group}]") +
                    magenta(f" [{tokentype}]") +
                    magenta(" [Captcha Bot]") +
                    red(f" Error while checking captcha! ⚠️")
                )
                self.catpcha_recover(
                    token, 
                    group, 
                    tokentype, 
                    channelid, 
                    dmchannelid, 
                    userid
                )
                break
            time.sleep(0.5)
    #========================================================================================================================
    def _main_(self):
        bot_main_thread = threading.Thread(
            target=self.bot_main, 
            args=(self.group,)
        )
        bot_main_thread.start()
        time.sleep(0.1)
        if self.extratokencheck:
            bot_extra_thread = threading.Thread(
                target=self.bot_extra, 
                args=(self.group,)
            )
            bot_extra_thread.start()
        time.sleep(10)
        run__bot__hunt__and__battle_thread = threading.Thread(
            target=self.run__bot__hunt__and__battle, 
            args=(
                self.main_token,self.group,
                "Main  Token", 
                self.main_channelid, 
                self.main_serverid
            )
        )
        run__bot__animal_thread = threading.Thread(
            target=self.run__bot__animal, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid, 
                ani_type
            )
        )
        run__bot__say__owo_thread = threading.Thread(
            target=self.run__bot__say__owo, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid
            )
        )
        run__bot__pray_thread = threading.Thread(
            target=self.run__bot__pray, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid, 
                pray
            )
        )
        run__bot__curse_thread = threading.Thread(
            target=self.run__bot__curse, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid, 
                curse
            )
        )
        run__bot__upgrade_thread = threading.Thread(
            target=self.run__bot__upgrade, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid
            )
        )
        run__bot__gamble_thread = threading.Thread(
            target=self.run__bot__gamble, 
            args=(
                self.main_token,
                self.group, 
                "Main  Token", 
                self.main_channelid
            )
        )
        run__bot__getquests_thread = threading.Thread(
            target=self.getquests, 
            args=(
                self.main_token, 
                self.extra_token, 
                self.main_id, 
                self.main_questchannelid,
                self.group, 
                "Main  Token", 
                self.main_serverid,
            )
        )
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
        if self.extratokencheck:
            extra__run__bot__hunt__and__battle_thread = threading.Thread(
                target=self.run__bot__hunt__and__battle, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid, 
                    self.extra_serverid
                )
            )
            extra__run__bot__animal_thread = threading.Thread(
                target=self.run__bot__animal,
                 args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid, 
                    ani_type
                )
            )
            extra__run__bot__say__owo_thread = threading.Thread(
                target=self.run__bot__say__owo, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid
                )
            )
            extra__run__bot__pray_thread = threading.Thread(
                target=self.run__bot__pray, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid, 
                    pray
                )
            )
            extra__run__bot__curse_thread = threading.Thread(
                target=self.run__bot__curse, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid, 
                    curse
                )
            )
            extra__run__bot__upgrade_thread = threading.Thread(
                target=self.run__bot__upgrade, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid
                )
            )
            extra__run__bot__gamble_thread = threading.Thread(
                target=self.run__bot__gamble, 
                args=(
                    self.extra_token,
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid
                )
            )
            extra__run__bot__getquests_thread = threading.Thread(
                target=self.getquests, 
                args=(
                    self.extra_token, 
                    self.main_token, 
                    self.extra_id, 
                    self.extra_questchannelid, 
                    self.group, 
                    "Extra Token", 
                    self.extra_serverid,
                )
            )
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

    def controller_recover(self, token, channelid, userid, group, tokentype):
        time.sleep(2)
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
            magenta(f" [{group}]") +
            magenta(f" [{tokentype}]") +
            magenta(" [Controller Bot]") +
            green(f" Control has been fixed ✅")
        )
        controller_thread1 = threading.Thread(
            target=self.controller, 
            args=(
                token, 
                channelid, 
                userid, 
                group, 
                tokentype
            )
        )
        controller_thread1.start()

    def controller(self, token, channelid, userid, group, tokentype):
        def send_mess(mess):
            print(
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                magenta(f" [{group}]") +
                blue(f" {mess}")
                )
        while True:
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
                        if (((id == self.main_id) or 
                             (id == self.extra_id)) and
                            (self.read_id(id_bot_message, userid, "id_activate"))):
                            content = bodycount["content"]
                            if ((content == f"{bot_prefix}stop") and
                                (self.task_bot_active)):
                                for bodycounts in body:
                                    self.add_id_to_cache(bodycounts["id"], userid, "id_activate")
                                self.active_bot = False
                                self.task_bot_active = False
                                send_mess('Bot stopped! ✅')
                                if self.main_thread.is_alive():
                                    self.main_thread.kill()
                            elif ((content == f"{bot_prefix}run") and
                                  (not self.task_bot_active)):
                                    for bodycounts in body:
                                        self.add_id_to_cache(bodycounts["id"], userid, "id_activate")
                                    self.main_thread = multiprocessing.Process(target=self._main_)
                                    self.main_thread.start()
                                    self.captcha_notification = False
                                    self.task_bot_active = True
                                    self.active_bot = True
                                    send_mess('Bot is Runing!')
                            elif (content == f"{bot_prefix}reset"):
                                for bodycounts in body:
                                    self.add_id_to_cache(bodycounts["id"], userid, "id_activate")
                                self.active_bot = False
                                self.task_bot_active = False
                                if self.main_thread.is_alive():
                                    self.main_thread.kill()
                                time.sleep(0.2)
                                self.main_thread = multiprocessing.Process(target=self._main_)
                                self.main_thread.start()
                                self.captcha_notification = False
                                self.task_bot_active = True
                                self.active_bot = True
                                send_mess('Bot reseted!')
                except json.JSONDecodeError as e:
                    print(e)
                    print(
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                        magenta(f" [{group}]") +
                        magenta(f" [{tokentype}]") +
                        magenta(" [Controller Bot]") +
                        red(f" Error while Control! ⚠️")
                    )
                    self.controller_recover(token, channelid, userid, group, tokentype)
                    break
            elif response.status_code == 401:
                print(
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") +
                    magenta(f" [{group}]") +
                    magenta(f" [{tokentype}]") +
                    magenta(" [Controller Bot]") +
                    red(f" 401: Unauthorized! ⚠️")
                )
            time.sleep(0.5)
    def ___main___(self, group, data):
        self.group = str(group)
        main                       = data['main']
        self.main_token            = str(main['token'])
        self.main_id               = str(token_decode(self.main_token))
        self.main_serverid         = str(main['serverid'])
        self.main_channelid        = str(main['channelid'])
        self.main_questchannelid   = str(main['questchannelid'])
        self.main_dmchannelid      = str(main['owo_dmschannelid'])

        extra                      = data['extra']
        self.extra_token           = str(extra['token'])
        self.extra_id              = str(token_decode(self.extra_token))
        self.extra_serverid        = str(extra['serverid'])
        self.extra_channelid       = str(extra['channelid'])
        self.extra_questchannelid  = str(extra['questchannelid'])
        self.extra_dmchannelid     = str(extra['owo_dmschannelid'])   
        if ((self.extra_token == self.main_token) or (self.extra_token == "")):
            self.extratokencheck = False
        self.starttime = time.time()
        self.main_thread = multiprocessing.Process(target=self._main_)
        self.main_thread.start()
        time.sleep(3.5)
        run__bot__captcha_thread = threading.Thread(
            target=self.run__bot__captcha, 
            args=(
                self.main_token, 
                self.group, 
                "Main  Token", 
                self.main_channelid, 
                self.main_dmchannelid, 
                self.main_id
            )
        )
        controller_thread1 = threading.Thread(
            target=self.controller, 
            args=(
                self.main_token, 
                self.main_channelid, 
                self.main_id,
                self.group, 
                "Main  Token"
            )
        )
        run__bot__captcha_thread.start()
        controller_thread1.start()
        if self.extratokencheck:
            extra__run__bot__captcha_thread = threading.Thread(
                target=self.run__bot__captcha, 
                args=(
                    self.extra_token, 
                    self.group, 
                    "Extra Token", 
                    self.extra_channelid, 
                    self.extra_dmchannelid, 
                    self.extra_id
                )
            )
            controller_thread2 = threading.Thread(
                target=self.controller, 
                args=(
                    self.extra_token, 
                    self.extra_channelid, 
                    self.extra_id, 
                    self.group, 
                    "Extra Token"
                )
            )
            extra__run__bot__captcha_thread.start()
            controller_thread2.start()
if __name__ == '__main__':
    check = threading.Thread(target= checkversion)
    check.start()
    install = threading.Thread(target= install_update)
    install.start()
    for i in range(number_of_groups):
        i += 1
        Process_api = threading.Thread(
            target= API().___main___,
            args=(
                f"Group {i}", 
                cfgs[f"group_{i}"]
            ), 
            name=f"Group_{i}"
        )
        Process_api.start()
        time.sleep(0.05)

    while True:
        """keep alive"""
        time.sleep(9**9)
