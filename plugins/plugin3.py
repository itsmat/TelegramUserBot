from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio, datetime
from pyrogram.errors import * 
from pyrogram.errors import UsernameInvalid
from pyrogram import Client, filters
from pyrogram.raw.functions.messages import StartBot, InstallStickerSet, DeleteHistory
from pytube import YouTube
import os, json, asyncio, requests, traceback, math
from random import randint
from PIL import Image
from gtts import gTTS
import time
import sys
import pyrogram
from pyrogram.raw.functions.messages import StartBot, InstallStickerSet, DeleteHistory
from pyrogram.raw import functions, types
from pyrogram import enums
from pyrogram.types import Message, User
import math
import asyncio
import shutil
import random
from pyrogram import emoji
from pyrogram.errors import FloodWait, MessageNotModified, ChatAdminRequired, UserAdminInvalid, PeerIdInvalid, UserIdInvalid
from pyrogram import emoji
from pyrogram.errors import FloodWait, MessageNotModified, ChatAdminRequired, UserAdminInvalid, PeerIdInvalid, UserIdInvalid
from PIL import Image
from pyrogram import emoji
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.errors import YouBlockedUser, StickersetInvalid
import shlex
import platform
import subprocess
import aiocron
from datetime import datetime
import pytz
import wikipedia
from faker import Faker
from faker.providers import internet
import pyshorteners
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Database:
    def __init__(self, file_name: str):
        self.database = file_name
        if os.path.exists(file_name) == False:
            f = open(file_name, "a+")
            f.write(json.dumps({"word":{}}))
            f.close()
    async def save(self, update: dict):
       f = open(self.database, "w")
       f.write(json.dumps(update))
       f.close()
    async def add_word(self, word: str, risposta: str):
        with open(self.database, "r") as f:
            update = json.load(f)
            update["word"][str(word)] = risposta
            await self.save(update)
            return json.load(open(self.database))["word"][word]

word = Database("word.json")

@Client.on_message(filters.user("self") & filters.command("search","."))
async def wikipediasearch(Client, message):
    event = await message.edit("`Ricerca..`")
    query = get_text(message)
    if not query:
        await event.edit("Sintassi errata")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"• [{s}]({url}) \n"
        except BaseException:
            pass
    await event.edit(
        "✅ Ho cercato {} su wikipedia!: \n\n🔗 Risultati della ricerca: \n\n{}".format(query, result),
        disable_web_page_preview=True,
    )

chatlogg = False
escluselogchat = []

@Client.on_message(filters.user("self") & filters.command("log","."))
async def log(c: Client, m: Message):
    await m.edit("""**⚠️ Aiuto CHAT LOG**

• `.escludilog` » Esclude una chat dal chat log.

• `.approvalog` » Riaggiunge una chat al chat log.

• `.chatlog` » Attiva/Disattiva il chat log.

• `.settalogchat {chatid}` » Imposterà la chat dove mandare i messaggi.
__Per il tag log `.tag`__
""")
@Client.on_message(filters.user("self") & filters.command("escludilog",".") & filters.private)
def escludilog(client, message):
   global escluselogchat
   if not message.chat.id in escluselogchat:
      escluselogchat.append(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} esclusa dal LOG.")
   else:
      message.edit("⚠️ Questa chat è già esclusa.")

@Client.on_message(filters.user("self") & filters.command("approvalog",".") & filters.private)
def approvalog(client, message):
   global escluselogchat
   if message.chat.id in escluselogchat:
      escluselogchat.remove(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} riaggiunta al LOG.")
   else:
      message.edit("⚠️ Questo chat è già stata aggiunta.")



@Client.on_message(filters.user("self") & filters.command("chatlog","."))
async def chatlog(client, message):
    global chatlogg
    if chatlogg == True:
        chatlogg = False
        await message.edit("✅ Modalità CHAT LOG disattivata.")
    else:
        chatlogg = True
        await message.edit("✅ Modalità CHAT LOG attivata.")

canalelogchat = {"canale": "me"}
d = canalelogchat["canale"]
@Client.on_message(filters.user("self") & filters.command("settalogchat","."))
async def settalogchatsettalogchat(client, message):
    global canalelogchat
    if message.text.split(" ")[1]:
        c = message.text.split(" ")[1]
        canalelogchat["canale"] = c
        await message.edit(f"**👥 Manderò i** messaggi menzionati in {c}.")
    else: 
        await message.edit("Utilizza .settalogchat {chatid}")

@Client.on_message(filters.incoming & filters.private)
async def fadfasdasdfafsd(client, message):
        print('Messaggio ricevuto')
        global chatlogg, escluselogchat, chatlogg, escluselogchat
        f = canalelogchat["canale"]
        if chatlogg == True and not message.chat.id in escluselogchat:
            chat_name = message.chat.title
            chat_id = message.chat.id
            tagged_msg_link = message.link
            user_ = f"@{message.from_user.username}" or message.from_user.mention
            TZ = pytz.timezone('Europe/Rome')
            datetime_tz = datetime.now(TZ)
            time_ =  datetime_tz.strftime("`%H:%M:%S` | `%d/%m/%Y`")
            final_tagged_msg = f"""**🔔 Hai ricevuto un messaggio**!
    👤 **Utente:** {user_} [`{chat_id}`]
    🔗 **Link:** [{chat_name}]({tagged_msg_link})
    ⏱ **Orario:** {time_}
    🗯 **Testo:** `{message.text}`
    """
            await client.send_message(f, final_tagged_msg)
            print('Messaggio inoltrato')
            message.continue_propagation()

#

logtag = False
escluse = []
@Client.on_message(filters.user("self") & filters.command("tag","."))
async def taghelp(c: Client, m: Message):
    await m.edit("""**⚠️ Aiuto TAG LOG**

• `.escluditag` » Esclude una chat dal tag log.

• `.approvatag` » Riaggiunge una chat al tag log.

• `.taglog` » Attiva/Disattiva il tag log.

• `.settaglog {chatid}` » Imposterà la chat dove mandare i messaggi.
""")

