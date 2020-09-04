from django.urls import path
# from .views import UserListView
from . import views
from django.conf import settings
from .views import GradeUpdateView, StatusUpdateView


app_name = 'assignment_app'
urlpatterns = [
    path('register_course/<int:pk>/', views.register_course, name='register-course'),
    path('main_dashboard/<int:pk>/', views.main_dashboard, name='main-dashboard'),
    path('assignment/<int:pk>/<int:i_n>/', views.submit_assignment, name='submit-assignment'),
    path('assignment/delete/<int:pk>/<int:i_n>/', views.del_assignment, name='delete-assignment'),
    path('assignment/update/<int:pk>/', views.update_assignment, name='update-assignment'),
    path('assignment/view_assignment_pdf/<int:pk>/', views.viewAssignmentPDF, name='view-assignment-pdf'),
    path('download_assignment/<int:pk>/', views.download_pdf, name='download-file'),
    path('score_student_section/<int:pk>/', views.student_result, name='score-student-section'),
    path('assignment/all_students/<int:pk>/', views.all_students, name='all-students'),
    path('assignment/dashboard/', views.dashboard, name='dashboard'),
    path('assignment/submission_denied/<int:pk>/<int:i_n>/', views.submission_denied, name='submission-denied'),
    path('assignment/score_student_section/update/<int:pk>/', GradeUpdateView.as_view(), name='update-grade'),
    # path('status/update/<int:pk>/', StatusUpdateView.as_view(), name='update-statuses'),
    path('update/<int:pk>/', views.update_submitted, name='update-status'),
    path('view_result/<int:pk>/', views.query_results, name='view-result'),
    path('all_courses/<int:pk>/', views.all_courses, name='all-courses'),
    path('del_courses/<int:pk>/', views.del_course, name='del-course'),
    path('del_upload_file/<int:pk>/', views.del_upload_file, name='del-upload-file'),
    path('student_dashboard/', views.student_dashboard, name='student-dashboard'),
    path('del_choose_course/<int:pk>/', views.del_choose_course, name='del-choose-course'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)