from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from datetime import datetime



TOKEN = '8264304458:AAFxYye-sNy4MX8jkbB5R3Vjbs4-seicPAw'

def buscar_cotacao(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resp = requests.get(url).json()
    chave = list(resp.keys())[0]  # Ex: USDBRL, EURBRL, BTCBRL
    return resp[chave]

# Formata data da API
def formatar_data(timestamp):
    dt = datetime.fromtimestamp(int(timestamp) / 1000)
    return dt.strftime("%d/%m/%Y %H:%M")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou o bot de cotações 💱\n\n"
        "Comandos disponíveis:\n"
        "💵 /dolar\n"
        "💶 /euro\n"
        "🪙 /bitcoin"
    )

# -------------------- DÓLAR --------------------
async def dolar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = buscar_cotacao("USD-BRL")

        mensagem = (
            f"💵 *{data['name']}*\n\n"
            f"➡️ *Compra:* R$ {data['bid']}\n"
            f"⬅️ *Venda:* R$ {data['ask']}\n\n"
            f"📈 *Alta:* R$ {data['high']}\n"
            f"📉 *Baixa:* R$ {data['low']}\n\n"
            f"📊 *Variação:* {data['pctChange']}%\n"

        )

        await update.message.reply_text(mensagem, parse_mode="Markdown")

    except:
        await update.message.reply_text("Erro ao buscar cotação do dólar 😢")

# -------------------- EURO --------------------
async def euro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = buscar_cotacao("EUR-BRL")

        mensagem = (
            f"💶 *{data['name']}*\n\n"
            f"➡️ *Compra:* R$ {data['bid']}\n"
            f"⬅️ *Venda:* R$ {data['ask']}\n\n"
            f"📈 *Alta:* R$ {data['high']}\n"
            f"📉 *Baixa:* R$ {data['low']}\n\n"
            f"📊 *Variação:* {data['pctChange']}%\n"
 
        )

        await update.message.reply_text(mensagem, parse_mode="Markdown")

    except:
        await update.message.reply_text("Erro ao buscar cotação do euro 😢")

# -------------------- BITCOIN --------------------
async def bitcoin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = buscar_cotacao("BTC-BRL")

        mensagem = (
            f"🪙 *{data['name']}*\n\n"
            f"➡️ *Compra:* R$ {data['bid']}\n"
            f"⬅️ *Venda:* R$ {data['ask']}\n\n"
            f"📈 *Alta:* R$ {data['high']}\n"
            f"📉 *Baixa:* R$ {data['low']}\n\n"
            f"📊 *Variação:* {data['pctChange']}%\n"
          
        )

        await update.message.reply_text(mensagem, parse_mode="Markdown")

    except:
        await update.message.reply_text("Erro ao buscar cotação do Bitcoin 😢")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dolar", dolar))
    app.add_handler(CommandHandler("euro", euro))
    app.add_handler(CommandHandler("bitcoin", bitcoin))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
