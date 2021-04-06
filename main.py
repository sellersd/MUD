from random import randint
from random import choice as ch

class Character():
    def __init__(self, name = ''):
        if name == '':
            self.name = 'Hardy Hedgehog'
        else:
            self.name = name
        self.health = 100
        self.strength = 50
        self.defense = 30
        print(self.name)


    def __del__(self):
        print('destroyed')


    def attack(self, opponent):
        self.d100 = randint(1, 101)
        self.total = self.strength - opponent.defense + self.d100
        if self.total > 100:
            self.dmg = self.total - 100
        else:
            self.dmg = 0

        opponent.health -= self.dmg
        print(self.strength, '-', opponent.defense,
                '+',  self.d100, '=', self.total)
        print(opponent.name, 'has', opponent.health, 'remaining.')

        if opponent.health <= 0:
            opponent.kill()
        elif self.health <= 0:
            self.kill()


    def kill(self):
        print(self.name, 'has died!')




class Room():
    def __init__(self, chars):
        self.description = ch(self.rooms)
        self.chars_in_room = chars

    def show_description(self):
        print(self.description)
        print('Also in the room: ', end = ' ')
        for char in self.chars_in_room:
            print(char.name, end = ', ')
        print()

    rooms = ['A cold, dark, smelly dungeon.',
            'A haunted forest.',
            'A scorching desert.',
            'A dark alley.',
            'A school hallway.']

commands = ['attack', 'camp', 'rest', 'help', 'look']
commands_desc = ['attack <target>, causes you to attack the given target',
                 'camp, you will camp for the night causing you to leave the game',
                 'rest, a brief rest that restores your health',
                 'help, displays this message',
                 'look, shows the room description along with any creatures and treasure present']


def WelcomeScreen():
    print('Welcome to the Arena! For a list of commands type \'help\'.')

def help():
    print('Helpful commands:')
    for cmd in commands:
        print(cmd, '\t', )

def main():
    WelcomeScreen()

    hero_name = input('Enter your name: ')
    hero = Character(hero_name)
    m1 = Character()
    room = Room([hero, m1])

    print(room.description)
    playing = True

    while playing:
        cmd = input('> ')
        if cmd == 'attack':
            while(hero.health > 0 and m1.health > 0):
                print(hero.name, 'attacks', m1.name, '!')
                hero.attack(m1)
                if m1.health < 0:
                    print(m1.name, 'has died!')
                    del m1
                else:
                    print(m1.name, 'attacks', hero.name, '!')
                    m1.attack(hero)
                    if hero.health < 0:
                        print(hero.name, 'has died!')
                        
        elif cmd == 'look':
            room.show_description()
        elif cmd == 'rest':
            print('You lay down to rest.')
            hero.health = 100
            print('You wake up feeling refreshed. You now have',
                    hero.health, 'health.')

        elif cmd == 'camp':
            print('You make camp for the night.')
            playing = False
        elif cmd == 'help':
            help()
        else:
            print('I do not know how to do that.')
            cmd = input('> ')
if __name__ == "__main__":
    main()