@Client.on_message(filters.user("self") & filters.command("escluditag",".") & filters.group)
def escluditag(client, message):
   global escluse
   if not message.chat.id in escluse:
      escluse.append(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} esclusa dal TAG LOG.")
   else:
      message.edit("⚠️ Questa chat è già esclusa.")

@Client.on_message(filters.user("self") & filters.command("approvatag",".") & filters.group)
def approvatag(client, message):
   global escluse
   if message.chat.id in escluse:
      escluse.remove(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} riaggiunta al TAG LOG.")
   else:
      message.edit("⚠️ Questo chat è già stata aggiunta.")


@Client.on_message(filters.user("self") & filters.command("taglog","."))
async def fdsa(client, message):
    global logtag
    if logtag == True:
        logtag = False
        await message.edit("✅ Modalità TAG LOG disattivata.")
    else:
        logtag = True
        await message.edit("✅ Modalità TAG LOG attivata.")
logger = {"channel": "me"}
f = logger["channel"]
@Client.on_message(filters.user("self") & filters.command("settaglog","."))
async def settaglog(client, message):
    global channel
    if message.text.split(" ")[1]:
        c = message.text.split(" ")[1]
        logger["channel"] = c
        await message.edit(f"**👥 Manderò i** messaggi menzionati in {c}.")
    else: 
        await message.edit("Utilizza .settaglog {chatid}")


@Client.on_message(filters.mentioned & filters.incoming)
async def mentioned_alert(client, message):
    global logtag, escluse
    f = logger["channel"]
    if logtag == True and not message.chat.id in escluse:
        if not message:
            message.continue_propagation()
            return
        if not message.from_user:
            message.continue_propagation()
            return 
        chat_name = message.chat.title
        chat_id = message.chat.id
        tagged_msg_link = message.link
        user_ = f"@{message.from_user.username}" or message.from_user.mention
        TZ = pytz.timezone('Europe/Rome')
        datetime_tz = datetime.now(TZ)
        time_ =  datetime_tz.strftime("`%H:%M:%S` | `%d/%m/%Y`")
        final_tagged_msg = f"""**🔔 Sei stato taggato**!
👤 **Utente:** {user_} 
👥 **Gruppo:** {chat_name} | `{chat_id}`
🔗 **Link:** [{chat_name}]({tagged_msg_link})
⏱ **Orario:** {time_}
"""
        await client.send_message(f, final_tagged_msg)
        message.continue_propagation()



@Client.on_message(filters.user("self") & filters.command("bin","."))
async def nobin(client, message):
    stark_m = await message.edit("`Attendi!`")
    bin = get_text(message)
    if not bin:
        await stark_m.edit(
            "⚠️ Bin non valido, ricordati di non inserire le 'x'.\n\n<code>.bin 4895041365</code>")
        return
    url = f"https://lookup.binlist.net/{bin}"
    r = requests.get(url=url)
    if r.status_code != 200:
        await stark_m.edit("⚠️ Bin non valido, ricordati di non inserire le 'x'.\n\n<code>.bin 4895041365</code>")
        return
    jr = r.json()
    data_is = (
        f"<b><u>✅ Informazioni ottenute</b></u>\n"
        f"• Bin: <code>{bin}</code> \n"
        f"• Tipologia: <code></code> \n"
        f"• Servizio: <code>{jr.get('scheme', '?')}</code> \n"
        f"• Provenienza: ➠ <code>{jr['country']['name']} {jr['country']['emoji']}</code> \n"
    )
    await stark_m.edit(data_is)


@Client.on_message(filters.user("self") & filters.command("short","."))
async def vom(client, message):
    event = await message.edit( "`🔄 Caricamento...`")
    link = get_text(message)
    if not link:
        await event.edit(
            "⚠️ Errore, utilizza .short {url} e assicurati che l'url sia valido."
        )
        return
    sed = pyshorteners.Shortener()
    kek = sed.dagd.short(link)
    bestisbest = (f'''**✅ Link convertito con successo!**

• 🔗 Originale: {link}
• 🆕 Short: {kek}'''
    )
    await event.edit(bestisbest)

@Client.on_message(filters.user("self") & filters.command("fakeide","."))
async def gen_fake_details(client, message):
    lel = await message.edit("`🔄 Caricamento...`")
    fake = Faker()
    name = str(fake.name())
    fake.add_provider(internet)
    address = str(fake.address())
    ip = fake.ipv4_private()
    cc = fake.credit_card_full()
    email = fake.ascii_free_email()
    job = fake.job()
    android = fake.android_platform_token()
    pc = fake.chrome()
    await lel.edit(
        f"""<b>✅ Identità fittizia generata!</b>

• Nome: <code>{name}</code>
• Indirizzo: <code>{address}</code>
• Email: <code>{email}</code>
• IP: <code>{ip}</code>
• Carta: <code>{cc}</code>
""",
    )

@Client.on_message(filters.user("self") & filters.command("id","."))
async def getids(client, message):
    msg = message.reply_to_message or message
    out_str = f"👥 **Chat ID** : `{(msg.forward_from_chat or msg.chat).id}`\n"
    #out_str += f"💬 **Message ID** : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f"🆔 **ID Utente** : `{msg.from_user.id}`\n"
    await message.edit(out_str)

@Client.on_message(filters.user("self") & filters.command("chatid","."))
async def getchatids(client, message):
    msg = message.reply_to_message or message
    out_str = f"👥 **Chat ID** : `{(msg.forward_from_chat or msg.chat).id}`\n"
    #out_str += f"💬 **Message ID** : `{msg.forward_from_message_id or msg.message_id}`\n"
    await message.edit(out_str)


