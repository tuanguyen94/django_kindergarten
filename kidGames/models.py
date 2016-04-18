from __future__ import unicode_literals
import os
from django.db import models

MEDIA_URL = 'static/media/'


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

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
	category_id = models.SmallIntegerField(blank=False)
	question_string = models.CharField(max_length=120,blank=False, null=True)
	question_number = models.SmallIntegerField(blank=False)
	background = img1 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img1 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img2 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img3 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img4 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img5 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img6 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img7 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img8 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	img9 = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_URL, 'upload', 'here')), blank=True, null=True)
	answeer = models.SmallIntegerField(blank=False)

	def __unicode__(self): #__str__
		return self.question_string