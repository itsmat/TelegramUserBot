import os
from time import sleep
from pyrogram import Client

try:
    os.remove("my.session")
except Exception:
    pass
try:
    os.remove("bot.session")
except Exception:
    pass
try:
    os.remove("session.session")
except Exception:
    pass

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        pass

def impostaapi():
    clear()
    while True:
        api_id = input("Inserisci app_id: ")
        if str(api_id).isdigit():
            break
        clear()
        print("app_id non valida!")
        sleep(2)
        clear()

    app_hash = input("Inserisci api_hash: ")
    if app_hash:
        creasess(api_id, app_hash)

def creasess(api_id, app_hash):
    app = Client("session", int(api_id), app_hash)
    try:
        clear()
        app.start()
    except Exception:
        clear()
        input("app_id/api_hash/numero di telefono non validi")
        impostaapi()
    session = app.export_session_string()
    print(f"String:\n\n{session}")
    app.stop()



clear()
impostaapi()