OK_FORMAT = True
test = {
    "name": "q4c",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert len(cheapestBestCameras) == 2
                    >>> assert len(bestCameras) == 110
                    >>> assert 'Ricoh Caplio R7' in cheapestBestCameras
                    >>> assert 'Samsung S830' in cheapestBestCameras
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