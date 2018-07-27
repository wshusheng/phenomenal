# -*- python -*-
#
#       Copyright INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
# ==============================================================================
from __future__ import division, print_function, absolute_import

import vtk
import os
import json
import numpy

from .vtk_transformation import (from_vertices_faces_to_vtk_poly_data,
                                 from_vtk_poly_data_to_vertices_faces)
# ==============================================================================

__all__ = ["write_vertices_faces_to_ply_file",
           "write_vtk_poly_data_to_ply_file",
           "read_ply_to_vertices_faces"]

# ==============================================================================


def write_vertices_faces_to_ply_file(filename, vertices, faces,
                                     vertices_colors=None,
                                     faces_colors=None):
    """ Write methods to save vertices and faces in ply format.
    """

    vtk_poly_data = from_vertices_faces_to_vtk_poly_data(
        vertices, faces,
        vertices_colors=vertices_colors,
        faces_colors=faces_colors)

    write_vtk_poly_data_to_ply_file(filename, vtk_poly_data)


def read_ply_to_vertices_faces(filename):
    """ Read ply file to vertices and faces
    """
    poly_data = read_ply_to_vtk_poly_data(filename)
    vertices, faces, colors = from_vtk_poly_data_to_vertices_faces(poly_data)

    return vertices, faces, colors


def write_vtk_poly_data_to_ply_file(filename, vtk_poly_data):

    ply_writer = vtk.vtkPLYWriter()
    ply_writer.SetFileTypeToASCII()
    ply_writer.SetFileName(filename)
    ply_writer.SetInputData(vtk_poly_data)
    ply_writer.SetArrayName("Colors")
    ply_writer.Write()


def read_ply_to_vtk_poly_data(filename):

    ply_reader = vtk.vtkPLYReader()
    ply_reader.SetFileName(filename)
    ply_reader.Update()

    return ply_reader.GetOutput()