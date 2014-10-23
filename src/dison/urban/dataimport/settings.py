# -*- coding: utf-8 -*-

from imio.urban.dataimport.settings import ImporterSettingsEditForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterFromSettingsForm
from imio.urban.dataimport.urbaweb.settings import UrbawebImporterSettings


class DisonImporterSettingsEditForm(ImporterSettingsEditForm):
    """ """


class DisonImporterSettings(UrbawebImporterSettings):
    """ """
    form = DisonImporterSettingsEditForm


class DisonImporterFromSettingsForm(UrbawebImporterFromSettingsForm):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """

        args = {
            'db_name': 'Tab_Urba 97.mdb',
        }

        return args
