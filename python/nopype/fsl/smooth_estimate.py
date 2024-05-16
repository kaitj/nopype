# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.824879

import typing

from ..styxdefs import *


SMOOTH_ESTIMATE_METADATA = Metadata(
    id="43c5a17623148d074c90f202493e9a65dccd7ac6",
    name="SmoothEstimate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SmoothEstimateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `smooth_estimate(...)`.
    """
    res_volume: OutputPathType
    """Residual fit image"""
    zstat_volume: OutputPathType
    """Zstat image"""


def smooth_estimate(
    runner: Runner,
    mask_file: InputPathType,
    dof: int | None = None,
    residual_fit_file: InputPathType | None = None,
    zstat_file: InputPathType | None = None,
) -> SmoothEstimateOutputs:
    """
    SmoothEstimate, as implemented in Nipype (module: nipype.interfaces.fsl,
    interface: SmoothEstimate).
    Estimates the smoothness of an image
    
    Args:
        runner: Command runner
        mask_file: Brain mask volume.
        dof: Number of degrees of freedom.
        residual_fit_file: Residual-fit image file.
        zstat_file: Zstat image file.
    Returns:
        NamedTuple of outputs (described in `SmoothEstimateOutputs`).
    """
    if (
        (zstat_file is not None) +
        (dof is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "zstat_file,\n"
            "dof"
        )
    if not (
        (zstat_file is not None) or
        (dof is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- zstat_file\n"
            "- dof"
        )
    if not (
        (dof is not None) ==
        (residual_fit_file is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "dof,\n"
            "residual_fit_file"
        )
    execution = runner.start_execution(SMOOTH_ESTIMATE_METADATA)
    cargs = []
    cargs.append("smoothest")
    if dof is not None:
        cargs.append(("--dof=" + str(dof)))
    cargs.append(("--mask=" + execution.input_file(mask_file)))
    if residual_fit_file is not None:
        cargs.append(("--res=" + execution.input_file(residual_fit_file)))
    if zstat_file is not None:
        cargs.append(("--zstat=" + execution.input_file(zstat_file)))
    ret = SmoothEstimateOutputs(
        res_volume=execution.output_file(f"{residual_fit_file}", optional=True),
        zstat_volume=execution.output_file(f"{zstat_file}", optional=True),
    )
    execution.run(cargs)
    return ret