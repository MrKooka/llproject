from django.contrib import admin
from .models import Word,Customer,Message,LogModels
from .forms import ProfileForm


@admin.register(Customer)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','chat_id','name')
    form  = ProfileForm

    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','profile','text','create_at')


# admin.site.register(CastomUser)
admin.site.register(Word)
admin.site.register(LogModels)

