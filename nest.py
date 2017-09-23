users=[]
new_user={
    'last':'sam',
    'first':'dengima',
    'username':"dengsam"
}

users.append(new_user)

new_user={
    'last':'emma',
    'first':'iranya',
    'username':"irasa"
}
users.append(new_user)
print(users)

for user_dict in users:
    for k, v in user_dict.items():
        print(k + ":" + v)
    print("\n")


