from django.urls import path 
from . import views
urlpatterns=[
    path('',views.yerkir,name='Page1'),
    path('Qaxaq/<int:id>/',views.qaxaq,name='Page2'),
    path('Poxoc/<int:id>/',views.poxoc,name='Page3'),
    path('Shenq/<int:id>/',views.shenq,name='Page4'),
    path('Bnakaran/<int:id>/',views.bnakaran,name='Page5'),
    path('Molorak/<int:id>/',views.molorak,name='Page6'),
    path('Support/',views.support,name='support')
]
