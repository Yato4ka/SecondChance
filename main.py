import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from pymongo import MongoClient
from aiogram.utils import executor

import craft
import lvl_up
import fight
import pay
import admin
import party
import owner
from mongodb import Finder as mongodb
from hero import Hero as hero

logging.basicConfig(level=logging.INFO)

# API_TOKEN = "5630709456:AAFOv7D-quDZVDTU9blzh5XCh2F56reaeDc"
API_TOKEN = "5748959263:AAGnr1pc749I2sOdJIJPJo2uHBJb4d2e2Q4"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

admin.register_handlers_admin(dp)
pay.register_handlers_pay(dp)
craft.register_handlers_craft(dp)
lvl_up.register_handlers_lvl_up(dp)
fight.register_handlers_fight(dp)
party.register_handlers_party(dp)
owner.register_handlers_owner(dp)

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


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    uid = message.from_user.id
    p_id = mongodb.findUserParamByID(uid)
    if p_id is None:
        await hero.name.set()
        await message.answer("Введите прозвище вашего персонажа. \n (Второй пункт анкеты)")

        @dp.message_handler(state=hero.name)
        async def cmd_name(message: types.Message, state: FSMContext):
            await hero.name.set()

            async with state.proxy() as data:
                data['Name'] = message.text
                uid = message.from_user.id
                name = data['Name']

                players.insert_one({
                    "_id": uid,
                    "name": name,
                    "level": hero.level,
                    "energy" : hero.energy,
                    "first_element": hero.first_element,
                    "second_element": hero.second_element,
                    "final_element": hero.final_element,

                    "MaxHp": hero.MaxHp,
                    "Hp": hero.Hp,
                    "regeneration": hero.regeneration,
                    "dexterity": hero.dexterity,
                    "defense": hero.defense,
                    "physical_damage": hero.physical_damage,
                    "magic_damage": hero.magic_damage,
                    "Krit_Chance": hero.Krit_Chance,
                    "Krit_damage": hero.Krit_damage,
                    "max_mana": hero.max_mana,
                    "regeneration_mana": hero.regeneration_mana,
                    "mana": hero.mana,

                    "magic_points": hero.magic_points,
                    "physical_points": hero.physical_points,
                    "rp_point": hero.rp_point,
                    "talent_point": hero.talent_point,

                    "condition" : hero.condition,

                    "active_def": hero.active_def,
                    "buf_active_def" : hero.buf_active_def,

                    "active_control" : hero.active_control,
                    "debuf_hp_reg" : hero.debuf_hp_reg,
                    "debuf_dex" : hero.debuf_dex,
                    "debuf_def" : hero.debuf_def,
                    "debuf_k_c" : hero.debuf_k_c,
                    "debuf_mana_reg" : hero.debuf_mana_reg,

                    "active_coverage" : hero.active_coverage,
                    "buf_hp": hero.buf_hp,
                    "buf_hp_reg": hero.buf_hp_reg,
                    "buf_dex": hero.buf_dex,
                    "buf_def": hero.buf_def,
                    "buf_fiz_dmg": hero.buf_fiz_dmg,
                    "buf_mag_dmg": hero.buf_mag_dmg,
                    "buf_k_c": hero.buf_k_c,
                    "buf_k_dmg": hero.buf_k_dmg,
                    "buf_mana": hero.buf_mana,
                    "buf_mana_reg": hero.buf_mana_reg,

                    "active_gain" : hero.active_gain,
                    "buf_rh": hero.buf_rh,
                    "buf_lh": hero.buf_lh,

                    "rp_charisma": hero.rp_charisma,
                    "rp_kraft_skill": hero.rp_kraft_skill,
                    "rp_alchemy_skill": hero.rp_alchemy_skill,
                    "rp_strength": hero.rp_strength,
                    "rp_dexterity": hero.rp_dexterity,
                    "rp_theft": hero.rp_theft,
                    "rp_stealth": hero.rp_stealth,
                    "rp_attentiveness": hero.rp_attentiveness,
                    "rp_hacking": hero.rp_hacking,
                    "rp_luck" : 0,
                    "rp_willpower": 0,
                    "rp_language": 0,
                    "rp_speed": 0,
                    "rp_intelligence": 0,

                    "Game_Master": hero.Game_Master,
                    "Helper": hero.Helper,
                    "Moderator": hero.Moderator,
                    "Admin": hero.Admin,

                    "right_hand": hero.right_hand,
                    "left_hand": hero.left_hand,
                    "armor": hero.armor,
                    "amulet": hero.amulet,
                    "ring1": hero.ring1,
                    "ring2": hero.ring2,
                    "accessory1": hero.accessory1,
                    "accessory2": hero.accessory2,
                    "pet": hero.pet,
                    "rune_charge": 0,

                    "slot1": hero.slot1,
                    "slot2": hero.slot2,
                    "slot3": hero.slot3,
                    "slot4": hero.slot4,
                    "slot5": hero.slot5,
                    "slot6": hero.slot6,
                    "slot7": hero.slot7,
                    "slot8": hero.slot8,
                    "slot9": hero.slot9,
                    "slot10": hero.slot10,

                    "material": hero.material,
                    "gold": hero.gold,
                    "coin": hero.coin,
                    "grass": hero.grass,
                    "grass2": hero.grass2,
                    "grass3": hero.grass3,
                    "iron": hero.iron,
                    "iron2": hero.iron2,
                    "iron3": hero.iron3,

                    "fraction": hero.fraction,
                    "fraction_respect": hero.fraction_respect,
                    "guild": hero.guild,
                    "guild_respect": hero.guild_respect,
                    "location": hero.location,

                    "home": 0,

                    "fraction_bonus_type": "отсутствует",
                    "fraction_bonus": 0,

                    "technique1": hero.technique1,
                    "technique2": hero.technique2,
                    "technique3": hero.technique3,
                    "technique4": hero.technique4,
                    "technique5": hero.technique5,
                    "technique6": hero.technique6,
                    "technique7": hero.technique7,
                    "technique8": hero.technique8,
                    "technique9": hero.technique9,
                    "technique10": hero.technique10,
                    "technique11": hero.technique11,
                    "technique12": hero.technique12,
                    "technique13": hero.technique13,
                    "technique14": hero.technique14,
                    "technique15": hero.technique15,
                    "technique16": hero.technique16,
                    "technique17": hero.technique17,
                    "technique18": hero.technique18,
                    "technique19": hero.technique19,
                    "technique20": hero.technique20,

                    "enemy1": hero.enemy1,
                    "enemy2": hero.enemy2,
                    "enemy3": hero.enemy3,
                    "enemy4": hero.enemy4,
                    "enemy5": hero.enemy5,

                    "nw_slot1": "Пусто",
                    "nw_slot2": "Пусто",
                    "nw_slot3": "Пусто",
                    "nw_slot4": "Пусто",
                    "nw_slot5": "Пусто",
                    "nw_slot6": "Пусто",
                    "nw_slot7": "Пусто",
                    "nw_slot8": "Пусто",
                    "nw_slot9": "Пусто",
                    "nw_slot10": "Пусто",
                    "nw_right_hand": "Пусто",
                    "nw_left_hand": "Пусто",
                    "hunger": 0,
                    "thirst": 0,
                    "cold": 0,
                    "version": 1.7,
                })

                await state.finish()
            await asyncio.sleep(1)
            await message.answer(f'Удачной игры!')
    else:
        await bot.send_message(message.chat.id, "У вас уже есть персонаж!")


