# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


GIFTI_CONVERT_METADATA = Metadata(
    id="9480e7d2b343860c91638bd03b1b25c561fae417",
    name="gifti-convert",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class GiftiConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gifti_convert(
    runner: Runner,
    gifti_encoding: str,
    input_gifti_file: str,
    output_gifti_file: str,
) -> GiftiConvertOutputs:
    """
    gifti-convert by Washington University School of Medicin.
    
    CONVERT A GIFTI FILE TO A DIFFERENT ENCODING.
    
    The value of <gifti-encoding> must be one of the following:
    
    ASCII
    BASE64_BINARY
    GZIP_BASE64_BINARY
    EXTERNAL_FILE_BINARY.
    
    Args:
        runner: Command runner
        gifti_encoding: what the output encoding should be
        input_gifti_file: the input gifti file
        output_gifti_file: output - the output gifti file
    Returns:
        NamedTuple of outputs (described in `GiftiConvertOutputs`).
    """
    execution = runner.start_execution(GIFTI_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-gifti-convert")
    cargs.append(gifti_encoding)
    cargs.append(input_gifti_file)
    cargs.append(output_gifti_file)
    ret = GiftiConvertOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
