import sys
import os
import bpy


def main():
    print(sys.version)
    path = "./assets/shoe.fbx"
    print(path)
    # print(bpy)
    bpy.ops.import_scene.fbx(filepath=path)

    camera = getCamera()
    print(camera)

    bpy.ops.render.render()

    dist = "./res.png"
    bpy.data.images['Render Result'].save_render(filepath=dist)


def getCamera():
    candidates = [
        obj for obj in bpy.context.scene.objects if obj.name == "Camera"]

    if len(candidates) == 0:
        return None

    return candidates[0]


if __name__ == "__main__":
    main()
