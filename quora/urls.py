from django.urls import path
from quora.views import signup,signin,signout,dashboard,questions,discussion,upvote,delete_question,delete_answer
urlpatterns = [
    path('signup/',signup),
    path('signin/',signin),
    path('signout/',signout),
    path('dashboard/',dashboard),
    path('questions/',questions),
    path('discussion/<int:question_id>/',discussion),
    path('upvote/<int:answer_id>/', upvote),
    path('delete_question/<int:question_id>/',delete_question),
    path('delete_answer/<int:answer_id>/',delete_answer),
]