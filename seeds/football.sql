-- -- -- Drop existing tables and types
-- DROP TABLE IF EXISTS game_result CASCADE;
-- DROP TABLE IF EXISTS game_week CASCADE;
-- DROP TABLE IF EXISTS manager_squad CASCADE;
-- DROP TABLE IF EXISTS manager_player CASCADE;
-- DROP TABLE IF EXISTS player CASCADE;
-- DROP TABLE IF EXISTS season CASCADE;
-- DROP TABLE IF EXISTS squad CASCADE;
-- DROP TABLE IF EXISTS manager CASCADE;

-- Drop existing tables and types
DROP TABLE IF EXISTS game_results;
DROP TABLE IF EXISTS game_weeks;
DROP TABLE IF EXISTS managers_squads;
DROP TABLE IF EXISTS managers_players;
DROP TABLE IF EXISTS squads_players;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS squads;
DROP TABLE IF EXISTS managers;
DROP TYPE IF EXISTS player_position_enum CASCADE;

-- DROP TYPE player_position_enum;
CREATE TYPE player_position_enum AS ENUM ('goalkeeper', 'defender', 'midfielder', 'attacker');


-- Create sequences if needed
CREATE SEQUENCE IF NOT EXISTS managers_id_seq;
CREATE SEQUENCE IF NOT EXISTS squads_id_seq;
CREATE SEQUENCE IF NOT EXISTS players_id_seq;
CREATE SEQUENCE IF NOT EXISTS managers_players_seq;
CREATE SEQUENCE IF NOT EXISTS managers_squads_seq;
CREATE SEQUENCE IF NOT EXISTS squads_players_seq;
CREATE SEQUENCE IF NOT EXISTS seasons_id_seq;
CREATE SEQUENCE IF NOT EXISTS game_weeks_id_seq;

-- Create manager table
CREATE TABLE managers (
    id SERIAL PRIMARY KEY,
    manager_name VARCHAR(255),
    manager_email VARCHAR(255),
    squads INTEGER[],
    players INTEGER[] 
);

-- Create squad table
CREATE TABLE squads (
    id SERIAL PRIMARY KEY,
    squad_name VARCHAR(255)
);

-- Create player table
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(255),
    player_position player_position_enum,
    player_points INTEGER DEFAULT 0,
    player_goals_for INTEGER DEFAULT 0,
    player_goals_against INTEGER DEFAULT 0
);

-- Create season table
CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    season_start_date DATE,
    season_length INTEGER,
    game_weeks INTEGER[],
    season_complete BOOLEAN DEFAULT FALSE,
    squad_id INTEGER REFERENCES squads(id)
);

-- Create game_week table
CREATE TABLE game_weeks (
    id SERIAL PRIMARY KEY,
    week_number INTEGER,
    game_week_date DATE,
    availability_full BOOLEAN DEFAULT FALSE,
    black_team_list INTEGER[],
    white_team_list INTEGER[],
    game_result BOOLEAN,
    season_id INTEGER REFERENCES seasons(id)
);

-- Create game_result table
CREATE TABLE game_results (
    id SERIAL PRIMARY KEY,
    black_team_list INTEGER[],
    white_team_list INTEGER[],
    final_score JSONB,
    winning_team VARCHAR(50),
    game_week_id INTEGER REFERENCES game_weeks(id)
);


CREATE TABLE managers_squads (
    manager_id INTEGER REFERENCES managers(id),
    squad_id INTEGER REFERENCES squads(id),
    PRIMARY KEY (manager_id, squad_id)
);

CREATE TABLE managers_players (
    manager_id INTEGER REFERENCES managers(id),
    player_id INTEGER REFERENCES players(id),
    PRIMARY KEY (manager_id, player_id)
);

CREATE TABLE squads_players (
    squad_id INTEGER REFERENCES squads(id),
    player_id INTEGER REFERENCES players(id),
    PRIMARY KEY (squad_id, player_id)
);
-- CREATE TABLE squad_player (
--     manager_id INTEGER REFERENCES manager(id),
--     player_id INTEGER REFERENCES player(id),
--     PRIMARY KEY (manager_id, player_id)
-- );

-- Insert data into manager table
INSERT INTO managers (manager_name, manager_email) VALUES
    ('Lee', 'lee@example.com'),
    ('Santi', 'santi@example.com');

-- Insert data into squad table
INSERT INTO squads (squad_name) VALUES
    ('Monday night Mile End'),
    ('Weekend Shacklewell Sharks');

-- Insert data into player table
INSERT INTO players (player_name, player_position) VALUES
    ('Tiago', 'defender'),
    ('Ehren', 'defender'),
    ('Toby', 'midfielder'),
    ('San', 'defender'),
    ('VD', 'defender'),
    ('Nils', 'midfielder'),
    ('Marco', 'midfielder'),
    ('Lee', 'midfielder'),
    ('Seb', 'attacker'),
    ('Kieran', 'midfielder'),
    ('Angus', 'defender'),
    ('Avi', 'midfielder'),
    ('Giacomo', 'midfielder'),
    ('Iain', 'midfielder'),
    ('David', 'midfielder');

INSERT INTO managers_squads(manager_id, squad_id) VALUES
    (1, 1),
    (2, 2);


INSERT INTO managers_players(manager_id, player_id) VALUES
    (1, 1),
    (2, 2),
    (2, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (2, 11),
    (2, 12),
    (2, 13),
    (2, 14),
    (1, 15);


INSERT INTO squads_players(squad_id, player_id) VALUES
    (1, 1),
    (2, 2),
    (2, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (2, 11),
    (2, 12),
    (2, 13),
    (2, 14),
    (1, 15);

-- Insert data into season table
INSERT INTO seasons (season_start_date, season_length, game_weeks, squad_id) VALUES
-- id, 
    ('2024-04-01', 12, ARRAY[]::INTEGER[], 1),
    ('2024-04-07', 12, ARRAY[]::INTEGER[], 2);

-- Insert data into game_week table
INSERT INTO game_weeks ( week_number, game_week_date, season_id) VALUES
-- id,
    (1, '2024-03-25', 1),
    (2, '2024-03-25', 1),
    (3, '2024-03-25', 1),
    (4, '2024-03-25', 1),
    (5, '2024-03-25', 1),
    (6, '2024-03-25', 1),
    (7, '2024-03-25', 1),
    (8, '2024-03-25', 1),
    (9, '2024-03-25', 1),
    (10,'2024-03-25', 1),
    (11,'2024-03-25', 1),
    (12,'2024-03-25', 1),
    (1, '2024-03-25', 2),
    (2, '2024-03-25', 2),
    (3, '2024-03-25', 2),
    (4, '2024-03-25', 2),
    (5, '2024-03-25', 2),
    (6, '2024-03-25', 2),
    (7, '2024-03-25', 2),
    (8, '2024-03-25', 2),
    (9, '2024-03-25', 2),
    (10, '2024-03-25', 2),
    (11, '2024-03-25', 2),
    (12, '2024-03-25', 2);

-- INSERT INTO game_result (week_number, season_id) VALUES


-- Insert data into game_result table (empty for now, to be populated during tests)
-- INSERT INTO game_result (black_team_list, white_team_list, final_score, winning_team) VALUES
--     (ARRAY[1, 2], ARRAY[3], '{"black_team": 2, "white_team": 1}', 'black_team');

