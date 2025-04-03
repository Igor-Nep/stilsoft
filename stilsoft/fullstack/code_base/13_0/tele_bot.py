import telebot, random
#https://core.telegram.org/bots/api#making-requests
#Checker_state_stil_bot
#8106710833:AAHD-nZHCeFopceKkFPjJ6u04i77TblyFmA

url = 'https://api.telegram.org/bot'
token = '8106710833:AAHD-nZHCeFopceKkFPjJ6u04i77TblyFmA'
bot = telebot.TeleBot(token)
hi_ = ['Привет','привет','Здоров','здоров','Добрый день']
work_ = ['работай','Работай','работать','Работать','поработать'] 
answers = ['Привет, гомосек!','Здравствуй, Залупа!','Здоров, терпила!','Хули тебе?','Салам, ебанутый','Хули надо?','Привет, несчастливый','Здоров, пидрятня']
work = ['Заебал','Не, я не в духе','Не могу работать, болею','А хуй тебе не отсосать?','Давай ка сам, старина']
dont_understand = ['Нихуя не понял','Напиши нормально, заебал','Что ты несёшь? Повтори нормально','Вынь хуй изо рта и напиши нормально','Хватит думать о любовнике, соберись и напиши нормально','Всё хуйня, давай по-новой']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in hi_:
        
        bot.send_message(message.from_user.id, random.choice(answers))
    elif message.text in work_:
        bot.send_message(message.from_user.id, random.choice(work))
    else:
        bot.send_message(message.from_user.id, random.choice(dont_understand))
bot.polling(none_stop=True, interval=0)

