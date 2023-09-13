OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert len(df.columns) == 16
                    >>> assert sorted(list(df.columns)) ==['accuracy','agegroup','bjp_oppose','bjp_support','college','days_whatsapp','hindu','low_caste','male','muslim','nationalistic','political_knowledge','treatment','uncongenial','vote_intention','whatsapp']
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
