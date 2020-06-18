# Use include() to add paths from the home application
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='list_courses'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('new/', views.NewCourseView.as_view(), name='course-new'),
]