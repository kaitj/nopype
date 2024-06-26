# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_ERODE_METADATA = Metadata(
    id="0021f8481a0b01758be8fef5a962d8b7c05be9e8",
    name="cifti-erode",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_erode(
    cifti_in: InputPathType,
    direction: str,
    surface_distance: float | int,
    volume_distance: float | int,
    cifti_out: InputPathType,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_merged_volume: bool = False,
    runner: Runner = None,
) -> CiftiErodeOutputs:
    """
    cifti-erode by Washington University School of Medicin.
    
    ERODE A CIFTI FILE.
    
    For all data values that are empty (for label data, unlabeled, for other
    data, zero), set the surrounding values to empty. The surrounding values are
    defined as the immediate neighbors and all values in the same structure
    within the specified distance (-merged-volume treats all voxels as one
    structure).
    
    The -*-corrected-areas options are intended for eroding on group average
    surfaces, but it is only an approximate correction.
    
    Args:
        cifti_in: the input cifti file
        direction: which dimension to dilate along, ROW or COLUMN
        surface_distance: the distance to dilate on surfaces, in mm
        volume_distance: the distance to dilate in the volume, in mm
        cifti_out: the output cifti file
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        opt_merged_volume: treat volume components as if they were a single
            component
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-erode")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(str(surface_distance))
    cargs.append(str(volume_distance))
    cargs.append(execution.input_file(cifti_out))
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    if opt_merged_volume:
        cargs.append("-merged-volume")
    ret = CiftiErodeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ERODE_METADATA",
    "CiftiErodeOutputs",
    "cifti_erode",
]
