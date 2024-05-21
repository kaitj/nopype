# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


V_3DCALC_METADATA = Metadata(
    id="51d63664df19d5ce9cfa8fe819a3a96c79c6650c",
    name="3dcalc",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""


def v_3dcalc(
    expr: str,
    in_file_a: InputPathType,
    in_file_b: InputPathType | None = None,
    in_file_c: InputPathType | None = None,
    other: InputPathType | None = None,
    overwrite: bool = False,
    single_idx: int | None = None,
    start_idx: int | None = None,
    stop_idx: int | None = None,
    runner: Runner = None,
) -> V3dcalcOutputs:
    """
    3dcalc by RWCox @ AFNI.
    
    AFNI's calculator program.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dcalc.html
    
    Args:
        expr: Expr.
        in_file_a: Input file to 3dcalc.
        in_file_b: Operand file to 3dcalc.
        in_file_c: Operand file to 3dcalc.
        other: Other options.
        overwrite: Overwrite output.
        single_idx: Volume index for in_file_a.
        start_idx: Start index for in_file_a.
        stop_idx: Stop index for in_file_a.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DCALC_METADATA)
    cargs = []
    cargs.append("3dcalc")
    cargs.extend(["-a", execution.input_file(in_file_a)])
    if in_file_b is not None:
        cargs.extend(["-b", execution.input_file(in_file_b)])
    if in_file_c is not None:
        cargs.extend(["-c", execution.input_file(in_file_c)])
    cargs.append("-expr")
    cargs.append(expr)
    if other is not None:
        cargs.append(execution.input_file(other))
    cargs.append("[OUT_FILE]")
    if overwrite:
        cargs.append("-overwrite")
    if single_idx is not None:
        cargs.append(str(single_idx))
    if start_idx is not None:
        cargs.append(str(start_idx))
    if stop_idx is not None:
        cargs.append(str(stop_idx))
    ret = V3dcalcOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file_a).stem}", optional=True),
    )
    execution.run(cargs)
    return ret