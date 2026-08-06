from services.company_lookup import get_company_info

def find_company_website(state):

    for company in state["companies"]:

        print(f"Searching website for {company.company}")

        info = get_company_info(company.company)

        company.company_website = info["company_website"]
        company.industry = info["industry"]
        company.headquarters = info["headquarters"]
        company.careers_page = info["careers_page"]

        print(company.company_website)

    return state