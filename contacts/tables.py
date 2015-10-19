import django_tables2 as tables
from models import Contact
from django_tables2.utils import A  # alias for Accessor

class ContactTable(tables.Table):
	class Meta:
		model = Contact
		fields = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'city',
					'state', 'zipCode', 'email1')
		attrs = {"class" : "paleblue"}