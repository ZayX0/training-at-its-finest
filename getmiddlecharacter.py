def get_middle(s):
    numChar = len(s)
    if numChar % 2 == 0:
        splitEven = list(s)
        middleCharE = numChar / 2
        finalMaybe = (splitEven[int(middleCharE - 1):int(middleCharE + 1)])
        final = finalMaybe[0] + finalMaybe[1]
        return final
    else:
        middleChar = numChar / 2

print(get_middle('thisd'))
