import subprocess
import os
from os.path import isfile, join, splitext

in_path = "in"
out_path = "out"
out_suffix = "-Hinted"
cmd = ["./ttfautohint.exe"]

for i in os.listdir(in_path):
    if not isfile(join(in_path, i)):
        continue

    split_i = splitext(i)
    i_name = split_i[0]
    i_ext = split_i[1]

    if i_ext != ".ttf":
        continue

    i_cmd = cmd.copy()
    i_cmd.extend([join(in_path, i), join(out_path, f"{i_name}{out_suffix}{i_ext}")])

    subprocess.run(i_cmd)
    print("Hinted", i)