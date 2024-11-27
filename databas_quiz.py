import random
import json

questions = [
    "Vad är en entitet?",
    "Vad är attribut?",
    "Vilka typer av relationer kan det finnas mellan olika objekt i en modell?",
    "Vad är en ER-modell ?",
    "Vad är huvudsyftet med normalisering ? Vad innebär det?",
    "Vilka olika normalformer finns det?",
    "Vad är denormalisering?",
    "Hur anges att en kolumn i en fysisk databas inte kan innehålla null värden?",
    "Vad är en constraint. Varför används constraints?",
    "Vilka typer av nycklar finns det i en fysisk databas? Vad är skillnaden mellan dessa?",
    "Vad är en kopplingstabell?",
    "Vilket syfte har ett index i en fysisk databas? Hur fungerar ett index?",
    "Vad är redundans?",
    "Vad är data integrity? Varför är det viktigt ?",
    "Vad är en AUTO_INCREMENT i en MySQL db? Vad används den till?",
    "Vad är SQL? Vad är skillnaden mellan SQL och MySQL?",
    "Vad är en query?",
    "Vad är en post i en tabell?",
    "Vad betyder CRUD?",
    "Nämn åtminstone 5 inbyggda funktioner som finns i SQL. Nämn åtminstone 1 funktion som är unik för MySQL.",
    "När används DISTINCT och COUNT?",
    "Hur används ORDER BY?",
    "Vad är en INNER JOIN? Hur gör man för att skapa den?",
    "Hur gör man för att lägga in en ny rad i en tabell?",
    "Hur gör man för att uppdatera en rad i en tabell?",
    "Hur gör man för att ta bort en rad i en tabell?",
    "Vad är ett alias i en query? Hur anges det?",
    "Hur tar man fram dagens datum i MySQL?",
    "Hur fungerar LIKE? Vad används det ofta till när man bygger applikationer?",
    "Vad är en stored procedure?",
    "Vad är skillnaden mellan en stored procedure och dynamisk SQL?",
    "Hur tar man bort en stored procedure?",
    "Vad är en SQL view?",
    "Vad är ofta syftet med att använda views?",
    "Vad innebär en GROUP BY?",
    "Hur sätts villkor i en GROUP BY?",
    "Vad är en subselect?",
    "Hur kopplas en subselect ihop med en huvudfråga?",
    "Hur görs en subselect i SELECT delen av en fråga?",
    "Hur görs en subselect i WHERE delen av en fråga?",
]
answers = []
while len(questions) > 0:
    question = random.choice(questions)
    answer = input(f"{question}\n")
    answer_set = {"question": question, "answer": answer}
    answers.append(answer_set)
    questions.remove(question)
print(answers)

FILE_PATH = "./quiz.json"

with open(FILE_PATH, "w", encoding="utf-8") as output_file:
    json.dump(answers, output_file, indent=2, ensure_ascii=False)
