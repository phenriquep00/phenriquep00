from venv.ex115.modules import style, datatreat, color

while True:
    style.write_title('MAIN MENU')
    print(f'{color.yellow("1 ->")} {color.blue("Check registered people")}')
    print(f'{color.yellow("2 ->")} {color.blue("Insert new person")}')
    print(f'{color.yellow("3 ->")} {color.blue("Exit")}')
    style.line()
    ask = datatreat.read_int(color.cyan('OPTION:'))
    while 0 < ask > 3:
        print(color.red('Please Type a valid option (1/2/3)! '))
        ask = datatreat.read_int('OPTION: ')
    if ask == 1:
        style.write_title('REGISTERED PEOPLE: ')
        with open('data115') as file:
            for line in file:
                print(line)
    if ask == 2:
        while True:
            name = str(input('NAME: '))
            try:
                age = str(input('AGE: '))
            except ValueError:
                print(color.red('Please type a valid age'))
                continue
            with open('data115', 'a') as file:
                file.write(f'{name:<30} {age}\n')
            keep = str(input('Want to add another person? [y/n]')[0].lower().strip())
            if 'n' in keep:
                break
            else:
                name = ''
                continue
    if ask == 3:
        print(color.green('PROCESS FINISHED! ', bold=True))
        break
