# adminconfig/apps.py
from django.apps import AppConfig
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AdminconfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "adminconfig"

    def ready(self):
        admin.site.site_header = _("Zooplankton Sample Database")
        admin.site.site_title = _("Zooplankton Sample Database")
        admin.site.index_title = _("Database Administration")