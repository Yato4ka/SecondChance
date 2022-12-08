from aiogram import Dispatcher, types
from pymongo import MongoClient
from mongodb import Finder as mongodb
from random import randint
import asyncio

cluster = MongoClient("mongodb+srv://Yato:1212@scrp.ym4yecy.mongodb.net/?retryWrites=true&w=majority")
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


class Alchemy:
    def search_grass(uid, random):
        cur = mongodb.findUserСurrencyByID(uid)
        have_grass = int(cur[3])
        new_grass = have_grass + random
        players.update_one({"_id": uid}, {"$set": {"grass": new_grass}})

    def give_pill(uid, n):
        inv = mongodb.findUserInventoryByID(uid)
        if inv[0] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot1": n}})
            return True
        elif inv[1] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot2": n}})
            return True
        elif inv[2] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot3": n}})
            return True
        elif inv[3] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot4": n}})
            return True
        elif inv[4] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot5": n}})
            return True
        elif inv[5] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot6": n}})
            return True
        elif inv[6] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot7": n}})
            return True
        elif inv[7] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot8": n}})
            return True
        elif inv[8] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot9": n}})
            return True
        elif inv[9] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot10": n}})
            return True
        else:
            return False


class Kraft:
    def search_iron(uid, random):
        cur = mongodb.findUserСurrencyByID(uid)
        have_iron = int(cur[6])
        new_iron = have_iron + random
        players.update_one({"_id": uid}, {"$set": {"iron": new_iron}})

    def give_weapon(uid, n, name_ow):
        inv = mongodb.findUserInventoryByID(uid)
        if inv[0] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot1": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot1": name_ow}})
            return True
        elif inv[1] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot2": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot2": name_ow}})
            return True
        elif inv[2] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot3": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot3": name_ow}})
            return True
        elif inv[3] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot4": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot4": name_ow}})
            return True
        elif inv[4] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot5": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot5": name_ow}})
            return True
        elif inv[5] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot6": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot6": name_ow}})
            return True
        elif inv[6] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot7": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot7": name_ow}})
            return True
        elif inv[7] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot8": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot8": name_ow}})
            return True
        elif inv[8] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot9": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot9": name_ow}})
            return True
        elif inv[9] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot10": n}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot10": name_ow}})
            return True
        else:
            return False


class Use:

    def check_msg(uid, msg):
        inv = mongodb.findUserInventoryByID(uid)
        if msg == 1:
            if inv[0] == 0:
                return [False]
            else:
                return [True, inv[0]]
        if msg == 2:
            if inv[1] == 0:
                return [False]
            else:
                return [True, inv[1]]
        if msg == 3:
            if inv[2] == 0:
                return [False]
            else:
                return [True, inv[2]]
        if msg == 4:
            if inv[3] == 0:
                return [False]
            else:
                return[True, inv[3]]
        if msg == 5:
            if inv[4] == 0:
                return [False]
            else:
                return [True, inv[4]]
        if msg == 6:
            if inv[5] == 0:
                return [False]
            else:
                return [True, inv[5]]
        if msg == 7:
            if inv[6] == 0:
                return [False]
            else:
                return [True, inv[6]]
        if msg == 8:
            if inv[7] == 0:
                return [False]
            else:
                return [True, inv[7]]
        if msg == 9:
            if inv[8] == 0:
                return [False]
            else:
                return [True, inv[8]]
        if msg == 10:
            if inv[9] == 0:
                return [False]
            else:
                return [True, inv[9]]

    def pill(uid, num):
        for check in inventory.find({"number": num}):
            print("Cult finder done")
            bust = check["energy_bust"]
            main = mongodb.findUserMainByID(uid)
            have_energy = int(main[2])
            new_energy = have_energy + bust
            players.update_one({"_id": uid}, {"$set": {"energy": new_energy}})

    def weapon(uid, hand, num, msg):
        invn = mongodb.findUserInventoryNameByID(uid)
        if msg == "1":
            r = invn[0]
            players.update_one({"_id": uid}, {"$set": {"nw_slot1": "Отсутствует"}})
        elif msg == "2":
            r = invn[1]
            players.update_one({"_id": uid}, {"$set": {"nw_slot2": "Отсутствует"}})
        elif msg == "3":
            r = invn[2]
            players.update_one({"_id": uid}, {"$set": {"nw_slot3": "Отсутствует"}})
        elif msg == "4":
            r = invn[3]
            players.update_one({"_id": uid}, {"$set": {"nw_slot4": "Отсутствует"}})
        elif msg == "5":
            r = invn[4]
            players.update_one({"_id": uid}, {"$set": {"nw_slot5": "Отсутствует"}})
        elif msg == "6":
            r = invn[5]
            players.update_one({"_id": uid}, {"$set": {"nw_slot6": "Отсутствует"}})
        elif msg == "7":
            r = invn[6]
            players.update_one({"_id": uid}, {"$set": {"nw_slot7": "Отсутствует"}})
        elif msg == "8":
            r = invn[7]
            players.update_one({"_id": uid}, {"$set": {"nw_slot8": "Отсутствует"}})
        elif msg == "9":
            r = invn[8]
            players.update_one({"_id": uid}, {"$set": {"nw_slot9": "Отсутствует"}})
        elif msg == "10":
            r = invn[9]
            players.update_one({"_id": uid}, {"$set": {"nw_slot10": "Отсутствует"}})

        if hand == "правую_руку":
            players.update_one({"_id": uid}, {"$set": {"right_hand": num}})
            players.update_one({"_id": uid}, {"$set": {"nw_right_hand": r}})
        elif hand == "левую_руку":
            players.update_one({"_id": uid}, {"$set": {"left_hand": num}})
            players.update_one({"_id": uid}, {"$set": {"nw_left_hand": r}})

    def check_hand(uid, hand):
        equip = mongodb.findUserEquipmentByID(uid)
        if hand == "правую_руку":
            r_hand = equip[0]
            if r_hand == 0:
                return True
            else:
                return False
        elif hand == "левую_руку":
            l_hand = equip[1]
            if l_hand == 0:
                return True
            else:
                return False

    def host2(host_uid, sum, slot):
        uid = host_uid
        inv = mongodb.findUserInventoryByID(uid)
        invn = mongodb.findUserInventoryNameByID(uid)
        if slot == 1:
            if inv[0] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
                return True
            elif inv[1] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
                return True
            elif inv[2] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
                return True
            elif inv[3] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
                return True
            elif inv[4] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
                return True
            elif inv[5] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
                return True
            elif inv[6] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
                return True
            elif inv[7] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
                return True
            elif inv[8] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
                return True
            elif inv[9] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory1": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
                return True
            else:
                return False
        if slot == 2:
            if inv[0] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
                return True
            elif inv[1] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
                return True
            elif inv[2] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
                return True
            elif inv[3] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
                return True
            elif inv[4] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
                return True
            elif inv[5] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
                return True
            elif inv[6] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
                return True
            elif inv[7] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
                return True
            elif inv[8] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
                return True
            elif inv[9] == 0:
                players.update_one({"_id": uid}, {"$set": {"accessory2": 0}})
                players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
                return True
            else:
                return False

    def host(host_uid, sum, hand):
        uid = host_uid
        inv = mongodb.findUserInventoryByID(uid)
        invn = mongodb.findUserInventoryNameByID(uid)
        if hand == "в_левой_руке":
            item = invn[11]
            if inv[0] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot1": item}})
                players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[1] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot2": item}})
                players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[2] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot3": item}})
                players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[3] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot4": item}})
                players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[4] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot5": item}})
                players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[5] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot6": item}})
                players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[6] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot7": item}})
                players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[7] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot8": item}})
                players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[8] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot9": item}})
                players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            elif inv[9] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot10": item}})
                players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_left_hand": "Пусто"}})
                return True
            else:
                return False
        elif hand == "в_правой_руке":
            item = invn[10]
            if inv[0] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot1": item}})
                players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[1] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot2": item}})
                players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[2] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot3": item}})
                players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[3] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot4": item}})
                players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[4] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot5": item}})
                players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[5] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot6": item}})
                players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[6] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot7": item}})
                players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[7] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot8": item}})
                players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[8] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot9": item}})
                players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})
                return True
            elif inv[9] == 0:
                players.update_one({"_id": uid}, {"$set": {"nw_slot10": item}})
                players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
                players.update_one({"_id": uid}, {"$set": {"left_hand": 0}})
                players.update_one({"_id": uid}, {"$set": {"nw_right_hand": "Пусто"}})



# @dp.message_handler(commands='Искать_траву')
async def searchgrass(message: types.Message):
    uid = message.from_user.id
    rp = mongodb.findUserRpByID(uid)
    await message.delete()
    check = int(rp[2])
    if check >= 1:
        random = randint(1, 5)
        Alchemy.search_grass(uid, random)
        await message.answer("Поиск травы завершен")
        await message.answer(f"Было найдено {random} Бэсу!")
    else:
        await message.answer("Недостаточный уровень алхимии!")


# @dp.message_handler(commands='Искать_руду')
async def searchiron(message: types.Message):
    uid = message.from_user.id
    rp = mongodb.findUserRpByID(uid)
    await message.delete()
    check = int(rp[1])
    if check >= 1:
        random = randint(1, 5)
        Kraft.search_iron(uid, random)
        await message.answer("Поиск руды завершен")
        await message.answer(f"Было найдено {random} базовой магической руды!")
    else:
        await message.answer("Недостаточный уровень крафта!")


# @dp.message_handler(commands='Создать_пилюлю_опыта')
async def pill(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    rp = mongodb.findUserRpByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    await message.delete()
    check = int(rp[2])
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = str(getter[0])
    name = str(getter[1])
    who = main[0]
    if what == "Малая" or what == "малая":
        n = 1
        lvl = 3
        if rp[2] >= 10:
            cost = 5
        else:
            cost = 10
    if what == "Средняя" or what == "средняя":
        n = 2
        lvl = 6
        if rp[2] >= 10:
            cost = 20
        else:
            cost = 40
    if what == "Большая" or what == "большая":
        n = 3
        lvl = 9
        if rp[2] >= 10:
            cost = 60
        else:
            cost = 120
    if check >= lvl:
        check_grass = cur[3]
        if check_grass >= cost:
            have_grass = int(cur[3])
            uid = mongodb.findUserIDByName(name)
            uid = uid[0]
            check2 = Alchemy.give_pill(uid, n)
            if check2 is True:
                await message.answer(f'Игроку {name} было выдан предмет "{what} пилюля опыта" \n'
                                     f'Алхимик - {who}!')
                new_grass = have_grass - cost
                players.update_one({"_id": uid}, {"$set": {"grass": new_grass}})
            else:
                await message.answer(f"Рюкзак игрока {name} переполнен!")
        else:
            await message.answer("Недостаточно травы Бэсу!")
    else:
        await message.answer("Недостаточный уровень алхимии!")


# @dp.message_handler(commands='Скрафтить_оружие')
async def weapon(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    rp = mongodb.findUserRpByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    await message.delete()
    check = int(rp[1])
    msg = message.get_args()
    getter = msg.replace(' для ', ' , ').split(' , ')
    name_ow = str(getter[1])
    type = str(getter[0])
    name = str(getter[2])
    who = main[0]
    if type == "E" or type == "e":
        n = 4
        lvl = 2
        if rp[1] >= 10:
            cost = 5
        else:
            cost = 10
    if type == "E+" or type == "e+":
        n = 10
        lvl = 4
        if rp[1] >= 10:
            cost = 10
        else:
            cost = 20
    if type == "D" or type == "d":
        n = 5
        lvl = 6
        if rp[1] >= 10:
            cost = 20
        else:
            cost = 40
    if type == "D+" or type == "d+":
        n = 16
        lvl = 8
        if rp[1] >= 10:
            cost = 25
        else:
            cost = 50
    if type == "C" or type == "c":
        n = 17
        lvl = 10
        if rp[1] >= 10:
            cost = 40
        else:
            cost = 80
    if type == "C+" or type == "c+":
        n = 18
        lvl = 12
        if rp[1] >= 10:
            cost = 50
        else:
            cost = 100
    if check >= lvl:
        check_iron = cur[6]
        if check_iron >= cost:
            have_iron = int(cur[6])
            uid = mongodb.findUserIDByName(name)
            uid = uid[0]
            check2 = Kraft.give_weapon(uid, n, name_ow)
            if check2 is True:
                new_iron = have_iron - cost
                players.update_one({"_id": uid}, {"$set": {"iron": new_iron}})
                await message.answer(f'Игроку {name} было выдан предмет "оружие {type} ранга" - "{name_ow}"! \n'
                                     f'Кузнец - {who}')
            else:
                await message.answer(f"Рюкзак игрока {name} переполнен!")
        else:
            await message.answer("Недостаточно руды !")
    else:
        await message.answer("Недостаточный уровень крафта!")


# @dp.message_handler(commands='Починить_оружие_игрока')
async def weapon_repair(message: types.Message):
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    rp = mongodb.findUserRpByID(uid)
    cur = mongodb.findUserСurrencyByID(uid)
    check = int(rp[1])
    msg = message.get_args()
    getter = msg.replace(' в ', ' , ').split(' , ')
    hand = str(getter[1])
    name = str(getter[0])
    who = main[0]
    for check_host in players.find({"name": name}):
        print("Cult finder done")
    if hand == "правой_руке":
        number = check_host["right_hand"]
        for type in inventory.find({"number": number}):
            print("Cult finder done")
        if type > 0:
            have = 1
            if type == "Оружие F ранга":
                n = 4
                cost = 1
                can = 1
                lvl = 1
            if type == "Оружие F+ ранга":
                n = 10
                cost = 2
                can = 1
                lvl = 1
            if type == "Оружие E ранга":
                n = 4
                cost = 5
                can = 1
                lvl = 2
            if type == "Оружие E+ ранга+":
                n = 10
                cost = 10
                can = 1
                lvl = 3
            if type == "Оружие D ранга":
                n = 5
                cost = 15
                can = 1
                lvl = 4
            if type == "Оружие D+ ранга":
                n = 16
                cost = 30
                can = 1
                lvl = 5
            if type == "Оружие C ранга":
                n = 17
                cost = 35
                can = 1
                lvl = 6
            if type == "Оружие C+ ранга":
                n = 18
                cost = 75
                can = 1
                lvl = 7
            if type == "Оружие B ранга":
                n = 6
                cost = 100
                can = 1
                lvl = 8
            if type == "Оружие B+ ранга":
                n = 19
                cost = 150
                can = 1
                lvl = 9
            if type == "Оружие A ранга":
                n = 12
                cost = 200
                can = 1
                lvl = 10
            if type == "Оружие A+ ранга":
                n = 20
                cost = 300
                can = 1
                lvl = 12
            if type == "Оружие S ранга":
                can = 0
            if type == "Оружие S+ ранга":
                can = 0
        else:
            have = 0
    if hand == "левой_руке":
        number = check_host["left_hand"]
        for type in inventory.find({"number": number}):
            print("Cult finder done")
        if type > 0:
            have = 1
            if type == "Оружие F ранга":
                n = 4
                cost = 1
                can = 1
                lvl = 1
            if type == "Оружие F+ ранга":
                n = 10
                cost = 2
                can = 1
                lvl = 1
            if type == "Оружие E ранга":
                n = 4
                cost = 5
                can = 1
                lvl = 2
            if type == "Оружие E+ ранга+":
                n = 10
                cost = 10
                can = 1
                lvl = 3
            if type == "Оружие D ранга":
                n = 5
                cost = 15
                can = 1
                lvl = 4
            if type == "Оружие D+ ранга":
                n = 16
                cost = 30
                can = 1
                lvl = 5
            if type == "Оружие C ранга":
                n = 17
                cost = 35
                can = 1
                lvl = 6
            if type == "Оружие C+ ранга":
                n = 18
                cost = 75
                can = 1
                lvl = 7
            if type == "Оружие B ранга":
                n = 6
                cost = 100
                can = 1
                lvl = 8
            if type == "Оружие B+ ранга":
                n = 19
                cost = 150
                can = 1
                lvl = 9
            if type == "Оружие A ранга":
                n = 12
                cost = 200
                can = 1
                lvl = 10
            if type == "Оружие A+ ранга":
                n = 20
                cost = 300
                can = 1
                lvl = 12
            if type == "Оружие S ранга":
                can = 0
            if type == "Оружие S+ ранга":
                can = 0
        else:
            have = 0
    if have == 0:
        await message.answer(f"У игрока {name} фнет оружия в этой руке!")
    if have == 1:
        await message.answer(f"Вы взяли оружие в руки...")
        if can == 0:
            await message.answer(f"Вы поняли, что это легендарное оружие и вы не способны его починить")
        if can == 1:
            await message.answer(f"Вы рассмотрели оружие и поняли, что починить его в теории возможно")
            if check >= lvl:
                check_iron = cur[6]
                if check_iron >= cost:
                    new_iron = check_iron - cost
                    players.update_one({"_id": uid}, {"$set": {"iron": new_iron}})
                    await message.answer(f'Оружие игрока {name} было починено и он снова может им пользоваться! \n'
                                             f'Кузнец - {who}')
                else:
                    await message.answer("Но у вас недостаточно руды !")
            else:
                await message.answer("Но у вас недостаточный уровень крафта!")


# @dp.message_handler(commands='Использовать_пилюлю')
async def usepill(message: types.Message):
    uid = message.from_user.id
    inv = mongodb.findUserInventoryByID(uid)
    msg = message.get_args()
    if msg == "1":
        if inv[0] == 0:
            await message.answer('Слот №1 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[0]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[0]
                players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №1 в рюкзаке не является пилюлей опыта!')
    if msg == "2":
        if inv[1] == 0:
            await message.answer('Слот №2 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[1]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[1]
                players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №2 в рюкзаке не является пилюлей опыта!')
    if msg == "3":
        if inv[2] == 0:
            await message.answer('Слот №2 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[2]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[2]
                players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №2 в рюкзаке не является пилюлей опыта!')
    if msg == "4":
        if inv[3] == 0:
            await message.answer('Слот №4 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[3]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[3]
                players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №4 в рюкзаке не является пилюлей опыта!')
    if msg == "5":
        if inv[4] == 0:
            await message.answer('Слот №5 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[4]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[4]
                players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №5 в рюкзаке не является пилюлей опыта!')
    if msg == "6":
        if inv[5] == 0:
            await message.answer('Слот №6 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[5]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[5]
                players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №6 в рюкзаке не является пилюлей опыта!')
    if msg == "7":
        if inv[6] == 0:
            await message.answer('Слот №7 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[6]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[6]
                players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №7 в рюкзаке не является пилюлей опыта!')
    if msg == "8":
        if inv[7] == 0:
            await message.answer('Слот №8 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[7]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[7]
                players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №8 в рюкзаке не является пилюлей опыта!')
    if msg == "9":
        if inv[8] == 0:
            await message.answer('Слот №9 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[8]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[8]
                players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №9 в рюкзаке не является пилюлей опыта!')
    if msg == "10":
        if inv[9] == 0:
            await message.answer('Слот №10 в рюкзаке пуст!')
        else:
            for check in inventory.find({"number": inv[9]}):
                print("Cult finder done")
            if check["Type"] == "пилюля":
                num = inv[9]
                players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
                await message.answer(f"Вы использовали предмет '{check['name']}' !")
                Use.pill(uid, num)
            else:
                await message.answer('Слот №10 в рюкзаке не является пилюлей опыта!')


# @dp.message_handler(commands='Использовать_оружие')
async def useweapon(message: types.Message):
    uid = message.from_user.id
    inv = mongodb.findUserInventoryByID(uid)
    msg = message.get_args()
    getter = msg.replace(' в ', ',').split(',')
    msg = str(getter[0])
    hand = str(getter[1])
    if msg == "1":
        if inv[0] == 0:
            await message.answer('Слот №1 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[0]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №1 в рюкзаке не является оружием!')
    if msg == "2":
        if inv[1] == 0:
            await message.answer('Слот №2 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[1]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №2 в рюкзаке не является оружием!')
    if msg == "3":
        if inv[2] == 0:
            await message.answer('Слот №3 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[2]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №3 в рюкзаке не является оружием!')
    if msg == "4":
        if inv[3] == 0:
            await message.answer('Слот №4 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[3]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №4 в рюкзаке не является оружием!')
    if msg == "5":
        if inv[4] == 0:
            await message.answer('Слот №5 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[4]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №5 в рюкзаке не является оружием!')
    if msg == "6":
        if inv[5] == 0:
            await message.answer('Слот №6 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[5]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №6 в рюкзаке не является оружием!')
    if msg == "7":
        if inv[6] == 0:
            await message.answer('Слот №7 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[6]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №7 в рюкзаке не является оружием!')
    if msg == "8":
        if inv[7] == 0:
            await message.answer('Слот №8 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[7]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №8 в рюкзаке не является оружием!')
    if msg == "9":
        if inv[8] == 0:
            await message.answer('Слот №9 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[8]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №9 в рюкзаке не является оружием!')
    if msg == "10":
        if inv[9] == 0:
            await message.answer('Слот №10 в рюкзаке пуст!')
        else:
            a = Use.check_hand(uid, hand)
            if a is False:
                await message.answer("В этой руке уже находится предмет!")
            if a is True:
                for check in inventory.find({"number": inv[9]}):
                    print("Cult finder done")
                if check["Type"] == "оружие":
                    players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
                    num = check['number']
                    Use.weapon(uid, hand, num, msg)
                    await message.answer(f"Предмет '{check['name']}' теперь в руке!")
                else:
                    await message.answer('Слот №10 в рюкзаке не является оружием!')


# @dp.message_handler(commands='Выкинуть_предмет_из_рюкзака')
async def drop(message: types.Message):
    uid = message.from_user.id
    invn = mongodb.findUserInventoryNameByID(uid)
    place = mongodb.findUserPlaceByID(uid)
    what = int(message.get_args())
    for loc in locations_and_clans.find({"num": place[4]}):
        print("Inv finder done")
    if what == 1:
        name = invn[0]
        players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot1": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 2:
        name = invn[1]
        players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot2": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 3:
        name = invn[2]
        players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot3": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 4:
        name = invn[3]
        players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot4": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 5:
        name = invn[4]
        players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot5": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 6:
        name = invn[5]
        players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot6": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 7:
        name = invn[6]
        players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot7": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 8:
        name = invn[7]
        players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot8": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 9:
        name = invn[8]
        players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot9": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')
    if what == 10:
        name = invn[9]
        players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
        players.update_one({"_id": uid}, {"$set": {"nw_slot10": "Пусто"}})
        await message.answer(f'Вы выкинули предмет "{name}" на локации: {loc["name"]} ')


# @dp.message_handler(commands='Активировать_рунный_камень')
async def userune(message: types.Message):
    uid = message.from_user.id
    inv = mongodb.findUserInventoryByID(uid)
    msg = message.get_args()
    getter = msg.replace(' в слоте ', ',').split(',')
    msg = int(getter[0])
    slot = int(getter[1])
    equip = mongodb.findUserEquipmentByID(uid)
    checker = Use.check_msg(uid, msg)
    if checker[0] is False:
        await message.answer(f'Слот f{msg} в рюкзаке пуст!')
    else:
        for check in inventory.find({"number": checker[1]}):
            print("Cult finder done")
        if check["Type"] == "руна":
            numb = check["number"]
            numn = check['name']
            if 0 < msg <= 10:
                if slot == 1:
                    if equip[6] >= 1:
                        await message.answer(f"Тут уже находится рунный камень!")
                    else:
                        players.update_one({"_id": uid}, {"$set": {"accessory1": numb}})
                        await message.answer(f"Рунный камень '{numn}' вставлен в слот №{slot}!")
                        if msg == 1:
                            players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
                        elif msg == 2:
                            players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
                        elif msg == 3:
                            players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
                        elif msg == 4:
                            players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
                        elif msg == 5:
                            players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
                        elif msg == 6:
                            players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
                        elif msg == 7:
                            players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
                        elif msg == 8:
                            players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
                        elif msg == 9:
                            players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
                        elif msg == 10:
                            players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
                elif slot == 2:
                    if equip[7] >= 1:
                        await message.answer(f"Тут уже находится рунный камень!")
                    else:
                        players.update_one({"_id": uid}, {"$set": {"accessory2": numb}})
                        await message.answer(f"Рунный камень '{numn}' вставлен в слот №{slot}!")
                        if msg == 1:
                            players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
                        elif msg == 2:
                            players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
                        elif msg == 3:
                            players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
                        elif msg == 4:
                            players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
                        elif msg == 5:
                            players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
                        elif msg == 6:
                            players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
                        elif msg == 7:
                            players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
                        elif msg == 8:
                            players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
                        elif msg == 9:
                            players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
                        elif msg == 10:
                            players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
                else:
                    await message.answer(
                        f"Слот №{slot} не существует! \n Пример команды: \n /Активировать_рунный_камень (слот в инвентаре от 1 до 10) в слот (слот для рун от 1 до 2)")
            else:
                await message.answer(f"Не существует слота в инвентаре номер №{msg}")
        else:
            await message.answer(f"Предмет №{msg} в инвентаре не является рунным камнем.")


# @dp.message_handler(commands='Деактивировать_рунный_камень')
async def unuserune(message: types.Message):
    uid = message.from_user.id
    host_uid = uid
    slot = int(message.get_args())
    equip = mongodb.findUserEquipmentByID(uid)
    if slot == 1:
        if equip[6] >= 1:
            sum = equip[6]
            host = Use.host2(host_uid, sum, slot)
            if host is True:
                await message.answer(f'Рунный камень был возращен в рюкзак.')
            else:
                await message.answer('Рюкзак переполнен!')
        else:
            await message.answer(f'У вас нет активированного рунного камня №1')
    if slot == 2:
        if equip[7] >= 1:
            sum = equip[7]
            host = Use.host2(host_uid, sum, slot)
            if host is True:
                await message.answer(f'Рунный камень был возращен в рюкзак.')
            else:
                await message.answer('Рюкзак переполнен!')
        else:
            await message.answer(f'У вас нет активированного рунного камня №2')
    else:
        await message.answer(f'Ошибка значений, пример команды : \n /Деактивировать_рунный_камень 2')


# @dp.message_handler(commands='Вернуть_в_рюкзак_оружие')
async def pay3(message: types.Message):
    uid = message.from_user.id
    host_uid = uid
    hand = message.get_args()
    equip = mongodb.findUserEquipmentByID(uid)
    if hand == "в_левой_руке":
        if equip[1] >= 1:
            sum = equip[1]
            host = Use.host(host_uid, sum, hand)
            if host is True:
                await message.answer(f'Оружие было возращено в рюкзак.')
            else:
                await message.answer('Рюкзак переполнен!')
        else:
            await message.answer(f'У вас нет оружия в левой руке')
    elif hand == "в_правой_руке":
        if equip[0] >= 1:
            sum = equip[0]
            host = Use.host(host_uid, sum, hand)
            if host is True:
                await message.answer(f'Оружие было возращено в рюкзак.')
            else:
                await message.answer('Рюкзак переполнен!')
        else:
            await message.answer(f'У вас нет оружия в правой руке')
    else:
        await message.answer(f'Ошибка значений, пример команды : \n /Вернуть_в_рюкзак_оружие в_левой_руке')


def register_handlers_craft(dp: Dispatcher):
    dp.register_message_handler(searchgrass, commands='Искать_траву')
    dp.register_message_handler(searchiron, commands='Искать_руду')

    dp.register_message_handler(pill, commands='Создать_пилюлю_опыта') # Какая для кого
    dp.register_message_handler(weapon, commands='Скрафтить_оружие') # ранг , имя для кого
    dp.register_message_handler(weapon_repair, commands='Починить_оружие_игрока') # имя в правой/левой_руке

    dp.register_message_handler(usepill, commands="Использовать_пилюлю")
    dp.register_message_handler(useweapon, commands="Использовать_оружие") #/Использовать_оружие 1 в левую_руку
    dp.register_message_handler(userune, commands='Активировать_рунный_камень')

    dp.register_message_handler(unuserune, commands='Деактивировать_рунный_камень')
    dp.register_message_handler(pay3, commands='Вернуть_в_рюкзак_оружие')  #/Вернуть_в_рюкзак_оружие в_левой_руке

    dp.register_message_handler(drop, commands='Выкинуть_предмет_из_рюкзака')  # /Выкинуть_предмет_из_рюкзака


