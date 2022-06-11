from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.forms import ValidationError
from django.urls import reverse


def is_Esprit_Email(value):
    """
    Tests if an email ends with @esprit.tn
    Args:
        value (any): model or form attribut value
    Returns:
        Boolean: if required constraints are met
    """

    if not str(value).endswith('@esprit.tn'):
        raise ValidationError(
            'Your email must be @esprit.tn', params={'value': value})
    return value
    
# Create your models here.
class User(models.Model):
     name=models.CharField('name',max_length=100)
     first_name=models.CharField(verbose_name="first name",max_length=100)
     email=models.EmailField(verbose_name="Email",null = False,validators=[is_Esprit_Email])
     def __str__(self) -> str:
        return f"{self.name}"
     def get_absolute_url(self):
        return reverse("Hub_home")
        

class Student(User):
    pass

    def __str__(self) -> str:
        return f"{self.name}"

class Coach(User):
    pass

    def __str__(self) -> str:
        return f"{self.name}"


class Project(models.Model):
    project_name = models.CharField(verbose_name="Nom du projet",max_length=100)
    project_duration= models.IntegerField(verbose_name="Duree estimee",default=0)
    time_allocated = models.IntegerField(verbose_name="Temps alloue",validators=[
        MinValueValidator(1,"the min value required is 1"),MaxValueValidator(10,"max value is 10")])
    needs = models.TextField(verbose_name="Besoins",max_length=100)
    desc = models.TextField(verbose_name="description",max_length=250)
    isValid= models.BooleanField(default=False)
    creator = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name= "Project_Owner",
        null = True
    )

    def __str__(self) -> str:
        return f"{self.project_name}"


    supervisor = models.ForeignKey (
            to = Coach,
            on_delete = models.SET_NULL,
            blank = True,
            null=True,
            related_name="project_coach"
        )


    members= models.ManyToManyField (
        to= Student,
        blank= True,
        related_name= "Les_membres",
        through="MembershipInProjects"
    )


class MembershipInProjects(models.Model):
    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    student= models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    time_allocated = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.project}_{ self.student}"

    class Meta:
        verbose_name_plural = "Memberships"