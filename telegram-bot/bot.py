import logging
from glob import glob
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from emoji import emojize

import settings


logging.basicConfig(filename='bot.log', level=logging.INFO)


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)    
        smile = emojize(smile)
        return smile
    return user_data['emoji']


def greet_user(update, context):
    print("Вызван /start")
        
    smile = get_smile(context.user_data)
    context.user_data['emoji'] = smile
    update.message.reply_text(f"Здравствуй, пользователь {smile}!")


def play_randon_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
    return message


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_randon_numbers(user_number)
        except(TypeError, ValueError):
            message = "Выведите целое число"
    else:
        message = "Выведите целое число"
    update.message.reply_text(message)


def send_cat(update, context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"))


def talk_to_me(update, context):    
    text = update.message.text
    print(text)
    smile = get_smile(context.user_data)
    context.user_data['emoji'] = smile
    update.message.reply_text(f"{text} {smile}")


def main():
    mybot = Updater(settings.API_KEY,use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
