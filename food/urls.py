from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('recipe_list',views.recipe_list,name='recips_list'),
    path('about',views.about,name='about'),
    path('add_your_own_recipes',views.add_your_own_recipes,name='add_your_own_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.search_results, name='search_results'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
