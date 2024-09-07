# 🚀 Projet : Exploitation de Données CSV avec Python et Neo4j

## 🎯 Objectif

Ce projet a pour finalité d'exploiter des données issues de fichiers CSV en utilisant Python afin d'alimenter une base de données Neo4j. Grâce à des scripts simples, nous importons des données dans la base et interagissons avec elles en utilisant le langage de requête Cypher.

## 🛠️ Technologies Utilisées

- **Python** : Pour traiter et manipuler les fichiers CSV.
- **Neo4j** : Base de données orientée graphes pour stocker et visualiser les données.
- **Cypher** : Langage de requête de Neo4j pour manipuler les nœuds et les relations.
- **VSCode** : Environnement de développement utilisé pour écrire les scripts.

## ⚙️ Installation et Configuration

### 1. Prérequis

Avant de commencer, assure-toi d'avoir installé les éléments suivants :
- **Python 3.x** : [Télécharge Python ici](https://www.python.org/downloads/)
- **Neo4j** : [Télécharge Neo4j ici](https://neo4j.com/download/)
- **VSCode** : [Télécharge Visual Studio Code ici](https://code.visualstudio.com/)

### 2. Cloner le dépôt

Clone ce projet sur ton ordinateur local :

```bash
git clone [https://github.com/ton-utilisateur/mon-projet-neo4j.git](https://github.com/Collins-Webdev/neo4j_database_atut.git)
cd mon-projet-neo4j
```

### 3. Créer un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel Python pour isoler les dépendances :

```bash
python -m venv env
source env/bin/activate   # Pour macOS/Linux
env\Scripts\activate       # Pour Windows
```

### 4. Installer les dépendances

Installe les dépendances nécessaires via `pip` :

```bash
pip install neo4j pandas
```

- **neo4j** : Pour interagir avec Neo4j.
- **pandas** : Pour lire et manipuler les fichiers CSV.

### 5. Configurer Neo4j

Démarre Neo4j et configure les identifiants d'accès à la base de données. Assure-toi que Neo4j est accessible à l'adresse `bolt://localhost:7687` ou `http://localhost:7474/browser/`.

## 📂 Structure du Projet

Voici la structure de base du projet :

```bash
neo4j_database_atut/
│
├── data/                 # Dossier contenant les fichiers CSV
│   └── personnes.csv     # Exemple de fichier CSV avec les données
├── database/             # Dossier contenant le dump de la BD Neo4J
│   └── neo4j.dump        # Dump de la BD Neo4J
│
├── neo4j_script.py       # Script Python pour insérer les données dans Neo4j
├── verify_neo4j.py       # Script Python pour vérifier l'insertion les données dans Neo4j
└── README.md             # Fichier d'explications
```

## 🚀 Étapes du Projet

### 1. Préparer les Données

Le fichier CSV contient les informations à insérer dans Neo4j. Voici un exemple de structure de `personnes.csv` :

```csv
nom,age,profession
Alice,29,Ingenieur
Bob,35,Docteur
```

### 2. Script Python pour Alimenter Neo4j

Le script `neo4j_script.py` lit les données du fichier CSV et insère les informations dans Neo4j sous forme de nœuds `Person`.

Voici un aperçu du script :

```python
import pandas as pd
from neo4j import GraphDatabase

# Connexion à Neo4j
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "votre_mot_de_passe"))

class Neo4jApp:

    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def create_person(self, name, age, occupation):
        with self.driver.session() as session:
            session.execute_write(self._create_and_return_person, name, age, occupation)

    @staticmethod
    def _create_and_return_person(tx, name, age, occupation):
        query = (
            "CREATE (p:Person {name: $name, age: $age, occupation: $occupation}) "
            "RETURN p"
        )
        result = tx.run(query, name=name, age=age, occupation=occupation)
        return result.single()

# Charger les données CSV
df = pd.read_csv('data/personnes.csv')

# Insérer chaque ligne dans Neo4j
app = Neo4jApp(driver)
for index, row in df.iterrows():
    app.create_person(row['nom'], row['age'], row['profession'])

app.close()
```

### 3. Vérification des Données dans Neo4j

Pour vérifier que les données ont bien été insérées, exécute cette commande Cypher dans Neo4j Browser :

```cypher
MATCH (p:Person) RETURN p
```

Cela retournera tous les nœuds `Person` avec leurs propriétés.

## 🧹 Suppression des Données

Pour supprimer un nœud `Person` spécifique ou toutes les données, tu peux utiliser les commandes Cypher suivantes :

- **Supprimer un nœud précis** :

  ```cypher
  MATCH (p:Person {name: 'Alice'})
  DETACH DELETE p
  ```

- **Supprimer tous les nœuds `Person`** :

  ```cypher
  MATCH (p:Person)
  DETACH DELETE p
  ```

## 🤝 Contribuer

Si tu souhaites contribuer à ce projet, n'hésite pas à soumettre des Pull Requests ou à signaler des problèmes.

## 📄 Licence

Ce projet est sous licence ATUT 2024. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
