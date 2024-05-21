# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SIGNED_DISTANCE_TO_SURFACE_METADATA = Metadata(
    id="776faeacd8f65f9e804110ff539f906d0c75dd79",
    name="signed-distance-to-surface",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SignedDistanceToSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `signed_distance_to_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric: OutputPathType
    """the output metric"""


def signed_distance_to_surface(
    surface_comp: InputPathType,
    surface_ref: InputPathType,
    metric: InputPathType,
    opt_winding_method: str | None = None,
    runner: Runner = None,
) -> SignedDistanceToSurfaceOutputs:
    """
    signed-distance-to-surface by Washington University School of Medicin.
    
    COMPUTE SIGNED DISTANCE FROM ONE SURFACE TO ANOTHER.
    
    Compute the signed distance function of the reference surface at every
    vertex on the comparison surface. NOTE: this relation is NOT symmetric, the
    line from a vertex to the closest point on the 'ref' surface (the one that
    defines the signed distance function) will only align with the normal of the
    'ref' surface. Valid specifiers for winding methods are as follows:
    
    EVEN_ODD (default)
    NEGATIVE
    NONZERO
    NORMALS
    
    The NORMALS method uses the normals of triangles and edges, or the closest
    triangle hit by a ray from the point. This method may be slightly faster,
    but is only reliable for a closed surface that does not cross through
    itself. All other methods count entry (positive) and exit (negative)
    crossings of a vertical ray from the point, then counts as inside if the
    total is odd, negative, or nonzero, respectively.
    
    Args:
        surface_comp: the comparison surface to measure the signed distance on
        surface_ref: the reference surface that defines the signed distance
            function
        metric: the output metric
        opt_winding_method: winding method for point inside surface test: name
            of the method (default EVEN_ODD)
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SignedDistanceToSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGNED_DISTANCE_TO_SURFACE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-signed-distance-to-surface")
    cargs.append(execution.input_file(surface_comp))
    cargs.append(execution.input_file(surface_ref))
    cargs.append(execution.input_file(metric))
    if opt_winding_method is not None:
        cargs.extend(["-winding", opt_winding_method])
    ret = SignedDistanceToSurfaceOutputs(
        root=execution.output_file("."),
        metric=execution.output_file(f"{pathlib.Path(metric).stem}"),
    )
    execution.run(cargs)
    return ret
