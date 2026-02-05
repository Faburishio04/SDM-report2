#!/usr/bin/python3

import re
                
def calc(A, B):
    # 型チェック：整数以外は -1
    if not isinstance(A, int) or not isinstance(B, int):
        return -1

    # 範囲チェック：1〜999 のみ許可
    if not (1 <= A <= 999):
        return -1
    if not (1 <= B <= 999):
        return -1

    # 正常系：掛け算
    return A * B

        
                
def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')

        # 入力を整数に変換
        try:
            A = int(A)
            B = int(B)
        except ValueError:
            print("input A * input B = ", -1)
            continue

        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
	main()
