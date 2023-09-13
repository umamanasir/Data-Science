OK_FORMAT = True
test = {
    "name": "q2",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert 'Model' not in camerasData.columns
                    >>> assert camerasData.shape == (1038, 12)
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