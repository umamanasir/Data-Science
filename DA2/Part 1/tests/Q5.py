OK_FORMAT = True
test = {
    "name": "Q5",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert 'Type' in netflixDataset.columns 
                    >>> assert 'Title' in netflixDataset.columns
                    >>> assert 'Director' in netflixDataset.columns
                    >>> assert 'Cast' in netflixDataset.columns
                    >>> assert 'Country' in netflixDataset.columns
                    >>> assert 'Date_added' in netflixDataset.columns
                    >>> assert 'Release_year' in netflixDataset.columns
                    >>> assert 'Rating' in netflixDataset.columns
                    >>> assert 'Listed_in' in netflixDataset.columns
                    >>> assert 'Duration' in netflixDataset.columns
                    >>> assert 'Description' in netflixDataset.columns
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