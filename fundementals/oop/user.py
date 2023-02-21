from player import Player

class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        rewards_member_string = 'No'
        if(self.is_rewards_member == True):
            rewards_member_string = 'Yes'
        print('----------')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.first_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Rewards Member: {rewards_member_string}')
        print(f'Gold Card Points: {self.gold_card_points}')
        print('----------')

        return self

    def enroll(self):
        if(self.is_rewards_member == False):
            self.is_rewards_member = True
            self.gold_card_points = 200
            return
        print('You are already enrolled...')

        return self

    def spend_points(self, amount):
        if(self.gold_card_points - amount < 0):
            print("You don't have enough points...")
        else:
            self.gold_card_points -= amount
            print(f'Thanks {self.first_name}! You just spent {amount} points. We hope you enjoy your reward!')
            print(f'Your new reward point balance is {self.gold_card_points}')

        return self

        

spencer_wind = User('Spencer','Wind','swind03@gmail.com',19)
spencer_wind.display_info().enroll()

issac_burnside = User('Isaac','Burnside','ikeburny@fake.com',22)
casey_partin = User('Casey','Partin','cmpartin@notreal.com',21)

spencer_wind.spend_points(50)
issac_burnside.enroll().spend_points(80)

spencer_wind.display_info()
issac_burnside.display_info()
casey_partin.display_info()

spencer_wind.enroll()

casey_partin.spend_points(40)

Patriot453 = Player(100, 'architect')

Patriot453.displayHealth()
Patriot453.takeDamage(25)
Patriot453.takeDamage(50)
Patriot453.takeDamage(50)