# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.604149

import typing

from ..styxdefs import *


V_3D_ECM_METADATA = Metadata(
    id="2451878998b675098e5305aa30ac6cf7e9bf71da",
    name="3dECM",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dEcmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_ecm(...)`.
    """
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_ecm(
    runner: Runner,
    in_file: InputPathType,
    autoclip: bool = False,
    automask: bool = False,
    eps: float | int | None = None,
    fecm: bool = False,
    full: bool = False,
    mask: InputPathType | None = None,
    max_iter: int | None = None,
    memory: float | int | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    polort: int | None = None,
    scale: float | int | None = None,
    shift: float | int | None = None,
    sparsity: float | int | None = None,
    thresh: float | int | None = None,
) -> V3dEcmOutputs:
    """
    ECM, as implemented in Nipype (module: nipype.interfaces.afni.preprocess,
    interface: ECM).
    Performs degree centrality on a dataset using a given maskfile via the 3dECM
    command
    For complete details, see the `3dECM Documentation.
    <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dECM.html>`_
    
    Args:
        runner: Command runner
        in_file: Input file to 3decm.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Mask the dataset to target brain-only voxels.
        eps: Sets the stopping criterion for the power iteration;
            :math:`l2\|v_\text{old} - v_\text{new}\| < eps\|v_\text{old}\|`; default
            = 0.001.
        fecm: Fast centrality method; substantial speed increase but cannot
            accommodate thresholding; automatically selected if -thresh or -sparsity
            are not set.
        full: Full power method; enables thresholding; automatically selected if
            -thresh or -sparsity are set.
        mask: Mask file to mask input data.
        max_iter: Sets the maximum number of iterations to use in the power
            iteration; default = 1000.
        memory: Limit memory consumption on system by setting the amount of gb
            to limit the algorithm to; default = 2gb.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        polort: No description provided.
        scale: Scale correlation coefficients in similarity matrix to after
            shifting, x >= 0.0; default = 1.0 for -full, 0.5 for -fecm.
        shift: Shift correlation coefficients in similarity matrix to enforce
            non-negativity, s >= 0.0; default = 0.0 for -full, 1.0 for -fecm.
        sparsity: Only take the top percent of connections.
        thresh: Threshold to exclude connections where corr <= thresh.
    Returns:
        NamedTuple of outputs (described in `V3dEcmOutputs`).
    """
    execution = runner.start_execution(V_3D_ECM_METADATA)
    cargs = []
    cargs.append("3dECM")
    cargs.append(execution.input_file(in_file))
    cargs.append("[ARGS]")
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    cargs.append("[ENVIRON]")
    if eps is not None:
        cargs.extend(["-eps", str(eps)])
    if fecm:
        cargs.append("-fecm")
    if full:
        cargs.append("-full")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if max_iter is not None:
        cargs.extend(["-max_iter", str(max_iter)])
    if memory is not None:
        cargs.extend(["-memory", str(memory)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if polort is not None:
        cargs.extend(["-polort", str(polort)])
    if scale is not None:
        cargs.extend(["-scale", str(scale)])
    if shift is not None:
        cargs.extend(["-shift", str(shift)])
    if sparsity is not None:
        cargs.extend(["-sparsity", str(sparsity)])
    if thresh is not None:
        cargs.extend(["-thresh", str(thresh)])
    ret = V3dEcmOutputs(
        out_file=execution.output_file(f"{in_file}_afni", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret