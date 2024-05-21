# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METRIC_GRADIENT_METADATA = Metadata(
    id="cc0cb424634fbc2eaea5656163a0f50668188412",
    name="metric-gradient",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricGradientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_gradient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the magnitude of the gradient"""


def metric_gradient(
    runner: Runner,
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_presmooth_kernel: float | int | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_vectors: bool = False,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    opt_average_normals: bool = False,
) -> MetricGradientOutputs:
    """
    metric-gradient by Washington University School of Medicin.
    
    SURFACE GRADIENT OF A METRIC FILE.
    
    At each vertex, the immediate neighbors are unfolded onto a plane tangent to
    the surface at the vertex (specifically, perpendicular to the normal). The
    gradient is computed using a regression between the unfolded positions of
    the vertices and their values. The gradient is then given by the slopes of
    the regression, and reconstructed as a 3D gradient vector. By default, takes
    the gradient of all columns, with no presmoothing, across the whole surface,
    without averaging the normals of the surface among neighbors.
    
    When using -corrected-areas, note that it is an approximate correction.
    Doing smoothing on individual surfaces before averaging/gradient is
    preferred, when possible, in order to make use of the original surface
    structure.
    
    Specifying an ROI will restrict the gradient to only use data from where the
    ROI metric is positive, and output zeros anywhere the ROI metric is not
    positive.
    
    By default, the first column of the roi metric is used for all input
    columns. When -match-columns is specified to the -roi option, the input and
    roi metrics must have the same number of columns, and for each input
    column's index, the same column index is used in the roi metric. If the
    -match-columns option to -roi is used while the -column option is also used,
    the number of columns of the roi metric must match the input metric, and it
    will use the roi column with the index of the selected input column.
    
    The vector output metric is organized such that the X, Y, and Z components
    from a single input column are consecutive columns.
    
    Args:
        runner: Command runner
        surface: the surface to compute the gradient on
        metric_in: the metric to compute the gradient of
        metric_out: the magnitude of the gradient
        opt_presmooth_kernel: smooth the metric before computing the gradient:
            the size of the gaussian smoothing kernel in mm, as sigma by default
        opt_roi_roi_metric: select a region of interest to take the gradient of:
            the area to take the gradient within, as a metric
        opt_vectors: output gradient vectors
        opt_column_column: select a single column to compute the gradient of:
            the column number or name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        opt_average_normals: average the normals of each vertex with its
            neighbors before using them to compute the gradient
    Returns:
        NamedTuple of outputs (described in `MetricGradientOutputs`).
    """
    execution = runner.start_execution(METRIC_GRADIENT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-gradient")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_presmooth_kernel is not None:
        cargs.extend(["-presmooth", str(opt_presmooth_kernel)])
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_vectors:
        cargs.append("-vectors")
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    if opt_average_normals:
        cargs.append("-average-normals")
    ret = MetricGradientOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret
