from django.urls import path
from main.views import add_light_cone, login_user, logout_user, \
    register, show_main, show_json, show_json_by_id, show_xml, show_xml_by_id, \
    get_item_json, add_item_ajax, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_light_cone/', add_light_cone, name='add_light_cone'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('json_ajax/', get_item_json, name='get_item_json'),
    path('add_light_cone_ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
