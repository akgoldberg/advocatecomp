from django.db import models

# Create your models here.
class User(models.Model):
	def full_name(self):
		return self.article + " " + self.firstName + " " + self.lastName + " " + self.title

	def __unicode__(self):
		return self.full_name()

	def full_address(self):
		return self.streetAddress1 + '\n' + self.streetAddress2 + '\n' + self.streetAddress3

	class Meta:
		ordering = ('firstName', 'lastName') # default sort order
		unique_together = ['firstName', 'lastName'] # no two contacts can have the same first/last name

	firstName = models.CharField(max_length=255, verbose_name='First name') 
	middleName = models.CharField(max_length=255, blank=True, verbose_name='Middle name')
	lastName = models.CharField(max_length=255, blank=True, verbose_name='Last name')
	photo = models.ImageField(null = True, blank = True, upload_to = './profiles', verbose_name = 'Profile Picture')
	article = models.CharField(max_length=255, blank=True, verbose_name='Article')
	title = models.CharField(max_length=255, blank=True, verbose_name='Title')
	nickName = models.CharField(max_length=255, blank=True, verbose_name='Nickname')
	streetAddress1 = models.CharField(max_length=255, blank=True, verbose_name='Address 1')
	streetAddress2 = models.CharField(max_length=255, blank=True, verbose_name='Address 2')
	streetAddress3 = models.CharField(max_length=255, blank=True, verbose_name='Address 3')
	city = models.CharField(max_length=255, blank=True, verbose_name='City')
	state = models.CharField(max_length=255, blank=True, verbose_name='State')
	zipCode = models.CharField(max_length=255, blank=True, verbose_name='Zip code')
	country = models.CharField(max_length=255, blank=True, verbose_name='Country')
	email1 = models.CharField(max_length=255, blank=True, verbose_name='Email')
	email2 = models.CharField(max_length=255, blank=True, verbose_name='Email 2')
	phone = models.CharField(max_length=255, blank=True, verbose_name='Phone')
	linkedIn = models.CharField(max_length=255, blank=True, verbose_name='LinkedIn')
	twitter = models.CharField(max_length=255, blank=True, verbose_name='Twitter')
	facebook = models.CharField(max_length=255, blank=True, verbose_name='Facebook')
	followed = models.BooleanField(default=False, verbose_name='Followed?')
	website = models.CharField(max_length=255, blank=True, verbose_name='Website')
	profession = models.CharField(max_length=255, blank=True, verbose_name='Profession')
	graduationYear = models.CharField(max_length=255, blank=True, verbose_name='Graduation year')
	otherDegrees = models.CharField(max_length=255, blank=True, verbose_name='Other degrees')
	board = models.CharField(max_length=255, blank=True, verbose_name='Board')
	positionHeld = models.CharField(max_length=255, blank=True, verbose_name='Position held')
	publishedWork = models.TextField(blank=True, verbose_name='Published work')
	notes = models.TextField(blank=True, verbose_name='Notes')	
	formCategory = models.CharField(max_length=255, blank=True, verbose_name='Form category')
	dateAdded = models.DateField(auto_now_add=True, blank=True, verbose_name='Date added')


class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name='Title') 
	text = models.TextField(blank = True, verbose_name='Text') 
	pub_date = models.DateTimeField(null = True)
	user = models.ForeignKey(User)
	img = models.ImageField(null = True, blank = True, upload_to = '.', verbose_name = 'Image')
	file_upload = models.FileField(null = True, blank = True, upload_to = '.')