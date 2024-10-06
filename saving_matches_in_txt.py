import requests

ipien_puuid = 'e_H-NaW6U88XCDjiUm0PtE11bXww5s0j7sbM4c9iuRAXZ8aAx7ZUYuHslueTVfivFnD2ioMfyZqS1Q'
api_key = 'RGAPI-9113d852-c423-4a20-9cac-3d268fe4df55'

def verify_api_key():
    global api_key
    api_key = input('Input your api key: ')

def get_quantity_matches():
    return int(input('Starting from the most recent one, how many matches you want?\nAnswer: '))

def write_matches_id_in_file(quantity_matches):
    url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{ipien_puuid}/ids?api_key={api_key}'

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")

    matchlist_data = response.json()

    with open(r'C:\Users\micha\Desktop\Project\League of Legends\matches_id.txt', 'a') as file:
        for i in range(quantity_matches):
            file.write(matchlist_data[i] + '\n')
    
    print('Matches were saved in the file')

def main():
    write_matches_id_in_file(20)

main()
