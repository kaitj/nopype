# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


VOLUME_LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="57b5e04991f64c68568cfa323f21d46032ad22c8",
    name="volume-label-export-table",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeLabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_export_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_label_export_table(
    label_in: InputPathType,
    map_: str,
    table_out: str,
    runner: Runner = None,
) -> VolumeLabelExportTableOutputs:
    """
    volume-label-export-table by Washington University School of Medicin.
    
    EXPORT LABEL TABLE FROM VOLUME AS TEXT.
    
    Takes the label table from the volume label map, and writes it to a text
    format matching what is expected by -volume-label-import.
    
    Args:
        label_in: the input volume label file
        map_: the number or name of the label map to use
        table_out: output - the output text file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeLabelExportTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_EXPORT_TABLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-export-table")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(table_out)
    ret = VolumeLabelExportTableOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_LABEL_EXPORT_TABLE_METADATA",
    "VolumeLabelExportTableOutputs",
    "volume_label_export_table",
]
