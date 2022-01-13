import sys
import bpy


def main():
    print(sys.version)
    path = "./assets/shoe.fbx"
    print(path)
    # print(bpy)
    bpy.ops.import_scene.fbx(filepath=path)

    scene = bpy.context.scene

    foo_objs = [obj for obj in scene.objects]

    for obj in foo_objs:
        print(obj)
        print(obj.name)


if __name__ == "__main__":
    main()
