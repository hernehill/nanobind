name = "nanobind"

version = "3.1.0.hh.1.0.0"

authors = [
    "AndoTwin Studio",
]

description = """tiny and efficient C++/Python bindings"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "eigen",
]

private_build_requires = []

variants = [
    ["python-3.10", "typing_extensions"],  # 3.10 is the minimum Python version
    ["python-3.11"],
    ["python-3.13"],
]

# NOTE: Remember to run git submodule update --init --recursive


def commands():
    env.REZ_NANOBIND_ROOT = "{root}"
    env.NANOBIND_ROOT_DIR = "{root}"
    env.NANOBIND_ROOT = "{root}"
    env.nanobind_ROOT = "{root}"
    env.nanobind_DIR = "{root}/nanobind/cmake"


uuid = "repository.nanobind"
