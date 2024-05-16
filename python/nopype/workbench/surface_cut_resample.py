# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.662562

import typing

from ..styxdefs import *


SURFACE_CUT_RESAMPLE_METADATA = Metadata(
    id="8819053df0ae223919c29fae0e5ef66382a3f0e8",
    name="surface-cut-resample",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceCutResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_cut_resample(...)`.
    """
    surface_out: OutputPathType
    """the output surface file"""


def surface_cut_resample(
    runner: Runner,
    surface_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    surface_out: InputPathType,
) -> SurfaceCutResampleOutputs:
    """
    RESAMPLE A CUT SURFACE.
    
    Resamples a surface file, given two spherical surfaces that are in register.
    Barycentric resampling is used, because it is usually better for resampling
    surfaces, and because it is needed to figure out the new topology anyway.
    
    Args:
        runner: Command runner
        surface_in: the surface file to resample
        current_sphere: a sphere surface with the mesh that the input surface is
            currently on
        new_sphere: a sphere surface that is in register with <current-sphere>
            and has the desired output mesh
        surface_out: the output surface file
    Returns:
        NamedTuple of outputs (described in `SurfaceCutResampleOutputs`).
    """
    execution = runner.start_execution(SURFACE_CUT_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-cut-resample")
    cargs.append(execution.input_file(surface_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceCutResampleOutputs(
        surface_out=execution.output_file(f"{surface_out}"),
    )
    execution.run(cargs)
    return ret