from neo4j import GraphDatabase


class HelloWorldExample:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run(
            "CREATE (a:Greeting) " "SET a.message = $message " "RETURN a.message + ', from node ' + id(a)",
            message=message,
        )
        return result.single()[0]


if __name__ == "__main__":
    greeter = HelloWorldExample(
        "bolt://neo4j:7687",  # url: "bolt://{コンテナ名}:7687"
        "neo4j",  # user: "neo4j"
        "password",  # password
    )
    greeter.print_greeting("hello, world")
    greeter.close()

    # 以下の URL で Neo4j Browser にアクセスできる
    # http://localhost:7474/browser/
