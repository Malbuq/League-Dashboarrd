import pandas as pd
import getting_match_data as md
import time

columns = {
    'isBeaOn': [],
    'isCarolOn': [],
    'isMichaelOn': [],
    'isNoon': [],
    'giselleKnowsHowToPlay': [],
    'michaelKnowsHowToPlay': [],
    'carolKnowsHowToPlay': [],
    'beaKnowsHowToPlay': [],
    'champion1': [],
    'champion2': [],
    'champion3': [],
    'champion4': [],
    'champion5': [],
    'weWon':[],
    'isGadoOn':[],
    'weHaveTank': [],
    'weHaveAdc': [],
    'weHaveApc': [],
    'weHaveBruiser': [],
    'weHaveSup': [],
    'gameDateMilliseconds':[],
    'matchId':[]
}

df = pd.DataFrame(columns)

file_path = 'matches_id.txt'

count = 0
with open(file_path, 'r') as file:
    for line in file:
        if(count == 100):
            count = 0
            print(f'ja fez {count}')
            matchId = line.strip()
            newRow = md.convertingMatchToRow(matchId)
            df = df._append(newRow, ignore_index=True)
            count += 1

        matchId = line.strip()
        newRow = md.convertingMatchToRow(matchId)
        df = df._append(newRow, ignore_index=True)
        count += 1

output_file_path = 'matches_data.csv'
df.to_csv(output_file_path, index=False)

