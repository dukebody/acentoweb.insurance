from zope import schema

from plone.directives import form

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobFile

from acentoweb.insurance import _

class IVehicleOffer(form.Schema):
    """A vehicle insurance quotation offer.
    """

    juridicalDefense = schema.Bool(
        title=_(u"Juridical defense")
        )

    notes = RichText(
        title=_(u"Notes"),
        required=False,
        )

    attachments = NamedBlobFile(
        title=_(u"Attached documentation"),
        required=False,
        )
