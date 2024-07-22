import functions
while True:
    print("""[1] Register new products
[2] View current products
[3] Set stock quantity
[4] Exit the program""")
    Main_Choice = functions.validation("What's is your choice?: ", convert_type=int)
    if Main_Choice == 1:
        functions.new_products_register()
    elif Main_Choice == 2:
        functions.show_past_registers()
    elif Main_Choice == 3:
        functions.change_stock()
    elif Main_Choice == 4:
        functions.wayout()

