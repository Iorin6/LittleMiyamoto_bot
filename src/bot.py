from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime

# Dictionary to store message limits for each user
limits = {}

# Function to set message limit for a user
def set_limit(update: Update, context: CallbackContext):
    args = context.args
    if len(args) != 2:
        update.message.reply_text("Usage: /limit <username> <limit>")
        return
    username = args[0]
    limit = int(args[1])
    limits[username] = limit
    update.message.reply_text(f"Message limit set to {limit} for user {username}")

# Function to count messages and apply penalty if limit is exceeded
def count_messages(update: Update, context: CallbackContext):
    user = update.message.from_user.username
    if user in limits:
        limits[user] -= 1
        if limits[user] <= 0:
            update.message.reply_text("You have reached the message limit. You have been muted until midnight.")
            return
    update.message.reply_text("Message received.")

# Function to reset message counters at midnight every day
def reset_limits(context: CallbackContext):
    global limits
    limits = {}
    context.job_queue.run_once(reset_limits, datetime.time(0, 0, 0))

# Function to provide description of available commands
def help_command(update: Update, context: CallbackContext):
    help_text = """
    Welcome to the chat activity management bot!

    Available commands:
    /limit <username> <limit> - Set message limit for a specific user.
    /help - Show this message with descriptions of available commands.
    """
    update.message.reply_text(help_text)

def main():
    # Set up the bot token
    bot_token = 'YOUR_BOT_TOKEN'
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("limit", set_limit))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, count_messages))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
