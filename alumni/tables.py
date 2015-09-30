import django_tables2 as tables
from models import User
from django_tables2.utils import A  # alias for Accessor

class UserTable(tables.Table):
	class Meta:
		model = User
		fields = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'city',
					'state', 'zipCode', 'email1')
		attrs = {"class" : "paleblue"}