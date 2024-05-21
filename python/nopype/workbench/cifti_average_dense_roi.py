# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_AVERAGE_DENSE_ROI_METADATA = Metadata(
    id="619087cc03ea03b97e13f0aa40b3200911bbec15",
    name="cifti-average-dense-roi",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiAverageDenseRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average_dense_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti dscalar file"""


def cifti_average_dense_roi(
    runner: Runner,
    cifti_out: InputPathType,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    opt_left_area_surf_left_surf: InputPathType | None = None,
    opt_right_area_surf_right_surf: InputPathType | None = None,
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiAverageDenseRoiOutputs:
    """
    cifti-average-dense-roi by Washington University School of Medicin.
    
    AVERAGE CIFTI ROWS ACROSS SUBJECTS BY ROI.
    
    Averages rows for each map of the ROI(s), across all files. ROI maps are
    treated as weighting functions, including negative values. For efficiency,
    ensure that everything that is not intended to be used is zero in the ROI
    map. If -cifti-roi is specified, -left-roi, -right-roi, -cerebellum-roi, and
    -vol-roi must not be specified. If multiple non-cifti ROI files are
    specified, they must have the same number of columns.
    
    Args:
        runner: Command runner
        cifti_out: output cifti dscalar file
        opt_cifti_roi_roi_cifti: cifti file containing combined weights: the roi
            cifti file
        opt_left_roi_roi_metric: weights to use for left hempsphere: the left
            roi as a metric file
        opt_right_roi_roi_metric: weights to use for right hempsphere: the right
            roi as a metric file
        opt_cerebellum_roi_roi_metric: weights to use for cerebellum surface:
            the cerebellum roi as a metric file
        opt_vol_roi_roi_vol: voxel weights to use: the roi volume file
        opt_left_area_surf_left_surf: specify the left surface for vertex area
            correction: the left surface file
        opt_right_area_surf_right_surf: specify the right surface for vertex
            area correction: the right surface file
        opt_cerebellum_area_surf_cerebellum_surf: specify the cerebellum surface
            for vertex area correction: the cerebellum surface file
        opt_cifti_cifti_in: specify an input cifti file: a cifti file to average
            across
    Returns:
        NamedTuple of outputs (described in `CiftiAverageDenseRoiOutputs`).
    """
    execution = runner.start_execution(CIFTI_AVERAGE_DENSE_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average-dense-roi")
    cargs.append(execution.input_file(cifti_out))
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_left_roi_roi_metric is not None:
        cargs.extend(["-left-roi", execution.input_file(opt_left_roi_roi_metric)])
    if opt_right_roi_roi_metric is not None:
        cargs.extend(["-right-roi", execution.input_file(opt_right_roi_roi_metric)])
    if opt_cerebellum_roi_roi_metric is not None:
        cargs.extend(["-cerebellum-roi", execution.input_file(opt_cerebellum_roi_roi_metric)])
    if opt_vol_roi_roi_vol is not None:
        cargs.extend(["-vol-roi", execution.input_file(opt_vol_roi_roi_vol)])
    if opt_left_area_surf_left_surf is not None:
        cargs.extend(["-left-area-surf", execution.input_file(opt_left_area_surf_left_surf)])
    if opt_right_area_surf_right_surf is not None:
        cargs.extend(["-right-area-surf", execution.input_file(opt_right_area_surf_right_surf)])
    if opt_cerebellum_area_surf_cerebellum_surf is not None:
        cargs.extend(["-cerebellum-area-surf", execution.input_file(opt_cerebellum_area_surf_cerebellum_surf)])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiAverageDenseRoiOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
