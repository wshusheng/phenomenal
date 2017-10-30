# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
"""
=========================
Multi-View Reconstruction
=========================

.. currentmodule:: alinea.phenomenal.multi_view_reconstruction


Multi-View Reconstruction
=========================

.. automodule:: alinea.phenomenal.multi_view_reconstruction.multi_view_reconstruction
.. currentmodule:: alinea.phenomenal.multi_view_reconstruction

.. autosummary::
   :toctree: generated/

    get_bounding_box_voxel_projected
    get_voxel_corners
    split_voxel_centers_in_eight
    split_voxel_centers_in_four
    voxel_is_visible_in_image
    kept_visible_voxel
    worker_split_voxel_centers_in_eight
     mp_split_voxel_centers_in_eight
    reconstruction_3d
    project_voxel_centers_on_image
    error_reconstruction
    error_reconstruction_lost
    error_reconstruction_precision
    volume

Formats
=======

.. automodule:: alinea.phenomenal.multi_view_reconstruction.formats
.. currentmodule:: alinea.phenomenal.multi_view_reconstruction

.. autosummary::
   :toctree: generated/

    save_matrix_to_stack_image
    write_xyz
    read_xyz
    write_to_csv
    read_from_csv

Routines
========

.. automodule:: alinea.phenomenal.multi_view_reconstruction.routines
.. currentmodule:: alinea.phenomenal.multi_view_reconstruction

.. autosummary::
   :toctree: generated/

    bounding_box
    remove_internal
    find_position_base_plant
    labeling_connected_component
    biggest_connected_component
    image_3d_to_voxel_centers
    voxel_centers_to_image_3d
"""
# ==============================================================================

from __future__ import division, print_function, absolute_import

from .multi_view_reconstruction import *
from .multi_view_reconstruction_without_loss import *
from .multi_view_reconstruction_octree import *
from .routines import *

# ==============================================================================

__all__ = [s for s in dir() if not s.startswith('_')]