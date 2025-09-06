from django.contrib import admin
from .models import * 

# Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'course', 'grade')
    list_filter = ['course']
    search_fields = ['question_text']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'course']



# Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
