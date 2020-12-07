import os
import os
import subprocess


# outputs the width, height, duration and bitrate of the video "10sbbb.mp4
def ex1(video):
    command = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,bit_rate -of " \
              "default=noprint_wrappers=1 {video}".format(video=video)
    subprocess.call(command, shell=True)


# renames different quality files using os.rename()
def ex2(video):
    rename = input("insert new name: ")
    os.rename(video, rename)


# this script avoids the problem of odd numbers for width/height inputs
def ex3(video):
    width = input("select new width (-1 if you want to keep the aspect ratio): ")
    height = input("select new height (-1 if you want to keep the aspect ratio): ")
    if height == "-1":
        height = "trunc(ow/a/2)*2"
    elif int(height) % 2 != 0:
        height = str(int(height) + 1)
    if width == "-1":
        width = "trunc(oh*a/2)*2"
    elif int(width) % 2 != 0:
        width = str(int(width) + 1)

    command = "ffmpeg -i {video} -filter:v scale=\"{width}:{height}\" out.mp4".format(video=video, width=width,
                                                                                      height=height)
    subprocess.call(command, shell=True)


def ex4(video):
    vcodec = input("insert video codec (\"copy\" to use input's codec): ")
    acodec = input("insert audio codec (\"copy\" to use input's codec): ")
    command = "ffmpeg -i {video} -c:v {vcodec} -c:a {acodec} out.mp4".format(video=video, vcodec=vcodec, acodec=acodec)
    subprocess.call(command, shell=True)


def ex5():
    while True:
        print("Select an option\n1. Parse video\n2. Rename video\n3. Resize video\n4. Transcript video with different "
              "codec\nElse. Get me the fuck outta here")
        option = input()
        if option == "1":
            video = input("insert video file: ")
            ex1(video)
        elif option == "2":
            video = input("insert video file: ")
            ex2(video)
        elif option == "3":
            video = input("insert video file: ")
            ex3(video)
        elif option == "4":
            video = input("insert video file: ")
            ex4(video)
        else:
            print("K bye")
            break


ex5()
