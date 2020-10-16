from pathlib import Path


def split_name(full_name):
    if '.' not in full_name:
        return ""
    dot_index = full_name.rfind('.')
    return full_name[:dot_index], full_name[dot_index:]


def add_space(s):
    return s.replace("][", "] [", 1)


dirPath = Path()
extr = '*.ass'
ext = '.ass'
ep = 274
for file in dirPath.glob(extr):
    if ep < 10:
        file.rename('0' + str(ep) + ext)
    else:
        file.rename(str(ep) + ext)
    ep += 1

team = '[CR] [JPBD]'
for file in dirPath.glob(extr):
     file_name, file_extension = split_name(file.name)
     file.rename(f'{str(dirPath.absolute())}\\{file_name} {team}{file_extension}')
