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
    while True:
        Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile, MaxLength=1)
        if Main_Choice in (1,2,3,4):
            break
        else:
            print('\033[31mUnsupported option. Please, try another one...\033[m')
        
    #Registering Area
    if Main_Choice == 1:
        print('='*117)
        functions.new_products_register(loadedfile)
        
    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        print()
        functions.header('Stock Management', character='*')
        Second_Choice = functions.return_file_data(filename)
        if Second_Choice == None or Second_Choice == [] or Second_Choice == '' or Second_Choice == {}:
            print('Nothing returned to us, sorry')
        else:
            print(functions.explainingheader)
            for item in Second_Choice:
                print(f'\033[32m{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
            functions.print_session_saveds_green()
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
#allow the user to change any information. Based on that, consider a separated option to just update the stock and the promotion 
#Consider removing the welcome everytime you get back to the home page
#Consider add a manual saving without the need to exit 

#THINK LATER: Do we really need to save that many informations on the file?