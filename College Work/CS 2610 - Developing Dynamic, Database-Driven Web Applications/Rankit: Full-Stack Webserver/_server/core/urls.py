from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('get_user/', view=views.get_user, name="Get user"),
    path('create_list/', view=views.create_list, name="Create list"),
    path('view_list/<int:id>/', view=views.view_list, name="View list"),
    path('edit_list/<int:id>/', view=views.edit_list, name="Edit list"),
    path('my_lists/', view=views.my_lists, name="My lists"),
    path('add_item/', view=views.add_item, name="Add item"),
    path('delete_item/<int:id>/', view=views.delete_item, name="Delete item"),
    path('update_items/', view=views.update_items, name="Update items"),
    path('configure_list/', view=views.configure_list, name="Configure list"),
    path('upload_image/', view=views.upload_image, name="Upload image"),
    path('my_images/', view=views.my_images, name="Get user images"),
    path('get_image/<str:id>/', view=views.get_image, name="Get image"),
    path('delete_image/<int:id>/', view=views.delete_image, name="Delete image"),
    path('get_list_images/<int:id>/', view=views.get_list_images, name="Get list images"),
    path('get_profile/<int:id>/', view=views.get_profile, name="Get profile"),
    path('configure_profile/', view=views.configure_profile, name="Configure profile"),
    path('comment/<int:id>/', view=views.comment, name="Comment on list"),
    path('get_comments/<int:id>/', view=views.get_comments, name="Get comments on list"),
    path('get_featured_lists/', view=views.get_featured_lists, name="Get featured lists"),
    path('search/', view=views.search, name="Search")
]