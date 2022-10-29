print("How to check commit")

#Calculator
def calculator(value1, value2, operator):
    if operator == 'kali' or operator == 'x' or operator == '*':
        hasil = value1 * value2
    elif operator == 'bagi' or operator == '/' or operator == 'b' :
        hasil = value1 / value2
    elif operator == 'tambah' :
        hasil = value1 + value2
    elif operator == 'kurang' :
        hasil = value1 - value2

    print('Hasilnya adalah : ',hasil)

    return hasil

value1 = int(input('Masukan Nilai Pertama : '))
value2 = int(input('Masukan Nilai Kedua : '))
inp_operator = input('Masukkan operator [kali, bagi, tambah, kurang] ')
calculator(value1,value2, inp_operator) 
