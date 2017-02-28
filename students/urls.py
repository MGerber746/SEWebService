from rest_framework.routers import SimpleRouter

from teachers import views


# Create a router and register our viewsets with it
router = SimpleRouter()
router.register(r'teachers', views.TeacherViewSet)
urlpatterns = router.urls
