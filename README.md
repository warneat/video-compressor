## video-compressor

(tl;dr) compress your videos in VID_YYYYMMDD_xxxxxx.jpg format into subfolders sorted by years with reduced filesize.<br />
For images, see also: [image-compressor](https://github.com/warneat/image-compressor/)
<br />

### Use-case:
If you run out of storage on your smartphone and don't want to spend hours deleting and sorting out videos, one easy solution is to simply reduce the file-size of your videos on the backup device (Computer/HDD/NAS?) by using this script and shove them back to your phone.<br />

### Notes:
- The naming-Convention VID_YYYYMMDD_xxxxxx.mp4 is assumed (default for most Android Camera-Apps).
- The video_compressor script only deals with .mp4 files.
- By default, file size will be reduced to about 55% of the original size, while maintaining acceptable quality (see also [Quality adjustments](https://github.com/warneat/video-compressor#quality-adjustments) below).
- No files will be deleted!
- A directory 'VID_compressed' is created which will hold the subdirectories VID_2019, VID_2020 ... per year respectively.
- .mp4 files that have weird numbers after the extension (as i experienced in my case) are copied without changes.
- Files without '.mp4' are being ignored.
- The video-compressor does **not** run through subdirectories.

Simply place `video_compressor.py` at the place your videos are sitting and run it. <br />

### Installation (Unix-like, MacOS)

Eighter install [FFMPEG](https://ffmpeg.org/) or go through the (horrible) process of [compiling](https://trac.ffmpeg.org/wiki/CompilationGuide) it by yourself for proper hardware-acceleration, but regular installation will do:

    sudo apt update -y
    sudo apt install ffmpeg
or for Mac

    brew install ffmpeg

*There are discussions about self-compiling it, as people seemed to have experienced bugs (i didn't) or not much speed improvements by doing so.*

Anyway, assuming Python (version >= 3.4) is installed, in terminal:

clone this repository, cd into it:

        git clone https://github.com/warneat/video-compressor && cd video-compressor

copy the script to your video folder e.g: 
    
        cp video_compressor.py ~/foo/bar/videos

Optionally, clean up/delete repository with

        cd .. &&  sudo rm -r video-compressor

#### Run

In your video directory run the script with 
    
        python3 video_compressor.py
    or
        ./video_compressor.py


### On Windows 

- [Install](https://ffmpeg.org/download.html) or [compile](https://trac.ffmpeg.org/wiki/CompilationGuide) the video processing library [FFMPEG](https://ffmpeg.org/)
- Download this repository or `git clone https://github.com/warneat/video-compressor` like above.
- move the video_compressor.py script to desired location and run it from there with `python .\video_compressor.py`


### Optional: Quality adjustments
-  FFMPEG takes a `-crf` argument to set the output quality. Higher values correspond to lower quality. For example 23 reduces the filesize to about 84 % compared to original. Default is 25 (file-size to 58%). They don't recommend values higher than 28 (filesize reduces 42%) [Detailed Information about `-crf` flag](https://trac.ffmpeg.org/wiki/Encode/H.264#crf)
- Lower values (higher output-quality) increase computing time dramatically
  
  To modify settings:
  - change `crf=xx` to your liking (line 39)
  
### Further reading
- FFMPEG really eats up all your computing-power!

- As the processing might take hours or days for a large amount of data, when accessing via remote/ssh you might want to use screen ([ultra-quick tutorial](https://linuxize.com/post/how-to-use-linux-screen/)) to keep it running in background without an open terminal session.<br> 
In a nutshell: Install it, `$screen` to start, [do stuff], `ctr+a` and `d` to detach. Reattach with `$screen -r`

- To automate (video) backups e.g Phone to NAS/Cloud-Server/Online-Account... i highly recommend the app [FolderSync](https://play.google.com/store/apps/details?id=dk.tacit.android.foldersync.lite) 

#### Feedback is very much apprechiated
