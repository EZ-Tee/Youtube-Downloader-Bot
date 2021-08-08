from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    sticker = "CAACAgEAAxkBAAIeSGELTx2IPwLHPV_aGClOIh2bVzdTAALjAANRKQ05F6bHecKQ5JseBA"
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel ⚒", url="https://t.me/ez_tee_youtibe")],
        [InlineKeyboardButton("Feedback👩‍🔧", url="https://t.me/eztee_chat")]
    ])
    
    await message.reply_sticker(sticker, reply_markup=joinButton)
    raise StopPropagation
