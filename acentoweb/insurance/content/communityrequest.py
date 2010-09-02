from zope import schema

from plone.directives import form

from plone.app.textfield import RichText

from acentoweb.insurance import _

class ICommunityRequest(form.Schema):
    """A conference presenter. Presenters can be added anywhere.
    """

    # holder data
    form.fieldset('holderData',
                  label=_(u"Holder data"),
                  fields=['holderName',
                          'holderId',
                          'holderTown',
                          'holderProvince',
                          'holderPhone']
                  )

    holderName = schema.TextLine(
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
                  label=_(u"Insured data"),
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
                  label=_(u"Building data"),
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

    housesInBottomFloor = schema.Bool(
        title=_(u'Are there any houses in the bottom floor?'),
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

    swimmingPool = schema.Bool(
        title=_(u'Are there swimming pools?'),
        )

    garages = schema.Bool(
        title=_(u'Are there garages?'),
        )

    garagesInCommunity = schema.Bool(
        title=_(u'Are the garages included in the community?'),
        )

    garageValue = schema.TextLine(
        title=_(u'Value of each parking lot'),
        description=_(u'Should not be included in the total of the continent'),
        )

    garageInCommunityHousesInsurance = schema.Bool(
        title=_(u'Are the garages included in the community houses insurance?'),
        )

    nParkingLots = schema.Int(
        title=_(u'Number of parking lots in the garages'),
        )

    nAdditionalHouses = schema.Int(
        title=_(u'Number of unifamiliar or semi-detached houses'),
        )

    nSquareMetersAddHouse = schema.Int(
        title=_(u'Number of square meters per unifamiliar or semi-detached house'),
        description=_(u'These should be included in the "Built square meters" field.'),
        )

    nOffices = schema.Int(
        title=_(u'Number of offices'),
        )

    nSquareMetersOffices = schema.Int(
        title=_(u'Number of total square meters dedicated to offices'),
        description=_(u'This cannot be included in the "Built square meters" field.'),
        )

    gardens = schema.Bool(
        title=_(u'Does the community have shared gardens?'),
        )

    housesDestination = schema.Choice(
        title=_(u'Houses destination'),
        values=([_(u'Main'), _(u'Secondary')]),
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

    businesses = schema.Bool(
        title=_(u'Are there businesses in the building?'),
        )

    nBusinesses = schema.Int(
        title=_(u'Number of businesses in the building'),
        required=False,
        )

    businessesInCommunity = schema.Bool(
        title=_(u'Are the businesses included in the community?')
        )


    existingInsurance = schema.Bool(
        title=_(u'Does the community currently have an insurance?'),
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

    extinguishersMaintenance = schema.Bool(
        title=_(u'Extinguishers maintenance'),
        )

    extinguishersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nDetectors = schema.Int(
        title=_(u'Number of fire detectors'),
        )

    detectorsMaintenance = schema.Bool(
        title=_(u'Detectors maintenance'),
        )

    detectorsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nWaterPumps = schema.Int(
        title=_(u'Number of fire water pumps'),
        )

    waterPumpsMaintenance = schema.Bool(
        title=_(u'Water pumps maintenance'),
        )

    waterPumpsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nAlarms = schema.Int(
        title=_(u'Number of fire alarms'),
        )

    alarmsMaintenance = schema.Bool(
        title=_(u'Alarms maintenance'),
        )

    alarmsCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    nWaterDispensers = schema.Int(
        title=_(u'Number of water dispensers'),
        )

    waterDispensersMaintenance = schema.Bool(
        title=_(u'Water dispensers maintenance'),
        )

    waterDispensersCompany = schema.TextLine(
        title=_(u'Maintenance company'),
        )

    firemenDistance = schema.Choice(
        title=_(u'Firemen distance'),
        values=[_(u'More than 15 km'), _(u'Less than 15 km')],
        )

    # XXX: ommiting robbery!!!

    # insurance values
    form.fieldset('valuesData',
                  label=_(u"Values data"),
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
                  label=_(u"Agent data"),
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
