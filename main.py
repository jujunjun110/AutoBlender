import sys
import os
import math
import itertools
import bpy
from bpy.types import bpy_prop_collection, Object
from typing import Optional, cast, List


class Transform:
    def __init__(self, pos_x, pos_y, pos_z, rot_x, rot_y, rot_z, alpha, beta):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.rot_z = rot_z
        self.alpha = alpha
        self.beta = beta


def main() -> None:
    path = "./assets/shoe.fbx"

    cube = getSceneObject("Cube")
    if cube is not None:
        bpy.data.objects.remove(cube, do_unlink=True)

    bpy.ops.import_scene.fbx(filepath=path)

    camera = getSceneObject("Camera")

    yaw_list = range(0, 360, 60)
    pitch_list = range(0, 360, 60)
    pairs = itertools.product(yaw_list, pitch_list)

    radius = 10
    transforms = [calcTransform(radius, pitch, yaw) for pitch, yaw in pairs]

    for transform in transforms:
        print(
            f"POS(X: {transform.pos_x}, Y: {transform.pos_y}, Z: {transform.pos_z})")
        print(
            f"ROT(X: {transform.rot_x * 180}, Y: {transform.rot_y* 180}, Z: {transform.rot_z* 180})")
        camera.location = transform.pos_x, transform.pos_y, transform.pos_z
        camera.rotation_euler = transform.rot_x, transform.rot_y, transform.rot_z

        bpy.ops.render.render()

        dist = f"./rendered/res_x{transform.alpha}_y{transform.beta}.png"
        bpy.data.images['Render Result'].save_render(filepath=dist)

    bpy.ops.wm.save_mainfile(filepath="./result/created.blend")


def calcTransform(radius: float, alpha: float, beta: float) -> Transform:
    pos_z = radius * math.cos(math.radians(beta))
    tmp_l = radius * math.sin(math.radians(beta))
    pos_x = tmp_l * math.cos(math.radians(alpha))
    pos_y = tmp_l * math.sin(math.radians(alpha))

    return Transform(pos_x, pos_y, pos_z, math.radians(beta), 0, math.radians(90 + alpha), alpha, beta)


def getSceneObject(name: str) -> Optional[Object]:
    objects = cast(List[Object], bpy.context.scene.objects)
    candidates = [obj for obj in objects if obj.name == name]
    # candidates = [obj for obj in bpy.context.scene.objects if obj.name == name]

    if len(candidates) == 0:
        return None

    return candidates[0]


if __name__ == "__main__":
    main()
