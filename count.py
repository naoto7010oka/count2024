#!/user/bin/python3
# SPDX-FileCopyrightText: 2024 Oka Naoto
from collections import Counter
import string

def count_alphabets(text):
    # テキストをすべて小文字に変換し、アルファベットのみ抽出
    text = text.lower()
    filtered_text = ''.join(char for char in text if char in string.ascii_lowercase)
    
    # 各アルファベットの出現回数をカウント
    counts = Counter(filtered_text)
    
    # アルファベット順にソート
    sorted_counts = {letter: counts.get(letter, 0) for letter in string.ascii_lowercase}
    
    return sorted_counts

# テキスト入力
text = input("文章を入力してください: ")
result = count_alphabets(text)

# 結果を表示
for letter, count in result.items():
    print(f"{letter}: {count}")

