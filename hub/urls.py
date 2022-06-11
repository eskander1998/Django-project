from unicodedata import name
from .views import Coach_addModelForm, HomePage, ListCoach, DetailCoach,List_Projet, ListStudent,ProjectlistView,Coach_add,CoachCreateView,CoachUpdateView
from django.urls import path

urlpatterns = [
    path('home/', HomePage, name="Hub_home"),
    path('listCoach/', ListCoach, name="Hub_Coach_list"),
    path('detailcoach/<int:id>', DetailCoach, name="Hub_detail_Coach"),
    path('coachupdate/<int:pk>', CoachUpdateView.as_view(), name="Hub_update_Coach"),
    path('listproject/', List_Projet, name="Hub_Project_list"),
    path('listproject2/', ProjectlistView.as_view(), name="Hub_ProjectListview_list"),
    path('coachadd/', Coach_add, name="Hub_Coach_add"),
    path('coachaddmodelform/', Coach_addModelForm, name="Hub_Coach_addmodelform"),
    path('coachaddmodelcreateview/', CoachCreateView.as_view(), name="Hub_CoachCreateView"),
    path('listStudents/', ListStudent, name="Hub_student_list"),


]
