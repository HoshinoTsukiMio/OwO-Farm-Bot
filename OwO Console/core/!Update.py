import requests, os, json, time
current_dir = os.getcwd()

# Join the current directory with the filename
flie_data = os.path.join(current_dir, 'core\\!Main.py')
file_config = os.path.join(current_dir, 'data\\setting_config.json')
print("Updating...")
update = requests.get("https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Main.py")
with open(flie_data, "wb") as f:
    f.write(update.content)
    f.close()
with open(file_config, 'r', encoding='utf-8') as a:
    cfgs = json.load(a)
    a.close()
    os.remove(file_config)

setting               = cfgs["settings"]
prefix                = setting['prefix']
bot_prefix            = setting['bot_prefix']
slash_command         = setting['slash_command']
sayowo                = setting['sayowo']
pray                  = setting['pray']
curse                 = setting['curse']
hunt                  = setting['hunt']
battle                = setting['battle']
autoquest             = setting['autoquest']
extratokencheck       = setting['extratoken']
randommess            = setting['randommess']
banbypass             = setting['banbypass']
#========================================================================================================================
inventory             = setting['inventory']
inventorycheck        = inventory['inventorycheck']
gemcheck              = inventory['gemcheck']
lootboxcheck          = inventory['lootboxcheck']
fabledlootboxcheck    = inventory['fabledlootboxcheck']
cratecheck            = inventory['cratecheck']
#========================================================================================================================
animals               = setting['animals']
ani_enable            = animals['enable']
ani_type              = animals['type']
animaltype            = animals['animaltype']
common                = animaltype['common']
uncommon              = animaltype['uncommon']
rare                  = animaltype['rare']
epic                  = animaltype['epic']
mythical              = animaltype['mythical']
patreon               = animaltype['patreon']
cpatreon              = animaltype['cpatreon']
legendary             = animaltype['legendary']
gem                   = animaltype['gem']
bot                   = animaltype['bot']
distorted             = animaltype['distorted']
fabled                = animaltype['fabled']
special               = animaltype['special']
hidden                = animaltype['hidden']
#========================================================================================================================
upgradeautohunt       = setting['upgradeautohunt']
upg_enable            = upgradeautohunt['enable']
upg_type              = upgradeautohunt['upgtype']
#========================================================================================================================
gamble                = setting['gamble']
coinflip              = gamble['coinflip']
coinflip_enable       = coinflip['enable']
coinflip_amount       = coinflip['amount']

slots                 = gamble['slots']
slots_enable          = slots['enable']
slots_amount          = slots['amount']
#========================================================================================================================
main                  = cfgs['main']
main_token            = main['token']
main_channelid        = main['channelid']
main_dmchannelid      = main['dmchannelid']
main_questchannelid   = main['questchannelid']

extra                 = cfgs['extra']
extra_token           = extra['token']
extra_channelid       = extra['channelid']
extra_dmchannelid     = extra['dmchannelid']
extra_questchannelid  = extra['questchannelid']


config_setting = {
    "settings": {
        "prefix": prefix,
        "bot_prefix": bot_prefix,
        "slash_command": slash_command
        "owo": sayowo,
        "pray": pray,
        "curse": curse,
        "hunt": hunt,
        "battle": battle,
        "autoquest": autoquest,
        "randommess": randommess,
        "banbypass": banbypass,
        "extratoken": extratokencheck,
        "inventory": {
            "inventorycheck": inventorycheck,
            "gemcheck": gemcheck,
            "lootboxcheck": lootboxcheck,
            "fabledlootboxcheck": fabledlootboxcheck,
            "cratecheck": cratecheck
        },
        "animals": {
            "enable": ani_enable,
            "type": ani_type,
            "animaltype": {
                "common": common,
                "uncommon": uncommon,
                "rare": rare,
                "epic": epic,
                "mythical": mythical,
                "patreon": patreon,
                "cpatreon": cpatreon,
                "legendary": legendary,
                "gem": gem,
                "bot": bot,
                "distorted": distorted,
                "fabled": fabled,
                "special": special,
                "hidden": hidden
            }
        },
        "upgradeautohunt": {
            "enable": upg_enable,
            "upgtype": upg_type
        },
        "gamble": {
            "coinflip": {
                "enable": coinflip_enable,
                "amount": coinflip_amount
            },
            "slots": {
                "enable": slots_enable,
                "amount": slots_amount
            }
        }
    },
    "main": {
        "note": "",
        "token": main_token,
        "channelid": main_channelid,
        "dmchannelid": main_dmchannelid,
        "questchannelid": main_dmchannelid
    },
    "extra": {
        "note": "",
        "token": extra_token,
        "channelid": extra_channelid,
        "dmchannelid": extra_dmchannelid,
        "questchannelid": extra_questchannelid
    }
}
with open(file_config, "w") as b:
    json_data = json.dumps(config_setting, indent=4)
    b.write(json_data)
    b.close()
print("Update complete!")
