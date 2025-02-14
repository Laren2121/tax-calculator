import requests
from domain.tax_calculator import calculate_tax

API_BASE_URL = "http://localhost:5001"

def get_tax_brackets(tax_year: str) -> list: 

    url = f"{API_BASE_URL}/tax-calculator/tax-year/{tax_year}"

    try: 
        response = requests.get(url, timeout=5) # check the timeout
        response.raise_for_status()
        data = response.json()
        tax_brackets = data.get("tax_brackets", [])
        if not tax_brackets: 
            raise Exception("No tax bracket data found for the specific tax year. ")
        return tax_brackets
    except requests.RequestException as e: 
        raise Exception(f"Error fetching tax brackets: {e}")
    
def calculcate_tax_for_year(salary: float, tax_year: str) -> dict: 
    tax_brackets = get_tax_brackets(tax_year)

    total_tax, effective_rate, tax_details = calculate_tax(salary, tax_brackets)

    result = {
        "salary": salary,
        "tax_year" : tax_year, 
        "total_tax" : round(total_tax, 2), 
        "effective_tax_rate" : round(effective_rate * 100, 2), 
        "tax_details" : tax_details
    }

    return result
