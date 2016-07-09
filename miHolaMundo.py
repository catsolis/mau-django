
###################
#El if:elif :else #
###################

nombre="Catchan"
if nombre == "Catchan":
	print('Catchan tara ra poder gatuno!')
elif nombre=="Dogchan":
	print('otro print')
else:
	print('el else aja aja')


###################
#   una funcion   #
###################
frutas="guineo"

def BorrandoLetras():
	print (" La fruta inicial es:" + frutas)
	print ("ejecutando BorrandoLetras en 3,2,1")
	if frutas=="banana":
		print ("nooo")
	elif frutas=="guineo":
		print(" Borrando: guine ")
	else:
		print("Bananas en pijamas")
#aqui la llamo
BorrandoLetras()

######################
# FUncion y Arreglo  #
######################

print("####################   una funcion   ####################")
def NombrarAnimales(mascota):
	print("Animalito: " + mascota + "  :D  ")

animales=["gato","perro","rino","ballena","tortuga"]

for envio in animales:
	NombrarAnimales(envio)
	print("salio!")


