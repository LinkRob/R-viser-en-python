import random

# La liste de verbes sous forme de dictionnaire
verbs = [
    {"traductions": ["être"], "inf": "be", "ps": "was/were", "pp": "been"},
    {"traductions": ["porter", "supporter"], "inf": "bear", "ps": "bore", "pp": "borne"},
    {"traductions": ["battre"], "inf": "beat", "ps": "beat", "pp": "beaten"},
    {"traductions": ["devenir"], "inf": "become", "ps": "became", "pp": "become"},
    {"traductions": ["commencer"], "inf": "begin", "ps": "began", "pp": "begun"},
    {"traductions": ["plier", "se courber", "courber"], "inf": "bend", "ps": "bent", "pp": "bent"},
    {"traductions": ["lier", "attacher"], "inf": "bind", "ps": "bound", "pp": "bound"},
    {"traductions": ["mordre"], "inf": "bite", "ps": "bit", "pp": "bitten"},
    {"traductions": ["saigner"], "inf": "bleed", "ps": "bled", "pp": "bled"},
    {"traductions": ["souffler"], "inf": "blow", "ps": "blew", "pp": "blown"},
    {"traductions": ["casser"], "inf": "break", "ps": "broke", "pp": "broken"},
    {"traductions": ["élever"], "inf": "breed", "ps": "bred", "pp": "bred"},
    {"traductions": ["apporter", "amener"], "inf": "bring", "ps": "brought", "pp": "brought"},
    {"traductions": ["construire"], "inf": "build", "ps": "built", "pp": "built"},
    {"traductions": ["brûler"], "inf": "burn", "ps": "burnt", "pp": "burnt"},
    {"traductions": ["éclater"], "inf": "burst", "ps": "burst", "pp": "burst"},
    {"traductions": ["acheter"], "inf": "buy", "ps": "bought", "pp": "bought"},
    {"traductions": ["rejeter", "jeter", "lancer"], "inf": "cast", "ps": "cast", "pp": "cast"},
    {"traductions": ["attraper"], "inf": "catch", "ps": "caught", "pp": "caught"},
    {"traductions": ["choisir"], "inf": "choose", "ps": "chose", "pp": "chosen"},
    {"traductions": ["venir"], "inf": "come", "ps": "came", "pp": "come"},
    {"traductions": ["coûter"], "inf": "cost", "ps": "cost", "pp": "cost"},
    {"traductions": ["ramper"], "inf": "creep", "ps": "crept", "pp": "crept"},
    {"traductions": ["couper"], "inf": "cut", "ps": "cut", "pp": "cut"},
    {"traductions": ["distribuer", "traiter"], "inf": "deal", "ps": "dealt", "pp": "dealt"},
    {"traductions": ["creuser"], "inf": "dig", "ps": "dug", "pp": "dug"},
    {"traductions": ["faire"], "inf": "do", "ps": "did", "pp": "done"},
    {"traductions": ["tracer", "dessiner"], "inf": "draw", "ps": "drew", "pp": "drawn"},
    {"traductions": ["rêver"], "inf": "dream", "ps": "dreamt", "pp": "dreamt"},
    {"traductions": ["boire"], "inf": "drink", "ps": "drank", "pp": "drunk"},
    {"traductions": ["conduire"], "inf": "drive", "ps": "drove", "pp": "driven"},
    {"traductions": ["manger"], "inf": "eat", "ps": "ate", "pp": "eaten"},
    {"traductions": ["tomber"], "inf": "fall", "ps": "fell", "pp": "fallen"},
    {"traductions": ["nourrir"], "inf": "feed", "ps": "fed", "pp": "fed"},
    {"traductions": ["sentir", "éprouver"], "inf": "feel", "ps": "felt", "pp": "felt"},
    {"traductions": ["se battre", "combattre"], "inf": "fight", "ps": "fought", "pp": "fought"},
    {"traductions": ["trouver"], "inf": "find", "ps": "found", "pp": "found"},
    {"traductions": ["fuir"], "inf": "flee", "ps": "fled", "pp": "fled"},
    {"traductions": ["voler"], "inf": "fly", "ps": "flew", "pp": "flown"},
    {"traductions": ["interdire"], "inf": "forbid", "ps": "forbade", "pp": "forbidden"},
    {"traductions": ["oublier"], "inf": "forget", "ps": "forgot", "pp": "forgotten"}
]

def clean_input(text):
    """Nettoie la saisie utilisateur (enlève 'to ', espaces, minuscules)"""
    text = text.strip().lower()
    if text.startswith("to "):
        text = text[3:].strip()
    return text

def run_quiz():
    print("=== SESSION D'ENTRAÎNEMENT - TEMPS PRIMITIFS ===")
    print("Tape 'q' ou 'exit' à tout moment pour quitter.\n")
    
    score = 0
    total = 0

    while True:
        verb = random.choice(verbs)
        mode = random.choice([1, 2, 3])
        
        if mode == 1:
            # Mode : Donne toutes les formes depuis le Français
            trad = random.choice(verb["traductions"])
            print(f"\n[FR -> EN] Traduis et donne les 3 formes pour : '{trad}'")
            user_inf = input("  Infinitive (ex: break) : ")
            if user_inf.lower() in ['q', 'exit']: break
            user_ps = input("  Past Simple (ex: broke) : ")
            if user_ps.lower() in ['q', 'exit']: break
            user_pp = input("  Past Participle (ex: broken) : ")
            if user_pp.lower() in ['q', 'exit']: break
            
            cond_inf = clean_input(user_inf) == verb["inf"]
            cond_ps = clean_input(user_ps) == verb["ps"] or (verb["inf"] == "be" and clean_input(user_ps) in ["was", "were", "was/were"])
            cond_pp = clean_input(user_pp) == verb["pp"]

            if cond_inf and cond_ps and cond_pp:
                print(" -> EXCELLENT ! 100% correct.")
                score += 1
            else:
                print(f" -> RATA [X] La bonne réponse était : to {verb['inf']} | {verb['ps']} | {verb['pp']}")

        elif mode == 2:
            # Mode : Trouve le Past Simple et Past Participle depuis l'infinitif
            print(f"\n[COMPLÈTE] Infinitif : 'to {verb['inf']}' ({', '.join(verb['traductions'])})")
            user_ps = input("  Past Simple : ")
            if user_ps.lower() in ['q', 'exit']: break
            user_pp = input("  Past Participle : ")
            if user_pp.lower() in ['q', 'exit']: break

            cond_ps = clean_input(user_ps) == verb["ps"] or (verb["inf"] == "be" and clean_input(user_ps) in ["was", "were", "was/were"])
            cond_pp = clean_input(user_pp) == verb["pp"]

            if cond_ps and cond_pp:
                print(" -> PARFAIT !")
                score += 1
            else:
                print(f" -> FAUX [X] Réponses : PS = {verb['ps']} | PP = {verb['pp']}")

        elif mode == 3:
            # Mode : Retrouve la traduction française depuis l'infinitif
            print(f"\n[EN -> FR] Que signifie 'to {verb['inf']}' ?")
            user_trad = input("  Traduction en français : ").strip().lower()
            if user_trad in ['q', 'exit']: break

            if any(t in user_trad for t in verb["traductions"]):
                print(f" -> BIEN JOUÉ ! (Traductions acceptées: {', '.join(verb['traductions'])})")
                score += 1
            else:
                print(f" -> INCORRECT [X] Traductions : {', '.join(verb['traductions'])}")

        total += 1
        print(f"Score actuel : {score}/{total}")

    print(f"\n--- Fin de session ! Score final : {score}/{total} ---")

if __name__ == "__main__":
    run_quiz()