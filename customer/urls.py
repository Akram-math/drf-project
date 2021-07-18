from django.conf.urls import url

from customer.views import CustomerView

urlpatterns = [
    url(r'^$', view=CustomerView.as_view(),name='customer'),
    #url
]