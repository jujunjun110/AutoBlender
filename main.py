import sys
import os
import bpy


def main():
    path = "./assets/shoe.fbx"

    cube = getSceneObject("Cube")
    if cube is not None:
        bpy.data.objects.remove(cube, do_unlink=True)

    bpy.ops.import_scene.fbx(filepath=path)
    bpy.ops.render.render()

    dist = "./res.png"
    bpy.data.images['Render Result'].save_render(filepath=dist)

    bpy.ops.wm.save_mainfile(filepath="./created.blend")


def getSceneObject(name: str):
    candidates = [
        obj for obj in bpy.context.scene.objects if obj.name == name]

    if len(candidates) == 0:
        return None

    return candidates[0]


if __name__ == "__main__":
    main()
