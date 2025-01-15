import os

def get_flag_names(directory):
    # 用於存儲檔名的清單
    flag_names = []

    # 歷遍目錄內的所有檔案
    for file in os.listdir(directory):
        # 檢查是否為.png檔案
        if file.endswith(".png") and file.startswith("flag-"):
            # 移除前綴"flag-"與後綴".png"
            flag_name = file[5:-4]
            flag_names.append(flag_name)

    return flag_names

# 指定目錄路徑
flag_directory = "./flag"

# 呼叫函式並輸出結果
flag_list = get_flag_names(flag_directory)
print(flag_list)
