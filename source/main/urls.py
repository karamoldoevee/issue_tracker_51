from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view
from webapp.views.views import IndexView, IssueView, IssueCreateView, issue_update_view, \
    issue_delete_view
from webapp.views.status_views import StatusView, StatusCreateView, status_update_view, status_delete_view
from webapp.views.type_views import TypeView, TypeCreateView, type_update_view, type_delete_view
from webapp.views.project_views import  ProjectIndexView, ProjectView, ProjectCreateView, project_update_view, \
    project_delete_view

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('issue/<int:pk>/', IssueView.as_view(), name='issue_view'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/update/', issue_update_view.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', issue_delete_view.as_view(), name='issue_delete'),
    path('status/view/', StatusView.as_view(), name='status_view'),
    path('type/view/', TypeView.as_view(), name='type_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('type/add', TypeCreateView.as_view(), name='type_add'),
    path('status/<int:pk>/update/', status_update_view.as_view(), name='status_update'),
    path('type/<int:pk>/update/', type_update_view.as_view(), name='type_update'),
    path('status/<int:pk>/delete/', status_delete_view.as_view(), name='status_delete'),
    path('type/<int:pk>/delete/', type_delete_view.as_view(), name='type_delete'),
    path('project/index/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/update/', project_update_view.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', project_delete_view.as_view(), name='project_delete'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout')
]
