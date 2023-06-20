def friend(names):
    friends = []
    for name in names:
        if len(name) == 4:
            friends.append(name)
    return friends
names = ["Ryan", "Kieran", "Jason", "Yous"]
second_names = friend(names)
print(second_names)