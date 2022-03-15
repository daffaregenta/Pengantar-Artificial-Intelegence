#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08

import csv
import pandas as pd

#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08
#Aturan Fuzzy
def aturanFuzzy(penghasilanRendah,penghasilanSedang,penghasilanTinggi,pengeluaranRendah,pengeluaranSedang,pengeluaranTinggi):
    
    #Berdasarkan tabel
    IYA = [0,0,0,0,0,0] # 6 YES
    TIDAK = [0,0,0] # 3 NO

    if (penghasilanRendah > 0) and (pengeluaranRendah > 0):
        IYA[0] = min(penghasilanRendah, pengeluaranRendah);
    if (penghasilanSedang> 0) and (pengeluaranRendah> 0):
        TIDAK[0] = min(penghasilanSedang, pengeluaranRendah);
    if (penghasilanTinggi>0) and (pengeluaranRendah>0):
        TIDAK[1] = min(penghasilanTinggi, pengeluaranRendah);
    if (penghasilanRendah > 0) and (pengeluaranSedang > 0):
        IYA[1] = min(penghasilanRendah,pengeluaranSedang);
    if (penghasilanSedang > 0) and (pengeluaranSedang > 0):
        IYA[2] = min(penghasilanSedang, pengeluaranSedang);
    if (penghasilanTinggi > 0) and (pengeluaranSedang > 0):
        TIDAK[2] = min(penghasilanTinggi, pengeluaranSedang);
    if (penghasilanRendah > 0) and (pengeluaranTinggi > 0):
        IYA[3] = min(penghasilanRendah,pengeluaranTinggi);
    if (penghasilanSedang> 0) and (pengeluaranTinggi > 0):
         IYA[4] = min(penghasilanSedang,pengeluaranTinggi);
    if (penghasilanTinggi > 0) and (pengeluaranTinggi > 0):
         IYA[5] = min(penghasilanTinggi, pengeluaranTinggi);
         
    return  max(IYA),max(TIDAK)

#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08
# rumus De-fuzzy
def defuzzy(IYA,TIDAK):
    return ((IYA * 60) + (TIDAK * 40)) / (IYA + TIDAK)

#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08
# Fungsi keanggotaan variabel penghasilan
def kurvapenghasilan(penghasilan): 
    penghasilanRendah =0;
    penghasilanSedang =0;
    penghasilanTinggi =0;

    if(penghasilan >= 14.5):
        penghasilanTinggi =1 ;
    elif (penghasilan > 8.1) and (penghasilan <14.5 ):
        penghasilanSedang = (14.5 - penghasilan)/(14.5 - 8.1);
        penghasilanTinggi = 1- penghasilanSedang;
    elif (penghasilan > 7) and (penghasilan < 8.1):
        penghasilanRendah = (8.1-penghasilan)/(8.1 - 7);
        penghasilanSedang = 1- penghasilanRendah;
    elif (penghasilan <= 7):
        penghasilanRendah =1;

    return penghasilanRendah,penghasilanSedang,penghasilanTinggi

#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08
# Fungsi keanggotaan variabel pengeluaran
def kurvapengeluaran(pengeluaran): 
    pengeluaranRendah = 0;
    pengeluaranSedang = 0;
    pengeluaranTinggi = 0;

    if (pengeluaran >= 10.21):
        pengeluaranTinggi = 1;
    elif (pengeluaran > 9) and (pengeluaran < 10.21):
        pengeluaranSedang = (10.21 - pengeluaran)/(10.21-9);
        pengeluaranTinggi = 1 - pengeluaranSedang;
    elif(pengeluaran == 9):
        pengeluaranSedang = 1;
    elif (pengeluaran > 7.54) and (pengeluaran < 9):
        pengeluaranRendah = (9-pengeluaran)/(9-7.54);
        pengeluaranSedang = 1-pengeluaranRendah;
    elif (pengeluaran <= 7.54):
        pengeluaranRendah = 1;
    return pengeluaranRendah,pengeluaranSedang,pengeluaranTinggi;


read_file = pd.read_excel('Mahasiswa.xls')
read_file.to_csv('Mahasiswa.csv', index = None, header=True)

temp = 0
#Muhammad Daffa Regenta Sutrisno
#1301184291
#IF-42-08
# membaca file Mahasiswa.xls yang telah diconvert ke bentuk xls
with open('Mahasiswa.csv') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    with open('Bantuan.csv', 'w', newline='') as data:
        fieldname =['No','penghasilan','pengeluaran']
        writer = csv.DictWriter(data,fieldname)
        writer.writeheader()
        for row in reader:
            penghasilanR, penghasilanS, penghasilanT = kurvapenghasilan(float(row[1]))
            pengeluaranR,pengeluaranS,pengeluaranT = kurvapengeluaran(float(row[2]))    
            IYA, TIDAK = aturanFuzzy(penghasilanR,penghasilanS,penghasilanT,pengeluaranR,pengeluaranS,pengeluaranT)
            x = defuzzy(IYA, TIDAK)
            if(x>=59) and (temp<=19):
                temp=temp+1
                print('ID =', row[0],'; PENGHASILAN =',row[1],'; PENGELUARAN =',row[2],'; SCORE =',x)
                writer.writerow({'No':row[0],'penghasilan':row[1],'pengeluaran':row[2]})

pd1 = pd.read_csv('Bantuan.csv')
pd1.to_excel('Bantuan.xls', index = None, header=True)