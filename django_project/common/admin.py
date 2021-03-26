from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Group as GroupModel,
    Membership as MembershipModel,
    Person as PersonModel,
)


class PersonAdmin(TranslationAdmin):
    group_fieldsets = True


class GroupAdmin(TranslationAdmin):
    group_fieldsets = True


admin.site.register(PersonModel, PersonAdmin)
admin.site.register(GroupModel, GroupAdmin)
admin.site.register(MembershipModel)
