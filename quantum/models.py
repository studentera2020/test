from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    Year_int=models.IntegerField(default=0)
    Year_char=models.CharField(max_length=10)
    subject=models.CharField(max_length=100)
    sub_chapter=models.CharField(max_length=50)
    pub_date=models.DateField()
    pdf=models.FileField(upload_to="pdfs")
    def __str__(self):
        return self.subject