from aiogram.filters.callback_data import CallbackData
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardButton
from database.requests import get_tasks, set_user
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command



start_kb = ReplyKeyboardBuilder()
start_kb.add(
    KeyboardButton(text='Меню 📂'),
    KeyboardButton(text='Помощь ❓'),
    KeyboardButton(text='Контакты 📞'),
)
start_kb.adjust(1, 2)
del_start_kb = ReplyKeyboardRemove()


menu_kb = ReplyKeyboardBuilder()
menu_kb.add(
    KeyboardButton(text='Расписание 📆'),
    # KeyboardButton(text='Заметки 📝'),
    KeyboardButton(text='Вернуться в начало 🏠')
)
menu_kb.adjust(2, 1)


liter_kb_10 = ReplyKeyboardBuilder()
liter_kb_10.add(
    KeyboardButton(text='Μ'),
    KeyboardButton(text='Ξ'),
    KeyboardButton(text='Ο'),
    KeyboardButton(text='Π'),
    KeyboardButton(text='Ρ'),
    KeyboardButton(text='Σ'),
    KeyboardButton(text='Τ'),
    KeyboardButton(text='Φ'),
    KeyboardButton(text='Χ'),
    KeyboardButton(text='Ψ'),
    KeyboardButton(text='🔀 Выбрать другой класс 🏫'),
    KeyboardButton(text='Вернуться в меню 📂🔙'),
    KeyboardButton(text='Вернуться в начало 🏠')
)
liter_kb_10.adjust(5)


liter_kb_11 = ReplyKeyboardBuilder()
liter_kb_11.add(
    KeyboardButton(text='Β'),
    KeyboardButton(text='Ζ'),
    KeyboardButton(text='Γ'),
    KeyboardButton(text='Ι'),
    KeyboardButton(text='Δ'),
    KeyboardButton(text='Η'),
    KeyboardButton(text='Θ'),
    KeyboardButton(text='Ε'),
    KeyboardButton(text='К'),
    KeyboardButton(text='Λ'),
    KeyboardButton(text='🔀 Выбрать другой класс 🏫'),
    KeyboardButton(text='Вернуться в меню 📂🔙'),
    KeyboardButton(text='Вернуться в начало 🏠')
)
liter_kb_11.adjust(5)

clases_kb = ReplyKeyboardBuilder()
clases_kb.add(
    KeyboardButton(text='10'),
    KeyboardButton(text='11'),
    KeyboardButton(text='Вернуться в меню 📂🔙'),
    KeyboardButton(text='Вернуться в начало 🏠'),
    KeyboardButton(text='🔄')
)
clases_kb.adjust(2,1)

group_kb = ReplyKeyboardBuilder()
group_kb.add(
    KeyboardButton(text='A',),
    KeyboardButton(text='B'),
    KeyboardButton(text='Выбрать другую литеру 🔠'),
    KeyboardButton(text='🔀 Выбрать другой класс 🏫'),
    KeyboardButton(text='Вернуться в меню 📂🔙'),
    KeyboardButton(text='Вернуться в начало 🏠')
)
group_kb.adjust(2,1,3,2)

# def classes_kb():
#     classes_list = [
#         [InlineKeyboardButton(text='1️⃣0️⃣', callback_data='10')],
#         [InlineKeyboardButton(text='1️⃣1️⃣', callback_data='11')],
#         [InlineKeyboardButton(text='🔄', callback_data='reload')]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=classes_list)



# def liter_kb_10():
#     liter_list_10 = [
#         KeyboardButton(text='Μ'),
#         KeyboardButton(text='Ξ'),
#         KeyboardButton(text='Ο'),
#         KeyboardButton(text='Π'),
#         KeyboardButton(text='Ρ'),
#         KeyboardButton(text='Σ'),
#         KeyboardButton(text='Τ'),
#         KeyboardButton(text='Φ'),
#         KeyboardButton(text='Χ'),
#         KeyboardButton(text='Ψ'),
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=liter_list_10)
# 
# def liter_kb_11():
#     liter_list_10 = [
#         KeyboardButton(text='Β'), 
#         KeyboardButton(text='Ζ'),
#         KeyboardButton(text='Γ'),
#         KeyboardButton(text='Ι'),
#         KeyboardButton(text='Δ'),
#         KeyboardButton(text='Η'),
#         KeyboardButton(text='Θ'),
#         KeyboardButton(text='Ε'),
#         KeyboardButton(text='Κ'),
#         KeyboardButton(text='Λ', callback_data='Λ')
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=liter_list_11)

# def group_kb():
#     group_list = [
#         [InlineKeyboardButton(text='Β', callback_data='Β')],
#         [InlineKeyboardButton(text='Ζ', callback_data='Ζ')],
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=group_list)

async def tasks(tg_id):
    await set_user(tg_id)
    tasks = await get_tasks(tg_id)
    notes_kb = InlineKeyboardBuilder()
    for task in tasks:
        notes_kb.add(InlineKeyboardButton(text=task.task, callback_data=f'task_{task.id}'))
    return notes_kb.adjust(1).as_markup()
