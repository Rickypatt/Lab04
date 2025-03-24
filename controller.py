import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSpell(self,e):

        lingua = self._view._ddLingua.value
        if lingua is None:
            self._view._textOut.controls.append(ft.Text("Attenzione. Seleziona lingua!", color="red"))
            self._view.page.update()
            return

        modality = self._view._ddModality.value
        if modality is None:
            self._view._textOut.controls.append(ft.Text("Attenzione. Seleziona modalità!", color="red"))
            self._view.page.update()

        frase = self._view._frase.value
        if frase == "":
            self._view._textOut.controls.append(ft.Text("Attenzione. Scrivi la frase da tradurre!", color="red"))
            self._view.page.update()

        self._view._textOut.controls.append(ft.Text(f"Frase inserita: {frase}", color="green"))

        if self.handleSentence(frase,lingua,modality) != None:
            err, tempo = self.handleSentence(frase,lingua,modality)
            self._view._textOut.controls.append(ft.Text(f"Parole errate: {err}", color="green"))
            self._view._textOut.controls.append(ft.Text(f"Tempo impiegato: {tempo}", color="green"))

        self._view.page.update()

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None




    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

