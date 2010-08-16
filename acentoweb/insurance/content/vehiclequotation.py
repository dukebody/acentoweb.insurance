from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText

from acentoweb.insurance import _

class IVehicleQuotation(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """

    # holder data
    form.fieldset('holderData',
                  label=_(u"Holder data"),
                  fields=['holderName',
                          'holderFamilyName',
                          'holderNIF',
                          'holderBirthDate',
                          'holderLicenseDate',]
                  )

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

    holderOwnership = schema.Bool(
            title=_(u"Is the holder the vehicle owner?"),
        )

    # vehicle data
    form.fieldset('vehicleData',
                  label=_(u"Vehicle data"),
                  fields=['vehicleBrand',
                          'vehicleModel',
                          'vehicleVersion',
                          'vehiclePlateNumber',
                          'vehicleFirstLicensingDate',]
                  )
    
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
    form.fieldset('additionalInfo',
                  label=_(u"Additional info"),
                  fields=['notes',]
                  )

    notes = RichText(
            title=_(u"Notes"),
            required=False
        )
