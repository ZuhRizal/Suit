from random import choice
import json
import operator


class Main:
	def enemy(self):
		# Pick random Enemy's card
		enemy = ["Batu","Gunting","Kertas"]
		return choice(enemy)

	def info(self,mS,eS):	# mS is My Scores, eS is Enemy Scores
		print(f"""
Game Suit Jawa
==============
Hasil	: {"Menang" if abs(mS-eS) >= eS else "Kalah"}
Player	: {mS}
Com		: {eS}

""")

	def highscore(self,S,N="Anonym"):				# S is score and N is name
		with open("datascore.json") as json_file:	# Open file
			file = json.load(json_file)				# Show file
			
		file["Score"][f"{N}"] = S					# Append key and value

		with open("datascore.json", "w") as json_file:
			json.dump(file, json_file, indent=4)

		with open("highscore.txt","w") as f:
			for n,s in file["Score"].items():
				f.write(f"{n} : {s} \n")

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
		mS = 0
		eS = 0
		with open("UI.json") as json_file:
			file = json.load(json_file)
			for f in file["MainMenu"]:
				print(f)

			# Main loop
			while True:
				menu = int(input("Pilih Menu : "))
				if menu > 3 or menu < 1:
					print("Maaf angka yang anda masukkan tidak tersedia di pilihan \n")

				if menu == 1:
					for f in file["Card"]:
						print(f)

					while True:
						try:
							card = int(input("Pilih Kartu : "))

						except ValueError:
							print("Maaf yang anda masukkan tidak tersedia di pilihan \n")
							continue

						else:
								rslt = self.rules(card, self.enemy())
								self.info(mS, eS)

								if rslt == "Menang":
									mS += 1
								else:
									eS += 1

								if card == 9:
									mS,eS = 0,0
								
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
					with open("UI.json") as f:
						file = json.load(f)
						for i in file["Score"]:
							print(i)
					with open("datascore.json") as f:
						file = json.load(f)
						for n,i in enumerate(file["Score"].items()):
							print(f"[{n+1}] {i[0]} : {i[1]}")
			
				if menu == 3:
					break