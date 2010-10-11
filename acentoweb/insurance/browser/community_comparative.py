from Products.Five.browser import BrowserView

from acentoweb.insurance.vocabulary import YesNoVocabulary


class CommunityComparativeView(BrowserView):

    def getTitleFromValue(self, value):
        """Return the title of the term with the provided value using
        the YesNoVocabulary.
        """

        return YesNoVocabulary.getTerm(value).title

    def getOffers(self):
        return self.context.listFolderContents(
            contentFilter={'portal_type':'acentoweb.insurance.communityoffer'})
