from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.index, name="index"),
    # 생성
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    # 내용 보기
    path("detail/<int:review_pk>", views.detail, name="detail"),
    # 수정
    path("edit/<int:review_pk>", views.edit, name="edit"),
    path("update/<int:review_pk>", views.update, name="update"),
    # 삭제
    path("delete/<int:review_pk>", views.delete, name="delete"),
]
