from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup,parseMode


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    img = "https://telegra.ph/file/af86973849bc43cc8e3ce.jpg"
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_photo(
img,
welcomed,
parse_mode=ParseMode.MARKDOWN,
disable_web_page_preview=True,
reply_markup=joinButton)
    raise StopPropagation
