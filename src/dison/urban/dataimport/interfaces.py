# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.interfaces import IAccessImporter

from plone.theme.interfaces import IDefaultPloneLayer


class IDisonDataImporter(IAccessImporter):
    """ marker interface for Dison Agorawin importer """


class IDisonUrbanDataimportLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""
