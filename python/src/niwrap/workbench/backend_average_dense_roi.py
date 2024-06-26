# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


BACKEND_AVERAGE_DENSE_ROI_METADATA = Metadata(
    id="636c2d8c5fef1ea15715dad85b98f4cfd6a352dc",
    name="backend-average-dense-roi",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class BackendAverageDenseRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_dense_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def backend_average_dense_roi(
    index_list: str,
    out_file: str,
    runner: Runner = None,
) -> BackendAverageDenseRoiOutputs:
    """
    backend-average-dense-roi by Washington University School of Medicin.
    
    CONNECTOME DB BACKEND COMMAND FOR CIFTI AVERAGE DENSE ROI.
    
    This command is probably not the one you are looking for, try
    -cifti-average-dense-roi. It takes the list of cifti files to average from
    standard input, and writes its output as little endian, 32-bit integer of
    row size followed by the row as 32-bit floats.
    
    Args:
        index_list: comma separated list of cifti indexes to average
        out_file: file to write the average row to
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `BackendAverageDenseRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BACKEND_AVERAGE_DENSE_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-backend-average-dense-roi")
    cargs.append(index_list)
    cargs.append(out_file)
    ret = BackendAverageDenseRoiOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BACKEND_AVERAGE_DENSE_ROI_METADATA",
    "BackendAverageDenseRoiOutputs",
    "backend_average_dense_roi",
]
