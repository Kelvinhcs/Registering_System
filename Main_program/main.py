import functions
filename = 'data.json'
while True:
    functions.header(' Welcome to our registering System ')
    print("""[1] Register new products
[2] View current products
[3] Set stock quantity
[4] Exit the program""")
    Main_Choice = functions.validation("What's is your choice?: ", convert_type=int)
    print('='*117)
    
    
    if Main_Choice == 1:
        functions.new_products_register()
        
        
    elif Main_Choice == 2:
        Second_Choice = functions.show_past_registers(filename)
        if Second_Choice == None or Second_Choice == [] or Second_Choice == '' or Second_Choice == {}:
            continue
        else:
            print(functions.explainingheader)
            for item in Second_Choice:
                print(f'{item["Name"]:^28}|{item["Distributor"]:^25}|{item["Original Price"]:^22.2f}| {item["Discount Percentage"]:<5}% - {item["Discount Money"]:<9.2f}|{item["Final Price"]:^19.2f}')
                
                
    elif Main_Choice == 3:
        functions.change_file_stock()
        
        
    elif Main_Choice == 4:
        functions.wayout()

