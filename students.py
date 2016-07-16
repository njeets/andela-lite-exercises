from datetime import date

students ={
	'name':['Njeri', 'Mbugua'],
	'date_of_birth':1992,
	'phone':'073433433',
}
print('the first name is {0} and the second name is {1}'.format(students.get('name')[0], students.get('name')[1]))
print(students['name'][0])
print(students['phone'])
print(students['date_of_birth'])
age = date.today().year - students['date_of_birth']
print(age)