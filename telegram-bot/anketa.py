from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from telegram.ext import ConversationHandler
from utils import main_keyboard


def anketa_start(update, context):
    update.message.reply_text(
        "Как вас зовут? Напишите имя и фамилию",
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"


def anketa_name(update, context):
    user_name = update.message.text
    print(len(user_name.split()))
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return "name"
    else:
        context.user_data['anketa'] = {"name": user_name}
        reply_keyboard = ["1", "2", "3", "4", "5"]
        update.message.reply_text(
            "Пожалуйста оцените нашего бота от 1 до 5",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
                )
        )
        return "rating"


def anketa_rating(update, context):
    context.user_data['anketa']['rating'] = int(update.message.text)
    update.message.reply_text(
        "Напишите комментарий, или нажмите /skip чтобы пропустить"
        )
    return "comment"


def anketa_skip(update, context):
    context.user_data['anketa']['comment'] = int(update.message.text)
    update.message.reply_text(
        f"""<b>Имя Фамилия</b> {context.user_data['anketa']['name']}
        <b>Оценка</b> {context.user_data['anketa']['rating']}""",
        reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def anketa_comment(update, context):
    context.user_data['anketa']['comment'] = int(update.message.text)
    update.message.reply_text(
        f"""<b>Имя Фамилия</b> {context.user_data['anketa']['name']}
        <b>Оценка</b> {context.user_data['anketa']['rating']}
        <b>Комментарий</b> {context.user_data['anketa']['comment']}""",
        reply_markup=main_keyboard(),
        parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def anketa_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")
