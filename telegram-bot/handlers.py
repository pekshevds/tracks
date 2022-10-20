from random import choice
from utils import play_randon_numbers, get_smile, has_object_on_image
from glob import glob
import os

from db import db, get_or_create_user


def greet_user(update, context):

    print("Вызван /start")
    user = get_or_create_user(db, update.effective_user, update.message.chat_id)
            
    smile = get_smile(context.user_data)
    context.user_data['emoji'] = smile
    update.message.reply_text(f"Здравствуй, пользователь {smile}!")


def guess_number(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat_id)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_randon_numbers(user_number)
        except (TypeError, ValueError):
            message = "Выведите целое число"
    else:
        message = "Выведите целое число"
    update.message.reply_text(message)


def send_cat(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat_id)
    cat_photo_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, "rb"))


def talk_to_me(update, context):    
    user = get_or_create_user(db, update.effective_user, update.message.chat_id)
    text = update.message.text    
    smile = get_smile(context.user_data)
    context.user_data['emoji'] = smile
    update.message.reply_text(f"{text} {smile}")


def check_user_photo(update, context):    
    update.message.reply_text("Идет обработка изображения")
    os.makedirs("downloads", exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join("downloads", update.message.photo[-1].file_id + ".jpg")
    photo_file.download(file_name)
    update.message.reply_text("Изображение сохранено")

    if has_object_on_image(file_name):
        update.message.reply_text("Обнаружен котик, сохраняю в библиотеку")
        new_file_name = os.path.join('images', f"cat_{photo_file.file_id}.jpg")
        os.rename(file_name, new_file_name)
    else:
        os.remove(file_name)
        update.message.reply_text("Котик не обнаружен")
    