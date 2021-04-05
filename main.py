from random import randint

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

rooms = ['A cold, dark, smelly dungeon.',
        'A haunted forest.',
        'A scorching desert.',
        'A dark alley.',
        'A school hallway.']

commands = ['attack', 'camp', 'rest']
def main():
    hero_name = input('Enter your name: ')
    hero = Character(hero_name)
    m1 = Character()

    playing = True
    while playing:
        cmd = input('> ')
        while(cmd not in commands):
            print('I do not know how to do that.')
            cmd = input('> ')
        if cmd == 'attack':
            while(hero.health > 0 and m1.health > 0):
                print(hero.name, 'attacks', m1.name, '!')
                hero.attack(m1)
                print(m1.name, 'attacks', hero.name, '!')
                m1.attack(hero)
        if cmd == 'rest':
            print('You lay down to rest.')
            hero.health = 100
            print('You wake up feeling refreshed. You now have',
                    hero.health, 'health.')

        if cmd == 'camp':
            print('You make camp for the night.')
            playing = False

if __name__ == "__main__":
    main()
