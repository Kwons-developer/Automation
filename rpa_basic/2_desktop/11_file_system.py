# 파일 기본
import os
import sys  # 한글 보여주는것
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

""" print(os.getcwd()) # current working directory 현재 잡업 공간

os.chdir("rpa_basic")   # rpa_basic 으로 작업 공간 이동
print(os.getcwd()) # current working directory 현재 잡업 공간

os.chdir("..")  # 부모 폴더로 이동
print(os.getcwd())

os.chdir("../..")   # 조부모 폴더로 이동
print(os.getcwd())

os.chdir("c:/") # 주어진 절대 경로로 이동 """

# 파일 경로 만들기
#file_path = os.path.join(os.getcwd(), "my_file.txt")        # 절대 경로 생성
#print(file_path)

# 파일 경로에서 폴더 정보 가져오기
#print(os.path.dirname(r"c:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\my_file.txt"))

# 파일 정보 가져오기
#import time
#import datetime

# 파일 생성 날짜 가져오기
#file_path = r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\2_desktop\11_file_system.py"

#ctime = os.path.getctime(r"c:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\2_desktop\11_file_system.py")
#print(ctime)
# 날짜 정보를 strftime
#print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
#mtime = os.path.getmtime(r"c:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\2_desktop\11_file_system.py")
#print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
#atime = os.path.getatime(file_path)
#print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
#size = os.path.getsize(file_path)
#print(size)     # 바이트 단위로 파일 크기 가져오기

file_path = r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\2_desktop\11_file_system.py"

# 파일 목록 가져오기 
#print(os.listdir())     # 모든 폴더, 파일 목록 가져오기
#print(os.listdir(r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic\2_desktop"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
#result = os.walk(r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic")       # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
#print(result)

#for root, dirs, files in result:
#    print(root, dirs, files)

# 만약 폴더 내에서 특정 파일 찾으려면?
""" name = "11_file_system.py"
result = []
for root, dirs, files in os.walk("."):
    if name in files:
        result.append(os.path.join(root, name))

print(result) """

# 만약 폴더 내에서 특정 패턴 가진 파일 찾으려면?
""" import fnmatch
pattern = "*.py"    # .py로 끝나는 모든 파일 찾기      제목*.py 이런식으로 다른 파일 찾아짐
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):      # 이름이 패턴과 일치하면
            result.append(os.path.join(root, name))
print(result) """


# 주어진 경로가 파일인지? 폴더인지?
#print(os.path.isdir(r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic"))       # rpa_basic 은 폴더인가?
#print(os.path.isfile(r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic"))       # rpa_basic 은 파일인가? 참 트루 반환함

# 만약 지정된 경로에 해당하는 파일이나 폴더가 없다면?
#print(os.path.isfile("awfefe.png")) # False 반환


# 주어진 경로 존재하는지?
#if os.path.exists(r"C:\Users\User\Desktop\프로그래밍\셀레니움\rpa_basic"):
#   print("파일 또는 폴더가 존재합니다.")
#else:
#    print("존재하지 않습니다")


# 파일 만들기
#open("new_file.txt", "a").close()       #빈 파일 생성

# 파일명 변경하기
#os.rename("new_file.txt", "new_file_rename.txt")    # 이름 변경

# 파일 삭제하기
#os.remove("new_file_rename.txt")

# 폴더 만들기
#os.mkdir("new_folder")  # 현재 경로에 폴더 만듬

# 여러 하위폴더 가진 폴더 만들기
#os.makedirs("new_folders/a/b/c")   # 하위 폴더 가지는폴더 생성 

# 폴더명 변경
#os.rename("new_folder", "new_folder_rename")

# 폴더 삭제하기
#os.rmdir("new_folder_rename")      하위 폴더 없을때만 rmdir 사용 가능

#하위 폴더가 있는 폴더 지우기
import shutil
#shutil.rmtree("new_folders")        # 폴더 안 비어있지 않아도 완전 삭제 가능
# 모든 파일 삭제될 수 있으므로 주의


# 파일 복사하기 
# 어떤 파일을 폴더 안으로 복사하기
#shutil.copy("file_menu.png", "test_folder")     # 원본 파일 경로, 대상 폴더 경로

# 어떤 파일을 폴더안에 새로운 파일 이름으로 복사하기
#shutil.copy("file_menu.png", "test_folder/copied_file_menu.png")        # 원본 경로, 대상 경로에 복사

#shutil.copyfile("file_menu.png", "test_folder/copied_file_menu_2.png")  # 원본 파일 경로, 대상 파일 경로

#shutil.copy2("file_menu.png", "test_folder/copy2.png")

# copy, copyfile : 메타정보 복사 안함
# copy2 : 메타 정보 복사함

# 폴더 복사
#shutil.copytree("test_folder", "test_folder2")      # 하위폴더도 다같이 복사함

# 폴더 이동
shutil.move("test_folder", "test_folder2")
shutil.move("폴더","없는 폴더") # 없는 폴더에 폴더를 넣으려하면 폴더명이 없는 폴더 이름으로 바뀜

