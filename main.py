import json
import operator
import random
import sys
import time

from num2words import num2words


# Misc Functions

# Types out strings within console for dramatic effect
def typingPrint(text):
    # For each character within string, write string
    for character in text:
        sys.stdout.write(character)
        # Clears the input buffer
        sys.stdout.flush()
        # Sets speed of typing
        time.sleep(0.05)


# Fighter Class
class Fighter:
    # Object attributes  
    def __init__(self, object_id, first_name, surname, gender, nation, fighting_out, style, age, weight, height, strength,
                 speed,
                 endurance,
                 sub_offence, sub_defence, win, lost, no_contest, weight_class, champion):

        self.id = object_id
        # Could add nicknames, would need to separate full name for announcement
        self.first_name = first_name
        self.surname = surname
        self.gender = gender  # Planned but never implemented / Newish
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
        self.no_contest = no_contest  # New
        self.weight_class = weight_class  # New
        self.champion = champion  # New

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

    def get_weight_class(self):
        return self.weight_class

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

    def set_weight_class(self, x):
        self.weight_class = x

    def set_champion(self, x):
        self.champion = x


# Algorithmic Functions

def game_maths(probability_of_success):
    # Returns true of false based on probability and uses percentage input
    return random.randint(0, 100) < (probability_of_success * 100)


