hrs = input("How many hours did you work: ")
h = float(hrs)
pay = input("What is your payrate: ")
p = float(pay)

if h > 40:
    OThours = h - 40
    OTpay = p * 1.5
    OTamount = OTpay * OThours
    TotalOTWage = (40 * p) + OTamount
    print(TotalOTWage)
else:
    Normalpay = h * p
    print(Normalpay)
