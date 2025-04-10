from database import conecta, encerra_conexao

def main():
    connection = conecta()
    cursor = connection.cursor()

    def insere_acoes(ticker, nome_empresa, setor, preco, data_cotacao):
        cmd_insert = "INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao) VALUES (%s,%s,%s,%s,%s);"
        values = (ticker, nome_empresa, setor, preco, data_cotacao)
        cursor.execute(cmd_insert, values)
        connection.commit()
        print("Dados inseridos com sucesso!")

    def seleciona():
        cmd_select = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3;"
        cursor.execute(cmd_select)
        acoes = cursor.fetchall()
        for acao in acoes:
            print(acao)
        return acoes

    def atualiza(novo_preco, ticker):
        cmd_update = "UPDATE acoes_b3 SET preco=%s WHERE ticker=%s"
        cursor.execute(cmd_update, (novo_preco, ticker))
        connection.commit()
        print("Registro atualizado com sucesso!")

    def deleta(ticker):
        cmd_delete = "DELETE FROM acoes_b3 WHERE ticker=%s"
        cursor.execute(cmd_delete, (ticker,))
        connection.commit()
        print("Registro deletado com sucesso!")

    encerra_conexao(connection)