OK_FORMAT = True
test = {
    "name": "",
    "points": 1,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> a = adultsData['workclass'].value_counts()
                    >>> assert a['Private'] == 36705
                    >>> assert a['Self emp not inc'] == 3862
                    >>> assert a['Local gov'] == 3136
                    >>> assert a['State gov'] == 1981
                    >>> assert a['Self emp inc'] == 1695
                    >>> assert a['Federal gov'] == 1432
                    >>> assert a['Without pay'] == 21
                    >>> assert a['Never worked'] == 10
                    >>> 
                    >>> b = adultsData['occupation'].value_counts()
                    >>> assert b['Craft repair'] == 7187
                    >>> assert b['Prof specialty'] == 6534
                    >>> assert b['Adm clerical'] == 6525
                    >>> assert b['Exec managerial'] == 6086
                    >>> assert b['Sales'] == 5504
                    >>> assert b['Other service'] == 5381
                    >>> assert b['Machine op inspct'] == 3022
                    >>> assert b['Transport moving'] == 2355
                    >>> assert b['Handlers cleaners'] == 2072
                    >>> assert b['Farming fishing'] == 1490
                    >>> assert b['Tech support'] == 1446
                    >>> assert b['Protective serv'] == 983
                    >>> assert b['Priv house serv'] == 242
                    >>> assert b['Armed Forces'] == 15
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