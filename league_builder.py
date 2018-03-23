import csv
import random

def write_file_clear(thing):
	with open('teams.txt', 'w') as file:
		file.write(thing + '\n')

def write_file(thing):
	with open('teams.txt', 'a') as file:
		file.write(thing + '\n')

def write_letter1(player_name, guardian_name, team_name):
	name = '_'.join(player_name.lower().split()) + '.txt'

	with open(name, 'w') as file:
		file.write('Dear ' + guardian_name + '\n')
		file.write('We want to announce that ' + player_name + ' is chosen to be a member of ' + team_name + '\n')
		file.write('Date and Time of first practice: TBA')


dragons = []
dragons_exp = []
sharks = []
sharks_exp = []
raptors = []
raptors_exp = []

if __name__ == '__main__':

	with open('soccer_players.csv', newline='') as csvfile:
		sp_reader = csv.DictReader(csvfile, delimiter = ',')
		rows = list(sp_reader)

		for row in rows:
			if row['Soccer Experience'] == 'YES':
				teams = ['Dragons', 'Sharks', 'Raptors']
				if len(dragons_exp) == 3:
					teams.remove('Dragons')
				if len(sharks_exp) == 3:
					teams.remove('Sharks')
				if len(raptors_exp) == 3:
					teams.remove('Raptors')

				chosen_team = random.choice(teams)
				if chosen_team == 'Dragons':
					dragons_exp.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )
				
				elif chosen_team == 'Sharks':
					sharks_exp.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )

				elif chosen_team == 'Raptors':
					raptors_exp.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )

			elif row['Soccer Experience'] == 'NO':
				teams = ['Dragons', 'Sharks', 'Raptors']
				if len(dragons) == 3:
					teams.remove('Dragons')
				if len(sharks) == 3:
					teams.remove('Sharks')
				if len(raptors) == 3:
					teams.remove('Raptors')

				chosen_team = random.choice(teams)
				if chosen_team == 'Dragons':
					dragons.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )
				
				elif chosen_team == 'Sharks':
					sharks.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )

				elif chosen_team == 'Raptors':
					raptors.append([row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']] )		

		dragons += dragons_exp
		sharks += sharks_exp
		raptors += raptors_exp


		write_file_clear('Dragons')
		for player in dragons:
			dragon_mem = ', '.join(player)
			write_file(dragon_mem)
		write_file('')

		write_file('Sharks')
		for player in sharks:
			shark_mem = ', '.join(player)
			write_file(shark_mem)
		write_file('')

		write_file('Raptors')
		for player in raptors:
			raptor_mem = ', '.join(player)
			write_file(raptor_mem)	
		write_file('')	

		for player in dragons:
			player_name = player[0]
			guardian_name = player[3]
			team_name = 'Dragons'
			write_letter1(player_name, guardian_name, team_name)

		for player in sharks:
			player_name = player[0]
			guardian_name = player[3]
			team_name = 'Sharks'
			write_letter1(player_name, guardian_name, team_name)

		for player in raptors:
			player_name = player[0]
			guardian_name = player[3]
			team_name = 'Raptors'
			write_letter1(player_name, guardian_name, team_name)
	

