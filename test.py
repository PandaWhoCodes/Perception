from __future__ import print_function
from cleverwrap import CleverWrap
cw = CleverWrap("API KEY")

import requests
import lint
import ginger
import json
import os

try:
    from urllib import urlencode, quote_plus
except ImportError:
    from urllib.parse import urlencode, quote_plus

try:
    import urllib2 as wdf_urllib
    from cookielib import CookieJar
except ImportError:
    import urllib.request as wdf_urllib
    from http.cookiejar import CookieJar

api_url = "https://languagetool.org/api/v2/check"
import telebot

bot = telebot.TeleBot("213368282:APIKEY")


def getRequest(url, data=None):
    try:
        data = data.encode('utf-8')
    except:
        pass
    finally:
        return wdf_urllib.Request(url=url, data=data)


def getResponse(text):
    simKey = ''
    text = text.replace(' ', ',')
    url = 'http://sandbox.api.simsimi.com/request.p?key=%s&lc=ch&ft=1.0&text=%s' % (
        'dd75290b-de5e-4ad3-985e-08dab681a5e6', text)
    print('Sent to message to server to get response')
    print(url)
    request = getRequest(url=url)
    response = wdf_urllib.urlopen(request)
    data = response.read().decode('utf-8', 'replace')
    res = json.loads(data)
    if res['result'] != 100:
        return 'Status: ' + res['result'] + ' -> ' + res['msg']
    else:
        if 'response' in res.keys():
            return res['response']
        else:
            return 1


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Howdy, I am here to help you with your grammar\nSend me a sentence and I'll send possible corrections")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    a = str(message.text)
    toShow = ""
    # r = requests.post(api_url, data={"text": a, "language": "en-us"})
    # errors = r.json()["matches"]

    errors = ginger.main(a)
    b = lint.main(a)
    if len(b) > 0:
        errors = errors + b
    if len(errors) < 1:
        # b=getResponse(a)
        b=cw.say(a)
        print(b)
        if b==1:
            bot.reply_to(message, "Awesome! No grammatical mistakes")
        else:
            bot.reply_to(message,str(b))
    else:
        for items in errors:
            toShow += items + "\n"
        fh = open('log.txt', 'a')
        fh.write(a)
        fh.write(toShow)
        fh.write("\n")
        bot.reply_to(message, toShow)


bot.polling()