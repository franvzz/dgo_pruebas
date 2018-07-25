from django.urls import path
from apps.uno_a_uno.views import (
    UnoAUnoList,
    UnoAUnoCreate,
    UnoAUnoDetail,
    UnoAUnoUpdate,
    UnoAUnoDelete,
)

app_name = "Uno A Uno"

urlpatterns = [
    path('delete/<int:pk>', UnoAUnoDelete.as_view(), name="delete"),
    path('update/<int:pk>', UnoAUnoUpdate.as_view(), name="update"),
    path('detail/<int:pk>', UnoAUnoDetail.as_view(), name="detail"),
    path('add', UnoAUnoCreate.as_view(), name="create"),
    path('', UnoAUnoList.as_view(), name="list"),
]
