import json
import logging
import textwrap

from openai import OpenAI

from api.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

if settings.ENVIRONMENT == "development":
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)


def generate_soap(transcript: str) -> str:
    """Helper function to generate note from transcript using OpenAI Chat Completions API."""
    logging.info("Generating note")

    sample_transcript = textwrap.dedent("""
    De patiënt is een 30-jarige rechtshandige Nederlandse man die zich bij de huisarts meldt met aanhoudende sombere gevoelens en verlies van interesse in dagelijkse activiteiten. Deze klachten zijn sinds enkele maanden aanwezig en beïnvloeden zijn functioneren op het werk en in sociale situaties. De huisarts heeft hem doorverwezen naar een psycholoog voor verdere evaluatie en behandeling. Alstublieft vraag ook uit naar medische en familliegeschiedenis, luxerende factoren, somatische factoren, aanhoudende stressoren, instandhoudende factoren en andere relevante klinische onderdelen.

    Psycholoog: Goedemiddag, welkom. Hoe gaat het vandaag met u?
    Patiënt: Het gaat niet zo goed. Ik voel me al maanden somber en niets lijkt me nog te interesseren.
    Psycholoog: Dat klinkt erg vervelend. Kunt u vertellen sinds wanneer u deze gevoelens ervaart?
    Patiënt: Ik denk dat het ongeveer drie maanden geleden begon.
    Psycholoog: Heeft u een idee waardoor deze gevoelens zijn ontstaan?
    Patiënt: Niet precies. Er is niets specifieks gebeurd, maar ik merk dat ik steeds minder plezier haal uit dingen die ik vroeger leuk vond.
    Psycholoog: Hoe beïnvloeden deze gevoelens uw dagelijks leven?
    Patiënt: Ik heb moeite om me op mijn werk te concentreren en zie vrienden nauwelijks meer. Ik voel me constant moe en heb nergens energie voor.
    Psycholoog: Heeft u last van slaapproblemen of veranderingen in uw eetlust?
    Patiënt: Ja, ik slaap slecht en heb weinig eetlust. Ik ben de afgelopen maanden ook wat afgevallen.
    Psycholoog: Heeft u eerder soortgelijke klachten gehad?
    Patiënt: Nee, dit is de eerste keer dat ik me zo voel.
    Psycholoog: Zijn er momenten waarop u zich beter voelt, of is de somberheid constant aanwezig?
    Patiënt: Het is vrijwel constant. Zelfs dingen die ik vroeger leuk vond, kunnen me nu niet opvrolijken.
    Psycholoog: Heeft u gedachten over zelfbeschadiging of suïcide?
    Patiënt: Soms denk ik dat het makkelijker zou zijn als ik er niet was, maar ik heb geen concrete plannen.
    Psycholoog: Het is belangrijk dat we deze gedachten serieus nemen. We zullen hier samen aan werken om uw situatie te verbeteren. We zullen een behandelplan opstellen dat past bij uw behoeften en samen werken aan uw herstel.
    """)

    # Example format for Tiptap editor as a JSON string
    example_format = {
        "type": "doc",
        "content": [
            {
                "type": "heading",
                "attrs": {"level": 2},
                "content": [{"type": "text", "text": "Example heading"}],
            },
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": "example paragraph"}],
            },
            {
                "type": "heading",
                "attrs": {"level": 3},
                "content": [{"type": "text", "text": "Features"}],
            },
            {
                "type": "orderedList",
                "attrs": {"tight": True, "start": 1},
                "content": [
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {"type": "text", "text": "Example list item"}
                                ],
                            },
                        ],
                    },
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {"type": "text", "text": "AI autocomplete (type "},
                                    {
                                        "type": "text",
                                        "marks": [{"type": "code"}],
                                        "text": "++",
                                    },
                                    {
                                        "type": "text",
                                        "text": " to activate, or select from slash menu)",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
    }
    example_format_str = json.dumps(example_format)

    # Call the OpenAI Chat Completions API
    completion = client.chat.completions.create(
        model="gpt-4o",  # gpt-4o, gpt-3.5-turbo
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "Je bent een behulpzame assistent gemaakt om to output JSON.",
            },
            {
                "role": "user",
                "content": f"Analyseer het onderstaande transcript en genereer de volgende secties in JSON-formaat voor een Tiptap-editor. Dit is het voorbeeld formaat: {example_format_str}. 1) Een samenvatting van het volledige transcript, met alle belangrijke zaken voor een psycholoog; 2) Een SOAP-notitie met de secties Subjectief, Objectief, Beoordeling en Plan; 3) Opvallende zaken of opmerkingen, met nadruk op wat de patiënt heeft gezegd en wat de psycholoog heeft opgemerkt; 4) Een reflectie op het optreden van de psycholoog, met focus op verbanden die niet zijn gelegd en onderwerpen die mogelijk niet zijn uitgevraagd. Zorg ervoor dat alle velden zijn ingevuld en baseer de output uitsluitend op wetenschappelijk onderzoek, klinische praktijk en de inhoud van het transcript, zonder aannames of verzinsels. Transcript: {transcript}",
            },
        ],
    )

    logging.debug(f"SOAP: {completion.choices[0].message.content}")
    return completion.choices[0].message.content
