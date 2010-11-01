from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.directives import form

from acentoweb.insurance import _

class ICommunityPolicy(form.Schema):
    """A community insurance policy.
    """

    title = schema.TextLine(
        title=_(u'NIF/CIF'),
        )

    company = schema.TextLine(
        title=_(u'Company'),
        )

    date = schema.Date(
        title=_(u'Effective date'),
        )

    bankAccount = schema.Int(
        title=_(u'Bank account number'),
        )

    paymentMethod = schema.Choice(
        title=_(u'Payment method'),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value='yearly', title=_(u'Yearly')),
             SimpleTerm(value='six-monthly', title=_(u'Each six months')),
             SimpleTerm(value='three-monthly', title=_(u'Each three months')),],
            ),
        )

    additionalNotes = schema.Text(
        title=_(u'Additional notes'),
        )

