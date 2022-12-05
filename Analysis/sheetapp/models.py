from django.db import models

# Create your models here.

class Order(models.Model):
	order_no=models.CharField(max_length=100)



class Process(models.Model):
	order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.CASCADE)
	process_name=models.CharField(null=True,blank=True,max_length=100)


class Productdetail(models.Model):
	process=models.ForeignKey(Process,null=True,blank=True,on_delete=models.CASCADE)
	name=models.CharField(null=True,blank=True,max_length=100)
	starttime=models.CharField(null=True,blank=True,max_length=100)
	endtime=models.CharField(null=True,blank=True,max_length=100)
	cycletime=models.CharField(null=True,blank=True,max_length=100)
	width=models.IntegerField(null=True,blank=True)
	thickness=models.DecimalField(null=True,blank=True)
	weight=models.DecimalField(null=True,blank=True)
