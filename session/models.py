from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from jobpost.models import District
# from tuition.models import District,Subject,Class_in
from multiselectfield import MultiSelectField

# Create your models here.

class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    CATEGORY=(
        ('Student', 'Student'),
        ('Fresher', 'Fresher'),
        ('Experience', 'Experience'),
        ('Experience Plus', 'Experience Plus'),
    )
    BLOOD_GROUP=(
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField()
    blood_group=models.CharField(max_length=3, choices=BLOOD_GROUP)
    gender = models.CharField(max_length=50, choices=GENRE_CHOICES)
    address = models.CharField(max_length=150)
    phone=models.CharField(max_length=13)
    nationality = models.CharField(max_length=30)
    religion = models.CharField(max_length=50)
    biodata=models.TextField()
    category=models.CharField(max_length=50,choices=CATEGORY,null=True)
    image=models.ImageField(default='default.jpg', upload_to='session/images')

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# class TuitionProfile(models.Model):
class JobProfile(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('in_job', 'In Job'),
    )
    # Choice_style = (
    #     ('Group_Tuition', 'Group Tuition'),
    #     ('Private_Tuition', 'Private Tuition'),
    # )
    Choice_Place = (
        ('remote', 'Remote'),
        ('Onsite', 'On site'),
        # ('Home_Visit', 'Home Visit'),
        # ('My_Place', 'My Place'),
    )
    Choice_Approach = (
        ('web_development', 'Web Development'),
        ('web_design', 'Web Design'),
        ('graphich_design', 'Graphich Design'),
        ('seo', 'Search Engine Optimization'),
        ('digital_merketing', 'Degital Merketing'),
        ('apps_development', 'App Development'),
        ('programing', 'Programing'),
        ('game_development', 'Game Development'),
    )
    Skill = (
        ('social_media_marketing', 'Social media marketing'),
        ('search_engine_optimization', 'Search Engine Optimization'),
        ('adobe_photoshop', 'Adobe Photoshop'),
        ('html', 'html'),
        ('css', 'css'),
        ('javascript', 'javascript'),
        ('wordpress', 'wordpress'),
        ('php', 'php'),
        ('python', 'python'),
        ('go', 'go'),
        ('java', 'java'),
        ('c++', 'c++'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobprofile')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='district')
    # style = MultiSelectField(choices=Choice_style, max_choices=3, max_length=100)
    place = MultiSelectField(choices=Choice_Place,max_choices=3, max_length=100)
    approach = MultiSelectField(choices=Choice_Approach, max_length=100)
    skill = MultiSelectField(choices=Skill, max_length=100)
    # subject = models.ManyToManyField(Subject, related_name='subjects')
    # class_in = models.ManyToManyField(Class_in, related_name='classes')
    expected_salary = models.CharField(max_length=100)
    # days_per_week=models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS)
