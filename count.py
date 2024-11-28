#!/user/bin/python3
# SPDX-FileCopyrightText: 2024 Oka Naoto
from collections import Counter
import string

def count_alphabets(text):

    text = text.lower()
    filtered_text = ''.join(char for char in text if char in string.ascii_lowercase)
    

    counts = Counter(filtered_text)
    
    sorted_counts = {letter: counts.get(letter, 0) for letter in string.ascii_lowercase}
    
    return sorted_counts


text = input("文章を入力してください: ")
result = count_alphabets(text)


for letter, count in result.items():
    print(f"{letter}: {count}")

