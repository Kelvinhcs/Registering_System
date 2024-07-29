import functions, json
from time import sleep
filename = 'data.json'
functions.header(' Welcome to our registering System ')
c = 0
while True:
    loadedfile = functions.pull_file(filename, counter=c)
    c += 1
    print("""[1] Register new products
[2] Show past registers
[3] Update past registers
[4] Save Session updates
[5] Exit the program""")
    while True:
        Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile, MaxLength=1)
        if Main_Choice in (1,2,3,4,5):
            break
        else:
            print('\033[31mUnsupported option. Please, try another one...\033[m')
        

    #Registering Area
    if Main_Choice == 1:
        print('-'*121)
        functions.new_products_register(loadedfile)
        

    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        print()
        functions.header('Stock Management', character='-')
        Second_Choice = functions.pull_file(filename, error=False)
        if Second_Choice == None or Second_Choice == [] or Second_Choice == '' or Second_Choice == {}:
            print(f"\033[31mSorry, we can't reach the file, maybe it's because the file is empty\033[m")
            print('-'*121)
        else:
            print(functions.explainingheader)
            for number, item in enumerate(Second_Choice):
                print(f'\033[32m{number:<3}|{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
            functions.print_session_saveds_red()
            print('-'*121)
            sleep(2)
        print()


    #Changing any previous information           
    elif Main_Choice == 3:
        #Showing all the items in the file to let the user choose
        print()
        functions.header('Changing Section', character='-')
        Showing_Past = functions.pull_file(filename, error=False)
        if Showing_Past == None or Showing_Past == [] or Showing_Past == '' or Showing_Past == {}:
            print(f"\033[31mSorry, we can't reach the file, maybe it's because the file is empty\033[m")
            print('-'*121)
        else:
            print(functions.explainingheader)
            for number, item in enumerate(Showing_Past):
                print(f'\033[31m{number+1:<3}\033[m|{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}')
            print('-'*121)
            print()
        
        
            #taking the informations
            while True:
                #What dict we will need to change
                while True:
                    dict_position = functions.validation("Which item did you wan't to change?: ", loadedfile, MaxLength=3, convert_type=int) - 1
                    if dict_position > len(Showing_Past) or dict_position < 0:
                        print("\033[31mThis option, doesn't existe, please try again...\033[m")
                    else:
                        break
                print()
                
                
                #What item we will need to change
                while True:
                    print(f"\033[32m[1] Name\n[2] Stock quantity\n[3] Original Price\n[4] Discount percentage\033[m")
                    op2 = functions.validation("Which item did you wan't to change?: ", loadedfile, MaxLength=3, convert_type=int)
                    if op2 < 1 or op2 > 4:
                        print("\033[31mInvalid option, please try again...\033[m")
                    else:
                        break
                dict_item = functions.op2_return(op2)
                
                
                
                if dict_item[0] == 'Name':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=str)
                elif dict_item[0] == 'Discount Percentage':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=float)
                else:
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=int)
                    
                placeholder = loadedfile[dict_position]
                placeholder[dict_item[0]] = new_value
                DiscountMoney_placeholder = (placeholder['Original Price']*placeholder['Discount Percentage'])/100
                FinalPrice_placeholder = placeholder['Original Price'] - DiscountMoney_placeholder 
                placeholder['Discount Money'] = DiscountMoney_placeholder
                placeholder['Final Price'] = FinalPrice_placeholder
                
                
                #Showing how the change look and asking if the user wants it or no     
                print('-'*121)
                print(functions.explainingheader)
                print(f'\033[31m{"1  "}\033[m|{placeholder["Name"]:^28}|{placeholder["Stock"]:^24}|{placeholder["Original Price"]:^22.2f}|{placeholder["Discount Percentage"]:>6}% - {placeholder["Discount Money"]:<10.2f}|{placeholder["Final Price"]:^19.2f}')
                print('-'*121)
                print()
                print('\033[32m[1] Update the file \033[m\n\033[31m[2] Type all informations again\033[m')
                print()
                while True:
                    pl = functions.validation('What is your choice?: ', loadedfile, MaxLength=1, convert_type=int)
                    if pl < 1 or pl > 2:
                        print("\033[31mInvalid option, please try again...\033[m")
                    else:
                        break
                if pl == 1:
                    functions.header('\033[31mPLEASE BE CAREFUL\033[m')
                    while True:
                        pl2 = functions.validation('\033[31mThis action will save it directly to the file, Are you sure[y/s]?:\033[m ',loadedfile, MaxLength=1, convert_type=str)
                        if pl2 in ('y', 's'):
                            break
                        else:
                            print("\033[31mInvalid option, please try again...\033[m")
                    if pl2 == 'y':
                        del loadedfile[dict_position]
                        loadedfile.insert(dict_position, placeholder)
                        try:
                            with open(filename, 'w') as file:
                                json.dump(loadedfile, file, indent=2)
                        except Exception as error:
                            print('\033[31mNothing in this session was saved...\033[m')
                            print(error)
                        else:
                            placeholder.clear()
                            print('\033[32mThis session was completely saved...\033[m')
                            break
                    if pl2 == 'n':
                        print('Restarting...')
                        continue
                
                if pl == 2:
                    print('Restarting...')
        

        
    #A way to save the session data on the file without needing to exit the program    
    elif Main_Choice == 4:
        if functions.session == []:
            print()
            functions.header("We don't have any data on current sesion to be saved.", character='*')
            print()
            sleep(2)
        else:
            print()
            functions.header(f'{"Session data":^121}', character='-')
            print(functions.explainingheader)
            functions.print_session_saveds_red()
            print('-'*121)
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
        print('='*121)
        functions.wayout(loadedfile)

    functions.header("Products Register")


#THINK LATER: Do we really need to save that many informations on the file?