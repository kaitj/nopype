# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_TRANSPOSE_METADATA = Metadata(
    id="6ffc7a423c8a06509ed552536c929cc1ebe31375",
    name="cifti-transpose",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiTransposeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_transpose(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_transpose(
    cifti_in: InputPathType,
    cifti_out: InputPathType,
    opt_mem_limit_limit_gb: float | int | None = None,
    runner: Runner = None,
) -> CiftiTransposeOutputs:
    """
    cifti-transpose by Washington University School of Medicin.
    
    TRANSPOSE A CIFTI FILE.
    
    The input must be a 2-dimensional cifti file. The output is a cifti file
    where every row in the input is a column in the output.
    
    Args:
        cifti_in: the input cifti file
        cifti_out: the output cifti file
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in gigabytes
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiTransposeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_TRANSPOSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-transpose")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(execution.input_file(cifti_out))
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    ret = CiftiTransposeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
