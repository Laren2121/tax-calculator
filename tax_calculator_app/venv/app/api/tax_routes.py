from flask import Blueprint, request, jsonify
from services.tax_service import calculcate_tax_for_year

tax_blueprint = Blueprint('tax', __name__, url_prefix='/api')

ALLOWED_YEARS = {"2019", "2020", "2021", "2022"}

@tax_blueprint.route('/calculate-tax', methods=['GET'])
def calculate_tax(): 
    salary_param = request.args.get('salary')
    tax_year = request.args.get('tax_year')

    if not salary_param or not tax_year: 
        return jsonify({"errorr": "missing salary or tax year"}), 400
    
    if tax_year not in ALLOWED_YEARS: 
        return jsonify({"error": "Unsupported tax year: 2019, 2020, 2021, 2022"}), 400
    
    try: 
        salary = float(salary_param)
    except ValueError: 
        return jsonify({"errorr": "wrong value/ invalid salary parameter, must be a number"}), 400
    
    result = calculcate_tax_for_year(salary, tax_year)
    return jsonify(result), 200
