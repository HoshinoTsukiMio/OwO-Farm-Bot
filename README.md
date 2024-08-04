<br>
<h1 align="center">OwO Farm Bot v1-0.2.a334f635 </h1>

</p>

[❗・Important](#important)<br>
[👑・Features](#features)<br>
[⚙・setting_config.json example](#configjson-example)<br>
[💎・Get Token](#get-token)<br>
[📍・OwO DM channel id](#owo-dm-channel-id)<br>
[⚠️・Captcha Alert](#captcha-alert)<br>
[🔗・Required Links](#required-links)<br>
[🎈・Usage](#usage)<br>


## ❗・Important
-   You should use 2 account for access dual auto quest
-   Use of this farm bot may lead to actions being taken against your OwO profile and/or your Discord account. I am not responsible for them.
-   DO NOT USE ONE CHANNEL FOR TWO ACCOUNTS, USE IT FOR 1 ACCOUNT ONLY.
-   Discord may restart as a result of discord rpc overload.
-   It can detect virus due to captcha(ban) bypasser please turn off your antivirus(not really).
-   Slash command '/' still in beta mode cant be know does it work well

## 👑・Features

-   Auto Hunt
-   Auto Battle
-   Inventory Check
    -   Auto Gem Use (beta)
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
-   Captcha Protection v0.0.0 (beta)
-   **Extra Token**
    -   All Main Token Features

## ⚙・setting_config.json example

```
{
    "settings": {
        "prefix": "owo", prefix for owo you set in your server defaul is owo
        "bot_prefix": "! or any prefix this use to run bot like !run, !reset, !stop",
        "slash_command": true, turn on or off slsh command mode
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
    },
    "main":{
        "note": "",note what you want :P
        "token":"main token",
        "serverid": "", id ur server main
        "channelid":"channel id for main token",
        "dmchannelid":"owo bot dm channel id",
        "questchannelid": "auto quest channel id",
        "owo_dmschannelid":"main token owo bot dm channel id",
    },
    "extra":{
        "token":"extra token",
        "serverid": "", id ur server extra
        "channelid":"channel id for extra token",
        "questchannelid": "auto quest channel id",
        "owo_dmschannelid":"extra token owo bot dm channel id",
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
```
