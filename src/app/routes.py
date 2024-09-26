from flask import request, jsonify

from app.demo_store_handler import demo_store_handler

def register_routes(app):

    # @app.before_request
    # def before_request_check():
    #     if request.endpoint == 'home':
    #         return

    #     required_fields = ['clt', 'PHPSESSID', 'sess_lang', 'usr', 'profile_Id']

    #     for field in required_fields:
    #         if field not in request.form:
    #             return jsonify({"error": "Not authorized."}), 401

    @app.route('/')
    def home():
        return jsonify({"status": 200})
    
    @app.route('/demo', methods=["POST"])
    def demo_store():
        return demo_store_handler(request)
