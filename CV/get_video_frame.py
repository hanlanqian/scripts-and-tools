from unittest import main
import cv2
import argparse




def getFrameFromVideo(video_path, save_path):
    cam = cv2.VideoCapture(video_path)
    while True:
        flag, frame = cam.read()
        if not flag:
            print("no frame grab")
            return None

        else:
            cv2.imshow('display', frame)
            if cv2.waitKey(15)&0xff == 27:
                cv2.imwrite(save_path, frame)
                cam.release()
                cv2.destroyAllWindows()
                return frame



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video",)
    parser.add_argument("savePath",)
    args = parser.parse_args()
    print(args)

    frame = getFrameFromVideo(args.video, args.savePath)