from PIL import Image, ImageDraw

from point import Point


class Renderer:

    def __init__(self):
        self.w = 200
        self.h = 200
        self.p_w = 20
        self.p_h = 20
        pass

    def render_boxes(self, boxes):
        im = Image.new('RGB', (self.screen_width, self.screen_height), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        for box in boxes:
            self._render_box(box, draw)

        for box in boxes:
            self._render_points(box.points, draw)

        im.show()

    def _render_box(self, box, draw):
        print(box.x, box.y)

        start_x = box.x * self.w
        start_y = box.y * self.h

        shape = [(start_x, start_y), (end_x, end_y)]

        draw.rectangle(shape, fill=(box.color.r, box.color.g, box.color.b))

    def _get_center(self, x, y):
        return Point((self.screen_width / 2) + (x * self.position_ratio),
                     (self.screen_height / 2) + (y * self.position_ratio))
