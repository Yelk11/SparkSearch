DROP TABLE IF EXISTS hello;

CREATE TABLE hello (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
