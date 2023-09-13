OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert round(abs(conditioned_selection_bias),3) < 0.011
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
