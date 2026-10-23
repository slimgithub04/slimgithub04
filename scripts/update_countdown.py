"""Met à jour le compte à rebours du pied de page (assets/footer-*.svg).

Exécuté chaque jour par .github/workflows/profil.yml. Aucune dépendance externe.
"""
import datetime
import pathlib
import re

AVAILABLE = datetime.date(2027, 3, 1)
ROOT = pathlib.Path(__file__).resolve().parent.parent


def countdown_text(today):
    days = (AVAILABLE - today).days
    if days <= 0:
        return "Disponible dès maintenant"
    return f"Disponible dans {days} jour" + ("s" if days > 1 else "")


def main():
    text = countdown_text(datetime.datetime.now(datetime.timezone.utc).date())
    for path in sorted(ROOT.glob("assets/footer-*.svg")):
        svg = path.read_text(encoding="utf-8")
        new = re.sub(r'(<text id="countdown"[^>]*>)[^<]*(</text>)', lambda m: m.group(1) + text + m.group(2), svg)
        if new != svg:
            path.write_text(new, encoding="utf-8")
            print(f"{path.name} : {text}")


if __name__ == "__main__":
    main()
