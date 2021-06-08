from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from take_home.questions.api.views import QuestionViewSet, AnswerViewSet, ResponseViewSet, QuestionListViewSet
from take_home.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("questions", QuestionViewSet)
router.register("question_lists", QuestionListViewSet)
router.register("answers", AnswerViewSet)
router.register("responses", ResponseViewSet)


app_name = "api"
urlpatterns = router.urls
