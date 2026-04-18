import os
def toWebp(filename, root = ""):
    parts = filename.split(".")
    newFilename = os.path.join(root, parts[0] + ".webp")
    return newFilename