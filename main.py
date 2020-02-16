import exifread as er
import os

folder = input("""What directory is your folder located in? e.g: D:/Exif/Folder/
""")
file_list = os.listdir(folder)

for file in file_list:
    if not file.endswith('.txt'):
        f = open(folder + file, 'rb')
        tags = "%s" % er.process_file(f)
        rest = tags.split(": b'", 1)[0]
        txt = open(folder + file, 'w')
        wrest = txt.write(rest)
        print("File %s log saved." % file)
print("All done!")

