import sys
import bpy

def main():
    print(sys.version)
    path = "./assets/shoe.fbx"
    print(path)
    print(bpy)
    bpy.ops.import_scene.fbx(filepath=path)



if __name__ == "__main__":
    main()
