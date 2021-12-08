from django.conf.urls import url
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.urls import path

urlpatterns = [
    path('accounts/password_reset/',PasswordResetView.as_view(),name='password_reset'),
]

# from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),


    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),


        
    url(r'^complete/$', password_reset_complete, name='password_reset_complete'),
]
