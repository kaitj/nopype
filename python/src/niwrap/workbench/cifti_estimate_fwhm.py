# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_ESTIMATE_FWHM_METADATA = Metadata(
    id="7a751318234df01afe9551193ddbf150b9eff090",
    name="cifti-estimate-fwhm",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_estimate_fwhm(
    cifti: InputPathType,
    opt_merged_volume: bool = False,
    opt_column_column: float | int | None = None,
    opt_whole_file: bool = False,
    runner: Runner = None,
) -> CiftiEstimateFwhmOutputs:
    """
    cifti-estimate-fwhm by Washington University School of Medicin.
    
    ESTIMATE FWHM SMOOTHNESS OF A CIFTI FILE.
    
    Estimate the smoothness of the components of the cifti file, printing the
    estimates to standard output. If -merged-volume is used, all voxels are used
    as a single component, rather than separated by structure.
    
    <structure> must be one of the following:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Args:
        cifti: the input cifti file
        opt_merged_volume: treat volume components as if they were a single
            component
        opt_column_column: only output estimates for one column: the column
            number
        opt_whole_file: estimate for the whole file at once, not each column
            separately
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ESTIMATE_FWHM_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-estimate-fwhm")
    cargs.append(execution.input_file(cifti))
    if opt_merged_volume:
        cargs.append("-merged-volume")
    if opt_column_column is not None:
        cargs.extend(["-column", str(opt_column_column)])
    if opt_whole_file:
        cargs.append("-whole-file")
    ret = CiftiEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ESTIMATE_FWHM_METADATA",
    "CiftiEstimateFwhmOutputs",
    "cifti_estimate_fwhm",
]
