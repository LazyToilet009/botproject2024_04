from aiogram import Router, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import keyboard
from utils.random_fox import fox

router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)

@router.message(Command(commands=['стоп']))
@router.message(Command(commands=['stop']))
async def start(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Пока, {message.chat.first_name}!')

@router.message(Command(commands=['info', 'инфо']))
@router.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Твоё число: {number}')

@router.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Лови лису')
    await message.answer_photo(img_fox)