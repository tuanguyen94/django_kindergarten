from __future__ import unicode_literals

from django.db import models


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)
# Create your models here.

class user(models.Model):
	username = models.CharField(max_length=120,blank=True, null=True)
	password = models.CharField(max_length=120,blank=True, null=True)
	email = models.EmailField()

	def __unicode__(self): #__str__
		return self.username


#grid layout 3x3
#	1		2		3
#	4		5		6
#	7		8		9
#the answeer is location of image
#just a number
class question(models.Model):
	"""docstring for question"""
	category_id = models.DecimalField()
	question_string = models.CharField()
	question_number = models.DecimalField()
	img1 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img2 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img3 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img4 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img5 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img6 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img7 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img8 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	img9 =  models.ImageField(upload_to=get_image_path, blank=True, null=True)
	answeer: models.DecimalField()

	def __unicode__(self): #__str__
		return self.question_string