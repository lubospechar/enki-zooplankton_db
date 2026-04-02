from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _


class ZooplanktonAdminSite(AdminSite):
    site_header = _("Zooplankton Sample Database")
    site_title = _("Zooplankton Sample Database")
    index_title = _("Database Administration")