from box import Box, PLocation
from renderer import Renderer


def connect_adjacent_boxes(box1, box2):
    # relative to second box location

    # box2 above box1
    if box2.y > box1.y:
        box1.points[PLocation.TOP_LEFT.value].connect_to(box2.points[PLocation.BOT_LEFT.value])
        box1.points[PLocation.TOP_RIGHT.value].connect_to(box2.points[PLocation.BOT_RIGHT.value])

    # box2 below box1
    elif box2.y < box1.y:
        box2.points[PLocation.TOP_LEFT.value].connect_to(box1.points[PLocation.BOT_LEFT.value])
        box2.points[PLocation.TOP_RIGHT.value].connect_to(box1.points[PLocation.BOT_RIGHT.value])

    # box2 right to box1
    elif box2.x > box1.x:
        box1.points[PLocation.TOP_RIGHT.value].connect_to(box2.points[PLocation.TOP_LEFT.value])
        box1.points[PLocation.BOT_RIGHT.value].connect_to(box2.points[PLocation.BOT_LEFT.value])

    # box2 left to box1
    elif box2.x < box1.x:
        box2.points[PLocation.TOP_RIGHT.value].connect_to(box1.points[PLocation.TOP_LEFT.value])
        box2.points[PLocation.BOT_RIGHT.value].connect_to(box1.points[PLocation.BOT_LEFT.value])


def get_linked_boxes_of_point(point):
    boxes = []

    for connection in point.connections:
        if point.get_box_index() != connection.get_box_index():
            boxes.append(connection.get_box_index())

    return boxes


def are_points_connected_to_the_same_box(point1, point2):
    point2_linked_boxes = get_linked_boxes_of_point(point2)
    point1_linked_boxes = get_linked_boxes_of_point(point1)

    for box in point1_linked_boxes:
        if box in point2_linked_boxes:
            return True

    return False


def connect_remaining_points(box):
    p0 = box.points[PLocation.BOT_LEFT.value]
    p1 = box.points[PLocation.BOT_RIGHT.value]
    p2 = box.points[PLocation.TOP_LEFT.value]
    p3 = box.points[PLocation.TOP_RIGHT.value]

    link_options = [(p0, [p1, p2]),
                    (p1, [p3]),
                    (p2, [p3])]

    for option in link_options:

        current_point = option[0]

        while len(current_point.connections) < 2:
            for optional_point in option[1]:
                if not current_point.is_connected_to(optional_point) \
                        and len(optional_point.connections) < 2 \
                        and not are_points_connected_to_the_same_box(current_point, optional_point):
                    current_point.connect_to(optional_point)
                    break


def connect_boxes(boxes):
    for i in range(len(boxes) - 1):
        connect_adjacent_boxes(boxes[i], boxes[i + 1])
        connect_remaining_points(boxes[i])

    # connect remaining points in last box
    connect_remaining_points(boxes[len(boxes) - 1])


if __name__ == '__main__':
    # arr = [Box(0, 0), Box(10, 10), Box(10, -10), Box(-10, 10), Box(-10, -10)]
    arr = [Box(0, 0, Color(100, 30, 30))]

    for _ in range(10):
        arr.append(Box(*(random.randint(-10, 10) for i in range(2))))

    print(len(arr))

    renderer = Renderer(1000, 1000, 30, 30)
    renderer.render_boxes(arr)
