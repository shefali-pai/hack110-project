
points: int = 0
def find_princess(hobby: str, color: str) -> str:
    global points

    if hobby == "spending time in nature":
        points = points + 1 
    elif hobby == "singing":
        points = points + 2
    elif hobby == "swimming":
        points = points + 3
    elif hobby == "reading":
       points = points + 4
    if color == "green":
        points = points + 1
    if color == "red":
        points = points + 2
    if color == "blue":
        points = points + 3
    if color == "yellow":
        points = points + 4
    
    if points % 2:
        return "Princess Aurora"
    elif points % 3:
        return "Princess Belle"
    elif points % 4:
        return "Princess Cinderella"
    else: 
        return "Princess Ariel"

def link_getter(princess: str) -> str:
    if princess == 'Princess Belle':
        return f"/static/belle.jpeg"
    elif princess == 'Princess Ariel':
        return f"/static/Ariel.png"
    elif princess == "Princess Cinderella":
        return f"/static/Cinderella.png"
    else:
        return f"/static/Aurora.jpeg"





    
class user:
    id: int
    first_name: str
    last_name: str
    princess: str
    

    def __init__(self, id: int, fname: str, lname: str, princess: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.princess = princess
    

