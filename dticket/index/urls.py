from django.conf.urls import url

from index.views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]
