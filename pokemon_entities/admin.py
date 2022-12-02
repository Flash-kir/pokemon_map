from django.contrib import admin

from .models import Pokemon

admin.site.register(Pokemon)
#@admin.register(Pokemon)
#class PokemonAdmin(admin.ModelAdmin):
#    list_display = ('title',)
#    list_filter = ('title',)