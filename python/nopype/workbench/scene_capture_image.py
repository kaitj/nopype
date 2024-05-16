# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.645964

import typing

from ..styxdefs import *


SCENE_CAPTURE_IMAGE_METADATA = Metadata(
    id="6ba2c5ef98dcd29b02df9c315b9f429ad499737e",
    name="scene-capture-image",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SceneCaptureImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_capture_image(...)`.
    """


def scene_capture_image(
    runner: Runner,
    scene_file: str,
    scene_name_or_number: str,
    image_file_name: str,
    opt_size_window: bool = False,
    opt_size_capture: bool = False,
    opt_size_width_width: float | int | None = None,
    opt_size_height_height: float | int | None = None,
    opt_units_units: str | None = None,
    opt_margin_size: float | int | None = None,
    opt_no_scene_colors: bool = False,
    opt_show_capture_settings: bool = False,
    opt_renderer_renderer: str | None = None,
    opt_print_image_info: bool = False,
) -> SceneCaptureImageOutputs:
    """
    OFFSCREEN RENDERING OF SCENE TO AN IMAGE FILE.
    
    ----------------------------------------------------------------------
    
    Render content of browser windows displayed in a scene into image file(s).
    
    If none of the "-size" options are specified, the default is "-size-window"
    (Output image is size of the window that was saved in the scene).
    
    For the "-size" options that accept a width and/or height, the values
    default to number of pixels. To express the width and/or height in physical
    units (inches, centimeters, etc.), use the "-units" option. When physical
    units are used, the pixel width and height are derived using the physical
    width/height and the image resolution (see the "-resolution" option).
    
    Note that scenes created prior to version 1.2 (May 2016) do not contain
    information about the size of the window. Therefore, one must use the
    "-size-width-height" option.
    
    Examples:
    
    Generate an image of the second scene. Width and height of image is width
    and height of window saved in the scene.
    wb_command -scene-capture-image myscene.scene 2 image2.jpg
    
    Generate an image of the second scene with a margin around sides of the
    image. Width and height of image is width and height of window saved in the
    scene.
    wb_command -scene-capture-image myscene.scene 2 image2.jpg -margin 10
    
    Generate an image of the second scene that is 6 inches width with 300 pixels
    per inch. The resulting width is 1800 pixels. The resulting height of the
    image is a function of the width and the aspect ratio (height divided by
    width) of the window size saved in the scene.
    wb_command -scene-capture-image myscene.scene 2 image21.jpg \
    -size-width 6 -units INCHES -resolution 300 PIXELS_PER_INCH
    
    Print information about the size of the output image for the second scene
    (no image file is created) using a width of 4.5 centimeters.
    wb_command -scene-capture-image myscene.scene 2 test.jpg \
    -size-width 4.5 -units CENTIMETERS -print-image-info
    
    
    
    
    NO OFF SCREEN RENDERERS AVAILABLE ON THIS SYSTEM. COMMAND WILL FAIL !!!!
    
    
    ERROR: -scene-capture-image is not available !
    A required library for this command, Mesa3D (software version of OpenGL),
    was not available when this software was created. This command is not
    available for the Windows version of this software but should always be
    available in the Linux and MacOS versions.
    
    Args:
        runner: Command runner
        scene_file: scene file
        scene_name_or_number: name or number (starting at one) of the scene in
            the scene file
        image_file_name: output - image file name
            The file name must end with a valid extension that
            identifies the image file format. Valid extensions
            on this system are: (.bmp .jpeg .jpg .png .ppm).
            
            If there is more than one window in the scene,
            multiple image files are output with the window's
            number inserted into the name of the image file
            immediately before the image file's extension.
        opt_size_window: Output image is size of window's graphics region from
            when scene was created.
        opt_size_capture: Output image uses size from Capture Dialog when scene
            was created
        opt_size_width_width: Width for output image. Height is computed using
            the aspect ratio from the window's width and height saved in the scene.:
            Width for output image
        opt_size_height_height: Height for output image. Width is computed using
            the aspect ratio from the window's width and height saved in the scene.:
            Height for output image
        opt_units_units: Units for image width/height
            Default is PIXELS: Name of units for image
            width/height. Valid units are:
            INCHES
            CENTIMETERS
            MILLIMETERS
            METERS
            PIXELS
        opt_margin_size: Add a margin to sides of the image using the window's
            background color.: size of margin, in pixels, added to all sides of
            output image
        opt_no_scene_colors: Do not use background and foreground colors in
            scene
        opt_show_capture_settings: Print settings from Capture Dialog only, DO
            NOT create image file(s)
        opt_renderer_renderer: Select renderer for drawing image: Name of
            renderer to use for drawing image
        opt_print_image_info: Print the size and other information about output
            images only and DO NOT create any output images
    Returns:
        NamedTuple of outputs (described in `SceneCaptureImageOutputs`).
    """
    execution = runner.start_execution(SCENE_CAPTURE_IMAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-capture-image")
    cargs.append(scene_file)
    cargs.append(scene_name_or_number)
    cargs.append(image_file_name)
    if opt_size_window:
        cargs.append("-size-window")
    if opt_size_capture:
        cargs.append("-size-capture")
    if opt_size_width_width is not None:
        cargs.extend(["-size-width", str(opt_size_width_width)])
    if opt_size_height_height is not None:
        cargs.extend(["-size-height", str(opt_size_height_height)])
    if opt_units_units is not None:
        cargs.extend(["-units", opt_units_units])
    if opt_margin_size is not None:
        cargs.extend(["-margin", str(opt_margin_size)])
    if opt_no_scene_colors:
        cargs.append("-no-scene-colors")
    if opt_show_capture_settings:
        cargs.append("-show-capture-settings")
    if opt_renderer_renderer is not None:
        cargs.extend(["-renderer", opt_renderer_renderer])
    if opt_print_image_info:
        cargs.append("-print-image-info")
    ret = SceneCaptureImageOutputs(
    )
    execution.run(cargs)
    return ret