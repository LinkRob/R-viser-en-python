import random
import sys

# ==============================================================================
# BASE DE DONNÉES EXHAUSTIVE DE LA FICHE D'ANGLAIS
# ==============================================================================

ADJECTIFS = [
    # Irréguliers
    {"adj": "good / well", "comp": "better", "sup": "the best", "rule": "Irrégulier"},
    {"adj": "bad / ill", "comp": "worse", "sup": "the worst", "rule": "Irrégulier"},
    {"adj": "far", "comp": "further", "sup": "the furthest", "rule": "Irrégulier (ou farther/farthest)"},
    {"adj": "little", "comp": "less", "sup": "the least", "rule": "Irrégulier"},
    {"adj": "much / many", "comp": "more", "sup": "the most", "rule": "Irrégulier"},
    {"adj": "old (aîné / famille)", "comp": "elder", "sup": "the eldest", "rule": "Irrégulier pour la famille"},
    {"adj": "old (vieux / ancien)", "comp": "older", "sup": "the oldest", "rule": "Régulier"},

    # Courts - Doublement de consonne
    {"adj": "hot", "comp": "hotter", "sup": "the hottest", "rule": "Court - Doubler la consonne (-tter)"},
    {"adj": "big", "comp": "bigger", "sup": "the biggest", "rule": "Court - Doubler la consonne (-gger)"},
    {"adj": "red", "comp": "redder", "sup": "the reddest", "rule": "Court - Doubler la consonne (-dder)"},
    {"adj": "fat", "comp": "fatter", "sup": "the fattest", "rule": "Court - Doubler la consonne (-tter)"},

    # Courts finissant par -y (Consonne + Y -> -ier / -iest)
    {"adj": "pretty", "comp": "prettier", "sup": "the prettiest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "heavy", "comp": "heavier", "sup": "the heaviest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "healthy", "comp": "healthier", "sup": "the healthiest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "silly", "comp": "sillier", "sup": "the silliest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "happy", "comp": "happier", "sup": "the happiest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "friendly", "comp": "friendlier", "sup": "the friendliest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "noisy", "comp": "noisier", "sup": "the noisiest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "dry", "comp": "drier", "sup": "the driest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "early", "comp": "earlier", "sup": "the earliest", "rule": "Court en -y -> -ier / -iest"},
    {"adj": "narrow", "comp": "narrower", "sup": "the narrowest", "rule": "Se comporte comme un adj. en -y"},

    # Courts classiques & réguliers
    {"adj": "pale", "comp": "paler", "sup": "the palest", "rule": "Court (finit en -e)"},
    {"adj": "small", "comp": "smaller", "sup": "the smallest", "rule": "Court classique"},
    {"adj": "tall", "comp": "taller", "sup": "the tallest", "rule": "Court classique"},
    {"adj": "short", "comp": "shorter", "sup": "the shortest", "rule": "Court classique"},
    {"adj": "cold", "comp": "colder", "sup": "the coldest", "rule": "Court classique"},
    {"adj": "cool", "comp": "cooler", "sup": "the coolest", "rule": "Court (deux voyelles -> pas de doublement)"},
    {"adj": "fast", "comp": "faster", "sup": "the fastest", "rule": "Court classique"},
    {"adj": "cheap", "comp": "cheaper", "sup": "the cheapest", "rule": "Court classique"},

    # Longs
    {"adj": "amusing", "comp": "more amusing", "sup": "the most amusing", "rule": "Long -> More / The most"},
    {"adj": "intelligent", "comp": "more intelligent", "sup": "the most intelligent", "rule": "Long -> More / The most"},
    {"adj": "hopeful", "comp": "more hopeful", "sup": "the most hopeful", "rule": "Long -> More / The most"},
    {"adj": "useful", "comp": "more useful", "sup": "the most useful", "rule": "Long -> More / The most"},
    {"adj": "determined", "comp": "more determined", "sup": "the most determined", "rule": "Long -> More / The most"},
    {"adj": "jealous", "comp": "more jealous", "sup": "the most jealous", "rule": "Long -> More / The most"},
    {"adj": "beautiful", "comp": "more beautiful", "sup": "the most beautiful", "rule": "Long -> More / The most"},
    {"adj": "dangerous", "comp": "more dangerous", "sup": "the most dangerous", "rule": "Long -> More / The most"},
    {"adj": "sincere", "comp": "more sincere", "sup": "the most sincere", "rule": "Long -> More / The most"},
    {"adj": "pleasant", "comp": "more pleasant", "sup": "the most pleasant", "rule": "Long -> More / The most"},
    {"adj": "expensive", "comp": "more expensive", "sup": "the most expensive", "rule": "Long -> More / The most"},
    {"adj": "important", "comp": "more important", "sup": "the most important", "rule": "Long -> More / The most"}
]

