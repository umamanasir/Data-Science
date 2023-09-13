OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert q8Ans.values.value_counts()['Nominal'] == 7
                    >>> assert q8Ans.values.value_counts()['Discrete'] == 3
                    >>> assert q8Ans.values.value_counts()['Continous'] == 2
                    >>> assert q8Ans.values.value_counts()['Ordinal'] == 2
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