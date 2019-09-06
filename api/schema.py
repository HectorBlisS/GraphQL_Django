
import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
from api.models import Book

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(object):
    all_users = graphene.List(UserType)
    all_books = graphene.List(BookType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_books(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Book.objects.select_related('user').all()

