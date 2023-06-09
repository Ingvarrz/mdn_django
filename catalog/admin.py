from django.contrib import admin
from .models import Book, Author, Genre, BookInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BookInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]

admin.site.register(Genre)
admin.site.register(BookInstance)