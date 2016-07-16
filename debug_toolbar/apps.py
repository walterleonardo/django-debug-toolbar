from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from debug_toolbar import settings as dt_settings


class DebugToolbarConfig(AppConfig):
    name = 'debug_toolbar'
    verbose_name = _("Debug Toolbar")

    def ready(self):
        dt_settings.check_middleware()
