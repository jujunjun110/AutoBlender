from re import T
import argparse
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


class ExecutionConfig:
    def __init__(self, filePath: str, angle_step: int, cam_distance: int):
        self.filePath = filePath
        self.angleStep = angle_step
        self.cam_distance = cam_distance

    @staticmethod
    def parseArgs():
        default_path = "./assets/default.fbx"
        default_angle_step = 90
        default_cam_distance = 10

        parser = argparse.ArgumentParser()

        parser.add_argument('--file', type=str,  required=False, help="path of fbx file")
        parser.add_argument('--angleStep', type=int,  required=False, help="angle step for rotation")
        parser.add_argument('--camDistance', type=int,  required=False, help="camera distance")

        args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:])

        angle_step = default_angle_step if args.angleStep is None else args.angleStep
        file_path = default_path if args.file is None else args.file
        cam_distance = default_cam_distance if args.camDistance is None else args.camDistance

        return ExecutionConfig(file_path, angle_step, cam_distance)


def main() -> None:

    cube = get_scene_object("Cube")
    if cube is not None:
        bpy.data.objects.remove(cube, do_unlink=True)

    config = ExecutionConfig.parseArgs()
    exec(config)

    os.makedirs("./result", exist_ok=True)
    bpy.ops.wm.save_mainfile(filepath="./result/created.blend")


def exec(execConfig: ExecutionConfig):
    bpy.ops.import_scene.fbx(filepath=execConfig.filePath)

    camera = get_scene_object("Camera")

    yaw_list = range(0, 360, execConfig.angleStep)
    pitch_list = range(0, 181, execConfig.angleStep)
    pairs = itertools.product(yaw_list, pitch_list)

    transforms = [calc_camera_transform(execConfig.cam_distance, pitch, yaw) for pitch, yaw in pairs]
    bpy.context.scene.render.film_transparent = True

    for index, transform in enumerate(transforms):
        print(f"\nX: {transform.alpha}, Y: {transform.beta} ({index + 1} / {len(transforms)})")
        render_with_angles(camera, transform)


def render_with_angles(camera, transform):
    camera.location = transform.pos_x, transform.pos_y, transform.pos_z
    camera.rotation_euler = transform.rot_x, transform.rot_y, transform.rot_z

    bpy.ops.render.render()

    dist = f"./rendered/res_x{transform.alpha}_y{transform.beta}.png"
    bpy.data.images['Render Result'].save_render(filepath=dist)


def calc_camera_transform(radius: float, alpha: float, beta: float) -> Transform:
    tmp_l = radius * math.sin(math.radians(beta))

    pos_x = tmp_l * math.cos(math.radians(alpha))
    pos_y = tmp_l * math.sin(math.radians(alpha))
    pos_z = radius * math.cos(math.radians(beta))

    return Transform(pos_x, pos_y, pos_z, math.radians(beta), 0, math.radians(90 + alpha), alpha, beta)


def get_scene_object(name: str) -> Optional[Object]:
    objects = cast(List[Object], bpy.context.scene.objects)
    candidates = [obj for obj in objects if obj.name == name]

    if len(candidates) == 0:
        return None

    return candidates[0]


if __name__ == "__main__":
    main()
