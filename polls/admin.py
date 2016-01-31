from django.contrib import admin

from .models import Decision, Question

class DecisionInline(admin.TabularInline):
    model = Decision
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':
        ['collapse']}),
    ]

    inlines = [DecisionInline]


admin.site.register(Question, QuestionAdmin)
