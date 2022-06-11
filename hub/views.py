from re import template
from turtle import update
from django.views.generic import ListView,CreateView,UpdateView
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import CoachForm, CoachModelForm, StudentModelForm
from .models import Coach,Project, Student
# Create your views here.
def HomePage(request):
    return HttpResponse("<h1>Hello to .... </h1>")

def ListCoach(request):
    list = Coach.objects.all() #equivalent de select * from coach
    return render(
        request,
        'hub/list.html',
        {
            'list_Coach' :list
        }
    )

def DetailCoach(request,id):
    list = Coach.objects.get(id=id) #equivalent de select * from coach
    return render(
        request,
        'hub/detailcoach.html',
        {
            'detailcoach' :list
        }
    )


def List_Projet(request):
    list= Project.objects.all()
    return render(
        request,
        'hub/project_list.html',
        {
            'list_project' :list
        }
    )


class ProjectlistView(ListView):
    model=Project
    template_name='hub/project_list.html'    


class StudentListView(ListView):
    model = Student
    template_name ='hub/list_student.html'
    context_object_name='students'

# class StudentDetailView(DetailView):
#     model = Student
#     template_name ='hub/detail_student.html'

#########   Methode 1 pour creer un formulaire avec un template 
def Coach_add(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lasttname=request.POST.get('lastname')
        email=request.POST.get('email')
        Coach.objects.create(
            name= firstname,
            first_name=lasttname,
            email=email
        )
        return redirect('Hub_Coach_list')
    # print(request.POST)
    return render(request,'hub/coach_add.html')




def Coach_add(request):
    form =CoachForm()
    if request.method=="POST":
        form = CoachForm(request.POST)
        if form.is_valid():
            # firstname=form.cleaned_data.get('firstname')
            # lasttname=form.cleaned_data.get('lastname')
            # email=form.cleaned_data.get('email')
            # Coach.objects.create(
            #     name= firstname,
            #     first_name=lasttname,
            #     email=email
            # )
            Coach.objects.create(**form.cleaned_data)
            return redirect('Hub_Coach_list')
    # print(request.POST)
    return render(request,
                    'hub/coach_add.html',
                    {
                        'form' : form
                    })
    



def Coach_addModelForm(request):
    form =CoachForm()
    if request.method=="POST":
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach=form.save(commit=False)
            #traitement 
            coach.save()
            return redirect('Hub_Coach_list')
    return render(request,
                    'hub/coach_addModelform.html',
                    {
                        'form' : form
                    })
    
class CoachCreateView(CreateView):
    model= Coach
    form_class= CoachModelForm
    template_name="hub/coach_addModelform.html" 
    def get_success_url(self):
        return redirect('Hub_home')
        
class CoachUpdateView(UpdateView):
    model = Coach
    form_class = CoachModelForm
    template_name="hub/coach_addModelform.html" 
    



    
# def Student_addModelForm(request):
#     form =StudentModelForm()
#     if request.method=="POST":
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             student=form.save(commit=False)
#             #traitement 
#             student.save()
#             return redirect('Hub_Coach_list')
#     return render(request,
#                     'hub/coach_addModelform.html',
#                     {
#                         'form' : form
#                     })
    

def ListStudent(request):
    list = Student.objects.all() #equivalent de select * from coach
    return render(
        request,
        'hub/list_student.html',
        {
            'list_student' :list
        }
    )    