# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_STATS_METADATA = Metadata(
    id="94b5a70cd059e08d38d1ef5e737913c1bbbe4642",
    name="volume-stats",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_stats(
    runner: Runner,
    volume_in: InputPathType,
    opt_reduce_operation: str | None = None,
    opt_percentile_percent: float | int | None = None,
    opt_subvolume_subvolume: str | None = None,
    opt_roi_roi_volume: InputPathType | None = None,
    opt_show_map_name: bool = False,
) -> VolumeStatsOutputs:
    """
    volume-stats by Washington University School of Medicin.
    
    SPATIAL STATISTICS ON A VOLUME FILE.
    
    For each subvolume of the input, a line of text is printed, resulting from
    the specified reduction or percentile operation. Use -subvolume to only give
    output for a single subvolume. If the -roi option is used without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Exactly one of -reduce or
    -percentile must be specified.
    
    The argument to the -reduce option must be one of the following:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Args:
        runner: Command runner
        volume_in: the input volume
        opt_reduce_operation: use a reduction operation: the reduction operation
        opt_percentile_percent: give the value at a percentile: the percentile
            to find, must be between 0 and 100
        opt_subvolume_subvolume: only display output for one subvolume: the
            subvolume number or name
        opt_roi_roi_volume: only consider data inside an roi: the roi, as a
            volume file
        opt_show_map_name: print map index and name before each output
    Returns:
        NamedTuple of outputs (described in `VolumeStatsOutputs`).
    """
    execution = runner.start_execution(VOLUME_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-stats")
    cargs.append(execution.input_file(volume_in))
    if opt_reduce_operation is not None:
        cargs.extend(["-reduce", opt_reduce_operation])
    if opt_percentile_percent is not None:
        cargs.extend(["-percentile", str(opt_percentile_percent)])
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    if opt_roi_roi_volume is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_volume)])
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = VolumeStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
