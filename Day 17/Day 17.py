class User:
   # pass #just to skip it for now, will add logic later
    def __init__(self, user_id, username): #constructor
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# PascalCase
# camelCase
# snake_case

user_1 = User("001", 'Jeca')
user_2 = User("002", "Mire")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

