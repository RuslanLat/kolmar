import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
import pandas as pd
import config as cn
import sqlreq as sr
from aiogram import types

TOKEN = cn.BOT_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode="html")

dp = Dispatcher()

@dp.message(Command("номерчата"))
async def cmd_name(message: types.Message, command: CommandObject):
    await message.answer(f"{message.chat.id}")

@dp.message(Command("команды"))
async def cmd_name(message: types.Message, command: CommandObject):
    commands = ['топ3', 'отслеживать', 'неотслеживать', 'отслеживаемые', 'список', 'отчет', 'инфо', 'обновление', 'рассылка', 'группа']
    await message.answer(f"{', '.join(commands)}")


@dp.message(Command("рассылка"))
async def cmd_name(message: types.Message, command: CommandObject):
    if message.chat.id == sr.master_chat:
        query = cn.create_files_query
        # хардкод
        for key in sr.temporary_permission.keys():
            if key == -4087048084:
                new_query = query + " and subdivision_id = 1"
                params = 'subdivisions'
            elif key == -4054526368:
                new_query = query + " and department_id = 2"
                params = 'departments'
            else:
                new_query = query
                params = None
            filepath = sr.send_reports(new_query, params)
            await bot.send_document(chat_id=key, document=types.FSInputFile(path=filepath))


@dp.message(Command("топ3"))
async def cmd_name(message: types.Message, command: CommandObject):
    params = command.args
    params = sr.check_permission(message.chat.id, params)
    if params == 'denied':
        await message.answer("Нет доступа. Обратитесь к администратору.")
    else:
        query = cn.create_files_query
        if params is None:
            if message.chat.id == sr.master_chat:
                mes = '<b>3 сотрудника с наибольшей вероятностью уволиться:</b>\n'
                mes += sr.predictions(query, 'top')
                await message.answer(mes)
            else:
                await message.answer('Нет доступа к данным')
        else:
            dep_info = sr.find_reqs(params)
            if not dep_info:
                await message.answer(f"Департамент или отдел {params} не найден")
            else:
                mes = f'<b>3 сотрудника с наибольшей вероятностью уволиться {"департамента" if dep_info[1] == "department_id" else "отдела"}: <i>{params}</i></b>\n'
                add_req = f"and u.{dep_info[1]} = '{dep_info[0]}'"
                query += add_req
                mes += sr.predictions(query, 'top')
                await message.answer(mes)

@dp.message(Command("отчет"))
async def cmd_name(message: types.Document, command: CommandObject):
    params = command.args
    params = sr.check_permission(message.chat.id, params)
    if params == 'denied':
        await message.answer("Нет доступа. Обратитесь к администратору.")
    else:
        query = cn.create_files_query
        fname = str(pd.to_datetime('today').normalize().date()).replace('-', '')
        if params is None:
            if message.chat.id == sr.master_chat:
                file = sr.predictions(query, fname)
                await message.answer_document(document=types.FSInputFile(path=file))
            else:
                await message.answer('Нет доступа к данным')
        else:
            dep_info = sr.find_reqs(params)
            if not dep_info:
                await message.answer(f"Департамент или отдел {params} не найден")
            else:
                fname += '-' + str(params)
                add_req = f"and u.{dep_info[1]} = '{dep_info[0]}'"
                query += add_req
                file = sr.predictions(query, fname)
                await message.answer_document(document=types.FSInputFile(path=file))


@dp.message(Command("инфо"))
async def cmd_name(message: types.Message, command: CommandObject):
    if message.chat.id == sr.master_chat:
        if command.args is None:
            await message.answer("Не задан ID сотрудника")
        else:
            if command.args.isdigit():
                mes = sr.pers_info(int(command.args))
                await message.answer(mes)
            else:
                await message.answer("Не верный формат, введите ID сотрудника")
    else:
        await message.answer("В текущей версии доступно только HR")


@dp.message(Command("отслеживать"))
async def cmd_name(message: types.Message, command: CommandObject):
    if message.chat.id == sr.master_chat:
        if command.args is None:
            await message.answer("Не задан ID сотрудника")
        else:
            if command.args.isdigit():
                mes = sr.follow(int(command.args))
                await message.answer(mes)
            else:
                await message.answer("Не верный формат, введите ID сотрудника")
    else:
        await message.answer("В текущей версии добавлять и убирать отслеживание может только HR")

@dp.message(Command("неотслеживать"))
async def cmd_name(message: types.Message, command: CommandObject):
    if message.chat.id == sr.master_chat:
        if command.args is None:
            await message.answer("Не задан ID сотрудника")
        else:
            if command.args.isdigit():
                mes = sr.follow(int(command.args), False)
                await message.answer(mes)
            else:
                await message.answer("Не верный формат, введите ID сотрудника")
    else:
        await message.answer('В текущей версии добавлять и убирать отслеживание может только HR')

@dp.message(Command("список"))
async def cmd_name(message: types.Message, command: CommandObject):
    params = command.args
    params = sr.check_permission(message.chat.id, params)
    if params == 'denied':
        await message.answer("Нет доступа. Обратитесь к администратору.")
    else:
        query = '''
            SELECT CONCAT(u.name, ' ', u.lastname) as fio,
                   u.id, p.position, ub.is_view
            FROM public.users as u
            JOIN user_bots as ub on ub.user_id = u.id
            JOIN positions as p on p.position_id = u.position_id
        '''
        if params is None:
            if message.chat.id == sr.master_chat:
                mes = '<b>Все сотрудники</b>\n'
                mes += sr.user_list(query)
                await message.answer(mes)
            else:
                await message.answer('Нет доступа к данным')
        else:
            dep_info = sr.find_reqs(params)
            if not dep_info:
                await message.answer(f"Департамент или отдел {params} не найден")
            else:
                add_req = f"WHERE {dep_info[1]} = '{dep_info[0]}'"
                mes = f'<b>Сотрудники {"департамента" if dep_info[1] == "department_id" else "отдела"}: <i>{params}</i></b>\n'
                query += add_req
                mes += sr.user_list(query)
                await message.answer(mes)



@dp.message(Command("отслеживаемые"))
async def cmd_name(message: types.Message, command: CommandObject):
    params = command.args
    params = sr.check_permission(message.chat.id, params)
    if params == 'denied':
        await message.answer("Нет доступа. Обратитесь к администратору.")
    else:
        query = cn.follow_query
        if params is None:
            if message.chat.id == sr.master_chat:
                mes = '<b>Все сотрудники</b>\n'
                mes += sr.follow_list(query)
                await message.answer(mes)
            else:
                await message.answer('Нет доступа к данным')
        else:
            dep_info = sr.find_reqs(params)
            if not dep_info:
                await message.answer(f"Департамент или отдел {params} не найден")
            else:
                add_req = f"and {dep_info[1]} = '{dep_info[0]}'"
                mes = f'<b>Сотрудники {"департамента" if dep_info[1] == "department_id" else "отдела"}: <i>{params}</i></b>\n'
                query += add_req
                mes += sr.follow_list(query)
                await message.answer(mes)



@dp.message(Command("группа"))
async def cmd_name(message: types.Message, command: CommandObject):
    try:
        group_num, pers_id = command.args.split()
    except:
        await message.answer("Не задан ID сотрудника или номер группы")
    if message.chat.id == sr.master_chat:
        try:
            mes = sr.add_group(int(pers_id), int(group_num))
            await message.answer(mes)
        except:
            await message.answer("Не верный формат, введите ID сотрудника и группу")
    else:
        await message.answer("В текущей версии добавлять и убирать группу может только HR")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())