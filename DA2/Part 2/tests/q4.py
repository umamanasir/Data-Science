OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> for col in adultsData.columns:
                    ...     assert '-' not in col
                    >>> assert 'years of education' in adultsData.columns
                    >>> assert 'relationship status' in adultsData.columns
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