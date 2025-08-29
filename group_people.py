#Group of People

print('------Group of People Data------')

people = []
sum_age = average_age = 0
women = []

while True:
	person = {}
	person['name'] = str(input('Name:\n'))
	person['gender'] = str(input('Gender:\n')).strip().lower()[0]
	person['age'] = int(input('Age:\n'))
	
	people.append(person.copy())
	
	user_continue = str(input('Continue? [y/n]')).strip().lower()[0]
	if user_continue == 'n':
		print('See you soon!\n')
		break
		
print('-=' * 30)
		
amount_people = len(people)

for p in people:
	sum_age += p['age']
	if p['gender'] == 'f':
		women.append(p['name'])
	
average_age = sum_age / amount_people
print(f'{amount_people} People registered')
print(f'The average age of the Group is {average_age:.2f}')
print(f'Woman in this group: {women}')

print('The following person(s) have age above average!')
for p in people:
	if p['age'] > average_age:
		print(' ', end = ' ')
		for k, v in p.items():
			print(f'{k}: {v};', end = ' ')
		print()
print('Finished')
