# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_NORMALS_METADATA = Metadata(
    id="cd9ef7063094ee215a9944b8661fee6515043b6c",
    name="surface-normals",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceNormalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_normals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the normal vectors"""


def surface_normals(
    surface: InputPathType,
    metric_out: InputPathType,
    runner: Runner = None,
) -> SurfaceNormalsOutputs:
    """
    surface-normals by Washington University School of Medicin.
    
    OUTPUT VERTEX NORMALS AS METRIC FILE.
    
    Computes the normal vectors of the surface file, and outputs them as a 3
    column metric file.
    
    Args:
        surface: the surface to output the normals of
        metric_out: the normal vectors
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceNormalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_NORMALS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-normals")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_out))
    ret = SurfaceNormalsOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_NORMALS_METADATA",
    "SurfaceNormalsOutputs",
    "surface_normals",
]
