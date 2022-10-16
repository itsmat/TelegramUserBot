from pyrogram import Client 

Client = Client(
    'nomesessione', #nome sessione
    session_string = 'ab123c', #string session che ricavi da generatorestring.py avviandolo
    api_id = 123, #api id che prendi da my.telegram.org
    api_hash = "abc", #api hash che prendi da my.telegram.org
    plugins = dict(root="plugins") #cartella dei plugins
)

if __name__ == "__main__":
    Client.run()
