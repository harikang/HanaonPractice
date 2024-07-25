from src import *

if __name__=="__main__":
    directory = 'D:/workspace_hanabank/assignment/공유폴더.zip'  # 원하는 디렉토리 경로로 변경
    temp = 'D:/workspace_hanabank/assignment/temp'
    output_file_path = 'D:/workspace_hanabank/assignment/output.txt'
    unzip_file(directory, temp)
    folder_info = get_person_folder_info(temp)

    for folder, info in folder_info.items():
        print(f"Folder: {folder}")
        print(f"  Total Words: {info['total_words']}")
        print(f"  Total Size: {info['total_size']} bytes")
        print(f"  TXT File Count: {info['file_count']}")

    # 정보를 파일에 저장
    save_info_to_file(folder_info, output_file_path)
