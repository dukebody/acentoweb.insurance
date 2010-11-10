from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.directives import form

from acentoweb.insurance import _


ACCOUNT_NUMBER_LENGTH = 20

class ICommunityPolicy(form.Schema):
    """A community insurance policy.
    """

    title = schema.TextLine(
        title=_(u'Holder'),
        description=_(u'Full name or corporate name')
        )

    nif = schema.TextLine(
        title=_(u'NIF/CIF'),
        )

    company = schema.TextLine(
        title=_(u'Company'),
        )

    date = schema.Date(
        title=_(u'Effective date'),
        )

    bankName = schema.TextLine(
        title=_(u'Bank name'),
        )

    bankAccount = schema.TextLine(
        title=_(u'Bank account number'),
        min_length=ACCOUNT_NUMBER_LENGTH,
        max_length=ACCOUNT_NUMBER_LENGTH,
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

