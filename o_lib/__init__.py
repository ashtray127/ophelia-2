"""
    This allows for importing the whole folder with all the components named better
    ex.
        import o_lib
        o_lib.object.whatever()
    instead of
        import o_lib
        o_lib.o_object.whatever()

    (this file is what is called on import)
"""
# ---- LIBRARIES
import o_lib.o_input as input
import o_lib.o_model as model
import o_lib.o_object as object
import o_lib.o_math as math
import o_lib.o_util as util
import o_lib.o_consts as consts
import o_lib.o_component as component
import o_lib.o_camera as camera
import o_lib.o_tree as tree

from o_lib.o_math import Vertex2, Vertex3


# ---- COMPONENTS
import o_lib.components.o_renderer as renderer