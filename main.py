import random


# Fighter Class

class Fighter:
    def __init__(self, id, first_name, surname, gender, nation, fighting_out, style, age, weight, height, strength,
                 speed,
                 endurance,
                 sub_offence, sub_defence, win, lost, champion):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.gender = gender
        self.nation = nation
        self.fighting_out = fighting_out
        self.style = style
        self._age = age
        self.weight = weight
        self.height = height
        self.strength = strength
        self.speed = speed
        self.endurance = endurance
        self.sub_offence = sub_offence
        self.sub_defence = sub_defence
        self.win = win
        self.lost = lost
        self.champion = champion

    # Getters

    def get_id(self):
        return self.id

    def get_name(self):
        return self.first_name + " " + self.surname

    def get_gender(self):
        return self.gender

    def get_nation(self):
        return self.nation

    def get_fighting_out(self):
        return self.fighting_out

    def get_style(self):
        return self.style

    def get_age(self):
        return self._age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_strength(self):
        return self.strength

    def get_speed(self):
        return self.speed

    def get_endurance(self):
        return self.endurance

    def get_sub_offence(self):
        return self.sub_offence

    def get_sub_defence(self):
        return self.sub_defence

    def get_wins(self):
        return self.win

    def get_losses(self):
        return self.lost

    def get_champion(self):
        return self.champion

    # Setters

    def set_strength(self, x):
        self.strength = x

    def set_endurance(self, x):
        self.endurance = x

    def set_speed(self, x):
        self.speed = x

    def set_sub_offence(self, x):
        self.subOff = x

    def set_sub_defence(self, x):
        self.subdef = x

    def set_wins(self, x):
        self.win = x

    def set_losses(self, x):
        self.lost = x

    def set_champion(self, x):
        self.champion = x


# Algorithmic Functions

def game_maths(probability_of_success):
    return random.randint(0, 100) < (probability_of_success * 100)  # Calculates a random change based on a given input


