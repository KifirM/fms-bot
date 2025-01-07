import asyncio
import os
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import InputFile, FSInputFile

import aiogram

from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from common.bot_cmds_list import private

#from handlers.admin_private import user_admin_router
from handlers.user_private import user_private_router
# from handlers.user_group import user_group_router
#from common.bot_cmds_list import private


ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

dp.include_router(user_private_router)
# dp.include_router(user_group_router)


#dp.include_router(user_admin_router)


#async def on_startup(bot):
#    await drop_db()
#    await create_db()
#
#async def on_shutdown(bot):
#    print('бот устал')


async def main(): #ассинхронная функция

#    dp.startup.register(on_startup)
#    dp.shutdown.register(on_shutdown)
#    dp.update.middleware(DataBaseSession(session_pool=session_maker))


    await bot.delete_webhook(drop_pending_updates=True)  #чтобы пропустить обновления, пока бот не работал.
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES) #start_polling - ассинхронный метод, запускающий бота в работу (run_polling - не ассинхронный)

asyncio.run(main())
