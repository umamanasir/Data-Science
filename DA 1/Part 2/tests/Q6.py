OK_FORMAT = True
test = {
    "name": "Q6",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert len(belowForty) == 16
                    >>> assert len(ageBtwRange1) == 72
                    >>> assert len(ageBtwRange2) == 125
                    >>> assert len(ageBtwRange3) == 80
                    >>> assert len(aboveSeventy) == 10
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