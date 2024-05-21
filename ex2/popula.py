import csv
import json
from rdflib import Graph, Namespace, Literal, RDF, RDFS, OWL, URIRef

# Namespaces
ex = Namespace("http://www.example.org/disease-ontology#")
rdf = Namespace(RDF)
owl = Namespace(OWL)
rdfs = Namespace(RDFS)
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Ontologia inicial
g = Graph()

# Definir os prefixos
g.bind("ex", ex)
g.bind("owl", owl)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("xsd", xsd)

# Classes
g.add((ex.Disease, rdf.type, owl.Class))
g.add((ex.Symptom, rdf.type, owl.Class))
g.add((ex.Treatment, rdf.type, owl.Class))
g.add((ex.Patient, rdf.type, owl.Class))

# Propriedades
g.add((ex.hasSymptom, rdf.type, owl.ObjectProperty))
g.add((ex.hasSymptom, rdfs.domain, ex.Disease))
g.add((ex.hasSymptom, rdfs.range, ex.Symptom))

g.add((ex.hasTreatment, rdf.type, owl.ObjectProperty))
g.add((ex.hasTreatment, rdfs.domain, ex.Disease))
g.add((ex.hasTreatment, rdfs.range, ex.Treatment))

g.add((ex.exhibitsSymptom, rdf.type, owl.ObjectProperty))
g.add((ex.exhibitsSymptom, rdfs.domain, ex.Patient))
g.add((ex.exhibitsSymptom, rdfs.range, ex.Symptom))

g.add((ex.hasDisease, rdf.type, owl.ObjectProperty))
g.add((ex.hasDisease, rdfs.domain, ex.Patient))
g.add((ex.hasDisease, rdfs.range, ex.Disease))

g.add((ex.receivesTreatment, rdf.type, owl.ObjectProperty))
g.add((ex.receivesTreatment, rdfs.domain, ex.Patient))
g.add((ex.receivesTreatment, rdfs.range, ex.Treatment))

# Função para adicionar doenças e sintomas a partir do CSV
def populate_diseases_symptoms(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            disease_name = row[0].replace(" ", "_")
            disease_uri = ex[disease_name]
            g.add((disease_uri, rdf.type, ex.Disease))
            for symptom in row[1:]:
                if symptom:
                    symptom_name = symptom.strip().replace(" ", "_")
                    symptom_uri = ex[symptom_name]
                    if (symptom_uri, rdf.type, ex.Symptom) not in g:
                        g.add((symptom_uri, rdf.type, ex.Symptom))
                    g.add((disease_uri, ex.hasSymptom, symptom_uri))

# Função para adicionar descrições de doenças a partir do CSV
def populate_disease_descriptions(csv_file):
    g.add((ex.hasDescription, rdf.type, owl.DatatypeProperty))
    g.add((ex.hasDescription, rdfs.domain, ex.Disease))
    g.add((ex.hasDescription, rdfs.range, xsd.string))
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            disease_name = row[0].replace(" ", "_")
            description = row[1]
            disease_uri = ex[disease_name]
            g.add((disease_uri, ex.hasDescription, Literal(description, datatype=xsd.string)))

# Função para adicionar tratamentos a partir do CSV
def populate_disease_treatments(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            disease_name = row[0].replace(" ", "_")
            disease_uri = ex[disease_name]
            for treatment in row[1:]:
                if treatment:
                    treatment_name = treatment.strip().replace(" ", "_")
                    treatment_uri = ex[treatment_name]
                    if (treatment_uri, rdf.type, ex.Treatment) not in g:
                        g.add((treatment_uri, rdf.type, ex.Treatment))
                    g.add((disease_uri, ex.hasTreatment, treatment_uri))

# Função para adicionar pacientes a partir do JSON
def populate_patients(json_file):
    g.add((ex.name, rdf.type, owl.DatatypeProperty))
    g.add((ex.name, rdfs.domain, ex.Patient))
    g.add((ex.name, rdfs.range, xsd.string))
    with open(json_file, 'r') as file:
        data = json.load(file)
        for i, patient in enumerate(data):
            patient_id = f"Patient_{i+1}"
            patient_name = patient['nome']
            patient_uri = ex[patient_id]
            g.add((patient_uri, rdf.type, ex.Patient))
            g.add((patient_uri, ex.name, Literal(patient_name, datatype=xsd.string)))
            for symptom in patient['sintomas']:
                symptom_name = symptom.strip().replace(" ", "_")
                symptom_uri = ex[symptom_name]
                if (symptom_uri, rdf.type, ex.Symptom) not in g:
                    g.add((symptom_uri, rdf.type, ex.Symptom))
                g.add((patient_uri, ex.exhibitsSymptom, symptom_uri))

# Função principal
def main():
    populate_diseases_symptoms("Disease_Syntoms.csv")
    g.serialize(destination='ex2/med_doencas.ttl', format='turtle')

    populate_disease_descriptions('Disease_Description.csv')
    g.serialize(destination='ex2/med_descriptions.ttl', format='turtle')

    populate_disease_treatments('Disease_Treatment.csv')
    g.serialize(destination='ex2/med_tratamentos.ttl', format='turtle')

    populate_patients('doentes/pg53766.json')
    g.serialize(destination='ex2/med_doentes.ttl', format='turtle')

if __name__ == "__main__":
    main()
