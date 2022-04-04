from django.contrib import admin
from .models import Word,CastomUser,Message
from .forms import ProfileForm


@admin.register(CastomUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','external_id','name')
    form  = ProfileForm

    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','profile','text','create_at')


# admin.site.register(CastomUser)
admin.site.register(Word)
