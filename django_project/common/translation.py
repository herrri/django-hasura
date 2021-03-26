from modeltranslation.translator import translator, TranslationOptions

from .models import Person, Group


class PersonTranslationOptions(TranslationOptions):
    fields = ("description",)


class GroupTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Person, PersonTranslationOptions )
translator.register(Group, GroupTranslationOptions)