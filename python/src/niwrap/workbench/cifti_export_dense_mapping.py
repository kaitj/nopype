# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_EXPORT_DENSE_MAPPING_METADATA = Metadata(
    id="208bbece4ecfd083c9add2ae931044e548d4ff2d",
    name="cifti-export-dense-mapping",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiExportDenseMappingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_export_dense_mapping(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_export_dense_mapping(
    cifti: InputPathType,
    direction: str,
    opt_volume_all_text_out: str | None = None,
    runner: Runner = None,
) -> CiftiExportDenseMappingOutputs:
    """
    cifti-export-dense-mapping by Washington University School of Medicin.
    
    WRITE INDEX TO ELEMENT MAPPING AS TEXT.
    
    This command produces text files that describe the mapping from cifti
    indices to surface vertices or voxels. All indices are zero-based. The
    default format for -surface is lines of the form:
    
    <cifti-index> <vertex>
    
    The default format for -volume and -volume-all is lines of the form:
    
    <cifti-index> <i> <j> <k>
    
    For each <structure> argument, use one of the following strings:
    
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
        cifti: the cifti file
        direction: which direction to export the mapping from, ROW or COLUMN
        opt_volume_all_text_out: export the the mapping of all voxels: output -
            the output text file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiExportDenseMappingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_EXPORT_DENSE_MAPPING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-export-dense-mapping")
    cargs.append(execution.input_file(cifti))
    cargs.append(direction)
    if opt_volume_all_text_out is not None:
        cargs.extend(["-volume-all", opt_volume_all_text_out])
    ret = CiftiExportDenseMappingOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret