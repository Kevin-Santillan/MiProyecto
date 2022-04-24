def agregar(nombre,edad,direccion,telefono):
    datos["Nombre"]=nombre
    datos["Edad"]=edad
    datos["Direccion"]=direccion
    datos["Telefono"]=telefono

datos={}
nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese la edad: "))
direccion=input("Ingrese la direccion: ")
telefono=int(input("Ingrese el numero telefonico: "))
agregar(nombre,edad,direccion,telefono)

15 in datos
print(datos)