@Client.on_message(filters.user("self") & filters.command("dev","."))
async def dev(client, message):
  await message.edit("""🧑🏻‍💻 Userbot sviluppato da https://github.com/itsmat
♻️ Canale @ItsMatDev""")

@Client.on_message(filters.user("self") & filters.command("chatinfo","."))
async def chatinfof(client, message):
    if len(message.command) == 2:
        chat = message.command[1]
        ujwal = await client.get_chat(chat)
        msg = "**ℹ️ Informazioni sul gruppo** \n\n"
        msg += f"✍🏻Titolo » {ujwal.title}\n"
        msg += f"🆔Chat ID » `{ujwal.id}` \n"
        msg += f"👥Membri » {ujwal.members_count} \n"
        if ujwal.type == 'supergroup':
            msg += f"ℹ️ Tipo » Supergruppo\n"
        elif ujwal.type == 'channel':
            msg += f"ℹ️ Tipo » Canale\n"
        elif ujwal.type == 'group':
            msg += f"ℹ️ Tipo » gruppo\n"
        if ujwal.username:
            msg += f"🔗 Username » @{ujwal.username}\n"
        else:
            msg += f"🔗 Username » ✖️\n"
        if ujwal.description:
            msg += f"💭Descrizione » `{ujwal.description}`\n\n"
        else:
            msg += f"💭Descrizione » ✖️\n\n"
        await message.edit(msg, disable_web_page_preview=True)
    else:
        chat = message.chat.id
        ujwal = await client.get_chat(chat)
        msg = "**ℹ️ Informazioni sul gruppo** \n\n"
        msg += f"✍🏻Titolo » {ujwal.title}\n"
        msg += f"🆔Chat ID » `{ujwal.id}` \n"
        msg += f"👥Membri » {ujwal.members_count} \n"
        if ujwal.type == 'supergroup':
            msg += f"ℹ️ Tipo » Supergruppo\n"
        elif ujwal.type == 'channel':
            msg += f"ℹ️ Tipo » Canale\n"
        elif ujwal.type == 'group':
            msg += f"ℹ️ Tipo » gruppo\n"
        if ujwal.username:
            msg += f"🔗 Username » @{ujwal.username}\n"
        else:
            msg += f"🔗 Username » ✖️\n"
        if ujwal.description:
            msg += f"💭Descrizione » `{ujwal.description}`\n\n"
        else:
            msg += f"💭Descrizione » ✖️\n\n"
        await message.edit(msg, disable_web_page_preview=True)
    





f = filters.chat([])

