import sys
sys.path.insert(0,".")
from helpers import toWebp

def test_toWebp():
    filename = "test_method_webp.png"
    new_filename = toWebp(filename)
    assert new_filename == "test_method_webp.webp"