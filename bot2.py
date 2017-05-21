import telebot
import pprint
bot = telebot.TeleBot("213368282:AAG5SX8jPkyojfFWOlqudHFLpnZ-gKJNoF0")
from Perception.query import getItem

from Perception.insertion import *
def setWord(message):
    pid=message.chat.id
    sessid=message.message_id
    item= getItem()
    setSession(pid,item,sessid)
    return item
def setUser(message):
    pid=message.chat.id
    name=message.chat.first_name + " " + message.chat.last_name
    sessid=message.message_id
    setPerson(pid,name)

@bot.message_handler(commands=['start', 'newword','giveTags'])
def send_welcome(message):
    pid = message.chat.id

    if message.text == "/start":
        try:
            setUser(message)
        except Exception as e:
            rollback1()
            print(e.args,e)
            bot.reply_to(message, "Hey, I am perceptionbot. Reply with /newword to get a new word and /giveTags to check all tags")
            pass


    elif message.text == "/giveTags":
        print("CAME HERE")
        bot.reply_to(message,str(getTags(getpItem(pid))))
    else:
        text=setWord(message)
        bot.reply_to(message,text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    a = str(message.text)
    pid = message.chat.id
    sessid = message.message_id
    item= getpItem(pid)
    setPlay(pid,item,a,sessid)

bot.polling()
