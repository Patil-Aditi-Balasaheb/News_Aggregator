from django.db import models

###############################
#           UtMost            #
###############################
# Scrape data coming from websites
# The posts will contain images, urls and titles
# model - headline(title, image, url)


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title


class Users(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    contact = models.IntegerField(max_length=15)
    alternate_contact = models.IntegerField(max_length=15)
    topnews = models.BooleanField()
    business = models.BooleanField()
    technology = models.BooleanField()
    entertainment = models.BooleanField()
    sports = models.BooleanField()
    science = models.BooleanField()
    health = models.BooleanField()

    def __str__(self):
        return self.firstname+ " " +self.lastname