#! /bin/python3.10

import psycopg2
import os
import telebot

host_env = os.environ['HOST']
database_env = os.environ['DATABASE']
user_env = os.environ['USER']
password_env = os.environ['PASSWORD']
API_TOKEN = os.environ['TOKEN']

def connect_to_db(id, text, username):
    conn = psycopg2.connect(host=host_env, database=database_env, user=user_env, password=password_env)

    with conn.cursor() as cur:
        cur.execute("INSERT INTO messages(user_id,message,username) VALUES (%s,%s,%s)",(id, text, username))
        conn.commit()
    conn.close()
    
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,"Hello there, type smthg")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    connect_to_db(message.from_user.id, message.text, message.from_user.username)
    bot.reply_to(message, message.text)


bot.infinity_polling()




