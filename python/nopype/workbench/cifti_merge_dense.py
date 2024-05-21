# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_MERGE_DENSE_METADATA = Metadata(
    id="ac60ad26544c68ae324e607ff87b6b1a618c78a0",
    name="cifti-merge-dense",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge_dense(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_merge_dense(
    runner: Runner,
    direction: str,
    cifti_out: InputPathType,
    opt_label_collision_action: str | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
) -> CiftiMergeDenseOutputs:
    """
    cifti-merge-dense by Washington University School of Medicin.
    
    MERGE CIFTI FILES ALONG DENSE DIMENSION.
    
    The input cifti files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Args:
        runner: Command runner
        direction: which dimension to merge along, ROW or COLUMN
        cifti_out: the output cifti file
        opt_label_collision_action: how to handle conflicts between label keys:
            'ERROR', 'FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY' to match
            v1.4.2 and earlier
        opt_cifti_cifti_in: specify an input cifti file: a cifti file to merge
    Returns:
        NamedTuple of outputs (described in `CiftiMergeDenseOutputs`).
    """
    execution = runner.start_execution(CIFTI_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge-dense")
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_label_collision_action is not None:
        cargs.extend(["-label-collision", opt_label_collision_action])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiMergeDenseOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
