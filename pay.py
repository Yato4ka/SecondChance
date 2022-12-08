import asyncio

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

    def host(host_uid, sum, item_name):
        n = item_name
        uid = host_uid
        inv = mongodb.findUserInventoryByID(uid)
        if inv[0] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot1": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot1": n}})
            return True
        elif inv[1] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot2": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot2": n}})
            return True
        elif inv[2] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot3": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot3": n}})
            return True
        elif inv[3] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot4": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot4": n}})
            return True
        elif inv[4] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot5": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot5": n}})
            return True
        elif inv[5] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot6": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot6": n}})
            return True
        elif inv[6] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot7": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot7": n}})
            return True
        elif inv[7] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot8": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot8": n}})
            return True
        elif inv[8] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot9": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot9": n}})
            return True
        elif inv[9] == 0:
            players.update_one({"_id": uid}, {"$set": {"slot10": sum}})
            players.update_one({"_id": uid}, {"$set": {"nw_slot10": n}})
            return True
        else:
            return False



# @dp.message_handler(commands='Перевести')
async def pay(message: types.Message):
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
        if what == "золота":
            sender_have = check_sender["gold"]
            if sender_have >= how:
                players.update_one({"_id": uid}, {"$set": {"gold": sender_have - how}})
                await asyncio.sleep(3)
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["gold"]
                players.update_one({"name": name}, {"$set": {"gold": host_have + how}})
                await message.answer(f" Игрок {who} перевёл игроку {name} <{how}> {what}.")
            else:
                await message.answer(f" У вас нет {how} {what}!")
        if what == "бэсу":
            sender_have = check_sender["grass"]
            if sender_have >= how:
                players.update_one({"_id": uid}, {"$set": {"grass": sender_have - how}})
                await asyncio.sleep(3)
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["grass"]
                players.update_one({"name": name}, {"$set": {"grass": host_have + how}})
                await message.answer(f" Игрок {who} перевёл игроку {name} <{how}> {what}.")
            else:
                await message.answer(f" У вас нет {how} {what}!")
        if what == "базовой магической руды" or what == "бмр":
            sender_have = check_sender["iron"]
            if sender_have >= how:
                players.update_one({"_id": uid}, {"$set": {"iron": sender_have - how}})
                await asyncio.sleep(3)
                for check_host in players.find({"name": name}):
                    print("Cult finder done")
                host_have = check_host["iron"]
                players.update_one({"name": name}, {"$set": {"iron": host_have + how}})
                await message.answer(f" Игрок {who} перевёл игроку {name} <{how}> {what}.")
            else:
                await message.answer(f" У вас нет {how} {what}!")


# @dp.message_handler(commands='Передать_из_рюкзака')
async def pay2(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    what = int(getter[0])
    name = str(getter[1])
    inv = mongodb.findUserInventoryByID(uid)
    invn = mongodb.findUserInventoryNameByID(uid)
    for check_sender in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_sender["name"]
    check_player = Pay.check_player(name)
    if check_player[0] is False:
        await message.answer(f"Игрок {name} не найден.")
    elif check_player[0] is True:
        if what == 1:
            if inv[0] == 0:
                await message.answer('Слот №1 в рюкзаке пуст!')
            else:
                item_name = invn[0]
                sum = check_sender["slot1"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot1": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot1": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 2:
            if inv[1] == 0:
                await message.answer('Слот №2 в рюкзаке пуст!')
            else:
                item_name = invn[1]
                sum = check_sender["slot2"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot2": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot2": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 3:
            if inv[2] == 0:
                await message.answer('Слот №3 в рюкзаке пуст!')
            else:
                item_name = invn[2]
                sum = check_sender["slot3"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot3": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot3": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 4:
            if inv[3] == 0:
                await message.answer('Слот №4 в рюкзаке пуст!')
            else:
                item_name = invn[3]
                sum = check_sender["slot4"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot4": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot4": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 5:
            if inv[4] == 0:
                await message.answer('Слот №5 в рюкзаке пуст!')
            else:
                item_name = invn[4]
                sum = check_sender["slot5"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot5": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot5": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 6:
            if inv[5] == 0:
                await message.answer('Слот №6 в рюкзаке пуст!')
            else:
                item_name = invn[5]
                sum = check_sender["slot6"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot6": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot6": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 7:
            if inv[6] == 0:
                await message.answer('Слот №7 в рюкзаке пуст!')
            else:
                item_name = invn[6]
                sum = check_sender["slot7"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot7": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot7": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 8:
            if inv[7] == 0:
                await message.answer('Слот №8 в рюкзаке пуст!')
            else:
                item_name = invn[7]
                sum = check_sender["slot8"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot8": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot8": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 9:
            if inv[8] == 0:
                await message.answer('Слот №9 в рюкзаке пуст!')
            else:
                item_name = invn[8]
                sum = check_sender["slot9"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot9": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot9": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")
        if what == 10:
            if inv[9] == 0:
                await message.answer('Слот №10 в рюкзаке пуст!')
            else:
                item_name = invn[9]
                sum = check_sender["slot10"]
                for i in inventory.find({"number": sum}):
                    print("Cult finder done")
                host_uid = check_player[1]
                host = Pay.host(host_uid, sum, item_name)
                if host is True:
                    players.update_one({"_id": uid}, {"$set": {"slot10": 0}})
                    players.update_one({"_id": uid}, {"$set": {"nw_slot10": "Пусто"}})
                    await message.answer(f'Игрок {who} передал {name} <{i["name"]}>...')
                elif host is False:
                    await message.answer(f"Рюкзак игрока {name} переполнен!")


def register_handlers_pay(dp: Dispatcher):
    dp.register_message_handler(pay, commands='Перевести')
    dp.register_message_handler(pay2, commands='Передать_из_рюкзака')
