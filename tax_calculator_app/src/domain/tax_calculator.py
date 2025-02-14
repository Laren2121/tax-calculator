def calculate_tax(salary: float, tax_brackets: list) -> tuple:
    total_tax, tax_details =  0.0, []

    for bracket in tax_brackets: 
        bracket_min = bracket.get("min", 0)
        bracket_max = bracket.get("max") 
        rate = bracket.get("rate", 0)

        if salary <= bracket_min: 
            taxable = 0.0
        else: 
            if bracket_max is not None: 
                taxable = min(salary, bracket_max) - bracket_min
            else: 
                taxable = salary - bracket_min
        
        taxable = max(0, taxable)
        tax_for_bracket = taxable * rate
        total_tax += tax_for_bracket

        tax_details.append({
            "bracket": bracket, 
            "taxable_amount": taxable, 
            "tax" : tax_for_bracket
        })
        
    effective_rate = total_tax / salary if salary > 0 else 0
    return total_tax, effective_rate, tax_details