from django.db import models

# Create your models here.

class Student(models.Model):
    studentID = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=13)
    photograph = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    RESIDENCY_CHOICES = [
        ('ON', 'On Campus'),
        ('OFF', 'Off Campus'),
    ]
    residency = models.CharField(max_length=3, choices=RESIDENCY_CHOICES)
    STATUS_CHOICES = [
        ('REG', 'Regular'),
        ('FEE', 'Fee Paying'),
        ('DST', 'Distance'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def __str__(self):
        return '{} (STUDENT ID:{})'.format(self.name.title(), self.studentID)
    

    
class Course(models.Model):
    course_code = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name='enrolled_courses')
    opened = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    cancelled = models.BooleanField(default=False)
    cancellation_reason = models.TextField()


