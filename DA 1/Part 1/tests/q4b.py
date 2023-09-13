OK_FORMAT = True
test = {
    "name": "q4b",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert camerasScores.shape == (875,2)
                    >>> assert camerasScores.index.tolist() == camerasFiltered.index.tolist()
                    >>> assert 'price' in camerasScores.columns
                    >>> assert 'score' in camerasScores.columns
                    >>> assert camerasScores['price'].tolist() == camerasFiltered['Price'].tolist()
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