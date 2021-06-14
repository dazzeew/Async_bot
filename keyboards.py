from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton
mascom = ['Дисплей','Аккумулятор','Защитное стекло']

def main_keyboard():
	main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
	btn1_1 = KeyboardButton(mascom[0])
	btn1_2 = KeyboardButton(mascom[1])
	btn1_3 = KeyboardButton(mascom[2])
	main_kb.add(btn1_1,btn1_2).add(btn1_3)
	return main_kb

def fstep_keyboard():
	fstep_kb = ReplyKeyboardMarkup(resize_keyboard=True)
	btn2_1 = KeyboardButton('В главное меню')
	btn2_2 = KeyboardButton('Назад')
	fstep_kb.add(btn2_1).add(btn2_2)
	return fstep_kb


def sstep_keyboard():
	sstep_kb = ReplyKeyboardMarkup(resize_keyboard=True)
	btn3_1 = KeyboardButton('В главное меню')
	sstep_kb.add(btn3_1)
	return sstep_kb



