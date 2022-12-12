from django.urls import path
from beli_karya.views import *

app_name = 'beli_karya'

urlpatterns = [
    path('get-karyas', get_karyas, name='get_karyas'),
    path('', beli_karya, name='beli_karya'),
    path('get-karyas-json', get_karya_json, name='get_karya_json'),
    path('post-beli-karya-json', post_beli_karya_json, name='post_beli_karya_json')
]