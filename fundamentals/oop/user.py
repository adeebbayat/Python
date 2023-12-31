class User():

    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        if (self.is_rewards_member == True):
            print("User already a member.")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self,amount):
        if(self.gold_card_points < amount):
            print('You got no cash boi')
        else:
            self.gold_card_points -= amount
        return self

user1 = User("Chad","Brad","chadbrad@gmail.com",22)

user1.spend_points(50).enroll().display_info()



user2= User("Sarah","Johnson","sarahjohnson@yahoo.com",34)

user2.enroll()
user2.spend_points(80)
user2.display_info()

user3 = User("John","Smith","johnsmith@hotmail.com",80)

user3.display_info()
user3.spend_points(40)
