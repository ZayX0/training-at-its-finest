score = input('Insert a score between 0.0 and 1.0: ')

try:
    Testscore = float(score)
except:
    print('That is not a valid number')
    quit()

if 0.0 <= Testscore <= 1.0:
    if Testscore >= 0.9:
        print('A')
    elif Testscore >= 0.8:
        print('B')
    elif Testscore >= 0.7:
        print('C')
    elif Testscore >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('That score is out of range')
