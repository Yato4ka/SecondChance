import random

from mongodb import Finder as mongodb
from aiogram import types, Dispatcher
from pymongo import MongoClient

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


class Clans:
    def check_guild(name):
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        guild = check_host["guild"]
        if guild == 0:
            return True
        else:
            return False

    def check_fraction(name):
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        fraction = check_host["fraction"]
        if fraction == 0:
            return True
        else:
            return False

    def check_player(name):
        uid1 = mongodb.findUserIDByName(name)
        uid1 = uid1[0]
        if uid1 is None:
            return False
        else:
            return True

    def give_fraction_bonus(uid1):
        global party
        uid = uid1
        place = mongodb.findUserPlaceByID(uid)
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus_type": party["bonus_type"]}})
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus": party["bonus"]}})
        if party["bonus_type"] == "Посещение":
            print("!")
        if party["bonus_type"] == "Атака":
            fight = mongodb.findUserFightByID(uid)
            players.update_one({"_id": uid},
                               {"$set": {"physical_damage": fight[5] + party["fraction_bonus"]}})

    def give_fraction_bonus_for_leader(uid1, num):
        global party
        uid = uid1
        for party in fraction.find({"num": num}):
            print("Inv finder done")
        print(f'{party["name"]}')
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus_type": party["bonus_type"]}})
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus": party["bonus"]}})
        if party["bonus_type"] == "Посещение":
            print("!")
        if party["bonus_type"] == "Атака":
            fight = mongodb.findUserFightByID(uid)
            players.update_one({"_id": uid},
                               {"$set": {"physical_damage": fight[5] + party["fraction_bonus"]}})

    def pick_fraction_bonus(uid1):
        uid = uid1
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus_type": "отсутствует"}})
        players.update_one({"_id": uid}, {"$set": {"fraction_bonus": 0}})
        if party["bonus_type"] == "Посещение":
            print("!")
        if party["bonus_type"] == "Атака":
            fight = mongodb.findUserFightByID(uid)
            players.update_one({"_id": uid}, {"$set": {"physical_damage": fight[5] - party["fraction_bonus"]}})

# @dp.message_handler(commands='Пригласить_в_организацию')
async def invite(message: types.Message):
    uid = message.from_user.id
    name = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['leader'] == uid:
            check = Clans.check_player(name)
            if check is True:
                players.update_one({"name": name}, {"$set": {"enemy5": party["num"]}})
                await message.answer(f'{name}, вы были приглашены в ограницию "{party["name"]}" лидером! \n'
                                     f'Её рейтинг : {party["rep"]}/100 \n'
                                     f'Что бы вступить в организацию, напишите /Принять \n'
                                     f'Что бы отказать, напишите /Отказать \n')
            else:
                await message.answer(f"Игрок {name} не найден!")
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")

