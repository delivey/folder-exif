import exifread as er
import os

folder = input("""What directory is your folder located in? e.g: D:/Exif/Folder/
""")
file_list = os.listdir(folder)


for file in file_list:
    if not file.endswith('.txt'):
        f = open('%s%s' % (folder, file), 'rb')
        tags = er.process_file(f)
        strings = '%s' % tags
        sep = ": b'"
        rest = strings.split(sep, 1)[0]
        txt = open("%s%s.txt" % (folder, file), "w")
        txt.write("%s" % rest)
        print("File %s log saved." % file)

