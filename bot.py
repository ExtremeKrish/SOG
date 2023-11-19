import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

my_bot_token = '6171891363:AAEgSTM5I5w2ljZEl4uJ6cdgFmHJWqnHOmQ'

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.ERROR)  # Set level to ERROR to reduce console output

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    # Create a grid-style keyboard for the main menu
    main_menu_keyboard = [['My Account', 'Donate'], ['Invite', 'Support'], ['Statistics']]
    main_menu_markup = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Choose an option:",
        reply_markup=main_menu_markup,
    )

async def handle_menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text

    if user_input == 'My Account':
        # Sending a sample image as user's profile picture
        sample_image_url = 'https://example.com/sample_image.jpg'  # Replace with the actual URL
        await update.message.reply_photo(sample_image_url, caption="Your profile picture:")

    elif user_input == 'Donate':
        # Sends donation information
        await update.message.reply_text("Upi: 8756315115@fam")

    elif user_input == 'Invite':
        # Sends an invite link with the user's id as a parameter
        invite_link = f"https://t.me/YourBotUsername?start={update.effective_user.id}"
        invite_keyboard = [[InlineKeyboardButton("Forward Invite Link", switch_inline_query=invite_link)]]
        invite_markup = InlineKeyboardMarkup(invite_keyboard)
        await update.message.reply_text(f"Invite link:\n{invite_link}", reply_markup=invite_markup)

    elif user_input == 'Support':
        # Sends a support message and prompts a cancel button in the keyboard
        support_keyboard = [['Cancel']]
        support_markup = ReplyKeyboardMarkup(support_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text("Now you are directed to admin. How can I help you?", reply_markup=support_markup)

    elif user_input == 'Statistics':
        # Sends the number of active users of the bot and a back button in the keyboard
        active_users = 1000  # Replace with actual count
        statistics_keyboard = [['Back']]
        statistics_markup = ReplyKeyboardMarkup(statistics_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text(f"Active Users: {active_users}", reply_markup=statistics_markup)

# Add callback query handler to handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    query.answer()  # Acknowledge the callback

    # Handle different callback data
    if query.data == 'Back':
        await start(update, context)
    elif query.data == 'Cancel':
        await update.message.reply_text("Operation cancelled.", reply_markup=ReplyKeyboardRemove())

application = Application.builder().token(my_bot_token).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice))
application.add_handler(CallbackQueryHandler(button_click))

if __name__ == "__main__":
    application.run_polling()
