dict = {}
input = [9,3,9,3,9,7,9]


for item in input:
    try:
        if dict[item]:
            del dict[item]
            print('Foi e tem')

    except KeyError:
        print('Exception')
        dict[item] = item

print(dict.values())