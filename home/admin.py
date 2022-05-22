from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import themecolor,Links,Profil
admin.site.register(themecolor)
admin.site.register(Links)



@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    '''Admin View for Profil'''
    list_display = ('user','total_social_links')
    readonly_fields = ('total_social_links','social_links')

    def total_social_links(self, obj):
        return f'{obj.user.links_set.count()}'

    def social_links(self, instance):
        return format_html_join(
            mark_safe('<br>'),
            '{}',
            ((mark_safe(f"{link.name} | <a href='{link.link}'>{link.link} </a>"),) for link in instance.user.links_set.all())
        )or mark_safe("<span class='errors'>The user does not have any link.</span>")

