from mongodb import Finder as mongodb
from aiogram import types, Dispatcher
from pymongo import MongoClient
import random

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

class Pumping:
    def __init__(self, uid):
        self.uid = uid

    def lvl_up(uid):
        main = mongodb.findUserMainByID(uid)
        point = mongodb.findUserPointByID(uid)
        nlevel = main[1] + 1
        for cult in levels.find({"number": nlevel}):
            print("Cult finder done")
        check = main[2] - cult['cost']
        if main[2] <= cult['cost'] or check <= 0:
            return False
        else:
            players.update_one({"_id": uid}, {
                "$set": {"energy": main[2] - cult['cost']}})
            players.update_one({"_id": uid}, {
                "$set": {"level": main[1] + 1}})
            players.update_one({"_id": uid}, {
                "$set": {"magic_points": point[0] + 500}})
            players.update_one({"_id": uid}, {
                "$set": {"talent_point": point[3] + 1}})
            return True

    def check_swap1(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[3]
        if level != 'отсутствует':
            return False
        else:
            return True

    def check_swap2(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[4]
        if level != 'отсутствует':
            return False
        else:
            return True

    def check_swap3(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[5]
        if level != 'отсутствует':
            return False
        else:
            return True

    def check_element1(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[1]
        if level >= 10:
            return True
        else:
            return False

    def check_element2(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[1]
        if level >= 22:
            return True
        else:
            return False

    def check_element3(uid):
        main = mongodb.findUserMainByID(uid)
        level = main[1]
        if level >= 25:
            return True
        else:
            return False

    def check_true_element(el):
        if el == "Огонь" or el == "огонь":
            return True
        elif el == "Вода" or el == "вода":
            return True
        elif el == "Земля" or el == "земля":
            return True
        elif el == "Воздух" or el == "воздух":
            return True
        else:
            return False

    def find_final_el(uid):
        main = mongodb.findUserMainByID(uid)
        el1 = main[3]
        el2 = main[4]
        if el1 == "Огонь" or el1 == "огонь":
            if el2 == "Огонь" or el2 == "огонь":
                el3 = "Солнце"
            if el2 == "Вода" or el2 == "вода":
                el3 = "пар"
            if el2 == "Земля" or el2 == "земля":
                el3 = "лава"
            if el2 == "Воздух" or el2 == "воздух":
                el3 = "Молния"
        elif el1 == "Вода" or el1 == "вода":
            if el2 == "Огонь" or el2 == "огонь":
                el3 = "пар"
            if el2 == "Вода" or el2 == "вода":
                el3 = "Кровь"
            if el2 == "Земля" or el2 == "земля":
                el3 = "дерево"
            if el2 == "Воздух" or el2 == "воздух":
                el3 = "лёд"
        elif el1 == "Земля" or el1 == "земля":
            if el2 == "Огонь" or el2 == "огонь":
                el3 = "лава"
            if el2 == "Вода" or el2 == "вода":
                el3 = "дерево"
            if el2 == "Земля" or el2 == "земля":
                el3 = "Нефрит"
            if el2 == "Воздух" or el2 == "воздух":
                el3 = "песок"
        elif el1 == "Воздух" or el1 == "воздух":
            if el2 == "Огонь" or el2 == "огонь":
                el3 = "молния"
            if el2 == "Вода" or el2 == "вода":
                el3 = "лёд"
            if el2 == "Земля" or el2 == "земля":
                el3 = "песок"
            if el2 == "Воздух" or el2 == "воздух":
                el3 = "Гравитация"
        return [True, el3]



# @dp.message_handler(commands='Прокачать_магию')
async def magicupp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    stat = str(getter[0])
    how = int(getter[1])
    fight = mongodb.findUserFightByID(uid)
    point = mongodb.findUserPointByID(uid)
    have_magic_points = point[0]
    check = have_magic_points - how
    if point[0] < how or check < 0:
        await message.answer('Недостаточно очков навыков(маг)!')
    else:
        if point[0] >= 5 and how >= 5:
            if stat == "маг_база":
                have_magic_damage = fight[6]
                how1 = how / 100
                results_magic_damage = have_magic_damage + how1
                if results_magic_damage <= 100:
                    players.update_one({"_id": uid}, {"$set": {"magic_damage": results_magic_damage}})
                    players.update_one({"_id": uid}, {"$set": {"magic_points": have_magic_points - how}})
                    await message.answer(
                        f"Вы успешно улучшили {stat}! \n Новый уровень магической базы - {results_magic_damage}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень магической базы - 150 ")
            elif stat == "макс_мана":
                have_max_mana = fight[9]
                how1 = how / 5
                results_max_mana = have_max_mana + how1
                if results_max_mana <= 2000:
                    players.update_one({"_id": uid}, {"$set": {"max_mana": results_max_mana}})
                    players.update_one({"_id": uid}, {"$set": {"mana": results_max_mana}})
                    players.update_one({"_id": uid}, {"$set": {"magic_points": have_magic_points - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новый уровень максимальной маны - {results_max_mana}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень маны - 2000 ")
            elif stat == "регенерация_маны":
                have_regeneration_mana = fight[10]
                how1 = how / 5
                results_regeneration_mana = have_regeneration_mana + how1
                if results_regeneration_mana <= 500:
                    players.update_one({"_id": uid}, {"$set": {"regeneration_mana": results_regeneration_mana}})
                    players.update_one({"_id": uid}, {"$set": {"magic_points": have_magic_points - how}})
                await message.answer(
                    f"Вы успешно улучшили {stat}! \n Новый уровень регенерации маны - {results_regeneration_mana}")
            else:
                await message.answer("Слишком большой результат! \n Максимальный уровень регенерации маны - 200 ")
        else:
            await message.answer(f"Минимальное количество очков для прокачки : 5")

# @dp.message_handler(commands='Прокачать_физу')
async def fizupp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    stat = str(getter[0])
    how = int(getter[1])
    fight = mongodb.findUserFightByID(uid)
    point = mongodb.findUserPointByID(uid)
    have_physical_points = point[1]
    check_2 = have_physical_points - how
    if point[1] < how or check_2 < 0:
        await message.answer('Недостаточно очков навыков(физ)!')
    else:
        if point[1] >= 5 and how >= 5:
            if stat == "макс_хп":
                have_max_hp = fight[0]
                just_hp = fight[1]
                how1 = how * 2
                results_hp = have_max_hp + how1
                if results_hp <= 2000:
                    players.update_one({"_id": uid}, {"$set": {"MaxHp": results_hp}})
                    players.update_one({"_id": uid}, {"$set": {"Hp": just_hp + how1 }})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новый уровень HP - {results_hp}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень HP - 2000 ")
            elif stat == "регенерация":
                have_regeneration = fight[2]
                how1 = how / 2
                results_regeneration = have_regeneration + how1
                if results_regeneration <= 500:
                    players.update_one({"_id": uid}, {"$set": {"regeneration": results_regeneration}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новый уровень регенерации - {results_regeneration}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень регенерации - 500 ")
            elif stat == "ловкость":
                have_dexterity = fight[3]
                how1 = how / 10
                results_dexterity = have_dexterity + how1
                if results_dexterity <= 50:
                    players.update_one({"_id": uid}, {"$set": {"dexterity": results_dexterity}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новый уровень ловкости - {results_dexterity}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень ловкости - 50% ")
            elif stat == "защита":
                have_defense = fight[4]
                how1 = how / 10
                results_defense = have_defense + how1
                if results_defense <= 50:
                    players.update_one({"_id": uid}, {"$set": {"defense": results_defense}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новый уровень защиты - {results_defense}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень защиты - 50% ")
            elif stat == "физ_база":
                have_physical_damage = fight[5]
                how1 = how / 20
                results_physical_damage = have_physical_damage + how1
                if results_physical_damage <= 200:
                    players.update_one({"_id": uid}, {"$set": {"physical_damage": results_physical_damage}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(
                        f"Вы успешно улучшили {stat}!\n Новый уровень физ. базы - {results_physical_damage}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень физ. базы - 200 ")
            elif stat == "шанс_крита":
                have_Krit_Chance = fight[7]
                how1 = how / 10
                results_Krit_Chance = have_Krit_Chance + how1
                if results_Krit_Chance <= 100:
                    players.update_one({"_id": uid}, {"$set": {"Krit_Chance": results_Krit_Chance}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(
                        f"Вы успешно улучшили {stat}!\n Новый уровень шанса крита - {results_Krit_Chance}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень шанса крита - 100% ")
            elif stat == "урон_крита":
                have_Krit_damage = fight[8]
                how1 = how / 20
                results_Krit_damage = have_Krit_damage + how1
                if results_Krit_damage <= 200:
                    players.update_one({"_id": uid}, {"$set": {"Krit_damage": results_Krit_damage}})
                    players.update_one({"_id": uid}, {"$set": {"physical_points": have_physical_points - how}})
                    await message.answer(
                        f"Вы успешно улучшили {stat}!\n Новый уровень урона крита - {results_Krit_damage}")
                else:
                    await message.answer("Слишком большой результат! \n Максимальный уровень урона крита - 200% ")
        else:
            await message.answer(f"Минимальное количество очков для прокачки : 5")


# @dp.message_handler(commands='Прокачать_навыки')
async def rpupp(message: types.Message):
    uid = message.from_user.id
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    stat = str(getter[0])
    how = int(getter[1])
    rp = mongodb.findUserRpByID(uid)
    point = mongodb.findUserPointByID(uid)
    rp_point = point[2]
    check_2 = rp_point - how
    if point[2] < how or check_2 < 0:
        await message.answer('Недостаточно очков навыков(физ)!')
    else:
        if point[2] >= 5 and how >= 5:
            if stat == "харизма" or stat == "Харизма":
                have = rp[0]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_charisma": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "cила" or stat == "Сила":
                have = rp[3]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_strength": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "ловкость" or stat == "Ловкость":
                have = rp[4]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_dexterity": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "кража" or stat == "Кража":
                have = rp[5]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_theft": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "скрытность" or stat == "Скрытность":
                have = rp[6]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_stealth": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "внимательность" or stat == "Внимательность":
                have = rp[7]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_attentiveness": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "взлом" or stat == "Взлом":
                have = rp[8]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_hacking": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "сила_воли" or stat == "Сила_воли":
                have = rp[10]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_willpower": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "знание_языков" or stat == "Знание_языков":
                have = rp[11]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_language": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "Скорость_бега" or stat == "скорость_бега":
                have = rp[12]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_speed": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
            if stat == "Интеллект" or stat == "интеллект":
                have = rp[13]
                results = have + how
                if results <= 1000:
                    players.update_one({"_id": uid}, {"$set": {"rp_intelligence": results}})
                    players.update_one({"_id": uid}, {"$set": {"rp_point": rp_point - how}})
                    await message.answer(f"Вы успешно улучшили {stat}! \n Новое значение - {results}")
                else:
                    await message.answer(f'Слишком большой результат! \n Максимальный уровень навыка "{stat}" - 1000 ')
        else:
            await message.answer(f"Минимальное количество очков для прокачки : 5")



# @dp.message_handler(commands='Выбрать_первородный_элемент')
async def first_element(message: types.Message):
    uid = message.from_user.id
    el = message.get_args()
    check = Pumping.check_element1(uid)
    if check is True:
        check3 = Pumping.check_swap1(uid)
        if check3 is True:
            check2 = Pumping.check_true_element(el)
            if check2 is True:
                players.update_one({"_id": uid}, {"$set": {"first_element": el}})
                await message.answer(
                    f'Вы выбрали элемент {el} !\n Уже не терпится изучить все техники?')
            else:
                await message.answer(
                    f'Значение {el} не принимается.\n Пример команды:\n /Выбрать_первородный_элемент огонь')
        else:
            await message.answer('Вы уже выбрали элемент!')
    elif check is False:
        await message.answer('У вас недостаточный уровень!')


# @dp.message_handler(commands='Выбрать_вторичный_элемент')
async def second_element(message: types.Message):
    uid = message.from_user.id
    el = message.get_args()
    check = Pumping.check_element2(uid)
    if check is True:
        check3 = Pumping.check_swap2(uid)
        if check3 is True:
            check2 = Pumping.check_true_element(el)
            if check2 is True:
                players.update_one({"_id": uid}, {"$set": {"second_element": el}})
                await message.answer(
                    f'Вы выбрали элемент {el} !\n Уже не терпится изучить все техники?')
            else:
                await message.answer(
                    f'Значение {el} не принимается.\n Пример команды:\n /Выбрать_вторичный_элемент огонь')
        else:
            await message.answer('Вы уже выбрали элемент!')
    elif check is False:
        await message.answer('У вас недостаточный уровень!')


# @dp.message_handler(commands='Пробудить_истинный_элемент')
async def final_element(message: types.Message):
    uid = message.from_user.id
    check = Pumping.check_element3(uid)
    if check is True:
        check2 = Pumping.check_swap3(uid)
        if check2 is True:
            element3 = Pumping.find_final_el(uid)
            if element3[0] is True:
                el3 = element3[1]
                players.update_one({"_id": uid}, {"$set": {"final_element": el3}})
                await message.answer(f'Вы пробудили истинный элемент "{el3}!"')
            else:
                await message.answer(f'Что то пошло не так... обратитесь к админу что бы устранить баг.')
        else:
            await message.answer('Вы уже выбрали элемент!')
    elif check is False:
        await message.answer('У вас недостаточный уровень!')


# @dp.message_handler(commands='try')
async def roll(message: types.Message):
    r = random.randint(1,100)
    what = str(message.get_args())
    await message.answer(f"Вы попытались {what},"
                         f" результат броска - {r}/100!")


def register_handlers_lvl_up(dp: Dispatcher):
    dp.register_message_handler(magicupp, commands='Прокачать_магию')
    dp.register_message_handler(fizupp, commands='Прокачать_физу')
    dp.register_message_handler(first_element, commands='Выбрать_первородный_элемент')
    dp.register_message_handler(second_element, commands='Выбрать_вторичный_элемент')
    dp.register_message_handler(final_element, commands='Пробудить_истинный_элемент')
    dp.register_message_handler(rpupp, commands='Прокачать_навыки')
    dp.register_message_handler(roll, commands='try')

