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
        )

    holderTown = schema.TextLine(
        title=_(u"Holder town"),
        )

    holderProvince = schema.TextLine(
        title=_(u"Holder province"),
        )

    holderPhone = schema.TextLine(
        title=_(u"Holder phone number"),
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
        )

    insuredId = schema.TextLine(
        title=_(u"Insured NIF/CIF"),
        )

    insuredTown = schema.TextLine(
        title=_(u"Insured town"),
        )

    insuredProvince = schema.TextLine(
        title=_(u"Insured province"),
        )

    insuredPhone = schema.TextLine(
        title=_(u"Insured phone number"),
        )

    insuredContactPerson = schema.TextLine(
        title=_(u"Insured contact person"),
        )

    insuredContactPersonPhone = schema.TextLine(
        title=_(u"Insured contact person phone number"),
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
        )

    nMainDoors = schema.Int(
        title=_(u'Number of main doors'),
        )

    otherAccesses = schema.TextLine(
        title=_(u'Other accesses'),
        )

    nSquareMeters = schema.Int(
        title=_(u'Number of square meters built'),
        )

    nFloors = schema.Int(
        title=_(u'Number of floors high')
        )

    nHousesFloor = schema.Int(
        title=_(u'Number of houses per floor'),
        )

    nHouses = schema.Int(
        title=_(u'Number of houses in the building (total)'),
        )

    housesInBottomFloor = schema.Choice(
        title=_(u'Are there any houses in the bottom floor?'),
        vocabulary=YesNoVocabulary,
        )

    nSquareMetersHouse = schema.Int(
        title=_(u'Number of square meters per house'),
        )

    nUndergroundFloors = schema.Int(
        title=_(u'Number of underground floors'),
        )

    nCellars = schema.Int(
        title=_(u'Number of cellars'),
        )

    swimmingPool = schema.Choice(
        title=_(u'Are there swimming pools?'),
        vocabulary=YesNoVocabulary,
        )

    garages = schema.Choice(
        title=_(u'Are there garages?'),
        vocabulary=YesNoVocabulary,
        )

    garagesInCommunity = schema.Choice(
        title=_(u'Are the garages included in the community?'),
        vocabulary=YesNoVocabulary
        )

    garageValue = schema.TextLine(
        title=_(u'Value of each parking lot'),
        description=_(u'Should not be included in the total of the continent'),
        )

    garageInCommunityHousesInsurance = schema.Choice(
        title=_(u'Are the garages included in the community houses insurance?'),
        vocabulary=YesNoVocabulary,
        )

    nParkingLots = schema.Int(
        title=_(u'Number of parking lots in the garages'),
        )

    nAdditionalHouses = schema.Int(
        title=_(u'Number of unifamiliar or semi-detached houses'),
        )

    nSquareMetersAddHouse = schema.Int(
        title=_(u'Number of square meters per unifamiliar or semi-detached house'),
        description=_(u"These should be included in the 'Built square meters' field."),
        )

    nOffices = schema.Int(
        title=_(u'Number of offices'),
        )

    nSquareMetersOffices = schema.Int(
        title=_(u'Number of total square meters dedicated to offices'),
        description=_(u"This cannot be included in the 'Built square meters' field."),
        )

    gardens = schema.Choice(
        title=_(u'Does the community have shared gardens?'),
        vocabulary=YesNoVocabulary,
        )

    housesDestination = schema.Choice(
        title=_(u'Houses destination'),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value='main', title=_(u'Main')),
             SimpleTerm(value='secondary', title=_(u'Secondary'))],
            )
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
        )

    nBusinesses = schema.Int(
        title=_(u'Number of businesses in the building'),
        required=False,
        )

    businessesInCommunity = schema.Choice(
        title=_(u'Are the businesses included in the community?'),
        vocabulary=YesNoVocabulary,
        )


    existingInsurance = schema.Choice(
        title=_(u'Does the community currently have an insurance?'),
        vocabulary=YesNoVocabulary,
        )

    existingInsuranceExpiration = schema.Date(
        title=_(u'Existing insurance expiry date'),
        required=False,
        )

    existingInsuranceCompany = schema.TextLine(
        title=_(u'Current company'),
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
        )

    extinguishersMaintenance = schema.Choice(
        title=_(u'Extinguishers maintenance'),
        vocabulary=YesNoVocabulary,
        )

    extinguishersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nDetectors = schema.Int(
        title=_(u'Number of fire detectors'),
        )

    detectorsMaintenance = schema.Choice(
        title=_(u'Detectors maintenance'),
        vocabulary=YesNoVocabulary,
        )

    detectorsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nWaterPumps = schema.Int(
        title=_(u'Number of fire water pumps'),
        )

    waterPumpsMaintenance = schema.Choice(
        title=_(u'Water pumps maintenance'),
        vocabulary=YesNoVocabulary,
        )

    waterPumpsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nAlarms = schema.Int(
        title=_(u'Number of fire alarms'),
        )

    alarmsMaintenance = schema.Choice(
        title=_(u'Alarms maintenance'),
        vocabulary=YesNoVocabulary,
        )

    alarmsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nWaterDispensers = schema.Int(
        title=_(u'Number of water dispensers'),
        )

    waterDispensersMaintenance = schema.Choice(
        title=_(u'Water dispensers maintenance'),
        vocabulary=YesNoVocabulary,
        )

    waterDispensersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    firemenDistance = schema.Choice(
        title=_(u'Firemen distance'),
        vocabulary=SimpleVocabulary(
            [SimpleTerm(value='more15km', title=_(u'More than 15 km')),
             SimpleTerm(value='less15km', title=_(u'Less than 15 km'))],
            ),
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
        )

    continentHighHouses = schema.TextLine(
        title=_(u'High houses continent'),
        )

    continentAddedHouses = schema.TextLine(
        title=_(u'Unifamiliar or semi-detached houses continent'),
        )

    continentGarages = schema.TextLine(
        title=_(u'Garages continent'),
        )

    continentCellars = schema.TextLine(
        title=_(u'Cellars continent'),
        )

    containedTotal = schema.TextLine(
        title=_(u'Total contained'),
        )

    containedFurniture = schema.TextLine(
        title=_(u'Furniture contained'),
        )

    containedOthers = schema.TextLine(
        title=_(u'Others contained'),
        )

    # agent data
    form.fieldset('agentData',
                  label=_(u"Agent"),
                  fields=['agentName',
                          'agentCode',]
                  )

    agentName = schema.TextLine(
        title=_(u'Agent name'),
        )

    agentCode = schema.TextLine(
        title=_(u'Agent code'),
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
