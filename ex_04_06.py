hrs = input("How many hours did you work: ")
h = float(hrs)
pay = input("What is your payrate: ")
p = float(pay)

def computepay(payamount, hours):
    OThours = hours - 40
    OTpay = payamount * 1.5
    OTamount = OTpay * OThours
    TotalOTWage = (40 * payamount) + OTamount
    return TotalOTWage

if h > 40:
    print(computepay(p,h))
else:
    print(h * p)
