from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineQuery, Update


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", callback_data="help")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = "Hey <b>{message.from_user.first_name}</b>\n/help for More info"
await message.reply_text(
welcomed,
reply_markup=joinButton)

@Client.on_callback_query()
async def button(Client, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Client, update.message)

    raise StopPropagation
