from django.core.management.base import BaseCommand, CommandError
from contacts.models import Contact
import csv
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def defaultUser(model):
	username = model.firstName.lower() + model.lastName.lower()
	try:
		u = User.objects.create_user(username, password="12345", email=model.email1,
		first_name = model.firstName, last_name = model.lastName)
		u.save()
	except:
		u = None
		pass
	return u

class Command(BaseCommand):
	help = 'Adds alumni from a csv file of alumni'

	def add_arguments(self, parser):
		parser.add_argument('file', nargs='+', type=str)

	def handle(self, *args, **options):
		if len(args) != 1:
			print "Usage: ./manage.py adduser <filename>"
			return

		fname = args[0]
		try:
			f = open(fname, 'rU')
   		except:
   			raise CommandError('File "%s" cannot be opened.' % fname)

   		reader = csv.reader(f)
		header = next(reader)
		for row in reader:
			info = dict(zip(header, row))
			try:
				contact, created = Contact.objects.get_or_create(**info)
			except:
				#self.stdout.write("Could not load " + row[0] + " " + row[1] + ".\n")
				pass
			if created:
				contact.alum = True
				contact.user = defaultUser(contact)
				contact.save()
   		self.stdout.write('Finished adding users.')

        
