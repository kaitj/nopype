# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_CREATE_METADATA = Metadata(
    id="6b68d42d72c2c4735fac585516c23277e6915e5c",
    name="volume-create",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_create(
    runner: Runner,
    i_dim: float | int,
    j_dim: float | int,
    k_dim: float | int,
    volume_out: InputPathType,
) -> VolumeCreateOutputs:
    """
    volume-create by Washington University School of Medicin.
    
    CREATE A BLANK VOLUME FILE.
    
    Creates a volume file full of zeros. Exactly one of -plumb or -sform must be
    specified.
    
    Args:
        runner: Command runner
        i_dim: length of first dimension
        j_dim: length of second dimension
        k_dim: length of third dimension
        volume_out: the output volume
    Returns:
        NamedTuple of outputs (described in `VolumeCreateOutputs`).
    """
    execution = runner.start_execution(VOLUME_CREATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-create")
    cargs.append(str(i_dim))
    cargs.append(str(j_dim))
    cargs.append(str(k_dim))
    cargs.append(execution.input_file(volume_out))
    ret = VolumeCreateOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret
