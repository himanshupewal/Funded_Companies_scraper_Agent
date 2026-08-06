import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from prompts.company_prompt import COMPANY_PROMPT
from services.llm import company_llm


ABOUT_PATHS = [
    "/about",
    "/about-us",
    "/company",
    "/our-story",
]


CAREER_PATHS = [
    "/careers",
    "/career",
    "/jobs",
    "/join-us",
    "/work-with-us",
]


def fetch_page(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
        )

        if response.status_code == 200:

            soup = BeautifulSoup(
                response.text,
                "html.parser",
            )

            return soup.get_text(
                "\n",
                strip=True,
            )

    except:
        pass

    return ""


def enrich_company(website):

    homepage = fetch_page(website)

    about = ""

    careers = ""

    careers_url = ""

    # -----------------------
    # Try About page
    # -----------------------

    for path in ABOUT_PATHS:

        text = fetch_page(
            urljoin(website, path)
        )

        if text:

            about = text

            break

    # -----------------------
    # Try Careers page
    # -----------------------

    for path in CAREER_PATHS:

        url = urljoin(
            website,
            path,
        )

        text = fetch_page(url)

        if text:

            careers = text

            careers_url = url

            break

    # -----------------------
    # Merge all text
    # -----------------------

    content = "\n\n".join(
        [
            homepage,
            about,
            careers,
        ]
    )

    content = content[:15000]

    try:

        result = company_llm.invoke(

            COMPANY_PROMPT
            + "\n\n"
            + content

        )

        return {

            "industry": result.industry,

            "headquarters": result.headquarters,

            "careers_page": careers_url,

        }

    except Exception as e:

        print(e)

        return {

            "industry": "",

            "headquarters": "",

            "careers_page": careers_url,

        }