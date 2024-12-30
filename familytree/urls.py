from rest_framework.routers import DefaultRouter
from .views import FamilyMemberViewSet, RelationshipViewSet

router = DefaultRouter()
router.register('members', FamilyMemberViewSet)
router.register('relationships', RelationshipViewSet)

urlpatterns = router.urls
