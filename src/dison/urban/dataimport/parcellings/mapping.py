# -*- coding: utf-8 -*-

from dison.urban.dataimport.parcellings.mappers import ParcellingFactory
from dison.urban.dataimport.parcellings.mappers import TitleMapper

from imio.urban.dataimport.access.mapper import AccessSimpleMapper as SimpleMapper


OBJECTS_NESTING = [
    (
        'PARCELLING', [],
    ),
]

FIELDS_MAPPINGS = {
    'PARCELLING':
    {
        'factory': [ParcellingFactory],

        'mappers': {
            SimpleMapper: (
                {
                    'from': 'Cle_Lot',
                    'to': 'id',
                },
                {
                    'from': 'Autorise',
                    'to': 'authorizationDate',
                },
                {
                    'from': 'Lot',
                    'to': 'changesDescription',
                },
            ),

            TitleMapper: {
                'from': 'Lotis',
                'to': ('label', 'subdividerName'),
            },
        },
    },
}
