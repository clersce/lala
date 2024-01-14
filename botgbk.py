import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes,MessageHandler,filters
telegram_token = "6591813378:AAH9uGB2oa_kjHz8u87A7dNivYZkoYJZ63E" 
user_bot = "tester"
listgbk=["Gunting","Batu","Kertas"]

async def no_clue(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ketik /start untuk memulai.")

async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! saya bot tester yang menyediakan game untuk seru-seruan ^o^, klik /gamelist jika kamu ingin tahu apa saja game yang bisa saya lakukan!^o^")

async def  gamelist(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Oke..! ini adalah game yang bisa saya mainkan!! kalau begitu pilihlah game berikut ini !\n1. /Gunting_batu_kertas ")
    

async def gbk(update: Update, context:ContextTypes.DEFAULT_TYPE):   
    await update.message.reply_text("Cara bermain gunting batu kertas ^.^: \n1. Pilihlah antara Gunting/Batu/Kertas \n2. Ketikkan pilihan anda dan send! (Perhatikan huruf kapital!)")

async def gbkstart(update: Update, context:ContextTypes.DEFAULT_TYPE):
    pil_bot = random.choice(listgbk) 
    pil : str = update.message.text
    pil_mu = pil
    if  pil in pil_mu== pil_bot :
        await update.message.reply_text(f"Eitss... Seri!\nBot = {pil_bot}\nKamu = {pil_mu}")
    elif 'Gunting' in pil_mu :
        if pil_bot == "Kertas":
            await update.message.reply_text(f"Well done ! Kamu menang! \n(Bot = {pil_bot})\n(Kamu = {pil_mu})")
        else :
            await update.message.reply_text (f"Nice try! Kamu kalah! \n(Bot = {pil_bot})\n(Kamu = {pil_mu})")   
    elif "Batu" in pil_mu:
        if pil_bot == "Gunting":
            await update.message.reply_text(f"Well done! Kamu menang! \n(Bot = {pil_bot})\n(Kamu = {pil_mu})")
        else :
            await update.message.reply_text (f"Nice try! Kamu kalah! \n(Bot = {pil_bot})\n(Kamu = {pil_mu})")   
    elif "Kertas" in pil_mu:
        if pil_bot == "Batu":
            await update.message.reply_text(f"Well done ! Kamu menang! \n(Bot= {pil_bot})\n(Kamu = {pil_mu})")
        else :
            await update.message.reply_text (f"Nice try ! Kamu kalah! \n(Bot = {pil_bot})\n(Kamu = {pil_mu})")   
    elif (pil_mu == "gunting") or (pil_mu == "batu") or (pil_mu == "kertas") :
        await update.message.reply_text(f"Coba cek huruf kapitalmu...")
    else :
        await update.message.reply_text("Bot tidak mengerti.. klik /start untuk mulai")

async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")

if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(telegram_token).build()
    #command
    app.add_handler(CommandHandler('start', start_command))
   
    app.add_handler(CommandHandler('gamelist', gamelist))
    app.add_handler(CommandHandler('Gunting_batu_kertas', gbk))
    
    #message

    
    app.add_handler(MessageHandler(filters.TEXT, gbkstart))
    
    
    #errorhandler
    app.add_error_handler(error)

    #pengulangan
    app.run_polling(poll_interval=1)

        