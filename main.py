import sys
import os
import bpy
from bpy.types import bpy_prop_collection, Object
from typing import Optional, cast, List



def main()->None:
    path = "./assets/shoe.fbx"

    cube = getSceneObject("Cube")
    if cube is not None:
        bpy.data.objects.remove(cube, do_unlink=True)

    bpy.ops.import_scene.fbx(filepath=path)

    bpy.ops.render.render()

    dist = "./rendered/res.png"
    bpy.data.images['Render Result'].save_render(filepath=dist)

    bpy.ops.wm.save_mainfile(filepath="./result/created.blend")


def getSceneObject(name: str) -> Optional[Object]:
    objects =cast(List[Object], bpy.context.scene.objects)
    candidates = [ obj for obj in objects if obj.name == name]

    if len(candidates) == 0:
        return None

    return candidates[0]


if __name__ == "__main__":
    main()
