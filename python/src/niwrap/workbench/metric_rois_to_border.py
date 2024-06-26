# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


METRIC_ROIS_TO_BORDER_METADATA = Metadata(
    id="5665125d3656b52cf1ca6caaac3e3b292f925d44",
    name="metric-rois-to-border",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricRoisToBorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_rois_to_border(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


def metric_rois_to_border(
    surface: InputPathType,
    metric: InputPathType,
    class_name: str,
    border_out: InputPathType,
    opt_placement_fraction: float | int | None = None,
    opt_column_column: str | None = None,
    runner: Runner = None,
) -> MetricRoisToBorderOutputs:
    """
    metric-rois-to-border by Washington University School of Medicin.
    
    DRAW BORDERS AROUND METRIC ROIS.
    
    For each ROI column, finds all edges on the mesh that cross the boundary of
    the ROI, and draws borders through them. By default, this is done on all
    columns in the input file, using the map name as the name for the border.
    
    Args:
        surface: the surface to use for neighbor information
        metric: the input metric containing ROIs
        class_name: the name to use for the class of the output borders
        border_out: the output border file
        opt_placement_fraction: set how far along the edge border points are
            drawn: fraction along edge from inside vertex (default 0.33)
        opt_column_column: select a single column: the column number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricRoisToBorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ROIS_TO_BORDER_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-rois-to-border")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric))
    cargs.append(class_name)
    cargs.append(execution.input_file(border_out))
    if opt_placement_fraction is not None:
        cargs.extend(["-placement", str(opt_placement_fraction)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = MetricRoisToBorderOutputs(
        root=execution.output_file("."),
        border_out=execution.output_file(f"{pathlib.Path(border_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_ROIS_TO_BORDER_METADATA",
    "MetricRoisToBorderOutputs",
    "metric_rois_to_border",
]
