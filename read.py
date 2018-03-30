import cv2
import argparse
import os

import csv

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-id", "--id", default="00HFP")

root_path = 'D:/workspace-dataset/charades/Charades_v1_rgb'
target_path = 'D:/workspace-dataset/charades/Charades_v1_labeling'

# parse the arguments
args = vars(ap.parse_args())
video_id = args['id']

dir_path = root_path + '/' + video_id
video_fps = 24

# read images, save their name as list
image_name_list = []
for f in os.listdir(dir_path):
    if f.endswith('jpg'):
        image_name_list.append(f)

# determine the height, width, channels from the first image
image_path = os.path.join(dir_path, image_name_list[0])
frame = cv2.imread(image_path)
# cv2.imshow('video', frame)
height, width, channels = frame.shape

# define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
if not os.path.exists(target_path):
    os.makedirs(target_path)
out = cv2.VideoWriter(target_path + '/' + video_id + '_action.avi', fourcc, video_fps, (width, height))

action_list_time = []

# read csv file
f = open('./Charades_v1_train.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    if line[0] == video_id:
        action_list = line[9].split(';')
        for action in action_list:
            action_time = action.split(' ')
            action_time[1] = int(float(action_time[1]) * video_fps)
            action_time[2] = int(float(action_time[2]) * video_fps)
            action_list_time.append(action_time)
f.close()

# generate class_list from text file
class_list = {}

## read text file
f = open('./Charades_v1_classes.txt', 'r')
while True:
    line = f.readline()
    list_temp = []
    class_id = line.split(' ')[0]
    class_description = line[5:].strip('\n')
    class_list[class_id] = class_description
    if not line: break
f.close()

font = cv2.FONT_HERSHEY_SIMPLEX

frame_index = 1
for image_name in image_name_list:
    frame_index = frame_index + 1
    image_path = os.path.join(dir_path, image_name)
    frame = cv2.imread(image_path)

    cv2.putText(frame, str(frame_index) + '/' + str(len(image_name_list)), (10, 20), font, 0.5, (255,255,255), 1, cv2.LINE_AA)

    action_i = 0
    for action_time in action_list_time:
        if frame_index in range(action_time[1], action_time[2]):
            action_i = action_i + 1
            cv2.putText(frame, class_list[action_time[0]], (10, 20 + action_i * 20), font, 0.5, (255,255,255), 1, cv2.LINE_AA)

    out.write(frame)

    cv2.imshow(video_id, frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

out.release()
# cv2.destoryAllWindows()
