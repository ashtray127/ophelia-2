# -----------------------------------------------------
#                        TYPES
# -----------------------------------------------------

BoundingBox = tuple[tuple[float, float], tuple[float, float], tuple[float, float]]

# -----------------------------------------------------
#                        VERTEXES
# -----------------------------------------------------
class Vertex2:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def pair(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    
    def offset(self, x: float, y: float) -> "Vertex2":
        self.x += x
        self.y += y
        return self
    

    def scale(self, x: float, y: float) -> "Vertex2":
        self.x *= x
        self.y *= y
        return self
    

    def copy_scale(self, x: float, y: float) -> "Vertex2":
        return Vertex2(self.x * x, self.y * y)


    def copy(self) -> "Vertex2":
        return Vertex2(self.x, self.y)
    

    def copy_offset(self, x: float, y: float) -> "Vertex2":
        return Vertex2(self.x + x, self.y + y)
    

class Vertex3:

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @property
    def pair(self) ->  tuple[float, float, float]:
        return (self.x, self.y, self.z)
    

    def offset(self, x: float, y: float, z: float) -> "Vertex3":
        self.x += x
        self.y += y
        self.z += z
        return self
    

    def copy(self) -> "Vertex3":
        return Vertex3(self.x, self.y, self.z)
    

    def scale(self, x: float, y: float, z: float) -> "Vertex3":
        self.x *= x
        self.y *= y
        self.z *= z
        return self
    

    def copy_scale(self, x: float, y: float, z: float) -> "Vertex3":
        return Vertex3(self.x * x, self.y * y, self.z * z)


    def copy_offset(self, x: float, y: float, z: float):
        return Vertex3(self.x + x, self.y + y, self.z + z)
    
    
# ----------------------------------------------------------
#                           MISC
# ----------------------------------------------------------
def calculate_bounding_box(vertices: list[Vertex3]) -> BoundingBox:
    min_x = min(v.x for v in vertices)
    max_x = max(v.x for v in vertices)
    min_y = min(v.y for v in vertices)
    max_y = max(v.y for v in vertices)
    min_z = min(v.z for v in vertices)
    max_z = max(v.z for v in vertices)
    return (min_x, max_x), (min_y, max_y), (min_z, max_z)