import random
from aiogram.dispatcher.filters.state import State, StatesGroup


def randrange_float(start, stop, step):
    return random.randint(0, int((stop - start) / step)) * step + start

def get_strength():
    return randrange_float(2.00, 6.00, 0.5)


def get_regeneration():
    return randrange_float(1.00, 10.00, 0.5)


class Hero(StatesGroup):

    # Основная инфа
    name = State()
    level = 1
    energy = 0
    first_element = 'отсутствует'
    second_element = 'отсутствует'
    final_element = 'отсутствует'

    # боевые характеристики
    MaxHp = 50.00
    Hp = 50.00
    regeneration = get_regeneration()
    dexterity = 5.00
    defense = 0.00
    physical_damage = get_strength()
    magic_damage = 0.00
    Krit_Chance = 0.00
    Krit_damage = 0.00
    max_mana = 0.00
    regeneration_mana = 0.00
    mana = 0.00

    #действующие бафы
    condition = 0

    active_coverage = 0
    buf_hp = 0
    buf_hp_reg = 0
    buf_dex = 0
    buf_def = 0
    buf_fiz_dmg = 0
    buf_mag_dmg = 0
    buf_k_c = 0
    buf_k_dmg = 0
    buf_mana = 0
    buf_mana_reg = 0

    buf_active_def = 0
    active_def = 0

    active_control = 0
    debuf_hp_reg = 0
    debuf_dex = 0
    debuf_def = 0
    debuf_k_c = 0
    debuf_mana_reg = 0

    active_gain = 0
    buf_rh = 0
    buf_lh = 0

    # типы поинтов для прокачки
    magic_points = 0
    physical_points = 0
    rp_point = 5
    talent_point = 0

    # Ролевые характеристики
    rp_charisma = 1
    rp_kraft_skill = 0
    rp_alchemy_skill = 0
    rp_strength = 0
    rp_dexterity = 0
    rp_theft = 0
    rp_stealth = 0
    rp_attentiveness = 0
    rp_hacking = 0

    # Информация о правах
    Game_Master = False
    Helper = False
    Moderator = False
    Admin = False

    # Экипировка
    right_hand = 0
    left_hand = 0
    armor = 0

    amulet = 0
    ring1 = 0
    ring2 = 0
    accessory1 = 0
    accessory2 = 0
    pet = 0


    # Рюкзак
    slot1 = 0
    slot2 = 0
    slot3 = 0
    slot4 = 0
    slot5 = 0
    slot6 = 0
    slot7 = 0
    slot8 = 0
    slot9 = 0
    slot10 = 0

    # Валюта и расходники
    material = 0
    gold = 0
    coin = 0
    grass = 0
    grass2 = 0
    grass3 = 0
    iron = 0
    iron2 = 0
    iron3 = 0

    # Сторона
    fraction = 0
    fraction_respect = 0
    guild = 0
    guild_respect = 0
    location = 0

    # Способности
    technique1 = 0
    technique2 = 0
    technique3 = 0
    technique4 = 0
    technique5 = 0
    technique6 = 0
    technique7 = 0
    technique8 = 0
    technique9 = 0
    technique10 = 0
    technique11 = 0
    technique12 = 0
    technique13 = 0
    technique14 = 0
    technique15 = 0
    technique16 = 0
    technique17 = 0
    technique18 = 0
    technique19 = 0
    technique20 = 0

    # нынешний враг
    enemy1 = 0
    enemy2 = 0
    enemy3 = 0
    enemy4 = 0
    enemy5 = 0


