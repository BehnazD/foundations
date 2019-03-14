#!/usr/local/bin/python3
import cgi
import csv

form = cgi.FieldStorage()
user_input = form.getvalue('color').lower()
my_list=[]
bla_bla =False


with open('scripts/colors.csv', 'r') as csv_file:
	reader = csv.reader(csv_file)

	for row in reader:
		my_list.append(row)

for row in my_list:
	rgb ='_'.join(row[-3:])
	del row[-3:]
	row.append(rgb)

if ' ' in user_input:
	user_input = user_input.replace(' ', '_')

for list in my_list:
	if user_input in list:
		bla_bla =True
if bla_bla == True:

	print("""
    	<html>
    	<body>
    	<p>
    	This is a valid color, %s
    	<p>
    	</body>
    	</html>
    	""" % user_input)
	    
else:
	print("""
	 	<html>
     	<body>
     	<p>
     	This is not a valid color, %s
     	<p>
     	</body>
     	</html>
     	""" % user_input)
	    
	   