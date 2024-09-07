from neo4j import GraphDatabase

class Neo4jApp:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_person(self, name, age, occupation):
        with self._driver.session() as session:
            session.execute_write(self._create_and_return_person, name, age, occupation)

    @staticmethod
    def _create_and_return_person(tx, name, age, occupation):
        query = (
            "CREATE (p:Person {name: $name, age: $age, occupation: $occupation}) "
            "RETURN p"
        )
        result = tx.run(query, name=name, age=age, occupation=occupation)
        return result.single()

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"  # Remplacez par votre nom d'utilisateur
    password = "adminadmin"  # Remplacez par votre mot de passe
    
    app = Neo4jApp(uri, user, password)
    app.create_person("qwerty HAYA@", 29, "Engineer")
    app.close()
