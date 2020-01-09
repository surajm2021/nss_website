from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

class Gender(models.Model):
	gender = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.gender}"

class Status(models.Model):
	status = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.status}"

class Branch(models.Model):
	branch = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.branch}"

class Batch(models.Model):
	batch = models.CharField(max_length=100)
	def __str__(self):
		return f"{self.batch}"

class Nss_team_member(models.Model):
	name = models.CharField(max_length=100,help_text='Name of nss team memner')
	batch = models.ForeignKey(Batch,null=True,on_delete=models.CASCADE)
	achievement = models.CharField(max_length=100)
	branch = models.ForeignKey(Branch,null=True,on_delete=models.CASCADE)
	sex = models.ForeignKey(Gender,null=True,on_delete=models.CASCADE)
	status = models.ForeignKey(Status,null=True,on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='nss_team_member_pics')
	added_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.name} member"
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img=Image.open(self.image.path)	
		if img.height >100 or img.width >100:
			output_size = (250,250)
			img.thumbnail(output_size)
			img.save(self.image.path)						
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})
	
	

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    added_by =  models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
    	return f"{self.description}"
    def get_absolute_url(self):
    	return reverse('special-camp')
