from django.contrib import admin

from .models import Pokemon, PokemonEntity

admin.site.register(Pokemon)
admin.site.register(PokemonEntity)
#@admin.register(Pokemon)
#class PokemonAdmin(admin.ModelAdmin):
#    list_display = ('title',)
#    list_filter = ('title',)