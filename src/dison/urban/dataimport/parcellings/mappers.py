# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.factory import BaseFactory

import re


# Factory
class ParcellingFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.parcellings

    def getPortalType(self, container, **kwargs):
        return 'ParcellingTerm'


class TitleMapper(Mapper):

    regex = '(?P<subdivider>\D*?)\s+(?P<label>\d+/\d+)'

    def mapLabel(self, line):
        title = self.getData('Lotis')
        title = re.search(self.regex, title)
        if title:
            return title.group('label')
        return ''

    def mapSubdividername(self, line):
        title = self.getData('Lotis')
        title = re.search(self.regex, title)
        if title:
            return title.group('subdivider')
        return ''
