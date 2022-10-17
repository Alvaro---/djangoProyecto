from django.contrib import admin
from django.urls import path, include
from website.views import date, home, wellcome, jobs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wellcome, name="wellcome"),
    path('date', date),
    # path('home', home)
    path('', include("posts.urls")),
    path('', include("jobs.urls"))
]

handler404 = "website.views.not_found"
