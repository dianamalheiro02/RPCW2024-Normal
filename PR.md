# EX1
##    Define Classes
    Propriedades
    Pessoas
    Fruta
    Animais
    Geleias
    Vegejetais


##    Data properties

###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#animais
:animais rdf:type owl:DatatypeProperty ;
         rdfs:domain :Animais ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#fruta
:fruta rdf:type owl:DatatypeProperty ;
       rdfs:domain :Fruta ;
       rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#geleia
:geleia rdf:type owl:DatatypeProperty ;
        rdfs:domain :Geleias ;
        rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#nome
:nome rdf:type owl:DatatypeProperty ;
      rdfs:domain :Pessoas ;
      rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#nomeProp
:nomeProp rdf:type owl:DatatypeProperty ;
          rdfs:domain :Propriedade ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#vejetais
:vejetais rdf:type owl:DatatypeProperty ;
          rdfs:domain :Vejetais ;
          rdfs:range xsd:string .


##    Object Properties

###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#alimenta
:alimenta rdf:type owl:ObjectProperty ;
          rdfs:domain :Pessoas ;
          rdfs:range :Animais .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#colhe
:colhe rdf:type owl:ObjectProperty ;
       rdfs:domain :Pessoas ;
       rdfs:range :Fruta .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#contrata
:contrata rdf:type owl:ObjectProperty ;
          rdfs:domain :Pessoas ;
          rdfs:range :Pessoas .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#cria
:cria rdf:type owl:ObjectProperty ;
      rdfs:domain :Pessoas ;
      rdfs:range :Animais .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#cultivaF
:cultivaF rdf:type owl:ObjectProperty ;
          rdfs:domain :Pessoas ;
          rdfs:range :Fruta .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#cultivaV
:cultivaV rdf:type owl:ObjectProperty ;
          rdfs:domain :Pessoas ;
          rdfs:range :Vejetais .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#fazGeleias
:fazGeleias rdf:type owl:ObjectProperty ;
            rdfs:domain :Pessoas ;
            rdfs:range :Geleias .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#protege
:protege rdf:type owl:ObjectProperty ;
         rdfs:domain :Pessoas ;
         rdfs:range :Propriedade .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#tem
:tem rdf:type owl:ObjectProperty ;
     rdfs:domain :Pessoas ;
     rdfs:range :Pessoas .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#trocaF
:trocaF rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoas ;
        rdfs:range :Fruta .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#trocaV
:trocaV rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoas ;
        rdfs:range :Vejetais .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#vendeF
:vendeF rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoas ;
        rdfs:range :Fruta .


###  http://rpcw.di.uminho.pt/2024/2024/4/untitled-ontology-23#vendeV
:vendeV rdf:type owl:ObjectProperty ;
        rdfs:domain :Pessoas ;
        rdfs:range :Vejetais .


## Cria os indivíduos com os seus atributos e as suas relações;
Não tenho os 3 exemplos de cada. Tenho cenouras e alface mas não tomates, por exemplo. Fiquei apertada em relação ao tempo.


## Deixei a ontologia completa em: historia.ttl.

## Queries em queries.ttl. 
Ler o ficheiro e seguir as suas instruções. O que diz 'res' é o resultado que terei obtido.




# EX2
O meu PG é PG53766. Daí só estar presente esse ficheiro.

Para chegar ao resultado segui estes passos:

- Executar popula.py (tem em atenção os caminhos que tem no programa para os ficheiros);
- Executar as queries presentes em queries.txt (só até à 12, inclusive);
- Executar addConstruct.py;
- Adicionar a nova ontologia criada (med_doentes2.ttl);
- Executar query 13;
- Executar queries1415.py para obter resultado das últimas 2 queries nos ficheiros ResQuery14 e 15, respetivamente.

