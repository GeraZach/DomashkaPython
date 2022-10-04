Trash_list = []
Glass_list = ['beer_bottle', 'vodka_bottle']
Metal_list = ['wrench_metal']
Wood_list = ['chair_wood']
Trash_list.extend(Glass_list)
Trash_list.extend(Metal_list)
Trash_list.extend(Wood_list)

Trash_list.sort()
Glass_list.sort()
Metal_list.sort()
Wood_list.sort()

operationType = str(input('insert operation type'))

if operationType == 'find':
    TrashType = str(input('type trash type'))
    if TrashType == 'glass':
        print(Glass_list)
    elif TrashType == 'wood':
        print(Wood_list)
    elif TrashType == 'Metal':
        print(Metal_list)
    elif TrashType == 'all':
        print(Trash_list)
    else:
        print('Incorrect type. Try again.')
elif operationType == 'add':
    TrashTypeAdd = str(input('Type type of trash you wanna add'))
    if TrashTypeAdd == 'glass':
        print(Glass_list)
        Glass_list.append(str(input('type a glass item u wanna add')))
        print(Glass_list)
    elif TrashTypeAdd == 'wood':
        print(Wood_list)
        Wood_list.append(str(input('type a wooden item u wanna add')))
        print(Wood_list)
    elif TrashTypeAdd == 'metal':
        print(Metal_list)
        Metal_list.append(str(input('type a metal item u wanna add')))
        print(Metal_list)
    else:
        print('incorrect command')

