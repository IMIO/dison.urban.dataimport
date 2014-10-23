# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from dison.urban.dataimport.interfaces import IDisonDataImporter


class DisonDataImporter(UrbawebDataImporter):
    """ """

    implements(IDisonDataImporter)
