from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.directives import form

from plone.app.textfield import RichText

from acentoweb.insurance import _
from acentoweb.insurance.vocabulary import YesNoVocabulary


class ICommunityRequest(form.Schema):
    """A community quotation request.
    """

    # holder data
    form.fieldset('holderData',
                  label=_(u"Holder"),
                  fields=['title', # holderName
                          'holderId',
                          'holderAddress',
                          'holderTownPostCode',
                          'holderPhone',
                          'holderEMail']
                  )

    title = schema.TextLine(
        title=_(u"Name"),
        )

    holderId = schema.TextLine(
        title=_(u"NIF/CIF"),
        required=False,
        )

    holderAddress = schema.TextLine(
        title=_(u"Address"),
        required=False,
        )

    holderTownPostCode = schema.TextLine(
        title=_(u"Town - Postal Code"),
        required=False,
        )

    holderPhone = schema.TextLine(
        title=_(u"Phone number"),
        required=False,
        )

    holderEMail = schema.TextLine(
        title=_(u"E-mail"),
        required=False,
        )


    # insurance data
    form.fieldset('insuranceData',
                  label=_(u"Insurance"),
                  fields=['insuranceSituation',
                          'insuranceTownPostCode',
                          'insuranceBuildingAdmin',
                          'insuranceContactPerson',
                          'insuranceContactPhone']
                  )

    insuranceSituation = schema.TextLine(
        title=_(u"Situation"),
        required=False,
        )

    insuranceTownPostCode = schema.TextLine(
        title=_(u"Town - Postal Code"),
        required=False,
        )

    insuranceBuildingAdmin = schema.TextLine(
        title=_(u"Building Administrator"),
        required=False,
        )

    insuranceContactPerson = schema.TextLine(
        title=_(u"Contact person"),
        required=False,
        )

    insuranceContactPhone = schema.TextLine(
        title=_(u"Contact phone"),
        required=False,
        )


    # insurance values
    form.fieldset('valuesData',
                  label=_(u"Values"),
                  fields=['continentTotal',
                          'containedTotal',
                          'continentGarages',
                          'continentCellars',
                          'oldInsurance',
                          'oldInsuranceCompany',
                          'oldInsuranceExpiry'
                          ]
                  )

    continentTotal = schema.TextLine(
        title=_(u'Total continent'),
        required=False,
        )


    containedTotal = schema.TextLine(
        title=_(u'Total contained'),
        required=False,
        )

    continentGarages = schema.TextLine(
        title=_(u'Garages continent'),
        required=False,
        )

    continentCellars = schema.TextLine(
        title=_(u'Cellars continent'),
        required=False,
        )

    oldInsurance = schema.Choice(
        title=_(u'Does it have an insurance policy now?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    oldInsuranceCompany = schema.TextLine(
        title=_(u'Current insurance company'),
        required=False,
        )

    oldInsuranceExpiry = schema.TextLine(
        title=_(u'Expiry date'),
        required=False,
        )


    # agent data
    form.fieldset('agentData',
                  label=_(u"Agent"),
                  fields=['agentName',
                          'agentCode',]
                  )

    agentName = schema.TextLine(
        title=_(u'Agent name'),
        required=False,
        )

    agentCode = schema.TextLine(
        title=_(u'Agent code'),
        required=False,
        )



    # building data
    form.fieldset('buildingData',
                  label=_(u"Building"),
                  fields=['buildingYear',
                          'closedNeighborhood',
                          'm2',
                          'm2Gardens',
                          'nBuildings',
                          'nMainDoors',
                          'otherAccesses',
                          'nFloors',
                          'nHousesFloor',
                          'nHouses',
                          'nUndergroundFloors',
                          'nCellars',
                          'cellarsInCommunity',
                          'nSwimmingPools',
                          'garages',
                          'garagesInCommunity',
                          'garageValue',
                          'nParkingLots',
                          'nAdditionalHouses',
                          'm2AddHouse',
                          'm2AddHouseTotal',
                          'nOffices',
                          'm2Offices',
                          'housesDestination',
                          'electricRepairmentsYear',
                          'electricRepairmentsType',
                          'drainPipesRepairmentsYear',
                          'waterConductionRepairmentsYear',
                          'businesses',
                          'nBusinesses',
                          'm2Businesses',
                          'businessesInCommunity',
                          'businessesDescription',
                          'nExtinguishers'
                          ]
                  )

    buildingYear = schema.Int(
        title=_(u'Year the building was built'),
        required=False,
        )

    closedNeighborhood = schema.Choice(
        title=_(u'Is it a closed neighborhood?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    m2 = schema.Int(
        title=_(u'Number of square meters built'),
        required=False,
        )

    m2Gardens = schema.Int(
        title=_(u'Number of garden square meters'),
        required=False,
        )

    nBuildings = schema.Int(
        title=_(u'Number of buildings'),
        required=False,
        )

    nMainDoors = schema.Int(
        title=_(u'Number of main doors'),
        required=False,
        )

    nFloors = schema.Int(
        title=_(u'Number of floors'),
        required=False,
        )

    nHousesFloor = schema.Int(
        title=_(u'Number of houses per floor'),
        required=False,
        )

    nHouses = schema.Int(
        title=_(u'Number of houses in the building (total)'),
        required=False,
        )

    nUndergroundFloors = schema.Int(
        title=_(u'Number of underground floors'),
        required=False,
        )

    nCellars = schema.Int(
        title=_(u'Number of cellars'),
        required=False,
        )

    cellarsInCommunity = schema.Choice(
        title=_(u'Are the cellars included in the community?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    nSwimmingPools = schema.Int(
        title=_(u'Number of swimming pools'),
        required=False,
        )

    garages = schema.Choice(
        title=_(u'Are there garages?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    garagesInCommunity = schema.Choice(
        title=_(u'Are the garages included in the community?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    garageValue = schema.TextLine(
        title=_(u'Value of each parking lot'),
        description=_(u'Should not be included in the total of the continent'),
        required=False,
        )

    nParkingLots = schema.Int(
        title=_(u'Number of parking lots in the garages'),
        required=False,
        )

    nAdditionalHouses = schema.Int(
        title=_(u'Number of unifamiliar or semi-detached houses'),
        required=False,
        )

    m2AddHouse = schema.Int(
        title=_(u'Number of square meters per unifamiliar or semi-detached house'),
        description=_(u"These should be included in the 'Built square meters' field."),
        required=False,
        )

    m2AddHouseTotal = schema.Int(
        title=_(u'Total square meters dedicated to unifamiliar or semi-detached houses'),
        required=False,
        )

    nOffices = schema.Int(
        title=_(u'Number of offices'),
        required=False,
        )

    m2Offices = schema.Int(
        title=_(u'Number of square meters dedicated to offices'),
        description=_(u"This cannot be included in the 'Built square meters' field."),
        required=False,
        )

    housesDestination = schema.Choice(
        title=_(u'Houses destination'),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value='main', title=_(u'Main')),
             SimpleTerm(value='secondary', title=_(u'Secondary'))],
            ),
        required=False,
        )

    electricRepairmentsYear = schema.Int(
        title=_(u'Electric repairments year'),
        description=_(u'Leave blank if not performed'),
        required=False,
        )

    electricRepairmentsType = schema.TextLine(
        title=_(u'Repairment type'),
        required=False,
        )

    drainPipesRepairmentsYear = schema.Int(
        title=_(u'Drain pipes repairments year'),
        description=_(u'Leave blank if not performed'),
        required=False,
        )

    waterConductionRepairmentsYear = schema.Int(
        title=_(u'Water conduction repairments year'),
        description=_(u'Leave blank if not performed'),
        required=False,
        )

    businesses = schema.Choice(
        title=_(u'Are there businesses in the building?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    nBusinesses = schema.Int(
        title=_(u'Number of businesses in the building'),
        required=False,
        )

    businessesInCommunity = schema.Choice(
        title=_(u'Are the businesses included in the community?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    m2Businesses = schema.Int(
        title=_(u'Square meters dedicated to business'),
        required=False,
        )

    businessesDescription = RichText(
        title=_(u'Businesses description'),
        description=_(u'If the businesses are included in the community insurance, enter the number of businesses, square meters and activity description of each one.'),
        required=False,
        )

    nExtinguishers = schema.Int(
        title=_(u'Number of fire extinguishers'),
        required=False,
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
