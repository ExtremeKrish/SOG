from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram import Update
# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6171891363:AAEgSTM5I5w2ljZEl4uJ6cdgFmHJWqnHOmQ'

def start(update, context):
    update.message.reply_text('Hello! I am your echo bot. Type anything, and I will repeat it.')

def echo(update, context):
    user_input = update.message.text
    update.message.reply_text(f'You said: {user_input}')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handlers
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)

    # Add handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
