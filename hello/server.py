from fastapi import FastAPI

app = FastAPI()

#Route Params
@app.get("/saudacao/{nome}") #Decorator
def saudacao(nome: str):
    texto = f"Ola {nome}, tudo em paz?!"
    return {"mensagem: ": texto}

@app.get("/quadrado/{numero}")
def quadrado(numero: int):
    resultado = numero * numero
    texto = f"O quadrado de {numero} é: {resultado}"
    return {"mensagem": texto}

#Query Params ?, =, &
@app.get("/dobro")
def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f"O dobro de {valor} e {resultado}"}

@app.get("/area-retangulo")
def area_retangulo(largura: int, altura: int = 1):
    area = largura * altura
    return {"area": area}