from django.db import models
# Create your models here.

# one to one :
# class female (models.Model):
#     Name = models.CharField(max_length=55,null=True)
#     def __str__(self):
#             return self.Name

# class male (models.Model):
#     Name = models.CharField(max_length=55,null=True)
#     girls = models.OneToOneField(female, on_delete=models.CASCADE)
#     def __str__(self):
#             return self.Name

# # one to many :
# class product (models.Model):
#     Name = models.CharField(max_length=55,null=True)

#     def __str__(self):
#             return self.Name

# class user (models.Model):
#     title = models.CharField(max_length=55,null=True)
#     products = models.ForeignKey(product, on_delete=models.CASCADE)

#     def __str__(self):
#             return self.title
    
        
# # many to many
    
# class video (models.Model):
#     title = models.CharField(max_length=55,null=True)

#     def __str__(self):
#             return self.title

# class username (models.Model):
#     title = models.CharField(max_length=55,null=True)
#     watch = models.ManyToManyField(video,null=True)

#     def __str__(self):
#                 return self.title
    
class login(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=55)