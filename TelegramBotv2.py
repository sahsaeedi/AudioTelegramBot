import telebot
from STT import SpeechToText
import os
from duratinAudio import audio_duration
import random


r = random.randint(0,100)
bot = telebot.TeleBot(token= '1636116851:AAFtwKEXGJavIZtb9rpBYFCTNxrO47jWNFA')
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message, 'سلام رفیق')

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    sentence = None

    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('./audioogg/{n}.ogg'.format(n = r), 'wb') as new_file:
        new_file.write(downloaded_file)
    
    os.system('ffmpeg -y -i ./audioogg/{n}.ogg ./audiowav/{s}.wav'.format(n=r, s=r))

    hours, mins, secounds = audio_duration('./audiowav/{s}.wav'.format(s=r))
    try:
        if hours == 0 and mins == 0 and secounds <= 10:
            sentence = load_model('./audiowav/{s}.wav'.format(s=r))
        else:
            sentence = 'ویس شما بیشتر از 10 ثانیه است . لطفا ویس بعدی را با زمان کمتر از 10 ثانیه بفرستید'
        bot.reply_to(message, sentence)

    except:
        bot.reply_to(message, 'دوباره امتحان کنید')

def load_model(path):
    obj = SpeechToText(path)
    sentence = obj.predict()
    return sentence
    
    
        
bot.polling(none_stop=True, timeout=123)