GRAMMAIRE_NOMS = [
    {"q": "Traduis : 'Les pauvres'", "a": "the poor", "note": "Toujours THE + adj, JAMAIS de -s"},
    {"q": "Traduis : 'Les riches'", "a": "the rich", "note": "Pas de -s à la fin d'un adjectif collectif"},
    {"q": "Traduis : 'Les morts'", "a": "the dead", "note": "Toujours THE + adjectif"},
    {"q": "Traduis : 'Les vivants'", "a": "the living", "note": "Toujours THE + adjectif"},
    {"q": "Traduis : 'Les chômeurs'", "a": "the unemployed", "note": "Toujours THE + adjectif"},
    {"q": "Traduis : 'L'inconnu'", "a": "the unknown", "note": "Précédé de THE"},
    {"q": "Traduis : 'Le pauvre !'", "a": "poor man!", "note": "Épithète au singulier -> doit avoir un nom (man)"},
    {"q": "Traduis : 'Un mort'", "a": "a dead man", "note": "Au singulier -> nom obligatoire"},
    {"q": "Traduis : 'Une Anglaise'", "a": "an english woman", "note": "Nom féminin obligatoire"},
    {"q": "Traduis : 'Des Anglais'", "a": "some english people", "note": "Adjectif + nom au pluriel"},
    {"q": "Traduis : 'La maison des riches' (avec 'of')", "a": "the houses of the rich", "note": "Pas de cas possessif avec 'the rich'"}
]

EXPRESSIONS = [
    {"fr": "C'est le moins qu'on puisse dire", "en": "it's the least you can say"},
    {"fr": "C'est le moindre de mes soucis", "en": "that's the least of my worries"},
    {"fr": "C'est la plus belle ville que j'aie jamais vue", "en": "it's the most beautiful city i've ever seen"},
    {"fr": "C'est le plus beau jour de ma vie", "en": "it's the most beautiful day of my life"},
    {"fr": "Le meilleur spectacle de tous les temps", "en": "the best show ever"},
    {"fr": "Plus on est de fous, plus on rit", "en": "the more, the merrier"}
]

PIEGES = [
    {"q": "Quel est le comparatif de 'good' ?", "a": "better", "rule": "Irrégulier (good -> better)"},
    {"q": "Quel est le superlatif de 'bad' ?", "a": "the worst", "rule": "Irrégulier (bad -> the worst)"},
    {"q": "Traduis : 'Les riches' (attention au -s)", "a": "the rich", "rule": "JAMAIS de -s aux adjectifs employés comme noms"},
    {"q": "Quel est le comparatif de 'far' ?", "a": "further", "rule": "Irrégulier (far -> further / farther)"},
    {"q": "Quel est le superlatif de 'little' ?", "a": "the least", "rule": "Irrégulier (little -> the least)"},
    {"q": "Comment écrit-on le comparatif de 'hot' ?", "a": "hotter", "rule": "Doublement du t (hotter)"},
    {"q": "Comment dit-on 'mon frère aîné' ?", "a": "my elder brother", "rule": "Old -> elder pour la famille"},
    {"q": "Traduis : 'La maison des riches'", "a": "the houses of the rich", "rule": "Pas de 's pour the rich (utiliser 'of')"},
    {"q": "Quel est le comparatif de 'heavy' ?", "a": "heavier", "rule": "Consonne + y -> -ier"},
    {"q": "Traduis : 'Plus on est de fous, plus on rit'", "a": "the more, the merrier", "rule": "Expression par cœur"}
]

def clean(text):
    return text.strip().lower().replace("’", "'").replace("!", "")

# ==============================================================================
# FONCTIONS DES MODES
# ==============================================================================

def mode_revision_globale():
    print("\n--- MODE 1 : RÉVISION GLOBALE TOUTES CATÉGORIES ---")
    score = 0
    total = 0
    
    # Mix de tout : Adjectifs, Grammaire Noms, Expressions
    pool = []
    for item in ADJECTIFS:
        pool.append(("adj_comp", f"Comparatif (+) de '{item['adj']}'", item['comp'], item['rule']))
        pool.append(("adj_sup", f"Superlatif (++) de '{item['adj']}' (avec 'the')", item['sup'], item['rule']))
    for item in GRAMMAIRE_NOMS:
        pool.append(("gram", item['q'], item['a'], item['note']))
    for item in EXPRESSIONS:
        pool.append(("exp", f"Traduis : '{item['fr']}'", item['en'], "Expression par cœur"))

    random.shuffle(pool)

    for i in range(15):
        cat, question, target, rule = pool[i]
        ans = input(f"\n[{i+1}/15] {question} : ")
        if clean(ans) in [clean(target), clean(target.split('/')[0])]:
            print("  ✓ EXACT !")
            score += 1
        else:
            print(f"  ✗ FAUX ! Réponse attendue : {target}")
            print(f"    -> Règle : {rule}")
        total += 1

    print(f"\n Score Révision Globale : {score}/{total}")

def mode_sprint_10():
    print("\n--- MODE 2 : SPRINT 10 ADJECTIFS AU HASARD ---")
    score = 0
    selected = random.sample(ADJECTIFS, 10)

    for i, item in enumerate(selected, 1):
        q_type = random.choice(["comp", "sup"])
        if q_type == "comp":
            prompt = f"Comparatif (+ ) de '{item['adj']}'"
            target = item['comp']
        else:
            prompt = f"Superlatif (++ ) de '{item['adj']}' (avec 'the')"
            target = item['sup']

        ans = input(f"\n[{i}/10] {prompt} : ")
        if clean(ans) in [clean(target), clean(target.split('/')[0])]:
            print("  ✓ EXACT !")
            score += 1
        else:
            print(f"  ✗ FAUX ! Réponse attendue : {target} [{item['rule']}]")

    print(f"\n Score Sprint 10 Adjectifs : {score}/10")

def mode_interro_piegeuse():
    print("\n" + "!"*60)
    print("  MODE 3 : INTERRO PIÉGEUSE (10 QUESTIONS CRITIQUES)")
    print("  0 excuse sur les erreurs classiques du cours !")
    print("!"*60)
    score = 0

    for i, p in enumerate(PIEGES, 1):
        ans = input(f"\n[PIÈGE {i}/10] {p['q']} : ")
        if clean(ans) == clean(p['a']):
            print("  ✓ PARFAIT ! Piège évité.")
            score += 1
        else:
            print(f"  ✗ PIÈGE TOMBÉ ! La réponse exacte est : {p['a']}")
            print(f"    Rappel : {p['rule']}")

    print(f"\n Score Interro Piégeuse : {score}/10")

def mode_examen_4_points():
    print("\n" + "="*60)
    print("  MODE 4 : EXAMEN COMPLET SUR 4 POINTS (1 POINT PAR CATÉGORIE)")
    print("="*60)
    
    total_score = 0

    # Catégorie 1 : Comparatifs / Superlatifs réguliers & longs
    print("\n--- CATÉGORIE 1 : Adjectifs Réguliers & Longs (1 point) ---")
    item = random.choice([x for x in ADJECTIFS if "Long" in x['rule'] or "Court classique" in x['rule']])
    ans = input(f"Superlatif (++) de '{item['adj']}' (avec 'the') : ")
    if clean(ans) == clean(item['sup']):
        print("  ✓ Correct (+1 pt)")
        total_score += 1
    else:
        print(f"  ✗ Erreur. C'était : {item['sup']}")

    # Catégorie 2 : Exceptions & Adjectifs Irréguliers
    print("\n--- CATÉGORIE 2 : Exceptions & Irréguliers (1 point) ---")
    item = random.choice([x for x in ADJECTIFS if "Irrégulier" in x['rule']])
    ans = input(f"Comparatif (+) de '{item['adj']}' : ")
    if clean(ans) in [clean(item['comp']), clean(item['comp'].split('/')[0])]:
        print("  ✓ Correct (+1 pt)")
        total_score += 1
    else:
        print(f"  ✗ Erreur. C'était : {item['comp']}")

    # Catégorie 3 : Adjectifs employés comme noms (the rich, the poor...)
    print("\n--- CATÉGORIE 3 : Adjectifs comme Noms / Épithètes (1 point) ---")
    item = random.choice(GRAMMAIRE_NOMS)
    ans = input(f"{item['q']} : ")
    if clean(ans) == clean(item['a']):
        print("  ✓ Correct (+1 pt)")
        total_score += 1
    else:
        print(f"  ✗ Erreur. C'était : {item['a']}")

    # Catégorie 4 : Expressions de la fiche
    print("\n--- CATÉGORIE 4 : Expressions & Traduction (1 point) ---")
    item = random.choice(EXPRESSIONS)
    ans = input(f"Traduis : '{item['fr']}' : ")
    if clean(ans) == clean(item['en']):
        print("  ✓ Correct (+1 pt)")
        total_score += 1
    else:
        print(f"  ✗ Erreur. C'était : {item['en']}")

    print("\n" + "="*60)
    print(f"  NOTE FINALE D'EXAMEN : {total_score} / 4")
    if total_score == 4:
        print("  RÉSULTAT : 100% SANS FAUTE. Tu es paré face à ton père !")
    else:
        print("  RÉSULTAT : Relis la section manquée avant d'y aller.")
    print("="*60)

# ==============================================================================
# MENU PRINCIPAL
# ==============================================================================

def main():
    while True:
        print("\n==================================================")
        print("  SCRIPT ULTIME DE RÉVISION : ANGLAIS (0 FAUTE)")
        print("==================================================")
        print("1) Révision globale (Toutes catégories mélangées)")
        print("2) Sprint 10 adjectifs n'importe lesquels")
        print("3) Interro piégeuse (Focus pièges & exceptions)")
        print("4) Examen complet sur 4 points (1 pt / catégorie)")
        print("5) Quitter")
        
        choice = input("\nFais ton choix (1/2/3/4/5) : ").strip()
        
        if choice == "1":
            mode_revision_globale()
        elif choice == "2":
            mode_sprint_10()
        elif choice == "3":
            mode_interro_piegeuse()
        elif choice == "4":
            mode_examen_4_points()
        elif choice == "5":
            print("\nBonne chance. Sois confiant et direct !")
            sys.exit()
        else:
            print("Choix invalide, tape un chiffre entre 1 et 5.")

if __name__ == "__main__":
    main()