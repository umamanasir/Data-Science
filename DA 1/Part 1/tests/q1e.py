OK_FORMAT = True
test = {
    "name": "q1e",
    "points": 5,
    "suites": [
        {
            "cases": [ 
                {
                    "code": r"""
                    >>> assert list(shapesData['sum of interior angles']) == [180, 360, 540, 720, 900, 1080, 1260, 1440]
                    >>> assert list(shapesData['name']) == ['Triangle','Square','Pentagon','Hexagon','Heptagon','Octagon','Nonagon','Decagon']
                    >>> assert list(shapesData['area of shape']) == [0.433, 1.000, 1.720, 2.598, 3.634, 4.828, 6.182, 7.694]
                    >>> assert list(shapesData['sides']) == [3,4,5,6,7,8,9,10]
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