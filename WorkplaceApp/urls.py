from django.urls import path, include  # Import include
from django.contrib.auth import views as auth_views  # Import auth views
from django.views.generic import TemplateView  # Import TemplateView
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('auth/', views.login, name="login"),
    path('acctype/', views.selectacctype, name="acctype"),
    path('acctype/stuacc/', views.createstuacc, name='stuacc'),
    path('acctype/comacc/', views.createcomacc, name="comacc"),

    # Include the password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Serve the password_reset.html template
    path('password_reset.html', TemplateView.as_view(template_name='password_reset.html'), name='password_reset_html'),

    # Your other URLs
    path('stufeed/<str:stuid>/', views.stufeed, name="stufeed"),
    path('addpost/<str:comid>/', views.comaddpost, name="addpost"),
    path('mypost/<str:comid>/', views.mypost, name="mypost"),
    path('addtofav/<str:stuid>,<str:fid>/', views.addtofav, name="addtofav"),
    path('stufav/<str:stuid>/', views.stufav, name="stufav"),
    path('removefrmfav/<str:stuid>,<str:fid>/', views.removefrmfav, name="removefrmfav"),
    path('logout/', views.logout, name="logout"),
    path('editpost/<str:comid>,<str:fid>/', views.editpost, name="editpost"),
    path('deletepost/<str:comid>,<str:fid>/', views.deletepost, name="deletepost"),
    path('apply/<str:stuid>,<str:fid>/', views.apply, name="apply"),
    path('comnotifications/<str:comid>/', views.ComNotifications, name="ComNotifications"),
    path('markasreadCom/<str:comid>,<str:notid>/', views.markasreadCom, name="markasreadCom"),
    path('StuNotifications/<str:stuid>/', views.StuNotifications, name="StuNotifications"),
    path('markasreadStu/<str:stuid>,<str:notid>/', views.markasreadStu, name="markasreadStu"),
    path('commsg/<str:comid>/', views.commsg, name="commsg"),
    path('comchat/<str:comid>,<str:senderid>/', views.comchat, name="comchat"),
    path('msgseen/<str:comid>,<str:msgid>/', views.msgseen, name="msgseen"),
    path('stumsg/<str:stuid>/', views.stumsg, name="stumsg"),
    path('stumsgseen/<str:stuid>,<str:msgid>/', views.stumsgseen, name="stumsgseen"),
    path('stuchat/<str:stuid>,<str:senderid>/', views.stuchat, name="stuchat"),
    path('viewCompany/<str:stuid>,<str:comid>/', views.viewCompany, name="viewCompany"),
    path('accounts/login/', views.login, name="login_submit"),
]
