OK_FORMAT = True
test = {
    "name": "q5b",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert cameraComparison.shape == (875,2)
                    >>> assert cameraComparison.index.tolist() == camerasFiltered.index.tolist()
                    >>> assert 'better' in cameraComparison.columns
                    >>> assert 'price' in cameraComparison.columns
                    >>> assert cameraComparison['price'].tolist() == camerasFiltered['Price'].tolist()
                    >>> assert cameraComparison['better'].value_counts()[False] == 846
                    >>> 
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