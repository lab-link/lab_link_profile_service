from flask import request, jsonify
from flask import Blueprint

def profile_portfolio_routes_wrapper(db):
    from models import ProfilePortfolios
    profile_portfolio_blueprint = Blueprint('profile_portfolio', __name__)

    @profile_portfolio_blueprint.route("/save-portfolio", methods=['POST'])
    def save_portfolio():
        """
        This API stores a profile into mysql.
        :param {}: JSON
        :return: string
        """
        if request.method == 'POST':
            content = request.get_json()
            portfolio_id = content.get("portfolio_id", None)
            profile_id = content.get("profile_id", None)
            employer_name = content.get("employer_name", None)
            experience_data = content.get("experience_data", None)

            new_portfolio = ProfilePortfolios(
                portfolio_id=portfolio_id,
                profile_id=profile_id,
                employer_name=employer_name,
                experience_data=experience_data,
            )
            db.session.add(new_portfolio)
            db.session.commit()
            return jsonify(message="Portfolio saved successfully!"), 201
        else:
            return jsonify(message="Method not allowed"), 405
        
    @profile_portfolio_blueprint.route("/get-portfolio/<int:portfolio_id>", methods=['GET'])
    def get_portfolio(portfolio_id):
        """
        This API fetches a portfolio by ID from mysql.
        :param portfolio_id: int
        :return: JSON
        """
        portfolio = ProfilePortfolios.query.get(portfolio_id)
        if portfolio:
            return jsonify({
                'portfolio_id': portfolio.portfolio_id,
                'profile_id': portfolio.profile_id,
                'employer_name': portfolio.employer_name,
                'experience_data': portfolio.experience_data
            }), 200
        else:
            return jsonify(message="Portfolio not found"), 404

    @profile_portfolio_blueprint.route("/update-portfolio/<int:portfolio_id>", methods=['PUT'])
    def update_portfolio(portfolio_id):
        """
        This API updates a portfolio in the database.
        :param portfolio_id: int
        :param {}: JSON
        :return: string
        """
        if request.method == 'PUT':
            content = request.get_json()
            portfolio = ProfilePortfolios.query.get(portfolio_id)
            
            if not portfolio:
                return jsonify(message="Portfolio not found"), 404
            
            portfolio.profile_id = content.get("profile_id", portfolio.profile_id)
            portfolio.employer_name = content.get("employer_name", portfolio.employer_name)
            portfolio.experience_data = content.get("experience_data", portfolio.experience_data)
            
            db.session.commit()
            return jsonify(message="Portfolio updated successfully!"), 200
        else:
            return jsonify(message="Method not allowed"), 405

    return profile_portfolio_blueprint