#ffmpeg -i input.avi -c:a aac -b:a 128k -c:v libx264 -crf 23 output.mp4

import sys
import os

def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 128k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python __.py input_file output_name')
    i = sys.argv[1]
    o = sys.argv[2]
    convert_avi_to_mp4(i,o)
