## \package PSEv1.variant
# classes representing the variant class to facilitate box_resize

import hoomd

from . import _PSEv1
from . import shear_function

## Variant class holding a functional form of shear field
# Used as an argument for box_resize class to deform the box
class shear_variant(hoomd.variant._variant):
    ## Specify shear field represented by a function form with a limited timesteps
    #
    # \param function_form the functional form of the sinusoidal shear
    # \param total_timestep the total timesteps of the shear, equal to shear_end_timestep - shear_start_timestep, must be positive
    # \param max_strain the maximum absolute value of the strain, use 0.5 in almost all the cases
    def __init__(self, function_form, total_timestep, max_strain = 0.5):

        # initialize the base class
        super(shear_variant, self).__init__()

	# check total_timestep is positive
        if total_timestep <= 0:
            hoomd.context.msg.error("Cannot create a shear_variant with 0 or negative points\n")
            raise RuntimeError('Error creating variant')

        # create the c++ mirror class
        self.cpp_variant = _PSEv1.VariantShearFunction(function_form.cpp_function, int(total_timestep), -max_strain, max_strain)
