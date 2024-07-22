#base function to save the modifications or not based on personal user choice
#and ending imediatly dont savig if ctrl+c is press
def wayout():
    print('\033[31mThe user decided to stop the program...\033[m')
    print("[1] Save and Exit\n[2] Exit without saving")
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
        save()
        exit()
    elif choice == 2:
        print('\033[31mNothing in this session was saved...\033[m')
        exit()
    
    
#gonna save the inputs on the .json file
def save():
    pass


#validation process of inputs that triggers a function when ctrl+c is pressed
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
 
 
#thats the most self-explain name that i wrote in my whole life        
def new_products_register():
    pass


#show all the products that alredy have a register
def show_past_registers():
    pass


#show the products again, and alow you to change the stock quantity
def change_stock():
    show_past_registers()
    pass

