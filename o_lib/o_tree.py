"""
    Managing the tree of objects
"""
import random

from o_lib.o_util import verbose_print
from o_lib.o_object import EngineObject
from o_lib.o_consts import VALID_OBJECT_ID_CHARS, OBJECT_ID_LEN, OID, TreeNode
from o_lib.o_math import Vertex2, Vertex3


def gen_object_id() -> OID:
    return "".join(random.choice(VALID_OBJECT_ID_CHARS) for _ in range(OBJECT_ID_LEN))

def gen_unique_object_id(tree: "EngineTree") -> OID:
    while (new_id := gen_object_id()) in tree.objects.keys():
        pass # Loops, re-generating the OID every time until it's unique
    return new_id

class EngineTree: # NOTE: A singleton class
    """
        Singleton class where it stores the tree/hierarchy of objects.
        Singleton just means there (should) only be 1 instance of it globally
    """

    _the_instance: "EngineTree | None" = None
    @staticmethod
    def get_instance() -> "EngineTree":
        if EngineTree._the_instance is None:
            verbose_print("Creating the EngineTree instance...")
            EngineTree._the_instance = EngineTree()
        return EngineTree._the_instance
    
    # ----------------------------------------------------

    tree_data: TreeNode
    objects: dict[OID, EngineObject]

    def __init__(self):
        self.tree_data = ( "ROOT", [] )
    
    def get_position(self, position: list[int]):
        pass


    def check_position(self, position: list[int]):
        pass

    
    def append_child(self, position: Vertex2, )

    

EngineTree.get_instance()