def fight_function(fighter_list, fighter_one, fighter_two):
    # Fighter Attributes

    fighter_one_name = (fighter_list[fighter_one].get_name())
    fighter_two_name = (fighter_list[fighter_two].get_name())

    fighter_one_champion = (fighter_list[fighter_one].get_champion())  # New Addition if Check is Fighter is a champion
    fighter_two_champion = (fighter_list[fighter_two].get_champion())

    fighter_one_wins = (fighter_list[fighter_one].get_wins())
    fighter_two_wins = (fighter_list[fighter_two].get_wins())

    fighter_one_losses = (fighter_list[fighter_one].get_losses())
    fighter_two_losses = (fighter_list[fighter_two].get_losses())

    fighter_one_strength = (fighter_list[fighter_one].get_strength())
    fighter_two_strength = (fighter_list[fighter_two].get_strength())

    fighter_one_endurance = (fighter_list[fighter_one].get_endurance())
    fighter_two_endurance = (fighter_list[fighter_two].get_endurance())

    fighter_one_sub_offence = (fighter_list[fighter_one].get_sub_offence())
    fighter_two_sub_offence = (fighter_list[fighter_two].get_sub_offence())

    fighter_one_sub_defence = (fighter_list[fighter_one].get_sub_defence())
    fighter_two_sub_defence = (fighter_list[fighter_two].get_sub_defence())

    fighter_one_hp = 100 + fighter_one_endurance
    fighter_two_hp = 100 + fighter_two_endurance

    fighter_one_ap = 100 + fighter_one_strength / 10
    fighter_two_ap = 100 + fighter_two_strength / 10

    fighter_one_speed = (fighter_list[fighter_one].get_speed())
    fighter_one_speed = fighter_one_speed / 100 / 5

    fighter_two_speed = (fighter_list[fighter_two].get_speed())
    fighter_two_speed = fighter_two_speed / 100 / 5

    # Fight Variables

    fight_over = False
    roundsPassed = 1

    if fighter_list[fighter_one].get_weight() >= 93 or fighter_list[fighter_one].get_weight() <= 120 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Heavyweight"
    elif fighter_list[fighter_one].get_weight() >= 84 or fighter_list[fighter_one].get_weight() <= 92 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Light Heavyweight"
    elif fighter_list[fighter_one].get_weight() >= 77 or fighter_list[fighter_one].get_weight() <= 83 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Middleweight"
    elif fighter_list[fighter_one].get_weight() >= 70 or fighter_list[fighter_one].get_weight() <= 76 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Welterweight"
    elif fighter_list[fighter_one].get_weight() >= 66 or fighter_list[fighter_one].get_weight() <= 69 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Lightweight"
    elif fighter_list[fighter_one].get_weight() >= 61 or fighter_list[fighter_one].get_weight() <= 65 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Featherweight"
    elif fighter_list[fighter_one].get_weight() >= 57 or fighter_list[fighter_one].get_weight() <= 60 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Bantamweight"
    elif fighter_list[fighter_one].get_weight() >= 52 or fighter_list[fighter_one].get_weight() <= 56 and fighter_list[
        fighter_one].get_gender() == "Male":
        weightclass = "Flyweight"
    elif fighter_list[fighter_one].get_weight() >= 61 or fighter_list[fighter_one].get_weight() <= 66 and fighter_list[
        fighter_one].get_gender() == "Female":
        weightclass = "Featherweight"
    elif fighter_list[fighter_one].get_weight() >= 57 or fighter_list[fighter_one].get_weight() <= 60 and fighter_list[
        fighter_one].get_gender() == "Female":
        weightclass = "Bantamweight"
    elif fighter_list[fighter_one].get_weight() >= 52 or fighter_list[fighter_one].get_weight() <= 56 and fighter_list[
        fighter_one].get_gender() == "Female":
        weightclass = "Flyweight"
    elif fighter_list[fighter_one].get_weight() >= 0 or fighter_list[fighter_one].get_weight() <= 51 and fighter_list[
        fighter_one].get_gender() == "Female":
        weightclass = "Strawweight"

    if fighter_one_champion | fighter_two_champion == True:
        # If any fighter is a champion, fight rounds is changed
        # from 3 to 5
        rounds = 5
        print("Championship")
    else:
        rounds = 3
        print("Normal Bout")

    while fighter_one_hp > 0 and fighter_two_hp > 0 and roundsPassed != rounds or roundsPassed < rounds and fight_over != True:  # While fighters still
        # have health and fight is not over

        match game_maths(0.10):  # 0.10% chance of submission takedown
            case True:
                if fighter_one_sub_offence > fighter_two_sub_defence:  # if the selected player's offence is more than defence then
                    match game_maths(0.25):  # 0.25% chance of take down
                        case True:
                            print(fighter_one_name + " takes down " + fighter_two_name)
                            fighter_two_hp = fighter_two_hp - fighter_one_sub_offence  # Second fighter's health is reduced by first fighter's submission offence
                else:
                    match game_maths(
                        0.10):  # If Fighter two's defence is higher than fighter one's sub offence, then takedown attempt has a 0.10% chance of success
                        case True:
                            print(fighter_one_name + " takes downs " + fighter_two_name)
                            fighter_two_hp = fighter_two_hp - fighter_one_sub_offence  # Second fighter's health is reduced by first fighter's submission offence

                if fighter_two_hp <= 0 and fighter_two_champion:
                    print(fighter_two_name + "taps out! \n")
                    fighter_list.append(fighter_list[fighter_two].set_champion(False))
                    fighter_list.append(fighter_list[fighter_one].set_champion(True))
                    fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                    fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                    print(
                        "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at four "
                        "minutes, four seconds \n of round number ", roundsPassed, "\n declaring the winner \n by "
                                                                                   "submission \n ANNNND NEW AFC "
                                                                                   "Undisputed " + weightclass +
                                                                                   " champion of the world! " + fighter_one_name)  # Inspired by recent champion as of late 2022 ;)
                    fight_over = True
                    break
                if fighter_two_hp <= 0 and fighter_one_champion == true:
                    print(fighter_two_name + " taps out! \n")
                    fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                    fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                    print(
                        "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at two minutes, thirty-five seconds of round number ",
                        roundsPassed, "\n declaring the winner \n by submission \n" + fighter_one_name)
                    fight_over = True
                    break
                # game_menu(fighter_list)

            case False:
                if fighter_two_sub_offence > fighter_one_sub_defence:  # if the selected player's offence is more than defence then
                    match game_maths(0.25):  # 0.25% chance of take down
                        case True:
                            print(fighter_two_name + " takes down and attempts to submit: " + fighter_one_name)
                            fighter_one_hp = fighter_one_hp - fighter_two_sub_offence  # Second fighter's health is reduced by first fighter's submission offence
                else:
                    match game_maths(
                        0.10):  # If Fighter one's defence is higher than fighter two's sub offence, then takedown attempt has a 0.10% chance of success
                        case True:
                            print(fighter_two_name + " takes down and attempts to submit: " + fighter_one_name)
                            fighter_one_hp = fighter_one_hp - fighter_two_sub_offence  # Second fighter's health is reduced by first fighter's submission offence

                if fighter_one_hp <= 0 and fighter_one_champion:
                    print(fighter_one_name + " taps out! \n")
                    fight_over = True
                    fighter_list.append(fighter_list[fighter_one].set_champion(False))
                    fighter_list.append(fighter_list[fighter_two].set_champion(True))
                    fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                    fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                    print(
                        "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at four "
                        "minutes, four seconds \n of round number ", roundsPassed, "\n declaring the winner \n by "
                                                                                   "submission \n ANNNND NEW AFC "
                                                                                   "Undisputed " + weightclass +
                                                                                   " champion of the world! " + fighter_two_name)  # Inspired by recent champion as of late 2022 ;)
                elif fighter_one_hp <= 0 and fighter_two_champion:
                    print(fighter_one_name + " taps out! \n")
                    fight_over = True
                    fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                    fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                    print(
                        "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at one minutes, thirty-five seconds of round number ",
                        roundsPassed, "\n declaring the winner \n by submission \n" + fighter_two_name)

                # game_menu(fighter_list)

        while game_maths(
                0.25 + fighter_one_speed) == True and fight_over != True:  # While fight is not over, if true fighter one hits opponent
            print(fighter_one_name + " hits " + fighter_two_name + "\n")
            fighter_two_hp = fighter_two_hp - fighter_one_ap  # deduct health from attacker's action points
            if not game_maths(0.25 + fighter_one_speed):
                if game_maths(
                        0.25 + fighter_two_speed):  # if false and second fighter's chance is true then do the reverse
                    print(fighter_two_name + " hits " + fighter_one_name + "\n")
                    fighter_one_hp = fighter_one_hp - fighter_two_ap
            if game_maths(
                    0.25 + fighter_two_speed) == False and fight_over == False:  # If second fighter's chance is false then both have missed
                print("Both fighters have failed to land a hit! \n")

            if fighter_one_hp <= 0 and fight_over != True and fighter_one_champion:
                print(fighter_one_name + " is knocked out! \n")
                fight_over = True
                fighter_list.append(fighter_list[fighter_one].set_champion(False))
                fighter_list.append(fighter_list[fighter_two].set_champion(True))
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                print(
                    "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at two "
                    "minutes, thirty seconds \n of round number ", roundsPassed, "\n declaring the winner \n by "
                                                                                 "Knockout... \n ANNNND NEW AFC "
                                                                                 "Undisputed " + weightclass +
                                                                                 " champion of the world! " + fighter_two_name)
                break
                menu(fighter_list)

            elif fighter_one_hp <= 0 and fighter_two_champion:
                print(fighter_two_name + " is knocked out! \n")
                fight_over = True
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                print(
                    "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at one minute, thirty-five seconds of round number ",
                    roundsPassed, "\n declaring the winner \n by knockout... \n" + fighter_two_name)

            if fighter_two_hp <= 0 and fight_over != True and fighter_two_champion:
                print(fighter_two_name + " is knocked out! \n")
                fight_over = True
                fighter_list.append(fighter_list[fighter_two].set_champion(False))
                fighter_list.append(fighter_list[fighter_one].set_champion(True))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                print(
                    "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at two "
                    "minutes, thirty seconds \n of round number ", roundsPassed, "\n declaring the winner \n by "
                                                                                 "Knockout... \n ANNNND NEW AFC "
                                                                                 "Undisputed " + weightclass +
                                                                                 " champion of the world! " + fighter_one_name)
            elif fighter_two_hp <= 0 and fighter_one_champion:
                print(fighter_two_name + " is knocked out! \n")
                fight_over = True
                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                print(
                    "Ladies and Gentlemen, referee Garlic Herb has called a stop to this contest \n at one minute, thirty-five seconds of round number ",
                    roundsPassed, "\n declaring the winner \n by knockout... \n" + fighter_one_name)

        roundsPassed = roundsPassed + 1

        if roundsPassed == rounds and fight_over != True:
            if fighter_two_hp - fighter_two_endurance < fighter_one_hp - fighter_one_endurance:
                print("INSERT LINE FROM FIGHT... by winner via unanimous decision ", fighter_one_name)
                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fight_over = True
            elif fighter_one_hp - fighter_one_endurance < fighter_two_hp - fighter_two_endurance:
                print("INSERT LINE FROM FIGHT... by winner via unanimous decision ", fighter_two_name)
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                fight_over = True
            elif fighter_one_hp - fighter_one_endurance == fighter_two_hp - fighter_two_endurance:
                print("INSERT LINE FROM FIGHT...  The Judges have scored this fight a draw!")
                # fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1)) ADD DRAWS / NO CONTEST
                # fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fight_over = True

        if roundsPassed == rounds and fight_over != True and fighter_one_champion:
            if fighter_two_hp - fighter_two_endurance < fighter_one_hp - fighter_one_endurance:
                print("INSERT LINE FROM FIGHT... by winner via unanimous decision ", fighter_one_name)
                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fight_over = True
            elif fighter_one_hp - fighter_one_endurance < fighter_two_hp - fighter_two_endurance:
                print("INSERT LINE FROM FIGHT... by winner via unanimous decision ", fighter_two_name)
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                fighter_list.append(fighter_list[fighter_one].set_champion(False))
                fighter_list.append(fighter_list[fighter_two].set_champion(True))
                fight_over = True
            elif fighter_one_hp - fighter_one_endurance == fighter_two_hp - fighter_two_endurance:
                print("INSERT LINE FROM FIGHT...  The Judges have scored this fight a draw!")
                fight_over = True


