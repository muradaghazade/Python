contacts = {'Fidan':584758475, 'Rafik':8957689576, 'Sabina':65876584554, 'Samir':4854545794, 'Nergiz':57846746746, 'Tariyel':23784738435, 'Albina':909454537543}

def contact_shower(cotact_name):
    print(f'{cotact_name}\'s phone number is {contacts[cotact_name]}')

def new_contact_shower(cotact_name):
    print(f'{cotact_name} is added to contacts.')

def contact_creator(a):
    if a == 'Yes':
        phone = int(input('Enter the phone number: '))
        contacts[n] = phone
        new_contact_shower(n)
    else:
        print('New contact is not added.')

while True:
    name = input('Enter the name: ')
    n = name.capitalize()
    if n in contacts.keys():
        contact_shower(n)
    elif n == 'Exit':
        print('Exiting program')
        break
    else:
        question = input('Do you want to add this person to contacts? ')
        answer = question.capitalize()
        contact_creator(answer)

print(f'All your contacts:')
for k, v in contacts.items():
    print(f'{k}:{v}')