"""

Metric units:
seconds
kilograms
meters
"""

import pygame as pg
import pymunk as pm
import pymunk.pygame_util


pg.init()


SIZE = 1280, 720

FPS = 60

CAPTION = "Simulator"

dt = 1 / FPS

display = pg.display.set_mode(SIZE)

pg.display.set_caption(CAPTION)
camera_position = pg.Vector2()

space = pm.Space()
debug_draw_options = pm.pygame_util.DrawOptions(display)

space.gravity = 0, 9.8

density = 1000

rocket = pm.Body()
rocket_shape = pm.Poly.create_box(rocket, (50, 100), 5)
rocket_shape.density = density
space.add(rocket, rocket_shape)

ground = pm.Body(body_type=pm.Body.STATIC)
ground_y = 200
ground_shape = pm.Segment(ground, (-3000, ground_y), (3000, ground_y), 100)
space.add(ground, ground_shape)


def main() -> None:
    clock = pg.Clock()
    time = 0.0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        space.step(dt)
        display.fill((0, 0, 0))
        offset = (SIZE[0] / 2, SIZE[1] / 2) - camera_position
        debug_draw_options.transform = pm.Transform.translation(offset[0], offset[1])
        space.debug_draw(debug_draw_options)
        pg.display.update()
        frame = clock.tick(FPS) / 1000
        time += frame


if __name__ == "__main__":
    main()