def fight_function(fighter_list, fighter_one, fighter_two):
    
    # Fighter Algorithmic Attributes

    fighter_one_hp = 100 + fighter_list[fighter_one].get_endurance()
    fighter_two_hp = 100 + fighter_list[fighter_two].get_endurance()

    fighter_one_ap = 100 + fighter_list[fighter_one].get_strength() / 10
    fighter_two_ap = 100 + fighter_list[fighter_two].get_strength() / 10

    fighter_one_speed = (fighter_list[fighter_one].get_speed())
    fighter_one_speed = fighter_one_speed / 100 / 5

    fighter_two_speed = (fighter_list[fighter_two].get_speed())
    fighter_two_speed = fighter_two_speed / 100 / 5

    # Adds correct pronouns for each fighter
    # fighter_one gender will be the same as fighter_two
    # No need to check here as it is validated before fight / This isn't Russian MMA
    if fighter_list[fighter_one].get_gender() == "Male":
        pronoun = "He stands, "
    else:
        pronoun = "She stands, "

    # Fight Variables

    fight_over = False  # Possibly redundant
    rounds_passed = 1

    # NEW: Array of submission types
    submission_list = ["Kimura", "Twister", "Heel Hook", "Hammerlock", "Kneebar", "Omoplata", "Calf Slicer", "Toe Hold",
                       "Reverse Armbar", "Americana", "Gogoplata", "Neck Crank", "Achilles' Lock", "Guillotine Choke",
                       "Peruvian Necktie", "Triangle Choke", "Anaconda Choke", "Armbar", "Wrist Lock", "Ninja Choke",
                       "Banana Split", "D'Arce Choke", "Pace Choke", "Rear Naked Choke", "Arm-Triangle Choke"]

    # NEW: Array of referees
    referee_list = ["Garlic Herb", "Mason Herzog", "Mark Mandard", "Bart Smith", "Mike Suspran", "Danny Liotta",
                    "Peter Keithson", "Chris Cognoni"]

    # NEW: Array of potential finishing moves
    move_list = ["Jab", "Overhand", "Round Kick", "Flying Knee", "Spinning Back-Fist", "Spinning Elbow", "Hook", "Cross"]

    # NEW: Array lists of number ranges to generate stoppage time between rounds
    minute_list = random.choice(list(range(1, 4)))
    second_list = random.choice(list(range(0, 59)))

    # NEW: Just a list between 1 and 15, used to generate random ranks
    # Could be replaced with proper ranks within object that act like championship and are swapped between fighters
    # If implemented would need to increment all fighters in a given weight-class, could be messy if fighters can switch weights
    rank_list = random.choice(list(range(1, 15)))

    # Selects a random referee from list
    random_referee = random.choice(referee_list)

    # NEW: Checks to see if either fighter is a champion
    if fighter_list[fighter_one].get_champion() | fighter_list[fighter_two].get_champion():

        # Sets number of rounds to 5 instead of 3 for championship bouts
        rounds = 5

        # Used for decisions, could implement round scoring but would require more advanced fighting algorithm
        # Default scoring for unanimous decision for five round fights
        score = "50-45"

        # NEW: Fight intro with typing effect
        if fighter_list[fighter_one].get_champion():
            typingPrint("Ladies and Gentlemen, THIS IS the main event of the evening,\n")
            typingPrint("sanctioned by the ABM athletic commission, our three judges scoring\n")
            typingPrint("this contest at octagon side are, John Doe, Adam Smith and Leonardo Vinci\n")
            typingPrint("and when the action begins a referee in charge of the octagon, ")
            typingPrint(random_referee)
            typingPrint("\nAND NOW")
            typingPrint("\nFor those in attendance and AFC fans watching this console prompt")
            typingPrint("\nThis is the moment you've all been waiting for!")
            typingPrint("\nLIVE from the Python interpreter Arena in Python 3.11")

            # I remember hearing that this part may or may not be trademarked, so I adapted it
            typingPrint("\nIt's time to fight!")
            typingPrint("\n5 Rounds for the undisputed AFC ")

            # Both fighters will be in same weight-class, could implement catch weight
            # If fighter 1 weight is > fighter 2, ask user if okay to proceed, if true, catch weight is true
            # Could implement weight cutting / gaining
            typingPrint(fighter_list[fighter_one].get_weight_class())

            typingPrint(" championship of the world\n")
            # As of writing this, this has been replaced by a cringe sponsorship. I cry
            # This is pre-hydration zone MMA
            typingPrint("introducing first, fighting out of the green corner, a ")
            typingPrint(fighter_list[fighter_two].get_style())
            typingPrint(" style fighter\n")  # Could replace with translation, e.g. Boxing = Boxer etc
            typingPrint("holding a professional record\n")
            typingPrint(str(fighter_list[fighter_two].get_wins()))
            typingPrint(" wins\n")
            typingPrint(str(fighter_list[fighter_two].get_losses()))
            typingPrint(" losses\n")

            # Checks if fighter has any no contests, if they do, then announcer will say it
            # Otherwise it will skip it
            if fighter_list[fighter_two].get_no_contest() > 0:
                typingPrint(str(fighter_list[fighter_two].get_no_contest()))
                typingPrint(" no contests\n")

            typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

            # Announcer lists tale of the tape
            typingPrint(str(fighter_list[fighter_two].get_height()))
            typingPrint("cm tall, weighing in at ")  # Unlike my favourite promotion, AFC uses metric
            typingPrint(str(fighter_list[fighter_two].get_weight()))
            typingPrint("kg\nFighting out of ")
            typingPrint(fighter_list[fighter_two].get_fighting_out())
            typingPrint("\nPresenting the number ")

            # Gets random rank for non-champion fighter
            typingPrint(str(rank_list))
            typingPrint(" ranked ")
            typingPrint(fighter_list[fighter_one].get_weight_class())
            typingPrint(" contender in the world \nThe challenger! \n")
            typingPrint(fighter_list[fighter_two].get_name() + "\n")

            # Champion announcement
            typingPrint("\nand now introducing the champion, fighting out of the blue corner, a ")  # If only one member of the brand left, I wouldn't cringe as much
            typingPrint(fighter_list[fighter_one].get_style())
            typingPrint(" style fighter\n")  # Could replace with translation, e.g. Boxing = Boxer etc
            typingPrint("holding a professional record\n")
            typingPrint(str(fighter_list[fighter_one].get_wins()))
            typingPrint(" wins\n")
            typingPrint(str(fighter_list[fighter_one].get_losses()))
            typingPrint(" losses\n")

            # Checks if fighter has any no contests, if they do, then announcer will say it
            # Otherwise it will skip it
            if fighter_list[fighter_one].get_no_contest() > 0:
                typingPrint(str(fighter_list[fighter_one].get_no_contest()))
                typingPrint(" no contests\n")

            typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

            # Announcer lists tale of the tape of champion
            typingPrint(str(fighter_list[fighter_one].get_height()))
            typingPrint("cm tall, weighing in at ")
            typingPrint(str(fighter_list[fighter_one].get_weight()))
            typingPrint("kg\nFighting out of ")  # Unlike my favourite promotion, AFC uses metric
            typingPrint(fighter_list[fighter_one].get_fighting_out())
            typingPrint("\nPresenting the reigning... , defending..., undisputed AFC ")
            typingPrint(fighter_list[fighter_one].get_weight_class())
            typingPrint(" champion of the world \n")
            typingPrint(fighter_list[fighter_one].get_name() + "\n\n")

        # Same as above but reversed if the selected fighter isn't the champion
        if fighter_list[fighter_two].get_champion():
            typingPrint("Ladies and Gentlemen, THIS IS the main event of the evening,\n")
            typingPrint("sanctioned by the ABM athletic commission, our three judges scoring\n")
            typingPrint("this contest at octagon side are, John Doe, Adam Smith and Leonardo Vinci\n")
            typingPrint("and when the action begins a referee in charge of the octagon, ")
            typingPrint(random_referee)
            typingPrint("\nAND NOW")
            typingPrint("\nFor those in attendance and AFC fans watching this console prompt")
            typingPrint("\nThis is the moment you've all been waiting for!")
            typingPrint("\nLIVE from the Python interpreter Arena in Python 3.11")

            # I remember hearing that this part may or may not be trademarked, so I adapted it
            typingPrint("\nIt's time to fight!")
            typingPrint("\n5 Rounds for the undisputed AFC ")

            # Both fighters will be in same weight class
            typingPrint(fighter_list[fighter_one].get_weight_class())

            typingPrint(" championship of the world\n")
            typingPrint("introducing first, fighting out of the green corner, a ")  # It's not even a good brand.
            typingPrint(fighter_list[fighter_one].get_style())
            typingPrint(" style fighter\n")
            typingPrint("holding a professional record\n")
            typingPrint(str(fighter_list[fighter_one].get_wins()))
            typingPrint(" wins\n")
            typingPrint(str(fighter_list[fighter_one].get_losses()))
            typingPrint(" losses\n")

            # Checks no contest
            if fighter_list[fighter_one].get_no_contest() > 0:
                typingPrint(str(fighter_list[fighter_one].get_no_contest()))
                typingPrint(" no contests\n")

            typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

            # Lists tale of the tape
            typingPrint(str(fighter_list[fighter_one].get_height()))
            typingPrint("cm tall, weighing in at ")
            typingPrint(str(fighter_list[fighter_one].get_weight()))
            typingPrint("kg\nFighting out of ")
            typingPrint(fighter_list[fighter_one].get_fighting_out())
            typingPrint("\nPresenting the number ")

            # Generates random rank for non-champion fighter/player
            typingPrint(str(rank_list))
            typingPrint(" ranked ")
            typingPrint(fighter_list[fighter_one].get_weight_class())
            typingPrint(" contender in the world \nThe challenger! \n")
            typingPrint(fighter_list[fighter_one].get_name() + "\n")
            typingPrint("\nand now introducing the champion, fighting out of the blue corner, a ")  # Can't believe Arsenal are even sponsored by it
            typingPrint(fighter_list[fighter_two].get_style())
            typingPrint(" style fighter\n")
            typingPrint("holding a professional record\n")
            typingPrint(str(fighter_list[fighter_two].get_wins()))
            typingPrint(" wins\n")
            typingPrint(str(fighter_list[fighter_two].get_losses()))
            typingPrint(" losses\n")

            # Checks no contests
            if fighter_list[fighter_two].get_no_contest() > 0:
                typingPrint(str(fighter_list[fighter_two].get_no_contest()))
                typingPrint(" no contests\n")

            typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

            # Lists tale of the tape for champion
            typingPrint(str(fighter_list[fighter_two].get_height()))
            typingPrint("cm tall, weighing in at ")
            typingPrint(str(fighter_list[fighter_two].get_weight()))
            typingPrint("kg\nFighting out of ")
            typingPrint(fighter_list[fighter_two].get_fighting_out())
            typingPrint("\nPresenting the reigning... , defending..., undisputed AFC ")
            typingPrint(fighter_list[fighter_one].get_weight_class())
            typingPrint(" champion of the world \n")
            typingPrint(fighter_list[fighter_two].get_name() + "\n\n")

    # Else if neither fighter is a champion
    else:
        rounds = 3  # Normal bouts are only three rounds
        score = "30-27"  # Default scoring for unanimous decision for three round fights
        fighter_two_rank = rank_list  # Generates rank for fighters
        fighter_one_rank = fighter_two_rank - 1  # Need to validate for 0, maybe make it interim champion

        # NEW: Fight intro with typing effect
        typingPrint("Ladies and gentlemen, this fight is three rounds in the AFC ")
        typingPrint(fighter_list[fighter_one].get_weight_class())
        typingPrint(" division\n")
        typingPrint("Introducing first, fighting out of the green corner\nA ")  # Hope my favourite team doesn't get sponsored by them
        typingPrint(fighter_list[fighter_two].get_style())
        typingPrint(" style fighter\n")
        typingPrint("holding a record of\n")
        typingPrint(str(fighter_list[fighter_two].get_wins()))
        typingPrint(" wins\n")
        typingPrint(str(fighter_list[fighter_two].get_losses()))
        typingPrint(" losses\n")

        # Checks if no contest
        if fighter_list[fighter_two].get_no_contest() != 0:
            typingPrint(str(fighter_list[fighter_two].get_no_contest()))
            typingPrint(" no contests \n")

        typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

        # Lists tale of the tape for fighter two
        typingPrint(str(fighter_list[fighter_two].get_height()))
        typingPrint("cm, weighing in at ")
        typingPrint(str(fighter_list[fighter_two].get_weight()))
        typingPrint("kg\n")
        typingPrint("Fighting out of ")
        typingPrint(fighter_list[fighter_two].get_fighting_out())
        typingPrint("\nPresenting, the number ")
        typingPrint(str(fighter_two_rank))
        typingPrint(" ranked ")
        typingPrint(fighter_list[fighter_one].get_weight_class())
        typingPrint(" contender in the world,\n")
        typingPrint(fighter_list[fighter_two].get_name() + "\n\n")

        # Announces higher ranked fighter

        typingPrint("And now introducing their opponent, fighting out of the blue corner\nA ")  # My favourite team already has a good sports drink sponsor
        typingPrint(fighter_list[fighter_one].get_style())
        typingPrint(" style fighter\n")
        typingPrint("holding a record of\n")
        typingPrint(str(fighter_list[fighter_one].get_wins()))
        typingPrint(" wins\n")
        typingPrint(str(fighter_list[fighter_one].get_losses()))
        typingPrint(" losses\n")

        # Checks for no contests
        if fighter_list[fighter_one].get_no_contest() != 0:
            typingPrint(str(fighter_list[fighter_one].get_no_contest()))
            typingPrint(" no contests \n")

        typingPrint("\n" + pronoun)  # Uses correct pronouns for fighters

        typingPrint(str(fighter_list[fighter_one].get_height()))
        typingPrint("cm, weighing in at ")
        typingPrint(str(fighter_list[fighter_one].get_weight()))
        typingPrint("kg\n")
        typingPrint("Fighting out of ")
        typingPrint(fighter_list[fighter_one].get_fighting_out())
        typingPrint("\nPresenting, the number ")
        typingPrint(str(fighter_one_rank))
        typingPrint(" ranked ")
        typingPrint(fighter_list[fighter_one].get_weight_class())
        typingPrint(" contender in the world,\n")
        typingPrint(fighter_list[fighter_one].get_name())

        typingPrint("\nBefore the action begins, our referee in charge, ")
        typingPrint(random_referee + "\n")

    while fighter_one_hp > 0 and fighter_two_hp > 0 and rounds_passed != rounds or rounds_passed < rounds and not fight_over:

        # 0.10% chance of a successful takedown and submission attempt
        match game_maths(0.10):

            # If game maths returns true, then selected fighter object gets to attempt
            case True:
                print(fighter_list[fighter_one].get_name(), "attempts a takedown\n")

                # If selected fighter object submission stats are greater than fighter two object
                if fighter_list[fighter_one].get_sub_offence() > fighter_list[fighter_two].get_sub_defence():

                    # Roll again for submission attempt at 0.25% chance
                    match game_maths(0.25):

                        # If true takedown and submission attempt is successful
                        case True:
                            print(fighter_list[fighter_one].get_name(), "takes down and attempts a submission on", fighter_list[fighter_two].get_name())

                            # Submission reduces second object fighter's health
                            fighter_two_hp = fighter_two_hp - fighter_list[fighter_one].get_sub_offence()

                # Else chances of successful take down is reduced from 0.25% to 0.10%
                else:
                    match game_maths(0.10):
                        case True:
                            print(fighter_list[fighter_one].get_name(), "attempts a takedown\n")
                            print(fighter_list[fighter_one].get_name(), "takes down attempts a submission on", fighter_list[fighter_two].get_name())

                            # Submission reduces second object fighter's health
                            fighter_two_hp = fighter_two_hp - fighter_list[fighter_one].get_sub_offence()

                # If object fighter two health is 0 and fighter two attribute champion is true
                if fighter_two_hp <= 0 and fighter_list[fighter_two].get_champion():
                    print(fighter_list[fighter_two].get_name() + "taps out! \n")

                    # Change object attributes
                    fighter_list[fighter_one].set_champion(True)  # Selected fighter object champion attribute changes from false to true
                    fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)  # Increment object wins by 1
                    fighter_list[fighter_two].set_champion(False)  # fighter two object champion attribute changes from true to false
                    fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)  # Increment object losses by 1

                    # NEW: End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND NEW AFC Undisputed ")
                    typingPrint(fighter_list[fighter_one].get_weight_class())
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_list[fighter_one].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

                # If selected fighter object is champion
                if fighter_two_hp <= 0 and fighter_list[fighter_one].get_champion():
                    print(fighter_list[fighter_two].get_name() + " taps out! \n")

                    # Just increment wins and losses for victor and loser objects
                    fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                    fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                    # End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND STILL AFC Undisputed ")
                    typingPrint(fighter_list[fighter_one].get_weight_class())
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_list[fighter_one].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

                # If both fighter objects champion attributes = false and fighter two object health is 0
                if fighter_two_hp <= 0 and not fighter_list[fighter_one].get_champion() and not fighter_list[fighter_two].get_champion():
                    print(fighter_list[fighter_two].get_name() + " taps out! \n")

                    # Just increment wins and losses for victor and loser objects
                    fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                    fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                    # End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list) + "\n")
                    typingPrint(fighter_list[fighter_one].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

            # If false is returned, fighter two object gets to attempt a submission
            case False:
                print(fighter_list[fighter_two].get_name(), "attempts a takedown\n")

                # If fighter two object submission stats are greater than selected fighter object's stats
                if fighter_list[fighter_two].get_sub_offence() > fighter_list[fighter_one].get_sub_defence():

                    # Roll again for submission attempt at 0.25% chance
                    match game_maths(0.25):

                        # If true takedown and submission attempt is successful
                        case True:
                            print(fighter_list[fighter_two].get_name() + " takes down and attempts to submit: " + fighter_list[fighter_one].get_name())

                            # Submission reduces second fighter's health
                            fighter_one_hp = fighter_one_hp - fighter_list[fighter_two].get_sub_offence()

                # Else chances of successful take down is reduced from 0.25% to 0.10%
                else:
                    match game_maths(0.10):
                        case True:
                            print(fighter_list[fighter_two].get_name() + " takes down and attempts to submit: " + fighter_list[fighter_one].get_name())

                            # Submission reduces second fighter's health
                            fighter_one_hp = fighter_one_hp - fighter_list[fighter_two].get_sub_offence()

                # If selected fighter object health is 0 and is champion attribute is true
                if fighter_one_hp <= 0 and fighter_list[fighter_one].get_champion():
                    print(fighter_list[fighter_one].get_name() + " taps out! \n")

                    # Change object attributes
                    fighter_list[fighter_one].set_champion(False)  # Change selected fighter object champion attribute to false
                    fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)  # Increment selected fighter losses attribute by 1
                    fighter_list[fighter_two].set_champion(True)  # Change second fighter object champion attribute to true
                    fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)  # Increment second fighter object wins attribute by 1

                    # End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND NEW AFC Undisputed ")
                    typingPrint(fighter_list[fighter_one].get_weight_class())
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_list[fighter_two].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

                # If selected fighter object health is 0 and fighter two object is champion is true
                elif fighter_one_hp <= 0 and fighter_list[fighter_two].get_champion():
                    print(fighter_list[fighter_one].get_name() + " taps out! \n")

                    # Just increment wins and losses for victor and loser objects
                    fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)
                    fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)

                    # End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list))
                    typingPrint("\nAND STILL AFC Undisputed ")
                    typingPrint(fighter_list[fighter_one].get_weight_class())
                    typingPrint(" champion of the world... \n")
                    typingPrint(fighter_list[fighter_two].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

                # If neither objects has champion attribute set to true
                if fighter_one_hp <= 0 and not fighter_list[fighter_one].get_champion() and not fighter_list[fighter_two].get_champion():
                    print(fighter_list[fighter_one].get_name() + " taps out! \n")

                    # Just increment wins and losses for victor and loser objects
                    fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)
                    fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)

                    # End of fight announcement
                    typingPrint("Ladies and Gentlemen, referee ")
                    typingPrint(random_referee)
                    typingPrint(" has called a stop to this contest at ")
                    typingPrint(num2words(minute_list))
                    typingPrint(" minutes and ")
                    typingPrint(num2words(second_list))
                    typingPrint(" seconds of round number ")
                    typingPrint(str(rounds_passed))
                    typingPrint("\ndeclaring the winner by submission due to a ")
                    typingPrint(random.choice(submission_list) + "\n")
                    typingPrint(fighter_list[fighter_two].get_name())

                    game_menu(fighter_list, fighter_one)  # Send user back to menu
                    break

        # While the fight is not over and fighter one's speed + 0.25% returns true
        while game_maths(0.25 + fighter_one_speed) and not fight_over:

            # Selected player object hits second fighter object
            print(fighter_list[fighter_one].get_name() + " hits " + fighter_list[fighter_two].get_name() + "\n")

            # fighter two object health is reduced by selected fighter's action points
            fighter_two_hp = fighter_two_hp - fighter_one_ap

            # if false is returned
            if not game_maths(0.25 + fighter_one_speed):

                # If true is returned for fighter two object speed
                if game_maths(0.25 + fighter_two_speed):

                    # Fighter two object hits selected fighter object
                    print(fighter_list[fighter_two].get_name() + " hits " + fighter_list[fighter_one].get_name() + "\n")

                    # Selected fighter object health is reduced by fighter two object action points
                    fighter_one_hp = fighter_one_hp - fighter_two_ap

            # if false is returned again
            if game_maths(0.25 + fighter_two_speed) is False and not fight_over:

                # Both objects failed to hit
                print("Both fighters have failed to land a hit! \n")

            # If selected object health is 0 due to hits and selected fighter object attribute champion is true
            if fighter_one_hp <= 0 and not fight_over and fighter_list[fighter_one].get_champion():

                # Selected fighter object hits a random move and knocks out fighter two object
                print(fighter_list[fighter_two].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_one].get_name() + " is knocked out! \n")

                # Change object attributes
                fighter_list[fighter_one].set_champion(False)  # Selected fighter object champion attribute is set to false
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)  # Increment selected fighter object losses attribute by 1
                fighter_list[fighter_two].set_champion(True)  # fighter two object champion attribute is set to true
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)  # Increment second fighter object wins attribute by 1

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_two].get_name())
                fight_over = True  # End of fight = true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if selected object health is 0 due to hits and fighter two object attribute champion is true
            elif fighter_one_hp <= 0 and fighter_list[fighter_two].get_champion():

                # fighter two object hits a random move and knocks out selected fighter object
                print(fighter_list[fighter_two].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_one].get_name() + " is knocked out! \n")

                # Just increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_two].get_name())
                fight_over = True  # End of fight = true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # If fighter two object health is 0 due to hits and fighter two object attribute champion is true
            if fighter_two_hp <= 0 and not fight_over and fighter_list[fighter_two].get_champion():

                # Selected fighter object hits a random move and knocks out fighter two object
                print(fighter_list[fighter_one].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_two].get_name() + " is knocked out! \n")

                # Change object attributes
                fighter_list[fighter_one].set_champion(True)  # Selected fighter object champion attribute is set to true
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)  # Increment selected fighter object wins attribute by 1
                fighter_list[fighter_two].set_champion(False)  # fighter two object champion attribute is set to false
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)  # Increment second fighter object losses attribute by 1

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_one].get_name())
                fight_over = True  # End of fight is true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if fighter two object health is 0 due to hits and selected fighter object attribute champion is true
            elif fighter_two_hp <= 0 and fighter_list[fighter_one].get_champion():

                # Selected fighter object hits a random move and knocks out fighter two object
                print(fighter_list[fighter_one].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_two].get_name() + " is knocked out! \n")

                # Just increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout ")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_one].get_name())
                fight_over = True  # End of fight = true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # If selected object health is 0 due to hits and selected fighter object and fighter two object attribute champion is false
            if fighter_one_hp <= 0 and not fighter_list[fighter_one].get_champion() and not fighter_list[fighter_two].get_champion():

                print(fighter_list[fighter_two].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_one].get_name() + " is knocked out! \n")

                # Just increment wins and losses for victor and loser objects
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout\n")
                typingPrint(fighter_list[fighter_two].get_name())
                fight_over = True  # End of fight = true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # If fighter two object health is 0 due to hits and selected fighter object and fighter two object attribute champion is false
            if fighter_two_hp <= 0 and not fighter_list[fighter_one].get_champion() and not fighter_list[fighter_two].get_champion():

                # Selected fighter object hits a random move and knocks out fighter two object
                print(fighter_list[fighter_one].get_name(), "lands a good", random.choice(move_list), "! \n")
                print(fighter_list[fighter_two].get_name() + " is knocked out! \n")

                # Just increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, referee ")
                typingPrint(random_referee)
                typingPrint(" has called a stop to this contest at ")
                typingPrint(num2words(minute_list))
                typingPrint(" minutes and ")
                typingPrint(num2words(second_list))
                typingPrint(" seconds of round number ")
                typingPrint(str(rounds_passed))
                typingPrint("\ndeclaring the winner by knockout\n")
                typingPrint(fighter_list[fighter_one].get_name())
                fight_over = True  # End of fight = true

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

        # Increment rounds by 1
        rounds_passed = rounds_passed + 1

        # If rounds passed equal number of allotted rounds
        if rounds_passed == rounds and not fight_over and not fighter_list[fighter_one].get_champion() | fighter_list[fighter_two].get_champion():

            # If fighter two object health minus object endurance attribute is less than selected fighter's health minus object endurance attribute
            if fighter_two_hp - fighter_list[fighter_two].get_endurance() < fighter_one_hp - fighter_list[fighter_one].get_endurance():

                # Selected fighter object wins by decision
                # Increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision\n")
                typingPrint(fighter_list[fighter_one].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if reverse is true
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() < fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Second fighter object wins by decision
                # Increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision\n")
                typingPrint(fighter_list[fighter_two].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if both object health minus endurance is equal
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() == fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Fight is considered a draw
                # Increment both fighter two and selected fighter object no contest attribute by 1
                fighter_list[fighter_one].set_no_contest(fighter_list[fighter_one].get_no_contest() + 1)
                fighter_list[fighter_two].set_no_contest(fighter_list[fighter_two].get_no_contest() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n28-26 ")
                typingPrint(fighter_list[fighter_one].get_name())
                typingPrint("\n28-26 ")
                typingPrint(fighter_list[fighter_two].get_name())
                typingPrint("\nand 27-27, this fight is considered a draw")

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

        # If rounds passed equal number of allotted rounds and selected fighter champion attribute is true
        if rounds_passed == rounds and not fight_over and fighter_list[fighter_one].get_champion():

            # If fighter two object health minus object endurance attribute is less than selected fighter's health minus object endurance attribute
            if fighter_two_hp - fighter_list[fighter_two].get_endurance() < fighter_one_hp - fighter_list[fighter_one].get_endurance():

                # Selected fighter object wins by decision and retains champion attribute
                # Increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_one].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if reverse is true
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() < fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Fighter two object wins by decision and gains true champion attribute
                # Change object attributes
                fighter_list[fighter_one].set_champion(False)  # Selected fighter object champion attribute is set to false
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)  # Increment selected fighter object losses attribute by 1
                fighter_list[fighter_two].set_champion(True)  # fighter two object champion attribute is set to true
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)  # Increment second fighter object wins attribute by 1

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_two].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if both object health minus endurance is equal
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() == fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Fight is considered a draw
                # Increment both fighter two and selected fighter object no contest attribute by 1
                # Selected fighter retains champion attribute
                fighter_list[fighter_one].set_no_contest(fighter_list[fighter_one].get_no_contest() + 1)
                fighter_list[fighter_two].set_no_contest(fighter_list[fighter_two].get_no_contest() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n48-46 ")
                typingPrint(fighter_list[fighter_one].get_name())
                typingPrint("\n48-46 ")
                typingPrint(fighter_list[fighter_two].get_name())
                typingPrint("\nand 47-47, this fight is considered a draw")

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

        # If rounds passed equal number of allotted rounds and fighter two champion attribute is true
        if rounds_passed == rounds and not fight_over and fighter_list[fighter_two].get_champion():

            # If fighter two object health minus object endurance attribute is less than selected fighter's health minus object endurance attribute
            if fighter_two_hp - fighter_list[fighter_two].get_endurance() < fighter_one_hp - fighter_list[fighter_one].get_endurance():

                # Selected fighter object wins by decision and gains true champion attribute
                # Change object attributes
                fighter_list[fighter_one].set_champion(True)  # Selected fighter object champion attribute is set to true
                fighter_list[fighter_one].set_wins(fighter_list[fighter_one].get_wins() + 1)  # Increment selected fighter object wins attribute by 1
                fighter_list[fighter_two].set_champion(False)  # fighter two object champion attribute is set to false
                fighter_list[fighter_two].set_losses(fighter_list[fighter_two].get_losses() + 1)  # Increment second fighter object losses attribute by 1

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND NEW AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_one].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if reverse is true
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() < fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Fighter two object wins by decision and retains champion attribute
                # Increment wins and losses for victor and loser objects
                fighter_list[fighter_one].set_losses(fighter_list[fighter_one].get_losses() + 1)
                fighter_list[fighter_two].set_wins(fighter_list[fighter_two].get_wins() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest ")
                typingPrint(score)
                typingPrint(" for the winner, by unanimous decision")
                typingPrint("\nAND STILL AFC Undisputed ")
                typingPrint(fighter_list[fighter_one].get_weight_class())
                typingPrint(" champion of the world... \n")
                typingPrint(fighter_list[fighter_two].get_name())

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break

            # Else if both object health minus endurance is equal
            elif fighter_one_hp - fighter_list[fighter_one].get_endurance() == fighter_two_hp - fighter_list[fighter_two].get_endurance():

                # Fight is considered a draw
                # Increment both fighter two and selected fighter object no contest attribute by 1
                # Fighter two object retains champion attribute
                fighter_list[fighter_one].set_no_contest(fighter_list[fighter_one].get_no_contest() + 1)
                fighter_list[fighter_two].set_no_contest(fighter_list[fighter_two].get_no_contest() + 1)

                # End of fight announcement
                typingPrint("Ladies and Gentlemen, after ")
                typingPrint(str(rounds))
                typingPrint(" rounds we go to the judges score cards for a decision")
                typingPrint("\nall three judges score this contest \n48-46 ")
                typingPrint(fighter_list[fighter_one].get_name())
                typingPrint("\n48-46 ")
                typingPrint(fighter_list[fighter_two].get_name())
                typingPrint("\nand 47-47, this fight is considered a draw")

                game_menu(fighter_list, fighter_one)  # Send user back to menu
                break


# Main Functions

def main():
    fighter_list = []  # Python List / Replaces C/C++ Vectors and acts like Java's ArrayLists

    selected_fighter = 4
    # NEW: Reads JSON file and creates objects from JSON Objects
    f = open('fighters.json', encoding="utf8")
    data = json.load(f)

    # For each object in JSON file, create a fighter object and insert into fighter_list array
    for i in data['Fighters']:
        json_object = i
        a_fighter = Fighter(json_object["ID"], json_object["firstName"], json_object["surName"], json_object["gender"],
                            json_object["nation"], json_object["fightingOut"], json_object["style"], json_object["age"],
                            json_object["weight"], json_object["height"], json_object["strength"], json_object["speed"],
                            json_object["endurance"], json_object["subOffence"], json_object["subDefence"],
                            json_object["won"], json_object["lost"], json_object["noContest"],
                            json_object["weightclass"], json_object['champion'])
        fighter_list.append(a_fighter)

    menu(fighter_list, selected_fighter)  # Execute menu function


def menu(fighter_list, selected_fighter):

    # Display Menu
    print("\n|==========================================================|\n|                   BunnyCorp MMA Game     "
          "                |\n|==========================================================|\n|     1. Add Fighters     "
          "                                 |\n|     2. View Fighters                                     |\n|     3. "
          "Play Game                                         |\n|     0. Exit Game                                    "
          "     |\n|==========================================================|")

    choice = input("\nPlease select an option.\n")  # Get user input

    # Switch Case Menu
    match choice:
        case '1':  # Create a fighter
            last_elem = operator.itemgetter(-1)(fighter_list)  # Get last object in list
            last_id = last_elem.get_id() + 1  # Increment last ID in list by 1
            print("|==================== Create a Fighter ====================|")  # Create a fighter menu
            first_name = input("\n --- Insert your fighter's first name. --- \n")  # Get user input for name
            second_name = input("\n --- Insert your fighter's last name. --- \n")  # Get user input for last name

            # Validate gender
            while True:
                gender = input("\n --- Insert your fighter's gender. --- \n")  # Get user input for gender
                gender = gender.capitalize()  # Allows console to accept lower case name
                try:
                    gender = str(gender)
                except(Exception,):
                    print("Invalid!")
                if gender.isdigit():
                    print("\nEnter non numeric input.\n")  # Validates only text
                    continue  # Continue unless given valid input
                if gender != 'Male' and gender != 'Female':  # Validates only real inputs
                    print("Please enter valid input")
                    continue  # Continue unless given valid input
                break

            nation = input("\n --- Insert your fighter's home country. --- \n")  # Get user input for country
            fighting_out = input("\n --- Insert your fighter's city. --- \n")  # Get user input for city
            style = input("\n --- Insert your fighter's fighting style. --- \n")  # Get user input for fighting style

            while True:
                age = input("\n --- Insert your fighter's age. --- \n")  # Get user input for age
                try:
                    age = int(age)
                except(Exception,):
                    print("\nEnter numeric digits.\n")  # Validates numeric inputs
                    continue
                if age < 17 or age > 50:  # Validate age requirements
                    print("\nToo young or old, please enter an age between 17 and 50\n")
                    continue
                break

            while True:
                weight = input("\n --- Insert your fighter's weight in kg. --- \n")  # Get user input for weight
                try:
                    weight = int(weight)
                except(Exception,):
                    print("\nEnter numeric digits.\n")  # Validates numeric input
                    continue
                if weight < 1:
                    print("\nPlease enter a positive value\n")  # Validates positive integer
                    continue
                break

            while True:
                height = input("\n --- Insert your fighter's height in cm. --- \n")  # Get user input for height
                try:
                    height = int(height)
                except(Exception,):
                    print("\nEnter numeric digits.\n")  # Validates numeric input
                    continue
                if height < 1:
                    print("\nPlease enter a positive value\n")  # Validates positive integer
                    continue
                break

            # Based on user weight input, generates accurate weightclass
            if 93 <= weight <= 120 and gender == "Male":
                weightclass = "Heavyweight"
            elif 84 <= weight <= 92 and gender == "Male":
                weightclass = "Light Heavyweight"
            elif 77 <= weight <= 83 and gender == "Male":
                weightclass = "Middleweight"
            elif 70 <= weight <= 76 and gender == "Male":
                weightclass = "Welterweight"
            elif 66 <= weight <= 69 and gender == "Male":
                weightclass = "Lightweight"
            elif 61 <= weight <= 65 and gender == "Male":
                weightclass = "Featherweight"
            elif 57 <= weight <= 60 and gender == "Male":
                weightclass = "Bantamweight"
            elif 52 <= weight <= 56 and gender == "Male":
                weightclass = "Flyweight"
            elif 61 <= weight <= 66 and gender == "Female":
                weightclass = "Featherweight"
            elif 57 <= weight <= 60 and gender == "Female":
                weightclass = "Bantamweight"
            elif 52 <= weight <= 56 and gender == "Female":
                weightclass = "Flyweight"
            elif 0 <= weight <= 51 and gender == "Female":
                weightclass = "Strawweight"

            # Creates new fighter object based on user input
            new_fighter = Fighter(last_id, first_name, second_name, gender, nation, fighting_out, style, age, weight,
                                  height, 30, 30, 30, 30, 30, 0, 0, 0, weightclass, False)

            fighter_list.append(new_fighter)  # Inserts new object into fighter_list array
            menu(fighter_list, selected_fighter)  # Sends user to menu

        case '2':
            # List all fighters

            # For each object in fighter_list array, print out object attributes
            for obj in fighter_list:
                print("\n|========================= Fighter ========================|\n")
                if obj.get_champion():  # If fighter object champion attribute is true
                    status = obj.get_weight_class() + " Champion"  # Change status string to weight class + champion
                else:
                    status = "None"  # Else status string = none
                print(obj.get_name(), "\nFrom: ", obj.get_nation(), "\nFighting out of:", obj.get_fighting_out(),
                      "\nFight Style:", obj.get_style(), "\nAge: ", obj.get_age(), "\nWeight: ", obj.get_weight(),
                      "kg", "\nHeight:", obj.get_height(), "cm", "\nStrength: ", obj.get_strength(), "\nSpeed:",
                      obj.get_speed(), "\nEndurance:", obj.get_endurance(), "\nTakedown Defence:",
                      obj.get_sub_defence(), "\nSubmission Offence:", obj.get_sub_offence(), "\nWins:",
                      obj.get_wins(), "\nLosses:", obj.get_losses(), "\nNo Contests:", obj.get_no_contest(),
                      "\nTitles:", status)
                continue
            menu(fighter_list, selected_fighter)  # Send user to menu
        case '3':
            # Send user to game menu
            game_menu(fighter_list, selected_fighter)
        case '0':
            # Close program
            exit(0)


# Training function
def trainer_menu(fighter_list, selected_fighter):

    # Display menu options
    choice = input(
        "\n1 : Strength\n2 : Speed\n3 : Endurance\n4 : Submission Offence\n5 : Submission Defence \n6 : View Stats \n7 : Back \n")

    match choice:

        case '1':  # Strength training
            if game_maths(0.80):  # 80% chance of successful training session
                if fighter_list[selected_fighter].get_strength() != 100:  # If strength isn't maxed out
                    training_strength = fighter_list[selected_fighter].get_strength()  # Get selected fighter object's strength
                    fighter_list[selected_fighter].set_strength(training_strength + 1)  # Increase strength by 1
                    print("Strength increased from:", training_strength, "to",  # Display results
                          fighter_list[selected_fighter].get_strength())
                else:
                    print("\nFighter at max strength!")  # If object strength attribute is maxed out, display message
            else:  # if false is returned, accident at gym is triggered
                if fighter_list[selected_fighter].get_strength() != 0:  # If object strength doesn't equal 0
                    training_strength = fighter_list[selected_fighter].get_strength()  # Get selected fighter object's strength
                    fighter_list[selected_fighter].set_strength(training_strength - 1)  # Decrease strength by 1
                    print("Accident at GYM!", "\nStrength decreased from:", training_strength, "to",  # Display results
                          fighter_list[selected_fighter].get_strength())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '2':  # Speed training
            if game_maths(0.80):  # 80% chance of successful training session
                if fighter_list[selected_fighter].get_speed() != 100:  # If speed isn't maxed out
                    training_speed = fighter_list[selected_fighter].get_speed()  # Get selected fighter object's speed
                    fighter_list[selected_fighter].set_speed(training_speed + 1)  # Increase speed by 1
                    print("Speed increased from:", training_speed, "to",  # Display results
                          fighter_list[selected_fighter].get_speed())
                else:
                    print("\nFighter at max speed!")  # If object speed attribute is maxed out, display message
            else:  # if false is returned, accident at gym is triggered
                if fighter_list[selected_fighter].get_speed() != 0:
                    training_speed = fighter_list[selected_fighter].get_speed()  # Get selected fighter object's speed
                    fighter_list[selected_fighter].set_speed(training_speed - 1)  # Decrease speed by 1
                    print("Accident at GYM!", "\nSpeed decreased from:", training_speed, "to",  # Display results
                          fighter_list[selected_fighter].get_speed())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '3':  # Endurance training
            if game_maths(0.80):  # 80% chance of successful training session
                if fighter_list[selected_fighter].get_endurance() != 100:  # If endurance isn't maxed out
                    training_endurance = fighter_list[selected_fighter].get_endurance()  # Get selected fighter object's endurance
                    fighter_list[selected_fighter].set_endurance(training_endurance + 1)  # Increase endurance by 1
                    print("Endurance increased from:", training_endurance, "to",  # Display results
                          fighter_list[selected_fighter].get_endurance())
                else:
                    print("\nFighter at max endurance!")  # If object endurance attribute is maxed out, display message
            else:  # if false is returned, accident at gym is triggered
                if fighter_list[selected_fighter].get_endurance() != 0:
                    training_endurance = fighter_list[selected_fighter].get_endurance()  # Get selected fighter object's endurance
                    fighter_list[selected_fighter].set_endurance(training_endurance - 1)  # Decrease endurance by 1
                    print("Accident at GYM!", "\nEndurance decreased from:", training_endurance, "to",  # Display results
                          fighter_list[selected_fighter].get_endurance())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '4':  # Submission offence training
            if game_maths(0.80):  # 80% chance of successful training session
                if fighter_list[selected_fighter].get_sub_offence() != 100:  # If submission offence isn't maxed out
                    training_submission_offence = fighter_list[selected_fighter].get_sub_offence()  # Get selected fighter object's sub offence
                    fighter_list[selected_fighter].set_sub_offence(training_submission_offence + 1)  # Increase sub offence by 1
                    print("Submission offence increased from:", training_submission_offence, "to",  # Display results
                          fighter_list[selected_fighter].get_sub_offence())
                else:
                    print("\nFighter at max submission offence!")  # If object submission offence attribute is maxed out, display message
            else:  # if false is returned, accident at gym is triggered
                if fighter_list[selected_fighter].get_sub_offence() != 0:
                    training_submission_offence = fighter_list[selected_fighter].get_sub_offence()  # Get selected fighter object's sub offence
                    fighter_list[selected_fighter].set_sub_offence(training_submission_offence - 1)  # Decrease sub offence by 1
                    print("Accident at GYM!", "\nSubmission offence decreased from:", training_submission_offence, "to",  # Display results
                          fighter_list[selected_fighter].get_sub_offence())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '5':  # Submission defence training
            if game_maths(0.80):  # 80% chance of successful training session
                if fighter_list[selected_fighter].get_sub_defence() != 100:  # If submission defence isn't maxed out
                    training_submission_defence = fighter_list[selected_fighter].get_sub_defence()  # Get selected fighter object's sub defence
                    fighter_list[selected_fighter].set_sub_defence(training_submission_defence + 1)  # Increase sub defence by 1
                    print("Submission defence increased from:", training_submission_defence, "to",  # Display results
                          fighter_list[selected_fighter].get_sub_defence())
                else:
                    print("\nFighter at max submission defence!")  # If object submission defence attribute is maxed out, display message
            else:  # if false is returned, accident at gym is triggered
                if fighter_list[selected_fighter].get_sub_defence() != 0:
                    training_submission_defence = fighter_list[selected_fighter].get_sub_defence()  # Get selected fighter object's sub defence
                    fighter_list[selected_fighter].set_sub_defence(training_submission_defence - 1)  # Decrease sub defence by 1
                    print("Accident at GYM!", "\nSubmission defence decreased from:", training_submission_defence, "to",  # Display results
                          fighter_list[selected_fighter].get_sub_defence())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '6':  # View selected object's current attribute stats
            print("Current Fighter Skills: \n Strength: ", fighter_list[selected_fighter].get_strength(), "\n Speed: ",
                  fighter_list[selected_fighter].get_speed(), "\n Endurance: ",
                  fighter_list[selected_fighter].get_endurance(), "\n Submission Offence: ",
                  fighter_list[selected_fighter].get_sub_offence(), "\n Submission Defence: ",
                  fighter_list[selected_fighter].get_sub_defence())
            trainer_menu(fighter_list, selected_fighter)  # Send user back to training menu

        case '7':
            game_menu(fighter_list, selected_fighter)  # Go back to game menu


# Game menu function
def game_menu(fighter_list, selected_fighter):

    print(  # Display menu
        '\n|==========================================================|\n|'
        '                   BunnyCorp MMA Game                     |\n'
        '|==========================================================|\n|'
        '     1. Pick Fighter                                      |\n|'
        '     2. Train Fighters                                    |\n|'
        '     3. Fight                                             |\n|'
        '     4. Main Menu                                         |\n'
        '|==========================================================|\n')

    print("Currently selected fighter: ", fighter_list[selected_fighter].get_name())  # Tell user of currently selected fighter
    choice = input("\nPlease select an option.\n")  # Get user menu input

    match choice:
        case '1':  # Select fighter object
            print("\n|========================= Fighter ========================|\n")
            for obj in fighter_list:  # For each object in fighter list array, display object attributes
                print("Index:", str(fighter_list.index(obj)).ljust(3), "| Gender:", obj.get_gender().ljust(6),
                      "| Weightclass:", obj.get_weight_class().ljust(17), "| Name:",
                      obj.get_name())  # Used zfill for index, replaced to ljust for UX

            while True:
                selected_fighter = input("\nPlease select a fighter (Index)")  # Get user input for fighter object selection
                try:
                    selected_fighter = int(selected_fighter)  # Selected fighter = input
                except(Exception,):
                    print("\nEnter numeric digits.\n")  # Validates for numeric inputs
                    continue
                break
            print("You have selected:", fighter_list[selected_fighter].get_name())  # Prints out selected fighter
            game_menu(fighter_list, selected_fighter)  # Sends user back

        case '2':  # Sends user to training function
            trainer_menu(fighter_list, selected_fighter)
        case '3':  # Sends user to fight menu
            fight_menu(fighter_list, selected_fighter)
        case '4':  # Sends user to main menu
            menu(fighter_list, selected_fighter)


# Fight menu function
def fight_menu(fighter_list, selected_fighter):
    print("\n|========================= Fighters ========================|\n")
    for obj in fighter_list:  # For each object in fighter list array, display object attributes
        if fighter_list[selected_fighter].get_weight_class() == obj.get_weight_class() and fighter_list[selected_fighter].get_gender() == obj.get_gender():  # Only shows fighter objects, selected fighter can fight
            print("Index |", str(fighter_list.index(obj)).ljust(3), obj.get_name(), "| Sex:", obj.get_gender().ljust(6), "| WC:", obj.get_weight_class().ljust(17),
                  "\nStats | Str:", obj.get_strength(), "| Spd:", obj.get_speed(), "| End:", obj.get_endurance(), "| Sub-Off:", obj.get_sub_offence(), "| Sub-Def:", obj.get_sub_defence(),
                  "\nRecord| W:", obj.get_wins(), "L:", obj.get_losses(), "NC:", obj.get_no_contest(), "\nChampion:", obj.get_champion(), "\n")

    while True:
        choice = input("Select a fighter from index: ")  # Get user input for selected fighter object opponent object
        try:
            choice = int(choice)  # Input equals opponent object index
        except(Exception,):
            print("\nEnter numeric digits.\n")  # Validates numeric input
            continue
        if choice == selected_fighter:  # Validates same fighter object
            print("\n You cannot select the same fighter!")
            continue
        if fighter_list[choice].get_gender() == "Female" and fighter_list[selected_fighter].get_gender() == "Male":  # Validates object gender and prevents mixed gender fights
            print("\n You cannot have mixed gender fights!")
            continue
        if fighter_list[choice].get_weight_class() != fighter_list[selected_fighter].get_weight_class():  # Validates object weight class and prevents mixed weight class fights
            print("\n You cannot have mixed weight classes!")
            continue
        fight_function(fighter_list, selected_fighter, choice)  # Executes fight function with given parameters
        break


main()  # Start program
