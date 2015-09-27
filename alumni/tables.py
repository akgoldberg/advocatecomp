import django_tables2 as tables
from models import User

class UserTable(tables.Table):
	class Meta:
		model = User
		fields = ('firstName', 'lastName', 'graduationYear',
					'otherDegrees', 'profession', 'board',
					'positionHeld', 'full_address', 'city',
					'state', 'zipCode', 'email1')
		# add class="pale blue" to <table> tag
		attrs = {"class" : "paleblue"}