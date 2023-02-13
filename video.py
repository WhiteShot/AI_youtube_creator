import os
import cv2
from PIL import Image

print(os.getcwd())

os.chdir("C:\\Users\\Mark\\PycharmProjects\\AI_youtube_creator\\imgs")
path = "C:\\Users\\Mark\\PycharmProjects\\AI_youtube_creator\\imgs"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height

mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        im = Image.open(os.path.join(path, file))

        width, height = im.size
        print(width, height)

        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
        imResize.save(file, 'PNG', quality=95)

        print(im.filename.split('\\')[-1], " is resized")


def generate_video(time=20):
    image_folder = "C:\\Users\\Mark\\PycharmProjects\\AI_youtube_creator\\imgs"
    video_name = 'mygeneratedvideo.mp4'
    os.chdir("C:\\Users\\Mark\\PycharmProjects\\AI_youtube_creator\\")

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]
    print('img : ', images[0])
    frame = cv2.imread('imgs/' + images[0])
    height, width, layers = frame.shape
    fps_d = len(images)/time
    print("video fps: ", fps_d)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, fps_d, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


generate_video()