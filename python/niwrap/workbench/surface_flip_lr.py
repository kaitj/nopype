# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_FLIP_LR_METADATA = Metadata(
    id="43bc2e7c2b3bf7be50042ae316b5af59925dab6d",
    name="surface-flip-lr",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceFlipLrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_flip_lr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output flipped surface"""


def surface_flip_lr(
    surface: InputPathType,
    surface_out: InputPathType,
    runner: Runner = None,
) -> SurfaceFlipLrOutputs:
    """
    surface-flip-lr by Washington University School of Medicin.
    
    MIRROR A SURFACE THROUGH THE YZ PLANE.
    
    This command negates the x coordinate of each vertex, and flips the surface
    normals, so that you have a surface of opposite handedness with the same
    features and vertex correspondence, with normals consistent with the
    original surface. That is, if the input surface has normals facing outward,
    the output surface will also have normals facing outward.
    
    Args:
        surface: the surface to flip
        surface_out: the output flipped surface
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceFlipLrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FLIP_LR_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-flip-lr")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceFlipLrOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).stem}"),
    )
    execution.run(cargs)
    return ret
