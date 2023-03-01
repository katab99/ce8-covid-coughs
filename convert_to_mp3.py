import os
from pydub import AudioSegment
import pandas as pd 

# to read metadata
PATH = "./data/metadata_compiled.csv"
df = pd.read_csv(PATH)

df = df[pd.notna(df['status'])]


def convert_to_mp3(path_to_file):

    for dirname, _, filenames in os.walk(path_to_file):
        for filename in filenames:
            print(os.path.join(dirname, filename))
            
            if "webm" in filename:
                FILE = filename.replace(".webm", "")

                if FILE in df['uuid'].unique():
                    INPUT = dirname + filename
                    OUTPUT = "./conv/" + filename + ".mp3"
                    OUTPUT = OUTPUT.replace(".webm", "")

                    print("----")
                    print("inpit", INPUT)
                    print("outpit test", OUTPUT)
                    print("----")

                    AudioSegment.from_file(INPUT).export(OUTPUT, format="mp3")

            elif "ogg" in filename: 
                FILE = filename.replace(".ogg", "")

                if FILE in df['uuid'].unique():
                    INPUT = dirname + filename
                    OUTPUT = "./conv/" + filename + ".mp3"
                    OUTPUT = OUTPUT.replace(".ogg", "")

                    print("----")
                    print("inpit", INPUT)
                    print("outpit test", OUTPUT)
                    print("----")

                    AudioSegment.from_file(INPUT).export(OUTPUT, format="mp3")

    pass



convert_to_mp3('./soundfiles/')