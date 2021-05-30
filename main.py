from menu import menu_list
from random import choice
from typing import List, Union
import json


class Main:
    def __init__(self):
        self._score: int = 0
        self._enemyScore: int = 0
        self.__card: List[str] = ["B", "G", "K"]

    @property
    def enemy(self) -> str:
        return self.__card

    def info(self):
        print(f"""
Game Suit Jawa
==============
Hasil	: {"Menang" if self._score >= self._enemyScore else "Kalah"}
Player	: {self._score}
Com	: {self._enemyScore}
""")

    def highscore(self):
        print(menu_list[2])
        with open("score.json") as json_file:
            print("\n".join(f"  [{n+1}] {i[1]} : {i[0]}" for n, i in enumerate(reversed(list(json.load(json_file)["Score"].items())))))
            print(f"""
  [-] Ketik DEL untuk menghapus score
  [-] Ketik MENU untuk kembali ke main menu
""")

    def add_score(self, name: str="Anonym"):
        with open("score.json") as json_file:
            file = json.load(json_file)
        file["Score"][str(self._score)] = name.capitalize()
        with open("score.json","w") as json_file:
            json.dump(file, json_file, indent=4, sort_keys=True)

    def del_score(self, num: int):
        with open("score.json") as json_file:
            file = json.load(json_file)
        delete = list(file["Score"].items())
        del delete[len(delete) - num]
        file["Score"] = dict(delete)
        with open("score.json","w") as json_file:
            json.dump(file, json_file, indent=4, sort_keys=True)

    def iswin(self, user: str, enemy: str, result: bool=False) -> bool:
        user = self.enemy[user-1]
        if (user == "B" and enemy == "G") or (user == "G" and enemy == "K") or (user == "K" and enemy == "B"):
            return True
        elif user == enemy:
            self._enemyScore -= 1
            return result
        else:
            return result

    def play(self):
        global menu_list
        while True:
            print(menu_list[0])
            menu = int(input("Pilih Menu : "))
            if menu == 1:
                print(menu_list[1])
                while True:
                    card = int(input("Pilih Kartu : "))
                    self.info()
                    if card in [1,2,3,9,0]:
                        if self.iswin(card, choice(self.enemy)):
                            self._score += 1
                        else:
                            self._enemyScore += 1

                        if card == 9:
                            self._score, self._enemyScore = 0, 0

                        if card == 0:
                            print("Beri nama untuk menyimpan highscore")
                            self.add_score(input("Masukkan nama : "))
                            break
                self._score, self._enemyScore = 0, 0
            if menu == 2:
                self.highscore()

                order = input("Tulis Perintah : ")
                if order == "DEL":
                    num = int(input("Masukan nomor highscore : "))
                    self.del_score(num)
            if menu == 3:
                break

if __name__ == "__main__":
    Main().play()