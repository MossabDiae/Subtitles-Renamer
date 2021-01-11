# Subtitles-Renamer
Renames Subtitles to match the videos naming pattern for auto loading.

## INSTALL
Just put the script in the same dicrectory as Videos and Subtitles and use
`python subsrenamer.py` or `python3 subsrenamer.py`
#### proper installation:
```
git clone https://github.com/mossaybo/Subtitles-Renamer.git
cd Subtitles-Renamer/
sudo cp subsrenamer.py /usr/local/bin/subsrenamer
sudo chmod +x /usr/local/bin/subsrenamer
```
this will make the script executable and can be run anywhere using `subsrenamer`
## HOW TO USE
the script assumes that videos and subtitles are in the same current working directory

`-v` : give the first common part of all video names that is from the beginning till where the episode number is mentioned.

e.g: if your video is `[AkihitoSubs] Hyouka - 02 [BD 1920x1080 x265 10Bit AC3].mkv`
	do `-v "[AkihitoSubs] Hyouka - "`

`-s` : same thing , give first name part of the subtitles until the Ep number is mentioned.

e.g: if sub files names `Demon Slayer Kimetsu no Yaiba.S01E19.CC.ja.srt`
	do `-s "Demon Slayer Kimetsu no Yaiba.S01E"`

`--dry-run` : non-destructive , do not rename just print and quit

#### notice: 
	1- make the arguments inside ".."
	2- do not forget spaces
### EXAMPLE:
- a directory with current listing :
```
$ ls
Demon Slayer Kimetsu no Yaiba.S01E01.CC.ja.srt  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 01 [1080p][HEVC].mkv
Demon Slayer Kimetsu no Yaiba.S01E02.CC.ja.srt  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 02 [1080p][HEVC].mkv
Demon Slayer Kimetsu no Yaiba.S01E03.CC.ja.srt  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 03 [1080p][HEVC].mkv
```
- running :

`subsrenamer -v "[Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - " -s "Demon Slayer Kimetsu no Yaiba.S01E"`

- results in: 
```
$ ls
[Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 01 [1080p][HEVC].mkv  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 02 [1080p][HEVC].srt
[Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 01 [1080p][HEVC].srt  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 03 [1080p][HEVC].mkv
[Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 02 [1080p][HEVC].mkv  [Hakata Ramen] Kimetsu no Yaiba (Demon Slayer) - 03 [1080p][HEVC].srt
```

### Known problems
- sometimes the videos differ in the final part , the script doesn't check for that yet.

### ToDo / wishlist features :
- [ ] better handling of user input/ error reporting.
- [ ] rename each sub based on its corresponding episode (aka match first AND last part)
- [ ] set custom directory where the subs reside
- [ ] make possible to generate an undo script placed in working directory to undo the renaming 
