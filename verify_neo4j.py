def find_person(self, name):
    with self._driver.session() as session:
        result = session.execute_read(self._find_and_return_person, name)
        for record in result:
            print(record["p"])

@staticmethod
def _find_and_return_person(tx, name):
    query = "MATCH (p:Person {name: $name}) RETURN p"
    result = tx.run(query, name=name)
    return result
