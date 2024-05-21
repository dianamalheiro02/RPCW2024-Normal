from rdflib import Graph, Namespace

# Carregar a ontologia existente
g = Graph()
g.parse("med_doentes2.ttl", format="ttl")

# Definir o namespace
ex = Namespace("http://www.example.org/disease-ontology#")

# Consulta SPARQL para distribuição das doenças pelos sintomas
query_symptoms = """
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?symptom (COUNT(?disease) AS ?numDiseases)
WHERE {
    ?disease a ex:Disease ;
             ex:hasSymptom ?symptom .
}
GROUP BY ?symptom
ORDER BY ?symptom
"""

# Consulta SPARQL para distribuição das doenças pelos tratamentos
query_treatments = """
PREFIX ex: <http://www.example.org/disease-ontology#>

SELECT ?treatment (COUNT(?disease) AS ?numDiseases)
WHERE {
    ?disease a ex:Disease ;
             ex:hasTreatment ?treatment .
}
GROUP BY ?treatment
ORDER BY ?treatment
"""

# Função para executar uma consulta SPARQL
def execute_query(query):
    return g.query(query)

# Função para salvar resultados em um arquivo
def save_results_to_file(filename, results, header):
    with open(filename, "w") as file:
        file.write(header + "\n")
        for row in results:
            entity = row[0]
            count = row[1]
            file.write(f"{entity}, {count}\n")

# Executar a consulta de distribuição das doenças pelos sintomas
results_symptoms = execute_query(query_symptoms)
save_results_to_file("ResQuery14.txt", results_symptoms, "Sintoma, Numero de Doencas")

# Executar a consulta de distribuição das doenças pelos tratamentos
results_treatments = execute_query(query_treatments)
save_results_to_file("ResQuery15.txt", results_treatments, "Tratamento, Numero de Doencas")

print("Os resultados foram salvos nos arquivos 'distribuicao_doencas_sintomas.txt' e 'distribuicao_doencas_tratamentos.txt'.")
