# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_FIND_CLUSTERS_METADATA = Metadata(
    id="f73f2390bc8f228c5ea82870ebbb4d7bdefcbc12",
    name="cifti-find-clusters",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiFindClustersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_find_clusters(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_find_clusters(
    runner: Runner,
    cifti: InputPathType,
    surface_value_threshold: float | int,
    surface_minimum_area: float | int,
    volume_value_threshold: float | int,
    volume_minimum_size: float | int,
    direction: str,
    cifti_out: InputPathType,
    opt_less_than: bool = False,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_merged_volume: bool = False,
    opt_start_startval: float | int | None = None,
) -> CiftiFindClustersOutputs:
    """
    cifti-find-clusters by Washington University School of Medicin.
    
    FILTER CLUSTERS BY AREA/VOLUME.
    
    Outputs a cifti file with nonzero integers for all brainordinates within a
    large enough cluster, and zeros elsewhere. The integers denote cluster
    membership (by default, first cluster found will use value 1, second cluster
    2, etc). Cluster values are not reused across maps of the output, but
    instead keep counting up. The input cifti file must have a brain models
    mapping on the chosen dimension, columns for .dtseries, and either for
    .dconn. The ROI should have a brain models mapping along columns, exactly
    matching the mapping of the chosen direction in the input file. Data outside
    the ROI is ignored.
    
    Args:
        runner: Command runner
        cifti: the input cifti
        surface_value_threshold: threshold for surface data values
        surface_minimum_area: threshold for surface cluster area, in mm^2
        volume_value_threshold: threshold for volume data values
        volume_minimum_size: threshold for volume cluster size, in mm^3
        direction: which dimension to use for spatial information, ROW or COLUMN
        cifti_out: the output cifti
        opt_less_than: find values less than <value-threshold>, rather than
            greater
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        opt_cifti_roi_roi_cifti: search only within regions of interest: the
            regions to search within, as a cifti file
        opt_merged_volume: treat volume components as if they were a single
            component
        opt_start_startval: start labeling clusters from a value other than 1:
            the value to give the first cluster found
    Returns:
        NamedTuple of outputs (described in `CiftiFindClustersOutputs`).
    """
    execution = runner.start_execution(CIFTI_FIND_CLUSTERS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-find-clusters")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surface_value_threshold))
    cargs.append(str(surface_minimum_area))
    cargs.append(str(volume_value_threshold))
    cargs.append(str(volume_minimum_size))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_less_than:
        cargs.append("-less-than")
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_merged_volume:
        cargs.append("-merged-volume")
    if opt_start_startval is not None:
        cargs.extend(["-start", str(opt_start_startval)])
    ret = CiftiFindClustersOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
