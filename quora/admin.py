from django.contrib import admin

from quora.models import Question,Answer,Upvote
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Upvote)

