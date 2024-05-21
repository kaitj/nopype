# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


ATROPOS_METADATA = Metadata(
    id="a3fe198eae3a480d2f2de7ff2c29bb1679f296c5",
    name="Atropos",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AtroposOutputs(typing.NamedTuple):
    """
    Output object returned when calling `atropos(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    classified_image: OutputPathType
    """No description provided."""
    posteriors: OutputPathType
    """A list of items which are file. No description provided."""


def atropos(
    runner: Runner,
    initialization: typing.Literal["Random", "Otsu", "KMeans", "PriorProbabilityImages", "PriorLabelImage"],
    intensity_images: list[InputPathType],
    mask_image: InputPathType,
    number_of_tissue_classes: int,
    convergence_threshold: float | int | None = None,
    dimension: typing.Literal[3, 2, 4] | None = 3,
    kmeans_init_centers: list[float | int] = None,
    likelihood_model: str | None = None,
    maximum_number_of_icm_terations: int | None = None,
    mrf_radius: list[int] = None,
    mrf_smoothing_factor: float | int | None = None,
    n_iterations: int | None = None,
    num_threads: int | None = 1,
    out_classified_image_name: InputPathType | None = None,
    output_posteriors_name_template: str | None = "POSTERIOR_%02d.nii.gz",
    posterior_formulation: str | None = None,
    prior_image: InputPathType | None = None,
    prior_image_2: str | None = None,
    prior_probability_threshold: float | int | None = None,
    prior_weighting: float | int | None = None,
    save_posteriors: bool = False,
    use_mixture_model_proportions: bool = False,
    use_random_seed: bool = True,
) -> AtroposOutputs:
    """
    Atropos by Nipype (interface).
    
    
    A multivariate n-class segmentation algorithm.
    A finite mixture modeling (FMM) segmentation approach with possibilities for
    specifying prior constraints. These prior constraints include the
    specification of a prior label image, prior probability images (one for each
    class), and/or an MRF prior to enforce spatial smoothing of the labels.
    Similar algorithms include FAST and SPM.
    
    Args:
        runner: Command runner
        initialization: 'random' or 'otsu' or 'kmeans' or
            'priorprobabilityimages' or 'priorlabelimage'. No description provided.
        intensity_images: No description provided.
        mask_image: No description provided.
        number_of_tissue_classes: No description provided.
        convergence_threshold: No description provided.
        dimension: 3 or 2 or 4. Image dimension (2, 3, or 4).
        kmeans_init_centers: No description provided.
        likelihood_model: No description provided.
        maximum_number_of_icm_terations: No description provided.
        mrf_radius: A list of items which are an integer. No description
            provided.
        mrf_smoothing_factor: No description provided.
        n_iterations: No description provided.
        num_threads: Number of itk threads to use.
        out_classified_image_name: No description provided.
        output_posteriors_name_template: No description provided.
        posterior_formulation: No description provided.
        prior_image: file or string or a string. Either a string pattern (e.g.,
            'prior%02d.nii') or an existing vector-image file.
        prior_image_2: file or string or a string. Either a string pattern
            (e.g., 'prior%02d.nii') or an existing vector-image file.
        prior_probability_threshold: No description provided.
        prior_weighting: No description provided.
        save_posteriors: No description provided.
        use_mixture_model_proportions: No description provided.
        use_random_seed: Use random seed value over constant.
    Returns:
        NamedTuple of outputs (described in `AtroposOutputs`).
    """
    if kmeans_init_centers is not None and not (1 <= len(kmeans_init_centers)): 
        raise ValueError(f"Length of 'kmeans_init_centers' must be greater than 1 but was {len(kmeans_init_centers)}")
    if (
        (prior_image is not None) +
        (prior_image_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "prior_image,\n"
            "prior_image_2"
        )
    execution = runner.start_execution(ATROPOS_METADATA)
    cargs = []
    cargs.append("Atropos")
    if convergence_threshold is not None:
        cargs.append(str(convergence_threshold))
    if dimension is not None:
        cargs.extend(["--image-dimensionality", str(dimension)])
    cargs.append("[ICM_USE_SYNCHRONOUS_UPDATE]")
    cargs.append(initialization)
    cargs.extend(["--intensity-image", *[execution.input_file(f) for f in intensity_images]])
    if kmeans_init_centers is not None:
        cargs.extend(map(str, kmeans_init_centers))
    if likelihood_model is not None:
        cargs.extend(["--likelihood-model", likelihood_model])
    cargs.extend(["--mask-image", execution.input_file(mask_image)])
    if maximum_number_of_icm_terations is not None:
        cargs.append(str(maximum_number_of_icm_terations))
    if mrf_radius is not None:
        cargs.extend(map(str, mrf_radius))
    if mrf_smoothing_factor is not None:
        cargs.append(str(mrf_smoothing_factor))
    if n_iterations is not None:
        cargs.append(str(n_iterations))
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append(str(number_of_tissue_classes))
    if out_classified_image_name is not None:
        cargs.append(execution.input_file(out_classified_image_name))
    if output_posteriors_name_template is not None:
        cargs.append(output_posteriors_name_template)
    if posterior_formulation is not None:
        cargs.append(posterior_formulation)
    if prior_image_2 is not None:
        cargs.append(prior_image_2)
    if prior_probability_threshold is not None:
        cargs.append(str(prior_probability_threshold))
    if prior_weighting is not None:
        cargs.append(str(prior_weighting))
    if save_posteriors:
        cargs.append("--save_posteriors")
    if use_mixture_model_proportions:
        cargs.append("--use_mixture_model_proportions")
    if use_random_seed:
        cargs.append("--use-random-seed")
    ret = AtroposOutputs(
        root=execution.output_file("."),
        classified_image=execution.output_file(f"classified_image", optional=True),
        posteriors=execution.output_file(f"posteriors", optional=True),
    )
    execution.run(cargs)
    return ret
