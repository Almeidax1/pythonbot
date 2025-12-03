from telegram.ext import Updater, MessageHandler, Filters
import pandas as pd
from datetime import datetime

# Token do seu bot
TOKEN = '8264304458:AAFxYye-sNy4MX8jkbB5R3Vjbs4-seicPAw'

# Lista para armazenar mensagens
mensagens = []

# Função para salvar no Excel
def salvar_em_excel():
    df = pd.DataFrame(mensagens, columns=['Data', 'Usuário', 'Mensagem'])
    df.to_excel("mensagens_telegram.xlsx", index=False)

# Função que lida com mensagens
def receber_mensagem(update, context):
    usuario = update.message.from_user.username
    texto = update.message.text
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    mensagens.append([data, usuario, texto])
    salvar_em_excel()

    update.message.reply_text("Mensagem salva no Excel!")

# Inicialização do bot
updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, receber_mensagem))

print("Bot em execução...")
updater.start_polling()
updater.idle()

