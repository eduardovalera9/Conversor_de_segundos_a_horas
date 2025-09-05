#Elaborar un programa que al introducir una cantidad de segundos muestre
# el tiempo en horas, minutos y segundos

segundos= input("Ingrese los segundos (s): ")
segundos= int(segundos)
horas= segundos//3600
sobrante_de_segundos= segundos%3600
minutos= sobrante_de_segundos//60
sobrante_de_segundos2= sobrante_de_segundos%60
print ("Horas:")
print(horas)
print("Minutos:")
print(minutos)
print("Segundos:")
print(sobrante_de_segundos2)
