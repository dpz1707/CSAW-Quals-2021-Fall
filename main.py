import piexif
import piexif.helper

#"C:\Users\nydan\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\piexif\__pycache__"
dict = piexif.load("worldMap.jpg")

print(piexif.dump(dict))

for ifd in ("0th", "Exif", "GPS", "1st"):
    for tag in dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], dict[ifd][tag])

user_comment = piexif.helper.UserComment.load(dict["Exif"][piexif.ExifIFD.UserComment])
print(user_comment)