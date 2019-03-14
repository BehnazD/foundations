#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import csv
# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
user_input = form.getvalue('color').lower()
user_input = input("-")
user_input = user_input.lower()

color=[]


with open('scripts/colors.csv') as csv_file:
	reader = csv.reader(csv_file)
	my_list = list(reader)
	for list in my_list:
		color.append(f"{list[-3]},{list[-2]},{list[-1]}")

	print (color)
	#print ("rgb")
	"""for row in my_list:
			if user_input or rgb in my_list:	
	
				print(
				<html>
				<body>
				<p>
				Valid color
				</p>
				</body>
				</html>
				.format(user_input))
			else:
				print(
				<html>
				<body>
				<p>
				Not Valid color
				</p>
				</body>
				</html>
				 .format(user_input))"""
