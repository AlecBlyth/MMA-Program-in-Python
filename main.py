import random
import json
import time, os, sys
import operator
from num2words import num2words


# Misc Functions

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("clear")


# Fighter Class
class Fighter:
    def __init__(self, id, first_name, surname, gender, nation, fighting_out, style, age, weight, height, strength,
                 speed,
                 endurance,
                 sub_offence, sub_defence, win, lost, no_contest, champion):
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
        self.no_contest = no_contest
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

    def get_no_contest(self):
        return self.no_contest

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
        self.sub_offence = x

    def set_sub_defence(self, x):
        self.sub_defence = x

    def set_wins(self, x):
        self.win = x

    def set_losses(self, x):
        self.lost = x

    def set_no_contest(self, x):
        self.no_contest = x

    def set_champion(self, x):
        self.champion = x


# Algorithmic Functions

def game_maths(probability_of_success):
    return random.randint(0, 100) < (probability_of_success * 100)


def fight_function(fighter_list, fighter_one, fighter_two):
    # Fighter Attributes

    fighter_one_name = (fighter_list[fighter_one].get_name())
    fighter_two_name = (fighter_list[fighter_two].get_name())

    fighter_one_champion = (fighter_list[fighter_one].get_champion())
    fighter_two_champion = (fighter_list[fighter_two].get_champion())

    fighter_one_wins = (fighter_list[fighter_one].get_wins())
    fighter_two_wins = (fighter_list[fighter_two].get_wins())

    fighter_one_no_contest = (fighter_list[fighter_one].get_no_contest())
    fighter_two_no_contest = (fighter_list[fighter_two].get_no_contest())

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
    rounds_passed = 1

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

    submission_list = ["Kimura", "Twister", "Heel Hook", "Hammerlock", "Kneebar", "Omoplata", "Calf Slicer", "Toe Hold",
                       "Reverse Armbar", "Americana", "Gogoplata", "Neck Crank", "Achilles' Lock", "Guillotine Choke",
                       "Peruvian Necktie", "Triangle Choke", "Anaconda Choke", "Armbar", "Wrist Lock", "Ninja Choke",
                       "Banana Split", "D'Arce Choke", "Pace Choke", "Rear Naked Choke", "Arm-Triangle Choke"]

    referee_list = ["Garlic Herb", "Mason Herzog", "Mark Mandard", "Bart Smith", "Mike Suspran", "Danny Liotta",
                    "Peter Keithson", "Chris Cognoni"]

    minute_list = random.choice(list(range(1, 4)))
    second_list = random.choice(list(range(0, 59)))

    if fighter_one_champion | fighter_two_champion:
        rounds = 5
        score = "50-45"
        print("Championship")
    else:
        rounds = 3
        score = "30-27"
        print("Normal Bout")

    while fighter_one_hp > 0 and fighter_two_hp > 0 and rounds_passed != rounds or rounds_passed < rounds and not fight_over:

        match game_maths(0.10):
            case True:
                if fighter_one_sub_offence > fighter_two_sub_defence:
                    match game_maths(0.25):
                        case True:
                            print(fighter_one_name + " attempts a submission on  " + fighter_two_name)
                            fighter_two_hp = fighter_two_hp - fighter_one_sub_offence
                else:
                    match game_maths(0.10):
                        case True:
                            print(fighter_one_name + " attempts a submission on " + fighter_two_name)
                            fighter_two_hp = fighter_two_hp - fighter_one_sub_offence

                if fighter_two_hp <= 0 and fighter_two_champion:
                    print(fighter_two_name + "taps out! \n")

                    fighter_list.append(fighter_list[fighter_two].set_champion(False))
                    fighter_list.append(fighter_list[fighter_one].set_champion(True))
                    fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                    fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND NEW AFC Undisputed ")
                    typingPrint(weightclass)
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_one_name)
                    fight_over = True
                    break

                if fighter_two_hp <= 0 and fighter_one_champion:
                    print(fighter_two_name + " taps out! \n")

                    fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                    fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND STILL AFC Undisputed ")
                    typingPrint(weightclass)
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_one_name)
                    fight_over = True
                    break

                if fighter_two_hp <= 0 and not fighter_one_champion and not fighter_two_champion:
                    print(fighter_two_name + " taps out! \n")

                    fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                    fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    print("\n")
                    typingPrint(fighter_one_name)
                    fight_over = True
                    break

            case False:
                if fighter_two_sub_offence > fighter_one_sub_defence:
                    match game_maths(0.25):
                        case True:
                            print(fighter_two_name + " takes down and attempts to submit: " + fighter_one_name)
                            fighter_one_hp = fighter_one_hp - fighter_two_sub_offence
                else:
                    match game_maths(0.10):
                        case True:
                            print(fighter_two_name + " takes down and attempts to submit: " + fighter_one_name)
                            fighter_one_hp = fighter_one_hp - fighter_two_sub_offence

                if fighter_one_hp <= 0 and fighter_one_champion:

                    print(fighter_one_name + " taps out! \n")

                    fighter_list.append(fighter_list[fighter_one].set_champion(False))
                    fighter_list.append(fighter_list[fighter_two].set_champion(True))
                    fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                    fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND NEW AFC Undisputed ")
                    typingPrint(weightclass)
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_two_name)
                    fight_over = True
                    break

                elif fighter_one_hp <= 0 and fighter_two_champion:

                    print(fighter_one_name + " taps out! \n")

                    fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                    fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND STILL AFC Undisputed ")
                    typingPrint(weightclass)
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_two_name)
                    fight_over = True
                    break

                if fighter_one_hp <= 0 and not fighter_one_champion and not fighter_two_champion:
                    print(fighter_two_name + " taps out! \n")

                    fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                    fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random.choice(referee_list))
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    print("\n")
                    typingPrint(fighter_two_name)
                    fight_over = True
                    break

        while game_maths(0.25 + fighter_one_speed) == True and not fight_over:

            print(fighter_one_name + " hits " + fighter_two_name + "\n")
            fighter_two_hp = fighter_two_hp - fighter_one_ap

            if not game_maths(0.25 + fighter_one_speed):

                if game_maths(0.25 + fighter_two_speed):
                    print(fighter_two_name + " hits " + fighter_one_name + "\n")
                    fighter_one_hp = fighter_one_hp - fighter_two_ap

            if game_maths(0.25 + fighter_two_speed) == False and not fight_over:
                print("Both fighters have failed to land a hit! \n")

            if fighter_one_hp <= 0 and not fight_over and fighter_one_champion:

                print(fighter_one_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_one].set_champion(False))
                fighter_list.append(fighter_list[fighter_two].set_champion(True))
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            elif fighter_one_hp <= 0 and fighter_two_champion:

                print(fighter_two_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            if fighter_two_hp <= 0 and not fight_over and fighter_two_champion:

                print(fighter_two_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_two].set_champion(False))
                fighter_list.append(fighter_list[fighter_one].set_champion(True))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

            elif fighter_two_hp <= 0 and fighter_one_champion:

                print(fighter_two_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

            if fighter_one_hp <= 0 and not fighter_one_champion and not fighter_two_champion:
                print(fighter_one_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout")
                print("\n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            if fighter_two_hp <= 0 and not fighter_one_champion and not fighter_two_champion:
                print(fighter_two_name + " is knocked out! \n")

                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random.choice(referee_list))
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout")
                print("\n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

        rounds_passed = rounds_passed + 1

        if rounds_passed == rounds and not fight_over and not fighter_one_champion | fighter_two_champion:
            if fighter_two_hp - fighter_two_endurance < fighter_one_hp - fighter_one_endurance:

                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                print("\n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance < fighter_two_hp - fighter_two_endurance:
                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                print("\n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance == fighter_two_hp - fighter_two_endurance:

                fighter_list.append(fighter_list[fighter_one].set_no_contest(fighter_one_no_contest + 1))
                fighter_list.append(fighter_list[fighter_two].set_no_contest(fighter_two_no_contest + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n 28-26 ")
                typingPrint(fighter_one_name)
                typingPrint("\n28-26")
                typingPrint(fighter_two_name)
                typingPrint("\nand 27-27, this fight is considered a draw")

                fight_over = True
                break

        if rounds_passed == rounds and not fight_over and fighter_one_champion:
            if fighter_two_hp - fighter_two_endurance < fighter_one_hp - fighter_one_endurance:

                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance < fighter_two_hp - fighter_two_endurance:

                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))
                fighter_list.append(fighter_list[fighter_one].set_champion(False))
                fighter_list.append(fighter_list[fighter_two].set_champion(True))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance == fighter_two_hp - fighter_two_endurance:

                fighter_list.append(fighter_list[fighter_one].set_no_contest(fighter_one_no_contest + 1))
                fighter_list.append(fighter_list[fighter_two].set_no_contest(fighter_two_no_contest + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n 48-46 ")
                typingPrint(fighter_one_name)
                typingPrint("\n48-46")
                typingPrint(fighter_two_name)
                typingPrint("\nand 47-47, this fight is considered a draw")

                fight_over = True
                break

        if rounds_passed == rounds and not fight_over and fighter_two_champion:
            if fighter_two_hp - fighter_two_endurance < fighter_one_hp - fighter_one_endurance:

                fighter_list.append(fighter_list[fighter_two].set_losses(fighter_two_losses + 1))
                fighter_list.append(fighter_list[fighter_one].set_wins(fighter_one_wins + 1))
                fighter_list.append(fighter_list[fighter_one].set_champion(True))
                fighter_list.append(fighter_list[fighter_two].set_champion(False))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_one_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance < fighter_two_hp - fighter_two_endurance:

                fighter_list.append(fighter_list[fighter_one].set_losses(fighter_one_losses + 1))
                fighter_list.append(fighter_list[fighter_two].set_wins(fighter_two_wins + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(weightclass)
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_two_name)

                fight_over = True
                break

            elif fighter_one_hp - fighter_one_endurance == fighter_two_hp - fighter_two_endurance:

                fighter_list.append(fighter_list[fighter_one].set_no_contest(fighter_one_no_contest + 1))
                fighter_list.append(fighter_list[fighter_two].set_no_contest(fighter_two_no_contest + 1))

                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n 48-46 ")
                typingPrint(fighter_one_name)
                typingPrint("\n48-46")
                typingPrint(fighter_two_name)
                typingPrint("\nand 47-47, this fight is considered a draw")

                fight_over = True
                break


# Main Functions

def main():
    fighter_list = []  # Python List / Replaces C/C++ Vectors and acts like Java's ArrayLists

    f = open('fighters.json', encoding="utf8")
    data = json.load(f)
    for i in data['Fighters']:
        json_object = i
        a_fighter = Fighter(json_object["ID"], json_object["firstName"], json_object["surName"], json_object["gender"],
                            json_object["nation"], json_object["fightingOut"], json_object["style"], json_object["age"],
                            json_object["weight"], json_object["height"], json_object["strength"], json_object["speed"],
                            json_object["endurance"], json_object["subOffence"], json_object["subDefence"],
                            json_object["won"], json_object["lost"], json_object["noContest"], json_object['champion'])
        fighter_list.append(a_fighter)

    menu(fighter_list)


def menu(fighter_list):
    print("\n|==========================================================|\n|                   BunnyCorp MMA Game     "
          "                |\n|==========================================================|\n|     1. Add Fighters     "
          "                                 |\n|     2. View Fighters                                     |\n|     3. "
          "Play Game                                         |\n|     0. Exit Game                                    "
          "     |\n|==========================================================|")

    choice = input("\nPlease select an option.\n")

    match choice:
        case '1':

            last_elem = operator.itemgetter(-1)(fighter_list)
            last_id = last_elem.get_id() + 1
            print("|==================== Create a Fighter ====================|")
            first_name = input("\n --- Insert your fighter's first name. --- \n")
            second_name = input("\n --- Insert your fighter's last name. --- \n")

            while True:
                gender = input("\n --- Insert your fighter's gender. --- \n")
                gender = gender.capitalize()
                print(gender)
                try:
                    gender = str(gender)
                except:
                    print("Invalid!")
                if gender.isdigit():
                    print("\nEnter non numeric input.\n")
                    continue
                if gender != 'Male' and gender != 'Female':
                    print("Please enter valid input")
                    continue
                break

            nation = input("\n --- Insert your fighter's home country. --- \n")
            fightingOut = input("\n --- Insert your fighter's city. --- \n")
            style = input("\n --- Insert your fighter's fighting style. --- \n")

            while True:
                age = input("\n --- Insert your fighter's age. --- \n")
                try:
                    age = int(age)
                except:
                    print("\nEnter numeric digits.\n")
                    continue
                if age < 17 or age > 50:
                    print("\nToo young or old, please enter an age between 17 and 50\n")
                    continue
                break

            while True:
                weight = input("\n --- Insert your fighter's weight in kg. --- \n")
                try:
                    weight = int(weight)
                except:
                    print("\nEnter numeric digits.\n")
                    continue
                if weight < 1:
                    print("\nPlease enter a positive value\n")
                    continue
                break

            while True:
                height = input("\n --- Insert your fighter's height in cm. --- \n")
                try:
                    height = int(height)
                except:
                    print("\nEnter numeric digits.\n")
                    continue
                if height < 1:
                    print("\nPlease enter a positive value\n")
                    continue
                break
            new_fighter = Fighter(last_id, first_name, second_name, gender, nation, fightingOut, style, age, weight,
                                  height, 30, 30, 30, 30, 30, 0, 0, 0, False)
            fighter_list.append(new_fighter)
            menu(fighter_list)

        case '2':
            print("VIEW FIGHTER")

            for obj in fighter_list:
                print("\n|========================= Fighter ========================|\nFighter Name:")

                if obj.get_weight() >= 93 and obj.get_weight() <= 120 and obj.get_gender() == "Male":
                    weightclass = "Heavyweight"
                elif 84 <= obj.get_weight() <= 92 and obj.get_gender() == "Male":
                    weightclass = "Light Heavyweight"
                elif 77 <= obj.get_weight() <= 83 and obj.get_gender() == "Male":
                    weightclass = "Middleweight"
                elif 70 <= obj.get_weight() <= 76 and obj.get_gender() == "Male":
                    weightclass = "Welterweight"
                elif 66 <= obj.get_weight() <= 69 and obj.get_gender() == "Male":
                    weightclass = "Lightweight"
                elif 61 <= obj.get_weight() <= 65 and obj.get_gender() == "Male":
                    weightclass = "Featherweight"
                elif 57 <= obj.get_weight() <= 60 and obj.get_gender() == "Male":
                    weightclass = "Bantamweight"
                elif 52 <= obj.get_weight() <= 56 and obj.get_gender() == "Male":
                    weightclass = "Flyweight"
                elif 61 <= obj.get_weight() <= 66 and obj.get_gender() == "Female":
                    weightclass = "Woman's Featherweight"
                elif 57 <= obj.get_weight() <= 60 and obj.get_gender() == "Female":
                    weightclass = "Woman's Bantamweight"
                elif 52 <= obj.get_weight() <= 56 and obj.get_gender() == "Female":
                    weightclass = "Woman's Flyweight"
                elif 0 <= obj.get_weight() <= 51 and obj.get_gender() == "Female":
                    weightclass = "Woman's Strawweight"

                if obj.get_champion() == True:
                    status = weightclass + " champion"
                else:
                    status = "None"
                print(obj.get_name(), "\nFrom: ", obj.get_nation(), "\nFighting out of: ", obj.get_fighting_out(),
                      "\nFight Style: ", obj.get_style(), "\nAge: ", obj.get_age(), "\nWeight: ", obj.get_weight(),
                      "kg", "\nHeight: ", obj.get_height(), "cm", "\nStrength: ", obj.get_strength(), "\nSpeed: ",
                      obj.get_speed(), "\nEndurance: ", obj.get_endurance(), "\nTakedown Defence: ",
                      obj.get_sub_defence(), "\nSubmission Offence: ", obj.get_sub_offence(), "\nWins: ",
                      obj.get_wins(), "\nLosses: ", obj.get_losses(), "\nNo Contests: ", obj.get_no_contest(),
                      "\nTitles: ", status)

                menu(fighter_list)

        case '3':
            game_menu(fighter_list)
        case '0':
            exit(0)


def game_menu(fighter_list):
    print(
        '\n|==========================================================|\n|'
        '                   BunnyCorp MMA Game                     |\n'
        '|==========================================================|\n|'
        '     1. Pick Fighter                                      |\n|'
        '     2. Train Fighters                                    |\n|'
        '     3. Fight                                             |\n|'
        '     4. Main Menu                                         |\n'
        '|==========================================================|\n')

    choice = input("\nPlease select an option.\n")

    match choice:
        case '1':
            print("Pick Fighter")
        case '2':
            print("Train")
        case '3':
            print("Fight")
        case '4':
            menu(fighter_list)


main()
