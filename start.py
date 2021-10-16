import requests, time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import json

def getNews(update: Update, context: CallbackContext) -> None:
  response = requests.get('https://dashboard.nbshare.io/api/v1/apps/reddit')
  data = response.json()
  for x in data: 
    comments = x['no_of_comments']
    sentiment = x['sentiment']
    sentiment_score = x['sentiment_score']
    ticker = x['ticker']
    t = ticker, 'with' , str(comments), 'comments is', str(sentiment_score), str(sentiment)
    t = " ".join(t)
    update.message.reply_text(t)

updater = Updater('2083621450:AAEnmEJEuco9WqfiakULun5JTaIpoJ_Yq2o')

updater.dispatcher.add_handler(CommandHandler('news', getNews))

updater.start_polling()
updater.idle()