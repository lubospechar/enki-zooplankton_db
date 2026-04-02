from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SamplesConfig(AppConfig):
    name = "samples"
    verbose_name = _("Samples")
