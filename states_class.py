from aiogram.dispatcher.filters.state import State, StatesGroup

class steps(StatesGroup):
	change_zch = State()
	confirm_pars = State()
	choice_number = State()

