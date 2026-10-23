import os
import shlex
import sys
import zipfile

LANGUAGE = "it"

TEXT = {
    "it": {
        "compress_title": "--- COMPRESSIONE (ZIP) ---",
        "folder_prompt": "Trascina qui la cartella da zippare (o scrivi il percorso): ",
        "folder_not_found": "ERRORE: Cartella non trovata",
        "zip_name_prompt": "Come vuoi chiamare il file ZIP? (esempio mio_archivio.zip): ",
        "empty_zip_name": "Inserisci un nome per il file ZIP.",
        "output_exists": "Il file esiste già: {path}",
        "overwrite_prompt": "Vuoi sostituirlo? (s/N): ",
        "compression_error": "ERRORE durante la compressione: {error}",
        "compressing": "\nSto comprimendo '{path}'...",
        "zip_created": "Azione eseguita con successo! File creato: {path}",
        "extract_title": "--- ESTRAZIONE IN CORSO (UNZIP) ---",
        "zip_prompt": "Trascina qui il file ZIP da estrarre (o scrivi il percorso): ",
        "file_not_found": "ERRORE: File non trovato: {path}",
        "zip_extension": "ERRORE: Seleziona un file con estensione .zip",
        "invalid_archive": "ERRORE: Il file selezionato non è un archivio ZIP valido",
        "destination_prompt": "Cartella di destinazione (Invio per creare una cartella accanto allo ZIP): ",
        "destination_exists": "La cartella di destinazione esiste già: {path}",
        "extract_confirm_prompt": "Continuare e unire/sostituire i file? (s/N): ",
        "cancelled": "Operazione annullata.",
        "extracting": "\nSto estraendo '{path}'...",
        "extract_error": "ERRORE durante l'estrazione: {error}",
        "extracted": "Estrazione completata: {count} {label} in {path}",
        "menu_title": "    ZIPPER AND UNZIPPER VERSION 1.0",
        "menu_hint": "SELEZIONA 1-3  |  INVIO PER APRIRE  |  CTRL+C PER USCIRE",
        "compress_option": "1. Comprimi una cartella in ZIP",
        "extract_option": "2. Estrai una cartella ZIP",
        "exit_option": "3. Esci",
        "choice_prompt": "\nScegli un'opzione (1-3): ",
        "goodbye": "\nA presto!",
        "invalid_option": "Opzione non valida",
    },
    "en": {
        "compress_title": "--- ZIP COMPRESSION ---",
        "folder_prompt": "Drop the folder to zip here (or type its path): ",
        "folder_not_found": "ERROR: Folder not found",
        "zip_name_prompt": "What should the ZIP file be called? (example: my_archive.zip): ",
        "empty_zip_name": "Enter a name for the ZIP file.",
        "output_exists": "This file already exists: {path}",
        "overwrite_prompt": "Replace it? (y/N): ",
        "compression_error": "ERROR during compression: {error}",
        "compressing": "\nCompressing '{path}'...",
        "zip_created": "Done! ZIP created: {path}",
        "extract_title": "--- EXTRACTING ZIP ---",
        "zip_prompt": "Drop the ZIP file here (or type its path): ",
        "file_not_found": "ERROR: File not found: {path}",
        "zip_extension": "ERROR: Select a file with a .zip extension",
        "invalid_archive": "ERROR: The selected file is not a valid ZIP archive",
        "destination_prompt": "Destination folder (press Enter to create a folder beside the ZIP): ",
        "destination_exists": "The destination folder already exists: {path}",
        "extract_confirm_prompt": "Continue and merge/replace files? (y/N): ",
        "cancelled": "Operation cancelled.",
        "extracting": "\nExtracting '{path}'...",
        "extract_error": "ERROR during extraction: {error}",
        "extracted": "Extraction complete: {count} {label} in {path}",
        "menu_title": "    ZIPPER AND UNZIPPER VERSION 1.0",
        "menu_hint": "SELECT 1-3  |  ENTER TO OPEN  |  CTRL+C TO EXIT",
        "compress_option": "1. Zip a folder",
        "extract_option": "2. Extract a ZIP file",
        "exit_option": "3. Exit",
        "choice_prompt": "\nChoose an option (1-3): ",
        "goodbye": "\nGoodbye!",
        "invalid_option": "Invalid option",
    },
    "es": {
        "compress_title": "--- COMPRIMIR EN ZIP ---",
        "folder_prompt": "Arrastra aquí la carpeta que quieres comprimir (o escribe la ruta): ",
        "folder_not_found": "ERROR: No se encontró la carpeta",
        "zip_name_prompt": "¿Qué nombre quieres para el archivo ZIP? (ejemplo: mi_archivo.zip): ",
        "empty_zip_name": "Escribe un nombre para el archivo ZIP.",
        "output_exists": "Este archivo ya existe: {path}",
        "overwrite_prompt": "¿Reemplazarlo? (s/N): ",
        "compression_error": "ERROR durante la compresión: {error}",
        "compressing": "\nComprimiendo '{path}'...",
        "zip_created": "¡Listo! Archivo ZIP creado: {path}",
        "extract_title": "--- EXTRAYENDO ZIP ---",
        "zip_prompt": "Arrastra aquí el archivo ZIP (o escribe la ruta): ",
        "file_not_found": "ERROR: No se encontró el archivo: {path}",
        "zip_extension": "ERROR: Selecciona un archivo con extensión .zip",
        "invalid_archive": "ERROR: El archivo seleccionado no es un ZIP válido",
        "destination_prompt": "Carpeta de destino (Enter para crear una carpeta junto al ZIP): ",
        "destination_exists": "La carpeta de destino ya existe: {path}",
        "extract_confirm_prompt": "¿Continuar y combinar/reemplazar archivos? (s/N): ",
        "cancelled": "Operación cancelada.",
        "extracting": "\nExtrayendo '{path}'...",
        "extract_error": "ERROR durante la extracción: {error}",
        "extracted": "Extracción completada: {count} {label} en {path}",
        "menu_title": "    ZIPPER AND UNZIPPER VERSION 1.0",
        "menu_hint": "ELIGE 1-3  |  ENTER PARA ABRIR  |  CTRL+C PARA SALIR",
        "compress_option": "1. Comprimir una carpeta en ZIP",
        "extract_option": "2. Extraer un archivo ZIP",
        "exit_option": "3. Salir",
        "choice_prompt": "\nElige una opción (1-3): ",
        "goodbye": "\n¡Hasta luego!",
        "invalid_option": "Opción no válida",
    },
    "fr": {
        "compress_title": "--- COMPRESSION ZIP ---",
        "folder_prompt": "Dépose le dossier à compresser ici (ou saisis son chemin) : ",
        "folder_not_found": "ERREUR : Dossier introuvable",
        "zip_name_prompt": "Quel nom donner au fichier ZIP ? (exemple : mon_archive.zip) : ",
        "empty_zip_name": "Saisis un nom pour le fichier ZIP.",
        "output_exists": "Ce fichier existe déjà : {path}",
        "overwrite_prompt": "Le remplacer ? (o/N) : ",
        "compression_error": "ERREUR pendant la compression : {error}",
        "compressing": "\nCompression de '{path}'...",
        "zip_created": "Terminé ! Archive ZIP créée : {path}",
        "extract_title": "--- EXTRACTION ZIP ---",
        "zip_prompt": "Dépose le fichier ZIP ici (ou saisis son chemin) : ",
        "file_not_found": "ERREUR : Fichier introuvable : {path}",
        "zip_extension": "ERREUR : Sélectionne un fichier avec l’extension .zip",
        "invalid_archive": "ERREUR : Le fichier sélectionné n’est pas une archive ZIP valide",
        "destination_prompt": "Dossier de destination (Entrée pour créer un dossier à côté du ZIP) : ",
        "destination_exists": "Le dossier de destination existe déjà : {path}",
        "extract_confirm_prompt": "Continuer et fusionner/remplacer les fichiers ? (o/N) : ",
        "cancelled": "Opération annulée.",
        "extracting": "\nExtraction de '{path}'...",
        "extract_error": "ERREUR pendant l’extraction : {error}",
        "extracted": "Extraction terminée : {count} {label} dans {path}",
        "menu_title": "    ZIPPER AND UNZIPPER VERSION 1.0",
        "menu_hint": "CHOISIS 1-3  |  ENTRÉE POUR OUVRIR  |  CTRL+C POUR QUITTER",
        "compress_option": "1. Compresser un dossier en ZIP",
        "extract_option": "2. Extraire une archive ZIP",
        "exit_option": "3. Quitter",
        "choice_prompt": "\nChoisis une option (1-3) : ",
        "goodbye": "\nÀ bientôt !",
        "invalid_option": "Option invalide",
    },
    "de": {
        "compress_title": "--- ORDNER ALS ZIP KOMPRIMIEREN ---",
        "folder_prompt": "Ziehe den Ordner hierher (oder gib den Pfad ein): ",
        "folder_not_found": "FEHLER: Ordner nicht gefunden",
        "zip_name_prompt": "Wie soll die ZIP-Datei heißen? (Beispiel: mein_archiv.zip): ",
        "empty_zip_name": "Gib einen Namen für die ZIP-Datei ein.",
        "output_exists": "Diese Datei ist bereits vorhanden: {path}",
        "overwrite_prompt": "Ersetzen? (j/N): ",
        "compression_error": "FEHLER beim Komprimieren: {error}",
        "compressing": "\n'{path}' wird komprimiert...",
        "zip_created": "Fertig! ZIP-Datei erstellt: {path}",
        "extract_title": "--- ZIP WIRD ENTPACKT ---",
        "zip_prompt": "Ziehe die ZIP-Datei hierher (oder gib den Pfad ein): ",
        "file_not_found": "FEHLER: Datei nicht gefunden: {path}",
        "zip_extension": "FEHLER: Wähle eine Datei mit der Endung .zip",
        "invalid_archive": "FEHLER: Die ausgewählte Datei ist kein gültiges ZIP-Archiv",
        "destination_prompt": "Zielordner (Enter erstellt einen Ordner neben der ZIP-Datei): ",
        "destination_exists": "Der Zielordner ist bereits vorhanden: {path}",
        "extract_confirm_prompt": "Fortfahren und Dateien zusammenführen/ersetzen? (j/N): ",
        "cancelled": "Vorgang abgebrochen.",
        "extracting": "\n'{path}' wird entpackt...",
        "extract_error": "FEHLER beim Entpacken: {error}",
        "extracted": "Entpacken abgeschlossen: {count} {label} in {path}",
        "menu_title": "    ZIPPER AND UNZIPPER VERSION 1.0",
        "menu_hint": "1-3 WÄHLEN  |  ENTER ZUM ÖFFNEN  |  CTRL+C ZUM BEENDEN",
        "compress_option": "1. Ordner als ZIP komprimieren",
        "extract_option": "2. ZIP-Datei entpacken",
        "exit_option": "3. Beenden",
        "choice_prompt": "\nBitte Option wählen (1-3): ",
        "goodbye": "\nAuf Wiedersehen!",
        "invalid_option": "Ungültige Option",
    },
}

