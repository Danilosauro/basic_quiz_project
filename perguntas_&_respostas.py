
print("------------------------Na trilha da adaptacao----------------------------------")


print("------------------------Ambiente mesofitico----------------------------------")

print("--------------------------pergunta 1-----------------------------------")

print("Ambientes mesofíticos são caracterizados pela presença de plantas com folhas dorsiventrais, largas e verdes em sua maioria, além de vistosas. Você, como professor de biologia, é questionado por seus estudantes sobre quais traços ambientais permitem aos vegetais de ambiente mesofítico possuírem as características acima citadas.  Com o objetivo de sanar a dúvida inicial e incentivar a curiosidade do estudante, você responde que:")

print("a) O fato destes vegetais se encontrarem em regiões de extrema pluviosidade.'")
print("b) Estes vegetais suportam a maior parte das variações ambientais, logo, não faz muita diferença o ambiente em que se encontram.​")
print("c) Os principais traços ambientais que permitem as características são a elevada umidade relativa do ar e a composição do solo, porém, sem extremos. ​")

respostaum = input("Digite uma das opcoes:") 
pontos=0

if respostaum =='c' or respostaum =='C':
    pontos=pontos+10
    print("Parabens, voce acertou! Agora voce tem"),print(pontos), print("pontos") 
    
    #tratamento de exceções
elif respostaum == 'b' or respostaum  =='B' or respostaum =='a' or respostaum == 'A':
   print("Voce errou! voce tem"), print (pontos), print("pontos")  

else:
    pontos 
    print("Alternativa inválida")


print("---------------------------pergunta 2--------------------------------------") 

print("Você foi contratado para ser o responsável pelo projeto de recuperação de uma área  de floresta úmida que foi convertida em pasto. Após dois anos de projeto, visitas e avaliações a respeito dos estágios, você e sua equipe percebem que a vegetação encontra-se no estágio secundário de sucessão ecológica, no qual ainda não há formação de dossel completa e consequentemente há alta incidência luminosa. Qual das seguintes características você espera encontrar nas análises anatômicas dos vegetais  para condução do estudo?")

print("a) Parênquimas bem desenvolvidos e cutícula mais espessa.​")
print("b) Folhas epiestomáticas​") 
print("c) Sistema de condução pouco desenvolvido​") 

respostadois = input('Digite uma das opcoes:') 

if respostadois == 'a':
    pontos=pontos+10
    print("Voce acertou! Agora voce tem"), print(pontos),print("pontos") 


else:
    print("voce errou! Voce tem"), print(pontos),print("pontos")


print("---------------------------pergunta 3--------------------------------------") 

print("Ambientes mesofíticos são caracterizados por apresentar fatores ambientais intermediários, porém possuem um fator considerado limitante para os vegetais. Que fator é esse?")

print("a)Luminosidade ")
print("b)Alta temperatura")
print("c)Temperatura amena ")  

respostatres= input("Digite uma das opcoes:")

#acerto
if respostatres == 'a': 
   pontos=pontos+10
   print("Voce acertou! Agora voce tem "), print(pontos), print("pontos") 

#erro
else:
    print("voce errou! voce tem "), print(pontos), print("pontos") 


print("---------------------------pergunta 4--------------------------------------") 

print("Qual adaptação anatômica é característica das plantas mesofíticas?​") 

print("a)Cutícula espessa") 
print("b)Parênquima aquifero")
print("c)Baixa densidade de tricomas") 

respostaquatro = input ("Digite uma das opcoes:")

#acerto
if respostaquatro == 'c':
    pontos=pontos+10
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos")

#erro
else: 
    print("voce errou! voce tem "), print(pontos), print (pontos)


print("---------------------------pergunta 5--------------------------------------")  

print("Qual o principal desafio encontrado em plantas de ambientes mesofíticos?​")

print("a) Alta luminosidade nas copas")
print("b) Baixa disponibilidade de água")
print("c) Baixa umidade")

respostacinco = input ("Digite uma das opcoes:")

if respostacinco == 'a':
    pontos=pontos+10 
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else: 
    print("voce errou! voce tem "), print(pontos), print (pontos) 



print("---------------------------Ambiente hidrofítico-------------------------------------")

print("---------------------------pergunta 6--------------------------------------")  
print("Ecossistemas de água doce podem abrigar uma alta e complexa diversidade de organismos. Esses ambientes podem ser classificados como ecossistemas lóticos e lênticos. Qual desses é conhecido como lêntico?​")

