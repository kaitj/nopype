# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


GIFTI_LABEL_ADD_PREFIX_METADATA = Metadata(
    id="245f082bd4867c44614b2c3bcad70fdb4b41af8f",
    name="gifti-label-add-prefix",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class GiftiLabelAddPrefixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_label_add_prefix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_out: OutputPathType
    """the output label file"""


def gifti_label_add_prefix(
    label_in: InputPathType,
    prefix: str,
    label_out: InputPathType,
    runner: Runner = None,
) -> GiftiLabelAddPrefixOutputs:
    """
    gifti-label-add-prefix by Washington University School of Medicin.
    
    ADD PREFIX TO ALL LABEL NAMES IN A GIFTI LABEL FILE.
    
    For each label other than '???', prepend <prefix> to the label name.
    
    Args:
        label_in: the input label file
        prefix: the prefix string to add
        label_out: the output label file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `GiftiLabelAddPrefixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_LABEL_ADD_PREFIX_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-gifti-label-add-prefix")
    cargs.append(execution.input_file(label_in))
    cargs.append(prefix)
    cargs.append(execution.input_file(label_out))
    ret = GiftiLabelAddPrefixOutputs(
        root=execution.output_file("."),
        label_out=execution.output_file(f"{pathlib.Path(label_out).stem}"),
    )
    execution.run(cargs)
    return ret
