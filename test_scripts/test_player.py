from models.player import Player
from models.team import Team
from models.match import Match

p = Player("diaa", 1, "Midfielder")
p.save_to_db()

t = Team("Red Lions", "Coach Zaki")
t.save_to_db()

m = Match("Team A", "Team B", "2025-05-19", 2, 1)
m.save_to_db()