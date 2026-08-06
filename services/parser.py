import re


ROUNDS = [
    "Pre-Seed",
    "Seed",
    "Pre-Series A",
    "Series A",
    "Series B",
    "Series C",
    "Series D",
    "Series E",
]


SKIP = [
    "growth-stage startups",
    "growth stage startups",
    "early-stage startups",
    "early stage startups",
    "other startups",
    "startup funding",
    "city-wise",
    "segment-wise",
    "bareback media",
    "newsletter",
    "follow us",
    "privacy policy",
]


def split_events(paragraph):

    paragraph = re.sub(r"\bwhile\b", ".", paragraph, flags=re.I)
    paragraph = re.sub(r"\bmeanwhile\b", ".", paragraph, flags=re.I)
    paragraph = re.sub(r"\balso\b", ".", paragraph, flags=re.I)
    paragraph = re.sub(r"\bin addition\b", ".", paragraph, flags=re.I)

    events = re.split(r"\.\s+", paragraph)

    return events


def extract_company(event):

    patterns = [

        r"([A-Z][A-Za-z0-9&' .-]+?)\s+raised",

        r"([A-Z][A-Za-z0-9&' .-]+?)\s+secured",

        r"startup\s+([A-Z][A-Za-z0-9&' .-]+?)\s+raised",

        r"startup\s+([A-Z][A-Za-z0-9&' .-]+?)\s+secured",

        r"platform\s+([A-Z][A-Za-z0-9&' .-]+?)\s+raised",

        r"platform\s+([A-Z][A-Za-z0-9&' .-]+?)\s+secured",

        r"company\s+([A-Z][A-Za-z0-9&' .-]+?)\s+raised",

        r"company\s+([A-Z][A-Za-z0-9&' .-]+?)\s+secured",
    ]

    for pattern in patterns:

        m = re.search(pattern, event, re.I)

        if m:
            return m.group(1).strip()

    return None


def extract_amount(event):

    m = re.search(

        r"(\$[\d.,]+\s*(?:million|billion|Mn|Bn)|Rs\s[\d.,]+\s*crore)",

        event,

        re.I,

    )

    if m:
        return m.group(1)

    return "Unknown"


def extract_round(event):

    for r in ROUNDS:

        if r.lower() in event.lower():
            return r

    return "Unknown"


def extract_investors(event):

    m = re.search(

        r"led by\s(.+)",

        event,

        re.I,

    )

    if m:
        return m.group(1).strip()

    return ""


def extract_companies(text):

    companies = []

    paragraphs = text.split("\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if len(paragraph) < 40:
            continue

        lower = paragraph.lower()

        if any(x in lower for x in SKIP):
            continue

        if "raised" not in lower and "secured" not in lower:
            continue

        events = split_events(paragraph)

        for event in events:

            company = extract_company(event)

            if company is None:
                continue

            companies.append(
                {
                    "company": company,
                    "amount": extract_amount(event),
                    "round": extract_round(event),
                    "investors": extract_investors(event),
                }
            )

    return companies