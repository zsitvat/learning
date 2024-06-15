CREATE TABLE IF NOT EXISTS tasks(
id      int  PRIMARY KEY,
name    VARCHAR      NOT NULL,
description VARCHAR,
status    VARCHAR  NOT NULL,
created_at TIMESTAMP    NOT NULL,
updated_at TIMESTAMP    NOT NULL
);