# Main Functions

def main():
    fighter_list = []  # Python List / Replaces C/C++ Vectors and acts like Java's ArrayLists

    f1 = Fighter(1000, "Sebastian", "Ackermann", "Male", "Germany", "Brandenburgische, Talheim", "Boxing", 39, 105, 178,
                 90, 75, 89, 65, 70, 21, 5, True)
    f2 = Fighter(1001, "Richard", "Phelps", "Male", "Belgium", "Tiegemberg, Tongrinne", "Jiu-Jitsu", 22, 100, 180, 89,
                 80, 84, 70, 80, 15, 8, False)
    f3 = Fighter(1002, "Luis Barros", "Azevedo", "Male", "Brazil", "Francisco, Boaventura", "Brazilian Jiu-Jitsu", 27,
                 87, 175, 87, 78, 90, 80, 74, 17, 3, True)
    f4 = Fighter(1003, "Roch", "Casgrain", "Male", "France", "Paris", "Judo", 30, 86, 182, 88, 76, 91, 75, 76, 16, 7,
                 False)
    f5 = Fighter(1004, "Alec", "Blyth", "Male", "United Kingdom", "Kirkcaldy, Fife", "Kickboxing", 29, 80, 168, 95, 90,
                 95, 80, 85, 50, 0, True)
    f6 = Fighter(1005, "Neil", "Shaw", "Male", "United Kingdom", "Glasgow", "Boxing", 25, 78, 167, 89, 89, 85, 75, 73,
                 13, 2, False)
    f7 = Fighter(1006, "Peter", "Millar", "Male", "United States", "Anaheim, California", "Karate", 30, 75, 169, 84, 79,
                 84, 70, 78, 28, 6, True)
    f8 = Fighter(1007, "Finnur", "Hjörleifsson", "Male", "Iceland", "Reykjavík", "Karate", 37, 73, 170, 86, 81, 81, 87,
                 89, 21, 3, False)
    f9 = Fighter(1008, "Riley", "Franklin", "Male", "United States", "Miami, Florida", "Taekwondo", 28, 68, 168, 85, 82,
                 82, 80, 80, 13, 8, True)
    f10 = Fighter(1009, "Guang", "Tseng", "Male", "China", "Beijing", "Karate", 26, 69, 171, 86, 83, 81, 83, 83, 10, 3,
                  False)
    f11 = Fighter(1010, "Jonas", "Friedmann", "Male", "United States", "Denver, Colorado", "Kickboxing", 29, 64, 165,
                  84, 85, 80, 79, 91, 18, 8, True)
    f12 = Fighter(1011, "Khasucha", "Desheriyev", "Male", "Ukraine", "Kiev", "Wrestling", 35, 62, 168, 83, 87, 79, 90,
                  87, 14, 6, False)
    f13 = Fighter(1012, "Lukáš", "Hlaváč", "Male", "Croatia", "Zagreb", "Kickboxing", 20, 58, 168, 82, 89, 78, 87, 89,
                  19, 2, True)
    f14 = Fighter(1013, "Ronald", "Diaz", "Male", "United States", "Los Angeles, California", "Karate", 34, 58, 165, 87,
                  90, 76, 83, 75, 12, 4, False)
    f15 = Fighter(1014, "John", "Morris", "Male", "United States", "Fargo, North Dakota", "Kickboxing", 31, 52, 165, 80,
                  90, 76, 76, 74, 15, 7, True)
    f16 = Fighter(1015, "Troy", "Ryan", "Male", "United States", "Las Vegas, Nevada", "Karate", 27, 55, 166, 79, 87, 77,
                  83, 71, 11, 4, False)
    f17 = Fighter(1016, "Júlia", "Souza", "Female", "United States", "New York", "Kickboxing", 21, 63, 172, 74, 90, 79,
                  73, 72, 12, 2, True)
    f18 = Fighter(1017, "Mieczysława", "Dudek", "Female", "Poland", "Warsaw", "Wrestling", 24, 62, 168, 73, 87, 78, 69,
                  73, 4, 3, False)
    f19 = Fighter(1018, "Elena", "Toscano", "Female", "Italy", "Rome", "Kickboxing", 30, 59, 164, 73, 87, 74, 81, 75,
                  14, 6, True)
    f20 = Fighter(1019, "Maja", "Miletić", "Female", "United States", "Eden Prairie, Minnesota", "Karate", 27, 58, 163,
                  75, 89, 75, 72, 73, 9, 4, False)
    f21 = Fighter(1020, "Abby", "Patterson", "Female", "United Kingdom", "Liverpool", "Kickboxing", 26, 56, 167, 74, 79,
                  78, 67, 76, 12, 2, True)
    f22 = Fighter(1021, "Hannah", "Willis", "Female", "United States", "Boston, Massachusetts", "Kickboxing", 28, 53,
                  162, 72, 77, 76, 60, 83, 5, 7, False)
    f23 = Fighter(1022, "Katherine", "Fleming", "Female", "United States", "Stafford, Texas", "Karate", 24, 50, 160, 72,
                  80, 73, 69, 80, 17, 3, True)
    f24 = Fighter(1023, "Naomi", "Benson", "Female", "United States", "Waitsburg, Washington", "Kickboxing", 26, 49,
                  159, 70, 81, 74, 51, 50, 9, 9, False)

    fighter_list.append(f1)
    fighter_list.append(f2)
    fighter_list.append(f3)
    fighter_list.append(f4)
    fighter_list.append(f5)
    fighter_list.append(f6)
    fighter_list.append(f7)
    fighter_list.append(f8)
    fighter_list.append(f9)
    fighter_list.append(f10)
    fighter_list.append(f11)
    fighter_list.append(f12)
    fighter_list.append(f13)
    fighter_list.append(f14)
    fighter_list.append(f15)
    fighter_list.append(f16)
    fighter_list.append(f17)
    fighter_list.append(f18)
    fighter_list.append(f19)
    fighter_list.append(f20)
    fighter_list.append(f21)
    fighter_list.append(f22)
    fighter_list.append(f23)
    fighter_list.append(f24)

    menu(fighter_list)


def menu(fighter_list):
    fighter_one = 0
    fighter_two = 1

    print("\n|==========================================================|\n|                   BunnyCorp MMA Game     "
          "                |\n|==========================================================|\n|     1. Add Fighters     "
          "                                 |\n|     2. View Fighters                                     |\n|     3. "
          "Play Game                                         |\n|     0. Exit Game                                    "
          "     |\n|==========================================================|")

    fight_function(fighter_list, fighter_one, fighter_two)


main()
