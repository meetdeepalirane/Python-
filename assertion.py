#assertions are statements that you can use to set sanity checks during the development process.

import os
with open("C:/Users/admin/Untitled Folder/sample.txt") as fr:
    fr.seek(0)
    assert os.path.getsize("C:/Users/admin/Untitled Folder/sample.txt") ==0,"File is  empty"
    print(fr.read())