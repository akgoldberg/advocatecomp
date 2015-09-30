from django.core.management.base import BaseCommand, CommandError
from alumni.models import User
import csv

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
			u = User(**info)
			u.save()
   		self.stdout.write('Successfully added users.')

        
