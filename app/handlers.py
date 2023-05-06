import aiogram
import messages
import config
import instagrapi
import re

from misc import dispatcher

vendor_code_regepxp = re.compile(r'\d{6,10}')

instagram_client = instagrapi.Client()
instagram_client.login(config.INSTAGRAM_LOGIN, config.INSTAGRAM_PASSWORD)

@dispatcher.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    return await message.answer(messages.HELLO_MESSAGE)

@dispatcher.message_handler()
async def handle_url(message: aiogram.types.Message):
    instagram_post_url = message.text.strip()
    try:
        media_pk = instagram_client.media_pk_from_url(instagram_post_url)
        media_id = instagram_client.media_id(media_pk=media_pk)
        media_info = instagram_client.media_info(media_pk=media_pk)

        caption = media_info.caption_text

        find_from_caption = re.findall(vendor_code_regepxp, caption)

        if find_from_caption:
            if len(find_from_caption) == 1:
                return await message.reply(messages.FOUND_URL.format(find_from_caption[0]))
            else:
                inline_keyboard = aiogram.types.InlineKeyboardMarkup(row_width=1)
                for code in find_from_caption:
                    inline_keyboard.add(aiogram.types.InlineKeyboardButton(text=code, url=messages.FOUND_URL.format(code)))
                return await message.reply(text=messages.FOUND.format(len(find_from_caption)), reply_markup=inline_keyboard)


        comments = instagram_client.media_comments(media_id=media_id, amount=20) #? 0 = all
        if found_vendor_codes := list(set(filter(lambda comment: re.findall(vendor_code_regepxp, comment.text), comments))):
            if len(found_vendor_codes) == 1:
                return await message.reply(messages.FOUND_URL.format(find_from_caption[0]))
            else:
                inline_keyboard = aiogram.types.InlineKeyboardMarkup(row_width=1)
                for code in found_vendor_codes:
                    inline_keyboard.add(aiogram.types.InlineKeyboardButton(text=code, url=messages.FOUND_URL.format(code)))
                return await message.reply(text=messages.FOUND.format(len(found_vendor_codes)), reply_markup=inline_keyboard)

        else:
            return await message.reply(messages.VENDOR_CODE_WAS_NOT_FOUND)
    except Exception as e: #? Left for logging
        return await message.reply(messages.ERROR)
