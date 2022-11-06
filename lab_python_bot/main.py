import requests
from countries import countries
from aiogram import Bot, Dispatcher, types, executor
import datetime

TOKEN = ''

def nationality(name: str) -> dict:
    r = requests.get(f'https://api.nationalize.io/?name={name}').json()
    l = {}
    for i in r['country']:
        l[countries[i['country_id']]] = float(i['probability'])*100
    return l
    
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Send me any name and i will give it\'s nationality!')
    

@dp.message_handler()
async def get_nationality(message: types.Message):
    print(f'User: {message.from_user.username}, Time: {datetime.datetime.now()} \nMessage: {message.text}')
    try:
        n = nationality(message.text)
        reply = ''
        for country, probability in n.items():
            reply += country + ' ' + str(probability) + '% \n'
        await message.answer(reply)
    except:
        await message.answer('I can\'t find this name :(')

if __name__ == '__main__':
    executor.start_polling(dp)