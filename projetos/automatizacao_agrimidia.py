import requests  #importa a biblioteca que faz as requisições para a url 
import re #importa a função que permite utilizar regex

url = "https://agrimidia.com.br/revistas/" #url que queremos usar 

response = requests.get(url) #response guarda a resposta da requisição que foi feita aquela url 
content = response.text #content guarda o conteudo da response em texto

urls_edicao = re.findall(r'https:\/\/agrimidia.com.br\/revista\/(?:ai|si)?-edicao-\d+\/', content) #usa regex para achar um padrão dentro do content
datas_edicoes = re.findall(r'\d{2}\/\d{4}', content) #procura com regex um padrao 

ultima_edicao = None #guarda a data mais nova da edição

for edicoes in datas_edicoes: #percorre cada data que capturamos com datas_edicoes
    mes_ano_nova_edicao = edicoes.split("/") #separa a data em mes e ano em formato de string 
    mes_nova_edicao = int(mes_ano_nova_edicao[0]) #guarda mes em forma numerica 
    ano_nova_edicao = int(mes_ano_nova_edicao[1]) #guarda ano em forma numerica

    if ultima_edicao == None: #verifica se a variavel ultima_edicao ainda esta vazia
        ultima_edicao = edicoes #se estiver, guarda a primeira data que pegamos
        
    else:
        comparar_edicao = ultima_edicao.split("/")
        mes_ultima_edicao = int(comparar_edicao[0])
        ano_ultima_edicao = int(comparar_edicao[1])

        if ano_nova_edicao > ano_ultima_edicao:
            ultima_edicao = edicoes

        elif ano_nova_edicao == ano_ultima_edicao:
            if mes_nova_edicao > mes_ultima_edicao:
                ultima_edicao = edicoes
         
print(ultima_edicao)













"""
 Entrar no site
Encontrar a revista Suinocultura Industrial
 Descobrir qual é a edição mais recente
 Ver se essa edição já foi capturada
      NÃO
Entrar na página dessa edição
 Encontrar o Embed
 Entrar no Embed
 Descobrir onde está o PDF
 Baixar o PDF
Transformar/processar o PDF
 Capturar os dados necessários
Salvar no formato do veículo"""