@Client.on_message(filters.user("self") & filters.command("autoread","."))
async def autoreada(client, message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit(f"✅ AutoRead disattivato in {message.chat.id}")
    else:
        f.add(message.chat.id)
        await message.edit(f"✅ AutoRead attivato in {message.chat.id}")

@Client.on_message(f)
async def auto_read(client, message):
    await client.read_history(message.chat.id)
    message.continue_propagation()

@Client.on_message(filters.user("self") & filters.command("save","."))
async def save(client, message):
    if message.reply_to_message:
        await message.reply_to_message.forward("me")
        await message.edit("✅ Fatto")
    else:
        await message.edit(f"⚠️ Errore, rispondi ad un messaggio")

@Client.on_message(filters.user("self") & filters.command("purge","."))
def purge(client, message):
    app = client
    count = 0
    msg = message.reply_to_message
    for msg in app.iter_history(message.chat.id, offset_id=msg.message_id, reverse=True):
        app.delete_messages(message.chat.id, msg.message_id)
        count +=1
    purge_complete= app.send_message(msg.chat.id,f'✅ {count} Messaggi eliminati!')
    time.sleep(1)
    app.delete_messages(chat_id=msg.chat.id, message_ids=purge_complete.message_id)

@Client.on_message(filters.user("self") & filters.command("del","."))
async def del_msg(client, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)



async def run_cmd(cmd: str):
    """Run"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
async def convert_to_image(message, client):
    """
    Convert Most Media Formats To Raw Image
    """
    if not message:
        return None
    if not message.reply_to_message:
        return None
    final_path = None
    if not (
        message.reply_to_message.video
        or message.reply_to_message.photo
        or message.reply_to_message.sticker
        or message.reply_to_message.media
        or message.reply_to_message.animation
        or message.reply_to_message.audio
    ):
        return None
    if message.reply_to_message.photo:
        final_path = await message.reply_to_message.download()
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.mime_type == "image/webp":
            final_path = "webp_to_png_s_proton.png"
            path_s = await message.reply_to_message.download()
            im = Image.open(path_s)
            im.save(final_path, "PNG")
        else:
            path_s = await client.download_media(message.reply_to_message)
            final_path = "lottie_proton.png"
            cmd = (
                f"lottie_convert.py --frame 0 -if lottie -of png {path_s} {final_path}"
            )
            await run_cmd(cmd)
    elif message.reply_to_message.audio:
        thumb = message.reply_to_message.audio.thumbs[0].file_id
        final_path = await client.download_media(thumb)
    elif message.reply_to_message.video or message.reply_to_message.animation:
        final_path = "fetched_thumb.png"
        vid_path = await client.download_media(message.reply_to_message)
        await run_cmd(f"ffmpeg -i {vid_path} -filter:v scale=500:500 -an {final_path}")
    return final_path

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@Client.on_message(filters.user("self") & filters.command("addsticker","."))
async def kang_stick(client, message):
    NEXAUB = client
    kang_msg = await message.edit("__Caricamento...__")
    if not message.reply_to_message:
        return await message.edit("⚠️ Rispondi ad uno sticker!")
    if not message.reply_to_message.sticker:
        return await message.edit("⚠️ Rispondi ad uno sticker!")
    a_emoji = get_arg(message)
    pack = 1
    nm = message.from_user.username
    packname = f"@{nm}'s Sticker Pack {pack}"
    packshortname = f"itsmatdev_{message.from_user.id}_{pack}"
    emoji = "🤔"
    try:
        a_emoji = a_emoji.strip()
        if not a_emoji.isalpha():
            if not a_emoji.isnumeric():
                emoji = a_emoji
        else:
            emoji = "🤔"
    except:
        emoji = "🤔"
    exist = None
    is_anim = False
    if message.reply_to_message.sticker:
        if not a_emoji:
            emoji = message.reply_to_message.sticker.emoji or "🤔"
        is_anim = message.reply_to_message.sticker.is_animated
        if is_anim:
            packshortname += f"_animato"
            packname += f"Animato"
        if message.reply_to_message.sticker.mime_type == "application/x-tgsticker":
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
        else:
            cool = await convert_to_image(message, NEXAUB)
            if not cool:
                return await kang_msg.edit("⚠️ Media non supportato")
            file_name = resize_image(cool)
    elif message.reply_to_message.document:
        if message.reply_to_message.document.mime_type == "application/x-tgsticker":
            is_anim = True
            packshortname += f"_animato"
            packname += " Animato"
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
    else:
        cool = await convert_to_image(message, NEXAUB)
        if not cool:
            return await kang_msg.edit("⚠️ Media non supportato")
        file_name = resize_image(cool)
    try:
        exist = await NEXAUB.invoke(
            GetStickerSet(
                stickerset=InputStickerSetShortName(
                    short_name=packshortname
                ),
                hash=0
            )
        )
    except StickersetInvalid:
        pass
    if exist:
        try:
            await NEXAUB.send_message("Stickers", "/addsticker")
        except YouBlockedUser:
            await NEXAUB.edit("Sto sbloccando @Stickers")
            await NEXAUB.unblock_user("Stickers")
            await NEXAUB.send_message("Stickers", "/addsticker")
        await NEXAUB.send_message("Stickers", packshortname)
        await asyncio.sleep(0.2)
        limit = "50" if is_anim else "120"
        messi = (await NEXAUB.get_history("Stickers", 1))[0]
        while limit in messi.text:
            pack += 1
            prev_pack = int(pack) - 1
            await kang_msg.edit(f"🔄 Il pacchetto `{prev_pack}` è completo! Cambio pacchetto in `{pack}`")
            packname = f"@{nm}'s Sticker Pack {pack}"
            packshortname = f"itsmatdev_{message.from_user.id}_{pack}"
            if is_anim:
                packshortname += f"_animato"
            packname += " Animato"
            await NEXAUB.send_message("Stickers", packshortname)
            await asyncio.sleep(0.2)
            messi = (await NEXAUB.get_history("Stickers", 1))[0]
            if messi.text == "Invalid pack selected.":
                if is_anim:
                    await NEXAUB.send_message("Stickers", "/newanimated")
                else:
                    await NEXAUB.send_message("Stickers", "/newpack")
                await asyncio.sleep(0.5)
                await NEXAUB.send_message("Stickers", packname)
                await asyncio.sleep(0.2)
                await NEXAUB.send_document("Stickers", file_name)
                await asyncio.sleep(1)
                await NEXAUB.send_message("Stickers", emoji)
                await asyncio.sleep(0.8)
                await NEXAUB.send_message("Stickers", "/publish")
                if is_anim:
                    await NEXAUB.send_message("Stickers", f"<{packname}>")
                await NEXAUB.send_message("Stickers", "/skip")
                await asyncio.sleep(0.5)
                await NEXAUB.send_message("Stickers", packshortname)
                return await kang_msg.edit("**✅ Sticker aggiunto!**\n__Lo sticker è stato aggiunto al tuo sticker pack con successo.__\nPuoi visualizzare il tuo pacchetto [QUI](https://t.me/addstickers/{})".format(packshortname))
        await NEXAUB.send_document("Stickers", file_name)
        await asyncio.sleep(1)
        await NEXAUB.send_message("Stickers", emoji)
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", "/done")
        await kang_msg.edit("**✅ Sticker aggiunto!**\n__Lo sticker è stato aggiunto al tuo sticker pack con successo.__\nPuoi visualizzare il tuo pacchetto [QUI](https://t.me/addstickers/{})".format(packshortname))
    else:
        if is_anim:
            await NEXAUB.send_message("Stickers", "/newanimated")
        else:
            await NEXAUB.send_message("Stickers", "/newpack")
        await NEXAUB.send_message("Stickers", packname)
        await asyncio.sleep(0.2)
        await NEXAUB.send_document("Stickers", file_name)
        await asyncio.sleep(1)
        await NEXAUB.send_message("Stickers", emoji)
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", "/publish")
        await asyncio.sleep(0.5)
        if is_anim:
            await NEXAUB.send_message("Stickers", f"<{packname}>")
        await NEXAUB.send_message("Stickers", "/skip")
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", packshortname)
        await kang_msg.edit("**✅ Sticker aggiunto!**\n__Lo sticker è stato aggiunto al tuo sticker pack con successo.__\nPuoi visualizzare il tuo pacchetto [QUI](https://t.me/addstickers/{})".format(packshortname))
        try:
            if os.path.exists("ItsMatDev.png"):
                os.remove("ItsMatDev.png")
            downname = "./Downloads"
            if os.path.isdir(downname):
                shutil.rmtree(downname)
        except:
            print("Can't remove downloaded sticker files")
            return


def resize_image(image):
    im = Image.open(image)
    maxsize = (512, 512)
    if (im.width and im.height) < 512:
        size1 = im.width
        size2 = im.height
        if im.width > im.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(maxsize)
    file_name = "ItsMatDev.png"
    im.save(file_name, "PNG")
    if os.path.exists(image):
        os.remove(image)
    return file_name


def get_text(message: Message):
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.user("self") & filters.command("all",".") & filters.group)
async def tagall(client, message):
    msg = await message.edit("`Attendere.....`")
    sh = get_text(message)
    mentions = ""
    async for member in client.iter_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    await message.delete(msg)
    kk = [mentions[i : i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"{i}"
        await client.send_message(message.chat.id, j)

# checkvoip

@Client.on_message(filters.user("self") & filters.command("checkvoip","."))
async def checkvoip(client, message):
    if message.reply_to_message:
        checker = await client.get_users(message.reply_to_message.from_user.id)
        username=checker.username if checker.username else "✖️"
        if checker.dc_id == 4:
            await message.edit(f"""✅ L'utente @{username} **non** risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter {checker.dc_id} 
🌍 Continente: Europa""")
        if checker.dc_id == 1:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: America""")
        if checker.dc_id == 5:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: Asia""")
        if checker.dc_id == 2:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: Non Disponibile""")
        elif checker.dc_id == None:
            await message.edit("""**__⛔️ Datacenter non decifrabile!__**
L'utente su cui vuoi informazioni non ha una foto profilo.""")
    else:
        checker = await client.get_users(message.text.split(" ")[1])
        username=checker.username if checker.username else "✖️"
        if checker.dc_id == 4:
            await message.edit(f"""✅ L'utente @{username} **non** risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter {checker.dc_id} 
🌍 Continente: Europa""")
        if checker.dc_id == 1:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: America""")
        if checker.dc_id == 5:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: Asia""")
        if checker.dc_id == 2:
            await message.edit(f"""❌ L'utente @{username} risulta essere un VoIP.
👤 {checker.mention}
🆔 `{checker.id}`
📡 DataCenter: {checker.dc_id} 
🌍 Continente: Non Disponibile""")
        elif checker.dc_id == None:
            await message.edit("""**__⛔️ Datacenter non decifrabile!__**
L'utente su cui vuoi informazioni non ha una foto profilo.""")


@Client.on_message(filters.user("self") & filters.command("sg","."))
async def sg(client, message):
    if message.reply_to_message:
        resolved = await client.resolve_peer("@SangMataInfo_bot")
        try:
            cc = await message.edit("__Attendi...__")
            await client.send_message(f"@SangMataInfo_bot", f'/search_id {message.reply_to_message.from_user.id}')
            time.sleep(5)
            #await message.reply_to_message.forward("@SangMataInfo_bot")
            msg = await client.get_history("@SangMataInfo_bot")
            await msg[1].forward(message.reply_to_message.chat.id)
            await msg[0].forward(message.reply_to_message.chat.id)
            await message.delete(cc)
        except:
            traceback.print_exc()
            try:
                await message.edit("⚠️ Errore")
            except:
                await client.send_message(message.reply_to_message.chat.id, "⚠️ Errore")
    else:
        await message.edit("Rispondi al messaggio di un utente.")
# afk
afk = False
approve = []
text = {"mex": "Messaggio AFK"}
@Client.on_message(filters.user("self") & filters.command("msgafk","."))
async def fdghnsdnsfgngsdf(client, message):
   global text
   p = message.text.replace(".msgafk", "")
   text["mex"] = p
   await message.edit(f"✅ Messaggio AFK impostato.")
@Client.on_message(filters.user("self") & filters.command("afk",".") )
async def setAFK(client, message):
   global afk
   if afk == True:
      afk = False
      await message.edit("✅ Modalità AFK disattivata.")
   else:
      afk = True
      await message.edit("*✅ Modalità AFK attivata.")

status = False
@Client.on_message(filters.user("self") & filters.command("autostatus","."))
async def safasfas(client, message):
    global status
    if not status:
        status = True
        await message.edit(f"✅ Autostatus attivato")
    else:
        status = False
        await message.edit("❌ Autostatus disabilitato")
@Client.on_user_status()
async def auto(client, message):
    global statusafk
    global afk
    if statusafk:
        p = await client.get_me()
        if p.status == "online":
            afk = False
            print('sono online, afk off')
        else:
            afk = True
            print('sono offline, afk on')
    global status
    if status:
        p = await client.get_me()
        if p.status == "online":
            if not p.last_name == "[Online]":
                await client.update_profile(last_name="[Online]")
                print('online')
        else:
            if not p.last_name == "[Offline]":
                await client.update_profile(last_name="[Offline]")
                print('offline')


statusafk = False
@Client.on_message(filters.user("self") & filters.command("autostatusafk","."))
async def dfsfadsdfassdf(client, message):
    global statusafk
    if not statusafk:
        statusafk = True
        await message.edit(f"✅ Autostatus AFK attivato")
    else:
        statusafk = False
        await message.edit("❌ Autostatus AFK disabilitato")


@Client.on_message(filters.incoming & filters.private & ~filters.bot, group=-1)
async def funzioneafk(client, message):
   global afk, approve, text
   if afk == True and not message.chat.id in approve:
      await message.reply_text(text["mex"], quote=False)
      await client.forward_messages(
    chat_id=message.chat.id,
    from_chat_id=-1001545761956,
    message_ids=6
)

@Client.on_message(filters.user("self") & filters.command("approve",".") & filters.private & ~filters.bot)
def accept(client, message):
   global approve
   if not message.chat.id in approve:
      approve.append(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} approvata.")
   else:
      message.edit("⚠️ Questa chat è già approvata.")
@Client.on_message(filters.user("self") & filters.command("disapprove",".") & filters.private & ~filters.bot)
def disapprove(client, message):
   global approve
   if message.chat.id in approve:
      approve.remove(message.chat.id)
      message.edit(f"✅ Chat {message.chat.id} disapprovata.")
   else:
      message.edit("⚠️ Questo utente non è approvato.")