LANGUAGE_OPTIONS = [
    ("it", "Italiano"),
    ("en", "English"),
    ("es", "Español"),
    ("fr", "Français"),
    ("de", "Deutsch"),
]

YES_OPTIONS = {
    "it": {"s", "si", "sì"},
    "en": {"y", "yes"},
    "es": {"s", "si", "sí"},
    "fr": {"o", "oui"},
    "de": {"j", "ja"},
}


def text(key, **values):
    return TEXT[LANGUAGE][key].format(**values)


def render_menu():
    title = "ZIPPER // ARCHIVE UTILITY"
    subtitle = text("menu_title").strip()
    options = [
        text("compress_option"),
        text("extract_option"),
        text("exit_option"),
    ]
    hint = text("menu_hint")
    width = max(len(title), len(subtitle), len(hint), *(len(option) + 2 for option in options))
    border = "+" + "-" * (width + 2) + "+"
    color_enabled = (
        sys.stdout.isatty()
        and os.environ.get("TERM") != "dumb"
        and "NO_COLOR" not in os.environ
    )

    def color(value, code):
        return f"\033[{code}m{value}\033[0m" if color_enabled else value

    print()
    print(color(border, "36;1"))
    print(color(f"| {title:<{width}} |", "96;1"))
    print(f"| {subtitle:<{width}} |")
    print(color(border, "36;1"))
    for index, option in enumerate(options):
        row = f"  {option}"
        row = f"| {row:<{width}} |"
        print(color(row, "44;97;1") if index == 0 else row)
    print(color(border, "36;1"))
    print(color(f"| {hint:<{width}} |", "90"))
    print(color(border, "36;1"))


