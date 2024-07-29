import json
from time import sleep
session = [] #variable that will handle all the new registers
explainingheader = f'{"Nº":<3}|{"Product Name":^28}|{"Stock Quantity (Units)":^24}|{"Original Price (US$)":^22}|{"Discount (US$)":^20}|{"Final Price (US$)":^19}' #created just to avoid typing ALL again


#informs that cant be pulled the content of the master file
#if the program runs without reaching the old data, this appears
#that will cause to erase the past data when trying to save the new informations
def error_pulling():
        print('\033[31mBECAREFULL!!! WE CANNOT LOAD THE FILE\033[m')
        print('\033[31mTHE RETURN IS JUST A EMPTY LIST\033[m')
        print('\033[31mIF THE APLICATTION IS ALREDY BEEN USED BY YOU\033[m')
        print("\033[31mWE EXTREMELLY RECOMMEND TO DON'T USE THE APLICATTION\033[m")
        print("\033[31mIF IS YOUR FIRST TIME USING THE APP, PLEASE DISCONSIDER THIS INFO\033[m")
        sleep(4)


#opens the main file and returns to a variable on the main program    
def pull_file(filename, counter=0, error=True):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        if error and counter <= 0:
            error_pulling()
        return []
    except json.JSONDecodeError:
        if error and counter <= 0:    
            error_pulling()
        return []
    

#display the header with the message that you want
def header(msg, character='='):
    print(character*121)
    print(f'{msg:^121}')
    print(character*121)


#everytime the ctrl+c or the exit option be selected this will me trigered    
#if ctrl+c be pressed again it imediatly ends without saving nothing
#otherwise will asks if you wanna save or not
#if the choice was to save, re-write the old data on the file to our varible that has everything that was on the file plus our new data
#if its not, your discard everything you do in the session
def wayout(loadedfile):
    print('\033[31mThe user decided to stop the program...\033[m')
    print()
    print("\033[32m[1] Send the informations saved localy to the File\033[m\n\033[31m[2] Exit without saving\033[m")
    while True:
        try:
            choice = int(input("What's your choice?: "))
        except KeyboardInterrupt: #stop imediatly
            print('\033[31mStopping the program right now...\033[m')
            exit()
        except:
            print('\033[31mERROR! Please type a valid option...\033[m')
        else:
            if choice in (1,2):
                break
    if choice == 1:
        save_on_file(loadedfile) # re-write everything in the file
        exit()
    elif choice == 2:
        print('\033[31mNothing in this session was saved...\033[m')
        exit()

#first put the session things on our variable that hold the entire file
#if all goes right, tries to re-write the main file with our varible that have all the old data + our new sessions saving
#THINK LATER: if nothing was changed we dont need to write it all again on the file.
def save_on_file(loadedfile, filename='data.json'):
    global session
    try:
        for item in session:
            loadedfile.append(item)
    except Exception as error:
        print('\033[31mWe cannot save the session because of this error...\033[m')
        print(error)
    else:
        try:
            with open(filename, 'w') as file:
                json.dump(loadedfile, file, indent=2)
        except Exception as error:
            print('\033[31mNothing in this session was saved...\033[m')
            print(error)
        else:
            session.clear()
            print('\033[32mThis session was completely saved...\033[m')
        

#validation process of inputs that triggers a function when ctrl+c or exit button is pressed
def validation(msg, loadedfile, MaxLength=1, convert_type=str, percentage=False, options=False, start=1, stop=1):
    while True:
        try:
            choice = convert_type(input(msg))
        except KeyboardInterrupt:
            wayout(loadedfile)
        except:
            print('\033[31mERROR! Please type a valid option...\033[m')
        else:
            if percentage == True and choice > 100:
                print('\033[31mERROR! This percentage is above 100%, please try again...\033[m')
                continue
            elif options:
                if choice in range(start, stop+1):
                    return choice
                else:
                    print('\033[31mUnsupported option. Please, try another one...\033[m')
                    continue
            elif len(str(choice).strip()) >= 1 and len(str(choice).strip()) <= MaxLength:
                return choice
            else:
                if convert_type == float:
                    print(f"\033[31mSorry, that name pass the {MaxLength-2} limit characters, try to type it again...\033[m")
                else:
                    print(f"\033[31mSorry, that name pass the {MaxLength} limit characters, try to type it again...\033[m")


#try to register a series of inputs on a dictionary, if its all right append it to the loaded list from the main file     
def new_products_register(loadedfile):
    global session
    while True:
        
        #first of all, get the informations and save on a dictionary
        name = validation('Product name: ', loadedfile, MaxLength=28).strip()
        stock = validation('What is the stock quantity right now?: ', loadedfile, convert_type=int, MaxLength=7)
        price = validation('Product price: US$', convert_type=float, loadedfile=loadedfile, MaxLength=8)
        DiscountPercentage = validation('What percentage of discount will it have now?: ', convert_type=float, loadedfile=loadedfile, MaxLength=5, percentage=True)
        print()
        DiscountMoney = price*DiscountPercentage/100
        finalprice = price - DiscountMoney
        LastTyped = {'Name': name, 'Stock':stock, 'Original Price':price, 'Discount Money':DiscountMoney, 'Discount Percentage':DiscountPercentage, 'Final Price':finalprice}
        
        #here the program will show the last things you wrote in a formated way
        print('='*121)
        print(explainingheader)        
        print(f'{'1  '}|{name:^28}|{stock:^24}|{price:^22.2f}|{DiscountPercentage:>6}% - {DiscountMoney:<10.2f}|{finalprice:^19.2f}')
        print('='*121)
        print()
        
        #if you agree it will save on loaded list from the main file, case you don't it will restart the process
        print('\033[32m[1] Save Locally\033[m\n\033[31m[2] Type all informations again\033[m')
        while True:
            choice = validation('Did you want to save localy those informations?: ', convert_type=int, loadedfile=loadedfile, MaxLength=1)
            if choice in (1,2):
                break
        if choice == 1:
            session.append(LastTyped)
            print('-'*121)
            print()
            break


#show in red color all the things that are registered only in this session 
def print_session_saveds_red():
    global session
    for cont, item in enumerate(session, start=1):
        if item == []: 
            continue
        else:
            print(f'\033[31m{cont:<3}|{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
            
            
def print_file_data(loadedfile, msg):
    print()
    header(msg, character='-')
    if loadedfile == None or loadedfile == [] or loadedfile == '' or loadedfile == {}:
        print(f"\033[31mSorry, we can't reach the file, maybe it's because the file is empty\033[m")
        print('-'*121)
        print()
    else:
        print(explainingheader)
        for number, item in enumerate(loadedfile, start=1):
            print(f'\033[32m{number:<3}|{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
        

def op2_return(op):
    if op == 1:
        return 'Name', 28
    if op == 2:
        return 'Stock', 7
    if op == 3:
        return 'Original Price', 8
    if op == 4:
        return 'Discount Percentage', 5
