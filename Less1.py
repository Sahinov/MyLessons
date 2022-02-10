#echo "# MyLessons" >> README.me

#git init
#git add README.md
#git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/Sahinov/MyLessons.git
#git push -u origin main
import platform
import sys

info = 'OS info is \n{}\n\nPython Version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture()
)
print(info)

with open('info_os.txt', 'w') as ff:
    ff.write(info)