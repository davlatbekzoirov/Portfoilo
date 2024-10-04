from django.contrib import admin
from .models import Portfolio, Blog, Technology

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date')
	search_fields = ('title',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date_created')
	search_fields = ('title',)
	filter_horizontal = ('technologies',)  #

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ('name',)
