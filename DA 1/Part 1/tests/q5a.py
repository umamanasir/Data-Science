OK_FORMAT = True
test = {
    "name": "q5a",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert compare(camerasFiltered.loc['Toshiba PDR-M65']) == False
                    >>> assert compare(camerasFiltered.loc['Canon PowerShot SD950 IS']) == True
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