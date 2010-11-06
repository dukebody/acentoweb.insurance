from DateTime.DateTime import DateTime

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class PurgeOldRequests(BrowserView):

    def __call__(self):
        """Mark all unsuccessful requests older than 30 days as
        obsolete.
        """

        wf = getToolByName(self.context, 'portal_workflow')
        catalog = getToolByName(self.context, 'portal_catalog')

        now = DateTime()
        thirtydaysago = now - 30
        obsolete = catalog(portal_type='acentoweb.insurance.communityrequest',
                           review_state=['pending', 'quoted'],
                           created={'query':thirtydaysago, 'range':'max'})

        for brain in obsolete:
            wf.doActionFor(brain.getObject(), 'expire')

        return
