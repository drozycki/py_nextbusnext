TEST_AGENCY_ID = "sfmta-cis"
TEST_ROUTE_ID = "F"
TEST_STOP_ID = "5184"
TEST_DIRECTION_ID = "F_0_var0"

MOCK_AGENCY_LIST_RESPONSE = [
    {
        "id": "sfmta-cis",
        "name": "San Francisco Muni CIS",
        "shortName": "SF Muni CIS",
        "region": "California-Northern",
        "website": "http://www.sfmta.com",
        "logo": "/logos/muniLogoSmall.gif",
        "nxbs2RedirectUrl": "",
    },
]

MOCK_ROUTE_LIST_RESPONSE = [
    {
        "id": "F",
        "rev": 1057,
        "title": "F Market & Wharves",
        "description": "7am-10pm daily",
        "color": "b49a36",
        "textColor": "000000",
        "hidden": False,
        "timestamp": "2024-06-23T03:06:58Z",
    },
]

MOCK_ROUTE_DETAILS_RESPONSE = {
    "id": "F",
    "rev": 1057,
    "title": "F Market & Wharves",
    "description": "7am-10pm daily",
    "color": "b49a36",
    "textColor": "000000",
    "hidden": False,
    "boundingBox": {
        "latMin": 37.7625799,
        "latMax": 37.8085899,
        "lonMin": -122.43498,
        "lonMax": -122.39344,
    },
    "stops": [
        {
            "id": "5184",
            "lat": 37.8071299,
            "lon": -122.41732,
            "name": "Jones St & Beach St",
            "code": "15184",
            "hidden": False,
            "showDestinationSelector": True,
            "directions": ["F_0_var1", "F_0_var0"],
        },
    ],
    "directions": [
        {
            "id": "F_0_var1",
            "shortName": "Castro + Market",
            "name": "Castro + Market",
            "useForUi": False,
            "stops": [
                "5184",
            ],
        },
        {
            "id": "F_0_var0",
            "shortName": "Castro",
            "name": "Castro",
            "useForUi": True,
            "stops": [
                "5184",
            ],
        },
        {
            "id": "F_1_var0",
            "shortName": "Fisherman`s Wharf",
            "name": "Fisherman`s Wharf",
            "useForUi": True,
            "stops": [
                "5184_ar",
            ],
        },
    ],
    "paths": [
        {
            "id": "F_1_var0_16_4530_5184_ar",
            "points": [
                {"lat": 37.80835, "lon": -122.41029},
                {"lat": 37.80829, "lon": -122.41032},
                {"lat": 37.80833, "lon": -122.4105},
                {"lat": 37.80862, "lon": -122.4124},
                {"lat": 37.80862, "lon": -122.41253},
                {"lat": 37.80859, "lon": -122.41336},
                {"lat": 37.8085, "lon": -122.41337},
                {"lat": 37.80842, "lon": -122.41417},
                {"lat": 37.80832, "lon": -122.41551},
                {"lat": 37.80801, "lon": -122.41745},
                {"lat": 37.80724, "lon": -122.41732},
                {"lat": 37.80713, "lon": -122.41732},
            ],
        },
    ],
    "timestamp": "2024-06-23T03:06:58Z",
}

MOCK_PREDICTIONS_RESPONSE = [
    {
        "serverTimestamp": 1720034290432,
        "nxbs2RedirectUrl": "",
        "route": {
            "id": "F",
            "title": "F Market & Wharves",
            "description": "7am-10pm daily",
            "color": "b49a36",
            "textColor": "000000",
            "hidden": False,
        },
        "stop": {
            "id": "5184",
            "lat": 37.8071299,
            "lon": -122.41732,
            "name": "Jones St & Beach St",
            "code": "15184",
            "hidden": False,
            "showDestinationSelector": True,
            "route": "F",
        },
        "values": [
            {
                "timestamp": 1720034640000,
                "minutes": 5,
                "affectedByLayover": True,
                "isDeparture": True,
                "occupancyStatus": 0,
                "occupancyDescription": "Empty",
                "vehiclesInConsist": 1,
                "linkedVehicleIds": "1080",
                "vehicleId": "1080",
                "vehicleType": None,
                "direction": {
                    "id": "F_0_var0",
                    "name": "Castro",
                    "destinationName": "Castro",
                },
                "tripId": "11618999_M31",
                "delay": 0,
                "predUsingNavigationTm": False,
                "departure": True,
            },
            {
                "timestamp": 1720035360000,
                "minutes": 17,
                "affectedByLayover": True,
                "isDeparture": True,
                "occupancyStatus": -1,
                "occupancyDescription": "Unknown",
                "vehiclesInConsist": 1,
                "linkedVehicleIds": "1070",
                "vehicleId": "1070",
                "vehicleType": None,
                "direction": {
                    "id": "F_0_var0",
                    "name": "Castro",
                    "destinationName": "Castro",
                },
                "tripId": "11619000_M31",
                "delay": 0,
                "predUsingNavigationTm": False,
                "departure": True,
            },
            {
                "timestamp": 1720036080000,
                "minutes": 29,
                "affectedByLayover": True,
                "isDeparture": True,
                "occupancyStatus": -1,
                "occupancyDescription": "Unknown",
                "vehiclesInConsist": 1,
                "linkedVehicleIds": "1079",
                "vehicleId": "1079",
                "vehicleType": None,
                "direction": {
                    "id": "F_0_var0",
                    "name": "Castro",
                    "destinationName": "Castro",
                },
                "tripId": "11619001_M31",
                "delay": 0,
                "predUsingNavigationTm": False,
                "departure": True,
            },
        ],
    }
]
