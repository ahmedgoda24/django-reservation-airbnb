from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path( '',views.PropertyList.as_view() , name='property_list' ),
    path('<slug:slug>',views.PropertyDetail.as_view() , name='property_detail'),
    # path( 'new',views.NewProperty.as_view() , name='property_new' ),
    # path('category/<str:category>',views.property_by_category , name='property_by_category'),
    # path('api/list' , api_view.PropertyListApi.as_view(), name='property_api_list'),
    # path('api/list/<int:pk>' , api_view.PropertyDetailApi.as_view(), name='property_api_detail')
]
