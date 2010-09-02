from five import grok
from zope import schema

from plone.directives import form, dexterity

from plone.app.textfield import RichText
from collective.dnifield.field import DNI

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
                          'holderLicenseDate',
                          'holderOwnership']
                  )

    holderName = schema.TextLine(
            title=_(u"Holder name"),
        )

    holderFamilyName = schema.TextLine(
            title=_(u"Holder family name"),
        )

    holderNIF = DNI(
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

    # driver data (optional)
    form.fieldset('driverData',
                  label=_(u"Driver data"),
                  fields=['driverName',
                          'driverFamilyName',
                          'driverNIF',
                          'driverBirthDate',
                          'driverLicenseDate',
                          'driverOwnership']
                  )

    driverName = schema.TextLine(
            title=_(u"Driver name"),
            required=False,
        )

    driverFamilyName = schema.TextLine(
            title=_(u"Driver family name"),
            required=False,
        )

    driverNIF = schema.TextLine(
            title=_(u"Driver identity number"),
            required=False,        
        )

    driverBirthDate = schema.Date(
            title=_(u"Driver birthday date"),
            required=False,        
        )

    driverLicenseDate = schema.Date(
            title=_(u"Driver driving license expedition date"),
            required=False,
        )

    driverOwnership = schema.Bool(
            title=_(u"Is the driver the vehicle owner?"),
        )

    # auxiliar driver data (optional)
    form.fieldset('auxDriverData',
                  label=_(u"Auxiliar driver data"),
                  fields=['auxDriverName',
                          'auxDriverFamilyName',
                          'auxDriverNIF',
                          'auxDriverBirthDate',
                          'auxDriverLicenseDate',
                          'auxDriverOwnership']
                  )

    auxDriverName = schema.TextLine(
            title=_(u"Auxiliar driver name"),
            required=False,        
        )

    auxDriverFamilyName = schema.TextLine(
            title=_(u"Auxiliar driver family name"),
            required=False,        
        )

    auxDriverNIF = schema.TextLine(
            title=_(u"Auxiliar driver identity number"),
            required=False,        
        )

    auxDriverBirthDate = schema.Date(
            title=_(u"Auxiliar driver birthday date"),
            required=False,        
        )

    auxDriverLicenseDate = schema.Date(
            title=_(u"Auxiliar driver driving license expedition date"),
            required=False,        
        )

    auxDriverOwnership = schema.Bool(
            title=_(u"Is the auxiliar driver the vehicle owner?"),
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