def scegli_lingua():
    global LANGUAGE
    while True:
        print("\nChoose language / Scegli la lingua / Elige el idioma / Choisis la langue / Sprache wählen")
        for numero, (_, nome) in enumerate(LANGUAGE_OPTIONS, start=1):
            print(f"{numero}. {nome}")
        scelta = input(f"Select / Seleziona (1-{len(LANGUAGE_OPTIONS)}): ").strip()
        if scelta.isdigit() and 1 <= int(scelta) <= len(LANGUAGE_OPTIONS):
            LANGUAGE = LANGUAGE_OPTIONS[int(scelta) - 1][0]
            return
        print("Scelta non valida / Invalid choice")


def normalizza_percorso(percorso):
    percorso = percorso.strip()
    percorso_senza_virgolette = percorso.strip("'\"")
    if (
        len(percorso_senza_virgolette) >= 3
        and percorso_senza_virgolette[1] == ":"
        and percorso_senza_virgolette[2] in "\\/"
    ) or percorso_senza_virgolette.startswith("\\\\"):
        return percorso_senza_virgolette
    try:
        parti = shlex.split(percorso)
    except ValueError:
        parti = [percorso.strip("'\"")]
    return " ".join(parti) if parti else percorso.strip("'\"")


def leggi_percorso(prompt):
    return normalizza_percorso(input(prompt))


