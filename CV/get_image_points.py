import cv2
import argparse


def get_coordinates(original, ):
    coordinates = []

    def onMouse(event, x, y, flags, ustc):
        if event == 1:
            coordinates.append((x, y))
            cv2.circle(original, (x, y), 3, color=(255, 255, 0), thickness=2)
            print(x, y)

    cv2.namedWindow('test')
    cv2.setMouseCallback('test', onMouse, 0)
    cv2.imshow('test', original)
    cv2.waitKey(0)
    return coordinates


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image', default='./frame.png', type=str, help="the image path", )
    # parser.add_argument('image', type=str, help="the image path")
    args = parser.parse_args()

    print(args.image)
    image = cv2.imread(args.image)
    print(image.shape)
    x = get_coordinates(image)
    print(x)

