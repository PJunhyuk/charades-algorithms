def read_videoid_csv():
    video_id_list = []

    # read csv file
    f = open('./Charades_v1_train.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if line[0] != 'id':
            video_id_list.append(line[0])
    f.close()

    return video_id_list


def read_actionlist_csv(video_id):
    action_list_time = []

    # read csv file
    f = open('./Charades_v1_train.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if line[0] == video_id:
            if line[9] == '':
                action_list_time = []
            else:
                action_list = line[9].split(';')
                for action in action_list:
                    action_time = action.split(' ')
                    action_time[1] = int(float(action_time[1]) * video_fps)
                    action_time[2] = int(float(action_time[2]) * video_fps)
                    action_list_time.append(action_time)
    f.close()

    return action_list_time


def read_data_text():
    # generate class_list from text file
    class_list = {}

    ## read text file
    f = open('./Charades_v1_classes.txt', 'r')
    while True:
        line = f.readline()
        class_id = line.split(' ')[0]
        class_description = line[5:].strip('\n')
        class_list[class_id] = class_description
        if not line: break
    f.close()

    return class_list


def save_video(video_id):
    dir_path = root_path + '/' + video_id

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

    out.release()
    # cv2.destoryAllWindows()


def show_video(video_id):
    dir_path = root_path + '/' + video_id

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

        cv2.imshow(video_id, frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

    # cv2.destoryAllWindows()


if __name__ == "__main__":
    # Import the required modules

    ## Check time required
    import time
    time_start = time.time()

    import cv2
    import argparse
    import os
    import csv

    # argument parser
    ap = argparse.ArgumentParser()
    ap.add_argument("-path", "--rootpath", default = "D:/workspace-dataset/charades/Charades_v1_rgb")
    ap.add_argument("-id", "--id", default="00HFP")
    ap.add_argument("-s", "--save", default="False")

    # parse the arguments
    args = vars(ap.parse_args())
    video_id = args['id']
    root_path = args['rootpath']
    is_save = args['save']

    target_path = 'D:/workspace-dataset/charades/Charades_v1_with_actions'

    video_fps = 24

    video_id_list = read_videoid_csv()
    class_list = read_data_text()

    if video_id == "all":
        for i, id in enumerate(video_id_list):
            action_list_time = read_actionlist_csv(id)
            save_video(id)
            print("saving " + id + " (" + str(i+1) + ", " + str(len(video_id_list)) + ") ... " + "total " + str(time.time() - time_start)[:4] + "sec spent..")
    else:
        action_list_time = read_actionlist_csv(video_id)
        if is_save == "True":
            save_video(video_id)
        else:
            show_video(video_id)

    print("Time(s): " + str(time.time() - time_start))