#gmex
gruppi = {"group": []}
@Client.on_message(filters.user("self") & filters.command("addgroup","."))
async def addg(client, message):
   global gruppi
   p = message.text.split(" ")[1]
   info = await client.get_chat(p)
   gruppi["group"].append(info.id)
   await message.edit(f"✅ Chat {info.id} aggiunta alla lista gruppi del gmex.")
@Client.on_message(filters.user("self") & filters.command("remgroup","."))
async def remg(client, message):
   global gruppi
   p = message.text.split(" ")[1]
   info = await client.get_chat(p)
   gruppi["group"].remove(info.id)
   await message.edit(f"✅ Chat {info.id} rimossa dalle lista gruppi del gmex.")

@Client.on_message(filters.user("self") & filters.command("gmex","."))
async def remg(client, message):
   global gruppi
   p = message.text.replace(".gmex", "")
   for g in gruppi["group"]:
       try:
           await client.send_message(g, p)
           await message.edit("✅ Gmex completato con successo.")
       except:
           await message.edit("❌ Errore")
#mute
mutati = []
textsmute = {"mex": "msg mute."}

@Client.on_message(filters.user("self") & filters.command("msgmute","."))
async def setmute(client, message): 
   global textsmute
   p = message.text.replace(".msgmute", "")
   textsmute["mex"] = p
   await message.edit(f"✅ Messaggio .mute impostato.")

@Client.on_message(filters.user("self") & filters.command("mute","."))
async def mute(client, message):
   global mutati
   global textsmute
   textss = textsmute["mex"]
   if message.chat.id in mutati:
      await message.edit("❌ Utente già mutato")
   else:
      mutati.append(message.chat.id)
      await message.edit(textss)

textsunmute = {"mex": "msg unmute"}
@Client.on_message(filters.user("self") & filters.command("msgunmute","."))
async def msgunmute(client, message):
   global textsunmute
   p = message.text.replace(".msgunmute", "")
   textsunmute["mex"] = p
   await message.edit(f"✅ Messaggio .unmute impostato.")

@Client.on_message(filters.user("self") & filters.command("unmute","."))
def unmute(client, message):
   global mutati
   global textsunmute
   textss = textsunmute["mex"]
   if message.chat.id in mutati:
      mutati.remove(message.chat.id)
      message.edit(textss)
   else:
      message.edit("✅ L'utente non è mutato")
@Client.on_message(filters.incoming & filters.private)
async def delete(client, message):
   global mutati
   if message.chat.id in mutati:
      await message.delete()
#info



WHOIS = (
    '**ℹ️ INFO UTENTE ℹ️**\n\n'
    "**• 🧑🏻Nome:** {first_name}\n"
    "**• 🔖Cognome:** {last_name}\n"
    "**• 🌐Username**: @{username}\n"
    "**• 🆔ID**: `{user_id}`\n"
    '**• 📡DC:** {user_dc}\n'
    "**• 🔗Permalink:** [{first_name}](tg://user?id={user_id})\n\n"
    "**• 📖Bio:**\n`{bio}`"
)

WHOIS_PIC = (
    '**ℹ️ INFO UTENTE ℹ️**\n\n'
    "**• 🧑🏻Nome:** {first_name}\n"
    "**• 🔖Cognome:** {last_name}\n"
    "**• 🌐Username**: @{username}\n"
    "**• 🆔ID**: `{user_id}`\n"
    '**• 📡DC:** {user_dc}\n'
    "**• 🔗Permalink:** [{first_name}](tg://user?id={user_id})\n\n"
    "**• 📖Bio:**\n`{bio}`"
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.last_online_date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )



def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic[0].date).strftime("%d.%m.%Y, %H:%M:%S")


@Client.on_message(filters.command("whois", [".", ""]) & filters.me)
async def who_is(client, message):
    bot = client
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await bot.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("I don't know that User.")
        await asyncio.sleep(2)
        await message.delete()
        return

    user_details = await bot.get_chat(get_user)
    bio = user_details.bio
    pic_count = await bot.get_chat_photos_count(user.id)

    if not user.photo:
        await message.edit(
            WHOIS.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "✖️",
                username=user.username if user.username else "✖️",
                last_online=LastOnline(user),
                bio=bio if bio else "✖️",
                user_dc=user.dc_id if user.dc_id else "✖️"
            ),
            disable_web_page_preview=True,
        )
    elif user.photo:
        await bot.send_message(
            message.chat.id,
            text=WHOIS_PIC.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "✖️",
                username=user.username if user.username else "✖️",
                last_online=LastOnline(user),
                bio=bio if bio else "✖️",
                user_dc=user.dc_id if user.dc_id else "✖️"
            ),
        )

        await message.delete()


























































#netban
@Client.on_message(filters.user("self") & filters.command("netb","."))
async def netban(client, message):
   await message.delete()
   scammer = message.text.split(" ")[1]
   motivo = message.text.replace(f".netb {scammer}", "")
   a = await client.get_users(scammer)
   await client.send_message(message.chat.id,
   f"""
**⚠️UTENTE NETBANNATO⚠️**

👤Nome » {a.first_name}
📧Username » @{a.username} 
🆔ID Utente » `{a.id}`

👮🏻‍♂Admin » [{message.from_user.first_name}](tg://user?id={message.from_user.id})
📝Motivazione » {motivo} 

<a href='t.me/netbanbro'>🗂Prove</a>
""", disable_web_page_preview=True)
#covid


@Client.on_message(filters.user("self") & filters.command("covid","."))
async def sdfassdf(client, message):
    citta = message.text.split(" ")[1]
    link = requests.get(f"https://covid-api.mmediagroup.fr/v1/cases?country={citta}")
    js = json.loads(link.text)
    contagi = js["All"]["confirmed"]
    ricoverati = js["All"]["recovered"]
    morti = js["All"]["deaths"]
    await message.edit(f"""**🇮Info sul corona virus in {citta}:**
**😷 Contagiati:** {contagi}
**☠️ Morti:** {morti}
""")

