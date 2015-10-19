from django_filters import *
from models import Contact

class ContactFilter(FilterSet):

	allC = Contact.objects.all()
	boards = set([c.board for c in allC])
	state = sorted(set([c.state for c in allC]))
	positionHeld = set([c.positionHeld for c in allC])
	
	BOARD_CHOICES = zip(boards, boards)
	BOARD_CHOICES.insert(0, ('', 'Board'))
	STATE_CHOICES = zip(state, state)
	STATE_CHOICES.insert(0, ('', 'State'))
	POSITION_CHOICES = zip(positionHeld, positionHeld)
	POSITION_CHOICES.insert(0, ('', 'Position'))

	board = ChoiceFilter(choices=BOARD_CHOICES, label = 'State')
	state = ChoiceFilter(choices=STATE_CHOICES, label = 'Board')
	positionHeld = ChoiceFilter(choices=POSITION_CHOICES, label='Position Held')
	firstName = CharFilter(lookup_type='startswith', label='First Name')
	lastName = CharFilter(lookup_type='startswith', label='Last Name')

	class Meta:
		model = Contact
		fields = ['firstName','lastName', 'state', 'board', 'positionHeld']