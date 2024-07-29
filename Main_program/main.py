import functions, json
from time import sleep
filename = 'data.json'
c = 0
while True:
    loadedfile = functions.pull_file(filename, counter=c)
    c += 1
    #Asksing for what to do
    functions.header("Products registering system")
    print("""[1] Register new products
[2] Show past registers
[3] Update past registers
[4] Save Session updates
[5] Exit the program""")
    Main_Choice = functions.validation(msg="What's is your choice?: ", convert_type=int, loadedfile=loadedfile, MaxLength=1, options=True, start=1, stop=5)


    #Registering Area
    if Main_Choice == 1:
        print(functions.Straight_Line)
        functions.new_products_register(loadedfile)
        

    #Showing all the past registers on green and the locals on red   
    elif Main_Choice == 2:
        legend = functions.print_file_data(loadedfile, 'Stock Management')
        functions.print_session_saveds_red()
        print(functions.Straight_Line)
        if legend != 1:
            print('\033[32mGreen represents the saved data\033[m')
            print('\033[31mRed represents the sessions data\033[m')
        print()
        sleep(2)

    #Changing any previous information           
    elif Main_Choice == 3:
        #if theres nothing on the file stops, but if it finds something ask the user what they want to do
        if loadedfile == None or loadedfile == [] or loadedfile == '' or loadedfile == {}:
            functions.padronized_file_error("Sorry, we cannot find anything on the file to update")
        else:
            functions.updating(loadedfile, filename)


    #A way to save the session data on the file without needing to exit the program    
    elif Main_Choice == 4:
        if functions.session == []:
            functions.padronized_file_error("We don't have any data on current sesion to be saved")
        else:
            print()
            functions.header(f'{"Session data":^121}', character='-')
            print(functions.explainingheader)
            functions.print_session_saveds_red()
            print(functions.Straight_Line)
            print()
            print("\033[32m[1] Send the informations saved localy to the File\033[m\n\033[31m[2] Send all later\033[m")
            choice = functions.validation("What is your choice?: ", loadedfile=loadedfile, MaxLength=1, convert_type=int, options=True, start=1, stop=2)
            if choice == 1:
                functions.push_file(loadedfile=loadedfile, filename=filename)
        
        
    #DONE  
    elif Main_Choice == 5:
        print(functions.Straight_Line)
        functions.wayout(loadedfile)

#THINK LATER: Do we really need to save that many informations on the file?
#THINK LATER: if nothing was changed we dont need to write it all again on the file. functions.py LINE 112