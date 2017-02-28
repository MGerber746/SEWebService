from rest_framework.routers import SimpleRouter

from students import views


# Create a router and register our viewsets with it
router = SimpleRouter()
router.register(r'students', views.StudentViewSet)
urlpatterns = router.urls
