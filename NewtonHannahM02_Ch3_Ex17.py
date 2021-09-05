Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(' Hello, please reboot your computer and try to connect.')
 Hello, please reboot your computer and try to connect.
>>> answer = input('Did that fix the problem? ')
Did that fix the problem? no
>>> if answer != 'yes':
	print('Reboot your router and try to connect.')
	answer = input('Did that fix the problem? ')
	if answer != 'yes':
		print('Make sure the cables between the router and modem are plugged in firmly.')
		answer = input('Did that fix the problem? ')
		if answer != 'yes':
			print('Move the router to a new location and try to connect.')
			answer = input('Did that fix the problem? ')
			if answer != 'yes':
				print('Get a New router.')

				
Reboot your router and try to connect.
Did that fix the problem? no
Make sure the cables between the router and modem are plugged in firmly.
Did that fix the problem? no
Move the router to a new location and try to connect.
Did that fix the problem? yes
>>> 