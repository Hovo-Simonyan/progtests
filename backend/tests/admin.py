from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" widht="75" height="75"')
        else:
            return 'No photo'


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer')
    list_display_links = ('id', 'answer')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'test')
    list_display_links = ('id', 'question')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'right_answers', 'duration', 'data')
    list_display_links = ('id', 'user')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Test, TestAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Category, CategoryAdmin)