# @dp.message_handler(commands='Принять')
async def accept(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    enemy = mongodb.findUserEnemyByID(uid)
    for party in clans.find({"num": enemy[4]}):
        print("Inv finder done")
    clan = place[2]
    enemy = enemy[4]
    if clan == 0:
        if enemy >= 1:
            players.update_one({"name": name}, {"$set": {"enemy5": 0}})
            if party["member1"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member1": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member1_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member2"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member2": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member2_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member3"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member3": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member3_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member4"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member4": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member4_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member5"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member5": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member5_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member6"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member6": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member6_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member7"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member7": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member7_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member8"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member8": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member8_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member9"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member9": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member9_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            elif party["member10"] == 0:
                clans.update_one({"num": enemy}, {"$set": {"member10": uid}})
                clans.update_one({"num": enemy}, {"$set": {"member10_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": enemy}})
                await message.answer(f'Игрок {name} вступил в организацию "{party["name"]}"')
            else:
                await message.answer(f"Все места в организации заняты!")
        else:
            await message.answer(f"Приглашений не обнаружено!")
    else:
        await message.answer(f'Вы уже состоите в организации!')


# @dp.message_handler(commands='Отклонить')
async def no(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    enemy = mongodb.findUserEnemyByID(uid)
    for party in clans.find({"num": enemy[4]}):
        print("Inv finder done")
    enemy = enemy[4]
    if enemy >= 1:
        players.update_one({"name": name}, {"$set": {"enemy5": 0}})
        await message.answer(f'Приглашение в организацию "{party["name"]}" было отклонено!')
    else:
        await message.answer(f"Приглашений не обнаружено!")


# @dp.message_handler(commands='Покинуть_организацию')
async def leave(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    clan = place[2]
    for party in clans.find({"num": clan}):
        print("Inv finder done")
    if clan > 1:
        players.update_one({"name": name}, {"$set": {"enemy5": 0}})
        if party["member1"] == uid:
            clans.update_one({"num": party["num"]}, {"$set": {"member1": 0 }})
            clans.update_one({"num": party["num"]}, {"$set": {"member1_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member2"] == uid:
            clans.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member2_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member3"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member3_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member4"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member4_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member5"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member5_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member6"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member6_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member7"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member7_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member8"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member8_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member9"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member9_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        elif party["member10"] == 0:
            clans.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
            clans.update_one({"num": party["num"]}, {"$set": {"member10_rep": 0}})
            players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
            players.update_one({"name": name}, {"$set": {"guild": 0}})
            await message.answer(f'Игрок {name} покинул организацию "{party["name"]}"')
        else:
            await message.answer(f"Похоже вы являетесь лидером организации! Расформирейте её или назначьте нового лидера!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Расформировать_организацию')
async def delete(message: types.Message):
    uid = message.from_user.id
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['leader'] == uid:
            clans.delete_one({"num": party["num"]})
            players.update_one({"_id": party['leader']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['leader']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member1']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member1']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member2']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member2']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member3']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member3']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member4']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member4']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member5']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member5']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member6']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member6']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member7']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member7']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member8']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member8']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member9']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member0']}, {"$set": {"guild": 0}})
            players.update_one({"_id": party['member10']}, {"$set": {"guild_respect": 0}})
            players.update_one({"_id": party['member10']}, {"$set": {"guild": 0}})

            await message.answer(f'Организация {party["name"]} была расформирована...')
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Сменить_лидера_на')
async def swap(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['leader'] == uid:
            for new_leader in players.find({"name": name}):
                print("Inv finder done")
            if party["member1"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member1": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member1_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member2"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member2": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member2_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member3"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member3": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member3_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member4"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member4": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member4_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member5"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member5": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member5_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member6"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member6": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member6_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member7"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member7": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member7_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member8"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member8": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member8_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member9"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member9": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member9_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member10"] == new_leader["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 100}})
                clans.update_one({"num": party["num"]}, {"$set": {"member10": uid}})
                clans.update_one({"num": party["num"]}, {"$set": {"member10_rep": 0}})
                players.update_one({"_id": uid}, {"$set": {"guild_respect": 0}})
                await message.answer(f'Лидер организации {party["name"]} был сменён на игрока {new_leader["name"]}...')
            else:
                await message.answer(f'Игрок {name} не состоит в организации {party["name"]}')
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Изменить_репутацию')
async def red(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = int(getter[0])
    name = str(getter[1])
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['leader'] == uid:
            check = Clans.check_player(name)
            if check is True:
                for new_leader in players.find({"name": name}):
                    print("Inv finder done")
                if party['leader'] == new_leader["_id"]:
                    await message.answer(f"Вы не можете повысить репутацию самому себе")
                if party["member1"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member1_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member2"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member2_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member3"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member3_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member4"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member4_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member5"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member5_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member6"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member6_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member7"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member7_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member8"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member8_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member9"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member9_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                elif party["member10"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"guild_respect": what}})
                    clans.update_one({"num": party["num"]}, {"$set": {"member10_rep": what}})
                    await message.answer(
                        f'Лидер организации {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}...')
                else:
                    await message.answer(f'Игрок {name} не состоит в организации {party["name"]}')
            else:
                await message.answer(f"Игрок {name} не найден!")
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Повысить_репутацию_лидера_на')
async def up(message: types.Message):
    uid = message.from_user.id
    what = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['member1'] == uid or party['member2'] == uid or party['member3'] == uid or party['member4'] == uid or party['member5'] == uid or party['member6'] == uid or party['member7'] == uid or party['member8'] == uid or party['member9'] == uid or party['member10'] == uid:
            players.update_one({"_id": party["leader"]}, {"$set": {"guild_respect": party["leader_rep"] + what}})
            clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": party["leader_rep"] + what}})
            await message.answer(
                f'Игрок {party["name"]} повысил репутацию лидера организации {party["name"]} на {what}.')


# @dp.message_handler(commands='Понизить_репутацию_лидера_на')
async def down(message: types.Message):
    uid = message.from_user.id
    what = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['member1'] == uid or party['member2'] == uid or party['member3'] == uid or party['member4'] == uid or party['member5'] == uid or party['member6'] == uid or party['member7'] == uid or party['member8'] == uid or party['member9'] == uid or party['member10'] == uid:
            players.update_one({"_id": party["leader"]}, {"$set": {"guild_respect": party["leader_rep"] - what}})
            clans.update_one({"num": party["num"]}, {"$set": {"leader_rep": party["leader_rep"] - what}})
            await message.answer(
                f'Игрок {party["name"]} понизил репутацию лидера организации {party["name"]} на {what}.')


# @dp.message_handler(commands='Выгнать_игрока')
async def kick(message: types.Message):
    global party
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        if party['leader'] == uid:
            for player in players.find({"name": name}):
                print("Inv finder done")
            if party["member1"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member1": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member1_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member2"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member2_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member3"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member3_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member4"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member4_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member5"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member5_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member6"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member6_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member7"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member7_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member8"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member8_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member9"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member9_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
            elif party["member10"] == player["_id"]:
                clans.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
                clans.update_one({"num": party["num"]}, {"$set": {"member10_rep": 0}})
                players.update_one({"name": name}, {"$set": {"guild_respect": 0}})
                players.update_one({"name": name}, {"$set": {"guild": 0}})
                await message.answer(f'Игрок {name} был выгнан из организации "{party["name"]}"')
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Профиль_организации')
async def prof(message: types.Message):
    global player7, player10, player9, player8, player6, player5, player4, player3, player2, player1, leader, rank, party
    uid = message.from_user.id
    place = mongodb.findUserPlaceByID(uid)
    if place[2] >= 1:
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        for leader in players.find({"_id": party["leader"]}):
            print("Inv finder done")
        for player1 in players.find({"_id": party["member1"]}):
            print("Inv finder done")
        for player2 in players.find({"_id": party["member2"]}):
            print("Inv finder done")
        for player3 in players.find({"_id": party["member3"]}):
            print("Inv finder done")
        for player4 in players.find({"_id": party["member4"]}):
            print("Inv finder done")
        for player5 in players.find({"_id": party["member5"]}):
            print("Inv finder done")
        for player6 in players.find({"_id": party["member6"]}):
            print("Inv finder done")
        for player7 in players.find({"_id": party["member7"]}):
            print("Inv finder done")
        for player8 in players.find({"_id": party["member8"]}):
            print("Inv finder done")
        for player9 in players.find({"_id": party["member9"]}):
            print("Inv finder done")
        for player10 in players.find({"_id": party["member10"]}):
            print("Inv finder done")
        if party["rep"] < 10:
            rank = "[︿]"
        if 10 <= party["rep"] < 20:
            rank = "[︽]"
        if 20 <= party["rep"] < 40:
            rank = "[︿﹀]"
        if 30 <= party["rep"] < 40:
            rank = "[︽﹀]"
        if 40 <= party["rep"] < 50:
            rank = "[︽︾]"
        if 50 <= party["rep"] < 60:
            rank = "[︼]"
        if 60 <= party["rep"] < 70:
            rank = "[︻]"
        if 70 <= party["rep"] < 80:
            rank = "[︼︻]"
        if 80 <= party["rep"] < 90:
            rank = "[⁂]"
        if 90 == party["rep"] < 100:
            rank = "[«⁂»]"
        await message.answer(f'''
⋤-----------------------------------------⋥
※ Профиль организации "{party["name"]}"!
Общая репутация: {party["rep"]}/90 rep - {rank}.

※ Лидер: {leader["name"]}.
Репутация лидера : {party["leader_rep"]}/100.
⋤-----------------------------------------⋥
Участники :

1) Имя: {player1["name"]}
Репутация: {party["member1_rep"]}/100.

2) Имя: {player2["name"]}
Репутация: {party["member2_rep"]}/100.

3) Имя: {player3["name"]}
Репутация: {party["member3_rep"]}/100.

4) Имя: {player4["name"]}
Репутация: {party["member4_rep"]}/100.

5) Имя: {player5["name"]}
Репутация: {party["member5_rep"]}/100.

6) Имя: {player6["name"]}
Репутация: {party["member6_rep"]}/100.

7) Имя: {player7["name"]}
Репутация: {party["member7_rep"]}/100.

8) Имя: {player8["name"]}
Репутация: {party["member8_rep"]}/100.

9) Имя: {player9["name"]}
Репутация: {party["member9_rep"]}/100.

10) Имя: {player10["name"]}
Репутация: {party["member10_rep"]}/100.
⋤-----------------------------------------⋥
''')
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Пригласить_в_фракцию')
async def invite2(message: types.Message):
    uid = message.from_user.id
    name = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[0] >= 1:
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        if party['leader'] == uid:
            check = Clans.check_player(name)
            if check is True:
                players.update_one({"name": name}, {"$set": {"enemy5": party["num"]}})
                await message.answer(f'{name}, вы были приглашены в фракцию "{party["name"]}"! \n'
                                     f'Что бы вступить в фракцию, напишите /Принять_приглашение \n'
                                     f'Что бы отказать, напишите /Отклонить_приглашение  \n')
            else:
                await message.answer(f"Игрок {name} не найден!")
        else:
            await message.answer(f"Вы не являетесь лидером фракции!")
    else:
        await message.answer(f"Вы не состоите в фракции!")

# @dp.message_handler(commands='Принять_приглашение')
async def accept2(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    enemy = mongodb.findUserEnemyByID(uid)
    for party in fraction.find({"num": enemy[4]}):
        print("Inv finder done")
    clan = place[0]
    enemy = enemy[4]
    if clan == 0:
        if enemy >= 1:
            players.update_one({"name": name}, {"$set": {"enemy5": 0}})
            if party["member1"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member1": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member1_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member2"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member2": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member2_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member3"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member3": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member3_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member4"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member4": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member4_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member5"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member5": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member5_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member6"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member6": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member6_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member7"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member7": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member7_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member8"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member8": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member8_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member9"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member9": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member9_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member10"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member10": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member10_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member11"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member11": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member11_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member12"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member12": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member12_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member13"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member13": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member13_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member14"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member14": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member14_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            elif party["member15"] == 0:
                fraction.update_one({"num": enemy}, {"$set": {"member15": uid}})
                fraction.update_one({"num": enemy}, {"$set": {"member15_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": enemy}})
                await message.answer(f'Игрок {name} вступил в фракцию "{party["name"]}"')
            else:
                await message.answer(f"Все места в фракции заняты!")
        else:
            await message.answer(f"Приглашений не обнаружено!")
    else:
        await message.answer(f'Вы уже состоите в фракции!')


# @dp.message_handler(commands='Отклонить_приглашение')
async def no2(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    enemy = mongodb.findUserEnemyByID(uid)
    for party in fraction.find({"num": enemy[4]}):
        print("Inv finder done")
    if enemy[4] >= 1:
        players.update_one({"name": name}, {"$set": {"enemy5": 0}})
        await message.answer(f'Приглашение в фракцию "{party["name"]}" было отклонено!')
    else:
        await message.answer(f"Приглашений не обнаружено!")


# @dp.message_handler(commands='Покинуть_фракцию')
async def leave2(message: types.Message):
    global party
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    clan = place[0]
    for party in fraction.find({"num": clan}):
        print("Inv finder done")
    if clan > 0:
        uid1 = uid
        players.update_one({"name": name}, {"$set": {"enemy5": 0}})
        if party["member1"] == uid:
            fraction.update_one({"num": party["num"]}, {"$set": {"member1": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member1_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member2"] == uid:
            fraction.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member2_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member3"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member3_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member4"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member4_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member5"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member5_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member6"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member6_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member7"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member7_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member8"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member8_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member9"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member9_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member10"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member10_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member11"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member11": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member11_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member12"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member12": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member12_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member13"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member13": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member13_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member14"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member14": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member14_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        elif party["member15"] == 0:
            fraction.update_one({"num": party["num"]}, {"$set": {"member15": 0}})
            fraction.update_one({"num": party["num"]}, {"$set": {"member15_rep": 0}})
            Clans.pick_fraction_bonus(uid1)
            players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
            players.update_one({"name": name}, {"$set": {"fraction": 0}})
            await message.answer(f'Игрок {name} покинул фракцию "{party["name"]}"')
        else:
            await message.answer(f"Похоже вы являетесь лидером фракции! Назначьте нового лидера пеоед выходом!")
    else:
        await message.answer(f"Вы не состоите в организации!")


# @dp.message_handler(commands='Сменить_лидера_фракции_на')
async def swap2(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    place = mongodb.findUserPlaceByID(uid)
    if place[0] >= 1:
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        if party['leader'] == uid:
            for new_leader in players.find({"name": name}):
                print("Inv finder done")
            if party["member1"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member1_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member1": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member1_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member2"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member2_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member2": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member2_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member3"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member3_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member3": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member3_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member4"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member4_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member4": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member4_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member5"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member5_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member5": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member5_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member6"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member6_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member6": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member6_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member7"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member7_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member7": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member7_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member8"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member8_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member8": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member8_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member9"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member9_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member9": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member9_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member10"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member10_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member10": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member10_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member11"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member11_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member11": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member11_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member12"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member12_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member12": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member12_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member13"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member13_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member13": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member13_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member14"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member14_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member14": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member14_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            if party["member15"] == new_leader["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"leader": new_leader["_id"]}})
                fraction.update_one({"num": party["num"]}, {"$set": {"leader_rep": 100}})
                if party["member15_rep"] < 50:
                    uid1 = new_leader["_id"]
                    Clans.give_fraction_bonus(uid1)
                players.update_one({"name": name}, {"$set": {"fraction_respect": 100}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member15": uid}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member15_rep": 90}})
                players.update_one({"_id": uid}, {"$set": {"fraction_respect": 90}})
                await message.answer(f'Лидер фракции {party["name"]} был сменён на игрока {new_leader["name"]}...')
            else:
                await message.answer(f'Игрок {name} не состоит в фракции {party["name"]}')
        else:
            await message.answer(f"Вы не являетесь лидером фракции!")
    else:
        await message.answer(f"Вы не состоите в фракции!")


# @dp.message_handler(commands='Изменить_репутацию_в_фракции')
async def red2(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = int(getter[0])
    name = str(getter[1])
    place = mongodb.findUserPlaceByID(uid)
    if place[0] >= 1:
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        if party['leader'] == uid:
            check = Clans.check_player(name)
            if check is True:
                for new_leader in players.find({"name": name}):
                    print("Inv finder done")
                if party['leader'] == new_leader["_id"]:
                    await message.answer(f"Вы не можете повысить репутацию самому себе")
                uid1 = new_leader["_id"]
                place = mongodb.findUserPlaceByID(uid)
                if party["member1"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member1_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member2"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member2_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member3"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member3_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member4"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member4_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member5"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member5_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member6"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member6_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member7"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member7_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member8"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member8_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member9"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member9_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member10"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member10_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member11"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member11_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member12"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member12_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member13"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member13_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member14"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member14_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                elif party["member15"] == new_leader["_id"]:
                    players.update_one({"name": name}, {"$set": {"fraction_respect": what}})
                    fraction.update_one({"num": party["num"]}, {"$set": {"member15_rep": what}})
                    have = place[1]
                    bonus = place[1] + what
                    if have <= 50 <= bonus:
                        Clans.give_fraction_bonus(uid1)
                    if have >= 50 > bonus:
                        Clans.pick_fraction_bonus(uid1)
                    await message.answer(
                        f'Лидер фракции {party["name"]} изменил репутацию игрока {new_leader["name"]} на {what}.')
                else:
                    await message.answer(f'Игрок {name} не состоит в фракции {party["name"]}')
            else:
                await message.answer(f"Игрок {name} не найден!")
        else:
            await message.answer(f"Вы не являетесь лидером фракции!")
    else:
        await message.answer(f"Вы не состоите в фракции!")


# @dp.message_handler(commands='Выгнать_игрока_из_фракции')
async def kick2(message: types.Message):
    global party
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = message.get_args()
    place = mongodb.findUserPlaceByID(uid)
    if place[0] >= 1:
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        if party['leader'] == uid:
            for player in players.find({"name": name}):
                print("Inv finder done")
            uid1 = player["_id"]
            if party["member1"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member1": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member1_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            elif party["member2"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member2_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            elif party["member3"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member3_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member4"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member4_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member5"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member5_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member6"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member6_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member7"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member7_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member8"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member8_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member9"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member9_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member10"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member10_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member11"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member11": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member11_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member12"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member12": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member12_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member13"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member13": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member13_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member14"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member14": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member14_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
            if party["member15"] == player["_id"]:
                fraction.update_one({"num": party["num"]}, {"$set": {"member15": 0}})
                fraction.update_one({"num": party["num"]}, {"$set": {"member15_rep": 0}})
                players.update_one({"name": name}, {"$set": {"fraction_respect": 0}})
                players.update_one({"name": name}, {"$set": {"fraction": 0}})
                Clans.pick_fraction_bonus(uid1)
                await message.answer(f'Игрок {name} был выгнан из фракции "{party["name"]}"')
        else:
            await message.answer(f"Вы не являетесь лидером фракции!")
    else:
        await message.answer(f"Вы не состоите в фракции!")


# @dp.message_handler(commands='Профиль_фракции')
async def prof2(message: types.Message):
    global player7, player10, player9, player8, player6, player5, player4, player3, player2, player1, leader, rank, party, player15, player14, player13, player12, player11, text, cur
    uid = message.from_user.id
    place = mongodb.findUserPlaceByID(uid)
    if place[0] >= 1:
        for party in fraction.find({"num": place[0]}):
            print("Inv finder done")
        for leader in players.find({"_id": party["leader"]}):
            print("Inv finder done")
        for player1 in players.find({"_id": party["member1"]}):
            print("Inv finder done")
        for player2 in players.find({"_id": party["member2"]}):
            print("Inv finder done")
        for player3 in players.find({"_id": party["member3"]}):
            print("Inv finder done")
        for player4 in players.find({"_id": party["member4"]}):
            print("Inv finder done")
        for player5 in players.find({"_id": party["member5"]}):
            print("Inv finder done")
        for player6 in players.find({"_id": party["member6"]}):
            print("Inv finder done")
        for player7 in players.find({"_id": party["member7"]}):
            print("Inv finder done")
        for player8 in players.find({"_id": party["member8"]}):
            print("Inv finder done")
        for player9 in players.find({"_id": party["member9"]}):
            print("Inv finder done")
        for player10 in players.find({"_id": party["member10"]}):
            print("Inv finder done")
        for player11 in players.find({"_id": party["member11"]}):
            print("Inv finder done")
        for player12 in players.find({"_id": party["member12"]}):
            print("Inv finder done")
        for player13 in players.find({"_id": party["member13"]}):
            print("Inv finder done")
        for player14 in players.find({"_id": party["member14"]}):
            print("Inv finder done")
        for player15 in players.find({"_id": party["member15"]}):
            print("Inv finder done")
        if party["bonus_type"] == "-":
            text = ""
        if party["bonus_type"] == "Посещение":
            text = "Свободное посещение всех горордов (если вы не находитесь в чёрном списке этого города)"
        else:
            text = ""
        await message.answer(f'''
⋤-----------------------------------------⋥
※ Профиль фракции "{party["name"]}"!
※ Лидер: {leader["name"]}.

※ Захваченные точки: [в разработке]
※ Основной город: {party["main"]}
※ Бонус фракции: {text}
⋤-----------------------------------------⋥
Участники (без учёта НПС и второстепенных персонажей):

1) Имя: {player1["name"]}
Репутация: {party["member1_rep"]}/100.

2) Имя: {player2["name"]}
Репутация: {party["member2_rep"]}/100.

3) Имя: {player3["name"]}
Репутация: {party["member3_rep"]}/100.

4) Имя: {player4["name"]}
Репутация: {party["member4_rep"]}/100.

5) Имя: {player5["name"]}
Репутация: {party["member5_rep"]}/100.

6) Имя: {player6["name"]}
Репутация: {party["member6_rep"]}/100.

7) Имя: {player7["name"]}
Репутация: {party["member7_rep"]}/100.

8) Имя: {player8["name"]}
Репутация: {party["member8_rep"]}/100.

9) Имя: {player9["name"]}
Репутация: {party["member9_rep"]}/100.

10) Имя: {player10["name"]}
Репутация: {party["member10_rep"]}/100.

11) Имя: {player11["name"]}
Репутация: {party["member11_rep"]}/100.

12) Имя: {player12["name"]}
Репутация: {party["member12_rep"]}/100.

13) Имя: {player13["name"]}
Репутация: {party["member13_rep"]}/100.

14) Имя: {player14["name"]}
Репутация: {party["member14_rep"]}/100.

15) Имя: {player15["name"]}
Репутация: {party["member15_rep"]}/100.
⋤-----------------------------------------⋥
''')
    else:
        await message.answer(f"Вы не состоите в фракции!")


# @dp.message_handler(commands='Открыть_дешевый_кейс')
async def case(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    coin = cur[2]
    gold = cur[1]
    energy = main[2]
    if coin >= 5:
        players.update_one({"_id": uid}, {"$set": {"coin": coin - 5}})
        await message.answer(
            f"Потрачено 5 коинов, посмотрим же на вашу удачу...")
        a = random.randint(1, 20)
        if a == 1 or a == 2:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 25}})
            await message.answer(f'Вам выпало 25 золота из 150 возможных!')
        elif a == 3 or a == 4:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 50}})
            await message.answer(f'Вам выпало 50 золота из 150 возможных!')
        elif a == 5 or a == 6:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 75}})
            await message.answer(f'Вам выпало 75 золота из 150 возможных!')
        elif a == 7 or a == 8:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 100}})
            await message.answer(f'Вам выпало 100 золота из 150 возможных!')
        elif a == 9 or a == 10:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 125}})
            await message.answer(f'Вам выпало 125 золота из 150 возможных!')
        elif a == 12 or a == 11:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 150}})
            await message.answer(f'Вам выпало 150 золота из 150 возможных!')
        elif a == 13 or a == 14:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 50}})
            await message.answer(f'Вам выпало 50 энергии из 300 возможных!')
        elif a == 15 or a == 16:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 100}})
            await message.answer(f'Вам выпало 100 энергии из 300 возможных!')
        elif a == 17 or a == 18:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 200}})
            await message.answer(f'Вам выпало 200 энергии из 300 возможных!')
        elif a == 19 or a == 20:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 300}})
            await message.answer(f'Вам выпало 300 энергии из 300 возможных!')


