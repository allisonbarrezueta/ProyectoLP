from django.db import models

class animal(models.Model):
    id_animal = models.AutoField(primary_key=True,unique=True)
    tamano = models.CharField('Tamano de animal', max_length=15)
    sexo = models.CharField('Sexo',max_length=10)
    raza = models.CharField('Raza de animal', max_length=60, blank=True,default='NA')
    perdido = models.BooleanField(default=False)
    descripcion = models.CharField('Descripcion',max_length=100, default='NA')
    direccion = models.ForeignKey('direccion', on_delete=models.CASCADE)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return '{id} animal: {sexo} de tamano {tamano}'.format(
        id = self.id_animal,
        sexo = self.sexo,
        tamano = self.tamano
        )

class direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True,unique=True)
    direccion1 = models.CharField(max_length=60)
    direccion2 = models.CharField(max_length=60)

    def __str__(self):
        return '{id} direccion: {d1}, {d2}'.format(
        id = self.id_direccion,
        d1 = self.direccion1,
        d2 = self.direccion2
        )

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True,unique=True)
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=40)
    usuario = models.CharField('username', max_length=20)
    contrasena = models.CharField('password', max_length=20)
    celular = models.CharField('Telefono', max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{id} {username}'.format(
        id = self.id_usuario,
        username=self.usuario,
        )
