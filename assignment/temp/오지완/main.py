import os


def count_characters_and_files_in_txt_files(directory):
    total_characters = 0
    txt_file_count = 0

    # 디렉토리의 모든 파일을 탐색
    for filename in os.listdir(directory):
        # 파일이 .txt 확장자인지 확인
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            txt_file_count += 1

            # 파일을 열고 글자 수를 세기
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                total_characters += len(content)

    return total_characters, txt_file_count


# 예시: 특정 디렉토리의 경로를 지정
directory_path = 'C:\Workspace\project01'
total_characters, txt_file_count = count_characters_and_files_in_txt_files(directory_path)
print(f"텍스트 파일 개수: {txt_file_count}")
print(f"총 글자 수: {total_characters}")

