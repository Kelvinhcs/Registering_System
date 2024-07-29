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
    
    Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile, MaxLength=1, options=True, start=1, stop=5)


    #Registering Area
    if Main_Choice == 1:
        print('-'*121)
        functions.new_products_register(loadedfile)
        

    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        functions.print_file_data(loadedfile, 'Stock Management')
        functions.print_session_saveds_red()
        print('-'*121)
        print('\033[32mGreen represents the saved data\033[m')
        print('\033[31mRed represents the sessions data\033[m')
        print()
        sleep(2)

    #Changing any previous information           
    elif Main_Choice == 3:
        #if theres nothing on the file stops, but if it finds something ask the user what they want to do
        if loadedfile == None or loadedfile == [] or loadedfile == '' or loadedfile == {}:
            continue
        else:
            #taking the informations
            while True:
                loadedfile = functions.pull_file(filename, counter=c)
                functions.print_file_data(loadedfile, 'Changing Section')
                print('-'*121)
                print()
                #What dict we will need to change
                dict_position = functions.validation("Which item did you wan't to change?: ", loadedfile, MaxLength=3, convert_type=int, options=True, start=1, stop=len(loadedfile)) - 1
                print()
                
                
                #What item we will need to change
                print(f"\033[32m[1] Name\n[2] Stock quantity\n[3] Original Price\n[4] Discount percentage\033[m")
                op2 = functions.validation("Which item did you wan't to change?: ", loadedfile, MaxLength=3, convert_type=int, options=True, start=1, stop=4)
                dict_item = functions.op2_return(op2)
                
                
                #Making the changes
                if dict_item[0] == 'Name':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=str)
                elif dict_item[0] == 'Discount Percentage':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=float, percentage=True)
                elif dict_item[0] == 'Original Price':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=float)
                elif dict_item[0] == 'Stock':
                    new_value = functions.validation('New value: ', loadedfile, MaxLength=dict_item[1], convert_type=int)
                    
                placeholder = loadedfile[dict_position]
                placeholder[dict_item[0]] = new_value
                DiscountMoney_placeholder = (placeholder['Original Price']*placeholder['Discount Percentage'])/100
                FinalPrice_placeholder = placeholder['Original Price'] - DiscountMoney_placeholder 
                placeholder['Discount Money'] = DiscountMoney_placeholder
                placeholder['Final Price'] = FinalPrice_placeholder
                
                
                #Showing how the change look and asking if the user wants it or no     
                print()
                functions.header('Showing the changes', character='-')
                print(functions.explainingheader)
                print(f'\033[32m{'1  '}|{placeholder["Name"]:^28}|{placeholder["Stock"]:^24}|{placeholder["Original Price"]:^22.2f}|{placeholder["Discount Percentage"]:>6}% - {placeholder["Discount Money"]:<10.2f}|{placeholder["Final Price"]:^19.2f}\033[m')
                print('-'*121)
                print()
                print('\033[32m[1] Update the file \033[m\n\033[31m[2] Type all informations again\033[m')
                pl = functions.validation('What is your choice?: ', loadedfile, MaxLength=1, convert_type=int, options=True, start=1, stop=2)
                if pl == 2:
                    print('Restarting...')
                    continue
                if pl == 1:
                    functions.header('\033[31mPLEASE BE CAREFUL\033[m')
                    print('\033[31m[1] YES\n[2] NO\033[m')
                    pl2 = functions.validation('\033[31mThis action will save it directly to the file, Are you sure?:\033[m ',loadedfile, MaxLength=1, convert_type=int, options=True, start=1, stop=2)
                    if pl2 == 1:
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
                    if pl2 == 2:
                        print('Restarting...')
                        continue


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
            choice = functions.validation("What is your choice?: ", loadedfile=loadedfile, MaxLength=1, convert_type=int, options=True, start=1, stop=2)
            if choice == 1:
                functions.save_on_file(loadedfile=loadedfile, filename=filename)
        
        
    #DONE  
    elif Main_Choice == 5:
        print('='*121)
        functions.wayout(loadedfile)

    functions.header("Products Register")

#FIX THE ERROR: Na opção de update, mesmo colocando que quero digitar as informações novamente ele salva na loadedfile a mudança
#parcialmente resolvi fazendo o arquivo dar pull a cada loop, mas suspeito que eu tenha feito uma ligação da loadedfile com placeholder
#THINK LATER: Do we really need to save that many informations on the file?