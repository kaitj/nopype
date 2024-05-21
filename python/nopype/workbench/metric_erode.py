# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METRIC_ERODE_METADATA = Metadata(
    id="60e9fb531f701f2dbee43284fde775a563ab240e",
    name="metric-erode",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_erode(
    runner: Runner,
    metric: InputPathType,
    surface: InputPathType,
    distance: float | int,
    metric_out: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
) -> MetricErodeOutputs:
    """
    metric-erode by Washington University School of Medicin.
    
    ERODE A METRIC FILE.
    
    Around each vertex with a value of zero, set surrounding vertices to zero.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Args:
        runner: Command runner
        metric: the metric file to erode
        surface: the surface to compute on
        distance: distance in mm to erode
        metric_out: the output metric
        opt_roi_roi_metric: assume values outside this roi are nonzero: metric
            file, positive values denote vertices that have data
        opt_column_column: select a single column to erode: the column number or
            name
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
    Returns:
        NamedTuple of outputs (described in `MetricErodeOutputs`).
    """
    execution = runner.start_execution(METRIC_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-erode")
    cargs.append(execution.input_file(metric))
    cargs.append(execution.input_file(surface))
    cargs.append(str(distance))
    cargs.append(execution.input_file(metric_out))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricErodeOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret
