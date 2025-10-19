from django.db import models

class Experiencias(models.Model):
    ...

    def __str__(self):
        return self.titulo
    

class Certificados(models.Model):
    ...

    def __str__(self):
        return self.titulo


class Projetos(models.Model):
    ...

    def __str__(self):
        return self.titulo