print("a) Rio ")
print("b) Riacho")
print("c) Lago")

respostaseis = input ("Digite uma das opcoes:")
if respostaseis=='c': 
    pontos=pontos+10 
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos")  

else: 
    print("voce errou! voce tem "), print(pontos), print (pontos) 



print("---------------------------pergunta 7--------------------------------------")  

print("As plantas de ambiente hidrofítico podem crescer parcialmente ou completamente submersas em água, e para que isso seja possível elas apresentam várias adaptações, tanto morfológicas quanto anatômicas. Qual das adaptações abaixo é uma adaptação morfológica?​")

print("a) pneumatóforos")
print("b) cutículas delgadas")
print("c) mesofilo indiferenciado")

respostasete = input("Digite uma das opcoes:")

if respostasete =='a': 
    pontos=pontos+10
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else:
    print ("voce errou! voce tem "), print(pontos), print (pontos)  


print("---------------------------pergunta 8--------------------------------------") 

print("Apesar das plantas hidrofíticas ocorrerem em ambientes com disponibilidade de água, fator importante para distribuição dos organismos, o oxigênio pode ser um fator limitante, como as plantas respondem a esse problema?​")

print("a) Muitos esclereides ")
print("b) Estômatos na face adaxial ")
print("c) Parênquima aerífero ")

respostaoito = input("Digite uma das opcoes:") 

if respostaoito == 'c': 
    pontos=pontos+10 
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else: 
    print("voce errou! voce tem "), print(pontos), print (pontos) 


print("---------------------------pergunta 9--------------------------------------") 

print("As plantas hidrófitas apresentam adaptações morfológicas e anatômicas que permitem sua permanência em ambientes com alta disponibilidade de água. Entretanto nem toda planta que vive em um lugar alagado é considerada hidrófita, pois não apresentam tais adaptações. Sabendo disso, qual das características abaixo é crucial para uma planta ser considerada uma hidrófita?​")

print("a) Produzir suas gemas de renovação dentro do meio aquático")
print("b) Raízes livres, sem estarem aderidas a algum tipo de substrato")
print("c) Folhas de aspecto membranáceo e com alta densidade de tricomas ")


respostanove = input ("Digite uma das opcoes:")

if respostanove =='a': 
    pontos=pontos+10
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else: 
    print("voce errou! voce tem "), print(pontos), print (pontos) 


print("---------------------------pergunta 10--------------------------------------")  

print('''Você foi o botânico brasileiro escolhido pela NASA, numa missão de exploração e colonização do planeta Vulcano (com condições ambientais extremamente similares a Terra), visto que a terra atingiu o seu limite para manutenção da vida, devido as mudanças climáticas.​
Como você é especialista em anatomia vegetal, a sua tarefa na missão é gerar os relatórios acerca das características das plantas encontradas em Vulcano para que a colonização ocorra o mais rápido possível. ​
Ao encontrar um ecossistema lêntico e observar visualmente as plantas ali presentes e flutuantes na superfície aquática você espera encontrar abundância de qual tecido ou estrutura vegetal ? ''')

print("a) presença de aerênquima abundante")
print("b) Cutícula espessa e lignificada")
print("c) Estômatos em criptas")

respostadez = input ("Digite uma das opcoes:")

if respostadez == 'a': 
    pontos=pontos+10
    print ("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else: 
    print("voce errou! voce tem "), print(pontos), print (pontos) 


print("---------------------------pergunta 11--------------------------------------") 

print("O ambiente hidrofítico apresenta diversos desafios, como por exemplo:")

print("a) Escassez de água")
print("b) Falta de Oxigênio")
print("c) Falta de matéria orgânica")


respostaonze = input ("Digite uma das opcoes:")

if respostaonze == 'b':
    pontos=pontos+10 
    print ("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else: 
    print ("voce errou! voce tem "), print(pontos), print (pontos)

 

print("---------------------------pergunta 12--------------------------------------") 

print("Quais são os fatores que influenciam as plantas do ambientes aquáticos?")

print("a) Concetrações de sais ")
print("b) Disponibilidade de lipídeos no solo")
print("c) Composição de açúcares")

respostadoze = input ("Digite uma das opções:")

if respostadoze =='a': 
    pontos=pontos+10
    print("Voce acertou! Agora voce tem"), print (pontos), print("pontos") 

else:
    print ("voce errou! voce tem "), print(pontos), print (pontos)