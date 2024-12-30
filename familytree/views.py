from rest_framework.viewsets import ModelViewSet
from .models import FamilyMember, Relationship
from .serializers import FamilyMemberSerializer, RelationshipSerializer


class FamilyMemberViewSet(ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer


class RelationshipViewSet(ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
