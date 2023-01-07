GRANT ALL PRIVILEGES ON DATABASE "university" TO "postgres";


CREATE TABLE "Pessoa" (
  "cpf" char(14) PRIMARY KEY,
  "nome" varchar(128),
  "data_de_nascimento" char(10),
  "contato" uuid,
  "endereco" uuid
);

CREATE TABLE "Contato" (
  "id" uuid PRIMARY KEY,
  "telefone_1" varchar(14),
  "telefone_2" varchar(14),
  "email" varchar(256)
);

CREATE TABLE "Endereco" (
  "id" uuid PRIMARY KEY,
  "cidade" char(7),
  "uf" char(2),
  "cep" char(8),
  "logradouro" varchar(128),
  "numero" varchar(16),
  "bairro" varchar(64),
  "complemento" varchar(256)
);

CREATE TABLE "Estudante" (
  "rga" char(12) PRIMARY KEY,
  "pessoa" char(11),
  "curso" int,
  "unidade" int,
  "contato" uuid
);

CREATE TABLE "Professor" (
  "rga" char(12) PRIMARY KEY,
  "pessoa" char(11),
  "unidade" int,
  "contato" uuid
);

CREATE TABLE "Unidade" (
  "id" int PRIMARY KEY,
  "nome" varchar(32)
);

CREATE TABLE "Curso" (
  "id" int PRIMARY KEY,
  "nome" varchar(32),
  "unidade" int
);

ALTER TABLE "Pessoa" ADD FOREIGN KEY ("contato") REFERENCES "Contato" ("id");

ALTER TABLE "Pessoa" ADD FOREIGN KEY ("endereco") REFERENCES "Endereco" ("id");

ALTER TABLE "Estudante" ADD FOREIGN KEY ("pessoa") REFERENCES "Pessoa" ("cpf");

ALTER TABLE "Estudante" ADD FOREIGN KEY ("curso") REFERENCES "Curso" ("id");

ALTER TABLE "Estudante" ADD FOREIGN KEY ("unidade") REFERENCES "Unidade" ("id");

ALTER TABLE "Estudante" ADD FOREIGN KEY ("contato") REFERENCES "Contato" ("id");

ALTER TABLE "Professor" ADD FOREIGN KEY ("pessoa") REFERENCES "Pessoa" ("cpf");

ALTER TABLE "Professor" ADD FOREIGN KEY ("unidade") REFERENCES "Unidade" ("id");

ALTER TABLE "Professor" ADD FOREIGN KEY ("contato") REFERENCES "Contato" ("id");

ALTER TABLE "Curso" ADD FOREIGN KEY ("unidade") REFERENCES "Unidade" ("id");
