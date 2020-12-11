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
Com	: {eS}

""")

	def highscore(self,S,N="Anonym"):				# S is score and N is name
		with open("datascore.json") as json_file:	# Open file
			file = json.load(json_file)				# Show file
			
		file["Score"][f"{S}"] = N.capitalize()		# Append key and value

		with open("datascore.json", "w") as json_file:
			json.dump(file, json_file, indent=4,sort_keys=True)

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
		# Main loop
		while True:
			with open("UI.json") as json_file:
				file = json.load(json_file)
				for f in file["MainMenu"]:
					print(f)

			menu = int(input("Pilih Menu : "))
			print("")
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
								self.highscore(mS,user)
								mS,eS = 0,0
								break

			if menu == 2:
				for i in file["Score"]:
					print(i)
				with open("datascore.json") as f:
					file = json.load(f)
					for n,i in enumerate(reversed(list(file["Score"].items()))):
						print(f"[{n+1}] {i[1]} : {i[0]}")
					else: 
						print(f"""
[-] Ketik DEL untuk menghapus score
[-] Ketik MENU untuk kembali ke main menu
""")

				try:
					order = input("Tulis Perintah : ")
				except ValueError:
					print("Maaf yang anda masukkan tidak tersedia di pilihan \n")
					continue
				else:
					if order == "DEL":
						score = int(input("Masukan nomor highscore : "))
						if score == 0:
							pass

						else:
							with open("datascore.json") as json_file:	# Open file
								file = json.load(json_file)				# Show file

							delete = list(file["Score"].items())		# Create new variable that toward into specific data file
							del delete[len(delete)-score]				# Delete selected data
							file["Score"] = dict(delete)				# Open specific data file location
							
							with open("datascore.json", "w") as json_file:
								json.dump(file, json_file, indent=4,sort_keys=True)

					if order == "MENU":
						pass
		
			if menu == 3:
				break
