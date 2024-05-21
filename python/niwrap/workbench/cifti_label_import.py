# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_LABEL_IMPORT_METADATA = Metadata(
    id="80a9f467d099de8121c45581fd8ab22118a67fe8",
    name="cifti-label-import",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiLabelImportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_import(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output cifti label file"""


def cifti_label_import(
    input_: InputPathType,
    label_list_file: str,
    output: InputPathType,
    opt_discard_others: bool = False,
    opt_unlabeled_value_value: float | int | None = None,
    opt_drop_unused_labels: bool = False,
    runner: Runner = None,
) -> CiftiLabelImportOutputs:
    """
    cifti-label-import by Washington University School of Medicin.
    
    MAKE A CIFTI LABEL FILE FROM A CIFTI FILE.
    
    Creates a cifti label file from a cifti file with label-like values. You may
    specify the empty string (use "") for <label-list-file>, which will be
    treated as if it is an empty file. The label list file must have the
    following format (2 lines per label):
    
    <labelname>
    <key> <red> <green> <blue> <alpha>
    ...
    
    Label names are specified on a separate line from their value and color, in
    order to let label names contain spaces. Whitespace is trimmed from both
    ends of the label name, but is kept if it is in the middle of a label. Do
    not specify the "unlabeled" key in the file, it is assumed that 0 means not
    labeled unless -unlabeled-value is specified. The value of <key> specifies
    what value in the imported file should be used as this label (these same key
    values are also used in the output file). The values of <red>, <green>,
    <blue> and <alpha> must be integers from 0 to 255, and will specify the
    color the label is drawn as (alpha of 255 means fully opaque, which is
    probably what you want).
    
    By default, it will create new label names with names like LABEL_5 for any
    values encountered that are not mentioned in the list file, specify
    -discard-others to instead set these values to the "unlabeled" key.
    
    Args:
        input_: the input cifti file
        label_list_file: text file containing the values and names for labels
        output: the output cifti label file
        opt_discard_others: set any values not mentioned in the label list to
            the ??? label
        opt_unlabeled_value_value: set the value that will be interpreted as
            unlabeled: the numeric value for unlabeled (default 0)
        opt_drop_unused_labels: remove any unused label values from the label
            table
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiLabelImportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_IMPORT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-import")
    cargs.append(execution.input_file(input_))
    cargs.append(label_list_file)
    cargs.append(execution.input_file(output))
    if opt_discard_others:
        cargs.append("-discard-others")
    if opt_unlabeled_value_value is not None:
        cargs.extend(["-unlabeled-value", str(opt_unlabeled_value_value)])
    if opt_drop_unused_labels:
        cargs.append("-drop-unused-labels")
    ret = CiftiLabelImportOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret
