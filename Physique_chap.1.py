import random

# Summary of Physics Course Concepts (Chap 1: Les Forces)
COURSE_SUMMARY = """
=== CHAPITRE 1 : LES FORCES ===

A) Représentation d'une force
   - Notation : F_(auteur/receveur) (ex: F_marteau/clou = 20 N)
   - Échelle : ex. 1 cm <=> 10 N
   - Caractéristiques :
     • Origine : le mot lié à "sur" (ex: sur le clou -> origine le clou)
     • Effet : ex. enfoncer le clou
     • Sens : ex. vers le bas
     • Droite d'action : ex. verticale

B) Définition
   Une force est l'action d'un corps sur un autre.
   Elle est caractérisée par :
     1. Un point d'application
     2. Une droite d'action
     3. Un sens
     4. Une intensité exprimée en newtons (N)

C) Exemples de forces

   1. Le Poids / Force d'attraction gravitationnelle / de pesanteur :
      - Formule : G = m * g (ou F_Terre/objet)
      - G : Force d'attraction gravitationnelle / Poids [N]
      - m : Masse de l'objet [kg]
      - g : Accélération de la pesanteur [N/kg ou m/s²]

   2. Loi de Hooke (s'applique au ressort) :
      - l0 : longueur du ressort à vide (sans masse) [m]
      - l1 : longueur du ressort avec masse [m]
      - Allongement : Δl = l1 - l0
      - Formule de la force : F_masse/ressort = k * Δl
      - k : Constante de raideur du ressort [N/m]
      - N.B. : Plus la constante de raideur k est élevée, plus le ressort est difficile à étirer.
      - k reste constante pour un même ressort, quelle que soit la masse accrochée.
"""

# Base de questions pour le questionnaire
QUESTIONS = [
    {
        "question": "Quelle est l'unité de l'intensité d'une force dans le Système International ?",
        "options": ["a) Joule (J)", "b) Newton (N)", "c) Kilogramme (kg)", "d) Watt (W)"],
        "answer": "b",
        "explanation": "L'intensité d'une force s'exprime en newtons (N)."
    },
    {
        "question": "Quelles sont les 4 caractéristiques qui définissent une force ?",
        "options": [
            "a) Point d'application, droite d'action, sens, intensité",
            "b) Masse, vitesse, accélération, temps",
            "c) Origine, longueur, poids, volume",
            "d) Raideur, longueur à vide, allongement, énergie"
        ],
        "answer": "a",
        "explanation": "Une force est caractérisée par un point d'application, une droite d'action, un sens et une intensité."
    },
    {
        "question": "Dans la formule du poids G = m * g, que représente la variable 'm' et quelle est son unité ?",
        "options": [
            "a) Le mètre, en [m]",
            "b) La masse de l'objet, en [kg]",
            "c) La constante de raideur, en [N/m]",
            "d) Le poids, en [N]"
        ],
        "answer": "b",
        "explanation": "'m' est la masse de l'objet exprimée en kilogrammes [kg]."
    },
    {
        "question": "Comment calcule-t-on l'allongement (Δl) d'un ressort ?",
        "options": [
            "a) Δl = l0 + l1",
            "b) Δl = l1 / l0",
            "c) Δl = l1 - l0",
            "d) Δl = k * l1"
        ],
        "answer": "c",
        "explanation": "L'allongement est la différence entre la longueur finale et la longueur à vide : Δl = l1 - l0."
    },
    {
        "question": "Dans la loi de Hooke (F = k * Δl), quelle est l'unité de la constante de raideur 'k' ?",
        "options": [
            "a) N/m",
            "b) N*m",
            "c) kg/m",
            "d) N/kg"
        ],
        "answer": "a",
        "explanation": "La constante de raideur k s'exprime en newtons par mètre [N/m]."
    },
    {
        "question": "Si un ressort est très difficile à étirer, que peut-on dire de sa constante de raideur k ?",
        "options": [
            "a) Elle est très faible",
            "b) Elle est égale à zéro",
            "c) Elle est très élevée",
            "d) Elle varie en fonction du temps"
        ],
        "answer": "c",
        "explanation": "Plus la constante de raideur k est élevée, plus le ressort est dur / difficile à étirer."
    }
]

def run_quiz():
    print("=== QUIZ : PHYSIQUE - CHAPITRE 1 (LES FORCES) ===")
    print("Tape 'q' à tout moment pour quitter le quiz.\n")
    
    score = 0
    shuffled_questions = QUESTIONS.copy()
    random.shuffle(shuffled_questions)
    
    for i, q in enumerate(shuffled_questions, 1):
        print(f"Question {i}/{len(shuffled_questions)} : {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
            
        user_ans = input("Ta réponse (a, b, c ou d) : ").strip().lower()
        if user_ans == 'q':
            print("Quiz interrompu.")
            return

        if user_ans == q['answer']:
            print(" -> BRAVO ! Bonne réponse.\n")
            score += 1
        else:
            print(f" -> INCORRECT. La bonne réponse était la ({q['answer']}).")
            print(f"    Explication : {q['explanation']}\n")
            
    print(f"--- Fin du quiz ! Ton score final : {score}/{len(shuffled_questions)} ---")

def main():
    while True:
        print("\n==========================================")
        print("  MENU PRINCIPAL - COURS DE PHYSIQUE")
        print("==========================================")
        print(" 1 : Afficher la fiche de révision du cours")
        print(" 2 : Lancer le questionnaire / quiz")
        print(" 3 : Quitter")
        
        choice = input("Ton choix (1, 2 ou 3) : ").strip()
        
        if choice == "1":
            print(COURSE_SUMMARY)
        elif choice == "2":
            run_quiz()
        elif choice == "3":
            print("Bonne étude ! À bientôt.")
            break
        else:
            print("Choix invalide, merci de taper 1, 2 ou 3.")

if __name__ == "__main__":
    main()
