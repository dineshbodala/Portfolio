from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio



admin.site.register(Home)



class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 4

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]



admin.site.register(Portfolio)


