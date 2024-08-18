import os
import math
import time
import json
import queue
import random
import base64
import hashlib
import datetime
import threading
import multiprocessing
from file import phrases, actvar, gamblevar

start_time = time.time()
request_count = 0

version = "v3-0.1.fb3b77c087e7"


try:
    import requests
    import psutil
    import pytz
    from blessed import Terminal
    from notifypy import Notify
except ModuleNotFoundError:
    print("Please Run: ! Create venv and Install lib.bat")

    time.sleep(2)
    exit()

red = Terminal().red
green = Terminal().green
blue = Terminal().blue
yellow = Terminal().yellow
magenta = Terminal().magenta

# Get the current working directory
current_dir = os.getcwd()

# Join the current directory with the filename
file_config = os.path.join(current_dir, "data\\setting_config.json")
file_cache = os.path.join(current_dir, "data\\cache.json")
file_update = os.path.join(current_dir, "core\\!Update.py")
# Call cfg.json file
with open(file_config, "r", encoding="utf-8") as a:
    cfgs = json.load(a)
    a.close()


def clear_screen():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For macOS and Linux
    else:
        _ = os.system("clear")


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


"""▄▀█ █▀▀ █▀▀ █▀▀ █▀ █▀   ▀█▀ █░█ █▀▀   █▀ █▀▀ ▀█▀ ▀█▀ █ █▄░█ █▀▀ █▀
   █▀█ █▄▄ █▄▄ ██▄ ▄█ ▄█   ░█░ █▀█ ██▄   ▄█ ██▄ ░█░ ░█░ █ █░▀█ █▄█ ▄█"""
try:
    setting = cfgs["settings"]
    prefix = str(setting["owo_prefix"])
    bot_prefix = str(setting["control_prefix"])
    slash_command = boolean_conv(setting["slash_command"])
    sayowo = boolean_conv(setting["sayowo"])
    pray = boolean_conv(setting["pray"])
    curse = boolean_conv(setting["curse"])
    hunt = boolean_conv(setting["hunt"])
    battle = boolean_conv(setting["battle"])
    autoquest = boolean_conv(setting["autoquest"])
    randommess = boolean_conv(setting["randommess"])
    banbypass = boolean_conv(setting["banbypass"])
    # ========================================================================================================================
    inventory = setting["inventory"]
    inventorycheck = boolean_conv(inventory["inventorycheck"])
    gemcheck = boolean_conv(inventory["gemcheck"])
    lootboxcheck = boolean_conv(inventory["lootboxcheck"])
    fabledlootboxcheck = boolean_conv(inventory["fabledlootboxcheck"])
    cratecheck = boolean_conv(inventory["cratecheck"])
    # ========================================================================================================================
    animals = setting["animals"]
    ani_enable = boolean_conv(animals["enable"])
    ani_type = str(animals["type"])
    animaltype = animals["animaltype"]
    common = boolean_conv(animaltype["common"])
    uncommon = boolean_conv(animaltype["uncommon"])
    rare = boolean_conv(animaltype["rare"])
    epic = boolean_conv(animaltype["epic"])
    mythical = boolean_conv(animaltype["mythical"])
    patreon = boolean_conv(animaltype["patreon"])
    cpatreon = boolean_conv(animaltype["cpatreon"])
    legendary = boolean_conv(animaltype["legendary"])
    gem = boolean_conv(animaltype["gem"])
    bot = boolean_conv(animaltype["bot"])
    distorted = boolean_conv(animaltype["distorted"])
    fabled = boolean_conv(animaltype["fabled"])
    special = boolean_conv(animaltype["special"])
    hidden = boolean_conv(animaltype["hidden"])
    # ========================================================================================================================
    upgradeautohunt = setting["upgradeautohunt"]
    upg_enable = boolean_conv(upgradeautohunt["enable"])
    upg_type = str(upgradeautohunt["upgtype"])
    # ========================================================================================================================
    gamble = setting["gamble"]

    coinflip = gamble["coinflip"]
    coinflip_enable = boolean_conv(coinflip["enable"])
    coinflip_amount = P_str_int_conv(coinflip["amount"])

    slots = gamble["slots"]
    slots_enable = boolean_conv(slots["enable"])
    slots_amount = P_str_int_conv(slots["amount"])

    # ========================================================================================================================
except (IndexError, KeyError) as e:
    print(red("Check your setting_config.json there some missing"))
    time.sleep(1)
    os._exit(0)
time.sleep(1.5)
notification = Notify()
process = psutil.Process()
queues = queue.Queue()
lock = threading.Lock()
is_reading = False


def install_update():
    update = requests.get(
        "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Update.py"
    )
    with open(file_update, "wb") as fu:
        fu.write(update.content)
        fu.close()

    # ========================================================================================================================


def checkversion():
    response = requests.get(
        "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/data/version"
    )
    versions = response.text.strip()
    if versions != version:
        print(red("New version detected"))
        time.sleep(3)
        os._exit(0)


"""███╗░░░███╗░█████╗░██╗███╗░░██╗  ██████╗░███████╗███████╗
   ████╗░████║██╔══██╗██║████╗░██║  ██╔══██╗██╔════╝██╔════╝
   ██╔████╔██║███████║██║██╔██╗██║  ██║░░██║█████╗░░█████╗░░
   ██║╚██╔╝██║██╔══██║██║██║╚████║  ██║░░██║██╔══╝░░██╔══╝░░
   ██║░╚═╝░██║██║░░██║██║██║░╚███║  ██████╔╝███████╗██║░░░░░
   ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░░░░"""


