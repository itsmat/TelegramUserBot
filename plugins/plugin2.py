from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio, datetime
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.raw.functions.messages import StartBot, InstallStickerSet, DeleteHistory
from pytube import YouTube
import os, json, asyncio, requests, traceback, math
from random import randint
from PIL import Image
from gtts import gTTS
import asyncio
import time
import os
import re
import json
import aiohttp
import requests
import random
import asyncio
from datetime import datetime
from platform import python_version
from collections import deque
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__
from pyrogram import Client, filters

@Client.on_message(filters.user("self") & filters.command("creator","."))
async def creatore(client, message):
  await message.edit("""🧑🏻‍💻 Userbot sviluppato da https://github.com/itsmat
♻️ Canale @ItsMatDev""")


@Client.on_message(filters.user("self") & filters.command("sega","."))
async def SEGA(client, message):
  e = message
  for i in range(2):
    await asyncio.wait([e.edit("8=====D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8=✊===D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8==✊==D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8===✊=D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8==✊==D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8====✊D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8==✊==D")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8=====D💦")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8=====D💦💦")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("8=====D💦💦💦")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**Ush, ti sei segato **")])

@Client.on_message(filters.user("self") & filters.command("supreme","."))
async def SUPREME(client, message):
  e = message
  await asyncio.wait([e.edit("⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿")])              

@Client.on_message(filters.user("self") & filters.command("troll","."))
async def troll(client, message):
  e = message
  await asyncio.wait([e.edit("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄\n░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄\n░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█\n░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█\n░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█\n█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█\n█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█\n░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█\n░░░█░░██░░▀█▄▄▄█▄▄█▄████░█\n░░░░█░░░▀▀▄░█░░░█░███████░█\n░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█\n░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█\n░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█\n░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█")])              
  
@Client.on_message(filters.user("self") & filters.command("cesso","."))
async def cesso(client, message):
  e = message
  await asyncio.wait([e.edit("──────────────────────\n────────────███───────\n────────────███───────\n─────▄█████▄█▀▀───────\n──────▀█████──────────\n───────▄████▄─────────")])      

@Client.on_message(filters.user("self") & filters.command("lol","."))
async def lol(client, message):
  e = message
  await asyncio.wait([e.edit("╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱\n╱┗━━━┛╰━━━╯┗━━━┛╱")])      


@Client.on_message(filters.user("self") & filters.command("terra","."))
async def terra(client, message):
	deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await message.edit("".join(deq))
		deq.rotate(1)

@Client.on_message(filters.user("self") & filters.command("clock","."))
async def clock(client, message):
	deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await message.edit("".join(deq))
		deq.rotate(1)



@Client.on_message(filters.user("self") & filters.command("moon","."))
async def moon(client, message):
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await message.edit("".join(deq))
		deq.rotate(1)

@Client.on_message(filters.user("self") & filters.command("hack","."))
async def hack(client, message):
    try:
        e = message
        USER = message.from_user.first_name
        animation_interval = 2
        animation_ttl = range(0, 12)
        await e.edit("Inizio Hacking")
        animation_chars = [

                "Connessione a Telegram Data Center",
                f"Target Selected By {USER}",
                "Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
                "**Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
                "**Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
                "**Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
                "**Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
                "**Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
                "**Hacking... 84%\n█████████████████████▒▒▒▒ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database",
                "Hacking... 100%\n█████████HACKED███████████ **\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
                f"**Account Hackerato..."
            ]

        for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await e.edit(animation_chars[i % 12])
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@Client.on_message(filters.user("self") & filters.command("pene","."))
async def pene(client, message):
    e = message
    inizio = "............ ▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n"
    fine = "....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀\n"
    mezzoo = "....▐░░░░░░░░░░░▌\n"
    mezzo = ""
    for x in range(10):
        mezzo = mezzo + mezzoo
        await asyncio.wait([e.edit(inizio+mezzo+fine)])
        await asyncio.sleep(0.3)



a = """||            🚙"""
b = """||         🚙"""
c = """**Una piotta e dieci così, terza marcia, terza marcia, terza marcia.**"""
d = """__NON CI SONO PROBLEMI, NON CI SONO PROBLEMI__"""
e = """__Vi insegno a guidare...__"""
f = """||     🚙"""
g = """||  🚙"""
h = """**🚦 QUANDO IL SEMAFORO È ROSSO 🟢**"""
i = """🚦 QUANDO IL SEMAFORO È ROSSO 🟠"""
j = """🚦 QUANDO IL SEMAFORO È ROSSO 🔴"""
k = """**🚦 QUANDO IL SEMAFORO È ROSSO 🟢**"""
l = """**Si fa così, si fa così: taac.**"""
m = """Je imbocchi qua, je rigiri qua, fratellì, così."""
n = """|| 🚙"""
o = """||🚙"""
p = """Bada fratellì, **ho sfondato tutto fratellì**, ho sfonnato tutto."""
q = """__Ho preso er muro fratellì, te dico fermati fratellì. Ho preso er muro. ♿️__"""



@Client.on_message(filters.user("self") & filters.command("muro","."))
async def muro(client, message):
    target = message
    await target.edit(a)
    await asyncio.sleep(1.0)
    await target.edit(b)
    await asyncio.sleep(1.0)
    await target.edit(c)
    await asyncio.sleep(2.0)
    await target.edit(d)
    await asyncio.sleep(2.0)
    await target.edit(e)
    await asyncio.sleep(2.0)
    await target.edit(f)
    await asyncio.sleep(2.0)
    await target.edit(g)
    await asyncio.sleep(2.0)
    await target.edit(h)
    await asyncio.sleep(2.0)
    await target.edit(i)
    await asyncio.sleep(2.0)
    await target.edit(j)
    await asyncio.sleep(2.0)
    await target.edit(k)
    await asyncio.sleep(2.0)
    await target.edit(l)
    await asyncio.sleep(2.0)
    await target.edit(m)
    await asyncio.sleep(2.0)
    await target.edit(n)
    await asyncio.sleep(2.0)
    await target.edit(o)
    await asyncio.sleep(2.0)
    await target.edit(p)
    await asyncio.sleep(2.0)
    await target.edit(q)
    await asyncio.sleep(2.0)


random_number = random.randint(0, 100)

@Client.on_message(filters.user("self") & filters.command("gaytest","."))
async def gaytest(client, message):
    try:
        target = message
        if message.reply_to_message:
            info = await client.get_users(message.reply_to_message.from_user.id)
            gay = info.first_name
            #
            random_number = random.randint(0, 100)
            await target.edit(f"""**🏳‍🌈 Quanto sei gay Test**

        Ciao a tutti, oggi analizziamo la percentuale gay di {gay}.""")
            await asyncio.sleep(3.0)
            await target.edit(f"""**🧬 Risultati ottenuti!**

        ✅ {gay} è risultato **positivo gay** al {random_number}%.

        __👥 Consiglio di allontanarsi, potrebbe essere contagioso...__""")
        else:
            await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")



@Client.on_message(filters.user("self") & filters.command("prelievo","."))
async def prelievo(client, message):
    try:
        target = message
        if message.reply_to_message:
            info = await client.get_users(message.reply_to_message.from_user.id)
            name = info.first_name
            await target.edit(f"""**🧪 Test iniziato!**

        Oggi controlliamo l'organismo di {name}.""")
            await asyncio.sleep(2.0)
            await target.edit(f"""__🩸Prelevo un campione di sangue da {name}.__""")
            await asyncio.sleep(3.0)
            await target.edit(f"""**✅ Fatto!** {name} spero tu non abbia sentito troppo dolore 😇""")
            await asyncio.sleep(2.0)
            await target.edit(f"""__💉 Mando il campione in laboratorio per un'analisi.__""")
            await asyncio.sleep(2.0)
            await target.edit(f"""
                **🧪 Analisi effettuata!**

        😨 {name} sei risultato positivo all'**epatite** di tipo C...

        😰 Siamo tutti con te.🥺""")
        else:
            await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@Client.on_message(filters.user("self") & filters.command("sun","."))
async def sun(client, message):
    try:
        target = message
        info = await client.get_users(message.reply_to_message.from_user.id)
        name = info.first_name
        if message.reply_to_message:
            await target.edit(f"""☀️ ☁️ 

    __💁🏻 "che bella giornata oggi!"__.""")
            await asyncio.sleep(2.0)
            await target.edit(f"""* Arriva {name} *""")
            await asyncio.sleep(2.0)
            await target.edit(f"""⛈🌪💨

    🙎🏻 "ma procodd**""")
        else:
            await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@Client.on_message(filters.user("self") & filters.command("fortuna","."))
async def fortuna(client, message):
    try:
        target = message
        info = await client.get_users(message.reply_to_message.from_user.id)
        name = info.first_name
        random_number = random.randint(0, 100)
        random_num = random.randint(0, 100)
        if message.reply_to_message:
            await target.edit(f"""**☘️ Calcolo della fortuna**

    {name} __sei fortunato o sfortunato!?__
    __🦦 Scopriamolo 😄__""")
            await asyncio.sleep(3.0)
            await target.edit(f"""__🔄 Calcolo in corso...__""")
            await asyncio.sleep(2.0)
            await target.edit(f"""**✅ Calcolo fortuna effettuato**

    ☘️ {name} sei fortunato al {random_number}%.

    👎🏻 {name} sei sfortunato al {random_num}%""")
        else:
            await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
        
@Client.on_message(filters.user("self") & filters.command("win","."))
async def win(client, message):
    target = message
    await target.edit(f"""🚦🚘🚘🚘 3⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 2⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 1⃣""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚦🚘🚘🚘 🏁""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩                 🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩     🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🚩 🚗💨""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🥇🏆 🚘 🏆🥇""")

@Client.on_message(filters.user("self") & filters.command("aereo","."))
async def aereo(client, message):
    target = message
    await target.edit(f"""🛩

        🏢""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🛩
        🏢""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🔥
🔥🏢🔥
     🔥""")
    await asyncio.sleep(1.0)
    await target.edit(f"""💥
💥🏢💥
     💥""")
    await asyncio.sleep(1.0)
    await target.edit(f"""🔥🔥🔥""")

@Client.on_message(filters.user("self") & filters.command("light","."))
async def light(client, message):
    try:
        target = message
        info = await client.get_users(message.reply_to_message.from_user.id)
        name = info.first_name
        random_number = random.randint(0, 456)
        random_num = random.randint(0, 456)
        if message.reply_to_message:
            await target.edit(f"""**✔️ Game Started** 🛗""")
            await asyncio.sleep(2.0)
            await target.edit(f"""👧🏻 : 
    __🟢 Green Light...__""")
            await asyncio.sleep(3.0)
            await target.edit(f"""👧🏻 : 
    **🔴 Red Light!!**""")
            await asyncio.sleep(3.0)
            await target.edit(f"""👀 🤖""")
            await asyncio.sleep(2.0)
            await target.edit(f"""🏃🏻💥🔫""")
            await asyncio.sleep(3.0)
            await target.edit(f"""__Player {name} [{random_number}] eliminated.__""")
        else:
            await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@Client.on_message(filters.user("self") & filters.command("circo","."))
async def circo(client, message):
    try:
        target = message
        info = await client.get_users(message.reply_to_message.from_user.id)
        name = info.first_name
    except:
      await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    try:
      if message.reply_to_message:
        await target.edit(f"""**🤹🏻‍♂️ Er circo generator!**

  🎙 A breve estrarrò **un utente** da questo gruppo, **la persona estratta** sarà definita **"clown del gruppo"**.""")
        await asyncio.sleep(2.0)
        await target.edit(f"""__📤 Sto estraendo la persona...__""")
        await asyncio.sleep(2.0)
        await target.edit(f"""**🤹🏻‍♂️ Er circo generator!**

  **🎉 Complimenti** {name}, sei il nuovo **clown** del gruppo 🤡

  __🎪 Forza sbrigati!! Il circo ti sta aspettando.__""")
      else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")
    except:
      await target.edit(f"""__↪️ Questo comando funziona in reply.__""")

@Client.on_message(filters.user("self") & filters.command("diritti","."))
async def diritti(client, message):
    target = message
    if message.reply_to_message:
      info = await client.get_users(message.reply_to_message.from_user.id)
      name = info.first_name
      await target.edit(f"""**📇 Calcolo dei diritti**

__{name} a breve calcolerò quanti diritti hai!__""")
      await asyncio.sleep(2.0)
      await target.edit(f"""__🗳 Inizio il calcolo...__""")
      await asyncio.sleep(2.0)
      await target.edit(f"""**📈 Calcolo dei diritti terminato**

⚠️❗️⚠️❗️⚠️❗️⚠️❗️⚠️❗️⚠️❗️""")
      await asyncio.sleep(2.0)
      await target.edit(f"""**📈 Calcolo dei diritti terminato**

**__⚠️❗️ Errore nel sistema ❗️⚠️__**

📛 {name} è un utente **senza alcun diritto!**
__👩🏻 Probabilmente è una donna__""")
    else:
        await target.edit(f"""__↪️ Questo comando funziona in reply.__""")




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

async def pastebin(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Errore"}


@Client.on_message(filters.user("self") & filters.command("paste","."))
async def fdasd(client, message):
    pablo = await message.edit("Attendi...")
    tex_t = message.text
    message_s = tex_t
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("Solo i documenti e i testi sono supportati.")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text
    
    ext = "py"
    x = await pastebin(message_s, ext)
    p_link = x["url"]
    p_raw = x["raw"]
    
    pasted = f"**✅ Caricato con successo su pasty**\n\n• [Link]({p_link})\n\n• [Link Raw]({p_raw})"
    await pablo.edit(pasted, disable_web_page_preview=True)




