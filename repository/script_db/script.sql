drop database banco

CREATE database banco;

GRANT ALL PRIVILEGES ON banco_desafio.* TO 'root'@'localhost';

USE banco;

CREATE TABLE banco.produto(
    id int AUTO_INCREMENT,
    descricao varchar(50) NOT NULL,
    unidade varchar(5) NOT NULL,
    quantidade DECIMAL(10,2) NOT NULL,
    preco_real DECIMAL(10,2) NOT NULL,
    preco_dolar DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
 );

 ALTER TABLE banco.produto AUTO_INCREMENT = 1