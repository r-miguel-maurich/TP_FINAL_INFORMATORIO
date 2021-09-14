from django.db import models

class Usuario(models.Model):
        nombre = models.CharField(max_length=255, null=True, blank=True)
        apellido = models.CharField(max_length=255, null=True, blank=True)
        nickName = models.CharField(max_length=255, null=True, blank=True)
        isAdmin = models.BooleanField(null=True, blank=True)
        pas = models.CharField(max_length=255, null=True, blank=True)
        horaLogeo = models.DateTimeField(null=True, blank=True)
        puntajeTotal = models.IntegerField(verbose_name='puntajeTotal')
        class Meta:
            db_table = 'usuario'
        def __str__(self):
            return self.nombre

class Nivel(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    puntajeMin = models.IntegerField(verbose_name='puntajeTotal')
    puntajeMax = models.IntegerField(verbose_name='puntajeTotal')
#    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'nivel'


class Juego(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    juegan = models.ManyToManyField(Usuario, related_name="juegos")
    class Meta:
        db_table = 'juego'
    def __str__(self):
        return self.nombre



class Pregunta(models.Model):
    titulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    comentario = models.CharField(max_length=255, null=True, blank=True)
    juegos = models.ManyToManyField(Juego, related_name="juegos")
    class Meta:
        db_table = 'pregunta'
    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    isCorrecta = models.BooleanField(default=True)
    preguntas = models.ManyToManyField(Pregunta, related_name="preguntas")
    def __str__(self):
        return self.descripcion
    class Meta:
        db_table = 'respuesta'
