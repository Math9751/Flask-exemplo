USE Disco;

CREATE TABLE albuns (
    id integer not null auto_increment,
    album varchar(100),
    artista varchar(100),
    ano integer,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO albuns (album, artista, ano) VALUES ('And Justice for All', 'Metallica', 1988);
INSERT INTO albuns (album, artista, ano) VALUES ('Spreading the Disease', 'Anthrax', 1985);
INSERT INTO albuns (album, artista, ano) VALUES ('Rust in Peace', 'Megadeth', 1990);
INSERT INTO albuns (album, artista, ano) VALUES ('Reign in Blood', 'Slayer', 1986);