# @dp.message_handler(commands='Открыть_обычный_кейс')
async def case1(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    coin = cur[2]
    gold = cur[1]
    energy = main[2]
    if coin >= 25:
        players.update_one({"_id": uid}, {"$set": {"coin": coin - 25}})
        await message.answer(
            f"Потрачено 25 коинов, посмотрим же на вашу удачу...")
        a = random.randint(1, 20)
        if a == 1 or a == 2:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 100}})
            await message.answer(f'Вам выпало 100 золота из 750 возможных!')
        elif a == 3 or a == 4:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 250}})
            await message.answer(f'Вам выпало 250 золота из 750 возможных!')
        elif a == 5 or a == 6:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 375}})
            await message.answer(f'Вам выпало 375 золота из 750 возможных!')
        elif a == 7 or a == 8:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 500}})
            await message.answer(f'Вам выпало 500 золота из 750 возможных!')
        elif a == 9 or a == 10:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 625}})
            await message.answer(f'Вам выпало 625 золота из 750 возможных!')
        elif a == 12 or a == 11:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 750}})
            await message.answer(f'Вам выпало 750 золота из 750 возможных!')
        elif a == 13 or a == 14:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 250}})
            await message.answer(f'Вам выпало 250 энергии из 1500 возможных!')
        elif a == 15 or a == 16:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 500}})
            await message.answer(f'Вам выпало 500 энергии из 300 возможных!')
        elif a == 17 or a == 18:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 1000}})
            await message.answer(f'Вам выпало 1000 энергии из 1500 возможных!')
        elif a == 19 or a == 20:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 1500}})
            await message.answer(f'Вам выпало 1500 энергии из 1500 возможных!')


