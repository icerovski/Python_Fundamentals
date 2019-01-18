# 07. User Logins
logins = {}


def pair_in_dict(key, value):
    if key in logins and value == logins[key]:
        return True


def after_login():
    count = 0
    while True:
        line = input().split(' -> ')
        if line[0] == "end":
            print(f'unsuccessful login attempts: {count}')
            break
        else:
            username = line[0]
            password = line[1]
            if pair_in_dict(username, password):
                print(f'{username}: logged in successfully')
            else:
                count += 1
                print(f'{username}: login failed')
    return


while True:
    line = input().split(' -> ')
    if line[0] == "login":
        after_login()
        break
    else:
        logins[line[0]] = line[1]
