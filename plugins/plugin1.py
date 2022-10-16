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
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import *
import re
import asyncio
import sys
from os import environ, execle, path, remove
import asyncio
import time
from pyrogram.raw import functions, types
from pyrogram.errors import FloodWait


@Client.on_message(filters.command(['read'], ['.']) & filters.me)
async def dfssdfnsdfhjsdf(c: Client, m: Message):
    await m.edit("""**⚠️ Tipologie di Read**

• `.readall` » Legge tutti i messaggi di tutti i gruppi e canali in cui sei membro su Telegram.

• `.readalltag` » Legge tutte le menzioni (@) di tutti i gruppi e canali in cui sei membro su Telegram.

• `.readtag` » Legge tutte le menzioni (@) in un gruppo specifico.

• `.unread` » Imposterà la chat come non letta.

• `.autoread` » Abiliterà l'autoread automaticamente in una determinata chat.
""")

@Client.on_message(filters.command(['broadcast'], ['.']) & filters.me)
async def broadcast(c: Client, m: Message):
    await m.edit("""**⚠️ Tipologie di Broadcast**

• `.broadcastall {messaggio}` » Invierà un messaggio ovunque.

• `.broadcastg {messaggio}` » Invierà un messaggio a tutti i gruppi e supergruppi.

• `.broadcastc {messaggio}` » Invierà un messaggio a tutti i canali nei quali siete admin.""")

@Client.on_message(filters.command(['readalltag'], ['.']) & filters.me)
async def readtuttetag(c: Client, m: Message):
    request = functions.messages.GetAllChats(except_ids=[])
    try:
        result = await c.invoke(request)
    except FloodWait as e:
        await m.edit_text(
            f"⏳ Attendi {e.x} secondi"
        )
        return
    await m.edit("`🔄 Caricamento.`")
    time.sleep(1)
    await m.edit("`🔄 Caricamento..`")
    time.sleep(1)
    await m.edit("`🔄 Caricamento...`")
    for chat in result.chats:
        if type(chat) is types.Chat:
            peer_id = -chat.id
        elif type(chat) is types.Channel:
            peer_id = int(f"-100{chat.id}")
        peer = await c.resolve_peer(peer_id)
        request = functions.messages.ReadMentions(peer=peer)
        await c.invoke(request)
    await m.edit("✅👀 Ho letto tutte le **menzioni** di **tutti i gruppi**")

@Client.on_message(filters.command(['readall'], ['.']) & filters.me)
async def read(c: Client, m: Message):
    request = functions.messages.GetAllChats(except_ids=[])
    try:
        result = await c.invoke(request)
    except FloodWait as e:
        await m.edit_text(
            f"⏳ Attendi {e.x} secondi"
        )
        return
    await m.edit("`🔄 Caricamento.`")
    time.sleep(1)
    await m.edit("`🔄 Caricamento..`")
    time.sleep(1)
    await m.edit("`🔄 Caricamento...`")
    for chat in result.chats:
        if type(chat) is types.Chat:
            peer_id = -chat.id
        elif type(chat) is types.Channel:
            peer_id = int(f"-100{chat.id}")
        peer = await c.resolve_peer(peer_id)
        await c.read_chat_history(chat_id=peer_id)

    await m.edit("✅💬 Ho letto tutti i **messaggi** di **tutti i gruppi**")

@Client.on_message(filters.command(['readtag'], ['.']) & filters.me)
async def rrreadtag(c: Client, m: Message):
    await m.edit("`🔄 Caricamento.`")
    time.sleep(1)
    await m.edit("`🔄 Caricamento..`")
    peer = await c.resolve_peer(m.chat.id)
    request = functions.messages.ReadMentions(peer=peer)
    await c.invoke(request)
    await m.edit(f"✅👀 Ho letto tutte le **menzioni** di `{m.chat.id}`.")


@Client.on_message(filters.command(['broadcastall'], ['.']) & filters.me)
async def broadcccast(client, message):
    cmd = message.text.replace(".broadcastall", "")
    try:
        msg = cmd
        async for d in client.iter_dialogs():
            try:
                await client.send_message(chat_id=d.chat.id, text=msg)
            except:
                continue
    except Exception as error:
        await client.send_message(message.chat['id'],reply_to_message_id=int(message.message_id),text="⚠️ Errore")

@Client.on_message(filters.command(['broadcastg'], ['.']) & filters.me)
async def ghsdfq(client, message):
    cmd = message.text.replace(".broadcastg", "")
    msg = cmd
    groups = ["supergroup","group"]
    async for d in client.iter_dialogs():
        if d.chat.type in groups:
            try:
                await client.send_message(chat_id=d.chat.id, text=msg)
            except Exception as error:
                continue

@Client.on_message(filters.command(['broadcastc'], ['.']) & filters.me)
async def gsdfdgsf(client, message):
    cmd = message.text.replace(".broadcastc", "")
    msg = cmd
    groups = ["channel"]
    async for d in client.iter_dialogs():
        if d.chat.type in groups:
            try:
                await client.send_message(chat_id=d.chat.id, text=msg)
            except Exception as error:
                continue



@Client.on_message(filters.command(['unread'], ['.']) & filters.me)
async def sdfgsdfgsdgf(client, message):
    await message.delete()
    await asyncio.gather(
        client.invoke(
            functions.messages.MarkDialogUnread(
                peer=await client.resolve_peer(message.chat.id), unread=True
            )
        ),
    await client.send_message('me', f"✅👀 Ho impostato `{message.chat.id}` nelle chat **da leggere**")
    )

@Client.on_message(filters.command(['gethtml'], ['.']) & filters.me)
async def gethtml(client, message):
    if message.reply_to_message:
        await message.delete()
        msg = message.reply_to_message.text.markdown
        await message.reply(message.reply_to_message.text.html, parse_mode = 'markdown')
    else:
        await message.edit('⚠️ Rispondi ad un messaggio')
        

@Client.on_message(
    filters.command(["screenshot", "ss"], ".") & filters.private & filters.me
)
async def screenshot(client, message):
    await asyncio.gather(
        message.delete(),
        client.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=client.rnd_id(),
            )
        ),
    )





@Client.on_message(
    filters.command(["restart", "riavvia"], ".") & filters.private & filters.me
)
async def rerreerstart(client, message):
    await message.edit('''⚠️ Comando temporaneamente disabilitato.''')
'''    args = [sys.executable, "main.py"]
    execle(sys.executable, *args, environ)
    exit()
    return
'''
