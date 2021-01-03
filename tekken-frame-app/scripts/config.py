import os

parsers = {"html": "html.parser"}
data_path = os.getcwd() + "/tekken-frame-app/data"
tekken7_dpath = data_path + "/tekken_7"

datasources = {
    "tekken6": "http://www.avoidingthepuddle.com/tekken-6-frame-data",
    "tekkentag2": "https://rbnorway.org/ttt2-frame-data/",
    "tekken7": "https://rbnorway.org/t7-frame-data/"
}