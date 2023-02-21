
class Player:

    players = [] #CLASS LEVEL ATTRIBUTE

    def __init__(self, hp, profession) -> None:
        self.hp = hp
        self.proffesion = profession
        Player.players.append(self)
        
        # INSTANCE LEVEL METHOD

    def displayHealth(self):
        print(self.hp)

    def takeDamage(self, damage):
        self.hp -= damage
        if(self.hp <= 0):
            print(f'You have been killed!')
            return
        print(f"You've been attacked! Your new hp is {self.hp}")

        # CLASS LEVEL METHOD
    
    @classmethod
    def load(cls):
        pass

    

# CODING CHALLENGE

'''
    create an app that you give a date and it tells you what day of the week it will be on
'''
        