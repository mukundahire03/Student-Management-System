from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_Views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name = 'base'),

    # Login Path
    path('',views.LOGIN, name = 'login'),
    path('doLogin',views.doLogin, name = 'doLogin'),
    path('doLogout',views.doLogout, name = 'logout'),

    # Profile Update
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # This is Hod Panel Url
    path('Hod/Home', Hod_Views.home, name='hod_home'),

    # This is Student Section
    path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_Views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin>', Hod_Views.DELETE_STUDENT, name='delete_student'),


    # This is Staff Section
    path('Hod/Staff/Add', Hod_Views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', Hod_Views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_Views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', Hod_Views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_Views.DELETE_STAFF, name='delete_staff'),


    # This is Department Section
    path('Hod/Department/Add', Hod_Views.ADD_DEPARTMENT, name='add_department'),
    path('Hod/Department/View', Hod_Views.VIEW_DEPARTMENT, name='view_department'),
    path('Hod/Department/Edit/<str:id>', Hod_Views.EDIT_DEPARTMENT, name='edit_department'),
    path('Hod/Department/Update', Hod_Views.UPDATE_DEPARTMENT, name='update_department'),
    path('Hod/Department/Delete/<str:id>', Hod_Views.DELETE_DEPARTMENT, name='delete_department'),

    # This is Subject Section
    path('Hod/Subject/Add', Hod_Views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_Views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_Views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/Update', Hod_Views.UPDATE_SUBJECTT, name='update_subject'),
    path('Hod/Subject/Delete/<str:id>', Hod_Views.DELETE_SUBJECT, name='delete_subject'),



              ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