@dp.message_handler()
async def cmds(message: types.Message):
    global level_name, loc, text, party, tech20, tech19, tech18, tech17, tech16, tech15, tech14, tech13, tech12, tech11, tech10, tech9, tech8, tech7, tech6, tech5, tech4, tech3, tech2, tech1
    uid = message.from_user.id
    main = mongodb.findUserMainByID(uid)
    fight = mongodb.findUserFightByID(uid)
    point = mongodb.findUserPointByID(uid)
    rp = mongodb.findUserRpByID(uid)
    place = mongodb.findUserPlaceByID(uid)
    equip = mongodb.findUserEquipmentByID(uid)
    inv = mongodb.findUserInventoryByID(uid)
    invn = mongodb.findUserInventoryNameByID(uid)
    cur = mongodb.findUserCurrencyByID(uid)
    mag = mongodb.findUserMagicByID(uid)
    con = mongodb.findUserConditionByID(uid)
    con2 = mongodb.findUserCondition2ByID(uid)
    if message.text == 'Профиль':
        for level_name in levels.find({"number": (main[1])}):
            print("Cult finder done")
        for loc in locations_and_clans.find({"num": place[4]}):
            print("Inv finder done")
        for party in clans.find({"num": place[2]}):
            print("Inv finder done")
        text = ""
        bonus_f = place[5]
        if place[6] >= 1:
            text = f"(+{[place[6]]})"
        home = "отсутствует"
        if cur[9] >= 1:
            home = "присутствует"
        await message.delete()
        await message.answer(f"""
-----------------------------------------
★ Имя ➤ {main[0]}   (◡‿◡) 

Уровень ➤ {level_name['name']}
Природная энергия ➤ {main[2]}
Локация ➤ {loc["name"]}
Дом ➤ {home}

Первородный элемент ➤ {main[3]}
Вторичный элемент ➤ {main[4]}
Истинный элемент ➤ {main[5]}
-----------------------------------------
Боевая статисика:

Телосложение:
Физ. база ➤ {fight[5]}
Макс. здоровье ➤ {fight[0]}
Регенерация ➤ {fight[2]}
Здоровье ➤ {fight[1]}
Уклонение ➤ {fight[3]}
Защита ➤ {fight[4]}
Шанс критического попадания ➤ {fight[7]}
Урон критического попадания ➤ {fight[8]}

Магия:
Маг. база ➤ {fight[6]}
Макс. количество маны ➤ {fight[9]}
Востоновление маны ➤ {fight[10]}
Мана ➤ {fight[11]}

Руны:
Заряды рунной для атаки: {equip[9]}

            _|( ◡‿◡ )|_  
-----------------------------------------
""")
        await message.answer(f"""
-----------------------------------------
Мастерство крафта ➤ {rp[1]}/15
Мастерство алхимии ➤ {rp[2]}/15

Удача ➤ {rp[9]}/100%
-----------------------------------------
Ролевая статистика:

Интеллект ➤ {rp[13]}/1000
Сила воли ➤ {rp[10]}/1000
Знание языков ➤ {rp[11]}/1000
Харизма ➤ {rp[0]}/1000
Сила ➤ {rp[3]}/1000
Скорость бега ➤ {rp[12]}/1000
Ловкость ➤ {rp[4]}/1000
Кража ➤ {rp[5]}/1000
Скрытность ➤ {rp[6]}/1000
Внимательность ➤ {rp[7]}/1000
Взлом ➤ {rp[8]}/1000    
-----------------------------------------
Очки навыков(магия) ➤ {point[0]}
Очки навыков(физ) ➤ {point[1]}
Очки навыков(Рп) ➤ {point[2]}
Очки навыков(Таланты) ➤ {point[3]}           
-----------------------------------------
Фракция ➤ {place[0]}
Тип бонуса фракции: {bonus_f} {text}
Репутация в фракции ➤ {place[1]}/100
Организация ➤ {party["name"]} 
Репутация в организации ➤ {place[3]}/100
-----------------------------------------
""")

    elif message.text == 'Инвентарь' or message.text == 'Инв':
        if inv[0] > 0:
            for slot1 in inventory.find({"number": (inv[0])}):
                print("Inv finder done")
            name_slot_1 = slot1['name']
            if slot1["Type"] == "оружие":
                name_slot_1 = invn[0]
        else:
            name_slot_1 = "Пусто"
        if inv[1] > 0:
            for slot2 in inventory.find({"number": (inv[1])}):
                print("Inv finder done")
            name_slot_2 = slot2['name']
            if slot2["Type"] == "оружие":
                name_slot_2 = invn[1]
        else:
            name_slot_2 = "Пусто"
        if inv[2] > 0:
            for slot3 in inventory.find({"number": (inv[2])}):
                print("Inv finder done")
            name_slot_3 = slot3['name']
            if slot3["Type"] == "оружие":
                name_slot_3 = invn[2]
        else:
            name_slot_3 = "Пусто"
        if inv[3] > 0:
            for slot4 in inventory.find({"number": (inv[3])}):
                print("Inv finder done")
            name_slot_4 = slot4['name']
            if slot4["Type"] == "оружие":
                name_slot_4 = invn[3]
        else:
            name_slot_4 = "Пусто"

        if inv[4] > 0:
            for slot5 in inventory.find({"number": (inv[4])}):
                print("Inv finder done")
            name_slot_5 = slot5['name']
            if slot5["Type"] == "оружие":
                name_slot_5 = invn[4]
        else:
            name_slot_5 = "Пусто"
        if inv[5] > 0:
            for slot6 in inventory.find({"number": (inv[5])}):
                print("Inv finder done")
            name_slot_6 = slot6['name']
            if slot6["Type"] == "оружие":
                name_slot_6 = invn[5]
        else:
            name_slot_6 = "Пусто"
        if inv[6] > 0:
            for slot7 in inventory.find({"number": (inv[6])}):
                print("Inv finder done")
            name_slot_7 = slot7['name']
            if slot7["Type"] == "оружие":
                name_slot_7 = invn[6]
        else:
            name_slot_7 = "Пусто"
        if inv[7] > 0:
            for slot8 in inventory.find({"number": (inv[7])}):
                print("Inv finder done")
            name_slot_8 = slot8['name']
            if slot8["Type"] == "оружие":
                name_slot_8 = invn[7]
        else:
            name_slot_8 = "Пусто"
        if inv[8] > 0:
            for slot9 in inventory.find({"number": (inv[8])}):
                print("Inv finder done")
            name_slot_9 = slot9['name']
            if slot9["Type"] == "оружие":
                name_slot_9 = invn[8]
        else:
            name_slot_9 = "Пусто"
        if inv[9] > 0:
            for slot10 in inventory.find({"number": (inv[9])}):
                print("Inv finder done")
            name_slot_10 = slot10['name']
            if slot10["Type"] == "оружие":
                name_slot_10 = invn[9]
        else:
            name_slot_10 = "Пусто"

        if equip[0] > 0:
            for rhand in inventory.find({"number": (equip[0])}):
                print("Inv finder done")
            name_rhand = rhand['name']
            if rhand["Type"] == "оружие":
                name_rhand = invn[10]
        else:
            name_rhand = "Пусто"
        if equip[1] > 0:
            for lhand in inventory.find({"number": (equip[1])}):
                print("Inv finder done")
            name_lhand = lhand['name']
            if lhand["Type"] == "оружие":
                name_lhand = invn[11]
        else:
            name_lhand = "Пусто"

        for armor in inventory.find({"number": (equip[2])}):
            print("Inv finder done")
        for amulet in inventory.find({"number": (equip[3])}):
            print("Inv finder done")
        for ring in inventory.find({"number": (equip[4])}):
            print("Inv finder done")
        for ring2 in inventory.find({"number": (equip[5])}):
            print("Inv finder done")
        for art in inventory.find({"number": (equip[6])}):
            print("Inv finder done")
        for art2 in inventory.find({"number": (equip[7])}):
            print("Inv finder done")
        for pet in inventory.find({"number": (equip[8])}):
            print("Inv finder done")

        await message.delete()
        await message.answer(f"""
-----------------------------------------
Имя ➤ {main[0]}   (◡‿◡) 
-----------------------------------------
Экипировка:
    Правая рука -➤ {name_rhand}
    Левая рука -➤ {name_lhand}
    Рунный камень 1 -➤ {art['name']} 
    Рунный камень 2 -➤ {art2['name']} 
    
    Броня -➤ {armor['name']} [в разработке]

    Амулет -➤ {amulet['name']} [в разработке] 
    Кольцо -➤ {ring['name']} [в разработке]
    Кольцо 2 -➤ {ring2['name']} [в разработке]
    
    Фамильяр -➤ {pet['name']} [в разработке]
-----------------------------------------
Рюкзак:
    1 -➤ {name_slot_1}
    2 -➤ {name_slot_2}
    3 -➤ {name_slot_3}
    4 -➤ {name_slot_4}
    5 -➤ {name_slot_5}
    6 -➤ {name_slot_6}
    7 -➤ {name_slot_7}
    8 -➤ {name_slot_8}
    9 -➤ {name_slot_9}
    10 -➤ {name_slot_10}
    Материалы -➤ {cur[0]} [в разработке]
    Бэсу  -➤ {cur[3]}
    Трава1 -➤ {cur[4]} [в разработке]
    Трава2 -➤ {cur[5]} [в разработке]
    Базовая магическая руда -➤ {cur[6]}
    Высшая магическая руда -➤ {cur[7]} [в разработке]
    Мифрил -➤ {cur[8]} [в разработке]
-----------------------------------------
Карманы:
    Золото -➤ {cur[1]}
-----------------------------------------
Особое:
    Коины -➤ {cur[2]}
-----------------------------------------
""")

    elif message.text == 'Техники':
        for tech1 in techniques.find({"num": mag[0]}):
            print("Inv finder done")
        for tech2 in techniques.find({"num": mag[1]}):
            print("Inv finder done")
        for tech3 in techniques.find({"num": mag[2]}):
            print("Inv finder done")
        for tech4 in techniques.find({"num": mag[3]}):
            print("Inv finder done")
        for tech5 in techniques.find({"num": mag[4]}):
            print("Inv finder done")
        for tech6 in techniques.find({"num": mag[5]}):
            print("Inv finder done")
        for tech7 in techniques.find({"num": mag[6]}):
            print("Inv finder done")
        for tech8 in techniques.find({"num": mag[7]}):
            print("Inv finder done")
        for tech9 in techniques.find({"num": mag[8]}):
            print("Inv finder done")
        for tech10 in techniques.find({"num": mag[9]}):
            print("Inv finder done")
        for tech11 in techniques.find({"num": mag[10]}):
            print("Inv finder done")
        for tech12 in techniques.find({"num": mag[11]}):
            print("Inv finder done")
        for tech13 in techniques.find({"num": mag[12]}):
            print("Inv finder done")
        for tech14 in techniques.find({"num": mag[13]}):
            print("Inv finder done")
        for tech15 in techniques.find({"num": mag[14]}):
            print("Inv finder done")
        for tech16 in techniques.find({"num": mag[15]}):
            print("Inv finder done")
        for tech17 in techniques.find({"num": mag[16]}):
            print("Inv finder done")
        for tech18 in techniques.find({"num": mag[17]}):
            print("Inv finder done")
        for tech19 in techniques.find({"num": mag[18]}):
            print("Inv finder done")
        for tech20 in techniques.find({"num": mag[19]}):
            print("Inv finder done")
        await message.delete()
        await message.answer(f"""
-----------------------------------------
Имя ➤ {main[0]}   (◡‿◡) 
-----------------------------------------
Техника #1 -➤ {tech1["name"]}
Техника #2 -➤ {tech2["name"]}
Техника #3 -➤ {tech3["name"]}
Техника #4 -➤ {tech4["name"]}
Техника #5 -➤ {tech5["name"]}
Техника #6 -➤ {tech6["name"]}
Техника #7 -➤ {tech7["name"]}
Техника #8 -➤ {tech8["name"]} 
Техника #9 -➤ {tech9["name"]}
Техника #10 -➤ {tech10["name"]}  
Техника #11 -➤ {tech11["name"]}  
Техника #12 -➤ {tech12["name"]}  
Техника #13 -➤ {tech13["name"]}  
Техника #14 -➤ {tech14["name"]}  
Техника #15 -➤ {tech15["name"]}  
Техника #16 -➤ {tech16["name"]}  
Техника #17 -➤ {tech17["name"]}  
Техника #18 -➤ {tech18["name"]}  
Техника #19 -➤ {tech19["name"]}  
Техника #20 -➤ {tech20["name"]}  
----------------------------------------- 
""")

    elif message.text == "Статус":
        if con2[0] >= 1:
            front = "присутствует"
        else:
            front = "отсутствует"
        if con2[1] >= 1:
            front2 = "присутствует"
        else:
            front2 = "отсутствует"
        if con[13] >= 1:
            front3 = "присутствует"
        else:
            front3 = "отсутствует"
        if con[15] >= 1:
            front4 = "присутствует"
        else:
            front4 = "отсутствует"
        await message.answer(f"""
-----------------------------------------
Имя ➤ {main[0]}   (◡‿◡) 
-----------------------------------------
Голод -➤ {con2[7]}/100[в разработке]
Жажда -➤ {con2[8]}/100[в разработке]
Температура -➤ {con2[9]}/100[в разработке]

Действующий статус -➤ {con[0]}

Активная техника покрытия -➤ {front} ({con2[0]})
Действующий модификатор макс. хп  -➤ {con[1]}
Действующий модификатор регенерации -➤ {con[2]}
Действующий модификатор уклонения -➤ {con[3]}
Действующий модификатор защиты  -➤ {con[4]}
Действующий модификатор физ. базы -➤ {con[5]} 
Действующий модификатор маг. базы -➤ {con[6]} 
Действующий модификатор крит шанса -➤ {con[7]}
Действующий модификатор крит урона -➤ {con[8]} 
Действующий модификатор макс. маны -➤ {con[9]}
Действующий модификатор регенерации маны -➤ {con[10]}

Активная усиления оружия -➤ {front2} ({con2[1]})
Действующий модификатор урона оружия в правой руке -➤ {con[11]}
Действующий модификатор урона оружия в левой руке -➤ {con[12]}

Активная техника защиты -➤ {front3}({con[13]})
Действующий модификатор активной техники защиты -➤ {con[14]}

Активная техника контроля -➤ {front4} ({con[15]})
Действующий модификатор регенерации -➤ {con2[2]}
Действующий модификатор уклонения -➤ {con2[3]}
Действующий модификатор защиты  -➤ {con2[4]}
Действующий модификатор крит шанса -➤ {con2[5]}
Действующий модификатор регенерации маны -➤ {con2[6]}

""")

    elif message.text == "Прорваться":
        level_up = lvl_up.Pumping.lvl_up(uid)
        if level_up is True:
            await message.answer("Вы успешно прорвались на новый уровень")
        else:
            await message.answer("Недостаточно энергии")

    elif message.text == "Отдых":
        await message.answer("Вы успешно отдохнули!")
        hp = fight[1] + fight[2]
        mana = fight[11] + fight[10]
        maxHp = fight[0]
        maxMana = fight[9]
        players.update_one({"_id": uid}, {"$set": {"rune_charge": 5}})
        if maxHp > hp:
            players.update_one({"_id": uid}, {"$set": {"Hp": hp}})
            if maxMana > mana:
                players.update_one({"_id": uid}, {"$set": {"mana": mana}})
            else:
                players.update_one({"_id": uid}, {"$set": {"mana": maxMana}})
        else:
            players.update_one({"_id": uid}, {"$set": {"Hp": maxHp}})

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
