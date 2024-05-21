from rdflib import Graph, Namespace, URIRef
import requests

# Carregar a ontologia existente
g = Graph()
g.parse("ex2/med_doentes.ttl", format="ttl")

# Definir o namespace
ex = Namespace("http://www.example.org/disease-ontology#")

# Definir a query CONSTRUCT
construct_query = """
PREFIX ex: <http://www.example.org/disease-ontology#>
CONSTRUCT {
    ?patient ex:hasDisease ?disease .
}
WHERE {
    ?patient a ex:Patient ;
             ex:exhibitsSymptom ?symptom .
    ?disease ex:hasSymptom ?symptom .
}
"""

# Função para executar a query CONSTRUCT
def execute_construct_query(g, query):
    result_graph = g.query(query)
    return result_graph

# Executar a query CONSTRUCT e obter os triplos
triples = execute_construct_query(g, construct_query)

# Adicionar os triplos resultantes à ontologia existente
for s, p, o in triples:
    g.add((s, p, o))

# Salvar a ontologia atualizada
g.serialize(destination="med_doentes2.ttl", format="ttl")
