from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('maincourse', views.maincourse, name='maincourse'),
    path('addon', views.addon, name='addon'),
    path('semresults', views.result, name='result'),

    path('markupdate', views.markupdate, name='markupdate'),
    path('scheduleupdate', views.scheduleupdate, name='scheduleupdate'),
    path('viewschedule', views.viewschedule, name='viewschedule'),
    path('editmark/<int:id>', views.markedit),
    path('updatemark/<int:id>', views.updatemark),

    path('editschedule/<int:id>', views.scheduleedit),
    path('updateschedule/<int:id>', views.updateschedule),
    path('deleteschedule/<int:id>', views.destroyschedule),
    path('addschedule',views.addschedule,name='addschedule'),

    path('manageaddon', views.manageaddon, name='manageaddon'),
    path('editaddon/<int:id>', views.addonedit),
    path('updateaddon/<int:id>', views.updateaddon),
    path('deleteaddon/<int:id>', views.destroyaddon),
    path('addaddon',views.addaddon,name='addaddon'),

    path('defaultlist', views.defaultlist, name='defaultlist'),
    path('editdefault/<int:id>', views.defaultedit),
    path('updatedefault/<int:id>', views.updatedefault),
    path('deletedefault/<int:id>', views.destroydefault),
    path('adddefault',views.adddefault,name='adddefault'),

    path('duelist', views.duelist, name='duelist'),
    path('editdue/<int:id>', views.dueedit),
    path('updatedue/<int:id>', views.updatedue),
    path('deletedue/<int:id>', views.destroydue),
    path('adddue',views.adddue,name='adddue'),

    path('allotroom', views.allotroom, name='allotroom'),
    path('editallot/<int:id>', views.allotedit),
    path('updateallot/<int:id>', views.updateallot),
    path('deleteallot/<int:id>', views.destroyallot),
    path('addallot',views.addallot,name='addallot'),

    path('loanlist', views.loanlist, name='loanlist'),
    path('editloan/<int:id>', views.loanedit),
    path('updateloan/<int:id>', views.updateloan),
    path('deleteloan/<int:id>', views.destroyloan),
    path('addloan',views.addloan,name='addloan'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
