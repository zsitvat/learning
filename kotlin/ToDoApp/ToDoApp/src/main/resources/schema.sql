create table if not exists tasks(
name    VARCHAR      NOT NULL,
id      int  PRIMARY KEY,
description VARCHAR,
status    VARCHAR  NOT NULL,
deadline DATE,
userId  INT NOT NULL,
created_at TIMESTAMP    NOT NULL,
updated_at TIMESTAMP    NOT NULL
);