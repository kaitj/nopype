# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SCENE_FILE_MERGE_METADATA = Metadata(
    id="5350c41bc7fd58082574719625c1d6c0791e69a3",
    name="scene-file-merge",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SceneFileMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_merge(
    runner: Runner,
    scene_file_out: str,
    opt_scene_file_scene_file: str | None = None,
) -> SceneFileMergeOutputs:
    """
    scene-file-merge by Washington University School of Medicin.
    
    REARRANGE SCENES INTO A NEW FILE.
    
    Takes one or more scene files and constructs a new scene file by
    concatenating specified scenes from them.
    
    Example: wb_command -scene-file-merge out.scene -scene-file first.scene
    -scene 1 -scene-file second.scene
    
    This example would take the first scene from first.scene, followed by all
    scenes from second.scene, and write these scenes to out.scene.
    
    Args:
        runner: Command runner
        scene_file_out: output - the output scene file
        opt_scene_file_scene_file: specify a scene file to use scenes from: the
            input scene file
    Returns:
        NamedTuple of outputs (described in `SceneFileMergeOutputs`).
    """
    execution = runner.start_execution(SCENE_FILE_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-merge")
    cargs.append(scene_file_out)
    if opt_scene_file_scene_file is not None:
        cargs.extend(["-scene-file", opt_scene_file_scene_file])
    ret = SceneFileMergeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
