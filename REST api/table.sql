CREATE TABLE IF NOT EXISTS exercises(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  type INTEGER NOT NULL,
  complexity INTEGER NOT NULL
)
