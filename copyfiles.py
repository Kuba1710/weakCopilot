import os
import shutil
import torch
import tiktoken

def checkFileLenght(filename):
    print('checking length')
    with open(filename, 'r') as f:
        text = f.read()
    enc = tiktoken.get_encoding('gpt2')
    tokens = enc.encode(text)
    elements = torch.tensor(tokens)
    elementsSize = list(elements.size())
    if elementsSize[0] > 8192: #ugly shit
        return True
    else:
        return False

def copy(split):
    print('starting copy')
    if(split == "train"):
        data_root = "cpp_c_files/train"
        destination_dir = "files/train"
        print('train set')
    else:
        data_root = "cpp_c_files/validation"
        destination_dir = "files/validation"
        print('validation set')
    
    for root, _, files in os.walk(data_root):
            print('iterating through directroy')
            for file in files:
                print('iterating through files')
                if checkFileLenght(os.path.join(root, file)):
                    print('check passed')
                    print('performing copy')
                    shutil.copy(os.path.join(root, file), destination_dir)
                    print(f"Copied: {file} to {destination_dir}")

print("start")
copy("train")
copy("val")