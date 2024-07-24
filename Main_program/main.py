import functions
from time import sleep
filename = 'data.json'
loadedfile = functions.pull_file(filename)
functions.header(' Welcome to our registering System ')
while True:
    print("""[1] Register new products
[2] See products already registered
[3] Update past registers
[4] Send the new session items to the File
[5] Exit the program""")
    while True:
        Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile, MaxLength=1)
        if Main_Choice in (1,2,3,4,5):
            break
        else:
            print('\033[31mUnsupported option. Please, try another one...\033[m')
        
    #Registering Area
    if Main_Choice == 1:
        print('-'*117)
        functions.new_products_register(loadedfile)
        
    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        print()
        functions.header('Stock Management', character='-')
        Second_Choice = functions.return_file_data(filename)
        if Second_Choice == None or Second_Choice == [] or Second_Choice == '' or Second_Choice == {}:
            print('Nothing returned to us, sorry')
        else:
            print(functions.explainingheader)
            for item in Second_Choice:
                print(f'\033[32m{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
            functions.print_session_saveds_red()
            print('-'*117)
            sleep(2)
        print()


    #Changing any previous information           
    elif Main_Choice == 3:
        print('-'*117)
        functions.update_data()
        
 
    #A way to save the session data on the file without needing to exit the program    
    elif Main_Choice == 4:
        if functions.session == []:
            functions.header("We don't have any data on current sesion to be saved.", character='*')
        else:
            print()
            functions.header(f'{"Session data":^117}', character='-')
            print(functions.explainingheader)
            functions.print_session_saveds_red()
            print('-'*117)
            print()
            print("\033[32m[1] Send the informations saved localy to the File\033[m\n\033[31m[2] Send all later\033[m")
            while True:
                choice = functions.validation("What is your choice?: ", loadedfile=loadedfile, MaxLength=1, convert_type=int)
                if choice in (1,2):
                    break
            if choice == 1:
                functions.save_on_file(loadedfile=loadedfile, filename=filename)
                pass
            if choice == 2:
                pass
        
    #DONE  
    elif Main_Choice == 5:
        print('='*117)
        functions.wayout(loadedfile)

    functions.header("Products Register")
#NEW FEATURES
#allow the user to change any information. Based on that, consider a separated option to just update the stock and the promotion 
#Consider removing the welcome everytime you get back to the home page
#Consider add a manual saving without the need to exit 

#THINK LATER: Do we really need to save that many informations on the file?