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


class Finder:

    def __init__(self, uid):
        self.uid = uid

    def findUserParamByID(uid):
        for player in players.find({"_id": uid}):
            pid = player['_id']
            return pid

    def findUserIDByName(name):
        for player in players.find({"name": name}):
            return [player["_id"]]

    def findClanByID(num):
        for player in clans.find({"num": num}):
            return [player["_id"]]


    def findUserMainByID(uid):
        for player in players.find({"_id": uid}):
            return [player["name"], player["level"], player["energy"], player["first_element"], player["second_element"], player["final_element"]]

    def findUserFightByID(uid):
        for player in players.find({"_id": uid}):
            return [player["MaxHp"], player["Hp"], player["regeneration"], player["dexterity"], player["defense"],
                    player["physical_damage"], player["magic_damage"], player["Krit_Chance"], player["Krit_damage"],
                    player["max_mana"], player["regeneration_mana"], player["mana"]]

    def findUserConditionByID(uid):
        for player in players.find({"_id": uid}):
            return [player["condition"],
                    player["buf_hp"], player["buf_hp_reg"], player["buf_dex"], player["buf_def"],
                    player["buf_fiz_dmg"], player["buf_mag_dmg"],player["buf_k_c"], player["buf_k_dmg"],
                    player["buf_mana"], player["buf_mana_reg"], player["buf_rh"], player["buf_lh"],
                    player["active_def"], player["buf_active_def"], player['active_control']]

    def findUserCondition2ByID(uid):
        for player in players.find({"_id": uid}):
            return [player['active_coverage'], player['active_gain'], player['debuf_hp_reg'], player['debuf_dex'], player['debuf_def'],
                    player['debuf_k_c'], player['debuf_mana_reg'], player["hunger"],player["thirst"],player["cold"]]

    def findUserPointByID(uid):
        for player in players.find({"_id": uid}):
            return [player["magic_points"], player["physical_points"], player["rp_point"], player["talent_point"]]

    def findUserRpByID(uid):
        for player in players.find({"_id": uid}):
            return [player["rp_charisma"],
                    player["rp_kraft_skill"], player["rp_alchemy_skill"], player["rp_strength"], player["rp_dexterity"],
                    player["rp_theft"], player["rp_stealth"], player["rp_attentiveness"], player["rp_hacking"],
                    player["rp_luck"], player["rp_willpower"], player["rp_language"], player["rp_speed"],
                    player["rp_intelligence"]]

    def findUserAdminByID(uid):
        for player in players.find({"_id": uid}):
            return [player["Game_Master"], player["Helper"], player["Moderator"], player["Admin"]]

    def findUserEquipmentByID(uid):
        for player in players.find({"_id": uid}):
            return [player["right_hand"], player["left_hand"], player["armor"], player["amulet"], player["ring1"],
                    player["ring2"], player["accessory1"], player["accessory2"], player["pet"], player["rune_charge"]]

    def findUserInventoryByID(uid):
        for player in players.find({"_id": uid}):
            return [player["slot1"], player["slot2"], player["slot3"], player["slot4"], player["slot5"], player["slot6"],
                    player["slot7"], player["slot8"], player["slot9"], player["slot10"]]

    def findUserCurrencyByID(uid):
        for player in players.find({"_id": uid}):
            return [player["material"], player["gold"], player["coin"], player["grass"], player["grass2"], player["grass3"],
                    player["iron"], player["iron2"], player["iron3"], player["home"]]

    def findUserPlaceByID(uid):
        for player in players.find({"_id": uid}):
            return [player["fraction"], player["fraction_respect"], player["guild"], player["guild_respect"],
                    player["location"], player["fraction_bonus_type"], player["fraction_bonus"]]

    def findUserMagicByID(uid):
        for player in players.find({"_id": uid}):
            return [player["technique1"], player["technique2"], player["technique3"], player["technique4"], player["technique5"],
                    player["technique6"], player["technique7"], player["technique8"], player["technique9"], player["technique10"],
                    player["technique11"], player["technique12"], player["technique13"], player["technique14"], player["technique15"],
                    player["technique16"], player["technique17"], player["technique18"], player["technique19"], player["technique20"]]

    def findUserEnemyByID(uid):
        for player in players.find({"_id": uid}):
            return [player["enemy1"], player["enemy2"], player["enemy3"], player["enemy4"], player["enemy5"]]

    def findUserInventoryNameByID(uid):
        for player in players.find({"_id": uid}):
            return [player["nw_slot1"], player["nw_slot2"],player["nw_slot3"],player["nw_slot4"],player["nw_slot5"],
                    player["nw_slot6"],player["nw_slot7"],player["nw_slot8"],player["nw_slot9"],player["nw_slot10"],
                    player["nw_right_hand"],player["nw_left_hand"]]

    def findUserVersionByID(uid):
        for player in players.find({"_id": uid}):
            return [player["version"]]
