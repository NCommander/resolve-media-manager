#!/usr/bin/python3

import os
import sys
import argparse
import subprocess

acceptable_input_extensions = [
    '.mp4',
    '.MP4',
    '.mov',
    '.MOV',
    '.mkv',
    '.webm',
    '.ts',
]

def main():
    print("DaVinci Resolve Media Manager 0.2")
    print()
    print("THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,")
    print("EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES")
    print("OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.")
    print()

    parser = argparse.ArgumentParser()
    parser.add_argument('in_folder', help='Media to transcode to Resolve Format')
    parser.add_argument('out_folder', help="Optimized media write location")
    parser.add_argument('-n', dest='dry_run', action='store_true', default=False)

    args = parser.parse_args()

    in_folder = os.path.abspath(os.path.normpath(args.in_folder))
    out_folder = os.path.abspath(os.path.normpath(args.out_folder))

    if os.path.isdir(in_folder) == False:
        print("ERROR: %s must exist! Exiting ..." % (in_folder))
        return

    print("Media In Folder: " + in_folder)
    print("Media Out Folder: " + out_folder)

    processing_list = []

    for subdir, dirs, files in os.walk(in_folder):
        for file in files:
            in_path = subdir + os.sep + file

            extension =  os.path.splitext(in_path)[1]
            if extension not in acceptable_input_extensions:
                #print("ERROR: unknown file type: " + in_path)
                continue

            relative_path = os.path.relpath(in_path, in_folder)
            out_path = out_folder + os.sep + relative_path
            out_path = os.path.splitext(out_path)[0] + '.mkv'

            if os.path.exists(out_path) == True:
                print("SKIPPING: " + out_path)
                continue

            processing_list.append((in_path, out_path))


    for in_file, out_file in processing_list:
        print(in_file + " -> " + out_file)
        out_base_dir = os.path.dirname(out_file)
        #print(out_base_dir)

        ffmpeg_cmd = [
            'ffmpeg',
            '-hide_banner',
            '-loglevel', 'error',
            '-stats',
            '-i', in_file,
            '-vcodec', 'copy',
            '-acodec', 'pcm_s16le',
            '-movflags', 'use_metadata_tags',
            out_file
        ]

        if (args.dry_run == False):
            os.makedirs(out_base_dir, exist_ok=True)
            subprocess.call(ffmpeg_cmd)

if __name__ == '__main__':
    main()
