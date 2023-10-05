from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Features(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/team/')
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Test(models.Model):
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='images/test/')

    def __str__(self):
        return self.full_name


class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.full_name