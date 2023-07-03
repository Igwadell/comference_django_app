from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Speaker(models.Model):
    Category=models.ForeignKey(Category, related_name='speakers', on_delete=models.CASCADE)
    name =models.CharField(max_length= 255)
    Bio = models.TextField(blank=True, null=False)
    contact_info = models.CharField(max_length= 50)
    Profile_picture = models.ImageField(upload_to='speaker_images',blank=True, null=True)
    area_of_experience= models.CharField(max_length= 255)


    def __str__(self):
        return f"{self.name} - {self.Category}"

