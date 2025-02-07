def requesting_file():
    folder: str = str(input("Type folder path: "))
    while True:
        formatted_outcome = []
        formatted_outcome.append(input('Type format outcome: '))
        answer = str(input('Would you like to continue? [Y/N]: '))
        if answer in 'Nn':
                break
        else:
            while True:
                if answer not in 'Yy' and answer not in 'Nn':
                    print('Answer needs to be ["Y" or "N"] format')
                    answer = str(input('Would you like to continue? [Y/N]: '))
                while answer in 'Yy':
                    formatted_outcome.append(input('Type format outcome: '))
                    answer = str(input('Would you like to continue? [Y/N]: '))
                if answer in 'Nn':
                    break
            break
    return folder, formatted_outcome