# @dp.message_handler(commands='Открыть_дорогой_кейс')
async def case2(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    coin = cur[2]
    gold = cur[1]
    energy = main[2]
    if coin >= 50:
        players.update_one({"_id": uid}, {"$set": {"coin": coin - 50}})
        await message.answer(
            f"Потрачено 50 коинов, посмотрим же на вашу удачу...")
        a = random.randint(1, 20)
        if a == 1 or a == 2:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 250}})
            await message.answer(f'Вам выпало 250 золота из 1500 возможных!')
        elif a == 3 or a == 4:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 500}})
            await message.answer(f'Вам выпало 500 золота из 1500 возможных!')
        elif a == 5 or a == 6:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 750}})
            await message.answer(f'Вам выпало 750 золота из 1500 возможных!')
        elif a == 7 or a == 8:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 1000}})
            await message.answer(f'Вам выпало 1000 золота из 1500 возможных!')
        elif a == 9 or a == 10:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 1250}})
            await message.answer(f'Вам выпало 1250 золота из 1500 возможных!')
        elif a == 12 or a == 11:
            players.update_one({"_id": uid}, {"$set": {"gold": gold + 1500}})
            await message.answer(f'Вам выпало 1500 золота из 1500 возможных!')
        elif a == 13 or a == 14:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 500}})
            await message.answer(f'Вам выпало 500 энергии из 3000 возможных!')
        elif a == 15 or a == 16:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 1000}})
            await message.answer(f'Вам выпало 1000 энергии из 3000 возможных!')
        elif a == 17 or a == 18:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 2000}})
            await message.answer(f'Вам выпало 2000 энергии из 3000 возможных!')
        elif a == 19 or a == 20:
            players.update_one({"_id": uid}, {"$set": {"energy": energy + 3000}})
            await message.answer(f'Вам выпало 3000 энергии из 3000 возможных!')


