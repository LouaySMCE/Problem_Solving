import csv
import pandas as pd

a = pd.read_csv("notes_java.csv")
b = pd.read_csv("notes_uml.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='id')
merged.to_csv("notes_all.csv", index=False)
notes = pd.read_csv("notes_all.csv")

with open('notes_all.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

def convert(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j].isdigit():
                L[i][j]= int(L[i][j])
    return L
all_notes = convert(data)

def moyenne(L):
    moyennes = []
    for i in range(1,len(L)):
        s = 0
        moyennes.append(L[i][0])
        for j in range(1, len(L[i])):
            s += L[i][j]
        moyennes.append(s/(len(L[i])-1))
    return moyennes

def releve(releve_moyenne, releve_all):
    for i in range(0,len(releve_moyenne),2):
        releve_de_note = open(f"{releve_moyenne[i]}.txt", "w")
        releve_de_note.write("==========================\n")
        releve_de_note.write("==Relevé de note de" + str(releve_moyenne[i]))
        releve_de_note.write("==\n")
        releve_de_note.write("==========================\n")



print(all_notes)
