import random

from mongodb import Finder as mongodb
from aiogram import types, Dispatcher
from pymongo import MongoClient
import pay

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


class the_home:
    def check_home(name):
        for check_host in players.find({"name": name}):
            print("Cult finder done")
        guild = check_host["home"]
        if guild == 0:
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

    def check_lvl(lvl, num):
        for check_host in owner.find({"num": num}):
            print("Cult finder done")
        lvl1 = check_host["lvl"]
        if lvl1 >= lvl:
            return [True, lvl1]
        else:
            return [False, lvl1]

    def check_member1(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["member1"] == 0 or party["member2"] == 0:
            return True
        else:
            return False

    def check_member2(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["member1"] == 0 or party["member2"] == 0 or party["member3"] == 0 or party["member4"] == 0 or party["member5"] == 0:
            return True
        else:
            return False

    def check_member3(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["member1"] == 0 or party["member2"] == 0 or party["member3"] == 0 or party["member4"] == 0 or\
        party["member5"] or party[ "member6"] == 0 or party[ "member7"] == 0 or party[ "member8"] == 0 or\
        party[ "member9"] == 0 or party[ "member10"] == 0:
            return True
        else:
            return False

    def check_inventory1(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["chest_1"] == 0:
            slot = 1
            return [True, slot]
        elif party["chest_2"] == 0:
            slot = 2
            return [True, slot]
        elif party["chest_3"] == 0:
            slot = 3
            return [True, slot]
        elif party["chest_4"] == 0:
            slot = 4
            return [True, slot]
        elif party["chest_5"] == 0:
            slot = 5
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_7"] == 0:
            slot = 7
            return [True, slot]
        elif party["chest_8"] == 0:
            slot = 8
            return [True, slot]
        elif party["chest_9"] == 0:
            slot = 9
            return [True, slot]
        elif party["chest_10"] == 0:
            slot = 10
            return [True, slot]
        else:
            return [False]

    def check_inventory2(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["chest_1"] == 0:
            slot = 1
            return [True, slot]
        elif party["chest_2"] == 0:
            slot = 2
            return [True, slot]
        elif party["chest_3"] == 0:
            slot = 3
            return [True, slot]
        elif party["chest_4"] == 0:
            slot = 4
            return [True, slot]
        elif party["chest_5"] == 0:
            slot = 5
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_7"] == 0:
            slot = 7
            return [True, slot]
        elif party["chest_8"] == 0:
            slot = 8
            return [True, slot]
        elif party["chest_9"] == 0:
            slot = 9
            return [True, slot]
        elif party["chest_10"] == 0:
            slot = 10
            return [True, slot]
        elif party["chest_11"] == 0:
            slot = 11
            return [True, slot]
        elif party["chest_12"] == 0:
            slot = 12
            return [True, slot]
        elif party["chest_13"] == 0:
            slot = 13
            return [True, slot]
        elif party["chest_14"] == 0:
            slot = 14
            return [True, slot]
        elif party["chest_15"] == 0:
            slot = 15
            return [True, slot]
        elif party["chest_16"] == 0:
            slot = 16
            return [True, slot]
        elif party["chest_17"] == 0:
            slot = 17
            return [True, slot]
        elif party["chest_18"] == 0:
            slot = 18
            return [True, slot]
        elif party["chest_19"] == 0:
            slot = 19
            return [True, slot]
        elif party["chest_20"] == 0:
            slot = 20
            return [True, slot]
        else:
            return [False]

    def check_inventory3(num):
        for party in owner.find({"num": num}):
            print("Cult finder done")
        if party["chest_1"] == 0:
            slot = 1
            return [True, slot]
        elif party["chest_2"] == 0:
            slot = 2
            return [True, slot]
        elif party["chest_3"] == 0:
            slot = 3
            return [True, slot]
        elif party["chest_4"] == 0:
            slot = 4
            return [True, slot]
        elif party["chest_5"] == 0:
            slot = 5
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_6"] == 0:
            slot = 6
            return [True, slot]
        elif party["chest_7"] == 0:
            slot = 7
            return [True, slot]
        elif party["chest_8"] == 0:
            slot = 8
            return [True, slot]
        elif party["chest_9"] == 0:
            slot = 9
            return [True, slot]
        elif party["chest_10"] == 0:
            slot = 10
            return [True, slot]
        elif party["chest_11"] == 0:
            slot = 11
            return [True, slot]
        elif party["chest_12"] == 0:
            slot = 12
            return [True, slot]
        elif party["chest_13"] == 0:
            slot = 13
            return [True, slot]
        elif party["chest_14"] == 0:
            slot = 14
            return [True, slot]
        elif party["chest_15"] == 0:
            slot = 15
            return [True, slot]
        elif party["chest_16"] == 0:
            slot = 16
            return [True, slot]
        elif party["chest_17"] == 0:
            slot = 17
            return [True, slot]
        elif party["chest_18"] == 0:
            slot = 18
            return [True, slot]
        elif party["chest_19"] == 0:
            slot = 19
            return [True, slot]
        elif party["chest_20"] == 0:
            slot = 20
            return [True, slot]
        elif party["chest_21"] == 0:
            slot = 21
            return [True, slot]
        elif party["chest_22"] == 0:
            slot = 22
            return [True, slot]
        elif party["chest_23"] == 0:
            slot = 23
            return [True, slot]
        elif party["chest_24"] == 0:
            slot = 24
            return [True, slot]
        elif party["chest_25"] == 0:
            slot = 25
            return [True, slot]
        elif party["chest_26"] == 0:
            slot = 26
            return [True, slot]
        elif party["chest_27"] == 0:
            slot = 27
            return [True, slot]
        elif party["chest_28"] == 0:
            slot = 28
            return [True, slot]
        elif party["chest_29"] == 0:
            slot = 29
            return [True, slot]
        elif party["chest_30"] == 0:
            slot = 30
            return [True, slot]
        else:
            return [False]



# @dp.message_handler(commands='Пригласить_в_дом')
async def invite_home(message: types.Message):
    uid = message.from_user.id
    name = message.get_args()
    cur = mongodb.findUserCurrencyByID(uid)
    main = mongodb.findUserMainByID(uid)
    if cur[9] == 1:
        for home_tag in owner.find({"num": cur[9]}):
            print("Inv finder done")
        if home_tag['owner'] == uid:
            check = the_home.check_player(name)
            if check is True:
                lvl = 4
                num = cur[9]
                level = the_home.check_lvl(lvl, num)
                if level[0] is True:
                    if 4 <= level[1] < 6:
                        mem = the_home.check_member1(num)
                    elif 6 <= level[1] < 9:
                        mem = the_home.check_member2(num)
                    elif 9 <= level[1] <= 10:
                        mem = the_home.check_member3(num)
                    if mem is True:
                        players.update_one({"name": name}, {"$set": {"enemy4": home_tag["num"]}})
                        await message.answer(f'{name}, вы были приглашены в дом "{home_tag["name"]}" игрока {main[0]}! \n'
                                             f'Уровень дома : {home_tag["lvl"]}/10 \n'
                                             f'Что бы переехать в дом, напишите /+ \n'
                                             f'Что бы отказать, напишите /- \n')
                    else:
                        await message.answer(f"Вы достигли лимита жильцов на вашем уровне дома!")
                else:
                    await message.answer(f"Вам требуется минимум четвёртый уровень дома, что бы поселять в нём людей!")
            else:
                await message.answer(f"Игрок {name} не найден!")
        else:
            await message.answer(f"Вы не являетесь лидером организации!")
    else:
        await message.answer(f"Вы не состоите в организации!")

# @dp.message_handler(commands='+')
async def accept_home(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    cur = mongodb.findUserCurrencyByID(uid)
    enemy = mongodb.findUserEnemyByID(uid)
    for party in owner.find({"num": enemy[3]}):
        print("Inv finder done")
    clan = cur[9]
    enemy = enemy[3]
    if clan == 0:
        if enemy >= 1:
            if party["member1"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member1": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member2"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member2": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member3"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member3": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member4"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member4": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member5"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member5": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member6"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member6": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member7"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member7": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member8"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member8": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member9"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member9": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            elif party["member10"] == 0:
                owner.update_one({"num": enemy}, {"$set": {"member10": uid}})
                players.update_one({"name": name}, {"$set": {"home": enemy}})
                await message.answer(f'Игрок {name} переехал в "{party["name"]}"')
            else:
                await message.answer(f"Все места в доме заняты!")
            players.update_one({"name": name}, {"$set": {"enemy4": 0}})
        else:
            await message.answer(f"Приглашений не обнаружено!")
    else:
        await message.answer(f'Вы уже состоите в доме!')


# @dp.message_handler(commands='-')
async def no(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    enemy = mongodb.findUserEnemyByID(uid)
    for party in owner.find({"num": enemy[3]}):
        print("Inv finder done")
    enemy = enemy[3]
    if enemy >= 1:
        players.update_one({"name": name}, {"$set": {"enemy4": 0}})
        await message.answer(f'Приглашение в дом "{party["name"]}" было отклонено!')
    else:
        await message.answer(f"Приглашений не обнаружено!")


# @dp.message_handler(commands='Покинуть_дом')
async def leave(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    name = main[0]
    cur = mongodb.findUserCurrencyByID(uid)
    clan = cur[9]
    for party in owner.find({"num": clan}):
        print("Inv finder done")
    if clan >= 1:
        players.update_one({"name": name}, {"$set": {"enemy4": 0}})
        if party["member1"] == uid:
            owner.update_one({"num": party["num"]}, {"$set": {"member1": 0 }})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member2"] == uid:
            owner.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member3"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member4"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member5"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member6"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member7"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member8"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member9"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        elif party["member10"] == 0:
            owner.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
            players.update_one({"name": name}, {"$set": {"home": 0}})
            await message.answer(f'Игрок {name} покинул "{party["name"]}"')
        else:
            await message.answer(f"Похоже вы являетесь владельцем дома! Передайте права владельца дома другому игроку или продайте его админитсрации перед выходом!")
    else:
        await message.answer(f"У вас нет дома!")


# @dp.message_handler(commands='Передать_дом')
async def swap(message: types.Message):
    global party
    uid = message.from_user.id
    name = message.get_args()
    cur = mongodb.findUserCurrencyByID(uid)
    if cur[9] >= 1:
        for party in owner.find({"num": cur[9]}):
            print("Inv finder done")
        if party['owner'] == uid:
            for new_leader in players.find({"name": name}):
                print("Inv finder done")
            if party["member1"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member1": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member2"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member2": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member3"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member3": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member4"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member4": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member5"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member5": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member6"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member6": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member7"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member7": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member8"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member8": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member9"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member9": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            elif party["member10"] == new_leader["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"owner": new_leader["_id"]}})
                owner.update_one({"num": party["num"]}, {"$set": {"member10": uid}})
                await message.answer(f'Владелец {party["name"]} был сменён на игрока {new_leader["name"]}.')
            else:
                await message.answer(f'Игрок {name} не состоит в доме {party["name"]}')
        else:
            await message.answer(f"Вы не являетесь лидером дома!")
    else:
        await message.answer(f"Вы не состоите в доме!")


# @dp.message_handler(commands='Прогнать')
async def kick(message: types.Message):
    global party
    uid = message.from_user.id
    name = message.get_args()
    cur = mongodb.findUserCurrencyByID(uid)
    if cur[9] >= 1:
        for party in owner.find({"num": cur[9]}):
            print("Inv finder done")
        if party['owner'] == uid:
            for player in players.find({"name": name}):
                print("Inv finder done")
            if party["member1"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member1": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member2"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member2": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member3"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member3": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member4"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member4": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member5"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member5": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member6"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member6": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member7"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member7": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member8"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member8": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member9"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member9": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
            elif party["member10"] == player["_id"]:
                owner.update_one({"num": party["num"]}, {"$set": {"member10": 0}})
                players.update_one({"name": name}, {"$set": {"home": 0}})
                await message.answer(f'Игрок {name} был выгнан из "{party["name"]}"')
        else:
            await message.answer(f"Вы не являетесь владельцем дома!")
    else:
        await message.answer(f"Вы не состоите в доме!")


# @dp.message_handler(commands='Профиль_дома')
async def prof(message: types.Message):
    global player7, player10, player9, player8, player6, player5, player4, player3, player2, player1, leader, rank, party
    uid = message.from_user.id
    cur = mongodb.findUserCurrencyByID(uid)
    if cur[9] >= 1:
        for party in owner.find({"num": cur[9]}):
            print("Inv finder done")
        for leader in players.find({"_id": party["owner"]}):
            print("Inv finder done")

        if party["chest_1"] > 0:
            for slot1 in inventory.find({"number": party["chest_1"]}):
                print("Inv finder done")
            name_slot_1 = slot1['name']
            if slot1["Type"] == "оружие":
                name_slot_1 = party["chest_1_name"]
        else:
            name_slot_1 = "Пусто"

        if party["chest_2"] > 0:
            for slot2 in inventory.find({"number": party["chest_2"]}):
                print("Inv finder done")
            name_slot_2 = slot2['name']
            if slot1["Type"] == "оружие":
                name_slot_2 = party["chest_2_name"]
        else:
            name_slot_2 = "Пусто"

        if party["chest_3"] > 0:
            for slot3 in inventory.find({"number": party["chest_3"]}):
                print("Inv finder done")
            name_slot_3 = slot3['name']
            if slot3["Type"] == "оружие":
                name_slot_3 = party["chest_3_name"]
        else:
            name_slot_3 = "Пусто"

        if party["chest_4"] > 0:
            for slot4 in inventory.find({"number": party["chest_4"]}):
                print("Inv finder done")
            name_slot_4 = slot4['name']
            if slot4["Type"] == "оружие":
                name_slot_4 = party["chest_4_name"]
        else:
            name_slot_4 = "Пусто"

        if party["chest_5"] > 0:
            for slot5 in inventory.find({"number": party["chest_5"]}):
                print("Inv finder done")
            name_slot_5 = slot1['name']
            if slot5["Type"] == "оружие":
                name_slot_5 = party["chest_5_name"]
        else:
            name_slot_5 = "Пусто"

        if party["chest_6"] > 0:
            for slot6 in inventory.find({"number": party["chest_6"]}):
                print("Inv finder done")
            name_slot_6 = slot6['name']
            if slot6["Type"] == "оружие":
                name_slot_6 = party["chest_6_name"]
        else:
            name_slot_6 = "Пусто"

        if party["chest_7"] > 0:
            for slot7 in inventory.find({"number": party["chest_7"]}):
                print("Inv finder done")
            name_slot_7 = slot7['name']
            if slot7["Type"] == "оружие":
                name_slot_7 = party["chest_7_name"]
        else:
            name_slot_7 = "Пусто"

        if party["chest_1"] > 0:
            for slot8 in inventory.find({"number": party["chest_8"]}):
                print("Inv finder done")
            name_slot_8 = slot8['name']
            if slot8["Type"] == "оружие":
                name_slot_8 = party["chest_8_name"]
        else:
            name_slot_8 = "Пусто"

        if party["chest_9"] > 0:
            for slot9 in inventory.find({"number": party["chest_9"]}):
                print("Inv finder done")
            name_slot_9 = slot9['name']
            if slot9["Type"] == "оружие":
                name_slot_9 = party["chest_9_name"]
        else:
            name_slot_9 = "Пусто"

        if party["chest_10"] > 0:
            for slot10 in inventory.find({"number": party["chest_10"]}):
                print("Inv finder done")
            name_slot_10 = slot10['name']
            if slot10["Type"] == "оружие":
                name_slot_10 = party["chest_10_name"]
        else:
            name_slot_10 = "Пусто"

        if party['lvl'] < 3:
            name_slot_11 = "Откроется на 3lvl-е дома"
            name_slot_12 = "Откроется на 3lvl-е дома"
            name_slot_13 = "Откроется на 3lvl-е дома"
            name_slot_14 = "Откроется на 3lvl-е дома"
            name_slot_15 = "Откроется на 3lvl-е дома"
            name_slot_16 = "Откроется на 3lvl-е дома"
            name_slot_17 = "Откроется на 3lvl-е дома"
            name_slot_18 = "Откроется на 3lvl-е дома"
            name_slot_19 = "Откроется на 3lvl-е дома"
            name_slot_20 = "Откроется на 3lvl-е дома"
        else:
            if party["chest_11"] > 0:
                for slot11 in inventory.find({"number": party["chest_11"]}):
                    print("Inv finder done")
                name_slot_11 = slot11['name']
                if slot11["Type"] == "оружие":
                    name_slot_11 = party["chest_11_name"]
            else:
                name_slot_11 = "Пусто"
            if party["chest_12"] > 0:
                for slot12 in inventory.find({"number": party["chest_12"]}):
                    print("Inv finder done")
                name_slot_12 = slot12['name']
                if slot12["Type"] == "оружие":
                    name_slot_12 = party["chest_12_name"]
            else:
                name_slot_12 = "Пусто"
            if party["chest_13"] > 0:
                for slot13 in inventory.find({"number": party["chest_13"]}):
                    print("Inv finder done")
                name_slot_13 = slot13['name']
                if slot13["Type"] == "оружие":
                    name_slot_13 = party["chest_13_name"]
            else:
                name_slot_13 = "Пусто"
            if party["chest_14"] > 0:
                for slot14 in inventory.find({"number": party["chest_14"]}):
                    print("Inv finder done")
                name_slot_14 = slot14['name']
                if slot14["Type"] == "оружие":
                    name_slot_14 = party["chest_14_name"]
            else:
                name_slot_14 = "Пусто"
            if party["chest_15"] > 0:
                for slot15 in inventory.find({"number": party["chest_15"]}):
                    print("Inv finder done")
                name_slot_15 = slot15['name']
                if slot15["Type"] == "оружие":
                    name_slot_15 = party["chest_15_name"]
            else:
                name_slot_15 = "Пусто"
            if party["chest_16"] > 0:
                for slot16 in inventory.find({"number": party["chest_16"]}):
                    print("Inv finder done")
                name_slot_16 = slot16['name']
                if slot16["Type"] == "оружие":
                    name_slot_16 = party["chest_16_name"]
            else:
                name_slot_16 = "Пусто"
            if party["chest_17"] > 0:
                for slot17 in inventory.find({"number": party["chest_17"]}):
                    print("Inv finder done")
                name_slot_17 = slot17['name']
                if slot17["Type"] == "оружие":
                    name_slot_17 = party["chest_17_name"]
            else:
                name_slot_17 = "Пусто"
            if party["chest_18"] > 0:
                for slot18 in inventory.find({"number": party["chest_18"]}):
                    print("Inv finder done")
                name_slot_18 = slot18['name']
                if slot18["Type"] == "оружие":
                    name_slot_18 = party["chest_18_name"]
            else:
                name_slot_18 = "Пусто"
            if party["chest_19"] > 0:
                for slot19 in inventory.find({"number": party["chest_19"]}):
                    print("Inv finder done")
                name_slot_19 = slot19['name']
                if slot19["Type"] == "оружие":
                    name_slot_19 = party["chest_19_name"]
            else:
                name_slot_19 = "Пусто"
            if party["chest_20"] > 0:
                for slot20 in inventory.find({"number": party["chest_20"]}):
                    print("Inv finder done")
                name_slot_20 = slot20['name']
                if slot20["Type"] == "оружие":
                    name_slot_20 = party["chest_20_name"]
            else:
                name_slot_20 = "Пусто"

        if party['lvl'] < 7:
            name_slot_21 = "Откроется на 7lvl-е дома"
            name_slot_22 = "Откроется на 7lvl-е дома"
            name_slot_23 = "Откроется на 7lvl-е дома"
            name_slot_24 = "Откроется на 7lvl-е дома"
            name_slot_25 = "Откроется на 7lvl-е дома"
            name_slot_26 = "Откроется на 7lvl-е дома"
            name_slot_27 = "Откроется на 7lvl-е дома"
            name_slot_28 = "Откроется на 7lvl-е дома"
            name_slot_29 = "Откроется на 7lvl-е дома"
            name_slot_30 = "Откроется на 7lvl-е дома"
        else:
            if party["chest_21"] > 0:
                for slot21 in inventory.find({"number": party["chest_21"]}):
                    print("Inv finder done")
                name_slot_21 = slot21['name']
                if slot21["Type"] == "оружие":
                    name_slot_21 = party["chest_21_name"]
            else:
                name_slot_21 = "Пусто"
            if party["chest_22"] > 0:
                for slot22 in inventory.find({"number": party["chest_22"]}):
                    print("Inv finder done")
                name_slot_22 = slot22['name']
                if slot22["Type"] == "оружие":
                    name_slot_22 = party["chest_22_name"]
            else:
                name_slot_22 = "Пусто"
            if party["chest_23"] > 0:
                for slot23 in inventory.find({"number": party["chest_23"]}):
                    print("Inv finder done")
                name_slot_23 = slot23['name']
                if slot23["Type"] == "оружие":
                    name_slot_23 = party["chest_23_name"]
            else:
                name_slot_23 = "Пусто"
            if party["chest_24"] > 0:
                for slot24 in inventory.find({"number": party["chest_24"]}):
                    print("Inv finder done")
                name_slot_24 = slot24['name']
                if slot24["Type"] == "оружие":
                    name_slot_24 = party["chest_24_name"]
            else:
                name_slot_24 = "Пусто"
            if party["chest_25"] > 0:
                for slot25 in inventory.find({"number": party["chest_25"]}):
                    print("Inv finder done")
                name_slot_25 = slot25['name']
                if slot25["Type"] == "оружие":
                    name_slot_25 = party["chest_25_name"]
            else:
                name_slot_25 = "Пусто"
            if party["chest_26"] > 0:
                for slot26 in inventory.find({"number": party["chest_26"]}):
                    print("Inv finder done")
                name_slot_26 = slot26['name']
                if slot26["Type"] == "оружие":
                    name_slot_26 = party["chest_26_name"]
            else:
                name_slot_26 = "Пусто"
            if party["chest_27"] > 0:
                for slot27 in inventory.find({"number": party["chest_27"]}):
                    print("Inv finder done")
                name_slot_27 = slot27['name']
                if slot27["Type"] == "оружие":
                    name_slot_27 = party["chest_27_name"]
            else:
                name_slot_27 = "Пусто"
            if party["chest_28"] > 0:
                for slot28 in inventory.find({"number": party["chest_28"]}):
                    print("Inv finder done")
                name_slot_28 = slot28['name']
                if slot28["Type"] == "оружие":
                    name_slot_28 = party["chest_28_name"]
            else:
                name_slot_28 = "Пусто"
            if party["chest_29"] > 0:
                for slot29 in inventory.find({"number": party["chest_29"]}):
                    print("Inv finder done")
                name_slot_29 = slot29['name']
                if slot19["Type"] == "оружие":
                    name_slot_29 = party["chest_29_name"]
            else:
                name_slot_29 = "Пусто"
            if party["chest_30"] > 0:
                for slot30 in inventory.find({"number": party["chest_30"]}):
                    print("Inv finder done")
                name_slot_30 = slot30['name']
                if slot30["Type"] == "оружие":
                    name_slot_30 = party["chest_30_name"]
            else:
                name_slot_30 = "Пусто"

        if party["workbench_lvl"] > 0:
            if party["workbench_lvl"] == 1:
                workbench = "Верстак (1lvl/3lvl)"
            if party["workbench_lvl"] == 2:
                workbench = "Небольшая кузница(2lvl/3lvl)"
            if party["workbench_lvl"] == 3:
                workbench = "Небесная кузница(3lvl/3lvl)"
        else:
            workbench = "Отсутствует"

        if party["cooking_rack"] > 0:
            if party["cooking_rack"] == 1:
                cooking_rack = "Варочная стойка (1lvl/3lvl)"
            if party["cooking_rack"] == 2:
                cooking_rack = "Небольшая алхимическая станция(2lvl/3lvl)"
            if party["cooking_rack"] == 3:
                cooking_rack = "Небесная лаборатория (3lvl/3lvl)"
        else:
            cooking_rack = "Отсутствует"

        if party["lvl"] == 1:
            rank = "[︿]"
        if party["lvl"] == 2:
            rank = "[︽]"
        if party["lvl"] == 3:
            rank = "[︿﹀]"
        if party["lvl"] == 4:
            rank = "[︽﹀]"
        if party["lvl"] == 5:
            rank = "[︽︾]"
        if party["lvl"] == 6:
            rank = "[︼]"
        if party["lvl"] == 7:
            rank = "[︻]"
        if party["lvl"] == 8:
            rank = "[︼︻]"
        if party["lvl"] == 9:
            rank = "[⁂]"
        if party["lvl"] == 10:
            rank = "[«⁂»]"

        if party['lvl'] < 4:
            player1 = "Откроется на 4lvl-е дома"
            player2 = "Откроется на 4lvl-е дома"
        else:
            for player1 in players.find({"_id": party["member1"]}):
                print("Inv finder done")
            for player2 in players.find({"_id": party["member2"]}):
                print("Inv finder done")
            player1 = player1["name"]
            player2 = player2["name"]

        if party['lvl'] < 6:
            player3 = "Откроется на 6lvl-е дома"
            player4 = "Откроется на 6lvl-е дома"
            player5 = "Откроется на 6lvl-е дома"
        else:
            for player3 in players.find({"_id": party["member3"]}):
                print("Inv finder done")
            for player4 in players.find({"_id": party["member4"]}):
                print("Inv finder done")
            for player5 in players.find({"_id": party["member5"]}):
                print("Inv finder done")
            player3 = player3['name']
            player4 = player4['name']
            player5 = player5['name']

        if party['lvl'] < 9:
            player6 = "Откроется на 9lvl-е дома"
            player7 = "Откроется на 9lvl-е дома"
            player8 = "Откроется на 9lvl-е дома"
            player9 = "Откроется на 9lvl-е дома"
            player10 = "Откроется на 9lvl-е дома"
        else:
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
            player6 = player6["name"]
            player7 = player7["name"]
            player8 = player8["name"]
            player9 = player9["name"]
            player10 = player10["name"]

        await message.answer(f'''
⋤-----------------------------------------⋥
※ Профиль "{party["name"]}"!
※ Уровень дома: {party["lvl"]}/10 [{rank}].

※ Владелец: {leader["name"]}.

※ Кузница: {workbench}
※ Лаборатория: {cooking_rack}
※ Теплица: Отсутствует [в разработке]
※ Загон: Отсутствует [в разработке]
⋤-----------------------------------------⋥
※ Участники :

1) Имя: {player1}

2) Имя: {player2}

3) Имя: {player3}

4) Имя: {player4}

5) Имя: {player5}

6) Имя: {player6}

7) Имя: {player7}

8) Имя: {player8}

9) Имя: {player9}

10) Имя: {player10}

⋤-----------------------------------------⋥''')
        await message.answer(f'''
⋤-----------------------------------------⋥
Сундуки:

1) {name_slot_1}
2) {name_slot_2}
3) {name_slot_3}
4) {name_slot_4}
5) {name_slot_5}
6) {name_slot_6}
7) {name_slot_7}
8) {name_slot_8}
9) {name_slot_9}
10) {name_slot_10}
11) {name_slot_11}
12) {name_slot_12}
13) {name_slot_13}
14) {name_slot_14}
15) {name_slot_15}
16) {name_slot_16}
17) {name_slot_17}
18) {name_slot_18}
19) {name_slot_19}
20) {name_slot_20}
21) {name_slot_21}
22) {name_slot_22}
23) {name_slot_23}
24) {name_slot_24}
25) {name_slot_25}
26) {name_slot_26}
27) {name_slot_27}
28) {name_slot_28}
29) {name_slot_29}
30) {name_slot_30}

⋤-----------------------------------------⋥
''')
    else:
        await message.answer(f"Вы не состоите в доме!")

# @dp.message_handler(commands='Отправить_в_сундук')
async def chest_1(message: types.Message):
    global inv_slot, item_name
    uid = message.from_user.id
    msg = int(message.get_args())
    main = mongodb.findUserMainByID(uid)
    inv = mongodb.findUserInventoryByID(uid)
    invn = mongodb.findUserInventoryNameByID(uid)
    cur = mongodb.findUserCurrencyByID(uid)
    if cur[9] == 0:
        await message.answer(f"У вас нет дома!")
    else:
        for party in owner.find({"num": cur[9]}):
            print("Inv finder done")
        num = cur[9]
        a = the_home.check_inventory1(num)
        if party["lvl"] >= 3:
            a = the_home.check_inventory2(num)
        if party["lvl"] >= 7:
            a = the_home.check_inventory2(num)
        if a[0] is True:
            if msg == 1:
                inv_slot = inv[0]
                item_name = invn[0]
                players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
            if msg == 2:
                inv_slot = inv[1]
                item_name = invn[1]
                players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
            if msg == 3:
                inv_slot = inv[2]
                item_name = invn[2]
                players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
            if msg == 4:
                inv_slot = inv[3]
                item_name = invn[3]
                players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
            if msg == 5:
                inv_slot = inv[4]
                item_name = invn[4]
                players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
            if msg == 6:
                inv_slot = inv[5]
                item_name = invn[5]
                players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
            if msg == 7:
                inv_slot = inv[6]
                item_name = invn[6]
                players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
            if msg == 8:
                inv_slot = inv[7]
                item_name = invn[7]
                players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
            if msg == 9:
                inv_slot = inv[8]
                item_name = invn[8]
                players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
            if msg == 10:
                inv_slot = inv[9]
                item_name = invn[9]
                players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
            if inv_slot == 0:
                await message.answer(f'Слот №{msg} в рюкзаке пуст!')
            else:
                if a[1] == 1:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_1": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_1_name": item_name}})
                if a[1] == 2:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_2": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_2_name": item_name}})
                if a[1] == 3:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_3": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_3_name": item_name}})
                if a[1] == 4:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_4": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_4_name": item_name}})
                if a[1] == 5:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_5": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_5_name": item_name}})
                if a[1] == 6:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_6": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_6_name": item_name}})
                if a[1] == 7:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_7": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_7_name": item_name}})
                if a[1] == 8:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_8": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_8_name": item_name}})
                if a[1] == 9:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_9": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_9_name": item_name}})
                if a[1] == 10:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_10": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_10_name": item_name}})
                if a[1] == 11:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_11": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_11_name": item_name}})
                if a[1] == 12:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_12": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_12_name": item_name}})
                if a[1] == 13:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_13": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_13_name": item_name}})
                if a[1] == 14:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_14": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_14_name": item_name}})
                if a[1] == 15:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_15": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_15_name": item_name}})
                if a[1] == 16:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_16": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_16_name": item_name}})
                if a[1] == 17:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_17": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_17_name": item_name}})
                if a[1] == 18:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_18": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_18_name": item_name}})
                if a[1] == 19:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_19": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_19_name": item_name}})
                if a[1] == 20:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_20": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_20_name": item_name}})
                if a[1] == 21:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_21": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_21_name": item_name}})
                if a[1] == 22:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_22": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_22_name": item_name}})
                if a[1] == 23:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_23": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_23_name": item_name}})
                if a[1] == 24:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_24": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_24_name": item_name}})
                if a[1] == 25:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_25": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_25_name": item_name}})
                if a[1] == 26:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_26": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_26_name": item_name}})
                if a[1] == 27:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_27": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_27_name": item_name}})
                if a[1] == 28:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_28": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_28_name": item_name}})
                if a[1] == 29:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_29": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_29_name": item_name}})
                if a[1] == 30:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_30": inv_slot}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_30_name": item_name}})
                await message.answer(f'Игрок {main[0]} отправил предмет {item_name} в сундук №{a[1]}.')
        else:
            await message.answer(f"Все сундуки переполнены!")


