import telegram
from telegram.ext import Updater
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
import datetime
#iniciar
TOKEN = '5203805100:AAFgpxynY_DP4BLvtHm2pzE50bjX7UV0jvc'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bot = telegram.Bot(token=TOKEN)

#start
start_txt = "Olá 👋! Eu sou o bot de lembretes, e posso te ajudar a lembrar das coisas que você esquecer 😉! A lista de comandos está disponível em /comandos."
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=start_txt)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#comandos
def comandos(update: Update, context: CallbackContext):
    comandos = "/comandos"
    lembrar = "/lembrar"
    lista_comandos = (f"""
    Lista de Comandos:
    - comandos({comandos}): Mostra esta lista de comandos
    - lembrar({lembrar}): Faz o bot te lembrar de alguma coisa na data escolhida. Para usar basta digitar:
    /comandos DIA MÊS ANO 
    """)
    context.bot.send_message(chat_id=update.effective_chat.id, text=lista_comandos)
comandos_handler = CommandHandler('comandos', comandos)
dispatcher.add_handler(comandos_handler)
#twitter
def twitter(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Twitter do criador: https://www.twitter.com/yanchagas04/")
twt_handler = CommandHandler('twitter', twitter)
dispatcher.add_handler(twt_handler)
#instagram
def instagram(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Instagram do criador: https://www.instagram.com/yanchagas04/")
insta_handler = CommandHandler('instagram', instagram)
dispatcher.add_handler(insta_handler)
#lembrar
def lembrar(update: Update, context: CallbackContext):
    dia = (context.args[0])
    mês = (context.args[1])
    ano = (context.args[2])
    data_informada = [ano, mês, dia]
    data = "-".join(data_informada)
    data_agora = datetime.datetime.now()
    separar = data_agora.date()
    dia_sistema = str(separar.day)
    mes_sistema = str(separar.month)
    ano_sistema = str(separar.year)
    Lista = [ano_sistema, mes_sistema, dia_sistema]
    data_sistema = "-".join(Lista)
    msg = " ".join(context.args[3:])
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"OK! Iremos te lembrar disso em: {dia}/{mês}/{ano} ")
    while True:
        if data_sistema == data:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Olha o lembrete 🗞! Você me pediu pra lembrá-lo(a) hoje que: {msg}")
            break
lembrar_handler = CommandHandler('lembrar', lembrar)
dispatcher.add_handler(lembrar_handler)

"""
MODELO:
def twitter(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Twitter do criador: https://www.twitter.com/yanchagas04/")
twt_handler = CommandHandler('twitter', twitter)
dispatcher.add_handler(twt_handler)"""

updater.start_polling()

#iniciar o bot:
