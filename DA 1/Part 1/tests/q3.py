OK_FORMAT = True
test = {
    "name": "q3",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert 'Release date' not in camerasFiltered.columns
                    >>> assert camerasFiltered.shape == (875, 11)
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