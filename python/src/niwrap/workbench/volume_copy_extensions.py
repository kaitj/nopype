# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


VOLUME_COPY_EXTENSIONS_METADATA = Metadata(
    id="f972fa77b35d122c3070d721e78cb11504df9401",
    name="volume-copy-extensions",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeCopyExtensionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_copy_extensions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_copy_extensions(
    data_volume: InputPathType,
    extension_volume: InputPathType,
    volume_out: InputPathType,
    opt_drop_unknown: bool = False,
    runner: Runner = None,
) -> VolumeCopyExtensionsOutputs:
    """
    volume-copy-extensions by Washington University School of Medicin.
    
    COPY EXTENDED DATA TO ANOTHER VOLUME FILE.
    
    This command copies the information in a volume file that isn't a critical
    part of the standard header or data matrix, e.g. map names, palette
    settings, label tables. If -drop-unknown is not specified, it also copies
    similar kinds of information set by other software.
    
    Args:
        data_volume: the volume file containing the voxel data to use
        extension_volume: the volume file containing the extensions to use
        volume_out: the output volume
        opt_drop_unknown: don't copy extensions that workbench doesn't
            understand
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeCopyExtensionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_COPY_EXTENSIONS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-copy-extensions")
    cargs.append(execution.input_file(data_volume))
    cargs.append(execution.input_file(extension_volume))
    cargs.append(execution.input_file(volume_out))
    if opt_drop_unknown:
        cargs.append("-drop-unknown")
    ret = VolumeCopyExtensionsOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_COPY_EXTENSIONS_METADATA",
    "VolumeCopyExtensionsOutputs",
    "volume_copy_extensions",
]
