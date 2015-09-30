from django_filters import *
from models import *

class UserFilter(FilterSet):

	boards = set([u.board for u in User.objects.all()])
	state = sorted(set([u.state for u in User.objects.all()]))
	positionHeld = set([u.positionHeld for u in User.objects.all()])
	
	BOARD_CHOICES = zip(boards, boards)
	BOARD_CHOICES.insert(0, ('', 'All'))
	STATE_CHOICES = zip(state, state)
	STATE_CHOICES.insert(0, ('', 'All'))
	POSITION_CHOICES = zip(positionHeld, positionHeld)
	POSITION_CHOICES.insert(0, ('', 'All'))

	board = ChoiceFilter(choices=BOARD_CHOICES)
	state = ChoiceFilter(choices=STATE_CHOICES)
	positionHeld = ChoiceFilter(choices=POSITION_CHOICES)

	class Meta:
		model = User
		fields = ['firstName','lastName', 'state', 'board', 'positionHeld']
		together = ['firstName', 'lastName']