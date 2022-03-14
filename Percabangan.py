#percabangan if
nilai = 10
if (nilai > 9):
	print("Nilainya A")


#percabangan if else
nilai = 10
if (nilai < 9):
	print("Nilainya C")
else:
	print("Nilainya A")
	

#percabangan if, else, elif
umur = int(input("masukkan umur: "))
if (umur >= 1 and umur <= 6):
	print ("Balita")
elif (umur >= 7 and umur <= 12 ):
	print("SD")
elif (umur >= 13 and umur <= 15):
	print("SMP")
elif (umur >= 16 and umur <= 18):
	print("SMA/SMK")
elif (umur >= 19 and umur <= 22):
	print("Kuliah")
else:
	print("Orang Tua")