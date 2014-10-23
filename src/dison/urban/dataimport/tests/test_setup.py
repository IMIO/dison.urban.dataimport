# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from dison.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of dison.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if dison.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('dison.dataimport'))

    def test_uninstall(self):
        """Test if dison.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['dison.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('dison.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IDisonDataimportLayer is registered."""
        from dison.dataimport.interfaces import IDisonDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IDisonDataimportLayer in utils.registered_layers())
