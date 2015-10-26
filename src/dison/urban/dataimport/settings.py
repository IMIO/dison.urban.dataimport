# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm


class DisonImporterSettingsForm(ImporterSettingsForm):
    """ """


class DisonImporterSettings(ImporterSettings):
    """ """
    form = DisonImporterSettingsForm


class DisonImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = DisonImporterSettings
