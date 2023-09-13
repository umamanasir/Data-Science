OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert round(abs(bias_ATE),3) == 0.09
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
