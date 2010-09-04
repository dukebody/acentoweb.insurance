from zope import schema

from plone.directives import form

from acentoweb.insurance import _
from acentoweb.insurance.vocabulary import YesNoVocabulary

class ICommunityOffer(form.Schema):
    """A community quotation offer.
    """

    title = schema.TextLine(
        title=_(u'Company'),
        )

    fire = schema.Choice(
        title=_(u'Fire'),
        vocabulary=YesNoVocabulary,
        )

    cr = schema.Decimal(
        title=_(u'CR (euros)'),
        )

    crWaterExcess = schema.Decimal(
        title=_(u'CR excess for water damage'),
        )

    crThirds = schema.Choice(
        title=_(u'Consider third owners'),
        vocabulary=YesNoVocabulary,
        )

    glasses = schema.Choice(
        title=_(u'Glasses'),
        vocabulary=YesNoVocabulary,
        )

    burglary = schema.Choice(
        title=_(u'Burglary'),
        vocabulary=YesNoVocabulary,
        )

    communityWaters = schema.Choice(
        title=_(u'Communitary waters'),
        vocabulary=YesNoVocabulary,
        )

    privateWaters = schema.Choice(
        title=_(u'Private waters'),
        vocabulary=YesNoVocabulary,
        )

    excess = schema.Decimal(
        title=_(u'Excess (euros)'),
        )

    warrantyExtension = schema.Choice(
        title=_(u'Warranty extension'),
        vocabulary=YesNoVocabulary,
        )

    steticalDamages = schema.Choice(
        title=_(u'Stetical damages'),
        vocabulary=YesNoVocabulary,
        )

    twentyForSevenAssistance = schema.Choice(
        title=_(u'24h assistance'),
        vocabulary=YesNoVocabulary,
        )

    damageClaim = schema.Choice(
        title=_(u'Damage claim'),
        vocabulary=YesNoVocabulary,
        )

    juridicalDefense = schema.Choice(
        title=_(u'Juridical defense'),
        vocabulary=YesNoVocabulary,
        )

    totalAnualPremium = schema.Decimal(
        title=_(u'Total anual premium'),
        )
