from django.urls import path
from recipe.views import (
    FoodCategoriesAllViews,
    FoodCategoriesCrudViews,
    FoodAllViews,
)

urlpatterns = [
    path('food_categories_all_views/', FoodCategoriesAllViews.as_view()),
    path('food_categories_crud_views/', FoodCategoriesCrudViews.as_view()),
    path('food_all_views/', FoodAllViews.as_view()),

]