# @dp.message_handler(commands='Взять_из_сундука')
async def chest_2(message: types.Message):
    global inv_slot, item_name, party
    uid = message.from_user.id
    msg = int(message.get_args())
    cur = mongodb.findUserCurrencyByID(uid)
    print("вуф")
    if cur[9] == 0:
        await message.answer(f"У вас нет дома!")
    else:
        for party in owner.find({"num": cur[9]}):
            print("Inv finder done")
        print("вуф")
        if msg == 1:
            inv_slot = party["chest_1"]
            item_name = party["chest_1_name"]
        if msg == 2:
            inv_slot = party["chest_2"]
            item_name = party["chest_2_name"]
        if msg == 3:
            inv_slot = party["chest_3"]
            item_name = party["chest_3_name"]
        if msg == 4:
            inv_slot = party["chest_4"]
            item_name = party["chest_4_name"]
        if msg == 5:
            inv_slot = party["chest_5"]
            item_name = party["chest_5_name"]
        if msg == 6:
            inv_slot = party["chest_6"]
            item_name = party["chest_6_name"]
        if msg == 7:
            inv_slot = party["chest_7"]
            item_name = party["chest_7_name"]
        if msg == 8:
            inv_slot = party["chest_8"]
            item_name = party["chest_8_name"]
        if msg == 9:
            inv_slot = party["chest_9"]
            item_name = party["chest_9_name"]
        if msg == 10:
            inv_slot = party["chest_10"]
            item_name = party["chest_10_name"]
        if msg == 11:
            inv_slot = party["chest_11"]
            item_name = party["chest_11_name"]
        if msg == 12:
            inv_slot = party["chest_12"]
            item_name = party["chest_12_name"]
        if msg == 13:
            inv_slot = party["chest_13"]
            item_name = party["chest_13_name"]
        if msg == 14:
            inv_slot = party["chest_14"]
            item_name = party["chest_14_name"]
        if msg == 15:
            inv_slot = party["chest_15"]
            item_name = party["chest_15_name"]
        if msg == 16:
            inv_slot = party["chest_16"]
            item_name = party["chest_16_name"]
        if msg == 17:
            inv_slot = party["chest_17"]
            item_name = party["chest_17_name"]
        if msg == 18:
            inv_slot = party["chest_18"]
            item_name = party["chest_18_name"]
        if msg == 19:
            inv_slot = party["chest_19"]
            item_name = party["chest_19_name"]
        if msg == 20:
            inv_slot = party["chest_20"]
            item_name = party["chest_20_name"]
        if msg == 21:
            inv_slot = party["chest_21"]
            item_name = party["chest_21_name"]
        if msg == 22:
            inv_slot = party["chest_22"]
            item_name = party["chest_22_name"]
        if msg == 23:
            inv_slot = party["chest_23"]
            item_name = party["chest_23_name"]
        if msg == 24:
            inv_slot = party["chest_24"]
            item_name = party["chest_24_name"]
        if msg == 25:
            inv_slot = party["chest_25"]
            item_name = party["chest_25_name"]
        if msg == 26:
            inv_slot = party["chest_26"]
            item_name = party["chest_26_name"]
        if msg == 27:
            inv_slot = party["chest_27"]
            item_name = party["chest_27_name"]
        if msg == 28:
            inv_slot = party["chest_28"]
            item_name = party["chest_28_name"]
        if msg == 29:
            inv_slot = party["chest_29"]
            item_name = party["chest_29_name"]
        if msg == 30:
            inv_slot = party["chest_30"]
            item_name = party["chest_30_name"]
        if inv_slot == 0:
            await message.answer(f'Сундук №{msg} пуст!')
        else:
            print("вуф1")
            for i in inventory.find({"number": inv_slot}):
                print("Cult finder done")
            host_uid = uid
            sum = inv_slot
            host = pay.Pay.host(host_uid, sum, item_name)
            if host is True:
                if msg == 1:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_1": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_1_name": 0}})
                if msg == 2:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_2": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_2_name": 0}})
                if msg == 3:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_3": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_3_name": 0}})
                if msg == 4:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_4": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_4_name": 0}})
                if msg == 5:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_5": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_5_name": 0}})
                if msg == 6:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_6": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_6_name": 0}})
                if msg == 7:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_7": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_7_name": 0}})
                if msg == 8:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_8": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_8_name": 0}})
                if msg == 9:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_9": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_9_name": 0}})
                if msg == 10:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_10": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_10_name": 0}})
                if msg == 11:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_11": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_11_name": 0}})
                if msg == 12:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_12": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_12_name": 0}})
                if msg == 13:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_13": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_13_name": 0}})
                if msg == 14:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_14": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_14_name": 0}})
                if msg == 15:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_15": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_15_name": 0}})
                if msg == 16:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_16": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_16_name": 0}})
                if msg == 17:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_17": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_17_name": 0}})
                if msg == 18:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_18": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_18_name": 0}})
                if msg == 19:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_19": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_19_name": 0}})
                if msg == 20:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_20": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_20_name": 0}})
                if msg == 21:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_21": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_21_name": 0}})
                if msg == 22:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_22": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_22_name": 0}})
                if msg == 23:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_23": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_23_name": 0}})
                if msg == 24:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_24": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_24_name": 0}})
                if msg == 25:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_25": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_25_name": 0}})
                if msg == 26:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_26": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_26_name": 0}})
                if msg == 27:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_27": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_27_name": 0}})
                if msg == 28:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_28": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_28_name": 0}})
                if msg == 29:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_29": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_29_name": 0}})
                if msg == 30:
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_130": 0}})
                    owner.update_one({"num": cur[9]}, {"$set": {"chest_30_name": 0}})
                await message.answer(f'Вы нашли в сундуке №{msg} предмет "{i["name"]}".')
            elif host is False:
                await message.answer(f"Ваш рюкзак переполнен!")


