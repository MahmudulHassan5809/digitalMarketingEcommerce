from django.db import models

# Create your models here.
class Category(models.Model):
	category_name  = models.CharField(max_length=200)
	category_image = models.ImageField(upload_to="category/%Y/%m/%d/")
	parent   = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,null=True,blank=True)
	
	


	def __str__(self):
		full_path = [self.category_name]
		k = self.parent
		while k is not None:
			full_path.append(k.category_name)
			k = k.parent
		return ' -> '.join(full_path[::-1])


