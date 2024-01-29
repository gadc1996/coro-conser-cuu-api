from django.contrib import admin

# Register your models here.
from .models import Concert, Score


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    pass
    # list_display = ("name", "date", "time", "location", "image")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
    # list_display = ("name", "composer", "date", "image")
