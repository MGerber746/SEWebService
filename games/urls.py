from rest_framework.routers import SimpleRouter

from games import views


# Create a router and register our viewsets with it
router = SimpleRouter()
router.register(r'games', views.GameViewSet)
urlpatterns = router.urls
