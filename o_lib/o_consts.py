import string

# TYPES - used for type hinting
OID = str 
TreeNode = tuple[OID, list["TreeNode"]]

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Darkening effect higher value = less darkening
DARKENING_FACTOR = 60

# Rendering distance
RENDER_DISTANCE_FAR = DARKENING_FACTOR
RENDER_DISTANCE_BEHIND = 0
RENDER_DISTANCE_RIGHT = 50
RENDER_DISTANCE_LEFT = -RENDER_DISTANCE_RIGHT

# Printing variables
VERBOSE = True
DEBUG = True

# IDs
VALID_OBJECT_ID_CHARS = string.ascii_letters + string.digits
OBJECT_ID_LEN = 10

split_whole_value = .1
SPLIT_PERCENT = split_whole_value / 100

PRIMITIVES_DIR = "./primitives"
ALL_MODELS_DIR = "./total_modles"