# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_INFORMATION_METADATA = Metadata(
    id="4cdda12b9e875bcb72cbdad68225805c8fb4fb92",
    name="surface-information",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_information(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_information(
    surface_file: InputPathType,
    runner: Runner = None,
) -> SurfaceInformationOutputs:
    """
    surface-information by Washington University School of Medicin.
    
    DISPLAY INFORMATION ABOUT A SURFACE.
    
    Information about surface is displayed including vertices,
    triangles, bounding box, and spacing.
    
    Args:
        surface_file: Surface for which information is displayed
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceInformationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_INFORMATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-information")
    cargs.append(execution.input_file(surface_file))
    ret = SurfaceInformationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
