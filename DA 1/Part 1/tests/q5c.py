OK_FORMAT = True
test = {
    "name": "q5c",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert len(cheapestBetterCameras) == 2
                    >>> assert 'Kodak Z1275' in cheapestBetterCameras
                    >>> assert 'Olympus C-5500 Sport Zoom' in cheapestBetterCameras
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
            ],
            "scored": True,
            "setup": "",
            "teardown": "",
            "type": "doctest"
        }
    ]
}