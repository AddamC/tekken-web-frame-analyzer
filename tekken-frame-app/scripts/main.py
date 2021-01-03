import requests
import pandas as pd
import webbrowser as wb
import os
import config
from character import Character, Move
from bs4 import BeautifulSoup

header = {"command": 1, "hitlevel": 2, "damage": 3, "Start up frame": 4,
          "Block frame": 5, "Hit frame": 6, "Counter Hit frame": 7, "Notas": 8}


def write_character_html_file(char_name, content):
    file = open(os.getcwd() + "\\data\\raw\\" +
                char_name + "_frame_data.html", "w")
    file.write(content)
    file.close()
    print("frame data saved in: " + file.name)


def get_html_data(url, parser):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text[0:], parser)
    return soup


def open_file_browser(character, debug=False):
    filename = character + "_frame_data.html"
    filepath = "file:///" + os.getcwd() + "/" + filename.replace("\\", "/")
    wb.open_new_tab(filepath)
    if debug:
        print(os.getcwd() + "\n\t" + filename)


def table_config(table):
    table.columns(header.keys())


def color_for_values(val):
    val = str(val)
    if val.startswith("-"):
        color = "red"
    elif val.startswith("+"):
        color = "green"
    else:
        color = "white"
    return "background-color: %s" % color


def save_html_locally(file_name, content):
    html_file = open(file_name, "w")
    html_file.write(content)
    html_file.close()

def write_new_table(table, character):
    #new_table = pd.read_html("<table>" + str(character_inputs) + "</table>")[0]
    new_table = pd.read_html(str(table), header=0)[0]

    new_table.columns = header.keys()
    # print(type(new_table["damage"]))
    filtro = new_table[new_table["command"].str.contains("", na=False)]
    tabela = filtro.style.applymap(color_for_values)

    # print(new_table.to_html())
    # write_character_html_file(new_table.to_html())
    write_character_html_file(character, tabela.render())


def get_tekken7_content(get_local):
    characters = ["akuma", "king", "miguel", "xiaoyu", "alisa", "jin", "gigas", "hwoarang",
                  "claudio", "noctis", "law", "kazuya", "heihachi", "lars", "nina", "katarina"]

    failed_entries = []
    for character in characters[1:2]:
        try:
            completion = characters.index(character) / len(characters) * 100
            print("status: " + str(completion) + "%")

            print("acquiring frame data from: " + character)
            file_name = config.data_path + "/tekken_7/" + character + ".html"

            if get_local:
                html_file = open(file_name, "r")
                document = BeautifulSoup(html_file, 'html.parser')
                table = document.find("table")
            else:
                url = "https://rbnorway.org/" + character + "-t7-frames"
                document = get_html_data(url, 'html.parser')
                table = document.find_all("table")[0]  # Pega a primeira tabela
                moveset_data = table.find_all("tr")[1:]

                save_html_locally(file_name, str(table))

            moveset = [move_data.get_text().split('\n') for move_data in moveset_data]
            c = Character()
            c.char_name = character
            for move_data in moveset[0:2]:
                move = Move(move_data)
                c.moves.append(move.__dict__)

            print(c.to_json())

            # write_new_table(table, character)

        except Exception as err:
            print(err)
            failed_entries.append(character)
            print("\tError - " + character)
            continue

        if len(failed_entries) > 0:
            print("\nError while obtaining the following frame datas:\n")
            for entry in failed_entries:
                print("\t- " + entry)


if __name__ == "__main__":
    get_tekken7_content(False)

# conteudo retornado
# open_file_browser("law", True)
