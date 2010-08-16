import unittest2 as unittest
import doctest

from plone.app.testing.layers import IntegrationTesting
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

from Products.CMFCore.utils import getToolByName


optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

class InsuranceLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # load ZCML
        import acentoweb.insurance
        xmlconfig.file('configure.zcml', acentoweb.insurance,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'acentoweb.insurance:default')

INSURANCE_FIXTURE = InsuranceLayer()

INSURANCE_INTEGRATION_TESTING = IntegrationTesting(bases=(INSURANCE_FIXTURE,), name="Insurance:Integration")
INSURANCE_FUNCTIONAL_TESTING = FunctionalTesting(bases=(INSURANCE_FIXTURE,), name="Insurance:Functional")


class TestSetup(unittest.TestCase):
    layer = INSURANCE_INTEGRATION_TESTING

    def test_quotation_installed(self):
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('InsuranceQuotation'), None)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(TestSetup)
        ])
    return suite

