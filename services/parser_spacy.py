import spacy

nlp = spacy.load("en_core_web_sm")


def extract_companies(text: str):

    companies = []

    paragraphs = text.split("\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if len(paragraph) < 40:
            continue

        lower = paragraph.lower()

        if (
            "raised" not in lower
            and "secured" not in lower
            and "investment" not in lower
        ):
            continue

        print("=" * 100)
        print(paragraph)
        print("=" * 100)

        doc = nlp(paragraph)

        print("Entities")

        for ent in doc.ents:
            print(f"{ent.text:<40} {ent.label_}")

        print()

    return companies