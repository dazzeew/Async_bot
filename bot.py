from config import TOKEN
from keyboards import main_keyboard, fstep_keyboard, sstep_keyboard, mascom
from functions import url, Parcer, send_telegram
from states_class import steps


import time
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram

bot = Bot(TOKEN, parse_mode = 'HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
change_letter = 'Введите модель телефона или выберите команду'

async def anti_flood(*args, **kwargs):	
    m = args[0]
    await m.answer("Не флуди :)")



@dp.message_handler(commands = 'start', state = '*')
@dp.throttled(anti_flood,rate=3)
async def wasup(message):
	await message.reply(text = 'Привет, я пытаюсь заработать...\nВыбери что-то из меню', reply_markup = main_keyboard())
	await steps.change_zch.set()

@dp.message_handler(content_types = ['text'], state = steps.change_zch)
@dp.throttled(anti_flood,rate=3)
async def main_change(message, state: FSMContext):
	if message.text == mascom[0]:
		await message.answer(text = change_letter, reply_markup = sstep_keyboard())
		await state.update_data(id = 'section_id=93&q=')
		await steps.confirm_pars.set()
	elif message.text == mascom[1]:
		await message.answer(text = change_letter, reply_markup = sstep_keyboard())
		await state.update_data(id = 'section_id=95&q=')
		await steps.confirm_pars.set()
	elif message.text == mascom[2]:
		await message.answer(text = change_letter, reply_markup = sstep_keyboard())
		await state.update_data(id = '&q=защитное+стекло+')
		await steps.confirm_pars.set()
	else:
		await message.answer(text = 'Упс....', reply_markup = main_keyboard())
		return


@dp.message_handler(content_types = ['text'], state = steps.confirm_pars)
@dp.throttled(anti_flood,rate=3)
async def pars_model(message, state: FSMContext):
	if message.text == 'В главное меню':
		await message.answer(text = 'Выберите что-то из меню', reply_markup = main_keyboard())
		await steps.change_zch.set()
	else:
		user_data = await state.get_data()
		new_url = url(message.text, user_data['id'])
		await state.update_data(url = new_url)
		dictname = await Parcer(new_url)
		if dictname == {}:
			await message.reply(text = 'К сожалению такой запчасти нету, попробуйте снова или нажмите вернитесь в главное меню')
			return
		counter = 1
		info = ''
		for i in dictname:
				info += str(counter) + '. ' + i + ' \n' + dictname.get(i)[1].text + '\n\n'
				counter += 1
		info += 'Отправьте в чат номер запчасти, цену на замену которой вы бы хотели узнать'
		await message.answer(text = info, reply_markup = fstep_keyboard())
		await steps.choice_number.set()

@dp.message_handler(content_types = ['text'], state = steps.choice_number)
@dp.throttled(anti_flood,rate=3)
async def number_detail(message, state: FSMContext):
	if message.text == 'В главное меню':
		await message.answer(text = 'Выберите что-то из меню', reply_markup = main_keyboard())
		await steps.change_zch.set()
	elif message.text == 'Назад':
		await message.reply(text = 'Введите модель телефона', reply_markup = sstep_keyboard())
		await steps.confirm_pars.set()
	else:
		user_data = await state.get_data()
		dictname = await Parcer(user_data['url'])
		check = True
		for i in range(len(dictname)):
			if message.text == str(i + 1):
				check = False
				break
		if check:
			await message.reply(text = 'Такого номера запчасти нет!!', reply_markup = fstep_keyboard())
			return
		or_price = ['skip']
		for i in dictname:
			or_price.append(i + ' (' + dictname.get(i)[0].text.replace(" ", "") + "Рублей)\n\n")
		send_orientir = str(or_price[int(message.text)])
		send_telegram(str(or_price[int(message.text)]))
		await message.answer(text = send_orientir + 'Для просмотра других цен, введите цифру', reply_markup = fstep_keyboard())
		return



if __name__ == '__main__':
	executor.start_polling(dp)

