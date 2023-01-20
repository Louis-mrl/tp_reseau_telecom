notes = []
coefficients = []
for i in range(5):
    note_coefficient = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ").split()
    notes.append(float(note_coefficient[0]))
    coefficients.append(int(note_coefficient[1]))

moyenne = sum([note * coef for note, coef in zip(notes, coefficients)]) / sum(coefficients)

if moyenne < 8:
    print("L'étudiant à échoué.")
elif min(notes) < 8:
    print("L'étudiant à échoué.")
elif moyenne < 10:
    print("L'étudiant est reçu.")
else:
    print("L'étudiant est admis.")
