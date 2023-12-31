players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


class Player:
    new_team = []

    def __init__(self, index):
        self.name = players[index]["name"]
        self.age = players[index]["age"]
        self.position = players[index]["position"]
        self.team = players[index]["team"]
        
    
    @classmethod
    def get_team(cls,team_list):
        Player.new_team = [dict() for x in range(len(team_list))]
        for i in range(len(team_list)):
            Player.new_team[i]["age"]=Player(i).age
            Player.new_team[i]["name"]=Player(i).name
            Player.new_team[i]["position"]=Player(i).position
            Player.new_team[i]["team"]=Player(i).team
        print(Player.new_team)

        
Player.get_team(players)
