import os
import shutil

def extract_cpp_c_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    cpp_c_extensions = {".c", ".cpp", ".h", ".hpp", ".cc", ".hh", ".cxx", ".hxx"}

    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.endswith(ext) for ext in cpp_c_extensions):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, os.path.relpath(source_file, source_dir))
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                shutil.copy2(source_file, target_file)
                print(f"Copied: {source_file} -> {target_file}")

source_directory = "./repositories"
target_directory = "./cpp_c_files"
extract_cpp_c_files(source_directory, target_directory)
