#!/usr/bin/env python3
import os
import hashlib
import magic
import tqdm
import mimetypes

def get_md5(filename):
    md5=hashlib.md5()
    with open(f,'rb') as fd:
        fb=fd.read(BLOCKSIZE)
        while len(fb)>0:
            md5.update(fb)
            fb=fd.read(BLOCKSIZE)
    return md5.hexdigest()

def get_extension(filename):
    magic_string = magic.from_file(filename, mime=True)
    extension = mimetypes.guess_extension(magic_string,strict=False)
    magic_string="." + magic_string.replace("/","_")
    if extension:
        return extension

    return magic_string

BLOCKSIZE=65536
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in tqdm.tqdm(files):
    os.rename(f,get_md5(f)+get_extension(f))
