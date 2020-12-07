import os
import subprocess


def ex1_2(video, output1, output2, wave1, wave2, subtitles, output3):
    # cut
    command1 = "ffmpeg -ss 00:00:00 -i {video} -to 00:01:00 -c copy {output}".format(video=video, output=output)
    # extract audio mono
    command2 = "ffmpeg -i {video} -ac 1 {output}".format(video=output1, output=wave1)
    # bitrate
    command3 = "ffmpeg -i {input} -b:a 64k {output}".format(input=wave1, output=wave2)
    # subtitles
    command4 = "ffmpeg -i {subtitles} subtitles.ass".format(subtitles=subtitles)
    command5 = "ffmpeg -i {input} -vf ass=subtitles.ass {output}".format(input=output1, output=output2)
    # assemble
    command6 = "ffmpeg -i {input} -i {wave} -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac {output}".format(
        input=output2, wave=wave2, output=output3)
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)
    subprocess.call(command3, shell=True)
    subprocess.call(command4, shell=True)
    subprocess.call(command5, shell=True)
    subprocess.call(command6, shell=True)


def ex3(input):
    # using ffprobe like in previous lab
    command1 = "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {video}".format(
        video=input)
    command2 = "ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nokey=1:noprint_wrappers=1 {video}".format(
        video=input)

    acodec = subprocess.getoutput(command2)
    vcodec = subprocess.getoutput(command1)

    if vcodec == "mpeg2" or "h264":
        if acodec == "mp3":
            standard = "DVB, DTMB"
        elif acodec == "aac":
            standard = "DVB, ISDB, DTMB"
        elif acodec == "ac-3":
            standard = "DVB, ATSC, DTMB"
        elif acodec == "mp2" or "dra":
            standard = "DTMB"
        else:
            standard = "Non existing broadcasting standard"
    elif (vcodec == "avs" or "avs+") and (acodec == "aac" or "ac-3" or "mp2" or "mp3" or "dra"):
        standard = "DTMB"
    else:
        standard = "Non existing broadcasting standard"

    print("Broadcasting standard(s): {standard}".format(standard=standard))

# using a 10 second version bc im running out of storage in VM
# ex1_2("bbb.mp4", "10sbbb.mp4", "10sbbb_subbed.mp4", "bbb_mono.wav", "bbb_lowbr.wav", "subtitles.srt", "ex1.mp4")
ex3("ex1.mp4")
#for ex4 just use different videos from the seminars and labs as an argument to the previous function
