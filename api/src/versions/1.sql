CREATE TABLE player (
  id serial PRIMARY KEY,
  name text NOT NULL,
  hidden text[] DEFAULT '{}',
  visible text[] DEFAULT '{}',
  flowers text[] DEFAULT '{}',
  discard text[] DEFAULT '{}',
  drawn_tile text DEFAULT NULL
);
