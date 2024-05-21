# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


MRI_BINARIZE_METADATA = Metadata(
    id="ff8383ab748feefab4beb7a1b820c6284bf0c1e2",
    name="mri binarize",
    container_image_type="docker",
    container_image_tag="container/image",
)


class MriBinarizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_binarize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    binary_file_outfile: OutputPathType
    """Binarized output volume."""


def mri_binarize(
    binary_file: InputPathType,
    in_file: InputPathType,
    abs_: bool = False,
    bin_col_num: bool = False,
    bin_val: int | None = None,
    bin_val_not: int | None = None,
    count_file: bool = False,
    count_file_2: InputPathType | None = None,
    dilate: int | None = None,
    erode: int | None = None,
    erode2d: int | None = None,
    frame_no: int | None = None,
    invert: bool = False,
    mask_file: InputPathType | None = None,
    mask_thresh: float | int | None = None,
    match: list[int] = None,
    max_: float | int | None = None,
    merge_file: InputPathType | None = None,
    min_: float | int | None = None,
    out_type: typing.Literal["nii", "nii.gz", "mgz"] | None = None,
    rmax: float | int | None = None,
    rmin: float | int | None = None,
    subjects_dir: InputPathType | None = None,
    ventricles: bool = False,
    wm: bool = False,
    wm_ven_csf: bool = False,
    zero_edges: bool = False,
    zero_slice_edge: bool = False,
    runner: Runner = None,
) -> MriBinarizeOutputs:
    """
    mri binarize by Members of the Laboratories for Computational Neuroimaging (LCN)
    at the Athinoula A. Martinos Center for Biomedical Imaging.
    
    Program to binarize a volume (or volume-encoded surface file). Can also be
    used to merge with other binarizations. Binarization can be done based on
    threshold or on matched values.
    
    More information: https://surfer.nmr.mgh.harvard.edu/fswiki/mri_binarize
    
    Args:
        binary_file: Binary output volume.
        in_file: Input volume.
        abs_: Take abs of invol first (ie, make unsigned).
        bin_col_num: Set binarized voxel value to its column number.
        bin_val: Set vox within thresh to val (default is 1).
        bin_val_not: Set vox outside range to val (default is 0).
        count_file: A boolean or file. Save number of hits in ascii file (hits,
            ntotvox, pct).
        count_file_2: A boolean or file. Save number of hits in ascii file
            (hits, ntotvox, pct).
        dilate: Niters: dilate binarization in 3d.
        erode: Nerode: erode binarization in 3d (after any dilation).
        erode2d: Nerode2d: erode binarization in 2d (after any 3d erosion).
        frame_no: Use 0-based frame of input (default is 0).
        invert: Set binval=0, binvalnot=1.
        mask_file: Must be within mask.
        mask_thresh: Set thresh for mask.
        match: Match instead of threshold.
        max_: Max thresh.
        merge_file: Merge with mergevol.
        min_: Min thresh.
        out_type: 'nii' or 'nii.gz' or 'mgz'. Output file type.
        rmax: Compute max based on rmax*globalmean.
        rmin: Compute min based on rmin*globalmean.
        subjects_dir: file or string representing an existing directory.
            Subjects directory.
        ventricles: Set match vals those for aseg ventricles+choroid (not 4th).
        wm: Set match vals to 2 and 41 (aseg for cerebral wm).
        wm_ven_csf: Wm and ventricular csf, including choroid (not 4th).
        zero_edges: Zero the edge voxels.
        zero_slice_edge: Zero the edge slice voxels.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MriBinarizeOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        count_file +
        (count_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "count_file,\n"
            "count_file_2"
        )
    if (
        (min_ is not None) +
        wm_ven_csf
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "min,\n"
            "wm_ven_csf"
        )
    if (
        (max_ is not None) +
        wm_ven_csf
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "max,\n"
            "wm_ven_csf"
        )
    if (
        (max_ is not None) +
        (min_ is not None) +
        wm_ven_csf
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "max,\n"
            "min,\n"
            "wm_ven_csf"
        )
    if not (
        (max_ is not None) or
        (min_ is not None) or
        (match is not None)
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- max\n"
            "- min\n"
            "- match"
        )
    execution = runner.start_execution(MRI_BINARIZE_METADATA)
    cargs = []
    cargs.append("mri_binarize")
    if abs_:
        cargs.append("--abs")
    if bin_col_num:
        cargs.append("--bincol")
    if bin_val is not None:
        cargs.extend(["--binval", str(bin_val)])
    if bin_val_not is not None:
        cargs.extend(["--binvalnot", str(bin_val_not)])
    cargs.extend(["--o", execution.input_file(binary_file)])
    if count_file_2 is not None:
        cargs.extend(["--count", execution.input_file(count_file_2)])
    if dilate is not None:
        cargs.extend(["--dilate", str(dilate)])
    if erode is not None:
        cargs.extend(["--erode", str(erode)])
    if erode2d is not None:
        cargs.extend(["--erode2d", str(erode2d)])
    if frame_no is not None:
        cargs.extend(["--frame", str(frame_no)])
    cargs.extend(["--i", execution.input_file(in_file)])
    if invert:
        cargs.append("--inv")
    if mask_file is not None:
        cargs.extend(["--mask maskvol", execution.input_file(mask_file)])
    if mask_thresh is not None:
        cargs.extend(["--mask-thresh", str(mask_thresh)])
    if match is not None:
        cargs.extend(["--match", *map(str, match)])
    if max_ is not None:
        cargs.extend(["--max", str(max_)])
    if merge_file is not None:
        cargs.extend(["--merge", execution.input_file(merge_file)])
    if min_ is not None:
        cargs.extend(["--min", str(min_)])
    if out_type is not None:
        cargs.append(out_type)
    if rmax is not None:
        cargs.extend(["--rmax", str(rmax)])
    if rmin is not None:
        cargs.extend(["--rmin", str(rmin)])
    if subjects_dir is not None:
        cargs.append(execution.input_file(subjects_dir))
    if ventricles:
        cargs.append("--ventricles")
    if wm:
        cargs.append("--wm")
    if wm_ven_csf:
        cargs.append("--wm+vcsf")
    if zero_edges:
        cargs.append("--zero-edges")
    if zero_slice_edge:
        cargs.append("--zero-slice-edges")
    ret = MriBinarizeOutputs(
        root=execution.output_file("."),
        binary_file_outfile=execution.output_file(f"{pathlib.Path(binary_file).stem}", optional=True),
    )
    execution.run(cargs)
    return ret
