OK_FORMAT = True
test = {
    "name": "Q7",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert 'Date_added' not in netflixDataset.columns
                    >>> assert 'Added_date' in netflixDataset.columns
                    >>> assert 'Added_year' in netflixDataset.columns
                    >>> assert len(netflixDataset['Added_date']) == 5332
                    >>> assert len(netflixDataset['Added_year']) == 5332
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