class ____API____:
    def __init__(self):
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
        self.bot_status = True

        if self.curse and self.pray:
            self.pray = True
            self.curse = False

        self.bot_main_thread = None
        self.run__bot__getquests_thread = None
        self.run__bot__say__owo_thread = None
        self.run__bot__hunt__and__battle_thread = None
        self.run__bot__pray_thread = None
        self.run__bot__curse_thread = None
        self.run__bot__animal_thread = None
        self.run__bot__upgrade_thread = None
        self.run__bot__gamble_thread = None

        self.bot_extra_thread = None
        self.extra__run__bot__getquests_thread = None
        self.extra__run__bot__say__owo_thread = None
        self.extra__run__bot__hunt__and__battle_thread = None
        self.extra__run__bot__pray_thread = None
        self.extra__run__bot__curse_thread = None
        self.extra__run__bot__animal_thread = None
        self.extra__run__bot__upgrade_thread = None
        self.extra__run__bot__gamble_thread = None

        self.print_main_user = blue(f"Main User: {None}")
        self.print_extra_user = blue(f"Extra User: {None}")

        self.print_send_mess_control_bot = red(
            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
        ) + yellow(" Bot is starting!")

        self.print_captcha_check_main = red(
            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
        ) + yellow(f" Captcha Start")
        self.print_captcha_check_extra = red(
            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
        ) + yellow(f" Captcha Start")

        self.print_cl = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + red(
            f" Checklist ❌"
        )

        if sayowo:
            self.print_say_owo = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" OwO ✅")
        if not sayowo:
            self.print_say_owo = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(" OwO ❌")

        if hunt:
            self.print_h = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Hunt ✅")
        if not hunt:
            self.print_h = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + red(
                " Hunt ❌"
            )

        if battle:
            self.print_b = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Battle ✅")
        if not battle:
            self.print_b = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + red(
                " Battle ❌"
            )

        if ani_enable:
            self.print_bot_animal = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(f" Animals ✅")
        if not ani_enable:
            self.print_bot_animal = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(f" Animals ❌")

        if self.pray:
            self.print_pray = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(f" Pray ✅")
        if not self.pray:
            self.print_pray = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(f" Pray ❌")

        if self.curse:
            self.print_curse = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(f" Curse ✅")
        if not self.curse:
            self.print_curse = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(f" Curse ❌")

        if coinflip_enable:
            self.print_cf = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Gamble / CoinFlip ✅")
        if not coinflip_enable:
            self.print_cf = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(" Gamble / CoinFlip ❌")

        if slots_enable:
            self.print_s = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Gamble / slots ✅")
        if not slots_enable:
            self.print_s = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + red(
                " Gamble / slots ❌"
            )

        if upg_enable:
            self.print_upg = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Upgrade AutoHunt ✅")
        if not upg_enable:
            self.print_upg = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(" Upgrade AutoHunt ❌")

        if inventorycheck:
            self.print_inv = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" inventory checking ✅")
        if not inventorycheck:
            self.print_inv = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(" inventory checking ❌")

        if lootboxcheck or fabledlootboxcheck or cratecheck:
            self.print_box = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(f" box ✅")
        if (not lootboxcheck) and (not fabledlootboxcheck) and (not cratecheck):
            self.print_box = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(f" box ❌")

        if gemcheck:
            self.print_gem = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(" Gem ✅")
        if not gemcheck:
            self.print_gem = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(" Gem ❌")

        if autoquest:
            self.print_quest = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + green(f" quest 1: {None} quest 2: {None} quest 3: {None}")
        if not autoquest:
            self.print_quest = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + red(f" Auto quest off ❌")

    # ========================================================================================================================

    # ========================================================================================================================

    def add_user(self, user_ids, thread_name):
        global is_reading

        # waitting before read/write file
        queues.put(thread_name)
        while True:
            if queues.get() == thread_name:
                break
            queues.put(thread_name)

        # lock thread file to read
        with lock:
            is_reading = True
            try:
                with open(file_cache, "r") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                data = {}
            caches = data
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
                        "id_10": "0000000000000000000000",
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
                        "id_10": "0000000000000000000000",
                    },
                    "id_quest_battle": {
                        "id_1": "0000000000000000000000",
                        "id_2": "0000000000000000000000",
                        "id_3": "0000000000000000000000",
                        "id_4": "0000000000000000000000",
                        "id_5": "0000000000000000000000",
                        "id_6": "0000000000000000000000",
                        "id_7": "0000000000000000000000",
                        "id_8": "0000000000000000000000",
                        "id_9": "0000000000000000000000",
                        "id_10": "0000000000000000000000",
                    },
                }
            with open(file_cache, "w") as f:
                json.dump(caches, f, indent=4)
            is_reading = False

    def read_id(self, id_to_check, userid, path, thread_name):
        global is_reading

        # waitting before read/write file
        queues.put(thread_name)

        while True:
            if queues.get() == thread_name:
                break
            queues.put(thread_name)

        # lock thread file to read
        with lock:
            is_reading = True
            with open(file_cache, "r", encoding="utf-8") as f:
                data = json.load(f)
                f.close()
            is_reading = False
            id_captcha = data[userid][path]
            for value in id_captcha.values():
                if value == id_to_check:
                    return False
            return True

    def add_id_to_cache(self, new_id, userid, path, thread_name):
        global is_reading

        # waitting before read/write file
        queues.put(thread_name)

        while True:
            if queues.get() == thread_name:
                break
            queues.put(thread_name)

        # lock thread file to read
        with lock:
            is_reading = True
            with open(file_cache, "r") as read_data:
                data = json.load(read_data)
            if userid in data:
                id_quest_battle = data[userid].setdefault(path, {})
                id_list = list(id_quest_battle.values())
                id_list.insert(0, new_id)
                id_list = id_list[:10]
                data[userid][path] = {f"id_{i+1}": v for i, v in enumerate(id_list)}
                with open(file_cache, "w") as write_data:
                    json.dump(data, write_data, indent=4)
                    write_data.close()
                is_reading = False

    # ========================================================================================================================

    def notification_def(self, username, tokentype):
        notification = Notify()
        noti_count = 11
        while noti_count > -1:
            if self.captcha_notification == True:
                noti_count = noti_count - 1
                if noti_count > 0:
                    noti_count_str = str(noti_count)
                    notification.title = f"[{username}] Captcha Detected!"
                    notification.message = f"SOLVE CAPTCHA AND RESTART BOT\nyou only have {
                        noti_count_str}min left"
                    notification.icon = "data/owo.ico"
                    print_ = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                        + magenta(f" [{username}]")
                        + red(f" Time left {noti_count} Min! ⚠️")
                    )
                    if tokentype == "Extra Token":
                        self.print_captcha_check_extra = print_
                    else:
                        self.print_captcha_check_main = print_
                    notification.send()
                else:
                    noti_count_str = str(noti_count)
                    notification.title = f"[{username}] Captcha Detected!"
                    notification.message = f"You are Banned by OwO"
                    notification.icon = "data/owo.ico"
                    print_ = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                        + magenta(f" [{username}]")
                        + red(f" Time left {noti_count} Min! ⚠️")
                    )
                    if tokentype == "Extra Token":
                        self.print_captcha_check_extra = print_
                    else:
                        self.print_captcha_check_main = print_
                    notification.send()
                    time.sleep(3)
                    os._exit(0)
            else:
                break
            time.sleep(60)

    # ========================================================================================================================

    def rantime(self):
        rdt = random.randint(1, 5) + round(random.uniform(0, 1), 3)
        return rdt

    # ========================================================================================================================

    def rantime_2(self):
        rdt = random.randint(5, 30) + round(random.uniform(0, 1), 3)
        return rdt

    # ========================================================================================================================

    def nonce(self):
        rannonce = 1098393848631590 + math.floor(round(random.uniform(0, 1), 3) * 9999)
        return rannonce

    # ========================================================================================================================

    def autoseed(self, token):
        seed = hashlib.sha256(
            f"seedaccess-entropyverror-apiv10.{token}".encode()
        ).digest()
        return seed

    # ========================================================================================================================

    def generate_random_128bit_hex(self):
        "Tạo một chuỗi hexa ngẫu nhiên 128-bit."
        random_bytes = os.urandom(16)  # 16 byte = 128 bit
        return random_bytes.hex()

    # ========================================================================================================================

    def bot_owo(self, token, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": "owo",
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_say_owo = red(
            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
        ) + blue(" OwO ✅")

    # ========================================================================================================================

    def bot_hunt(self, token, timehunt, tokentype, channelid, session_id, serverid):
        global request_count
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
                            "integration_types": [0],
                            "global_popularity_rank": 1,
                            "options": [],
                            "description_localized": "Hunt for some animals!",
                            "name_localized": "hunt",
                        },
                        "attachments": [],
                    },
                    "nonce": self.nonce(),
                    "analytics_location": "slash_ui",
                },
            )
            request_count += 1
            pass
        else:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + "h",
                    "nonce": self.nonce(),
                    "tts": False,
                    "flags": 0,
                },
            )
            request_count += 1
        self.print_h = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            " Hunt ✅ (" + str(timehunt) + " ms)"
        )

    # ========================================================================================================================

    def bot_battle(self, token, timebattle, tokentype, channelid, session_id, serverid):
        global request_count
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
                                    "name_localized": "user",
                                }
                            ],
                            "integration_types": [0],
                            "global_popularity_rank": 2,
                            "description_localized": "Fight with your team of animals!",
                            "name_localized": "battle",
                        },
                        "attachments": [],
                    },
                    "nonce": self.nonce(),
                    "analytics_location": "slash_ui",
                },
            )
            request_count += 1
        else:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": prefix + "b",
                    "nonce": self.nonce(),
                    "tts": False,
                    "flags": 0,
                },
            )
            request_count += 1
        self.print_b = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            " Battle ✅ (" + str(timebattle) + " ms)"
        )

    # ========================================================================================================================

    def get_ran_mess(self):
        grm = random.randint(0, (len(phrases) - 1))
        return phrases[grm]

    # ========================================================================================================================

    def get_ran_act(self):
        gra = random.randint(0, (len(actvar) - 1))
        return actvar[gra]

    # ========================================================================================================================

    def get_ran_gamble(self):
        gra = random.randint(0, (len(gamblevar) - 1))
        return gamblevar[gra]

    # ========================================================================================================================

    def ran_message(self, token, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": self.get_ran_mess(),
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1

    # ========================================================================================================================

    def bot_animals(self, token, tokentype, channelid, ani_type):
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
        rank = [
            "c",
            "u",
            "r",
            "e",
            "m",
            "p",
            "cp",
            "l",
            "g",
            "b",
            "d",
            "f",
            "s",
            "h",
        ]
        for e, a in zip(ranks, rank):
            if animaltype["all"]:
                animaltypes = "all"
                break
            elif animaltype[e]:
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
            global request_count
            request_count += 1
            self.print_bot_animal = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + blue(f" Animals ✅ / Type: {ani_type}")
        else:
            self.print_bot_animal = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + blue(f" Animals ❌ / Error: Incorrect Type")

    # ========================================================================================================================

    def bot_pray(self, token, tokentype, channelid, pray):
        ct = None
        if pray:
            if tokentype == "Extra Token":
                ct = prefix + "pray"
                bt = "Pray"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif pray == "main":
            if tokentype == "Extra Token":
                ct = prefix + "pray <@" + self.main_id + ">"
                bt = "Pray to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif pray == "extra":
            if tokentype == "Extra Token":
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
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_pray = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            f" {bt} ✅"
        )

    # ========================================================================================================================

    def bot_curse(self, token, tokentype, channelid, curse):
        ct = None
        if curse:
            if tokentype == "Extra Token":
                ct = prefix + "curse"
                bt = "Curse"
            else:
                ct = prefix + "curse"
                bt = "Curse"
        elif curse == "main":
            if tokentype == "Extra Token":
                ct = prefix + "curse <@" + self.main_id + ">"
                bt = "Curse to main"
            else:
                ct = prefix + "pray"
                bt = "Pray"
        elif curse == "extra":
            if tokentype == "Extra Token":
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
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_curse = red(
            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
        ) + blue(f" {bt} ✅")

    # ========================================================================================================================

    def cookie(self, token, tokentype, channelid):
        if tokentype == "Extra Token":
            ct = prefix + "cookie <@" + self.main_id + ">"
        else:
            if self.extratokencheck:
                ct = prefix + "cookie <@" + self.extra_id + ">"
            else:
                ct = prefix + "cookie <@408785106942164992>"
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": ct,
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + green(" Cookie ✅")
        )

    # ========================================================================================================================

    def daily(self, token, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "daily",
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        print(
            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + green(" Daily ✅")
        )

    # ========================================================================================================================

    def bot_coinflip(self, token, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "cf " + coinflip_amount,
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_cf = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + green(
            " Gamble / CoinFlip ✅ / Amount: " + coinflip_amount
        )

    # ========================================================================================================================

    def bot_slots(self, token, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "s " + slots_amount,
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_s = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + green(
            " Gamble / slots ✅ / Amount: " + slots_amount
        )

    # ========================================================================================================================

    def upgradeall(self, token, tokentype, channelid):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "upg " + upg_type + " all",
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_upg = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            " Upgrade AutoHunt ✅"
        )

    """▒█▀▀█ █░░█ █▀▀ █▀▀ ▀▀█▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 ▒█░░░ ░▀░ █▀▀ ▀▀█▀▀
    ▒█░▒█ █░░█ █▀▀ ▀▀█ ░░█░░ 　 █▄▄█ █░░█ █░░█ 　 ▒█░░░ ▀█▀ ▀▀█ ░░█░░
    ░▀▀█▄ ░▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░"""

    def dailycount(self, userid, thread_name, tokentype):
        global is_reading

        # waitting before read/write file
        queues.put(thread_name)

        while True:
            if queues.get() == thread_name:
                break
            queues.put(thread_name)

        # lock thread file to read
        with lock:
            is_reading = True
            with open(file_cache, "r", encoding="utf-8") as c:
                data = json.load(c)
                c.close()
            base_time = datetime.time(7, 0, 0)
            day_base = datetime.datetime.strptime(
                data[userid]["day_daily"], "%Y-%m-%d"
            ).date()
            base_datetime = datetime.datetime.combine(day_base, base_time)
            base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
            now_utc = datetime.datetime.now(pytz.utc)
            if (base_datetime_utc < now_utc) and (data[userid]["daily"] == "done"):
                data[userid]["daily"] = "ready"
                with open(file_cache, "w", encoding="utf-8") as s:
                    json.dump(data, s, indent=4)
                    s.close()
                    dailycheckers = "ready"
            elif data[userid]["daily"] == "ready":
                dailycheckers = "ready"
            else:
                dailycheckers = "done"
                self.print_cl = red(
                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                ) + blue(f" Checklist done📜")
            is_reading = True
            return dailycheckers

    def checklist(self, token, tokentype, channelid, userid):
        if self.dailycount(userid, f"daily_{userid}", tokentype) == "ready":
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
                json={
                    "content": f"{prefix}cl",
                    "nonce": self.nonce(),
                    "tts": False,
                    "flags": 0,
                },
            )
            global request_count
            request_count += 1
            self.print_cl = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + blue(f" Sending Checklist📜...")
            time.sleep(0.5)
            while True:
                response = requests.get(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages?limit=1",
                    headers={"authorization": token},
                )
                request_count += 1
                try:
                    body = response.json()
                    author = body[0]["author"]
                    id = author["id"]
                    if (id == "408785106942164992") and (
                        "Checklist" in body[0]["embeds"][0]["author"]["name"]
                    ):
                        embeds = body[0]["embeds"]
                        cont = embeds[0]["description"]
                        self.print_cl = red(
                            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                        ) + blue(f" Getting Checklist🔎...")
                        if "☑️ 🎉" in cont:
                            global is_reading

                            # waitting before read/write file
                            queues.put(f"write_daily_{userid}")

                            while True:
                                if queues.get() == (f"write_daily_{userid}"):
                                    break
                                queues.put(f"write_daily_{userid}")

                            # lock thread file to read
                            with lock:
                                is_reading = True
                                with open(file_cache, "r", encoding="utf-8") as d:
                                    data = json.load(d)
                                    d.close()
                                now_utc = datetime.datetime.now(pytz.utc)
                                data[userid]["day_daily"] = now_utc.strftime("%Y-%m-%d")
                                data[userid]["daily"] = "done"
                                with open(file_cache, "w", encoding="utf-8") as e:
                                    json.dump(data, e, indent=4)
                                    e.close()
                                is_reading = False

                            return "checklist completed"
                        if "⬛ 🎁" in cont:
                            self.daily(token, tokentype, channelid)
                        if "⬛ 🍪" in cont:
                            self.cookie(token, tokentype, channelid)
                        if "⬛ 📝" in cont:
                            self.print_cl = red(
                                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                            ) + blue(f" YOUR DAILY VOTE IS AVAILABLE!")
                        break
                    else:
                        continue
                except (KeyError, json.JSONDecodeError) as e:
                    if (
                        isinstance(e, IndexError)
                        and str(e) == "list index out of range"
                    ):
                        self.print_cl = red(
                            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                        ) + red(" Unable to get Checklist❗")
                        return
                    else:
                        self.print_cl = red(
                            f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                        ) + red(" Unable to get Checklist❗")
                time.sleep(0.05)

    # ========================================================================================================================

    def checkinv(self, token, channelid, tokentype):
        if gemcheck:
            response = requests.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": token},
            )
            global request_count
            request_count += 1
            body = response.json()
            cont = body[0]["content"]
            if "You found:" in cont or "and caught a" in cont:
                collection = ["alulu"]
                self.print_inv = red(
                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                ) + blue(" inventory checking 🔍")
                if "gem1" not in cont:
                    collection.append("huntgem")
                if "gem3" not in cont:
                    collection.append("empgem")
                if "gem4" not in cont:
                    collection.append("luckgem")
                if "gem1" in cont and "gem3" in cont and "gem4" in cont:
                    self.getinv(token, channelid, tokentype, "nogem", ["nocollection"])
                else:
                    self.getinv(token, channelid, tokentype, "gemvar", collection)
        else:
            self.print_inv = red(
                f"{datetime.datetime.now().strftime('%H:%M:%S')}"
            ) + yellow(" inventory checking 🔍")
            self.getinv(token, channelid, tokentype, "nogem", ["nocollection"])

    # ========================================================================================================================

    def getinv(self, token, channelid, tokentype, gemc, collectc):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "inv",
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        time.sleep(3)
        response = requests.get(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
        )
        request_count += 1
        body = response.json()
        cont = body[0]["content"]
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
                self.gemuse(token, gem, channelid, tokentype)

        if lootboxcheck:
            if "`050`" in cont:
                time.sleep(2)
                self.boxuse(token, "lb all", channelid, tokentype)

        if fabledlootboxcheck:
            if "`049`" in cont:
                time.sleep(2)
                self.boxuse(token, "lootbox fabled all", channelid, tokentype)

        if cratecheck:
            if "`100`" in cont:
                time.sleep(2)
                self.boxuse(token, "wc all", channelid, tokentype)

    # ========================================================================================================================

    def boxuse(self, token, box, channelid, tokentype):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + box,
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_box = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            f" {box} ✅"
        )

    # ========================================================================================================================

    def gemuse(self, token, gem, channelid, tokentype):
        requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            headers={"authorization": token},
            json={
                "content": prefix + "use " + gem,
                "nonce": self.nonce(),
                "tts": False,
                "flags": 0,
            },
        )
        global request_count
        request_count += 1
        self.print_gem = red(f"{datetime.datetime.now().strftime('%H:%M:%S')}") + blue(
            " Gem ✅"
        )

    # ========================================================================================================================

    def questprayme(self, tokenrd, useridst, channelid, pro1, pro2):
        np = (pro2 - pro1) + 1
        self.pray_curse = False
        for np in range(np, 0, -1):
            if self.active_bot:
                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": tokenrd},
                    json={
                        "content": prefix + f"pray <@{useridst}>",
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime_2()
                time.sleep(300 + t)
                if np <= 1:
                    self.quest = True
                    self.pray_curse = True

    # ========================================================================================================================

    def questcurseme(self, tokenrd, useridst, channelid, pro1, pro2):
        np = (pro2 - pro1) + 1
        self.pray_curse = False
        for np in range(np, 0, -1):
            if self.active_bot:
                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": tokenrd},
                    json={
                        "content": prefix + f"curse <@{useridst}>",
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime_2()
                time.sleep(300 + t)
                if np <= 1:
                    self.pray_curse = True
                    self.quest = True

    # ========================================================================================================================

    def questbattlefriend(
        self,
        tokenst,
        tokenrd,
        useridst,
        channelid,
        pro1,
        pro2,
        session_id,
        session_id2,
        serverid,
    ):
        np = (pro2 - pro1) + 1
        self.battle_hunt = False

        def get_id(token, channelid, userid):
            response = requests.get(
                f"https://discord.com/api/v9/channels/{
                    channelid}/messages?limit=10",
                headers={"authorization": token},
            )
            global request_count
            request_count += 1
            body = response.json()
            for bodycount in body:
                if bodycount["author"]["id"] == "408785106942164992":
                    if (
                        (
                            self.read_id(
                                bodycount["id"],
                                useridst,
                                "id_quest_battle",
                                f"quest_getid_{useridst}",
                            )
                        )
                        and (bodycount["content"] == f"<@{userid}>")
                        and (
                            bodycount["embeds"][0]["description"]
                            == "`owo ab` to accept the battle!\n`owo db` to decline the battle!"
                        )
                    ):
                        bodycount["id"]
                        self.add_id_to_cache(
                            bodycount["id"],
                            useridst,
                            "id_quest_battle",
                            f"quest_addid_{useridst}",
                        )
                        return bodycount["id"]
                else:
                    continue
                return False

        for np in range(np, 0, -1):
            global request_count
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
                                    {"type": 6, "name": "user", "value": useridst}
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
                                            "name_localized": "user",
                                        }
                                    ],
                                    "integration_types": [0],
                                    "global_popularity_rank": 2,
                                    "description_localized": "Fight with your team of animals!",
                                    "name_localized": "battle",
                                },
                                "attachments": [],
                            },
                            "nonce": self.nonce(),
                            "analytics_location": "slash_ui",
                        },
                    )
                    request_count += 1
                    time.sleep(3)
                    requests.post(
                        f"https://discord.com/api/v9/interactions",
                        headers={"authorization": tokenst},
                        json={
                            "type": 3,
                            "nonce": self.nonce(),
                            "guild_id": serverid,
                            "channel_id": channelid,
                            "message_flags": 0,
                            "message_id": get_id(tokenst, channelid, useridst),
                            "application_id": "408785106942164992",
                            "session_id": session_id2,
                            "data": {"component_type": 2, "custom_id": "battle_accept"},
                        },
                    )
                    request_count += 1
                    t = self.rantime()
                    time.sleep(15 + t)
                    if np <= 1:
                        self.battle_hunt = True
                        self.quest = True

                else:
                    requests.post(
                        f"https://discord.com/api/v9/channels/{
                            channelid}/messages",
                        headers={"authorization": tokenrd},
                        json={
                            "content": prefix + f"b <@{useridst}>",
                            "nonce": self.nonce(),
                            "tts": False,
                            "flags": 0,
                        },
                    )
                    request_count += 1
                    time.sleep(3)
                    requests.post(
                        f"https://discord.com/api/v9/channels/{
                            channelid}/messages",
                        headers={"authorization": tokenst},
                        json={
                            "content": prefix + "ab",
                            "nonce": self.nonce(),
                            "tts": False,
                            "flags": 0,
                        },
                    )
                    request_count += 1
                    t = self.rantime()
                    time.sleep(15 + t)
                    if np <= 1:
                        time.sleep(5)
                        self.battle_hunt = True
                        self.quest = True

    # ========================================================================================================================

    def questuseactionreceive(self, tokenrd, useridst, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if self.active_bot:

                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": tokenrd},
                    json={
                        "content": prefix + f"{self.get_ran_act()} <@" + useridst + ">",
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True

    # ========================================================================================================================

    def questuseactionreceive(self, tokenrd, useridst, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if self.active_bot:

                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": tokenrd},
                    json={
                        "content": prefix + f"{self.get_ran_act()} <@" + useridst + ">",
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True

    # ========================================================================================================================

    def questuseactiongive(self, token, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if self.active_bot:
                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": token},
                    json={
                        "content": prefix
                        + f"{self.get_ran_act()} <@408785106942164992>",
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime()
                time.sleep(5 + t)
                if np <= 1:
                    self.quest = True

    # ========================================================================================================================

    def questgamble(self, token, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if self.active_bot and ((not coinflip_enable) or (not slots_enable)):
                requests.post(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages",
                    headers={"authorization": token},
                    json={
                        "content": prefix + self.get_ran_gamble(),
                        "nonce": self.nonce(),
                        "tts": False,
                        "flags": 0,
                    },
                )
                global request_count
                request_count += 1
                t = self.rantime()
                time.sleep(15 + t)
                if np <= 1:
                    self.quest = True

    # ========================================================================================================================

    def questsayowo(self, token, channelid, pro1, pro2):
        np = pro2 - pro1
        for np in range(np, 0, -1):
            if (not sayowo) and self.active_bot:
                self.bot_owo(token, "OwO Quest", channelid)
                global request_count
                request_count += 1
                t = self.rantime()
                time.sleep(15 + t)
                if np <= 1:
                    self.quest = True

    # ========================================================================================================================

    def doquest(
        self,
        quests,
        tokenst,
        tokenrd,
        useridst,
        channelid,
        progress1,
        progress2,
        serverid,
    ):
        global quest
        if ("owo") in quests:
            quest = False
            if not sayowo:
                do_questsayowo = threading.Thread(
                    target=self.questsayowo,
                    args=(tokenst, channelid, int(progress1), int(progress2)),
                )
                return do_questsayowo.start()
        elif ("Gamble") in quests and ((not slots_enable) or (not coinflip_enable)):
            quest = False
            do_questgamble = threading.Thread(
                target=self.questgamble,
                args=(tokenst, channelid, int(progress1), int(progress2)),
            )
            return do_questgamble.start()
        elif ("action give") in quests:
            quest = False
            do_questuseactiongive = threading.Thread(
                target=self.questuseactiongive,
                args=(tokenst, channelid, int(progress1), int(progress2)),
            )
            return do_questuseactiongive.start()
        if self.extratokencheck:
            if "curse" in quests:
                quest = False
                do_questcurseme = threading.Thread(
                    target=self.questcurseme,
                    args=(tokenrd, useridst, channelid, int(progress1), int(progress2)),
                )
                return do_questcurseme.start()
            elif ("pray") in quests:
                quest = False
                do_questprayme = threading.Thread(
                    target=self.questprayme,
                    args=(tokenrd, useridst, channelid, int(progress1), int(progress2)),
                )
                return do_questprayme.start()
            elif ("Battle") in quests:
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
                        serverid,
                    ),
                )
                return do_questbattlefriend.start()
            elif ("action recive") in quests:
                quest = False
                do_questuseactionreceive = threading.Thread(
                    target=self.questuseactionreceive,
                    args=(tokenrd, useridst, channelid, int(progress1), int(progress2)),
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
            bcheckquest1 = (
                cont[0]["description"].split("**2. ")[1].split("Progress: [")[0]
            )
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
            ccheckquest1 = (
                cont[0]["description"].split("**3. ")[1].split("Progress: [")[0]
            )
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
        elif "Use an action command on someone" in quest:
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

    def timecount(self, userid, tokentype):
        global is_reading

        # waitting before read/write file
        queues.put(f"day_quest_{userid}")

        while True:
            if queues.get() == f"day_quest_{userid}":
                break
            queues.put(f"day_quest_{userid}")

        # lock thread file to read
        with lock:
            is_reading = True
            with open(file_cache, "r", encoding="utf-8") as h:
                data = json.load(h)
                h.close()
            cache_store = data[userid]
            base_time = datetime.time(7, 0, 0)
            day_base = datetime.datetime.strptime(
                cache_store[f"day_quest"], "%Y-%m-%d"
            ).date()
            base_datetime = datetime.datetime.combine(day_base, base_time)
            base_datetime_utc = base_datetime.replace(tzinfo=pytz.utc)
            now_utc = datetime.datetime.now(pytz.utc)
            if (base_datetime_utc < now_utc) and (data[userid]["quest"] == "done"):
                data[userid]["quest"] = "ready"
                with open(file_cache, "w", encoding="utf-8") as i:
                    json.dump(data, i, indent=4)
                    i.close()
                    questcheckers = "ready"
            elif data[userid]["quest"] == "ready":
                questcheckers = "ready"
            else:
                questcheckers = "done"
                self.print_quest = red(
                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                ) + green(f" Quest done ✅")
            is_reading = False
            return questcheckers

    def getquests(
        self,
        tokenst,
        tokenrd,
        useridst,
        channelid,
        tokentype,
        serverid,
    ):
        questchecker = self.timecount(useridst, tokentype)
        aquests = ""
        bquests = ""
        cquests = ""
        if (self.active_bot) and (questchecker == "ready"):
            requests.post(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers={"authorization": tokenst},
                json={
                    "content": f"{prefix}q",
                    "nonce": self.nonce(),
                    "tts": False,
                    "flags": 0,
                },
            )
            global request_count
            request_count += 1
            time.sleep(2)
            response = requests.get(
                f"https://discord.com/api/v9/channels/{
                    channelid}/messages?limit=1",
                headers={"authorization": tokenst},
            )
            request_count += 1
            try:
                body = response.json()
                cont = body[0]["embeds"]
                conts = cont[0]["description"]
                time.sleep(2)
                if "You finished all of your quests!" in cont[0]["description"]:
                    global is_reading
                    with open(file_cache, "r", encoding="utf-8") as j:
                        data = json.load(j)
                        j.close()
                    now_utc = datetime.datetime.now(pytz.utc) + datetime.timedelta(
                        days=1
                    )
                    data[useridst]["day_quest"] = now_utc.strftime("%Y-%m-%d")
                    data[useridst]["quest"] = "done"
                    with open(file_cache, "w", encoding="utf-8") as k:
                        json.dump(data, k, indent=4)
                        k.close()

                    self.print_quest = red(
                        f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                    ) + green(" You have already finished all of your quests! ✅")
                else:
                    varquest1 = self.get_quest_1(cont, conts)
                    aquests, aprogress1, aprogress2 = varquest1
                    varquest2 = self.get_quest_2(cont, conts)
                    bquests, bprogress1, bprogress2 = varquest2
                    varquest3 = self.get_quest_3(cont, conts)
                    cquests, cprogress1, cprogress2 = varquest3
                    self.print_quest = red(
                        f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                    ) + yellow(
                        f" quest 1: {aquests} quest 2: {bquests} quest 3: {cquests}"
                    )
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
                                serverid,
                            ),
                        )
                        return do_quest_1.start()
                    elif (
                        (aquests == bquests)
                        or (aquests == cquests)
                        or (bquests == cquests)
                    ) and ((aquests != "") and (bquests != "")):
                        if aquests == bquests:
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
                                    serverid,
                                ),
                            )
                            do_quest_2.start
                            if cquests != "":
                                if (("pray" in aquests) or ("curse" in aquests)) and (
                                    ("pray" in cquests) or ("curse" in cquests)
                                ):
                                    progress = int(progress2) - int(progress1)
                                    time.sleep(progress * 60 * 5)
                                    do_quest_2_1 = threading.Thread(
                                        target=self.doquest,
                                        args=(
                                            cquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            cprogress1,
                                            cprogress2,
                                            serverid,
                                        ),
                                    )
                                    do_quest_2_1.start
                                else:
                                    do_quest_2_2 = threading.Thread(
                                        target=self.doquest,
                                        args=(
                                            cquests,
                                            tokenst,
                                            tokenrd,
                                            useridst,
                                            channelid,
                                            cprogress1,
                                            cprogress2,
                                            serverid,
                                        ),
                                    )
                                    do_quest_2_2.start
                        elif cquests != "":
                            if aquests == cquests:
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
                                        serverid,
                                    ),
                                )
                                do_quest_3.start
                                if (("pray" in aquests) or ("curse" in aquests)) and (
                                    ("pray" in bquests) or ("curse" in bquests)
                                ):
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
                                            serverid,
                                        ),
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
                                            serverid,
                                        ),
                                    )
                                    do_quest_3_2.start
                            elif bquests == cquests:
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
                                        serverid,
                                    ),
                                )
                                do_quest_4.start
                                if (("pray" in aquests) or ("curse" in aquests)) and (
                                    ("pray" in bquests) or ("curse" in bquests)
                                ):
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
                                            serverid,
                                        ),
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
                                            serverid,
                                        ),
                                    )
                                    do_quest_4_2.start
                    else:
                        if (("pray" in aquests) or ("curse" in aquests)) and (
                            ("pray" in bquests) or ("curse" in bquests)
                        ):
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
                                    serverid,
                                ),
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
                                        serverid,
                                    ),
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
                                    serverid,
                                ),
                            )
                            do_quest2.start()
                        elif (("pray" in aquests) or ("curse" in aquests)) and (
                            ("pray" in cquests) or ("curse" in cquests)
                        ):
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
                                    serverid,
                                ),
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
                                    serverid,
                                ),
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
                                    serverid,
                                ),
                            )
                            do_quest3.start()
                        elif (("pray" in bquests) or ("curse" in bquests)) and (
                            ("pray" in cquests) or ("curse" in cquests)
                        ):
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
                                    serverid,
                                ),
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
                                    serverid,
                                ),
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
                                    serverid,
                                ),
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
                                    serverid,
                                ),
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
                                        serverid,
                                    ),
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
                                        serverid,
                                    ),
                                )
                                do_quest3.start()
            except (KeyError, json.JSONDecodeError) as e:
                self.print_quest = (
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")
                    + magenta(f"[{tokentype}] ")
                    + red("Unable to check quest❗")
                )
        else:
            pass

    # ██████╗░██╗░░░██╗███╗░░██╗  ██████╗░░█████╗░████████╗
    # ██╔══██╗██║░░░██║████╗░██║  ██╔══██╗██╔══██╗╚══██╔══╝
    # ██████╔╝██║░░░██║██╔██╗██║  ██████╦╝██║░░██║░░░██║░░░
    # ██╔══██╗██║░░░██║██║╚████║  ██╔══██╗██║░░██║░░░██║░░░
    # ██║░░██║╚██████╔╝██║░╚███║  ██████╦╝╚█████╔╝░░░██║░░░
    # ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝  ╚═════╝░░╚════╝░░░░╚═╝░░░

    def bot_main(self):
        self.add_user(self.main_id, f"adduser_main")
        response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": self.main_token},
        )
        global request_count
        request_count += 1
        try:
            body = response.json()
            if str(body) == "401: Unauthorized":
                self.print_main_user = (
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")
                    + magenta(" [Main  Token]")
                    + red(f" / {str(body)}")
                )
                time.sleep(5)
                exit(0)
            else:
                self.print_main_user = blue(f"Main User: {body["username"]}")
                self.checklist(
                    self.main_token,
                    "Main  Token",
                    self.main_channelid,
                    self.main_id,
                )
        except (KeyError, json.JSONDecodeError) as e:
            self.print_main_user = (
                red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")
                + magenta(" [Main  Token]")
                + red(f" Error while checking Main  Token! ⚠️")
            )
            time.sleep(5)
            exit(0)

    # ========================================================================================================================

    def bot_extra(self):
        if self.extratokencheck:
            self.add_user(self.extra_id, f"adduser_extra")
            response = requests.get(
                f"https://canary.discord.com/api/v9/users/@me",
                headers={"authorization": self.extra_token},
            )
            global request_count
            request_count += 1
            try:
                body = response.json()
                if str(body) == "401: Unauthorized":
                    self.print_extra_user = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')} ")
                        + magenta(" [Extra  Token]")
                        + red(f" / {str(body)}")
                    )
                    time.sleep(5)
                    exit(0)
                else:
                    self.print_extra_user = blue(f"Extra User: {body["username"]}")
                    self.checklist(
                        self.extra_token,
                        "Extra Token",
                        self.extra_channelid,
                        self.extra_id,
                    )
            except (KeyError, json.JSONDecodeError) as e:
                self.print_extra_user = (
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                    + magenta(" [Extra Token]")
                    + red(f" Error while checking Extra Token! ⚠️")
                )
                time.sleep(5)
                exit(0)

    """ ▒█▀▀█ █▀▀█ █░░ █░░ 　 █░░ █▀▀█ █▀▀█ █▀▀█
        ▒█░░░ █▄▄█ █░░ █░░ 　 █░░ █░░█ █░░█ █░░█
        ▒█▄▄█ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀▀ █▀▀▀"""
    # ========================================================================================================================

    def run__bot__hunt__and__battle(self, tokens, tokentypes, channelids, serverid):
        session_id = self.generate_random_128bit_hex()
        while True:
            if self.active_bot:
                timehunt = self.rantime()
                timebattle = timehunt + 1
                if hunt:
                    time.sleep(timehunt)
                    timehunts = round(timehunt, 3)
                    self.bot_hunt(
                        tokens,
                        timehunts,
                        tokentypes,
                        channelids,
                        session_id,
                        serverid,
                    )
                    if inventorycheck:
                        time.sleep(1)
                        self.checkinv(tokens, channelids, tokentypes)
                if (battle) and self.battle_hunt:
                    time.sleep(timebattle + 5)
                    timebattles = round(timebattle, 3)
                    self.bot_battle(
                        tokens,
                        timebattles,
                        tokentypes,
                        channelids,
                        session_id,
                        serverid,
                    )
            else:
                break
            time.sleep(15)

    # ========================================================================================================================

    def run__bot__animal(self, tokens, tokentypes, channelid, ani_types):
        while True:
            if self.active_bot and ani_enable:
                self.bot_animals(tokens, tokentypes, channelid, ani_types)
            else:
                break
            t = self.rantime()
            time.sleep(60 + t)

    # ========================================================================================================================

    def run__bot__say__owo(self, tokens, tokentypes, channelids):
        while True:
            if self.active_bot and sayowo:
                self.bot_owo(tokens, tokentypes, channelids)
            else:
                break
            t = self.rantime()
            time.sleep(15 + t)

    # ========================================================================================================================

    def run__bot__pray(self, tokens, tokentypes, channelids, prays):
        while True:
            if self.active_bot and self.pray:
                if self.pray_curse:
                    self.bot_pray(tokens, tokentypes, channelids, prays)
            else:
                break
            t = self.rantime_2()
            time.sleep((5 * 60) + t)

    # ========================================================================================================================

    def run__bot__curse(self, tokens, tokentypes, channelids, curses):
        while True:
            if self.active_bot and self.curse:
                if self.pray_curse:
                    self.bot_curse(tokens, tokentypes, channelids, curses)
            else:
                break
            t = self.rantime_2()
            time.sleep((5 * 60) + t)

    # ========================================================================================================================

    def run__bot__upgrade(self, tokens, tokentypes, channelids):
        while True:
            if self.active_bot and ani_enable:
                self.upgradeall(tokens, tokentypes, channelids)
            else:
                break
            t = self.rantime_2()
            time.sleep((10 * 60) + t)

    # ========================================================================================================================

    def run__bot__gamble(self, tokens, tokentypes, channelids):
        while True:
            if self.active_bot:
                if slots_enable:
                    self.bot_slots(tokens, tokentypes, channelids)
                elif coinflip_enable:
                    self.bot_coinflip(tokens, tokentypes, channelids)
                else:
                    break
            t = self.rantime()
            time.sleep(15 + t)

    """░█████╗░░█████╗░██╗░░░░░██╗░░░░░  ██████╗░░█████╗░████████╗
        ██╔══██╗██╔══██╗██║░░░░░██║░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
        ██║░░╚═╝███████║██║░░░░░██║░░░░░  ██████╦╝██║░░██║░░░██║░░░
        ██║░░██╗██╔══██║██║░░░░░██║░░░░░  ██╔══██╗██║░░██║░░░██║░░░
        ╚█████╔╝██║░░██║███████╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░
        ░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░"""

    # ========================================================================================================================

    def main(self):
        self.bot_main_thread = threading.Thread(target=self.bot_main)
        self.bot_main_thread.start()
        self.bot_main_thread.join()
        time.sleep(5)

        if autoquest:
            self.run__bot__getquests_thread = threading.Thread(
                target=self.getquests,
                args=(
                    self.main_token,
                    self.extra_token,
                    self.main_id,
                    self.main_questchannelid,
                    "Main  Token",
                    self.main_serverid,
                ),
            )
            self.run__bot__getquests_thread.start()

        time.sleep(5)

        self.run__bot__hunt__and__battle_thread = threading.Thread(
            target=self.run__bot__hunt__and__battle,
            args=(
                self.main_token,
                "Main  Token",
                self.main_channelid,
                self.main_serverid,
            ),
        )
        self.run__bot__animal_thread = threading.Thread(
            target=self.run__bot__animal,
            args=(
                self.main_token,
                "Main  Token",
                self.main_channelid,
                ani_type,
            ),
        )
        self.run__bot__say__owo_thread = threading.Thread(
            target=self.run__bot__say__owo,
            args=(self.main_token, "Main  Token", self.main_channelid),
        )
        self.run__bot__pray_thread = threading.Thread(
            target=self.run__bot__pray,
            args=(
                self.main_token,
                "Main  Token",
                self.main_channelid,
                pray,
            ),
        )
        self.run__bot__curse_thread = threading.Thread(
            target=self.run__bot__curse,
            args=(
                self.main_token,
                "Main  Token",
                self.main_channelid,
                curse,
            ),
        )
        self.run__bot__upgrade_thread = threading.Thread(
            target=self.run__bot__upgrade,
            args=(self.main_token, "Main  Token", self.main_channelid),
        )
        self.run__bot__gamble_thread = threading.Thread(
            target=self.run__bot__gamble,
            args=(self.main_token, "Main  Token", self.main_channelid),
        )

        self.run__bot__say__owo_thread.start()
        self.run__bot__hunt__and__battle_thread.start()
        time.sleep(5)
        self.run__bot__pray_thread.start()
        self.run__bot__curse_thread.start()
        time.sleep(5)
        self.run__bot__upgrade_thread.start()
        self.run__bot__gamble_thread.start()
        self.run__bot__animal_thread.start()

    def extra(self):
        if self.extratokencheck:

            self.bot_extra_thread = threading.Thread(target=self.bot_extra)
            self.bot_extra_thread.start()
            self.bot_extra_thread.join()

            time.sleep(5)

            if autoquest:
                self.extra__run__bot__getquests_thread = threading.Thread(
                    target=self.getquests,
                    args=(
                        self.extra_token,
                        self.main_token,
                        self.extra_id,
                        self.extra_questchannelid,
                        "Extra Token",
                        self.extra_serverid,
                    ),
                )
                self.extra__run__bot__getquests_thread.start()

            time.sleep(5)

            self.extra__run__bot__hunt__and__battle_thread = threading.Thread(
                target=self.run__bot__hunt__and__battle,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                    self.extra_serverid,
                ),
            )
            self.extra__run__bot__animal_thread = threading.Thread(
                target=self.run__bot__animal,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                    ani_type,
                ),
            )
            self.extra__run__bot__say__owo_thread = threading.Thread(
                target=self.run__bot__say__owo,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                ),
            )
            self.extra__run__bot__pray_thread = threading.Thread(
                target=self.run__bot__pray,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                    pray,
                ),
            )
            self.extra__run__bot__curse_thread = threading.Thread(
                target=self.run__bot__curse,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                    curse,
                ),
            )
            self.extra__run__bot__upgrade_thread = threading.Thread(
                target=self.run__bot__upgrade,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                ),
            )
            self.extra__run__bot__gamble_thread = threading.Thread(
                target=self.run__bot__gamble,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                ),
            )

            self.extra__run__bot__say__owo_thread.start()
            self.extra__run__bot__hunt__and__battle_thread.start()
            time.sleep(5)
            self.extra__run__bot__pray_thread.start()
            self.extra__run__bot__curse_thread.start()
            time.sleep(5)
            self.extra__run__bot__animal_thread.start()
            self.extra__run__bot__upgrade_thread.start()
            self.extra__run__bot__gamble_thread.start()

    def stop_main(self):
        threads = [
            self.bot_main_thread,
            self.run__bot__getquests_thread,
            self.run__bot__say__owo_thread,
            self.run__bot__hunt__and__battle_thread,
            self.run__bot__pray_thread,
            self.run__bot__curse_thread,
            self.run__bot__animal_thread,
            self.run__bot__upgrade_thread,
            self.run__bot__gamble_thread,
        ]

        for thread in threads:
            try:
                if thread.is_alive():
                    thread.join(timeout=0)
            except AttributeError:
                pass

    def stop_extra(self):
        if self.extratokencheck:
            threads = [
                self.bot_extra_thread,
                self.extra__run__bot__getquests_thread,
                self.extra__run__bot__say__owo_thread,
                self.extra__run__bot__hunt__and__battle_thread,
                self.extra__run__bot__pray_thread,
                self.extra__run__bot__curse_thread,
                self.extra__run__bot__animal_thread,
                self.extra__run__bot__upgrade_thread,
                self.extra__run__bot__gamble_thread,
            ]

            for thread in threads:
                try:
                    if thread.is_alive():
                        thread.join(timeout=0)
                except AttributeError:
                    pass

    def __MAIN__(self):
        main = threading.Thread(target=self.main)
        extra = threading.Thread(target=self.extra)
        main.start()
        extra.start()

    def bot_recover(self):
        while True:
            try:
                if not self.run__bot__captcha_thread.is_alive():
                    self.run__bot__captcha_thread = threading.Thread(
                        target=self.run__bot__captcha,
                        args=(
                            self.main_token,
                            "Main  Token",
                            self.main_channelid,
                            self.main_dmchannelid,
                            self.main_id,
                        ),
                    )
                    self.run__bot__captcha_thread.start()
                    self.print_recover = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                        + magenta(" [Captcha/Controller Bot]")
                        + green(f" Captcha/Controller has been fixed! ⚠️")
                    )
            except AttributeError:
                pass
            try:
                if (not self.extra__run__bot__captcha_thread.is_alive()) and (
                    self.extratokencheck
                ):
                    self.extra__run__bot__captcha_thread = threading.Thread(
                        target=self.run__bot__captcha,
                        args=(
                            self.extra_token,
                            "Extra Token",
                            self.extra_channelid,
                            self.extra_dmchannelid,
                            self.extra_id,
                        ),
                    )
                    self.extra__run__bot__captcha_thread.start()
                    self.print_recover = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                        + magenta(" [Captcha/Controller Bot]")
                        + green(f" Captcha/Controller has been fixed! ⚠️")
                    )
            except AttributeError:
                pass

    def run__bot__captcha(self, token, tokentype, channelid, dmchannelid, userid):
        response = requests.get(
            f"https://canary.discord.com/api/v9/users/@me",
            headers={"authorization": token},
        )
        global request_count
        request_count += 1
        body = response.json()
        username = body["username"]
        while True:
            global is_reading

            try:
                response = requests.get(
                    f"https://discord.com/api/v9/channels/{
                        channelid}/messages?limit=10",
                    headers={"authorization": token},
                )
                request_count += 1
                responsedm = requests.get(
                    f"https://discord.com/api/v9/channels/{
                        dmchannelid}/messages?limit=1",
                    headers={"authorization": token},
                )
                request_count += 1

                if responsedm.status_code == 200:
                    with open(file_cache, "r", encoding="utf-8") as s:
                        data = json.load(s)
                        s.close()
                    bodydm = responsedm.json()
                    captcha_md = bodydm[0]["id"]
                    contentmd = bodydm[0]["content"]
                    id_captcha_dm = data[userid]["id_captcha_dm"]
                    if ("Are you a real human?" in contentmd) and (
                        captcha_md != id_captcha_dm
                    ):
                        data[userid]["id_captcha_dm"] = captcha_md
                        global is_reading

                        # waitting before read/write file
                        queues.put(f"id_captcha_dm_{userid}")

                        while True:
                            if queues.get() == (f"id_captcha_dm_{userid}"):
                                break
                            queues.put(f"id_captcha_dm_{userid}")

                        # lock thread file to read
                        with lock:
                            is_reading = True
                            with open(file_cache, "w", encoding="utf-8") as write_id_dm:
                                json.dump(data, write_id_dm, indent=4)
                                write_id_dm.close()
                            is_reading = False
                        print_ = (
                            red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                            + blue(f" [{username}]")
                            + red(f" Chat Captcha! ❌")
                        )
                        if tokentype == "Extra Token":
                            self.print_captcha_check_extra = print_
                        else:
                            self.print_captcha_check_main = print_
                        self.active_bot = False
                        self.task_bot_active = False
                        self.captcha_notification = True
                        if self.main_thread.is_alive():
                            self.main_thread.join(timeout=0)
                        time.sleep(0.001)
                        notification_bot = threading.Thread(
                            target=self.notification_def,
                            args=(username, tokentype,),
                            name=(f"notification_{username}",),
                        )
                        notification_bot.start()
                        notification_bot.join()

                if response.status_code == 200:

                    body = response.json()
                    for bodycount in body:
                        content = bodycount["content"]
                        id = bodycount["author"]["id"]
                        id_message = bodycount["id"]
                        # (idowo == "408785106942164992") and
                        if (
                            ("captcha" in content)
                            or (f"⚠️ **|** <@{userid}>" in content)
                            or (f"⚠️ **|**" in content)
                        ) and (
                            self.read_id(
                                id_message,
                                userid,
                                "id_captcha",
                                f"captcha_{userid}",
                            )
                        ):
                            print_ = (
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                                + blue(f" [{username}]")
                                + red(f" Chat Captcha! ❌")
                            )
                            if tokentype == "Extra Token":
                                self.print_captcha_check_extra = print_
                            else:
                                self.print_captcha_check_main = print_
                            self.active_bot = False
                            self.task_bot_active = False
                            self.captcha_notification = True
                            if self.main_thread.is_alive():
                                self.main_thread.join(timeout=0)
                            stop_main_thread = threading.Thread(target=self.stop_main)
                            stop_extra_thread = threading.Thread(target=self.stop_extra)
                            stop_main_thread.start()
                            stop_extra_thread.start()
                            time.sleep(0.001)
                            for bodycounts in body:
                                self.add_id_to_cache(
                                    bodycounts["id"],
                                    userid,
                                    "id_captcha",
                                    f"captcha_addid_{userid}",
                                )
                            notification_bot = threading.Thread(
                                target=self.notification_def,
                                args=(username,tokentype,),
                                name=(f"notification_{username}",),
                            )
                            notification_bot.start()
                        if ((id == self.main_id) or (id == self.extra_id)) and (
                            self.read_id(
                                id_message,
                                userid,
                                "id_activate",
                                f"bot_{userid}",
                            )
                        ):
                            content = bodycount["content"]
                            if (content == f"{bot_prefix}stop") and (
                                self.task_bot_active
                            ):
                                for bodycounts in body:
                                    self.add_id_to_cache(
                                        bodycounts["id"],
                                        userid,
                                        "id_activate",
                                        f"add_id_bot_{userid}",
                                    )
                                self.active_bot = False
                                self.task_bot_active = False
                                self.print_send_mess_control_bot = red(
                                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                                ) + yellow(" Bot was stopped! ✅")
                                if self.main_thread.is_alive():
                                    self.main_thread.join(timeout=0)
                                stop_main_thread = threading.Thread(
                                    target=self.stop_main
                                )
                                stop_extra_thread = threading.Thread(
                                    target=self.stop_extra
                                )
                                stop_main_thread.start()
                                stop_extra_thread.start()
                            elif (content == f"{bot_prefix}run") and (
                                not self.task_bot_active
                            ):
                                for bodycounts in body:
                                    self.add_id_to_cache(
                                        bodycounts["id"],
                                        userid,
                                        "id_activate",
                                        f"add_id_bot_{userid}",
                                    )

                                self.captcha_notification = False
                                self.task_bot_active = True
                                self.active_bot = True
                                self.main_thread = threading.Thread(
                                    target=self.__MAIN__
                                )
                                self.main_thread.start()
                                self.print_send_mess_control_bot = red(
                                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                                ) + yellow(" Bot is Running!")
                            elif content == f"{bot_prefix}reset":
                                self.active_bot = False
                                self.task_bot_active = False
                                for bodycounts in body:
                                    self.add_id_to_cache(
                                        bodycounts["id"],
                                        userid,
                                        "id_activate",
                                        f"add_id_bot_{userid}",
                                    )

                                if self.main_thread.is_alive():
                                    self.main_thread.join(timeout=0)
                                stop_main_thread = threading.Thread(
                                    target=self.stop_main
                                )
                                stop_extra_thread = threading.Thread(
                                    target=self.stop_extra
                                )
                                stop_main_thread.start()
                                stop_extra_thread.start()
                                self.captcha_notification = False
                                self.task_bot_active = True
                                self.active_bot = True
                                time.sleep(0.2)
                                self.main_thread = threading.Thread(
                                    target=self.__MAIN__
                                )
                                self.main_thread.start()
                                self.print_send_mess_control_bot = red(
                                    f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                                ) + yellow(" Bot was reseted!")
                            else:
                                if (self.task_bot_active == True) and (
                                    self.active_bot == True
                                ):
                                    self.print_send_mess_control_bot = red(
                                        f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                                    ) + blue(" Bot is alive⚡")
                                else:
                                    self.print_send_mess_control_bot = red(
                                        f"{datetime.datetime.now().strftime('%H:%M:%S')}"
                                    ) + blue(" Bot stopped ⭕")
                        if (
                            (not "captcha" in content)
                            and (not f"⚠️ **|** <@{userid}>" in content)
                            and (not f"⚠️ **|**" in content)
                        ) and (self.captcha_notification == False):
                            print_ = (
                                red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                                + blue(f" [{username}]")
                                + blue(f" Captcha Checked! ✅")
                            )
                            if tokentype == "Extra Token":
                                self.print_captcha_check_extra = print_
                            else:
                                self.print_captcha_check_main = print_
                else:
                    print_ = (
                        red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                        + magenta(" [Captcha/Controller Bot]")
                        + red(f" 401: Unauthorized! ⚠️")
                    )
                    if tokentype == "Extra Token":
                        self.print_captcha_check_extra = print_
                    else:
                        self.print_captcha_check_main = print_
            except (KeyError, json.JSONDecodeError, ConnectionResetError) as e:
                print_ = (
                    red(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                    + magenta(" [Captcha/Controller Bot]")
                    + red(f" Error while Run bot! ⚠️")
                )
                if tokentype == "Extra Token":
                    self.print_captcha_check_extra = print_
                else:
                    self.print_captcha_check_main = print_
                break
            time.sleep(1)

    def ___MAIN___(self, data):
        self.extratokencheck = data["extratoken"]
        main = data["main"]
        self.main_token = str(main["token"])
        self.main_id = str(token_decode(self.main_token))
        self.main_serverid = str(main["serverid"])
        self.main_channelid = str(main["channelid"])
        self.main_questchannelid = str(main["questchannelid"])
        self.main_dmchannelid = str(main["owo_dmschannelid"])

        extra = data["extra"]
        self.extra_token = str(extra["token"])
        self.extra_id = str(token_decode(self.extra_token))
        self.extra_serverid = str(extra["serverid"])
        self.extra_channelid = str(extra["channelid"])
        self.extra_questchannelid = str(extra["questchannelid"])
        self.extra_dmchannelid = str(extra["owo_dmschannelid"])

        if (self.extra_token == self.main_token) or (self.extra_token == ""):
            self.extratokencheck = False

        self.main_thread = threading.Thread(target=self.__MAIN__)
        self.main_thread.start()
        time.sleep(3.5)
        self.run__bot__captcha_thread = threading.Thread(
            target=self.run__bot__captcha,
            args=(
                self.main_token,
                "Main  Token",
                self.main_channelid,
                self.main_dmchannelid,
                self.main_id,
            ),
        )
        self.run__bot__captcha_thread.start()
        if self.extratokencheck:
            self.extra__run__bot__captcha_thread = threading.Thread(
                target=self.run__bot__captcha,
                args=(
                    self.extra_token,
                    "Extra Token",
                    self.extra_channelid,
                    self.extra_dmchannelid,
                    self.extra_id,
                ),
            )
            self.extra__run__bot__captcha_thread.start()
        time.sleep(2)
        recover_thread = threading.Thread(
            target=self.bot_recover,
        )
        recover_thread.start()


if __name__ == "__main__":
    check = threading.Thread(target=checkversion)
    check.start()
    install = threading.Thread(target=install_update)
    install.start()
    group_names = [key for key in cfgs if key.startswith("group_")]
    apis = []
    for i in group_names:
        api = ____API____()
        apis.append(api)

    for group_name, _API_ in zip(group_names, apis):
        data_store = cfgs[group_name]
        if data_store["active"]:
            i = int(group_name.split("_")[1])
            Process_api = threading.Thread(
                target=_API_.___MAIN___,
                args=(data_store,),
                name=f"Group_{i}",
            )
            Process_api.start()
        time.sleep(0.01)
    total_request_count = 0
    start_time2 = time.time()
    time.sleep(2)
    while True:
        """keep alive"""
        #clear_screen()
        time.sleep(
            0.000000000000000000000000000000000000000000000000000000000000001
        )  # idk what i am doing lol
        elapsed_time = time.time() - start_time
        elapsed_time2 = time.time() - start_time2
        total_request_count += request_count
        average_requests_per_second = request_count / elapsed_time
        average_total_request_per_second = total_request_count / elapsed_time2
        formatted_time_elapsed_time = time.strftime(
            "%H:%M:%S", time.gmtime(elapsed_time2)
        )
        print(
            (
                red(f"Time elapsed: {formatted_time_elapsed_time}\n \n")
                + blue(
                    f"Requests speed: {round(average_requests_per_second, 3)} req/s\n"
                )
                + green(
                    f"Average speed: {round(average_total_request_per_second, 3)} req/s\n"
                )
                + red(f"Average speed should under 17req/s\n")
            ),
            flush=True,
        )
        for group_name, _API_ in zip(group_names, apis):
            data_store = cfgs[group_name]
            if data_store["active"]:
                ii = int(group_name.split("_")[1])
                time.sleep(
                    0.000000000000000000000000000000000000000000000000000000000000001
                )
                print(
                    f"""Group {ii}
{_API_.print_main_user}
{_API_.print_extra_user}
{_API_.print_send_mess_control_bot}
{_API_.print_captcha_check_main}
{_API_.print_captcha_check_extra}
{_API_.print_quest}
{_API_.print_cl}
{_API_.print_say_owo}
{_API_.print_h}
{_API_.print_b}
{_API_.print_pray}
{_API_.print_curse}
{_API_.print_s}
{_API_.print_cf}
{_API_.print_upg}
{_API_.print_inv}
{_API_.print_box}
{_API_.print_gem}
{_API_.print_bot_animal}\n
""",
                    flush=True,
                )
        request_count = 0
        start_time = time.time()
        time.sleep(2)
