import zipfile
import os

def unzip_file(zip_path, extract_to):
    # ZIP 파일이 존재하는지 확인
    if not os.path.isfile(zip_path):
        print(f"Error: {zip_path} does not exist.")
        return

    # 추출할 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # ZIP 파일 열기
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 모든 파일 추출
        zip_ref.extractall(extract_to)
        print(f"Extracted all files to {extract_to}")
        

def count_words_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

def get_person_folder_info(directory):
    person_info = {}

    for root, dirs, files in os.walk(directory):
        # 사람 이름으로 된 최상위 폴더
        person_name = os.path.basename(root)
        
        # 사람이름을 기준으로 한 폴더가 아니면 넘어가기
        if root == directory:
            continue        
        # 최상위 폴더 기준으로 정보를 수집
        if person_name not in person_info:
            if len(person_name)==3 or len(person_name)==2:
                pass
            else:
                continue
            person_info[person_name] = {'total_words': 0, 'total_size': 0, 'file_count': 0}

        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                word_count = count_words_in_file(file_path)
                file_size = os.path.getsize(file_path)

                person_info[person_name]['total_words'] += word_count
                person_info[person_name]['total_size'] += file_size
                person_info[person_name]['file_count'] += 1
            if file.endswith('.docx'):
                "fill here"
                person_info[person_name]['total_words'] += word_count
                person_info[person_name]['total_size'] += file_size
                person_info[person_name]['file_count'] += 1


    return person_info

def save_info_to_file(get_person_folder_info, output_file_path):
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        for folder, info in get_person_folder_info.items():
            f.write(f"Folder: {folder}\n")
            f.write(f"  Total Words: {info['total_words']}\n")
            f.write(f"  Total Size: {info['total_size']} bytes\n")
            f.write(f"  TXT File Count: {info['file_count']}\n\n")

