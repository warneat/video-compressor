#!/usr/bin/env python3
import os
import inspect
import time
import subprocess


def compressing_loop(compressed_dir, script_dir, compressing_targets):

    for mp4 in compressing_targets:

        # files and directory infos
        year = target_year(mp4)
        new_dir = os.path.join(compressed_dir, str('VID_'+ year))
        old_path = os.path.join(script_dir, mp4)
        new_path = str(os.path.join(new_dir, mp4)).replace(
            '.mp4', '_compressed.mp4')

        try:
            # new dir available?
            if os.path.exists(new_dir) is False:
                os.mkdir(new_dir)

            # .mp4 already there?
            if os.path.exists(new_path):
                pass

        # happened once, try ignoring
        except FileExistsError:
            continue

        # compressing with ffmpeg
        # Threads Option in wrong position? Process is low priority anyway...
        command = str(
            'ffmpeg  '
            #+ '-loglevel warning '
            + '-threads 2 -i '
            + old_path
            + ' -vcodec libx264 -crf 25 '
            + new_path
        )

        print(
            f'\n\n############################## starting {mp4} ##############################\n\n')
        process = subprocess.call(command, shell=True)


def mp4_targets_list(script_dir):
    '''list of valid .mp4 file names including extension'''

    all_filenames = os.listdir(script_dir)

    target_mp4_list = []
    copy_list = []
    for filename in all_filenames:
        if (filename.split('.')[-1] == 'mp4' and    # correct extension
            filename[0] != '.' and                  # not hidden
                filename[:4] == 'VID_'):            # fits pattern
            target_mp4_list.append(filename)
        # had some strange filenames like VID_20xxxx.mp4.53635453
        elif ('.mp4' in filename and                # contains 'mp4'
              filename[0] != '.' and                # not hidden
              filename[:4] == 'VID_'):              # fits pattern
            copy_list.append(filename)
    return target_mp4_list, copy_list


def target_year(mp4):
    # assuming Android naming convention DCIM_2019 :(
    year = mp4.split('_')[1][:4]
    return year


def count_files_in_dirs(output_dir):
    # recursive
    file_amount = 0
    for dirpath, dirnames, filenames in os.walk(output_dir):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                file_amount += 1
    return file_amount


def main():
    try:
        # where am i? Path infos
        scrip_path = inspect.getframeinfo(inspect.currentframe()).filename
        script_dir = os.path.dirname(os.path.abspath(scrip_path))
        compressed_dir = os.path.join(script_dir, 'VID_compressed')

        # find targets
        compress_mp4_targets, copy_mp4_targets = mp4_targets_list(script_dir)
        mp4_compress_amout = len(compress_mp4_targets)
        mp4_copy_amount = len(copy_mp4_targets)

        # 0 targets ->stop
        if not mp4_compress_amout:
            print('No files to compress in this directory')
        else:
            print(f'\nFound {mp4_compress_amout} valid .mp4 files to compress')
            print(
                f'Found {mp4_copy_amount} .mp4 files to copy without compressing\n')

            # .../compressed folder available?
            try:
                if os.path.exists(compressed_dir) is False:
                    os.mkdir(compressed_dir)
            except FileExistsError:
                pass
            compressing_loop(compressed_dir, script_dir, compress_mp4_targets)

    except KeyboardInterrupt:
        print('bye')


if __name__ == '__main__':
    main()
