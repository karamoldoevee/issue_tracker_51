from django.urls import path

from .views.issue_views import IndexView, IssueView, IssueCreateView, IssueUpdateView, IssueDeleteView
from .views.status_views import StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView
from .views.type_views import  TypeView, TypeCreateView, TypeUpdateView, TypeDeleteView
from .views.project_views import ProjectIndexView, ProjectView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .views.user_views import UserProjectView, UserProjectCreateView, UserProjectUpdateView, UserProjectDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
    path('status/view/', StatusView.as_view(), name='status_view'),
    path('type/view/', TypeView.as_view(), name='type_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('type/add', TypeCreateView.as_view(), name='type_add'),
    path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('project/index/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('user/view/', UserProjectView.as_view(), name='user_view'),
    path('user/add/', UserProjectCreateView.as_view(), name='user_add'),
    path('user/<int:pk>/update/', UserProjectUpdateView.as_view(), name='user_update'),
    path('user/<int:pk>/user_delete/', UserProjectDeleteView.as_view(), name='user_delete'),
]
