import os
import os
import subprocess


def ex1(video, output):
    command = "ffmpeg -ss 00:00:00 -i {video} -to 00:00:10 -c copy {output}".format(video=video, output=output)
    subprocess.call(command, shell=True)


def ex2(video, output):
    command = "ffmpeg -i {video} -vf \"split=2[a][b], [b]histogram, format=yuva444p[hh],[a][hh]overlay\" {output}".format(
        video=video, output=output)
    subprocess.call(command, shell=True)


def ex3(video, output1, output2, output3, output4):
    command1 = "ffmpeg -i {video} -s 1280x720 -c:a copy {output}".format(video=video, output=output1)
    command2 = "ffmpeg -i {video} -s 680x480 -c:a copy {output}".format(video=video, output=output2)
    command3 = "ffmpeg -i {video} -s 360x240 -c:a copy {output}".format(video=video, output=output3)
    command4 = "ffmpeg -i {video} -s 160x120 -c:a copy {output}".format(video=video, output=output4)
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)
    subprocess.call(command3, shell=True)
    subprocess.call(command4, shell=True)


def ex4(video, output):
    command = "ffmpeg -i {video} -ac 1 -acodec mp3 -vcodec copy {output}".format(video=video, output=output)
    subprocess.call(command, shell=True)


ex1("bbb.mp4","10sbbb.mp4")
ex2("10sbbb.mp4","yuvbbb.mp4")
ex3("10sbbb.mp4","10sbbb720p.mp4","10sbbb480p.mp4","10sbbb360p.mp4","10sbbb160p.mp4")
ex4("10sbbb.mp4","10sbbbmono.mp4")