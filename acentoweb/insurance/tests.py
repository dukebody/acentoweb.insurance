import unittest2 as unittest
import doctest

from plone.testing import z2
from plone.app.testing.layers import IntegrationTesting
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import setRoles

from zope.configuration import xmlconfig

from Products.CMFCore.utils import getToolByName

from acentoweb.insurance.content.vehicleoffer import IVehicleOffer


optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)

class InsuranceLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # load ZCML
        import acentoweb.insurance
        xmlconfig.file('configure.zcml', acentoweb.insurance,
                       context=configurationContext)
        z2.installProduct(app, 'acentoweb.insurance')

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'acentoweb.insurance:default')

INSURANCE_FIXTURE = InsuranceLayer()

INSURANCE_INTEGRATION_TESTING = IntegrationTesting(bases=(INSURANCE_FIXTURE,), name="Insurance:Integration")
INSURANCE_FUNCTIONAL_TESTING = FunctionalTesting(bases=(INSURANCE_FIXTURE,), name="Insurance:Functional")


class TestSetup(unittest.TestCase):
    layer = INSURANCE_INTEGRATION_TESTING

    def test_vehiclequotation_installed(self):
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('acentoweb.insurance.vehiclequotation'), None)

    def test_vehicleoffer_installed(self):
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('acentoweb.insurance.vehicleoffer'), None)

    def test_communityrequest_installed(self):
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('acentoweb.insurance.communityrequest'), None)

    def test_communitypolicy_installed(self):
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('acentoweb.insurance.communitypolicy'), None)

    def test_vehicleoffer_adding(self):
        """Check that we can add vehicle insurance offers into
        vehicle quotations.
        """
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_NAME, ['Contributor'])

        portal.invokeFactory('acentoweb.insurance.vehiclequotation', 'quotation')
        quotation = portal['quotation']
        quotation.invokeFactory('acentoweb.insurance.vehicleoffer', 'vh1')
        vh1 = quotation['vh1']
        self.failUnless(IVehicleOffer.providedBy(vh1))

    def test_wf_existence(self):
        """Check that our custom workflows are present.
        """
        portal = self.layer['portal']
        wt = portal.portal_workflow
        self.failUnless('acentoweb.insurance.quotation_workflow' in wt.objectIds())

    def test_quotationwf_bindings(self):
        """Check that the quotation_workflow is binded to all quotation
        types.
        """
        portal = self.layer['portal']
        wt = portal.portal_workflow
        self.failUnless('acentoweb.insurance.quotation_workflow' in wt.getChainForPortalType('acentoweb.insurance.vehiclequotation'))
        self.failUnless('acentoweb.insurance.quotation_workflow' in wt.getChainForPortalType('acentoweb.insurance.communityrequest'))

    def test_allowedtypesintocommunityrequest(self):
        """
        Check that files and community quotation offers are addable
        into community quotation requests.
        """
        portal = self.layer['portal']
        typesTool = getToolByName(portal, 'portal_types')
        allowed_types = typesTool['acentoweb.insurance.communityrequest'].getProperty('allowed_content_types')
        self.assertTrue('File' in allowed_types)
        self.assertTrue('acentoweb.insurance.communityoffer' in allowed_types)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        unittest.makeSuite(TestSetup)
        ])
    return suite

