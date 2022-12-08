import asyncio
import random

from mongodb import Finder as mongodb
from aiogram import types, Dispatcher
from pymongo import MongoClient
import craft
import party

cluster = MongoClient("mongodb+srv://Yato:1212@scrp.ym4yecy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["scrp"]
players = db["players"]
levels = db['levels']
inventory = db['inventory']
techniques = db['techniques']
locations_and_clans = db['locations and clans']
clans = db["clans"]
owner = db['owner']
fraction = db['fraction']


class Pay:

    def __init__(self, uid):
        self.uid = uid

    def check_player(name):
        uid1 = mongodb.findUserIDByName(name)
        uid1 = uid1[0]
        if uid1 is None:
            return [False]
        else:
            return [True, uid1]

    def host(host_uid, sum):
        uid = host_uid
        inv = mongodb.findUserInventoryByID(uid)
        if inv[0] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
            return True
        elif inv[1] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
            return True
        elif inv[2] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
            return True
        elif inv[3] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
            return True
        elif inv[4] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
            return True
        elif inv[5] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
            return True
        elif inv[6] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
            return True
        elif inv[7] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
            return True
        elif inv[8] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
            return True
        elif inv[9] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
            return True
        else:
            return False


# @dp.message_handler(commands='Выдать')
async def give(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ' , ').split(' , ')
    what = str(getter[1])
    how = int(getter[0])
    name = str(getter[2])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        check_admin3 = check_sender["Moderator"]
        if check_admin is False:
            if check_admin3 is False:
                await message.answer(f"Недостаточно прав.")
            else:
                if what == "энергию":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    host_have = check_host["energy"]
                    players.update_one({"name": name}, {"$set": {"energy": host_have + how}})
                    await message.answer(f" Модератор {who} выдал игроку {name} <{how}> {what}.")
                if what == "физ_очки":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    host_have = check_host["physical_points"]
                    players.update_one({"name": name}, {"$set": {"physical_points": host_have + how}})
                    await message.answer(f" Модератор {who} выдал игроку {name} <{how}> {what}.")
                if what == "рп_очки":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    host_have = check_host["rp_point"]
                    players.update_one({"name": name}, {"$set": {"rp_point": host_have + how}})
                    await message.answer(f" Модератор {who} выдал игроку {name} <{how}> {what}.")
                else:
                    await message.answer(f"Недостаточно прав.")
        else:
            if what == "золота":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["gold"]
                players.update_one({"name": name}, {"$set": {"gold": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "бэсу":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["grass"]
                players.update_one({"name": name}, {"$set": {"grass": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "базовой магической руды" or what == "бмр":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["iron"]
                players.update_one({"name": name}, {"$set": {"iron": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "энергию":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["energy"]
                players.update_one({"name": name}, {"$set": {"energy": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "физ_очки":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["physical_points"]
                players.update_one({"name": name}, {"$set": {"physical_points": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "рп_очки":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_point"]
                players.update_one({"name": name}, {"$set": {"rp_point": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "мастерство_крафта":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_kraft_skill"]
                players.update_one({"name": name}, {"$set": {"rp_kraft_skill": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "мастерство_алхимии":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_alchemy_skill"]
                players.update_one({"name": name}, {"$set": {"rp_alchemy_skill": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "коины":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["coin"]
                players.update_one({"name": name}, {"$set": {"coin": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")
            if what == "материалы":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["material"]
                players.update_one({"name": name}, {"$set": {"material": host_have + how}})
                await message.answer(f" Администратор {who} выдал игроку {name} <{how}> {what}.")


# @dp.message_handler(commands='Выдать_в_рюкзак_тип1')
async def give2(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = int(getter[0])
    name = str(getter[1])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        if check_admin is False:
            await message.answer(f"Недостаточно прав.")
        else:
            for i in inventory.find({"number": what}):
                print("Cult finder done")
            if i["Type"] != "оружие" and i["Type"] != "пусто":
                host_uid = check_player[1]
                sum = what
                host = Pay.host(host_uid, sum)
                if host is True:
                    await message.answer(f'Администратор {who} выдал игроку {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
            else:
                await message.answer(f"Вы не можете выдавать оружие в этом типе!")


# @dp.message_handler(commands='Выдать_в_рюкзак_тип2')
async def give22(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ' , ').split(' , ')
    name_ow = str(getter[1])
    type = str(getter[0])
    name = str(getter[2])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        if check_admin is False:
            await message.answer(f"Недостаточно прав.")
        else:
            for i in inventory.find({"name": type}):
                print("Cult finder done")
            if i["Type"] == "оружие" :
                if type == "Оружие F ранга":
                    n = 4
                if type == "Оружие F+ ранга" :
                    n = 10
                if type == "Оружие E ранга" :
                    n = 4
                if type == "Оружие E+ ранга+" :
                    n = 10
                if type == "Оружие D ранга":
                    n = 5
                if type == "Оружие D+ ранга" :
                    n = 16
                if type == "Оружие C ранга":
                    n = 17
                if type == "Оружие C+ ранга":
                    n = 18
                if type == "Оружие B ранга":
                    n = 6
                if type == "Оружие B+ ранга":
                    n = 19
                if type == "Оружие A ранга":
                    n = 12
                if type == "Оружие A+ ранга":
                    n = 20
                if type == "Оружие S ранга":
                    n = 11
                if type == "Оружие S+ ранга":
                    n = 21
                uid = mongodb.findUserIDByName(name)
                uid = uid[0]
                check2 = craft.Kraft.give_weapon(uid, n, name_ow)
                if check2 is True:
                    await message.answer(
                        f'Игроку {name} было выдан предмет "оружие {type} ранга" - "{name_ow}" \n '
                        f'Администратор - {who}!')
                else:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
            else:
                await message.answer(f"Вы не можете выдавать оружие в этом типе!")


# @dp.message_handler(commands='Снять')
async def give3(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' у ', ' , ').split(' , ')
    what = str(getter[1])
    how = int(getter[0])
    name = str(getter[2])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        check_admin1 = check_sender["Game_Master"]
        if check_admin is False:
            if check_admin1 is False:
                await message.answer(f"Недостаточно прав.")
            else:
                if what == "хп" or what == "Хп":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    hp = check_host["Hp"]
                    players.update_one({"name": name}, {"$set": {"Hp": hp - how}})
                    await message.answer(f"Game-master {who} снял хп игрока {name} на <{how}> .")
                elif what == "маны" or what == "Маны" or what == "ману" or what == "ману":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    hp = check_host["mana"]
                    players.update_one({"name": name}, {"$set": {"mana": hp - how}})
                    await message.answer(f"Game-master {who} снял ману игрока {name} на <{how}> .")
                else:
                    await message.answer(f"Чет не правильно, примеры команды:\n"
                                         f"/Снять 10 , маны у Пельмень\n"
                                         f"/Снять 10 , хп у Пельмень")

        else:
            if what == "хп" or what == "Хп":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                hp = check_host["Hp"]
                players.update_one({"name": name}, {"$set": {"Hp": hp - how}})
                await message.answer(f" Администратор {who} снял хп игрока {name} на <{how}> .")
            if what == "маны" or what == "Маны" or what == "ману" or what == "ману":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                hp = check_host["mana"]
                players.update_one({"name": name}, {"$set": {"mana": hp - how}})
                await message.answer(f"Администратор {who} снял ману игрока {name} на <{how}> .")
            if what == "золота":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["gold"]
                players.update_one({"name": name}, {"$set": {"gold": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "бэсу":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["grass"]
                players.update_one({"name": name}, {"$set": {"grass": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "базовой магической руды" or what == "бмр":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["iron"]
                players.update_one({"name": name}, {"$set": {"iron": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "энергию":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["energy"]
                players.update_one({"name": name}, {"$set": {"energy": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "физ_очки":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["physical_points"]
                players.update_one({"name": name}, {"$set": {"physical_points": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "рп_очки":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_point"]
                players.update_one({"name": name}, {"$set": {"rp_point": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "мастерство_крафта":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_kraft_skill"]
                players.update_one({"name": name}, {"$set": {"rp_kraft_skill": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "мастерство_алхимии":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["rp_alchemy_skill"]
                players.update_one({"name": name}, {"$set": {"rp_alchemy_skill": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            if what == "коины":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["coin"]
                players.update_one({"name": name}, {"$set": {"coin": host_have - how}})
                await message.answer(f" Администратор {who} снял на <{how}> {what} игрока {name} .")
            else:
                await message.answer(f"Чет не правильно, примеры команды:\n"
                                     f"/Снять 10 , маны у Пельмень\n"
                                     f"/Снять 10 , хп у Пельмень")



# @dp.message_handler(commands='Восстановить')
async def give4(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' у ', ' , ').split(' , ')
    what = str(getter[1])
    how = int(getter[0])
    name = str(getter[2])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        check_admin1 = check_sender["Game_Master"]
        if check_admin is False:
            if check_admin1 is False:
                await message.answer(f"Недостаточно прав.")
            else:
                if what == "хп" or what == "Хп":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    hp = check_host["Hp"]
                    players.update_one({"name": name}, {"$set": {"Hp": hp + how}})
                    await message.answer(f"Game-master {who} восстоновил хп игрока {name} на <{how}> .")
                elif what == "маны" or what == "Маны" or what == "ману" or what == "ману":
                    for check_host in players.find({"name": name}):
                        print("Cult finder done")
                    hp = check_host["mana"]
                    players.update_one({"name": name}, {"$set": {"mana": hp + how}})
                    await message.answer(f"Game-master {who} восстоновил ману игрока {name} на <{how}> .")
                else:
                    await message.answer(f"Чет не правильно, примеры команды:\n"
                                         f"/Восстановить 10 , маны у Пельмень\n"
                                         f"/Восстановить 10 , хп у Пельмень")

        else:
            if what == "хп" or what == "Хп":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                hp = check_host["Hp"]
                players.update_one({"name": name}, {"$set": {"Hp": hp + how}})
                await message.answer(f" Администратор {who} восстоновил хп игрока {name} на <{how}> .")
            elif what == "маны" or what == "Маны" or what == "ману" or what == "ману":
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                hp = check_host["mana"]
                players.update_one({"name": name}, {"$set": {"mana": hp + how}})
                await message.answer(f"Администратор {who} восстоновил ману игрока {name} на <{how}> .")
            else:
                await message.answer(f"Чет не правильно, примеры команды:\n"
                                     f"/Восстановить 10 , маны у Пельмень\n"
                                     f"/Восстановить 10 , хп у Пельмень")


# @dp.message_handler(commands='Выдать_статус')
async def give5(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = str(getter[0])
    name = str(getter[1])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        check_admin1 = check_sender["Game_Master"]
        if check_admin is False:
            if check_admin1 is False:
                await message.answer(f"Недостаточно прав.")
            else:
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                players.update_one({"name": name}, {"$set": {"condition": what}})
                await message.answer(f" Администратор {who} изменил статус игрока {name} на <{what}> .")
        else:
            for check_host in players.find({"name": name}):
                print("Cult finder done")
            players.update_one({"name": name}, {"$set": {"condition": what}})
            await message.answer(f" Администратор {who} изменил статус игрока {name} на <{what}> .")


# @dp.message_handler(commands='Сменить_локацию')
async def lok(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' игроку ', ',').split(',')
    what = int(getter[0])
    name = str(getter[1])
    for loc in locations_and_clans.find({"num": what}):
        print("Inv finder done")
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        check_admin = check_sender["Admin"]
        check_admin1 = check_sender["Game_Master"]
        if check_admin is False:
            if check_admin1 is False:
                await message.answer(f"Недостаточно прав.")
            else:
                players.update_one({"name": name}, {"$set": {"location": what}})
                await message.answer(f' ГМ {who} изменил локацию игрока {name} на <{loc["name"]}> .')
        else:
            players.update_one({"name": name}, {"$set": {"location": what}})
            await message.answer(f' Администратор {who} изменил локацию игрока {name} на <{loc["name"]}> .')


# @dp.message_handler(commands='Создать_орагнизацию')
async def crate(message: types.Message):
    global check_sender, check_host
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' лидер ', ' , ').split(' , ')
    num = int(getter[1])
    party = str(getter[0])
    name = str(getter[2])
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        guild = check_host["guild"]
        if guild == 0:
            for check_sender in players.find({"_id": uid}):
                print("Cult finder done")
            who = check_sender["name"]
            check_admin = check_sender["Admin"]
            if check_admin is True:
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                check_clan = mongodb.findClanByID()
                if check_clan[0] is None:
                    clans.insert_one({
                        "name": party,
                        "rep": 0,
                        "leader": check_host["_id"],
                        "leader_rep": 100,
                        "member1": 0000000000,
                        "member1_rep": 0,
                        "member2": 0000000000,
                        "member2_rep": 0,
                        "member3": 0000000000,
                        "member3_rep": 0,
                        "member4": 0000000000,
                        "member4_rep": 0,
                        "member5": 0000000000,
                        "member5_rep": 0,
                        "member6": 0000000000,
                        "member6_rep": 0,
                        "member7": 0000000000,
                        "member7_rep": 0,
                        "member8": 0000000000,
                        "member8_rep": 0,
                        "member9": 0000000000,
                        "member9_rep": 0,
                        "member10": 0000000000,
                        "member10_rep": 0,
                        "num": num,
                    })
                    players.update_one({"_id": check_host["_id"]}, {"$set": {"guild": num}})
                    players.update_one({"_id": check_host["_id"]}, {"$set": {"guild_respect": 100}})
                    await message.answer(
                        f" Администратор {who} создал команду '{party}', лидером был назначен игрок {name}.")
                else:
                    await message.answer(f"Организация с таким номером уже существует!")
            else:
                await message.answer("Недостаточно прав!")
        else:
            await message.answer(f"Игрок {name} уже состоит в организации!")


# @dp.message_handler(commands='Повысить_репутацию_организации')
async def rep(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    name = str(getter[0])
    what = int(getter[1])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_admin = check_sender["Admin"]
    check_admin1 = check_sender["Game_Master"]
    if check_admin is False:
        if check_admin1 is False:
            await message.answer(f"Недостаточно прав.")
        else:
            for party in clans.find({"name": name}):
                print("Cult finder done")
            clans.update_one({"name": name}, {"$set": {"rep": party["rep"] + what}})
            await message.answer(f' ГМ {who} повысил рейтинг организации "{name}" на "{what}" .')
    else:
        for party in clans.find({"name": name}):
            print("Cult finder done")
        clans.update_one({"name": name}, {"$set": {"rep": party["rep"] + what}})
        await message.answer(f' Администратор {who} повысил рейтинг организации "{name}" на "{what}" .')


# @dp.message_handler(commands='Назначить_лидером_фракции')
async def crate2(message: types.Message):
    global check_fraction, check_sender, check_host
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' игрока ', ',').split(',')
    frac = str(getter[0])
    name = str(getter[1])
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        guild = check_host["fraction"]
        if guild == 0:
            for check_sender in players.find({"_id": uid}):
                print("Cult finder done")
            who = check_sender["name"]
            check_admin = check_sender["Admin"]
            if check_admin is True:
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                for check_fraction in fraction.find({"name": frac}):
                    print("Cult finder done")
                num = check_fraction['num']
                fraction.update_one({"num": num}, {"$set": {"leader": check_host["_id"]}})
                players.update_one({"_id": check_host["_id"]}, {"$set": {"fraction": num}})
                players.update_one({"_id": check_host["_id"]}, {"$set": {"fraction_respect": 100}})
                name1 = check_host["name"]
                party.Clans.give_fraction_bonus_for_leader(name1, num)
                await message.answer(
                    f" Администратор {who} назначил {name} лидером организации '{frac}'.")
            else:
                await message.answer("Недостаточно прав!")
        else:
            await message.answer(f"Игрок {name} уже состоит в организации!")


# @dp.message_handler(commands='update_1.5')
async def update_old(message: types.Message):
    uid = message.from_user.id
    v = mongodb.findUserVersionByID(uid)
    if v[0] != 1.72:
        players.update_one({"_id": uid}, {"$set": {"nw_slot1": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot2": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot3": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot4": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot5": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot6": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot7": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot8": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot9": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot10": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
        players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})

        players.update_one({"_id": uid}, {"$set": {"rune_charge": 0}})

        players.update_one({"_id": uid}, {"$set": {"rp_willpower": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_luck": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_language": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_speed": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_intelligence": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_1sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_2sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_3sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_4sword_master": 0}})

        players.update_one({"_id": uid}, {"$set": {"hunger": 0}})
        players.update_one({"_id": uid}, {"$set": {"thirst": 0}})
        players.update_one({"_id": uid}, {"$set": {"cold": 0}})

        players.update_one({"_id": uid}, {"$set": {"home": 0}})

        players.update_one({"_id": uid}, {"$set": {"fraction_bonus_type": "отсутствует"}})
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus": 0}})

        players.update_one({"_id": uid}, {"$set": {"version": 1.72}})

        await message.answer(f'Вы обновили версию бота до 1.7.2!')
    else:
        await message.answer(f'Вы уже обновили бота!!!')

# @dp.message_handler(commands='update_1.6')
async def update(message: types.Message):
    uid = message.from_user.id
    v = mongodb.findUserVersionByID(uid)
    if v[0] != 1.72:
        players.update_one({"_id": uid}, {"$set": {"rune_charge": 0}})

        players.update_one({"_id": uid}, {"$set": {"rp_language": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_speed": 0}})
        players.update_one({"_id": uid}, {"$set": {"rp_intelligence": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_1sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_2sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_3sword_master": 0}})
        # players.update_one({"_id": uid}, {"$set": {"rp_4sword_master": 0}})

        players.update_one({"_id": uid}, {"$set": {"hunger": 0}})
        players.update_one({"_id": uid}, {"$set": {"thirst": 0}})
        players.update_one({"_id": uid}, {"$set": {"cold": 0}})

        players.update_one({"_id": uid}, {"$set": {"home": 0}})

        players.update_one({"_id": uid}, {"$set": {"fraction_bonus_type": "отсутствует"}})
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus": 0}})

        players.update_one({"_id": uid}, {"$set": {"version": 1.72}})

        await message.answer(f'Вы обновили версию бота до 1.7.2!')
    else:
        await message.answer(f'Вы уже обновили бота!!!')


# @dp.message_handler(commands='Снять_технику_контроля')
async def unstop(message: types.Message):
    uid = message.from_user.id
    name = str(message.get_args())
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_admin = check_sender["Admin"]
    check_admin1 = check_sender["Game_Master"]
    if check_admin is False:
        if check_admin1 is False:
            await message.answer(f"Недостаточно прав.")
        else:
            for findid in players.find({"name": name}):
                print("Cult finder done")
            uid = findid['_id']
            con2 = mongodb.findUserCondition2ByID(uid)
            new_buf_hp_reg = con2[2]
            new_buf_dex = con2[3]
            new_buf_def = con2[4]
            new_buf_k_c = con2[5]
            new_buf_mana_reg = con2[6]
            players.update_one({"_id": uid}, {"$set": {"active_control": 0}})
            players.update_one({"_id": uid}, {"$set": {"debuf_hp_reg": 0}})
            players.update_one({"_id": uid}, {"$set": {"debuf_dex": 0}})
            players.update_one({"_id": uid}, {"$set": {"debuf_def": 0}})
            players.update_one({"_id": uid}, {"$set": {"debuf_k_c": 0}})
            players.update_one({"_id": uid}, {"$set": {"debuf_mana_reg": 0}})
            # статы
            regeneration = findid['regeneration']
            dexterity = findid['dexterity']
            defense = findid['defense']
            Krit_Chance = findid['Krit_Chance']
            regeneration_mana = findid['regeneration_mana']
            players.update_one({"_id": uid}, {"$set": {"regeneration": regeneration + new_buf_hp_reg}})
            players.update_one({"_id": uid}, {"$set": {"dexterity": dexterity + new_buf_dex}})
            players.update_one({"_id": uid}, {"$set": {"defense": defense + new_buf_def}})
            players.update_one({"_id": uid}, {"$set": {"Krit_Chance": Krit_Chance + new_buf_k_c}})
            players.update_one({"_id": uid}, {"$set": {"regeneration_mana": regeneration_mana + new_buf_mana_reg}})
            await message.answer(f' Гейм-мастер {who} снял технику контроля на игроке {name} .')
    else:
        for findid in players.find({"name": name}):
            print("Cult finder done")
        uid = findid['_id']
        con2 = mongodb.findUserCondition2ByID(uid)
        new_buf_hp_reg = con2[2]
        new_buf_dex = con2[3]
        new_buf_def = con2[4]
        new_buf_k_c = con2[5]
        new_buf_mana_reg = con2[6]
        players.update_one({"_id": uid}, {"$set": {"active_control": 0}})
        players.update_one({"_id": uid}, {"$set": {"debuf_hp_reg": 0}})
        players.update_one({"_id": uid}, {"$set": {"debuf_dex": 0}})
        players.update_one({"_id": uid}, {"$set": {"debuf_def": 0}})
        players.update_one({"_id": uid}, {"$set": {"debuf_k_c": 0}})
        players.update_one({"_id": uid}, {"$set": {"debuf_mana_reg": 0}})
        # статы
        regeneration = findid['regeneration']
        dexterity = findid['dexterity']
        defense = findid['defense']
        Krit_Chance = findid['Krit_Chance']
        regeneration_mana = findid['regeneration_mana']
        players.update_one({"_id": uid}, {"$set": {"regeneration": regeneration + new_buf_hp_reg}})
        players.update_one({"_id": uid}, {"$set": {"dexterity": dexterity + new_buf_dex}})
        players.update_one({"_id": uid}, {"$set": {"defense": defense + new_buf_def}})
        players.update_one({"_id": uid}, {"$set": {"Krit_Chance": Krit_Chance + new_buf_k_c}})
        players.update_one({"_id": uid}, {"$set": {"regeneration_mana": regeneration_mana + new_buf_mana_reg}})
        await message.answer(f' Администратор {who} снял технику контроля на игроке {name} .')


# @dp.message_handler(commands='Выдать_технику')
async def givetech(message: types.Message):
    global findid, techid
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ' , ').split(' , ')
    slot = int(getter[1])
    tech = str(getter[0])
    name = str(getter[2])
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_admin = check_sender["Admin"]
    if check_admin is False:
        await message.answer(f"Недостаточно прав.")
    else:
        for findid in players.find({"name": name}):
            print("Cult finder done")
        for techid in techniques.find({"name": tech}):
            print("Cult finder done")
        if slot == 1:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique1": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 2:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique2": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 3:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique3": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 4:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique4": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 5:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique5": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 6:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique6": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 7:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique7": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 8:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique8": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 9:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique9": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 10:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique10": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 11:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique11": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 12:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique12": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 13:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique13": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 14:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique14": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 15:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique15": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 16:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique16": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 17:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique17": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 18:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique18": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 19:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique19": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        elif slot == 20:
            players.update_one({"_id": findid['_id']}, {"$set": {"technique20": techid['num']}})
            await message.answer(f'Администратор {who} выдал игроку {name} технику {techid["name"]} в слот№{slot}')
        else:
            await message.answer(f"Слот номер {slot}???? Ты издеваешься над моим кодом!?")


# @dp.message_handler(commands='Выдать_дом')
async def crate3(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ' , ').split(' , ')
    num = int(getter[1])
    name_of_home = str(getter[0])
    name = str(getter[2])
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        for check_sender in players.find({"_id": uid}):
            print("Cult finder done")
        who = check_sender["name"]
        check_admin = check_sender["Admin"]
        if check_admin is True:
            for check_host in players.find({"name": name}):
                print("Cult finder done")
            owner.insert_one({
                "name": name_of_home,
                "lvl": 1,
                "owner": check_host["_id"],
                "padlock_lvl": 1,
                "member1": 0000000000,
                "member2": 0000000000,
                "member3": 0000000000,
                "member4": 0000000000,
                "member5": 0000000000,
                "member6": 0000000000,
                "member7": 0000000000,
                "member8": 0000000000,
                "member9": 0000000000,
                "member10": 0000000000,
                "chest_1": 0,
                "chest_1_name": "Пусто",
                "chest_2": 0,
                "chest_2_name": "Пусто",
                "chest_3": 0,
                "chest_3_name": "Пусто",
                "chest_4": 0,
                "chest_4_name": "Пусто",
                "chest_5": 0,
                "chest_5_name": "Пусто",
                "chest_6": 0,
                "chest_6_name": "Пусто",
                "chest_7": 0,
                "chest_7_name": "Пусто",
                "chest_8": 0,
                "chest_8_name": "Пусто",
                "chest_9": 0,
                "chest_9_name": "Пусто",
                "chest_10": 0,
                "chest_10_name": "Пусто",
                "chest_11": 0,
                "chest_11_name": "Пусто",
                "chest_12": 0,
                "chest_12_name": "Пусто",
                "chest_13": 0,
                "chest_13_name": "Пусто",
                "chest_14": 0,
                "chest_14_name": "Пусто",
                "chest_15": 0,
                "chest_15_name": "Пусто",
                "chest_16": 0,
                "chest_16_name": "Пусто",
                "chest_17": 0,
                "chest_17_name": "Пусто",
                "chest_18": 0,
                "chest_18_name": "Пусто",
                "chest_19": 0,
                "chest_19_name": "Пусто",
                "chest_20": 0,
                "chest_20_name": "Пусто",
                "chest_21": 0,
                "chest_21_name": "Пусто",
                "chest_22": 0,
                "chest_22_name": "Пусто",
                "chest_23": 0,
                "chest_23_name": "Пусто",
                "chest_24": 0,
                "chest_24_name": "Пусто",
                "chest_25": 0,
                "chest_25_name": "Пусто",
                "chest_26": 0,
                "chest_26_name": "Пусто",
                "chest_27": 0,
                "chest_27_name": "Пусто",
                "chest_28": 0,
                "chest_28_name": "Пусто",
                "chest_29": 0,
                "chest_29_name": "Пусто",
                "chest_30": 0,
                "chest_30_name": "Пусто",
                "workbench_lvl": 0,
                "cooking_rack": 0,
                "greenhouse": 0,
                "garden_bed_1": 0,
                "garden_bed_2": 0,
                "garden_bed_3": 0,
                "garden_bed_4": 0,
                "garden_bed_5": 0,
                "corral": 0,
                "place_1":0,
                "place_2": 0,
                "place_3": 0,
                "place_4": 0,
                "place_5": 0,
                "num": num,
            })
            players.update_one({"_id": check_host["_id"]}, {"$set": {"home": 1}})
            await message.answer(
                f" Администратор {who} создал {name_of_home}, владельцем был назначен игрок '{name}'.")
        else:
            await message.answer("Недостаточно прав!")

# @dp.message_handler(commands='info')
async def info(message: types.Message):
    uid = message.from_user.id
    v = mongodb.findUserVersionByID(uid)
    main = mongodb.findUserMainByID(uid)
    await message.answer(f"""
⋤-----------------------------------------⋥

Информация о @This_is_RP_bot :
Актуальная версия : 1.7.1 (1.71)
Ваша версия : {v[0]}
Гл. админ: @zhong_l1
Модераторы (тип: награда за тренировку) : @VaviI0m
Game-master's: @Nanomachines_son1 , @Haminoki

Вы зарегистрированы как '{main[0]}'.

Статус: включён (ну а как бы он вам ответил, еслиб был выключен?)

⋤-----------------------------------------⋥
""")

# check_admin1 = check_sender["Game_Master"]
# check_admin2 = check_sender["Helper"]
# check_admin3 = check_sender["Moderator"]
# check_admin4 = check_sender["Admin"]

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(give, commands='Выдать')
    dp.register_message_handler(give2, commands='Выдать_в_рюкзак_тип1')
    dp.register_message_handler(give22, commands='Выдать_в_рюкзак_тип2')
    dp.register_message_handler(give3, commands='Снять')
    dp.register_message_handler(give4, commands='Восстановить')
    dp.register_message_handler(give5, commands='Выдать_статус')
    dp.register_message_handler(lok, commands='Сменить_локацию')
    dp.register_message_handler(crate, commands='Создать_орагнизацию')
    dp.register_message_handler(crate3, commands = 'Выдать_дом')
    dp.register_message_handler(crate2, commands = 'Назначить_лидером_фракции')
    dp.register_message_handler(rep, commands='Повысить_репутацию_организации')
    dp.register_message_handler(update, commands='update_1.6')
    dp.register_message_handler(info, commands='info')
    dp.register_message_handler(update_old, commands='update_1.5')
    dp.register_message_handler(unstop, commands='Снять_технику_контроля')
    dp.register_message_handler(givetech, commands='Выдать_технику')

