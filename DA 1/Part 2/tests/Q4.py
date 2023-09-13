OK_FORMAT = True
test = {
    "name": "Q4",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert 'exercise induced angina' in heartDf.columns
                    >>> assert 'number of major vessels' in heartDf.columns
                    >>> assert 'chest pain type' in heartDf.columns
                    >>> assert 'fasting blood sugar' in heartDf.columns
                    >>> assert 'resting blood pressure' in heartDf.columns
                    >>> assert 'old peak' in heartDf.columns
                    >>> assert 'cholestrol levels' in heartDf.columns
                    >>> assert 'resting electrocardiographic' in heartDf.columns
                    >>> assert 'maximum heart rate' in heartDf.columns
                    >>> assert 'thall' not in heartDf.columns
                    >>> assert 'slp' not in heartDf.columns
                    >>> assert 'O2 saturation' in o2SaturationDf.columns
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