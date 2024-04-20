from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    main_menu = State()

class StartWork(StatesGroup):
    start_work = State()

