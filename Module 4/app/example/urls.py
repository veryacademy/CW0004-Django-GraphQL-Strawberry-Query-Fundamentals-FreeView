from django.urls import path
from strawberry.django.views import GraphQLView
from .graphql.schema import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema)),
]