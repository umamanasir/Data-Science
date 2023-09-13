OK_FORMAT = True
test = {
    "name": "Q4",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert netflixDataset.index.name == 'Show ID' 
                    >>> assert list(netflixDataset.index) == [i for i in range(1,5333)]
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