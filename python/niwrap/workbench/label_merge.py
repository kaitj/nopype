# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


LABEL_MERGE_METADATA = Metadata(
    id="38935d6b20004adb105681ed307cab61debc5c9a",
    name="label-merge",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class LabelMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label"""


def label_merge(
    label_out: InputPathType,
    opt_label_label_in: InputPathType | None = None,
    runner: Runner = None,
) -> LabelMergeOutputs:
    """
    label-merge by Washington University School of Medicin.
    
    MERGE LABEL FILES INTO A NEW FILE.
    
    Takes one or more label files and constructs a new label file by
    concatenating columns from them. The input files must have the same number
    of vertices and the same structure.
    
    Example: wb_command -label-merge out.label.gii -label first.label.gii
    -column 1 -label second.label.gii
    
    This example would take the first column from first.label.gii and all
    subvolumes from second.label.gii, and write these to out.label.gii.
    
    Args:
        label_out: the output label
        opt_label_label_in: specify an input label: a label file to use columns
            from
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `LabelMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-label-merge")
    cargs.append(execution.input_file(label_out))
    if opt_label_label_in is not None:
        cargs.extend(["-label", execution.input_file(opt_label_label_in)])
    ret = LabelMergeOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{pathlib.Path(label_out).stem}"),
    )
    execution.run(cargs)
    return ret
