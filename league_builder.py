import csv
import random

def write_file_clear(thing):
	with open('teams.txt', 'w') as file:
		file.write(thing + '\n')

def write_file(thing):
	with open('teams.txt', 'a') as file:
		file.write(thing + '\n')

def write_letter1(player_name, guardian_name, team_name):
	# Set up lower case _ separated file names
	name = player_name.lower().replace(' ', '_') + ".txt"

	with open(name, 'w') as file:
		file.write('Dear {},\n\n'
					'We want to announce that {} is chosen to be a member of {}\n'
					'Date and Time of first practice: TBA'.format(guardian_name, player_name, team_name))





if __name__ == '__main__':
	loop = True
	# Read the data from csv file
	with open('soccer_players.csv', newline='') as csvfile:
		sp_reader = csv.DictReader(csvfile, delimiter = ',')
		rows = list(sp_reader)

		while loop:
			dragons = []
			dragons_exp = []
			sharks = []
			sharks_exp = []
			raptors = []
			raptors_exp = []

			for row in rows:

				# Devide experienced players into 3 teams
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

				# Devide inexperienced players into 3 teams
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

			# Member lists of 3 teams
			dragons += dragons_exp
			sharks += sharks_exp
			raptors += raptors_exp

			# Avarage Height
			avr_height_dragon = 0
			for player in dragons:
				avr_height_dragon += int(player[1])
			avr_height_dragon /= len(dragons)


			avr_height_shark = 0
			for player in sharks:
				avr_height_shark += int(player[1])
			avr_height_shark /= len(sharks)


			avr_height_raptor = 0
			for player in raptors:
				avr_height_raptor += int(player[1])
			avr_height_raptor /= len(raptors)


			if avr_height_raptor <=42.6 and avr_height_raptor >= 42.2 and avr_height_shark<= 42.6 and avr_height_shark >= 42.2 and avr_height_dragon <= 42.6 and avr_height_dragon >= 42.2:
				loop = False
			else:
				continue	

		# Output teams.txt
		write_file_clear('Dragons:\n')
		for player in dragons:
			dragon_mem = ', '.join(player)
			write_file(dragon_mem)			
		write_file('\nAvarage height: {}\n\n'.format(avr_height_dragon))

		write_file('Sharks:\n')
		for player in sharks:
			shark_mem = ', '.join(player)
			write_file(shark_mem)
		write_file('\nAvarage height: {}\n\n'.format(avr_height_shark))

		write_file('Raptors:\n')
		for player in raptors:
			raptor_mem = ', '.join(player)
			write_file(raptor_mem)	
		write_file('\nAvarage height: {}\n\n'.format(avr_height_raptor))	

		# Output 18 letters
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
	


