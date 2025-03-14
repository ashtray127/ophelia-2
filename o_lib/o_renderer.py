from typing import Generator

import o_math
import o_consts
from o_math import Vertex2, Vertex3, BoundingBox
from o_util import debug_print, verbose_print

class RendererComponent:

    model_name: str
    vertices: list[Vertex3]
    edges: list[tuple[int, int]]
    faces: list[tuple[tuple[int, int, int, int], tuple[int, int, int]]]
    pivot: Vertex3

    render: bool

    def __init__(self, 
                 vertices: list[Vertex3],
                 edges: list[tuple[int, int]],
                 faces: list[tuple[tuple[int, int, int, int], tuple[int, int, int]]],
                 pivot: Vertex3):
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.pivot = pivot

    @property
    def bounding_box(self) -> BoundingBox:
        return o_math.calculate_bounding_box(self.vertices)


    @property
    def split_object_each_face(self) -> Generator[tuple[list[Vertex3], BoundingBox]]:
        split_objects_each_faces = []

        for face in self.faces:
            vertices_indices, color = face
            face_vertices = [self.vertices[i] for i in vertices_indices]
            bounding_box = o_math.calculate_bounding_box(face_vertices)
            
            split_objects_each_faces.append((face_vertices, bounding_box))

            yield face_vertices, bounding_box
        # TODO: figure out if the return is needed or if the yield does it for you
        #return split_objects_each_faces


    @property
    def split_objects_smaller_percent(self) -> Generator[tuple[list[Vertex3], BoundingBox]]:
        
        split_objects_each_faces: list[tuple[list[Vertex3], BoundingBox]] = []
        num_faces = len(self.faces)
        split_count = int(num_faces * o_consts.SPLIT_PERCENT)

        verbose_print(f"Splitting {self.model_name} into {split_count} smaller objects")

        for big_face in range(split_count):

            vertices_indices, color = self.faces[big_face]
            vertices: list[Vertex3] = [self.vertices[i] for i in vertices_indices]
            bounding_box = o_math.calculate_bounding_box(vertices)

            split_objects_each_faces.append((vertices, bounding_box))

            yield vertices, bounding_box

        
        if o_consts.VERBOSE: # NOTE: this is to increase performance if this information is unneeded
            verbose_print(f"Each bounding box is: ")
            for vertices, bounding_box in split_objects_each_faces:
                verbose_print(f"{bounding_box}")

        # TODO: figure out if the return is needed or if the yield does it for you
        #return split_objects_each_faces


    def scale(self, scale: float):
        for vertex in self.vertices:
            vertex.scale(scale, scale, scale)


    def save_model_to_disk(self):
        pass
        # TODO: implement
    


