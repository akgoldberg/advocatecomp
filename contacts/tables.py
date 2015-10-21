import django_tables2 as tables
from models import Contact
from django_tables2.utils import A  # alias for Accessor

class ContactTable(tables.Table):
	firstName = tables.LinkColumn('contacts.views.profile', args = [tables.A("pk"),])
	class Meta:
		model = Contact
		fields = ('firstName', 'lastName', 'graduationYear',
					 'board', 'positionHeld', 'city', 'state')
		attrs = {"class" : "paleblue"}