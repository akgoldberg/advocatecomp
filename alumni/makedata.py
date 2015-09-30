import names
import csv
import random
from faker import Factory

faker = Factory.create()
num = 1000
outfile = 'alumnitestdata.csv'
f = open(outfile, 'w')
writer = csv.writer(f, delimiter = ',')
# make the header
writer.writerow(['firstName', 'lastName', 'graduationYear', 'otherDegrees',
	'profession', 'board', 'positionHeld', 'streetAddress1', 'city', 'state',
	'zipCode', 'email1'])
for i in range(0,num):
	fn = names.get_first_name()
	ln = names.get_last_name()
	gy = random.randint(1940, 2019)
	od = random.choice([None, None, None, None, 'JD', 'PhD', 'MD'])
	pf = random.choice(['writer', 'publisher', 'doctor', 'lawyer', 'poet', 'chef', 'professor', 'teacher'])
	bd = random.choice(['Art', 'Business', 'Design', 'Features', 'Fiction', 'Poetry', 'Technology'])
	ph = random.choice(['President', 'Publisher', 'Art Editor', 'Blog Editor', 'Business Manager',
	 'Design Editor', 'Features Editor', 'Fiction Editor', 'Poetry Editor', 'Technology Editor',
	  'Hermes, Librarian', 'Alumni Relations Manager', 'Communicorn', 'Hestia'])
	add = " ".join(faker.address().split(' ')[:3])
	ct = faker.city()
	st = faker.state() 
	em = faker.email()
	zc = random.randint(10000, 99999)
	writer.writerow([fn, ln, gy, od, pf, bd, ph, add, ct, st, zc, em])