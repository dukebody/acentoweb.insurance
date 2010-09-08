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
                          'holderTown',
                          'holderProvince',
                          'holderPhone']
                  )

    title = schema.TextLine(
        title=_(u"Holder name"),
        )

    holderId = schema.TextLine(
        title=_(u"Holder NIF/CIF"),
        required=False,
        )

    holderTown = schema.TextLine(
        title=_(u"Holder town"),
        required=False,
        )

    holderProvince = schema.TextLine(
        title=_(u"Holder province"),
        required=False,
        )

    holderPhone = schema.TextLine(
        title=_(u"Holder phone number"),
        required=False,
        )

    # insured data (blank if same as holder)
    form.fieldset('insuredData',
                  label=_(u"Insured"),
                  fields=['insuredName',
                          'insuredId',
                          'insuredTown',
                          'insuredProvince',
                          'insuredPhone',
                          'insuredContactPerson',
                          'insuredContactPersonPhone',]
                  )

    insuredName = schema.TextLine(
        title=_(u"Insured name"),
        required=False,
        )

    insuredId = schema.TextLine(
        title=_(u"Insured NIF/CIF"),
        required=False,
        )

    insuredTown = schema.TextLine(
        title=_(u"Insured town"),
        required=False,
        )

    insuredProvince = schema.TextLine(
        title=_(u"Insured province"),
        required=False,
        )

    insuredPhone = schema.TextLine(
        title=_(u"Insured phone number"),
        required=False,
        )

    insuredContactPerson = schema.TextLine(
        title=_(u"Insured contact person"),
        required=False,
        )

    insuredContactPersonPhone = schema.TextLine(
        title=_(u"Insured contact person phone number"),
        required=False,
        )

    # building data

    form.fieldset('buildingData',
                  label=_(u"Building"),
                  fields=['buildingYear',
                          'nMainDoors',
                          'otherAccesses',
                          'nSquareMeters',
                          'nFloors',
                          'nHousesFloor',
                          'nHouses',
                          'housesInBottomFloor',
                          'nSquareMetersHouse',
                          'nUndergroundFloors',
                          'nCellars',
                          'swimmingPool',
                          'garages',
                          'garagesInCommunity',
                          'garageValue',
                          'garageInCommunityHousesInsurance',
                          'nParkingLots',
                          'nAdditionalHouses',
                          'nSquareMetersAddHouse',
                          'nOffices',
                          'nSquareMetersOffices',
                          'gardens',
                          'housesDestination',
                          'electricRepairmentsYear',
                          'drainPipesRepairmentsYear',
                          'businesses',
                          'nBusinesses',
                          'businessesInCommunity',
                          'existingInsurance',
                          'existingInsuranceExpiration',
                          'existingInsuranceCompany',
                          'businessesDescription',
                          ]
                  )

    buildingYear = schema.Int(
        title=_(u'Year the building was built'),
        required=False,
        )

    nMainDoors = schema.Int(
        title=_(u'Number of main doors'),
        required=False,
        )

    otherAccesses = schema.TextLine(
        title=_(u'Other accesses'),
        required=False,
        )

    nSquareMeters = schema.Int(
        title=_(u'Number of square meters built'),
        required=False,
        )

    nFloors = schema.Int(
        title=_(u'Number of floors high'),
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

    housesInBottomFloor = schema.Choice(
        title=_(u'Are there any houses in the bottom floor?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    nSquareMetersHouse = schema.Int(
        title=_(u'Number of square meters per house'),
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

    swimmingPool = schema.Choice(
        title=_(u'Are there swimming pools?'),
        vocabulary=YesNoVocabulary,
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

    garageInCommunityHousesInsurance = schema.Choice(
        title=_(u'Are the garages included in the community houses insurance?'),
        vocabulary=YesNoVocabulary,
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

    nSquareMetersAddHouse = schema.Int(
        title=_(u'Number of square meters per unifamiliar or semi-detached house'),
        description=_(u"These should be included in the 'Built square meters' field."),
        required=False,
        )

    nOffices = schema.Int(
        title=_(u'Number of offices'),
        required=False,
        )

    nSquareMetersOffices = schema.Int(
        title=_(u'Number of total square meters dedicated to offices'),
        description=_(u"This cannot be included in the 'Built square meters' field."),
        required=False,
        )

    gardens = schema.Choice(
        title=_(u'Does the community have shared gardens?'),
        vocabulary=YesNoVocabulary,
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

    drainPipesRepairmentsYear = schema.Int(
        title=_(u'Drain Pipes repairments year'),
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


    existingInsurance = schema.Choice(
        title=_(u'Does the community currently have an insurance?'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    existingInsuranceExpiration = schema.Date(
        title=_(u'Existing insurance expiry date'),
        required=False,
        )

    existingInsuranceCompany = schema.TextLine(
        title=_(u'Current company'),
        required=False,
        )

    businessesDescription = RichText(
        title=_(u'Businesses description'),
        description=_(u'If the businesses are included in the community, enter the number of businesses, square meters and activity description of each one.'),
        required=False,
        )

    # fire protections
    form.fieldset('fireProtections',
                  label=_(u"Fire protections"),
                  fields=['nExtinguishers',
                          'extinguishersMaintenance',
                          'extinguishersCompany',

                          'nDetectors',
                          'detectorsMaintenance',
                          'detectorsCompany',

                          'nWaterPumps',
                          'waterPumpsMaintenance',
                          'waterPumpsCompany',

                          'nAlarms',
                          'alarmsMaintenance',
                          'alarmsCompany',

                          'nWaterDispensers',
                          'waterDispensersMaintenance',
                          'waterDispensersCompany',

                          'firemenDistance',
                          ]
                  )


    nExtinguishers = schema.Int(
        title=_(u'Number of fire extinguishers'),
        required=False,
        )

    extinguishersMaintenance = schema.Choice(
        title=_(u'Extinguishers maintenance'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    extinguishersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        required=False,
        )

    nDetectors = schema.Int(
        title=_(u'Number of fire detectors'),
        required=False,
        )

    detectorsMaintenance = schema.Choice(
        title=_(u'Detectors maintenance'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    detectorsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        required=False,
        )

    nWaterPumps = schema.Int(
        title=_(u'Number of fire water pumps'),
        required=False,
        )

    waterPumpsMaintenance = schema.Choice(
        title=_(u'Water pumps maintenance'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    waterPumpsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        required=False,
        )

    nAlarms = schema.Int(
        title=_(u'Number of fire alarms'),
        required=False,
        )

    alarmsMaintenance = schema.Choice(
        title=_(u'Alarms maintenance'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    alarmsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        required=False,
        )

    nWaterDispensers = schema.Int(
        title=_(u'Number of water dispensers'),
        required=False,
        )

    waterDispensersMaintenance = schema.Choice(
        title=_(u'Water dispensers maintenance'),
        vocabulary=YesNoVocabulary,
        required=False,
        )

    waterDispensersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        required=False,
        )

    firemenDistance = schema.Choice(
        title=_(u'Firemen distance'),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value='more15km', title=_(u'More than 15 km')),
             SimpleTerm(value='less15km', title=_(u'Less than 15 km'))],
            ),
        required=False,
        )

    # XXX: ommiting robbery!!!

    # insurance values
    form.fieldset('valuesData',
                  label=_(u"Values"),
                  fields=['continentTotal',
                          'continentHighHouses',
                          'continentAddedHouses',
                          'continentGarages',
                          'continentCellars',

                          'containedTotal',
                          'containedFurniture',
                          'containedOthers',
                          ]
                  )

    continentTotal = schema.TextLine(
        title=_(u'Total continent'),
        required=False,
        )

    continentHighHouses = schema.TextLine(
        title=_(u'High houses continent'),
        required=False,
        )

    continentAddedHouses = schema.TextLine(
        title=_(u'Unifamiliar or semi-detached houses continent'),
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

    containedTotal = schema.TextLine(
        title=_(u'Total contained'),
        required=False,
        )

    containedFurniture = schema.TextLine(
        title=_(u'Furniture contained'),
        required=False,
        )

    containedOthers = schema.TextLine(
        title=_(u'Others contained'),
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

    # notes
    form.fieldset('additionalInfo',
                  label=_(u"Additional info"),
                  fields=['notes',]
                  )

    notes = RichText(
            title=_(u"Notes"),
            required=False
        )
