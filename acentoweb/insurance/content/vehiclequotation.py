from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from acentoweb.insurance import _

class IVehicleQuotation(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """

    # holder data
    holderName = schema.TextLine(
            title=_(u"Holder name"),
        )

    holderFamilyName = schema.TextLine(
            title=_(u"Holder family name"),
        )

    holderNIF = schema.TextLine(
            title=_(u"Holder identity number"),
        )

    holderBirthDate = schema.Date(
            title=_(u"Holder birthday date"),
        )

    holderLicenseDate = schema.Date(
            title=_(u"Holder driving license expedition date"),
        )

    holderLicenseDate = schema.Bool(
            title=_(u"Is the holder the vehicle owner?"),
        )


    holderNIF = schema.TextLine(
            title=_(u"Holder identity number"),
        )

    # vehicle data
    vehicleBrand = schema.TextLine(
            title=_(u"Vehicle brand"),
        )

    vehicleModel = schema.TextLine(
            title=_(u"Vehicle model"),
        )

    vehicleVersion = schema.TextLine(
            title=_(u"Vehicle version"),
        )

    vehiclePlateNumber = schema.TextLine(
            title=_(u"Vehicle license plate number"),
        )

    vehicleFirstLicensingDate = schema.Date(
            title=_(u"Vehicle first licensing date"),
        )

    # notes
    notes = RichText(
            title=_(u"Notes"),
            required=False
        )
