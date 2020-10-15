import config
from bs4 import BeautifulSoup
from character import Move

def extract_from_character(game = "tekken7"):
    data_path = config.tekken7_dpath if game == "tekken7" else "" 
    data_path += "\\law.html"
    movelist_html_file = open(data_path, 'r')
    
    soup = BeautifulSoup("\n".join(movelist_html_file.readlines()), 'html.parser')
    movelist_html_file.close()

    # obtem os movimentos e extrai eles para o objeto Move
    moves_rows = soup.find_all("tr")
    movelist = []
    for row in moves_rows[1:3]:
        index = 0
        move_data = []
        for column in row.find_all("td"):
            move_data.append(column.text)
            index = index + 1
        
        movelist.append(Move(move_data))
    print(movelist[0])


extract_from_character()