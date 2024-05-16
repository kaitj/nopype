# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.606448

import typing

from ..styxdefs import *


V_3DMASKAVE_METADATA = Metadata(
    id="f9b0df29f50dd8be27608bedc16e860e061759da",
    name="3dmaskave",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaskaveOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaskave(...)`.
    """
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3dmaskave(
    runner: Runner,
    in_file: InputPathType,
    mask: InputPathType | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    quiet: bool = False,
) -> V3dmaskaveOutputs:
    """
    Maskave, as implemented in Nipype (module: nipype.interfaces.afni.preprocess,
    interface: Maskave).
    Computes average of all voxels in the input dataset which satisfy the
    criterion in the options list
    For complete details, see the `3dmaskave Documentation.
    <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmaskave.html>`_
    
    Args:
        runner: Command runner
        in_file: Input file to 3dmaskave.
        mask: Matrix to align input file.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        quiet: Matrix to align input file.
    Returns:
        NamedTuple of outputs (described in `V3dmaskaveOutputs`).
    """
    execution = runner.start_execution(V_3DMASKAVE_METADATA)
    cargs = []
    cargs.append("3dmaskave")
    cargs.append(execution.input_file(in_file))
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if quiet:
        cargs.append("-quiet")
    cargs.append("[OUT_FILE]")
    cargs.append("[ARGS]")
    cargs.append("[ENVIRON]")
    if num_threads is not None:
        cargs.append(str(num_threads))
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dmaskaveOutputs(
        out_file=execution.output_file(f"{in_file}_maskave.1D", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret