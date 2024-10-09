from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions, register
from .models import FeedbackModel


@register(FeedbackModel)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)
