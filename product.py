material = input("material: ").lower()
print()
available = dict()
availablePrices = list()
notSorted = dict()
check = False

fp = open("product_material.txt", "r")

for line in fp.readlines():
    line = line[:-1].split(',')
    price = float(line[3][1:])

    if line[2].lower() == material and line[4] == "true":
        #print(line[4], price)
        available[price] = line    # potential bug if there are 2 things with the same price
        #print(line)               # it will not add new key-value pair, it will replace value in the existing key
	
        availablePrices.append(price)
        notSorted[line[0]] = price
        check = True

fp.close()

if check:
    print()
    # available = sorted(available)     # list with sorted keys [price, price, price, ...]
    available = sorted(available.items())   # [(price, [line]), (price, [line]), (price, [line]), ...]
    # it sorts by key (price)

    for i in available:
        #print(i)        # (price, [line])
        print(i[1])

    print()
    print(sorted(availablePrices))
    print()
    print(notSorted)
else:
    print("There is no any product made of '{}'".format(material))