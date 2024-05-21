# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


V_3DREFIT_METADATA = Metadata(
    id="13f5b136c3dc5d8409a5fe765d3cbe9249866baf",
    name="3drefit",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3drefitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3drefit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output file."""


def v_3drefit(
    in_file: InputPathType,
    atrcopy: list[str] = None,
    atrfloat: list[str] = None,
    atrint: list[str] = None,
    atrstring: list[str] = None,
    deoblique: bool = False,
    duporigin_file: InputPathType | None = None,
    nosaveatr: bool = False,
    saveatr: bool = False,
    space: typing.Literal["TLRC", "MNI", "ORIG"] | None = None,
    xdel: float | int | None = None,
    xorigin: str | None = None,
    xyzscale: float | int | None = None,
    ydel: float | int | None = None,
    yorigin: str | None = None,
    zdel: float | int | None = None,
    zorigin: str | None = None,
    runner: Runner = None,
) -> V3drefitOutputs:
    """
    3drefit by Nipype (interface).
    
    Changes some of the information inside a 3D dataset's header.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3drefit.html
    
    Args:
        in_file: Input file to 3drefit.
        atrcopy: (file, string). Copy afni header attribute from the given file
            into the header of the dataset(s) being modified. for more information
            on afni header attributes, see documentation file readme.attributes.
            more than one '-atrcopy' option can be used. for afni advanced users
            only. do not use -atrcopy or -atrstring with other modification options.
            see also -copyaux.
        atrfloat: (a string, a string). Create or modify floating point
            attributes. the input values may be specified as a single string in
            quotes or as a 1d filename or string, example '1 0.2 0 0 -0.2 1 0 0 0 0
            1 0' or flipz.1d or '1d:1,0.2,2@0,-0.2,1,2@0,2@0,1,0'.
        atrint: (a string, a string). Create or modify integer attributes. the
            input values may be specified as a single string in quotes or as a 1d
            filename or string, example '1 0 0 0 0 1 0 0 0 0 1 0' or flipz.1d or
            '1d:1,0,2@0,-0,1,2@0,2@0,1,0'.
        atrstring: (a string, a string). Copy the last given string into the
            dataset(s) being modified, giving it the attribute name given by the
            last string.to be safe, the last string should be in quotes.
        deoblique: Replace current transformation matrix with cardinal matrix.
        duporigin_file: Copies the xorigin, yorigin, and zorigin values from the
            header of the given dataset.
        nosaveatr: Opposite of -saveatr.
        saveatr: (default) copy the attributes that are known to afni into the
            dset->dblk structure thereby forcing changes to known attributes to be
            present in the output. this option only makes sense with -atrcopy.
        space: 'tlrc' or 'mni' or 'orig'. Associates the dataset with a specific
            template type, e.g. tlrc, mni, orig.
        xdel: New x voxel dimension in mm.
        xorigin: X distance for edge voxel offset.
        xyzscale: Scale the size of the dataset voxels by the given factor.
        ydel: New y voxel dimension in mm.
        yorigin: Y distance for edge voxel offset.
        zdel: New z voxel dimension in mm.
        zorigin: Z distance for edge voxel offset.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3drefitOutputs`).
    """
    runner = runner or get_global_runner()
    if atrcopy is not None and (len(atrcopy) != 2): 
        raise ValueError(f"Length of 'atrcopy' must be 2 but was {len(atrcopy)}")
    if atrfloat is not None and (len(atrfloat) != 2): 
        raise ValueError(f"Length of 'atrfloat' must be 2 but was {len(atrfloat)}")
    if atrint is not None and (len(atrint) != 2): 
        raise ValueError(f"Length of 'atrint' must be 2 but was {len(atrint)}")
    if atrstring is not None and (len(atrstring) != 2): 
        raise ValueError(f"Length of 'atrstring' must be 2 but was {len(atrstring)}")
    execution = runner.start_execution(V_3DREFIT_METADATA)
    cargs = []
    cargs.append("3drefit")
    cargs.append(execution.input_file(in_file))
    if atrcopy is not None:
        cargs.extend(["-atrcopy", *atrcopy])
    if atrfloat is not None:
        cargs.extend(["-atrfloat", *atrfloat])
    if atrint is not None:
        cargs.extend(["-atrint", *atrint])
    if atrstring is not None:
        cargs.extend(["-atrstring", *atrstring])
    if deoblique:
        cargs.append("-deoblique")
    if duporigin_file is not None:
        cargs.extend(["-duporigin", execution.input_file(duporigin_file)])
    if nosaveatr:
        cargs.append("-nosaveatr")
    if saveatr:
        cargs.append("-saveatr")
    if space is not None:
        cargs.extend(["-space", space])
    if xdel is not None:
        cargs.extend(["-xdel", str(xdel)])
    if xorigin is not None:
        cargs.extend(["-xorigin", xorigin])
    if xyzscale is not None:
        cargs.extend(["-xyzscale", str(xyzscale)])
    if ydel is not None:
        cargs.extend(["-ydel", str(ydel)])
    if yorigin is not None:
        cargs.extend(["-yorigin", yorigin])
    if zdel is not None:
        cargs.extend(["-zdel", str(zdel)])
    if zorigin is not None:
        cargs.extend(["-zorigin", zorigin])
    ret = V3drefitOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
