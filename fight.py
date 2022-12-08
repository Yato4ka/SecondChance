import asyncio
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


class Fight:
    def __init__(self, uid):
        self.uid = uid

    def check_slot(uid, tech):
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            if mag[0] == 0:
                return False
            else:
                return True
        if tech == 2:
            if mag[1] == 0:
                return False
            else:
                return True
        if tech == 3:
            if mag[2] == 0:
                return False
            else:
                return True
        if tech == 4:
            if mag[3] == 0:
                return False
            else:
                return True
        if tech == 5:
            if mag[4] == 0:
                return False
            else:
                return True
        if tech == 6:
            if mag[5] == 0:
                return False
            else:
                return True
        if tech == 7:
            if mag[6] == 0:
                return False
            else:
                return True
        if tech == 8:
            if mag[7] == 0:
                return False
            else:
                return True
        if tech == 9:
            if mag[8] == 0:
                return False
            else:
                return True
        if tech == 10:
            if mag[9] == 0:
                return False
            else:
                return True
        if tech == 11:
            if mag[10] == 0:
                return False
            else:
                return True
        if tech == 12:
            if mag[11] == 0:
                return False
            else:
                return True
        if tech == 13:
            if mag[12] == 0:
                return False
            else:
                return True
        if tech == 14:
            if mag[13] == 0:
                return False
            else:
                return True
        if tech == 15:
            if mag[14] == 0:
                return False
            else:
                return True
        if tech == 16:
            if mag[15] == 0:
                return False
            else:
                return True
        if tech == 17:
            if mag[16] == 0:
                return False
            else:
                return True
        if tech == 18:
            if mag[17] == 0:
                return False
            else:
                return True
        if tech == 19:
            if mag[18] == 0:
                return False
            else:
                return True
        if tech == 20:
            if mag[19] == 0:
                return False
            else:
                return True

    def check_type(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        dmg = tech_type["dmg"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Атака":
            return [True, dmg, cost, name]
        else:
            return [False]

    def check_type2(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        dmg = tech_type["dmg"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Усиление оружия":
            return [True, dmg, cost, name]
        else:
            return [False]

    def check_type3(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        buf_hp = tech_type["buf_hp"]
        buf_hp_reg = tech_type["buf_hp_reg"]
        buf_dex = tech_type["buf_dex"]
        buf_def = tech_type["buf_def"]
        buf_fiz_dmg = tech_type["buf_fiz_dmg"]
        buf_mag_dmg = tech_type["buf_mag_dmg"]
        buf_k_c = tech_type["buf_k_c"]
        buf_k_dmg = tech_type["buf_k_dmg"]
        buf_mana = tech_type["buf_mana"]
        buf_mana_reg = tech_type["buf_mana_reg"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Покрытие":
            return [True, name, cost, buf_hp, buf_hp_reg, buf_dex, buf_def, buf_fiz_dmg, buf_mag_dmg,  buf_k_c, buf_k_dmg, buf_mana, buf_mana_reg]
        else:
            return [False]

    def check_type4(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        buf_def = tech_type["buf_def"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Защита":
            return [True, name , cost, buf_def]
        else:
            return [False]


    def check_type5(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        dmg = tech_type["dmg"]
        buf_hp_reg = tech_type["buf_hp_reg"]
        buf_dex = tech_type["buf_dex"]
        buf_def = tech_type["buf_def"]
        buf_k_c = tech_type["buf_k_c"]
        buf_mana_reg = tech_type["buf_mana_reg"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Контроль":
            return [True, name , cost, dmg, buf_hp_reg, buf_dex, buf_def, buf_k_c, buf_mana_reg]
        else:
            return [False]


    def check_type6(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        buf_hp_reg = tech_type["buf_hp_reg"]
        buf_mana_reg = tech_type["buf_mana_reg"]
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Восстановление":
            return [True, name , cost, buf_hp_reg, buf_mana_reg]
        else:
            return [False]


    def check_type7(uid, tech):
        global tech_type
        mag = mongodb.findUserMagicByID(uid)
        if tech == 1:
            for tech_type in techniques.find({"num": (mag[0])}):
                print("Cult finder done")
        if tech == 2:
            for tech_type in techniques.find({"num": (mag[1])}):
                print("Cult finder done")
        if tech == 3:
            for tech_type in techniques.find({"num": (mag[2])}):
                print("Cult finder done")
        if tech == 4:
            for tech_type in techniques.find({"num": (mag[3])}):
                print("Cult finder done")
        if tech == 5:
            for tech_type in techniques.find({"num": (mag[4])}):
                print("Cult finder done")
        if tech == 6:
            for tech_type in techniques.find({"num": (mag[5])}):
                print("Cult finder done")
        if tech == 7:
            for tech_type in techniques.find({"num": (mag[6])}):
                print("Cult finder done")
        if tech == 8:
            for tech_type in techniques.find({"num": (mag[7])}):
                print("Cult finder done")
        if tech == 9:
            for tech_type in techniques.find({"num": (mag[8])}):
                print("Cult finder done")
        if tech == 10:
            for tech_type in techniques.find({"num": (mag[9])}):
                print("Cult finder done")
        if tech == 11:
            for tech_type in techniques.find({"num": (mag[10])}):
                print("Cult finder done")
        if tech == 12:
            for tech_type in techniques.find({"num": (mag[11])}):
                print("Cult finder done")
        if tech == 13:
            for tech_type in techniques.find({"num": (mag[12])}):
                print("Cult finder done")
        if tech == 14:
            for tech_type in techniques.find({"num": (mag[13])}):
                print("Cult finder done")
        if tech == 15:
            for tech_type in techniques.find({"num": (mag[14])}):
                print("Cult finder done")
        if tech == 16:
            for tech_type in techniques.find({"num": (mag[15])}):
                print("Cult finder done")
        if tech == 17:
            for tech_type in techniques.find({"num": (mag[16])}):
                print("Cult finder done")
        if tech == 18:
            for tech_type in techniques.find({"num": (mag[17])}):
                print("Cult finder done")
        if tech == 19:
            for tech_type in techniques.find({"num": (mag[18])}):
                print("Cult finder done")
        if tech == 20:
            for tech_type in techniques.find({"num": (mag[19])}):
                print("Cult finder done")
        cost = tech_type["cost"]
        type = tech_type["type"]
        name = tech_type["name"]
        if type == "Особое":
            return [True, name , cost]
        else:
            return [False]


    def check_evasion(uid, name):
        global findid
        for findid in players.find({"name": name}):
            print("Cult finder done")
        chance = random.randint(1,100)
        uid = findid['_id']
        fight = mongodb.findUserFightByID(uid)
        dex = int(fight[3])
        if dex >= chance:
            return True
        else:
            return False

    def check_krits(uid):
        chance = random.randint(1, 100)
        fight = mongodb.findUserFightByID(uid)
        krit = int(fight[7])
        print(f"{chance}, крит шанс- {krit}")
        if krit >= chance:
            print('тут я тру')
            return True
        else:
            print('тут фолс')
            return False

    def check_def(uid, name):
        global findid
        for findid in players.find({"name": name}):
            print("Cult finder done")
        uid = findid['_id']
        fight = mongodb.findUserFightByID(uid)
        defense = int(fight[4])
        if defense >= 1:
            return [True, defense]
        else:
            return [False]

    def check_active_def(uid, name):
        global findid
        for findid in players.find({"name": name}):
            print("Cult finder done12")
        con = mongodb.findUserConditionByID(uid)
        uid = findid['_id']
        fight = mongodb.findUserFightByID(uid)
        defense = int(con[13])
        buf_of_def = int(con[14])
        if defense > 1:
            time = con[13]
            players.update_one({"_id": uid}, {"$set": {"active_def": time - 1}})
            return [True, buf_of_def]
        elif defense == 1:
            asyncio.sleep(5)
            players.update_one({"_id": uid}, {"$set": {"active_def": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_active_def": 0}})
            players.update_one({"_id": uid}, {"$set": {"defense": fight[4] - buf_of_def}})
            return [True, buf_of_def]
        else:
            return [False]

    def check_active_control(name):
        global findid
        for findid in players.find({"name": name}):
            print("Cult finder done")
        uid = findid['_id']
        print(f"{uid}")
        con2 = mongodb.findUserCondition2ByID(uid)
        con = mongodb.findUserConditionByID(uid)
        print(f"{con[15]}")
        control = int(con[15])
        if control >= 1:
            uid = findid['_id']
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
            return [True]
        else:
            return [False]

    def check_active_coverage(uid):
        global check_mana
        con = mongodb.findUserConditionByID(uid)
        con2 = mongodb.findUserCondition2ByID(uid)
        coverage = int(con2[0])
        if coverage > 1:
            # понижаем длительность модификатора
            time = con2[0]
            players.update_one({"_id": uid}, {"$set": {"active_coverage": time - 1}})
        elif coverage == 1:
            buf_hp = con[1]
            buf_hp_reg = con[2]
            buf_dex = con[3]
            buf_def = con[4]
            buf_fiz_dmg = con[5]
            buf_mag_dmg = con[6]
            buf_k_c = con[7]
            buf_k_dmg = con[8]
            buf_mana = con[9]
            buf_mana_reg = con[10]
            asyncio.sleep(5)
            # сбрасываем модификаторы
            players.update_one({"_id": uid}, {"$set": {"active_coverage": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_hp": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_hp_reg": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_dex": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_def": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_fiz_dmg": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_mag_dmg": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_k_c": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_k_dmg": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_mana": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_mana_reg": 0}})
            # возвращаем статы типа
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            max_hp = check_mana['MaxHp']
            regeneration = check_mana['regeneration']
            dexterity = check_mana['dexterity']
            defense = check_mana['defense']
            physical_damage = check_mana['physical_damage']
            magic_damage = check_mana['magic_damage']
            Krit_Chance = check_mana['Krit_Chance']
            Krit_damage = check_mana['Krit_damage']
            max_mana = check_mana['max_mana']
            regeneration_mana = check_mana['regeneration_mana']
            players.update_one({"_id": uid}, {"$set": {"MaxHp": max_hp - buf_hp}})
            players.update_one({"_id": uid}, {"$set": {"regeneration": regeneration - buf_hp_reg}})
            players.update_one({"_id": uid}, {"$set": {"dexterity": dexterity - buf_dex}})
            players.update_one({"_id": uid}, {"$set": {"defense": defense - buf_def}})
            players.update_one({"_id": uid}, {"$set": {"physical_damage": physical_damage - buf_fiz_dmg}})
            players.update_one({"_id": uid}, {"$set": {"magic_damage": magic_damage - buf_mag_dmg}})
            players.update_one({"_id": uid}, {"$set": {"Krit_Chance": Krit_Chance - buf_k_c}})
            players.update_one({"_id": uid}, {"$set": {"Krit_damage": Krit_damage - buf_k_dmg}})
            players.update_one({"_id": uid}, {"$set": {"max_mana": max_mana - buf_mana}})
            players.update_one({"_id": uid}, {"$set": {"regeneration_mana": regeneration_mana - buf_mana_reg}})
            return [True]
        else:
            return [False]

    def check_active_gain(uid):
        con2 = mongodb.findUserCondition2ByID(uid)
        gain = con2[1]
        if gain > 1:
            time = con2[1]
            players.update_one({"_id": uid}, {"$set": {"active_gain": time - 1}})
            return [True]
        elif gain == 1:
            players.update_one({"_id": uid}, {"$set": {"active_gain": 0}})
            asyncio.sleep(5)
            players.update_one({"_id": uid}, {"$set": {"buf_lh": 0}})
            players.update_one({"_id": uid}, {"$set": {"buf_rh": 0}})
            return [True]
        else:
            return [False]


# @dp.message_handler(commands='Использовать_особую_технику')
async def rare_tech(message: types.Message):
    global check_mana
    uid = message.from_user.id
    tech = message.get_args()
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        print("а")
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        print("в")
        check_type7 = Fight.check_type7(uid, tech)
        if check_type7[0] is False:
            await message.answer(f"Техника №{tech} не является особой техникой!")
        elif check_type7[0] is True:
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            cost = check_type7[2]
            who = check_mana['name']
            mana = check_mana['mana']
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                name_of_tech = check_type7[1]
                players.update_one({"_id": uid}, {"$set": {"mana": mana - cost}})
                await message.answer(f'{who} использовал технику {name_of_tech}!')


# @dp.message_handler(commands='Использовать_технику_атаки')
async def atk_tech(message: types.Message):
    global findid, check_mana
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    tech = int(getter[0])
    name = str(getter[1])
    have_tech = Fight.check_slot(uid, tech)
    con = mongodb.findUserConditionByID(uid)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type = Fight.check_type(uid, tech)
        if check_type[0] is False:
            await message.answer(f"Техника №{tech} не является атакующей!")
        elif check_type[0] is True:
            cost = check_type[2]
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            who = check_mana['name']
            mana = check_mana['mana']
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                upload_message = await message.answer(f"Атакуем игрока {name} .")
                await asyncio.sleep(0.5)
                await upload_message.edit_text(text=f"Атакуем игрока {name} ..")
                await asyncio.sleep(0.5)
                await upload_message.edit_text(text=f"Атакуем игрока {name} ...")
                await asyncio.sleep(0.5)
                await upload_message.edit_text(text=f"Атака на игрока {name} совершена!")
                await asyncio.sleep(0.5)
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    check_coverage = Fight.check_active_coverage(uid)
                    if check_coverage[0] is True:
                        dmg = check_type[1]
                        buf_mag_dmg = con[6]
                        dmg = dmg + buf_mag_dmg
                        print(f'{dmg}')
                    else:
                        dmg = check_type[1]
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            name_of_tech = check_type[3]
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от техники <<{name_of_tech}>> игрока {who}, им было потрачено {cost} маны")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            name_of_tech = check_type[3]
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от техники <<{name_of_tech}>> игрока {who}, им было потрачено {cost} маны")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            name_of_tech = check_type[3]
                            players.update_one({"_id": uid}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от техники <<{name_of_tech}>> игрока {who}, им было потрачено {cost} маны")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            name_of_tech = check_type[3]
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg_with_def} урона от техники <<{name_of_tech}>> игрока {who}, им было потрачено {cost} маны")


# @dp.message_handler(commands='Использовать_технику_усиления_оружия')
async def weapon_buff_tech(message: types.Message):
    global check_mana
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    tech = int(getter[0])
    hand = str(getter[1])
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type2 = Fight.check_type2(uid, tech)
        if check_type2[0] is False:
            await message.answer(f"Техника №{tech} не является усилением оружия!")
        elif check_type2[0] is True:
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            cost = check_type2[2]
            who = check_mana['name']
            mana = check_mana['mana']
            name_of_tech = check_type2[3]
            dmg = check_type2[1]
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                if hand == "правую_руку":
                    weapon = check_mana['right_hand']
                    if weapon > 0:
                        players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                        players.update_one({"_id": uid}, {"$set": {"active_gain": 1}})
                        players.update_one({"_id": uid}, {"$set": {"buf_rh": dmg}})
                        await message.answer(f'''
Игрок {who} использовал технику <<{name_of_tech}>> для повышения урона оружия в правой руке на {dmg}
Было потрачено {cost} маны''')
                    else:
                        await message.answer(f"В правой руке нет оружия.")
                if hand == "левую_руку":
                    weapon = check_mana['left_hand']
                    if weapon > 0:
                        players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                        players.update_one({"_id": uid}, {"$set": {"active_gain": 1}})
                        players.update_one({"_id": uid}, {"$set": {"buf_lh": dmg}})
                        await message.answer(f'''
Игрок {who} использовал технику <<{name_of_tech}>> для повышения урона оружия в левой руке на {dmg}
Было потрачено {cost} маны''')
                    else:
                        await message.answer(f"В левой руке нет оружия.")


# @dp.message_handler(commands='Использовать_технику_покрытия')
async def coverage_tech(message: types.Message):
    global check_mana
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    tech = int(message.get_args())
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type3 = Fight.check_type3(uid, tech)
        if check_type3[0] is False:
            await message.answer(f"Техника №{tech} не является покрытием!")
        elif check_type3[0] is True:
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            cost = check_type3[2]
            who = check_mana['name']
            mana = check_mana['mana']
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                name_of_tech = check_type3[1]
                buf_hp = check_type3[3]
                buf_hp_reg = check_type3[4]
                buf_dex = check_type3[5]
                buf_def = check_type3[6]
                buf_fiz_dmg = check_type3[7]
                buf_mag_dmg = check_type3[8]
                buf_k_c = check_type3[9]
                buf_k_dmg = check_type3[10]
                buf_mana = check_type3[11]
                buf_mana_reg = check_type3[12]
                players.update_one({"_id": uid}, {"$set": {"active_coverage": 1}})
                players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                players.update_one({"_id": uid}, {"$set": {"buf_hp": buf_hp}})
                players.update_one({"_id": uid}, {"$set": {"buf_hp_reg": buf_hp_reg}})
                players.update_one({"_id": uid}, {"$set": {"buf_dex": buf_dex}})
                players.update_one({"_id": uid}, {"$set": {"buf_def": buf_def}})
                players.update_one({"_id": uid}, {"$set": {"buf_fiz_dmg": buf_fiz_dmg}})
                players.update_one({"_id": uid}, {"$set": {"buf_mag_dmg": buf_mag_dmg}})
                players.update_one({"_id": uid}, {"$set": {"buf_k_c": buf_k_c}})
                players.update_one({"_id": uid}, {"$set": {"buf_k_dmg": buf_k_dmg}})
                players.update_one({"_id": uid}, {"$set": {"buf_mana": buf_mana}})
                players.update_one({"_id": uid}, {"$set": {"buf_mana_reg": buf_mana_reg}})
                # добавляем к статам
                max_hp = check_mana['MaxHp']
                regeneration = check_mana['regeneration']
                dexterity = check_mana['dexterity']
                defense = check_mana['defense']
                physical_damage = check_mana['physical_damage']
                magic_damage = check_mana['magic_damage']
                Krit_Chance = check_mana['Krit_Chance']
                Krit_damage = check_mana['Krit_damage']
                max_mana = check_mana['max_mana']
                regeneration_mana = check_mana['regeneration_mana']
                players.update_one({"_id": uid}, {"$set": {"MaxHp": max_hp + buf_hp}})
                players.update_one({"_id": uid}, {"$set": {"regeneration": regeneration + buf_hp_reg}})
                players.update_one({"_id": uid}, {"$set": {"dexterity": dexterity + buf_dex}})
                players.update_one({"_id": uid}, {"$set": {"defense": defense + buf_def}})
                players.update_one({"_id": uid}, {"$set": {"physical_damage": physical_damage + buf_fiz_dmg}})
                players.update_one({"_id": uid}, {"$set": {"magic_damage": magic_damage + buf_mag_dmg}})
                players.update_one({"_id": uid}, {"$set": {"Krit_Chance": Krit_Chance + buf_k_c}})
                players.update_one({"_id": uid}, {"$set": {"Krit_damage": Krit_damage + buf_k_dmg}})
                players.update_one({"_id": uid}, {"$set": {"max_mana": max_mana + buf_mana}})
                players.update_one({"_id": uid}, {"$set": {"regeneration_mana": regeneration_mana + buf_mana_reg}})
                await message.answer(f'''
                Игрок {who} использовал технику <<{name_of_tech}>> для повышения характеристик.
                Было потрачено {cost} маны''')


# @dp.message_handler(commands='Использовать_технику_защиты')
async def def_tech(message: types.Message):
    global check_mana
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    tech = int(message.get_args())
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type4 = Fight.check_type4(uid, tech)
        if check_type4[0] is False:
            await message.answer(f"Техника №{tech} не является защитой!")
        elif check_type4[0] is True:
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            cost = check_type4[2]
            who = check_mana['name']
            mana = check_mana['mana']
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                name_of_tech = check_type4[1]
                buf_of_def = check_type4[3]
                defe = fight[4]
                players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                players.update_one({"_id": uid}, {"$set": {"active_def": 1}})
                players.update_one({"_id": uid}, {"$set": {"buf_active_def": buf_of_def}})
                players.update_one({"_id": uid}, {"$set": {"defense": defe + buf_of_def}})
                await message.answer(f"""
Игрок {who} использовал технику защиты {name_of_tech}, потратив {cost} маны.
Следующая атака проотивника будет подвергнута поглощению урона на {buf_of_def} %!""")


# @dp.message_handler(commands='Использовать_технику_контроля')
async def control_tech(message: types.Message):
    global findid, check_mana
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    tech = int(getter[0])
    name = str(getter[1])
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type5 = Fight.check_type5(uid, tech)
        if check_type5[0] is False:
            await message.answer(f"Техника №{tech} не является контролем!")
        elif check_type5[0] is True:
            for check_mana in players.find({"_id": uid}):
                print("Cult finder done")
            cost = check_type5[2]
            who = check_mana['name']
            mana = check_mana['mana']
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    if findid['active_control'] != 0:
                        await message.answer(f"Этот игрок уже находится под техникой контроля!")
                    else:
                        await message.answer("Противнику не удалось уклониться!")
                        name_of_tech = check_type5[1]
                        dmg = check_type5[3]
                        buf_hp_reg = check_type5[4]
                        buf_dex = check_type5[5]
                        buf_def = check_type5[6]
                        buf_k_c = check_type5[7]
                        buf_mana_reg = check_type5[8]
                        players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})

                        # модификаторы
                        uid = findid['_id']
                        con2 = mongodb.findUserCondition2ByID(uid)
                        new_buf_hp_reg = con2[2] - buf_hp_reg
                        new_buf_dex = con2[3] - buf_dex
                        new_buf_def = con2[4] - buf_def
                        new_buf_k_c = con2[5] - buf_k_c
                        new_buf_mana_reg = con2[6] + buf_mana_reg
                        players.update_one({"_id": uid}, {"$set": {"active_control": 1}})
                        players.update_one({"_id": uid}, {"$set": {"debuf_hp_reg": new_buf_hp_reg}})
                        players.update_one({"_id": uid}, {"$set": {"debuf_dex": new_buf_dex}})
                        players.update_one({"_id": uid}, {"$set": {"debuf_def": new_buf_def}})
                        players.update_one({"_id": uid}, {"$set": {"debuf_k_c": new_buf_k_c}})
                        players.update_one({"_id": uid}, {"$set": {"debuf_mana_reg": new_buf_mana_reg}})

                        # режем статы противника
                        hp = findid['Hp']
                        regeneration = findid['regeneration']
                        dexterity = findid['dexterity']
                        defense = findid['defense']
                        Krit_Chance = findid['Krit_Chance']
                        regeneration_mana = findid['regeneration_mana']

                        players.update_one({"_id": uid}, {"$set": {"Hp": hp - dmg}})
                        players.update_one({"_id": uid}, {"$set": {"regeneration": regeneration - buf_hp_reg}})
                        players.update_one({"_id": uid}, {"$set": {"dexterity": dexterity - buf_dex}})
                        players.update_one({"_id": uid}, {"$set": {"defense": defense - buf_def}})
                        players.update_one({"_id": uid}, {"$set": {"Krit_Chance": Krit_Chance - buf_k_c}})
                        players.update_one({"_id": uid},
                                           {"$set": {"regeneration_mana": regeneration_mana - buf_mana_reg}})
                        if dmg == 0:
                            await message.answer(f"""
                        Игрок {who} использовал технику контроля {name_of_tech} на {name}, потратив {cost} маны.
                        {name} был подвержен дебаффам!""")
                        if dmg >= 1:
                            await message.answer(f"""
                        Игрок {who} использовал технику контроля {name_of_tech} на {name}, потратив {cost} маны.
                        {name} был подвержен дебаффам и получил {dmg} урона!""")


# @dp.message_handler(commands='Использовать_технику_восстановления')
async def heal_tech(message: types.Message):
    global findid
    uid = message.from_user.id
    fight = mongodb.findUserFightByID(uid)
    main = mongodb.findUserMainByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    tech = int(getter[0])
    name = str(getter[1])
    have_tech = Fight.check_slot(uid, tech)
    if have_tech is False:
        await message.answer(f"Техника №{tech} отсутсвует!")
    if have_tech is True:
        check_type6 = Fight.check_type6(uid, tech)
        if check_type6[0] is False:
            await message.answer(f"Техника №{tech} не является восстановлением!")
        elif check_type6[0] is True:
            cost = check_type6[2]
            who = main[0]
            mana = fight[11]
            if mana - cost < 0:
                await message.answer(f"У вас не хватает маны!")
            if mana - cost >= 0:
                players.update_one({"_id": uid}, {"$set": {"mana": fight[11] - cost}})
                print(f'{fight[11]} - {cost} = {fight[11] - cost}')
                for findid in players.find({"name": name}):
                    print("Cult finder done")
                name_of_tech = check_type6[1]
                uid2 = findid['_id']
                hp = findid['Hp']
                heal = check_type6[3]
                mana_heal = check_type6[4]
                if heal >= 1 and mana_heal >= 1:
                    players.update_one({"_id": uid2}, {"$set": {"Hp": hp + heal}})
                    players.update_one({"_id": uid2}, {"$set": {"mana": mana + mana_heal}})
                    if uid == uid2:
                        await message.answer(f"""
Игрок {who} восстоновил cебе здоровье на {heal} хп и ману на {mana_heal}, использовав {name_of_tech}.
Потрачено маны - {cost}.""")
                    else:
                        await message.answer(f"""
Игрок {who} восстоновил здоровье игрока {name} на {heal} хп и ману на {mana_heal}, использовав {name_of_tech}.
Потрачено маны - {cost}.""")
                elif heal >= 1:
                    players.update_one({"_id": uid2}, {"$set": {"Hp": hp + heal}})
                    if uid == uid2:
                        await message.answer(f"""
Игрок {who} восстоновил cебе здоровье на {heal} хп, использовав {name_of_tech}.
Потрачено маны - {cost}.""")
                    else:
                        await message.answer(f"""
Игрок {who} восстоновил здоровье игрока {name} на {heal} хп, использовав {name_of_tech}.
Потрачено маны - {cost}.""")
                elif mana_heal >= 1:
                    players.update_one({"_id": uid2}, {"$set": {"mana": mana + mana_heal}})
                    if uid == uid2:
                        await message.answer(f"""
Игрок {who} восстоновил cебе ману на {mana_heal}, использовав {name_of_tech}.
Потрачено маны - {cost}.""")
                    else:
                        await message.answer(f"""
Игрок {who} восстоновил ману игрока {name} на {mana_heal}, использовав {name_of_tech}.
Потрачено маны - {cost}.""")


# @dp.message_handler(commands='Использовать_оружие_в')
async def weapon_atk(message: types.Message):
    global check_who, findid, check_left, check_right
    uid = message.from_user.id
    con = mongodb.findUserConditionByID(uid)
    invn = mongodb.findUserInventoryNameByID(uid)
    fight = mongodb.findUserFightByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    hand = str(getter[0])
    name = str(getter[1])
    equip = mongodb.findUserEquipmentByID(uid)
    check_coverage = Fight.check_active_coverage(uid)
    for check_who in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_who['name']
    check_active_gain = Fight.check_active_gain(uid)
    if hand == "левой_руке":
        check_equip = equip[1]
        if check_equip >= 1:
            krit = Fight.check_krits(uid)
            if krit is False:
                await message.answer('Крит не прошёл!')
                for check_left in inventory.find({"number": equip[1]}):
                    print("Cult finder done")
                if check_active_gain[0] is True:
                    buf_lh = con[12]
                    dmg = check_left["damage"] + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                else:
                    dmg = check_left["damage"] + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                for findid in players.find({"name": name}):
                    print("Cult finder done132")
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
            if krit is True:
                await message.answer('Крит прошёл!')
                for check_left in inventory.find({"number": equip[1]}):
                    print("Cult finder done")
                if check_active_gain[0] is True:
                    buf_lh = con[12]
                    dmg = check_left["damage"] + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                else:
                    dmg = check_left["damage"] + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done132")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[11]} игрока {who}")
        else:
            await message.answer(f"У вас нет оружия в левой руке!")
    elif hand == "правой_руке":
        check_equip = equip[0]
        if check_equip >= 1:
            krit = Fight.check_krits(uid)
            if krit is False:
                await message.answer('Крит не прошёл!')
                await message.answer("Крит урон не прошел!")
                for check_right in inventory.find({"number": equip[0]}):
                    print("Cult finder done")
                if check_active_gain[0] is True:
                    buf_lh = con[11]
                    dmg = check_right["damage"] + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                else:
                    dmg = check_right["damage"] + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} игрока {who}")
            elif krit is True:
                await message.answer('Крит прошёл!')
                await message.answer("Крит урон прошёл!")
                for check_right in inventory.find({"number": equip[0]}):
                    print("Cult finder done")
                if check_active_gain[0] is True:
                    buf_lh = con[11]
                    dmg = check_right["damage"] + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                else:
                    dmg = check_right["damage"] + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от оружия {invn[10]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} игрока {who}")
        else:
            await message.answer(f"У вас нет оружия в правой руке!")

    elif hand == "обеих_руках":
        check_equip = equip[1]
        check_equip2 = equip[0]
        if check_equip >= 1 and check_equip2 >= 1:
            krit = Fight.check_krits(uid)
            if krit is False:
                await message.answer('Крит не прошёл!')
                for check_right in inventory.find({"number": equip[0]}):
                    print("Cult finder done")
                dmg1 = check_right["damage"]
                for check_left in inventory.find({"number": equip[1]}):
                    print("Cult finder done")
                dmg2 = check_left["damage"]
                if check_active_gain[0] is True:
                    buf_rh = con[11]
                    buf_lh = con[12]
                    dmg = dmg1 + dmg2 + buf_rh + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                else:
                    dmg = dmg1 + dmg2 + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
            if krit is True:
                await message.answer('Крит прошёл!')
                for check_right in inventory.find({"number": equip[0]}):
                    print("Cult finder done")
                dmg1 = check_right["damage"]
                for check_left in inventory.find({"number": equip[1]}):
                    print("Cult finder done")
                dmg2 = check_left["damage"]
                if check_active_gain[0] is True:
                    buf_rh = con[11]
                    buf_lh = con[12]
                    dmg = dmg1 + dmg2 + buf_rh + buf_lh + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                else:
                    dmg = dmg1 + dmg2 + fight[5]
                    if check_coverage[0] is True:
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                evasion = Fight.check_evasion(uid, name)
                if evasion is True:
                    await message.answer("Противник уклонился!")
                elif evasion is False:
                    await message.answer("Противнику не удалось уклониться!")
                    for findid in players.find({"name": name}):
                        print("Cult finder done")
                    ac = Fight.check_active_control(name)
                    if ac[0] is True:
                        await message.answer(f"С противника снята техника контроля!")
                    elif ac[0] is False:
                        print('Контроля не было')
                    check_active_def = Fight.check_active_def(uid, name)
                    check_def = Fight.check_def(uid, name)
                    if check_active_def[0] is True:
                        await message.answer("Техника защиты противника присутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            defe = check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1] + check_active_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                    elif check_active_def[0] is False:
                        await message.answer("Техника защиты противника отсутствует!")
                        if check_def[0] is False:
                            await message.answer("Базовая защита противника отсутствует!")
                            players.update_one({"_id": findid["_id"]}, {"$set": {"Hp": findid["Hp"] - dmg}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
                        elif check_def[0] is True:
                            await message.answer("Базовая защита противника присутствует!")
                            defe = check_def[1]
                            dmg_without_def = dmg
                            procent = dmg_without_def / 100
                            procent = procent * defe
                            dmg_with_def = dmg_without_def - procent
                            hp = findid["Hp"] - dmg_with_def
                            players.update_one({"_id": findid['_id']}, {"$set": {"Hp": hp}})
                            await asyncio.sleep(5)
                            await message.answer(
                                f"Игроку {name} было нанесено {dmg} урона от {invn[10]} и {invn[11]} игрока {who}")
        else:
            await message.answer(f"У вас нет оружия в обеих руках!")


# @dp.message_handler(commands='Базовая_атака')
async def base_atk(message: types.Message):
    global check_enemy, check_enemy, check_who
    uid = message.from_user.id
    con = mongodb.findUserConditionByID(uid)
    fight = mongodb.findUserFightByID(uid)
    name = message.get_args()
    check_coverage = Fight.check_active_coverage(uid)
    for check_who in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_who['name']
    krit = Fight.check_krits(uid)
    if krit is False:
        await message.answer("Крит не прошёл!")
        if check_coverage[0] is True:
            dmg = fight[5]
            buf_fiz_dmg = con[5]
            dmg = dmg + buf_fiz_dmg
            print(f'{dmg}')
        else:
            dmg = fight[5]
        evasion = Fight.check_evasion(uid, name)
        for check_who in players.find({"_id": uid}):
            print("Cult finder done")
        who = check_who['name']
        if evasion is True:
            await message.answer("Противник уклонился!")
        elif evasion is False:
            for check_enemy in players.find({"name": name}):
                print("Cult finder done")
            await message.answer("Противнику не удалось уклониться!")
            ac = Fight.check_active_control(name)
            if ac[0] is True:
                await message.answer(f"С противника снята техника контроля!")
            elif ac[0] is False:
                print('Контроля не было')
            check_active_def = Fight.check_active_def(uid, name)
            check_def = Fight.check_def(uid, name)
            if check_active_def[0] is True:
                await message.answer("Техника защиты противника присутствует!")
                if check_def[0] is False:
                    await message.answer("Базовая защита противника отсутствует!")
                    defe = check_active_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await message.answer("Базовая защита противника отсутствует!")
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")
                elif check_def[0] is True:
                    await message.answer("Базовая защита противника присутствует!")
                    defe = check_def[1] + check_active_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")
            elif check_active_def[0] is False:
                await message.answer("Техника защиты противника отсутствует!")
                if check_def[0] is False:
                    await message.answer("Базовая защита противника отсутствует!")
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": check_enemy["Hp"] - dmg}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg} урона от базовой атаки игрока {who}")
                elif check_def[0] is True:
                    await message.answer("Базовая защита противника присутствует!")
                    defe = check_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")
    if krit is True:
        await message.answer("Крит прошёл!")
        if check_coverage[0] is True:
            dmg = fight[5]
            buf_fiz_dmg = con[5]
            dmg = dmg + buf_fiz_dmg
            dmg_without = dmg / 100
            dmg_without = dmg_without * fight[8]
            dmg = dmg + dmg_without
        else:
            dmg = fight[5]
            dmg_without = dmg / 100
            dmg_without = dmg_without * fight[8]
            dmg = dmg + dmg_without
        evasion = Fight.check_evasion(uid, name)
        for check_who in players.find({"_id": uid}):
            print("Cult finder done")
        who = check_who['name']
        if evasion is True:
            await message.answer("Противник уклонился!")
        elif evasion is False:
            for check_enemy in players.find({"name": name}):
                print("Cult finder done")
            await message.answer("Противнику не удалось уклониться!")
            ac = Fight.check_active_control(name)
            if ac[0] is True:
                await message.answer(f"С противника снята техника контроля!")
            elif ac[0] is False:
                print('Контроля не было')
            check_active_def = Fight.check_active_def(uid, name)
            check_def = Fight.check_def(uid, name)
            if check_active_def[0] is True:
                await message.answer("Техника защиты противника присутствует!")
                if check_def[0] is False:
                    await message.answer("Базовая защита противника отсутствует!")
                    defe = check_active_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await message.answer("Базовая защита противника отсутствует!")
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")
                elif check_def[0] is True:
                    await message.answer("Базовая защита противника присутствует!")
                    defe = check_def[1] + check_active_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")
            elif check_active_def[0] is False:
                await message.answer("Техника защиты противника отсутствует!")
                if check_def[0] is False:
                    await message.answer("Базовая защита противника отсутствует!")
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": check_enemy["Hp"] - dmg}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg} урона от базовой атаки игрока {who}")
                elif check_def[0] is True:
                    await message.answer("Базовая защита противника присутствует!")
                    defe = check_def[1]
                    dmg_without_def = dmg
                    procent = dmg_without_def / 100
                    procent = procent * defe
                    dmg_with_def = dmg_without_def - procent
                    hp = check_enemy["Hp"] - dmg_with_def
                    players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                    await asyncio.sleep(5)
                    await message.answer(
                        f"Игроку {name} было нанесено {dmg_with_def} урона от базовой атаки игрока {who}")


# @dp.message_handler(commands='Руническая_атака')
async def rune_atk(message: types.Message):
    global check_enemy, check_rune, dama, check_who
    uid = message.from_user.id
    con = mongodb.findUserConditionByID(uid)
    equip = mongodb.findUserEquipmentByID(uid)
    fight = mongodb.findUserFightByID(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    slot = int(getter[0])
    name = str(getter[1])
    check_coverage = Fight.check_active_coverage(uid)
    for check_who in players.find({"_id": uid}):
        print("Cult finder done")
    who = check_who['name']
    krit = Fight.check_krits(uid)
    if equip[0] == 0 and equip[1] == 0:
        await message.answer(f"У вас нет оружия в руке!")
    else:
        if slot == 1:
            dama = equip[6]
        elif slot == 2:
            dama = equip[7]
        else:
            await message.answer("Не существует такого слота под рунический камень!")
        for check_rune in inventory.find({"number": dama}):
            print("Cult finder done")
        if check_rune["dmg"] == 0:
            await message.answer(f"Рунный камень номер №1 не является атакующим!")
        else:
            if equip[9] == 0:
                await message.answer(f"Сила рунных камней уже была истрачена!")
            else:
                players.update_one({"_id": uid}, {"$set": {"rune_charge": equip[9] - check_rune['cost']}})
                if krit is False:
                    await message.answer("Крит не прошёл!")
                    if check_coverage[0] is True:
                        dmg = check_rune["dmg"]
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        print(f'{dmg}')
                    else:
                        dmg = check_rune["dmg"]
                    evasion = Fight.check_evasion(uid, name)
                    if evasion is True:
                        await message.answer("Противник уклонился!")
                    elif evasion is False:
                        for check_enemy in players.find({"name": name}):
                            print("Cult finder done")
                        await message.answer("Противнику не удалось уклониться!")
                        ac = Fight.check_active_control(name)
                        if ac[0] is True:
                            await message.answer(f"С противника снята техника контроля!")
                        elif ac[0] is False:
                            print('Контроля не было')
                        check_active_def = Fight.check_active_def(uid, name)
                        check_def = Fight.check_def(uid, name)
                        if check_active_def[0] is True:
                            await message.answer("Техника защиты противника присутствует!")
                            if check_def[0] is False:
                                await message.answer("Базовая защита противника отсутствует!")
                                players.update_one({"_id": check_enemy['_id']},
                                                   {"$set": {"Hp": check_enemy["Hp"] - dmg}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                            elif check_def[0] is True:
                                await message.answer("Базовая защита противника присутствует!")
                                defe = check_def[1] + check_def[2]
                                dmg_without_def = dmg
                                procent = dmg_without_def / 100
                                procent = procent * defe
                                dmg_with_def = dmg_without_def - procent
                                hp = check_enemy["Hp"] - dmg_with_def
                                players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                        elif check_active_def[0] is False:
                            await message.answer("Техника защиты противника отсутствует!")
                            if check_def[0] is False:
                                await message.answer("Базовая защита противника отсутствует!")
                                print(f" имя - {check_enemy['name']} ")
                                players.update_one({"_id": check_enemy['_id']},
                                                   {"$set": {"Hp": check_enemy["Hp"] - dmg}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                            elif check_def[0] is True:
                                await message.answer("Базовая защита противника присутствует!")
                                defe = check_def[1]
                                dmg_without_def = dmg
                                procent = dmg_without_def / 100
                                procent = procent * defe
                                dmg_with_def = dmg_without_def - procent
                                hp = check_enemy["Hp"] - dmg_with_def
                                players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                if krit is True:
                    await message.answer("Крит прошёл!")
                    if check_coverage[0] is True:
                        dmg = check_rune["dmg"]
                        buf_fiz_dmg = con[5]
                        dmg = dmg + buf_fiz_dmg
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    else:
                        dmg = check_rune["dmg"]
                        dmg_without = dmg / 100
                        dmg_without = dmg_without * fight[8]
                        dmg_krit = dmg + dmg_without
                        dmg = dmg + dmg_krit
                    evasion = Fight.check_evasion(uid, name)
                    for check_who in players.find({"_id": uid}):
                        print("Cult finder done")
                    who = check_who['name']
                    if evasion is True:
                        await message.answer("Противник уклонился!")
                    elif evasion is False:
                        for check_enemy in players.find({"name": name}):
                            print("Cult finder done")
                        await message.answer("Противнику не удалось уклониться!")
                        ac = Fight.check_active_control(name)
                        if ac[0] is True:
                            await message.answer(f"С противника снята техника контроля!")
                        elif ac[0] is False:
                            print('Контроля не было')
                        check_active_def = Fight.check_active_def(uid, name)
                        check_def = Fight.check_def(uid, name)
                        if check_active_def[0] is True:
                            await message.answer("Техника защиты противника присутствует!")
                            if check_def[0] is False:
                                await message.answer("Базовая защита противника отсутствует!")
                                defe = check_active_def[1]
                                dmg_without_def = dmg
                                procent = dmg_without_def / 100
                                procent = procent * defe
                                dmg_with_def = dmg_without_def - procent
                                hp = check_enemy["Hp"] - dmg_with_def
                                players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                                await message.answer("Базовая защита противника отсутствует!")
                                await asyncio.sleep(5)
                                players.update_one({"_id": check_enemy['_id']},
                                                   {"$set": {"Hp": check_enemy["Hp"] - hp}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                            elif check_def[0] is True:
                                await message.answer("Базовая защита противника присутствует!")
                                defe = check_def[1] + check_active_def[1]
                                dmg_without_def = dmg
                                procent = dmg_without_def / 100
                                procent = procent * defe
                                dmg_with_def = dmg_without_def - procent
                                hp = check_enemy["Hp"] - dmg_with_def
                                players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f"Игроку {name} было нанесено {dmg} урона от рунической атаки игрока {who}")

                        elif check_active_def[0] is False:
                            await message.answer("Техника защиты противника отсутствует!")
                            if check_def[0] is False:
                                await message.answer("Базовая защита противника отсутствует!")
                                players.update_one({"_id": check_enemy['_id']},
                                                   {"$set": {"Hp": check_enemy["Hp"] - dmg}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')
                            elif check_def[0] is True:
                                await message.answer("Базовая защита противника присутствует!")
                                defe = check_def[1]
                                dmg_without_def = dmg
                                procent = dmg_without_def / 100
                                procent = procent * defe
                                dmg_with_def = dmg_without_def - procent
                                hp = check_enemy["Hp"] - dmg_with_def
                                players.update_one({"_id": check_enemy['_id']}, {"$set": {"Hp": hp}})
                                await asyncio.sleep(5)
                                await message.answer(
                                    f'Игроку {name} было нанесено {dmg} урона от рунической атаки {check_rune["name"]} игрока {who}')



def register_handlers_fight(dp: Dispatcher):
    dp.register_message_handler(atk_tech, commands='Использовать_технику_атаки')
    dp.register_message_handler(weapon_buff_tech, commands='Использовать_технику_усиления_оружия')
    dp.register_message_handler(coverage_tech, commands='Использовать_технику_покрытия')
    dp.register_message_handler(def_tech, commands='Использовать_технику_защиты')
    dp.register_message_handler(control_tech, commands='Использовать_технику_контроля')
    dp.register_message_handler(heal_tech, commands = 'Использовать_технику_восстановления')
    dp.register_message_handler(weapon_atk, commands='Использовать_оружие_в')
    dp.register_message_handler(base_atk, commands='Базовая_атака')
    dp.register_message_handler(rare_tech, commands='Использовать_особую_технику')
    dp.register_message_handler(rune_atk, commands='Руническая_атака')
