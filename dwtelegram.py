import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters # pip install python-telegram-bot==13.7
with open('tokentelegram.txt', 'r') as file:
        tokent = file.read()
# Definisci la funzione che gestirà il comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ciao! Inviami un video e lo salverò con un nome.")

# Definisci la funzione che gestirà i messaggi contenenti video
def save_video(update, context):
    follength = len([f for f in os.listdir("vid/")if os.path.isfile(os.path.join("vid/", f))])
    video = update.message.video
    file_name = str(follength+1)+".mp4"
    video_file = context.bot.get_file(video.file_id)
    file_path = "vid/"+ file_name
    video_file.download(file_path)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ho salvato il video come {file_name}.")

# Crea un oggetto Updater e passa il token del tuo bot
updater = Updater(token=str(tokent), use_context=True)

# Ottieni il dispatcher per registrare i gestori di comandi e messaggi
dispatcher = updater.dispatcher

# Aggiungi un gestore per il comando /start
dispatcher.add_handler(CommandHandler('start', start))

# Aggiungi un gestore per i messaggi contenenti video
dispatcher.add_handler(MessageHandler(Filters.video, save_video))

# Avvia il bot
updater.start_polling()