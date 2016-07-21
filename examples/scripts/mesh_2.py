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
import alinea.phenomenal.plant_1
import alinea.phenomenal.misc
import alinea.phenomenal.data_transformation
import alinea.phenomenal.mesh
import alinea.phenomenal.viewer
import alinea.phenomenal.calibration

from alinea.phenomenal.multi_view_reconstruction import (
    reconstruction_3d)

from alinea.phenomenal.plant_1 import (
    plant_1_images_binarize,
    plant_1_calibration_camera_side,
    plant_1_calibration_camera_top)

# ==============================================================================

# # Load images binarize
# images = plant_1_images_binarize()
# calibration_side = plant_1_calibration_camera_side()
# calibration_top = plant_1_calibration_camera_top()
#
# # Select images
# images_projections = list()
# for angle in range(0, 360, 30):
#     img = images[angle]
#     projection = calibration_side.get_projection(angle)
#     images_projections.append((img, projection))
#
# img = images[-1]
# projection = calibration_top.get_projection(0)
# images_projections.append((img, projection))

# ==============================================================================

voxel_size = 1

# ==============================================================================

# # Multi-view reconstruction
# voxel_centers = reconstruction_3d(
#     images_projections, voxel_size=voxel_size, verbose=True)
#
# # Write
# alinea.phenomenal.misc.write_xyz(voxel_centers,
#                                  'voxel_centers_size_' + str(voxel_size))

# Read
voxel_centers = alinea.phenomenal.misc.read_xyz(
    'voxel_centers_size_' + str(voxel_size))

# Viewing
alinea.phenomenal.viewer.show_points_3d(voxel_centers,
                                        scale_factor=voxel_size,
                                        color=(0.1, 0.8, 0.1),
                                        figure_name=str(voxel_size))

# ==============================================================================

vertices, faces = alinea.phenomenal.mesh.meshing(
    voxel_centers, voxel_size,
    reduction=0.95, smoothing_iteration=0, verbose=True)

# ==============================================================================

alinea.phenomenal.viewer.show_mesh(vertices, faces)