#font ez

#btc
@Client.on_message(filters.user("self") & filters.command("btc","."))
async def btc(client, message):
   await message.edit("**Valore dei BitCoin in Italia 🇮🇹:\n\n " + str(requests.get("https://blockchain.info/ticker").json()["EUR"]["last"]) + "€")



#tts
@Client.on_message(filters.user("self") & filters.command("tts","."))
async def tts(client, message):
   k = message.text.split(" ", 1)
   if k.__len__() == 2:
      await message.delete()
      tts = gTTS(text=k[1], lang='it')
      tts.save("tts.ogg")
      await client.send_voice(message.chat.id, "tts.ogg")
      os.remove("tts.ogg")
   else:
      await message.edit("⚠️ Errore, utilizza .tts {testo}")
# stats

@Client.on_message(filters.user("self") & filters.command("stats","."))
async def stats(client, message):
    await message.edit("<i>🔄 Caricamento...</i>")
    private, gruppi, canali, sg, bots = 0, 0, 0, 0, 0
    async for dialog in client.get_dialogs():
        print(dialog.chat.first_name or dialog.chat.title)
        if dialog.chat.type in [enums.ChatType.PRIVATE]:
            private = private + 1
        elif dialog.chat.type in [enums.ChatType.BOT]:
            bots = bots + 1
        elif dialog.chat.type in [enums.ChatType.GROUP]:
            gruppi = gruppi + 1
        elif dialog.chat.type in [enums.ChatType.CHANNEL]:
            canali = canali + 1
        elif dialog.chat.type in [enums.ChatType.SUPERGROUP]:
            sg = sg + 1
    await asyncio.sleep(0.02)
    await message.edit(f"**📊 Statistiche di **[{message.from_user.first_name}](tg://user?id={message.from_user.id}):\n\n**👤 Chat Private: {private}\n🤖 Bot: {bots}\n🔝 Super Gruppi: {sg}\n📣 Canali: {canali}\n👥 Gruppi Privati: {gruppi}**")
# status


@Client.on_message(filters.user("self") & filters.command("status","."))
async def safasfasda(client, message):
    await message.edit(f"**UserBot online****")

@Client.on_message(filters.user("self") & filters.command("online","."))
async def online(client, message):
   await client.update_profile(last_name="[Online]")
   await message.edit("✅ Stato impostato su <u><b>ONLINE!</b></u>")
#Offline
@Client.on_message(filters.user("self") & filters.command("offline","."))
async def off(client, message):
   await client.update_profile(last_name="[Offline]")
   await message.edit("✅ Stato impostato su <u><b>OFFLINE!</b></u>")

@Client.on_message(filters.user("self") & filters.command("unstato","."))
async def delst(client, message):
   await client.update_profile(last_name="")
   await message.edit("Status rimosso")
@Client.on_message(filters.user("self") & filters.command("nome","."))
async def sfddsfsdf(client, message):
    p = message.text.split(" ")[1]
    await client.update_profile(first_name=p)
    await message.edit(f"""✅ Nome modificato con successo.

💬 Nome attuale:
{p}""")
# cognome
@Client.on_message(filters.user("self") & filters.command("cognome","."))
async def dfsgdfgssdg(client, message):
    p = message.text.split(" ")[1]
    await client.update_profile(last_name=p)
    await message.edit(f"""✅ Cognome modificato con successo.

💬 Cognome attuale:
{p}""")
# bio
@Client.on_message(filters.user("self") & filters.command("bio","."))
async def sdfgsdfgdgsf(client, message):
    p = message.text.replace(".bio", "")
    await client.update_profile(bio=p)
    await message.edit(f"""✅ Biografia modificata con successo.

💬 Biografia attuale:
{p}""")
st = False
ok = {"text": "Orario"}

@Client.on_message(filters.command(['help'], ['!','.','/']) & filters.me)
async def help(client, message):
    await message.edit("<a href='https://telegra.ph/Comandi-userbot-04-28'>🔗Clicca qui</a>", disable_web_page_preview=True)

@Client.on_message(filters.command(['comandi'], ['!','.','/']) & filters.me)
async def comandi(client, message):
    await message.edit("<a href='https://telegra.ph/Comandi-userbot-04-28'>🔗Clicca qui</a>", disable_web_page_preview=True)


@Client.on_message(filters.command(['cmd'], ['!','.','/']) & filters.me)
async def cmd_list(client, message):
    await message.edit("<a href='https://telegra.ph/Comandi-userbot-04-28'>🔗Clicca qui</a>", disable_web_page_preview=True)
# qbot
@Client.on_message(filters.user("self") & filters.command("qbot","."))
async def qbot(client, message):
    if message.reply_to_message:
        resolved = await client.resolve_peer("@QuotLyBot")
        try:
            await message.edit("__Attendi...__")
            await message.reply_to_message.forward("@QuotLyBot")
            time.sleep(5)
            await message.reply_to_message.forward("@QuotLyBot")
            await message.delete()
            msg = await client.get_history("@QuotLyBot")
            await msg[1].forward(message.reply_to_message.chat.id)
        except:
            traceback.print_exc()
            try:
                await message.edit("⚠️ Errore")
            except:
                await client.send_message(message.reply_to_message.chat.id, "⚠️ Errore")
    else:
        await message.edit("Rispondi al messaggio di un utente.")
# auto-status
# block unbock msg
texts = {"mex": "✅ bloccato correttamente."}
@Client.on_message(filters.user("self") & filters.command("msgblock","."))
async def setblock(client, message):
   global texts
   p = message.text.replace(".msgblock", "")
   texts["mex"] = p
   await message.edit(f"✅ Messaggio .block impostato.")


