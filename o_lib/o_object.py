from dataclasses import dataclass

from o_lib.o_renderer import RendererComponent
import o_math
from o_math import Vertex2, Vertex3

class EngineObject:
    position: Vertex3
    components: list[RendererComponent]

    def __init__(self):
        self.components = []
        self.
        

        
