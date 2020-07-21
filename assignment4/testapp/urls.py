from django.urls import path
from . import views

#from django.urls import path, include
#import testapp.views as testappviews
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'testapp'


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('testapp/', include('testapp.urls'))
    #path('testapp/wahiyat', testappviews.PAnalysisview)
    path('mainpage', views.PAnalysisview),
    path('<int:userid>', views.testlogininfo),
    path('<slug:userid>/<slug:userpwd>', views.testlogininfo2),
    path('testform', views.testformdisplay),
    path('testapp/create', views.CreateWview)
]