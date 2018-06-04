#beispiel1.py
def pruefziffer(code):
    check = (98-((int(code))%97))
    return check

land = "AT"
blz = "38282"
konto = "3026713"

kontolen = 11


if(len(konto) != kontolen):
    difference = kontolen-len(konto)
    for i in range(len(konto), kontolen):
        konto = "0" + konto
numbers = blz+konto
counter = 0
iban=blz+konto+"1029"+"00"
check = pruefziffer(iban)
print(check)
print(land + str( check), end = " ")



for i in range(0, len(numbers)):
    counter += 1
    print(numbers[i], end = "")
    if(counter == 4):
        print(" ", end = "")
        counter = 0

