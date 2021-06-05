import telebot
import requests
from bs4.element import TemplateString
from bs4 import BeautifulSoup
import json

appid = "77418365638fc9ba64022afadb25eca5"
token = '1847171808:AAEXQesrfvL47gsA9a6tgj9VE5B6r7J6Ojc'
bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)

@bot.message_handler(commands=['start'])
def go(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
    keyboard.row("Погода", "Гороскоп", "Курс Валют","Новости")
    bot.send_message(message.chat.id, "Чего желаете?", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == "Погода":
        bot.send_message(message.chat.id, weather(), reply_markup=keyboard)
    else:
        if message.text == "Гороскоп":
            msg=bot.send_message(message.chat.id, "Гороскоп", reply_markup=keyboard)
            geo(msg)
        else:
            if message.text == "Курс Валют":
                msg=bot.send_message(message.chat.id, "Курс Валют", reply_markup=keyboard)
                valutes(msg)
            else:
                if message.text == "Новости":
                    msg=bot.send_message(message.chat.id, news(), reply_markup=keyboard)
                    go(msg)
                else:
                    bot.send_message(message.chat.id,"Не вышло")

def weather():
    Days = 8

    res = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=Kemerovo&appid=ab148c0eed6d6c23408cfddbd5a972dc')
    data = res.json()
    data = data['list']
    Cont = ' '
    osadki = ''
    for i in range (Days):
        info = data[i+1]
        date = info['dt_txt']
        weather=info['main']['temp']-273
        veter=info['wind']['speed']
        cloud=info['clouds']['all']
    #Так и должно быть иначе вылезет ошибка, прикол питона с .get
        if info.get(['rain'][0],0) != 0:
            osadki = f"{info['rain']['3h']} мм"
        else:
            osadki = ' Нет'

        l = f"Погода на {date} \n "
        a = f"На улице {int(weather)} градусов \u2600\n"
        b = f"Ветер {str(veter)} мс \U0001F4A8\n"
        c = f"Небо затянуто на {str(cloud)}% \u26C5\n"
        d = f"Осадков {str(osadki)} \U0001F327\n"
        Cont+= l+a+b+c+d
    return Cont

def geo(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
    keyboard.add("Лев","Рыбы","Скорпион","Овен","Телец","Близнецы")
    keyboard.add("Рак","Дева","Весы","Стрелец","Козерог","Водолей")
    a=bot.send_message(message.chat.id,"Выберите знак зодиака",reply_markup=keyboard)
    bot.register_next_step_handler(a,viborGeo)
    
def valutes(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
    keyboard.add("Доллар США","Евро","Юань","Биткоин","Эфириум","Doge Coin")
    a=bot.send_message(message.chat.id,"Выберите знак зодиака",reply_markup=keyboard)
    bot.register_next_step_handler(a,viborValutes)
        

@bot.message_handler(content_types=['text'])
def viborGeo(message):
    if message.text == "Лев":
        bot.send_message(message.chat.id, "https://astrozodiac.net/media/2016/11/lev.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('leo'), reply_markup=keyboard)
        go(message)
    elif message.text == "Рыбы":
        bot.send_message(message.chat.id, "https://avatars.mds.yandex.net/get-zen_doc/1706517/pub_5e370c151bb3ea1db1aef7d2_5e3712b15c980e6fecc6bf11/scale_1200", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('pisces'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Скорпион":
        bot.send_message(message.chat.id, "https://wikiq.ru/wp-content/uploads/2018/10/skorpionjpg.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('scorpio'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Овен":
        bot.send_message(message.chat.id, "https://amorem.ru/upload/iblock/9ef/post_5d1eeca37c95f.jpeg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('aries'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Телец":
        bot.send_message(message.chat.id, "https://love-is.org/wp-content/uploads/2019/05/rak-i-telec-sovmestimost2.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('taurus'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Близнецы":
        bot.send_message(message.chat.id, "https://takprosto.cc/wp-content/uploads/o/osobennosti-znakov-zodiaka/8.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('gemini'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Рак":
        bot.send_message(message.chat.id, "https://vplate.ru/images/article/orig/2018/08/harakteristika-znaka-zodiaka-rak.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('cancer'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Дева":
        bot.send_message(message.chat.id, "https://vplate.ru/images/article/orig/2018/08/znak-zodiaka-deva-harakteristika-sovmestimost-i-podhodyashchie-talismany.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('virgo'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Весы":
        bot.send_message(message.chat.id, "https://www.sunhome.ru/i/cards/246/otkritka-dlya-znaka-zodiaka-vesi.orig.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('libra'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Стрелец":
        bot.send_message(message.chat.id, "http://auraplus.org/wp-content/uploads/2016/06/Goroskop-2016-dlya-Streltsa-zhenshhinyi-i-muzhchinyi.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('sagittarius'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Козерог":
        bot.send_message(message.chat.id, "https://best-lady.com/wp-content/uploads/2020/11/sovmestimost-kozeroga2.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('capricorn'), reply_markup=keyboard)
        go(msg)
    elif message.text == "Водолей":
        bot.send_message(message.chat.id, "https://onelove.su/wp-content/uploads/2019/07/vesy-i-vodolej-sovmestimost9.jpg", reply_markup=keyboard)
        msg=bot.send_message(message.chat.id, info('aquarius'), reply_markup=keyboard)
        go(msg)
    else:
        msg=bot.send_message(message.chat.id,"Что то пошло не так!")
        go(msg)

def info(param):
    request = requests.get(f'https://horo.mail.ru/prediction/{param}/today/')
    soup = BeautifulSoup(request.text, 'html')
    a=soup.find_all("div", {"class": "article__text"})
    a=soup.select('div > p')[0].get_text(strip=True)
    c="\n"
    b=soup.select('div > p')[1].get_text(strip=True)
    return a+c+b

@bot.message_handler(content_types=['text'])
def viborValutes(message):
    if message.text == "Доллар США":
        msg=bot.send_message(message.chat.id, f"{money('USD')} рублей", reply_markup=keyboard)
        go(message)
    elif message.text == "Евро":
        msg=bot.send_message(message.chat.id,f"{money('EUR')} рублей", reply_markup=keyboard)
        go(message)
    elif message.text == "Юань":
        msg=bot.send_message(message.chat.id,f"{money('CNY')} рублей", reply_markup=keyboard)
        go(message)
    elif message.text == "Биткоин":
        msg=bot.send_message(message.chat.id, cripts('bitcoin'), reply_markup=keyboard)
        go(message)
    elif message.text == "Эфириум":
        msg=bot.send_message(message.chat.id, cripts('ethereum'), reply_markup=keyboard)
        go(message)
    elif message.text == "Doge Coin":
        msg=bot.send_message(message.chat.id, cripts('dogecoin'), reply_markup=keyboard)
        go(message) 
    else:
        msg=bot.send_message(message.chat.id,"Что то пошло не так!")
        go(msg)
        
def money(val):
    request = requests.get('https://www.cbr.ru/currency_base/daily/')
    soup = BeautifulSoup(request.text, 'html')
    td_list = soup.find_all('td')
    i = 0
    for elem in td_list:
        if elem.text == val:
            ind = i
        i += 1
    return td_list[ind+3].text
    
def cripts(val):
    BTC = requests.get(f'http://api.coincap.io/v2/assets/{val}')
    BTC = BTC.json()
    BTC = BTC['data']
    BTC = f"Цена в USD : {BTC['priceUsd']}"
    return BTC

def news():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=ru&apiKey=f7edadb28b9f4813a5c3044a2b87eb27')
    X = json.loads(r.text)

    Name = X['articles'][0]['source']['name']
    a=f"Сообщает: {Name}\n"
    
    Desc =X['articles'][0]['description']
    b=f"Новость: {Desc}\n"
    
    Link = X['articles'][0]['url']
    c=f"Ссылка на полную новость : {Link}"
    return a+b+c
                 
bot.polling()
