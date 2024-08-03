import openai


def is_api_key_valid(api_key):
    openai.api_key = api_key
    engine = 'gpt-3.5-turbo-instruct'
    prompt_1 = 'Hauptstadt Deuschland?'
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt_1,
            max_tokens=5
        )
        return True
    except openai.error.AuthenticationError:
        return False


def text_prompt_ll(text="Nenne Hauptstat von China"):
    prompt = f'''in [] erhälst du einen Lebenslauf eines Kandidaten. 
    Erstelle eine Tabelle mit den Spalten
    "Name", "Nachname", "Adresse", "Telefon", "E-Mail", "Geburtsdatum", 
    "Technische Fähigkeiten", "Fachliche Fähigkeiten", "Sprachenkenntnisse",
    und befülle diese Tabelle mit den Daten 
    aus dem Lebenslauf. Achte auf die Reihenfolge der Spalten. 
    Gib die Tabelle als Output aus. Als Trennzeichen verwende "|".  
    Gebe NICHT die Überschriften der Spalten aus. 
    Hier ist der Lebenslauf: [{text}]'''
    return prompt

def text_prompt_stelle(text="Nenne Hauptstat von China"):
    prompt = f'''in [] erhälst du eine Stellenbeschreibung. 
    Erstelle eine Tabelle mit den Spalten
    "Account", "Stellenbezeichnung", "Ort", "Technische Anforderungen-Must Have",
    "Technische Anfoderungen-Nice to Have", "Anforderungen Sprache",
    und befülle diese Tabelle mit den Daten 
    aus der Stellenanzeige.
    Gib die Tabelle als Output aus. Als Trennzeichen verwende "|".  
    Gebe NICHT die Überschriften der Spalten aus. 
    Hier ist die Stellenenzeige: [{text}]'''
    return prompt
