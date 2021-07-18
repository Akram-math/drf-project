from django.conf.urls import url

from member.views import MemberView

urlpatterns = [
    url(r'^$', view=MemberView.as_view(),name='member')
    #url
]