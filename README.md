<br>
<h1 align="center">OwO Farm Bot v2-0.1.99a07a7461b8 </h1>

</p>

[❗ ・Important](#important)<br>
[👑・Features](#features)<br>
[🔨・setting example](#setting-example)<br>
[💎・Get Token](#get-token)<br>
[📍 ・Channel id](#channel-id)<br>
[📍 ・Server id](#server-id)<br>
[📍 ・OwO DM channel id](#owo-dm-channel-id)<br>
[⚠️・Captcha Alert](#%EF%B8%8Fcaptcha-alert)<br>
[🔗・Required Links](#required-links)<br>
[🎈 ・Usage](#usage)<br>


## ❗・Important
-   You should use 2 account for access dual auto quest
-   Use of this farm bot may lead to actions being taken against your OwO profile and/or your Discord account. I am not responsible for them.
-   DO NOT USE ONE CHANNEL FOR TWO ACCOUNTS, USE IT FOR 1 ACCOUNT ONLY.well

## 👑・Features
-   Can control bot to run or stop
-   Multi account farm (2 account per group)
-   Auto Hunt (slash command)
-   Auto Battle (slash command)
-   Inventory Check
    -   Auto Gem Use 
    -   Auto Lootbox Use
    -   Auto Fabled Lootbox Use
    -   Auto Crate Use
-   Auto Gamble
    -   Auto Coinflip
    -   Auto Slots
-   Auto Animals Sell OR Sacrifice,
-   Auto Upgrade Autohunt
-   Auto Pray or Curse
-   Auto Quest
-   Auto CheckList
    -   Auto Daily
    -   Auto Cookie
-   Captcha Protection v2.0.0 
-   **Extra Token**
    -   All Main Token Features

## ⚙・setting example
- all groups are not sync together, maintoken and extratoken in 1 group will do quest not do for other group
- bot is base on group account not how many account
- you can extend new group by add group
```
    "group_n":{
        "main":{
            "note": "note what you want :P",
            "token":"main token",
            "serverid": "id ur server main", 
            "channelid":"channel id for main token",
            "dmchannelid":"owo bot dm channel id",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"main token owo bot dm channel id"
        },
        "extra":{
            "note": "note what you want :P",
            "token":"extra token",
            "serverid": "id ur server extra", 
            "channelid":"channel id for extra token",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"extra token owo bot dm channel id"
        }
    }
```
- this is example of setting

```
{
    "settings": {
        "owo_prefix": "owo", prefix for owo you set in your server defaul is owo
        "control_prefix": "! or any prefix this use to run bot like !run, !stop",
        "slash_command": true, turn on or off slash command mode
        "sayowo": "true or false",
        "pray": "true or false",
        "curse": "true or false",
        "hunt": "true or false",
        "battle": "true or false",
        "autoquest": "true or false",
        "randommess": "true or false",
        "banbypass": "true or false",
        "extratoken": "true or false",
        "inventory": {
            "inventorycheck": "true or false",
            "gemcheck": "true or false",
            "lootboxcheck": "true or false",
            "fabledlootboxcheck": "true or false",
            "cratecheck": "true or false"
        },
        "animals": {
            "enable": "true or false",
            "type": "sell or sac",
            "animaltype": {
                "all": "true or false",
                "common": "true or false",
                "uncommon": "true or false",
                "rare": "true or false",
                "epic": "true or false",
                "mythical": "true or false",
                "patreon": "true or false",
                "cpatreon": "true or false",
                "legendary": "true or false",
                "gem": "true or false",
                "bot": "true or false",
                "distorted": "true or false",
                "fabled": "true or false",
                "special": "true or false",
                "hidden": "true or false"
            }
        },
        "upgradeautohunt": {
            "enable": "true or false",
            "upgtype": "efficiency, duration, cost, gain, exp or radar"
        },
        "gamble": {
            "coinflip": {
                "enable": "true or false",
                "amount": "any amount"
            },
            "slots": {
                "enable": "true or false",
                "amount": "any amount"
            }
        }
    }
    "group_1":{
        "main":{
            "note": "note what you want :P",
            "token":"main token",
            "serverid": "id ur server main", 
            "channelid":"channel id for main token",
            "dmchannelid":"owo bot dm channel id",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"main token owo bot dm channel id"
        },
        "extra":{
            "note": "note what you want :P",
            "token":"extra token",
            "serverid": "id ur server extra", 
            "channelid":"channel id for extra token",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"extra token owo bot dm channel id"
        }
    },
    "group_2":{
        "main":{
            "note": "note what you want :P",
            "token":"main token",
            "serverid": "id ur server main", 
            "channelid":"channel id for main token",
            "dmchannelid":"owo bot dm channel id",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"main token owo bot dm channel id"
        },
        "extra":{
            "note": "note what you want :P",
            "token":"extra token",
            "serverid": "id ur server extra", 
            "channelid":"channel id for extra token",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"extra token owo bot dm channel id"
        }
    },
    "group_3":{
        "main":{
            "note": "note what you want :P",
            "token":"main token",
            "serverid": "id ur server main", 
            "channelid":"channel id for main token",
            "dmchannelid":"owo bot dm channel id",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"main token owo bot dm channel id"
        },
        "extra":{
            "note": "note what you want :P",
            "token":"extra token",
            "serverid": "id ur server extra", 
            "channelid":"channel id for extra token",
            "questchannelid": "auto quest channel id",
            "owo_dmschannelid":"extra token owo bot dm channel id"
        }
    }
}
```

## 💎・Get Token
-  You can find some way to find token in youtube
```js
(webpackChunkdiscord_app.push([
    [""],
    {},
    (e) => {
        m = [];
        for (let c in e.c) m.push(e.c[c]);
    },
]),
m)
    .find((m) => m?.exports?.default?.getToken !== void 0)
    .exports.default.getToken();
```
## 📍・Channel id

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/images/ID%20Server.png)

## 📍・Server id

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/images/ID%20Server.png)

## 📍・OwO DM channel id

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-farm-bot/main/images/owochannelid.jpg)

## ⚠️・Captcha Alert

!!! If you want the captcha alert to work properly, turn off do not disturb

![](https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-farm-bot/main/images/captchaalert.png)



## 🔗・Required Links

[Python](https://www.python.org/downloads/)<br>
[Terminal (not really need)](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)<br>
[Farm Bot Zip File](https://codeload.github.com/HoshinoTsukiMio/OwO-Farm-Bot/zip/refs/heads/main)

## 🎈・Usage

```
> YOU NEED LATEST PYTHON !
> edit setting_config.json it in data folder
> ⚠DO NOT RUN ANY FILE .bat WITH ADMINISTRATOR⚠
> run "! Install Virtual Enviroment.bat" to set up Virtual Enviroment
> then you can run "! Run Bot.bat" to start bot
> enjoy and dont forget to update id it has a new version
```
