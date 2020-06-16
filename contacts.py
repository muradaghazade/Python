contacts = {'Fidan':584758475, 'Rafik':8957689576, 'Sabina':65876584554, 'Samir':4854545794, 'Nergiz':57846746746, 'Tariyel':23784738435, 'Albina':909454537543}

def contact_shower(cotact_name):
    print(f'{cotact_name}\'s phone number is {contacts[cotact_name]}')

def contact_creator(a):
    if a == 'yes':
        phone = int(input('Please enter the phone number: '))
        contacts[n] = phone
        contact_shower(n)
    else:
        print('New contact is not added.')

while True:
    name = input('Type whose phone number you want to see: ')
    n = name.capitalize()
    if n in contacts.keys():
        contact_shower(n)
    elif n == 'Exit':
        print('Exiting program')
        break
    else:
        question = input('Do you want to add this person\'s number? ')
        answer = question.lower()
        contact_creator(answer)

for k, v in contacts.items():
    print(k, v)