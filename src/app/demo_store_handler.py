import os

from flask import jsonify

BANNER_PATH = "/tmp/media/banner"
BANNER_NAME = "banner.jpg"
LOGO_PATH = "/tmp/media/logo"
LOGO_NAME = "Logo.png"

def demo_store_handler(request):
    logo = request.files.get("logo", None)
    banner = request.files.get("banner", None)

    if not logo:
        return jsonify({"error": "No logo uploaded"}), 400

    if not banner:
        return jsonify({"error": "No banner uploaded"}), 400
    
    if logo.filename != LOGO_NAME:
        return jsonify({"error": "Logo name inconrrect."}), 400
    
    if banner.filename != BANNER_NAME:
        return jsonify({"error": "Banner name inconrrect."}), 400
    
    logo.save(os.path.join(LOGO_PATH, LOGO_NAME))
    banner.save(os.path.join(BANNER_PATH, BANNER_NAME))

    return jsonify({"message": "Media successfully updated."}), 200
