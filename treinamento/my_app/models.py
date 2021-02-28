from django.db import models

# Create your models here.
class Endereco(models.Model):
    lista_estados = (  ("AC","Acre"),("AL","Alagoas"),("AP","Amapá"),("AM","Amazonas"),("BA","Bahia"),("CE","Ceará"), ("ES","Espírito Santo"), ("GO","Goías"),("MA","Maranhão"), ("MT","Mato Grosso"), ("MS","Mato Grosso do Sul"),("MG","Minas Gerais"),("PA","Pará"),("PB","Paraíba"),("PE","Pernambuco"), ("PI","Piauí"),("RJ","Rio de Janeiro"),("RN","Rio Grande do Norte"),("RS","Rio Grnade do Sul"),("RO","Rondônia"),("RR","Roraima"),("SC","Santa Catarina"),("SP","São Paulo"),("SE","Sergipe"),("TO","Tocantins"),("DF","Distrito Federal")   )
    cep = models.CharField(null = False, max_length = 100)
    estado = models.CharField(null = False, max_length = 2, choices=lista_estados)
    cidade = models.CharField(null = False, max_length = 100)
    def __str__(self):
        return f"{self.cep} | {self.cidade} | {self.estado}"

class Lanchonete(models.Model):
    nome = models.CharField(null = False, max_length = 100)
    endereco = models.ForeignKey(Endereco, null=False, on_delete=models.CASCADE)
    telefone = models.TextField(null = False)

    def __str__(self):
        return f"Nome:{self.nome} Endereço:{self.endereco}."

class Prato(models.Model):
    lanchonete = models.ForeignKey(Lanchonete, on_delete = models.CASCADE)
    nome = models.CharField(null = False, max_length = 100)
    preco = models.FloatField(null = False)

    def __str__(self):
        return f"{self.lanchonete.nome} | {self.nome} R$ {self.preco}"
