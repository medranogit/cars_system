import MySQLdb

user = "root"
password = ""
host = "localhost"
porta = 3306

banco = MySQLdb.connect(user=user, password= password, host=host, port=porta)

print('Conectando...')

#apagando uma database com nome especifico caso exista
banco.cursor().execute("DROP DATABASE IF EXISTS `carros_empresa`;")

#salvando o comando a cima
banco.commit()

#criando uma variavel para facilitar os codigos
banco_command = banco.cursor()

#criando tabela base
criar_tabela = '''
    CREATE DATABASE `carros_empresa`;
    USE `carros_empresa`;
    CREATE TABLE `carros` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `marca` varchar(50) NOT NULL,
      `cor` varchar(20) NOT NULL,
      `velocidade` varchar(20) NOT NULL,
      PRIMARY KEY (`id`))
    '''
banco_command.execute(criar_tabela)

# inserindo carros
banco_command.executemany(
      'INSERT INTO carros (nome, marca, cor, velocidade) VALUES (%s, %s, %s, %s)',
      [
            ('Lamborguini', 'Volkswagen', 'Laranja' ,'280'),
            ('Camaro', 'Chevrolet', 'Amarela' ,'250'),
      ])

#simples print do banco
banco_command.execute('select * from carros')
print(' -------------  Carritos:  -------------')
for carro in banco_command.fetchall():
    print(carro[1]+" - "+ carro[2])

# commitando para salvar
banco.commit()
# para encerrar conexao com o banco
banco.close()