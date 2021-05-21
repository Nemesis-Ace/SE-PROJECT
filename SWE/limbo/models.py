from django.db import models
from django.core.exceptions import ValidationError



class Student(models.Model):
    sid=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=100,unique=False)
    semester=models.CharField(max_length=100,unique=False)

    def __str__(self):
        return self.sid


class Course(models.Model):
    cid = models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=False)
    credits=models.IntegerField(unique=False)
    iid=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.name


class Mark(models.Model):
    student_id=models.CharField(max_length=50,unique=False)
    instructor_id=models.CharField(max_length=50,unique=False,null=True)
    course_id = models.CharField(max_length=50)
    course_name=models.CharField(max_length=50,unique=False)
    score= models.IntegerField(null=True)

    def __str__(self):
        return self.student_id


class Addon(models.Model):
    cid = models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=False)
    credits=models.IntegerField(unique=False)
    iid=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    iid = models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    iid = models.CharField(max_length=50,unique=False)
    day=models.CharField(max_length=50,unique=False)
    time=models.CharField(max_length=50,unique=False)
    type=models.CharField(max_length=50,unique=False)


    def __str__(self):
        return self.iid

class DefaultList(models.Model):
    sid = models.CharField(max_length=50,unique=False)
    amount=models.IntegerField(unique=False)
    remarks=models.CharField(max_length=200,unique=False)
    department=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.sid

class DueList(models.Model):
    sid = models.CharField(max_length=50,unique=False)
    amount=models.IntegerField(unique=False)
    department=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.sid

class HostelAllot(models.Model):
    sid = models.CharField(max_length=50,unique=True)
    room=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.sid

class LoanList(models.Model):
    sid = models.CharField(max_length=50,unique=False)
    book_name=models.CharField(max_length=50,unique=False)
    isbn_no=models.CharField(max_length=50,unique=False)
    borrow_date=models.CharField(max_length=50,unique=False)
    due_date=models.CharField(max_length=50,unique=False)

    def __str__(self):
        return self.sid
