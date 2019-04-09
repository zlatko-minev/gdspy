######################################################################
#                                                                    #
#  Copyright 2009-2019 Lucas Heitzmann Gabrielli.                    #
#  This file is part of gdspy, distributed under the terms of the    #
#  Boost Software License - Version 1.0.  See the accompanying       #
#  LICENSE file or <http://www.boost.org/LICENSE_1_0.txt>            #
#                                                                    #
######################################################################

import numpy
import pytest
import gdspy


@pytest.fixture
def target():
    return gdspy.GdsLibrary(infile='tests/test.gds').cell_dict

def assertsame(c1, c2):
    d1 = c1.get_polygons(by_spec=True)
    d2 = c2.get_polygons(by_spec=True)
    for key in d1:
        assert key in d2
        result = gdspy.boolean(d1[key], d2[key], 'xor', precision=1e-6)
        assert result is None

def test_polygonset(target):
    cell = gdspy.Cell('X', True).add(gdspy.PolygonSet([
        [(1, 1), (1, 2), (5, 3)],
        [(0, 0.5), (0, 3), (-4, 1), (0, -1), (4, 0.5)],
    ], 8, 9))
    assertsame(cell, target['polygonset'])
