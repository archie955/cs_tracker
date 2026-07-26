# Current outline of database schema

## Tables:

Users, Matches, PlayerMatches, Weapons, Grenades, Player Opens, Player Clutches, Player Side? (unsure)

easy to calculate data leave, harder to calculate can be pre done and stored, such as ADR in each PlayerMatch. Potentially pre-compute total data per player for each game mode, so PlayerPremier already aggregates statistics for premier, so I don't need to recalculate every single statistic by querying playermatch to find all player-server combos. If I include things like number of games and number of round, then calculating total stats can be done from there with absolute ease.