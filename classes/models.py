from django.db import models






class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField(max_length=30)
    tags= models.ManyToManyField(Tag , related_name="course")


class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="lecture")
    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    Lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE , primary_key=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    Lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE , primary_key=True)
    def __str__(self):
        return self.name


