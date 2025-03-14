from dataclasses import dataclass


import o_lib.o_math
from o_lib.o_math import Vertex2, Vertex3
from o_lib.o_component import Component

class EngineObject:
    name: str

    # NOTE: str is the component_type, and then it has a list to allow for multiple components of the same type
    components: dict[str, list[Component]]


    def __init__(self, name: str):
        self.name = name
        self.components = {}


    def add_component(self, component: Component):
        if component.component_type not in self.components:
            self.components[component.component_type] = []
        
        self.components[component.component_type].append(component)


    def remove_component(self, component_type: str, component_i: int = 0) -> bool:
        if component_type not in self.components:
            return False
        if len(self.components[component_type]) >= component_i:
            return False        

        del self.components[component_type][component_i]

        if len(self.components[component_type]) == 0:
            del self.components[component_type]
        return True


    def remove_components(self, component_type: str) -> bool:
        if component_type not in self.components:
            return False
        
        del self.components[component_type]
        return True


    def get_component(self, component_type: str) -> Component | None:
        if component_type not in self.components:
            return None
        
        return self.components[component_type][0]
    

    def get_components(self, component_type: str) -> list[Component] | None:
        if component_type not in self.components:
            return None
        
        return self.components[component_type]
    

    def save_as_prefab(self):
        pass # TODO


def load_object_prefab(self, path: str):
    pass # TODO


# TODO: Unit Tests
        
