
from o_math import Vertex2, Vertex3
from o_component import Component

class Transform(Component):

    component_type = "Transform"

    position: Vertex3
    rotation: Vertex3 # NOTE: may not be needed?
    scale:    Vertex3 # NOTE: may not be needed?

    def __init__(self):
        pass