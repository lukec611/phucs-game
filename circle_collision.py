import math
'''
    c1x: float - x position of circle 1
    c1y: float - y position of circle 1
    c1r: float - radius of circle 1
    c2x: float - x position of circle 2
    c2y: float - y position of circle 2
    c2r: float - radius of circle 2
    return: Boolean - if the circles touch eachother
'''
def circles_collide(c1x, c1y, c1r, c2x, c2y, c2r):
    # first get the distance between the circle 1
    # and circle 2
    distance = math.sqrt(
        math.pow(c1x - c2x, 2.0) +
        math.pow(c1y - c2y, 2.0)
    )
    # if the distance is less than the two radius' added together
    # the circle's must be touching
    return distance < c1r + c2r


def tests():
    tests = [
        { "c1x": 0, "c1y": 0, "c1r": 5, "c2x": 0, "c2y": 0, "c2r": 5, "collide": True },
        { "c1x": 0, "c1y": 0, "c1r": 5, "c2x": 10, "c2y": 0, "c2r": 5, "collide": False },
        { "c1x": 50, "c1y": 50, "c1r": 50, "c2x": 99, "c2y": 99, "c2r": 20, "collide": True },
        { "c1x": 50, "c1y": 50, "c1r": 50, "c2x": 199, "c2y": 99, "c2r": 5, "collide": False },
    ]
    for test in tests:
        testResult = circles_collide(test["c1x"], test["c1y"], test["c1r"], test["c2x"], test["c2y"], test["c2r"])
        assert testResult == test["collide"]
        print 'Yay works'

tests()