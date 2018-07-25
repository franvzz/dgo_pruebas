from django.urls import path
from apps.uno_a_muchos.views import (
    UnoAMuchosList,
    UnoAMuchosCreate,
    UnoAMuchosDetail,
    UnoAMuchosUpdate,
    UnoAMuchosDelete,
)

app_name = "Uno A Uno"

urlpatterns = [
    path('delete/<int:pk>', UnoAMuchosDelete.as_view(), name="delete"),
    path('update/<int:pk>', UnoAMuchosUpdate.as_view(), name="update"),
    path('detail/<int:pk>', UnoAMuchosDetail.as_view(), name="detail"),
    path('add', UnoAMuchosCreate.as_view(), name="create"),
    path('', UnoAMuchosList.as_view(), name="list"),
]
