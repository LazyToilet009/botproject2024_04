from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.shop_keyboard import make_keyboard


router = Router()


available_games = [
    'Minecraft',
    'GTA5',
    'CS2',
    'ULTRAKILL',
    'Half-Life'
]
available_grades = [
    'Ключ',
    'Аккаунт',
]


class Choice(StatesGroup):
    game = State()
    grade = State()


@router.message(Command(commands=['game_shop']))
async def start(message: types.Message, state: FSMContext):
    await message.answer('Какая игра вас интересует?', reply_markup=make_keyboard(available_games))
    await state.set_state(Choice.game)


@router.message(Choice.game, F.text.in_(available_games))
async def jobs(message: types.Message, state: FSMContext):
    await message.answer('Ключ или аккаунт с игрой?', reply_markup=make_keyboard(available_grades))
    await state.set_state(Choice.grade)


@router.message(Choice.game)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_games))


@router.message(Choice.grade, F.text.in_(available_grades))
async def grade(message: types.Message, state: FSMContext):
    await message.answer(f'Оплата прошла, скоро с вами свяжуться наш сотрудник.',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуйте ещё раз', reply_markup=make_keyboard(available_grades))