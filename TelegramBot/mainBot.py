from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, ConversationHandler
)

# Состояния для ConversationHandler
CHOOSE_DRINK, CHOOSE_TYPE, CONFIRM = range(3)

# Словарь для хранения заказа
order_data = {}

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [
        [InlineKeyboardButton("Кофе", callback_data="drink_coffee")],
        [InlineKeyboardButton("Чай", callback_data="drink_tea")],
        [InlineKeyboardButton("Вода", callback_data="drink_water")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать! Что вы хотите заказать?", reply_markup=reply_markup)
    return CHOOSE_DRINK

# Выбор типа напитка
async def choose_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Сохраняем выбор напитка
    drink_choice = query.data.split("_")[1]
    order_data["drink"] = drink_choice

    # Определяем кнопки в зависимости от выбора
    if drink_choice == "coffee":
        keyboard = [
            [InlineKeyboardButton("Арабика", callback_data="type_arabica")],
            [InlineKeyboardButton("Робуста", callback_data="type_robusta")],
        ]
        text = "Вы выбрали Кофе. Какой сорт предпочитаете?"
    elif drink_choice == "tea":
        keyboard = [
            [InlineKeyboardButton("Зеленый", callback_data="type_green")],
            [InlineKeyboardButton("Черный", callback_data="type_black")],
        ]
        text = "Вы выбрали Чай. Какой вид предпочитаете?"
    elif drink_choice == "water":
        keyboard = [
            [InlineKeyboardButton("Горячая", callback_data="type_hot")],
            [InlineKeyboardButton("Холодная", callback_data="type_cold")],
        ]
        text = "Вы выбрали Воду. Какую предпочитаете?"

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup)
    return CHOOSE_TYPE

# Подтверждение заказа
async def confirm_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Сохраняем выбор типа
    drink_type = query.data.split("_")[1]
    order_data["type"] = drink_type

    # Формируем итоговый заказ
    drink = order_data["drink"]
    drink_names = {"coffee": "Кофе", "tea": "Чай", "water": "Вода"}
    type_names = {
        "arabica": "Арабика", "robusta": "Робуста",
        "green": "Зеленый", "black": "Черный",
        "hot": "Горячая", "cold": "Холодная"
    }

    final_drink = drink_names[drink]
    final_type = type_names[drink_type]

    text = f"Ваш заказ: {final_drink}, {final_type}. Все верно?"
    keyboard = [
        [InlineKeyboardButton("Да", callback_data="confirm_yes")],
        [InlineKeyboardButton("Нет", callback_data="confirm_no")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup)
    return CONFIRM

# Обработка кнопки "Нет"
async def redo_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    # Возвращаем пользователя к выбору напитка
    keyboard = [
        [InlineKeyboardButton("Кофе", callback_data="drink_coffee")],
        [InlineKeyboardButton("Чай", callback_data="drink_tea")],
        [InlineKeyboardButton("Вода", callback_data="drink_water")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Давайте начнем заново. Что вы хотите заказать?", reply_markup=reply_markup)
    return CHOOSE_DRINK

# Завершение заказа
async def finalize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    if query.data == "confirm_yes":
        await query.edit_message_text("Спасибо за заказ! Мы скоро его приготовим.")
    return ConversationHandler.END

# Функция отмены
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Вы отменили процесс заказа. Напишите /start, чтобы начать заново.")
    return ConversationHandler.END

# Основная функция
def main():
    application = Application.builder().token("7633681474:AAHHHJPspKulKFF0BeB3LGSDMRtH1p4Wa8M").build()

    # Создаем ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSE_DRINK: [CallbackQueryHandler(choose_type, pattern="^drink_")],
            CHOOSE_TYPE: [CallbackQueryHandler(confirm_order, pattern="^type_")],
            CONFIRM: [
                CallbackQueryHandler(finalize, pattern="^confirm_yes$"),
                CallbackQueryHandler(redo_order, pattern="^confirm_no$")
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
