import functions
from time import sleep
filename = 'data.json'
loadedfile = functions.pull_file(filename)
while True:
    functions.header(' Welcome to our registering System ')
    print("""[1] Register new products
[2] View current products
[3] Update any information
[4] Exit the program""")
    Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile)
    
    #Registering Area
    if Main_Choice == 1:
        print('='*117)
        functions.new_products_register(loadedfile)
        
    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        print()
        functions.header('Stock Management', character='*')
        Second_Choice = functions.show_past_registers(filename)
        if Second_Choice == None or Second_Choice == [] or Second_Choice == '' or Second_Choice == {}:
            print('Nothing returned to us, sorry')
        else:
            print(functions.explainingheader)
            for item in Second_Choice:
                print(f'\033[32m{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>5}% - {item["Discount Money"]:<9.2f}|{item["Final Price"]:^19.2f}\033[m')
            functions.show_session_saveds()
            print('*'*117)
            sleep(2)
        print()


    #Changing any previous information           
    elif Main_Choice == 3:
        print('='*117)
        functions.update_data()
        
    #DONE  
    elif Main_Choice == 4:
        print('='*117)
        functions.wayout(loadedfile)


#NEW FEATURES
#allow the user to change any information
