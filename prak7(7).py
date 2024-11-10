# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:47:43 2024

@author: Lenovo
"""

def ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')

print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    try:
        number = int(input("masukkan angka: "))
        if number == 0:
            print("terima kasih telah menggunakan program saya")
            break
        print(f"({number}, '{ordinal_suffix(number)}')")
    except ValueError:
        print("Input harus berupa angka!")