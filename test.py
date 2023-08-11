grades = ['A', 'B', 'C']
addresses = {'philip': 'Maxwell Road'}

def print_name():
    name = input('What is your name: ')
    print(f'Welcome Mr/Miss {name}')
    address = addresses[name]
    print(f'Address: {address}')

print_name()