def comprimi_cartella():
    print(f"\n{text('compress_title')}")
    cartella = leggi_percorso(text("folder_prompt"))

    if not os.path.isdir(cartella):
        print(text("folder_not_found"))
        return

    nome_output = normalizza_percorso(input(text("zip_name_prompt")))
    if not nome_output:
        print(text("empty_zip_name"))
        return
    if not nome_output.lower().endswith(".zip"):
        nome_output += ".zip"
    nome_output = os.path.abspath(nome_output)

    if os.path.exists(nome_output):
        print(text("output_exists", path=nome_output))
        conferma = input(text("overwrite_prompt")).strip().lower()
        if conferma not in YES_OPTIONS[LANGUAGE]:
            print(text("cancelled"))
            return

    print(text("compressing", path=cartella))

    try:
        with zipfile.ZipFile(nome_output, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(cartella):
                dirs.sort()
                for file in sorted(files):
                    percorso_completo = os.path.abspath(os.path.join(root, file))
                    if percorso_completo == nome_output:
                        continue
                    percorso_relativo = os.path.relpath(
                        percorso_completo, start=cartella
                    )
                    zipf.write(percorso_completo, arcname=percorso_relativo)
    except (OSError, zipfile.BadZipFile, RuntimeError) as errore:
        print(text("compression_error", error=errore))
        return

    print(text("zip_created", path=os.path.abspath(nome_output)))


def estrai_zip():
    print(f"\n{text('extract_title')}")
    file_zip = leggi_percorso(text("zip_prompt"))

    if not os.path.isfile(file_zip):
        print(text("file_not_found", path=file_zip))
        return
    if not file_zip.lower().endswith(".zip"):
        print(text("zip_extension"))
        return
    if not zipfile.is_zipfile(file_zip):
        print(text("invalid_archive"))
        return

    cartella_zip = os.path.dirname(os.path.abspath(file_zip))
    cartella_default = os.path.splitext(os.path.basename(file_zip))[0]
    cartella_default = os.path.join(cartella_zip, cartella_default)
    destinazione = input(text("destination_prompt")).strip()

    if not destinazione:
        destinazione = cartella_default
    else:
        destinazione = normalizza_percorso(destinazione)

    if os.path.isdir(destinazione) and os.listdir(destinazione):
        print(text("destination_exists", path=os.path.abspath(destinazione)))
        conferma = input(text("extract_confirm_prompt")).strip().lower()
        if conferma not in YES_OPTIONS[LANGUAGE]:
            print(text("cancelled"))
            return

    print(text("extracting", path=file_zip))

    try:
        os.makedirs(destinazione, exist_ok=True)
        with zipfile.ZipFile(file_zip, "r") as zip_ref:
            elementi = zip_ref.namelist()
            zip_ref.extractall(destinazione)
    except (OSError, zipfile.BadZipFile, RuntimeError) as errore:
        print(text("extract_error", error=errore))
        return

    print(text(
        "extracted",
        count=len(elementi),
        label={
            "it": ("elemento" if len(elementi) == 1 else "elementi"),
            "en": ("item" if len(elementi) == 1 else "items"),
            "es": ("elemento" if len(elementi) == 1 else "elementos"),
            "fr": ("élément" if len(elementi) == 1 else "éléments"),
            "de": ("Eintrag" if len(elementi) == 1 else "Einträge"),
        }[LANGUAGE],
        path=os.path.abspath(destinazione),
    ))


def easter_egg():
    print("\n" + "="*40)
    print("BENVENUTO A MACHOTOMATO MODEEEE")
    print("="*40)
    print(r"""

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⣶⡆⠀⠿⠀⣶⠒⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⠾⠛⢹⣶⡤⢶⣿⡟⠶⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣤⣤⣤⣤⣴⠂⠸⠋⢀⣄⡉⠓⠀⠲⣶⣾⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⢀⣾⡿⠋⠁⣠⣤⣿⡟⢀⣠⣾⣿⣿⣿⣷⣶⣤⣼⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⣾⡟⠀⣰⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⢸⡿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀<-- Il pomodoro gigante e speciale
⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        Grazie per aver provato il mio programma!
    """)


def main():
    scegli_lingua()
    while True:
        render_menu()

        scelta = input(text("choice_prompt")).strip()

        if scelta =="1":
            comprimi_cartella()
        elif scelta == "2":
            estrai_zip()
        elif scelta == "3":
            print(text("goodbye"))
            break
        elif scelta == "machotomato":
            #WOW, come hai fatto a scoprire il machotomato!
            easter_egg()
        else:
            print(text("invalid_option"))

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{text('goodbye')}")
