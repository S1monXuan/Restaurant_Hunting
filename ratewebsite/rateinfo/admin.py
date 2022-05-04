from django.contrib import admin
from .models import Customer, Comment, Year, Season, Section, Type, Restaurant, Holder, Place
# Register your models here.

admin.site.register(Customer)
admin.site.register(Comment)
admin.site.register(Year)
admin.site.register(Season)
admin.site.register(Section)
admin.site.register(Type)
admin.site.register(Restaurant)
admin.site.register(Holder)
admin.site.register(Place)
