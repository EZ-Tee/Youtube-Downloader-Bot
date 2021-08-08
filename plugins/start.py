from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    sticke = "https://telegra.ph/file/af86973849bc43cc8e3ce.jpg"
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel ⚒", url="https://t.me/ez_tee_youtibe")],
        [InlineKeyboardButton("Feedback👩‍🔧", url="https://t.me/eztee_chat")]
    ])
    
    await message.reply_photo(
        sticke,
        reply_markup=joinButton)
    raise StopPropagation
