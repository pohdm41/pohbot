import telebot
import random

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
TOKEN = '6360219039:AAEU9dTjQJc5DY-rs0WABOaPwUxkcK9yy6o'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Create a dictionary to store assigned codes and their messages
assigned_codes = {}

# Function to handle code messages
@bot.message_handler(func=lambda message: message.text.isdigit() and len(message.text) == 8)
def handle_code_message(message):
    chat_id = message.chat.id
    code = message.text

    if code in assigned_codes:
        bot.send_message(chat_id, assigned_codes[code])
    else:
        bot.send_message(chat_id, f"Sorry, couldn't find any message assigned to this code: *{code}*", parse_mode='Markdown')

# Function to assign a code to a message
@bot.message_handler(func=lambda message: message.text.startswith('/assign '))
def assign_code_to_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    command_parts = message.text.split(' ')
    
    if len(command_parts) == 2 and len(command_parts[1]) == 6:
        code = command_parts[1]
        if code not in assigned_codes:
            assigned_codes[code] = f"Message assigned to code: *{code}*"
            bot.send_message(chat_id, f"Code {code} has been assigned to a message.", parse_mode='Markdown')
        else:
            bot.send_message(chat_id, f"Sorry, code *{code}* has already been assigned.", parse_mode='Markdown')
    else:
        bot.send_message(chat_id, "Invalid command. Please use '/assign' followed by a 6-digit code.", parse_mode='Markdown')

# Start the bot
bot.polling()
