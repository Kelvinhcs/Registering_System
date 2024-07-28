import functions
filename = 'data.json'
loadedfile = functions.pull_file(filename='data.json')
obijeto = {'Name':'tESTANDO', 'Stock':69, 'Original Price':69.69, 'Discount Money': 0.0, 'Discount Percentage': 0.0, 'Final Price':0.0 }
while True:
    functions.header('Stock Management', character='-')
    print(functions.explainingheader)
    for number, item in enumerate(loadedfile):
        print(f'\033[32m{number:<3}|{item["Name"]:^28}|{item["Stock"]:^24}|{item["Original Price"]:^22.2f}|{item["Discount Percentage"]:>6}% - {item["Discount Money"]:<10.2f}|{item["Final Price"]:^19.2f}\033[m')
    print('-'*121)
    print()
    testing = functions.validation('Typing: ', convert_type=int,  loadedfile=loadedfile, MaxLength=3)
    del loadedfile[testing]
    loadedfile.insert(testing, obijeto)