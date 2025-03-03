import random

actions = ['P', 'F', 'C']

action_user = input('Que veux-tu jouer? (C ou F ou P : ')

action_machine = actions[random.randint(0,2)]
print(f'La machine a joué {action_machine}')



if action_user == action_machine:
	print('Egalité')
elif action_user == 'P' and action_machine == 'F':
	print('Machine gagne')

elif action_user == 'F' and action_machine == 'P':
        print('Tu gagnes')

elif action_user == 'P' and action_machine == 'C':
        print('Tu gagnes')

elif action_user == 'C' and action_machine == 'P':
        print('Machine gagne')


elif action_user == 'C' and action_machine == 'F':
        print('Tu gagnes')

elif action_user == 'F' and action_machine == 'C':
        print('Machine gagne')
