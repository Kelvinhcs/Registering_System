session = [] #variable that will handle all the new registers
explainingheader = f'{"Product Name":^28}|{"Distributor":^25}|{"Original Price (US$)":^22}|{"Discount (US$)":^19}|{"Final Price (US$)":^19}' #created just to avoid typing ALL again

#display the header with the message that you want
def header(msg):
    print('='*117)
    print(f'{msg:^117}')
    print('='*117)


#everytime the ctrl+c or the exit option be selected this will me trigered    
#if ctrl+c be pressed again it imediatly ends without saving nothing
#otherwise will asks if you wanna save or not
#if the choice was to save, send all your sessions changes to a file
#if its not, your discard everything you do in the session
def wayout():
    print('\033[31mThe user decided to stop the program...\033[m')
    print("\033[32m[1] Send the informations saved localy to the Database\033[m\n\033[31m[2] Exit without saving\033[m")
    while True:
        try:
            choice = int(input("What's your choice?: "))
        except KeyboardInterrupt:
            print('\033[31mStopping the program right now...\033[m')
            exit()
        except:
            print('\033[31mERROR! Please type a valid option...\033[m')
        else:
            if choice in (1,2):
                break
    if choice == 1:
        print('\033[32mThis session was completely saved...\033[m')
        save_on_file()
        exit()
    elif choice == 2:
        print('\033[31mNothing in this session was saved...\033[m')
        exit()


#gonna save the inputs on the .json file
def save_on_file():
    pass


#validation process of inputs that triggers a function when ctrl+c or exit button is pressed
def validation(msg, convert_type=str):
    while True:
        try:
            choice = convert_type(input(msg))
        except KeyboardInterrupt:
            wayout()
        except:
            print('\033[31mERROR! Please type a valid option...\033[m')
        else:
            return choice


#bassicaly try to register a series of things on a dictionary and later to a list if its all right     
def new_products_register():
    global session
    while True:
        #first it will read all the informations and save on a dictionary
        name = validation('Product name: ').strip()
        price = validation('Product price: US$', convert_type=float)
        distributor = validation('What is the distributor?: ').strip()
        DiscountPercentage = validation('What percentage of discount will it have now?: ', convert_type=float)
        DiscountMoney = price*DiscountPercentage/100
        finalprice = price - DiscountMoney
        LastTyped = {'Name': name, 'Distributor':distributor, 'Original Price':price, 'Discount Money':DiscountMoney, 'Discount Percentage':DiscountPercentage, 'Final Price':finalprice}
        
        #here the program will show the last things you wrote
        print('='*117)
        print(explainingheader)        
        print(f'{name:^28}|{distributor:^25}|{price:^22.2f}| {DiscountPercentage:<5}% - {DiscountMoney:<9.2f}|{finalprice:^19.2f}')
        print('='*117)
        
        #if you agree it will save on a list, if you don't it will restart the process of typing
        print('\033[32m[1] Save Locally\033[m\n\033[31m[2] Type all informations again\033[m')
        while True:
            choice = validation('Did you want to save localy those informations?: ', convert_type=int)
            if choice in (1,2):
                break
        if choice == 1:
            session.append(LastTyped)
            break
        if choice == 2:
            continue


#return all the products that alredy have a register on the file
def show_past_registers(FileName):
    try:
        with open(FileName, 'r') as file:
            stuff_inside = file
    except KeyboardInterrupt:
        wayout()
    except FileNotFoundError or FileExistsError: 
        print('We cannot find the file to show you, sorry') 
    except Exception as error:
        print('I cant send you a list of your registers because of this')
        print(error)
    else:
        if stuff_inside == None or stuff_inside == [] or stuff_inside == '' or stuff_inside == {}:
            print('Nothing to show you unfortunatly')
        else:
            return stuff_inside
        
#show all the things that are saved on the session var (the list that we put all the things on register function)
def show_session_saveds():
    global session
    header(explainingheader)
    for counter,item in enumerate(session):
        if item == []: 
            continue
        else:
            print(f'{item["Name"]:^28}|{item["Distributor"]:^25}|{item["Original Price"]:^22.2f}| {item["Discount Percentage"]:<5}% - {item["Discount Money"]:<9.2f}|{item["Final Price"]:^19.2f}')
            
            
#show the products again, and alow you to change the stock quantity
def change_file_stock():
    show_past_registers()
    pass

