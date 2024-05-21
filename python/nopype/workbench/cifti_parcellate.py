# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_PARCELLATE_METADATA = Metadata(
    id="630bb503750beee49d78fb8cfebb0260c5131c7f",
    name="cifti-parcellate",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiParcellateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_parcellate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_parcellate(
    runner: Runner,
    cifti_in: InputPathType,
    cifti_label: InputPathType,
    direction: str,
    cifti_out: InputPathType,
    opt_spatial_weights: bool = False,
    opt_cifti_weights_weight_cifti: InputPathType | None = None,
    opt_method_method: str | None = None,
    opt_only_numeric: bool = False,
    opt_fill_value_value: float | int | None = None,
    opt_nonempty_mask_out: bool = False,
    opt_legacy_mode: bool = False,
    opt_include_empty: bool = False,
) -> CiftiParcellateOutputs:
    """
    cifti-parcellate by Washington University School of Medicin.
    
    PARCELLATE A CIFTI FILE.
    
    Each label (other than the unlabeled key) in the cifti label file will be
    treated as a parcel, and all rows or columns of data within the parcel are
    averaged together to form the parcel's output row or column. If -legacy-mode
    is specified, parcels will be defined as the overlap between a label and the
    data, with no errors for missing data vertices or voxels, and empty parcels
    discarded. The direction can be either an integer starting from 1, or the
    strings 'ROW' or 'COLUMN'. For dtseries or dscalar, use COLUMN. If you are
    parcellating a dconn in both directions, parcellating by ROW first will use
    much less memory.
    
    NOTE: the parcels in the output file are sorted by the numeric label keys,
    in ascending order.
    
    The parameter to the -method option must be one of the following:
    
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
    
    The -*-weights options are mutually exclusive and may only be used with MEAN
    (default), SUM, STDEV, SAMPSTDEV, VARIANCE, MEDIAN, or MODE (default for
    label data).
    
    Args:
        runner: Command runner
        cifti_in: the cifti file to parcellate
        cifti_label: a cifti label file to use for the parcellation
        direction: which mapping to parcellate (integer, ROW, or COLUMN)
        cifti_out: output cifti file
        opt_spatial_weights: use voxel volume and either vertex areas or metric
            files as weights
        opt_cifti_weights_weight_cifti: use a cifti file containing weights: the
            weights to use, as a cifti file
        opt_method_method: specify method of parcellation (default MEAN, or MODE
            if label data): the method to use to assign parcel values from the
            values of member brainordinates
        opt_only_numeric: exclude non-numeric values
        opt_fill_value_value: specify value to use in empty parcels (default 0):
            the value to fill empty parcels with
        opt_nonempty_mask_out: output a matching pscalar file that has 0s in
            empty parcels, and 1s elsewhere
        opt_legacy_mode: use the old behavior, parcels are defined by the
            intersection between labels and valid data, and empty parcels are
            discarded
        opt_include_empty: deprecated: now the default behavior
    Returns:
        NamedTuple of outputs (described in `CiftiParcellateOutputs`).
    """
    execution = runner.start_execution(CIFTI_PARCELLATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-parcellate")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(execution.input_file(cifti_label))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_spatial_weights:
        cargs.append("-spatial-weights")
    if opt_cifti_weights_weight_cifti is not None:
        cargs.extend(["-cifti-weights", execution.input_file(opt_cifti_weights_weight_cifti)])
    if opt_method_method is not None:
        cargs.extend(["-method", opt_method_method])
    if opt_only_numeric:
        cargs.append("-only-numeric")
    if opt_fill_value_value is not None:
        cargs.extend(["-fill-value", str(opt_fill_value_value)])
    if opt_nonempty_mask_out:
        cargs.append("-nonempty-mask-out")
    if opt_legacy_mode:
        cargs.append("-legacy-mode")
    if opt_include_empty:
        cargs.append("-include-empty")
    ret = CiftiParcellateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
