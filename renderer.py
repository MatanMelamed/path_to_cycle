from PIL import Image, ImageDraw


class Renderer:

    def __init__(self):
        self.w = 200
        self.h = 200
        self.p_w = 20
        self.p_h = 20
        pass

    def render_boxes(self, boxes):
        im = Image.new('RGB', (1000, 1000), (255, 255, 255))
        draw = ImageDraw.Draw(im)

        for box in boxes:
            self._render_box(box, draw)

        for box in boxes:
            self._render_points(box.points, draw)

        im.show()

    def _point_idx_to_pixels(self, point):
        return [(point.x * (self.w / 2)) + self.w / 4,
                (point.y * (self.h / 2)) + self.h / 4]

    def _render_box(self, box, draw):
        print(box.x, box.y)

        start_x = box.x * self.w
        start_y = box.y * self.h

        shape = [(start_x, start_y),
                 (start_x + self.w, start_y + self.h)]

        draw.rectangle(shape, fill=(0, 100, 100), outline=(0, 0, 0), width=5)

        draw.line((start_x + self.w / 2, start_y,
                   start_x + self.w / 2, start_y + self.h),
                  fill=(0, 0, 0),
                  width=1)

        draw.line((start_x, start_y + self.h / 2,
                   start_x + self.w, start_y + self.h / 2),
                  fill=(0, 0, 0),
                  width=1)

    def _render_points(self, points, draw):
        for point in points:
            start_x, start_y = self._point_idx_to_pixels(point)

            shape = [start_x - (self.p_w / 2), start_y - (self.p_h / 2),
                     start_x + (self.p_w / 2), start_y + (self.p_h / 2)]
            draw.ellipse(shape, fill=(200, 0, 0))

            self._render_point_connections(point, draw)

    def _render_point_connections(self, point, draw):
        for connection in point.connections:
            point_x, point_y = self._point_idx_to_pixels(point)
            conn_x, conn_y = self._point_idx_to_pixels(connection)
            draw.line([point_x, point_y, conn_x, conn_y], width=1, fill=(100, 0, 0))
