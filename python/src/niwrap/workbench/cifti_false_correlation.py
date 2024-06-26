# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_FALSE_CORRELATION_METADATA = Metadata(
    id="d9322fb5851e19b773262f02faf64bdc8b045a15",
    name="cifti-false-correlation",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiFalseCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_false_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti dscalar file"""


def cifti_false_correlation(
    cifti_in: InputPathType,
    v_3d_dist: float | int,
    geo_outer: float | int,
    geo_inner: float | int,
    cifti_out: InputPathType,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    runner: Runner = None,
) -> CiftiFalseCorrelationOutputs:
    """
    cifti-false-correlation by Washington University School of Medicin.
    
    COMPARE CORRELATION LOCALLY AND ACROSS/THROUGH SULCI/GYRI.
    
    For each vertex, compute the average correlation within a range of geodesic
    distances that don't cross a sulcus/gyrus, and the correlation to the
    closest vertex crossing a sulcus/gyrus. A vertex is considered to cross a
    sulcus/gyrus if the 3D distance is less than a third of the geodesic
    distance. The output file contains the ratio between these correlations, and
    some additional maps to help explain the ratio.
    
    Args:
        cifti_in: the cifti file to use for correlation
        v_3d_dist: maximum 3D distance to check around each vertex
        geo_outer: maximum geodesic distance to use for neighboring correlation
        geo_inner: minimum geodesic distance to use for neighboring correlation
        cifti_out: the output cifti dscalar file
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiFalseCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_FALSE_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-false-correlation")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(str(v_3d_dist))
    cargs.append(str(geo_outer))
    cargs.append(str(geo_inner))
    cargs.append(execution.input_file(cifti_out))
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    ret = CiftiFalseCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_FALSE_CORRELATION_METADATA",
    "CiftiFalseCorrelationOutputs",
    "cifti_false_correlation",
]
