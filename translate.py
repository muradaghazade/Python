d = {'alma': 'apple', 'ev': 'house', 'it': 'dog', 'mashin': 'car', 'pishiy': 'cat', 'az': 'few', 'aq': 'white', 'qara': 'black', 'goy': 'blue', 'qirmizi': 'red', 'sari': 'yellow', 'yashil': 'green', 'narinci': 'orange', 'boz': 'gray', 'cehrayi': 'pink', 'benovsheyi': 'purple'}


lang_one = "az to eng"
lang_two = "eng to az"
ex = "exit"

while True:
    desicion = input(f'Type {lang_one} or {lang_two} or {ex}\t')
    if desicion == lang_two:
        d = {value:key for key, value in d.items()}
        print(f'You choose English to Azerbaijan')
        en_word = input(f'Enter the word:\t')
        if en_word in d:
            print(f'{en_word} : {d[en_word]}')
            d = {key:value for value, key in d.items()}
        else:
            print(f'Word not found.')
            d = {key:value for value, key in d.items()}
    elif desicion == lang_one:
        
        d = {value:key for key, value in d.items()}
        d = {key:value for value, key in d.items()}
        print(f'You choose Azerbaijan to English')
        az_word = input(f'Enter the word:\t')
        if az_word in d:
            print(f'{az_word} : {d[az_word]}')
        else:
            print(f'Word not found.')
    elif desicion == ex:
        print(f'You exited program.')
        break