INSERT INTO usuarios (nome, email, senha)
VALUES
('João', 'joao@email.com', '123'),
('Maria', 'maria@email.com', '123'),
('Pedro', 'pedro@email.com', '123'),
('Ana', 'ana@email.com', '123'),
('Carlos', 'carlos@email.com', '123');

INSERT INTO filmes (usuario_id, titulo, ano_lancamento, genero, nota, capa_url)
VALUES
(1, 'Interestelar', '2014-01-01', 'Ficção Científica', 9.0, NULL),
(2, 'Titanic', '1997-01-01', 'Romance', 8.5, NULL),
(3, 'Avatar', '2009-01-01', 'Ficção Científica', 8.0, NULL),
(4, 'O Batman', '2022-01-01', 'Ação', 8.2, NULL),
(5, 'Toy Story', '1995-01-01', 'Animação', 8.3, NULL);