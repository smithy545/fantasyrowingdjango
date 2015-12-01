from django.contrib import admin

from .models import Athlete

class AthleteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info',  {'fields':['first_name','last_name','gender','birth_date']}),
        ('Physical Attributes', {'fields':['height','weight','age']}),
        ('Rowing History', {'fields':['clubs','started_rowing']}),
        ('Other',{'fields':['residence']}),
         ]
    def full_name(self, obj):
        return ("%s, %s" % (obj.last_name, obj.first_name))
    full_name.short_description = "Name"
    full_name.admin_order_field = 'last_name'
    list_display = ('full_name','clubs')
    search_fields = ['last_name', 'first_name', 'clubs']

admin.site.register(Athlete, AthleteAdmin)
