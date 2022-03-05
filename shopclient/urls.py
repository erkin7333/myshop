from django.urls import path
from .views import IndexView, MainCategory, AboutPage
app_name = "shopclient"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/', MainCategory.as_view(), name='category'),
    path('about/', AboutPage.as_view(), name='about'),
    # path('contact/', ContactPage.as_view(), name='contact')
]