# @dp.message_handler(commands='Улучшить_дом')
async def upgrade(message: types.Message):
    uid = message.from_user.id
    msg = str(message.get_args())
    cur = mongodb.findUserCurrencyByID(uid)
    if cur[9] == 0:
        await message.answer(f"У вас нет дома!")
    else:
        if msg == "уровень" or msg == "Уровень" or msg == "лвл" or msg == "lvl":
            money = cur[1]
            materials = cur[0]
            for party in owner.find({"num": cur[9]}):
                print("Inv finder done")
            if party["lvl"] == 1:
                cost = 500
                cost1 = 100
            elif party["lvl"] == 2:
                cost = 1000
                cost1 = 200
            elif party["lvl"] == 3:
                cost = 2000
                cost1 = 300
            elif party["lvl"] == 4:
                cost = 4000
                cost1 = 600
            elif party["lvl"] == 5:
                cost = 5000
                cost1 = 700
            elif party["lvl"] == 6:
                cost = 10000
                cost1 = 1000
            elif party["lvl"] == 7:
                cost = 15000
                cost1 = 2000
            elif party["lvl"] == 8:
                cost = 20000
                cost1 = 3000
            elif party["lvl"] == 9:
                cost = 25000
                cost1 = 5000
            if party["lvl"] == 10:
                await message.answer(f"У вас макимальный уровень дома!")
            else:
                if cost > money or cost1 > materials:
                    await message.answer(
                        f"У вас не хватает средств (для прокачки дома используется золото и материалы)")
                else:
                    players.update_one({"_id": uid}, {"$set": {"gold": money - cost}})
                    players.update_one({"_id": uid}, {"$set": {"material": materials - cost1}})
                    owner.update_one({"num": cur[9]}, {"$set": {"lvl": party["lvl"] + 1}})
                    await message.answer(
                        f'Вы повысили уровень "{party["name"]}"! \n Было потрачено {cost} монет и {cost1} материалов.')
        elif msg == "верстак" or msg == "Верстак" or msg == "Кузница" or msg == "кузница":
            money = cur[1]
            for party in owner.find({"num": cur[9]}):
                print("Inv finder done")
            if party["workbench_lvl"] == 0:
                cost = 1000
                lvl = 2
            elif party["workbench_lvl"] == 1:
                cost = 5000
                lvl = 5
            elif party["workbench_lvl"] == 2:
                cost = 10000
                lvl = 10
            else:
                await message.answer(f"Вы достигли максимального уровня кузницы!")
            if party["lvl"] >= lvl:
                if cost > money:
                    await message.answer(
                        f"У вас не хватает средств (для прокачки кузницы используется золото)")
                else:
                    players.update_one({"_id": uid}, {"$set": {"gold": money - cost}})
                    owner.update_one({"num": cur[9]}, {"$set": {"workbench_lvl": party["workbench_lvl"] + 1}})
                    await message.answer(
                        f'Вы повысили уровень кузницы ! \n Было потрачено {cost} монет.')
            else:
                await message.answer(f"Для дальнейшего повышения уровня кузницы тербуется {lvl} уровень дома!")
        elif msg == "Лаборатория" or msg == "лаборатория" or msg == "алхимия" or msg == "Алхимия":
            money = cur[1]
            for party in owner.find({"num": cur[9]}):
                print("Inv finder done")
            if party["cooking_rack"] == 0:
                cost = 1000
                lvl = 2
            elif party["cooking_rack"] == 1:
                cost = 5000
                lvl = 5
            elif party["cooking_rack"] == 2:
                cost = 10000
                lvl = 10
            else:
                await message.answer(f"Вы достигли максимального уровня лаборатории!")
            if party["lvl"] >= lvl:
                if cost > money:
                    await message.answer(
                        f"У вас не хватает средств (для прокачки лаборатории используется золото)")
                else:
                    players.update_one({"_id": uid}, {"$set": {"gold": money - cost}})
                    owner.update_one({"num": cur[9]}, {"$set": {"cooking_rack": party["cooking_rack"] + 1}})
                    await message.answer(
                        f'Вы повысили уровень лаборатории ! \n Было потрачено {cost} монет.')
            else:
                await message.answer(f"Для дальнейшего повышения уровня лаборатории тербуется {lvl} уровень дома!")




def register_handlers_owner(dp: Dispatcher):
    dp.register_message_handler(prof, commands='Профиль_дома')
    dp.register_message_handler(invite_home, commands='Пригласить_в_дом')
    dp.register_message_handler(accept_home, commands='+')
    dp.register_message_handler(no, commands='-')
    dp.register_message_handler(leave, commands='Покинуть_дом')
    dp.register_message_handler(swap, commands='Передать_дом')
    dp.register_message_handler(kick, commands='Прогнать')
    dp.register_message_handler(chest_1, commands='Отправить_в_сундук')
    dp.register_message_handler(chest_2, commands='Взять_из_сундука')
    dp.register_message_handler(upgrade, commands='Улучшить_дом')
