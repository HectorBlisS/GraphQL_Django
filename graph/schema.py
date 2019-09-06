from graphene import Schema, ObjectType
from api.schema import Query

class Query(Query, ObjectType):
    pass

schema = Schema(query=Query)