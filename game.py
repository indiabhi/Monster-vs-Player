from character import Character
from monsters import Dragon, Troll, Goblin

import sys

class Game(object):
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print "Monster just attacked Do u wanna dodge?"
            dodge_or_what = input("[Y]es or [N]o")
            if dodge_or_what.lower == "y":
                if self.player.dodge():
                    print "Dodge succesful!"
                else:
                    print "You were attacked"
                    self.player.hit_points -= 1
        else:
            print "Monster did not attack!"

    def player_turn(self):
        print "Do u wanna [A]ttack, [R]est or [Q]uit"
        player_action = input()
        if player_action.lower == "a":
            if self.player.attack:
                print "Attack Successful"
                if self.monster.dodge():
                    print "Monster Dodged!"
                else:
                    self.monster.hit_points -= 1
            else:
                print "Attack not Good Enough"
        elif player_action.lower == "r":
            self.player.rest()
        elif player_action.lower == "q":
            sys.exit()
        else:
            # self.player_turn()
            pass

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.experience += 1
            print "You have upped your experience!"
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()
        while self.player.hit_points and(self.monster or self.monsters):
            print "\n"+ "="*20
            print self.player
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print "You win!"
        elif self.monster or self.monsters:
            print "You lose!"
        sys.exit()

Game()