def register_handlers_party(dp: Dispatcher):
    dp.register_message_handler(invite, commands='Пригласить_в_организацию')
    dp.register_message_handler(accept, commands='Принять') #приглашение
    dp.register_message_handler(no, commands='Отклонить') #приглашение
    dp.register_message_handler(leave, commands = 'Покинуть_организацию')
    dp.register_message_handler(delete, commands='Расформировать_организацию')
    dp.register_message_handler(swap, commands='Сменить_лидера_на')
    dp.register_message_handler(red, commands='Изменить_репутацию')
    dp.register_message_handler(up, commands='Повысить_репутацию_лидера_на')
    dp.register_message_handler(down, commands='Понизить_репутацию_лидера_на')
    dp.register_message_handler(kick, commands='Выгнать_игрока')
    dp.register_message_handler(prof, commands='Профиль_организации')

    dp.register_message_handler(invite2, commands='Пригласить_в_фракцию')
    dp.register_message_handler(accept2, commands='Принять_приглашение')  # приглашение
    dp.register_message_handler(no2, commands='Отклонить_приглашение')  # приглашение
    dp.register_message_handler(leave2, commands='Покинуть_фракцию')
    dp.register_message_handler(swap2, commands='Сменить_лидера_фракции_на')
    dp.register_message_handler(red2, commands='Изменить_репутацию_в_фракции')
    dp.register_message_handler(kick2, commands='Выгнать_игрока_из_фракции')
    dp.register_message_handler(prof2, commands='Профиль_фракции')

    dp.register_message_handler(case, commands='Открыть_дешевый_кейс') # 5 коинов
    dp.register_message_handler(case1, commands='Открыть_обычный_кейс') # 25 коинов
    dp.register_message_handler(case2, commands='Открыть_дорогой_кейс') # 50 коинов
