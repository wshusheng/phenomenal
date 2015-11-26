# -*- python -*-
#
#       test_multi_view_reconstruction.py :
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       File author(s): Simon Artzet <simon.artzet@gmail.com>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
#       ========================================================================

#       ========================================================================
#       External Import
import collections

#       ========================================================================
#       Local Import
import alinea.phenomenal.multi_view_reconstruction

#       ========================================================================
#       Code


def test_oct_split():

    point_3d = (0.0, 0.0, 0.0)
    radius = 8

    points_3d = alinea.phenomenal.multi_view_reconstruction.corners_point_3d(
        point_3d, radius / 2)

    assert len(points_3d) == 8

    assert points_3d[0] == (-4., -4., -4.)
    assert points_3d[1] == (4., -4., -4.)
    assert points_3d[2] == (-4., 4., -4.)
    assert points_3d[3] == (-4., -4., 4.)
    assert points_3d[4] == (4., 4., -4.)
    assert points_3d[5] == (4., -4., 4.)
    assert points_3d[6] == (-4., 4., 4.)
    assert points_3d[7] == (4., 4., 4.)


def test_split_cubes():

    point_3d = (0.0, 0.0, 0.0)
    radius = 8

    points_3d = collections.deque()
    points_3d.append(point_3d)

    l = alinea.phenomenal.multi_view_reconstruction.split_points_3d(
        points_3d, radius)

    assert len(l) == 8

    assert l[0] == (-4., -4., -4.)
    assert l[1] == (4., -4., -4.)
    assert l[2] == (-4., 4., -4.)
    assert l[3] == (-4., -4., 4.)
    assert l[4] == (4., 4., -4.)
    assert l[5] == (4., -4., 4.)
    assert l[6] == (-4., 4., 4.)
    assert l[7] == (4., 4., 4.)

#       ========================================================================
#       LOCAL TEST

if __name__ == "__main__":
    test_oct_split()
    test_split_cubes()