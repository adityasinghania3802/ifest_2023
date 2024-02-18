from django.contrib import admin
from .models import *

# Register your models here.
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')


admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Player)