import functions

loadedfile = functions.pull_file(filename='data.json')
while True:
    price = functions.validation('Price: ', convert_type=float,  loadedfile=loadedfile)
    length = len(str(price))
    print(f"O tamanho de {price} é = {length}")
discount = int(input('Discount: '))
moneyofdiscount = price*discount/100
total = price - moneyofdiscount
print(price)
print(moneyofdiscount)
print(total)