from random import choice
import json


class Main:
	def enemy(self):
		# Pick random Enemy's card
		enemy = ["Batu","Gunting","Kertas"]
		return choice(enemy)

	def highscore(self,S,N="Anonym"):
		with open("UI.json") as json_file: # Open file
			file = json.load(json_file) # Show file
			
			name = file["Player"]["Name"]
			score = file["Player"]["Score"]
			
			name.append(N)
			score.append(S)
			with open("highscore.txt","a") as f:
				for n,i in enumerate(name):
					f.write(f"{i} : {score[n]} \n")

	def rules(self,U,E):
		# The rules that you can win, lose, or draw
		# U is user
		# E is enemy
		if U == 1:
			if E == "Batu":
				return "Seri"
			elif E == "Gunting":
				return "Menang"
			elif E == "Kertas":
				return "Kalah"
		elif U == 2:
			if E == "Batu":
				return "Kalah"
			elif E == "Gunting":
				return "Seri"
			elif E == "Kertas":
				return "Menang"
		elif U == 3:
			if E == "Batu":
				return "Menang"
			elif E == "Gunting":
				return "Kalah"
			elif E == "Kertas":
				return "Seri"
		else:
			return ""

	def play(self):
		score = 0
		with open("UI.json") as json_file:
			file = json.load(json_file)
			for f in file["MainMenu"]:
				print(f)

			# Main loop
			while True:
				# Error handling
				try:
					menu = int(input("Pilih Menu : "))
				# When error happend
				except ValueError:
					print("Maaf yang anda masukkan tidak tersedia di pilihan \n")
				# When program run without error
				else:
					if menu > 3 or menu < 1:
						print("Maaf angka yang anda masukkan tidak tersedia di pilihan \n")

					if menu == 1:
						for f in file["Card"]:
							print(f)

						while True:
							try:
								card = int(input("Pilih Kartu : "))

							except ValueError:
								print("Maaf yang anda masukkan tidak tersedia di pilihan")
								continue

							else:
									rslt = self.rules(card, self.enemy())
									print(rslt,"\n")

									if rslt == "Menang":
										score += 1
										print(score)
									else:
										score += 0
									if card == 0:
										print("Beri nama untuk menyimpan highscore")
										user = input("Masukkan nama : ")
										print("\n")

										self.highscore(score,user)

										for f in file["MainMenu"]:
											print(f)
										score = 0
										break

					if menu == 2:
						with open("highscore.txt") as f:
							print(f.read())
				
					if menu == 3:
						break