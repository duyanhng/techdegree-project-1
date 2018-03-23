import csv

if __name__  == '__main__':
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')

    for player in player_reader.items():
        print(player)

    with open('teams.txt', 'a') as file:
        file.write(team_name + "/n" + player_name + ", " + experience + ", " + guardian_name)


    with open('soccer_players.csv') as csvfile:
        player_reader = csv.reader(csvfile, delimiter=',')
        rows = list(player_reader)
        for row in rows:
                print(row)