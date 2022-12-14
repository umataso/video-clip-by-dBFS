# 動画ファイルを10分毎に区切るプログラム
# 長時間のファイルをそのままclip_by_dbfs.ipynbで切り抜きを行うと音ズレが起こるので

import ffmpeg
from file_loader import load_video
import os
video_path = load_video()
tmp = video_path.replace(video_path.split("/")[-1], "")
video_path = video_path.replace(tmp, "./")
print(video_path)
out_dir = video_path.replace(".mp4", "/")
print(out_dir)
#ffmpeg -i input.mp4 -c copy -f segment -flags +global_header -segment_format_options movflags=+faststart -reset_timestamps 1 -segment_time 1740 output%02d.mp4
stream = ffmpeg.input(video_path)
stream = stream.output(out_dir+"%02d.mp4", c="copy", flags="+global_header", f="segment", segment_time=f"{60*10}", reset_timestamps="1")
stream.run(overwrite_output=True)