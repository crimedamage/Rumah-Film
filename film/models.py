from django.db import models

# Create your models here.
LINK_CHOICES ={
	('DL','DOWNLOAD LINK'),
}
class Film(models.Model):
	idfilm  = models.IntegerField(default=0)
	namafilm = models.CharField(max_length=100,default="")
	genrefilm = models.CharField(max_length=100,default="")
	# tahunfilm = models.DateField(max_length=100,default="YYYY-MM-DD")
	# image = models.ImageField(upload_to='Films')
	# category = MultiSelectField(choices=CATEGORY_CHOICES)
	# negara = models.CharField(choices=NEGARA_CHOICES, max_length=10,default="other")
	# # category = models.ManyToManyField(CATEGORY_CHOICES)
	# status =MultiSelectField(choices=STATUS_CHOICES)
	# views_count = models.IntegerField(default=0)
	# year_or_product = models.DateField()
	# rating_count = models.IntegerField(default=0)
	# views_count = models.IntegerField(default=0)
	# linkReview = models.URLField(blank=True,default='#')
	# created = models.DateTimeField(default=timezone.now)
	# slug = models.SlugField(blank=True,null=True)
	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		self.slug = slugify(self.namafilm)
	# 	super(Film, self).save(*args, **kwargs)

	def __str__(self):

		return '{}'.format(self.namafilm) 



class Links_Film(models.Model):
	Film = models.ForeignKey(Film,related_name='film_link',on_delete=models.CASCADE)
	# type = models.CharField(choices=LINK_CHOICES, max_length=2)
	link_144 = models.TextField(blank=True,default='#')
	link_240 = models.TextField(blank=True,default='#')
	link_360 = models.TextField(blank=True,default='#')
	link_480 = models.TextField(blank=True,default='#')
	link_720 = models.TextField(blank=True,default='#')
	link_1080 = models.TextField(blank=True,default='#')
	verified = models.BooleanField(default=False)
	def __str__(self):
		return '{}'.format(self.Film)

class Xerror_Film(models.Model):
	tidakdiketahui = models.TextField(blank=True,default='#')
