def cannons_ready(gunners):
    counter = 0
    for val in gunners.values():
        if val == 'nay':
            counter = 1
            break
        else:
            continue
    return counter

result = cannons_ready({'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'})

if result == 1:
    print('Shiver me timbers!')
else:
    print('Fire!')