@Client.on_message(filters.user("self") & filters.command("block","."))
async def dasgsgdf(client, message):
    global texts
    textss = texts["mex"]
    if message.reply_to_message:
        try:
            await client.block_user(message.reply_to_message.from_user.id)
            await message.edit(textss)
        except:
            await message.edit("L'utente è già bloccato")
    else:
        try:
            await client.block_user(message.chat.id)
            await message.edit(textss)
        except:
            await message.edit("L'utente è già bloccato")


@Client.on_message(filters.user("self") & filters.command("unblock","."))
async def sdfdsfsf(client, message):
    if message.reply_to_message:
        chatid = message.reply_to_message.from_user.id
        info = await client.get_users(message.reply_to_message.from_user.id)
        unb = f'✅ {info.first_name} [`{chatid}`] sbloccato correttamente.'
        try:
            await client.unblock_user(message.reply_to_message.from_user.id)
            await message.edit(unb)
        except:
            await message.edit("L'utente non è bloccato")
    else:
        chatid = message.chat.id
        unb = f'✅ {message.chat.first_name} [`{chatid}`] sbloccato correttamente.'
        try:
            await client.unblock_user(message.chat.id)
            await message.edit(unb)
        except:
            await message.edit("L'utente non è bloccato")


# id and chat id


# verify
@Client.on_message(filters.user("self") & filters.command("verify","."))
def verifys(client, message):
    resolved = client.resolve_peer("@spambot")
    client.invoke(StartBot(bot=resolved, peer=resolved, random_id=randint(1000, 9999), start_param="e"))
    #avvia spam bot
    time.sleep(1)
    msg = client.get_chat_history("@spambot", 1)[0] #getta la risposta di spambot
    if msg.text.find("Good news") > -1 or msg.text.find("Buone notizie") > -1:
        message.edit("✅ Al momento non esiste alcuna limitazione sul tuo account.")
    else:
        message.edit("❌ Sei limitato")
# spam
@Client.on_message(filters.user("self") & filters.command("spam","."))
async def spam(client, message):
    await message.delete()
    n = message.text.split(" ")[1]
    r = message.text.replace(f".spam {n}", "")
    a = 0
    while a < int(n):
        a += 1
        await client.send_message(message.chat.id, r)
# forward
channel = {"channel": "vuoto"}
@Client.on_message(filters.user("self") & filters.command("setforward","."))
async def fsdasdfsdf(client, message):
    global channel
    if message.text.split(" ")[1]:
        c = message.text.split(" ")[1]
        channel["channel"] = c
        await message.edit(f"**👥 Inoltrerò i** messaggi in {c}.")
    else: 
        await message.edit("Utilizza .setforward {chatid}")

@Client.on_message(filters.user("self") & filters.command("forward","."))
async def fw(client, message):
    global channel
    if not channel["channel"] == "vuoto":
        if message.reply_to_message:
            try:
                f = channel["channel"]
                await message.reply_to_message.forward(f)
                await message.edit(f"**💭 Messaggio inoltrato correttamente in {f} .")
            except PeerIdInvalid:
                await message.edit("⚠️ Errore, controlla se sei admin nel canale o se l'id inserito è corretto")
            except UsernameInvalid:
                await message.edit("⚠️ Errore, controlla se sei admin nel canale o se l'id inserito è corretto")
            except:
                traceback.print_exc()
                await message.edit("⚠️ Errore, controlla se sei admin nel canale o se l'id inserito è corretto")
        else:
            await message.edit("⚠️ Errore, devi rispondere ad un messaggio")
    else:
        await message.edit("⚠️ Errore, nessun canale impostato")
# kickme

kickmetxt = {"mex": "Io vado via👋"}
@Client.on_message(filters.user("self") & filters.command("msgkickme","."))
async def setKickme(client, message):
   global kickmetxt
   p = message.text.replace(".msgkickme", "")
   kickmetxt["mex"] = p
   await message.edit(f"✅ Messaggio .kickme impostato.")

@Client.on_message(filters.user("self") & filters.command("kickme",".") & filters.group)
async def kickme(client, message):
    global kickmetxt
    try:
        await message.edit(kickmetxt["mex"])
        await client.leave_chat(message.chat.id, delete=True)
    except:
        pass

# filtri
@Client.on_message(filters.user("self") & filters.command("addfiltro","."))
async def setReply(client, message):
	with open("word.json", "r") as f:
		Commands = json.load(f)
		p = message.text.split(" ")[1]
		if not p in Commands["word"]:
			await word.add_word(p, message.text.replace(f".addfiltro {p}", ""))
			await message.edit(f"✅ Filtro {p} aggiunto.")
		else:
			await message.edit(f"⚠️ Filtro {p} già presente")

@Client.on_message(filters.user("self") & filters.command("remfiltro","."))
async def delReply(client, message):
	with open("word.json", "r") as f:
		Commands = json.load(f)
	p = message.text.split(" ")[1]
	if p in Commands["word"]:
		del Commands["word"][p]
		with open("word.json", "w+") as f:
			json.dump(Commands, f)
		await message.edit(f"✅ Filtro {p} rimosso.")
	else:
		await message.edit(f"⚠️ Il filtro {p} è inesistente.")


@Client.on_message(filters.user("self") & filters.command("filtri","."))
async def replyList(client, message):
	with open("word.json", "r") as f:
		Commands = json.load(f)
	mex = "**✍🏻 Lista filtri**\n"
	for i in Commands["word"]:
		mex += f"\n- {i}"
	await message.edit(mex)


@Client.on_message(filters.text & filters.user("self"))
async def Reply(client, message):
    update = json.load(open("word.json"))
    if message.text in update["word"].keys():
        reply = update["word"][f"{message.text}"]
        await message.edit(f"{reply}", disable_web_page_preview=True)
