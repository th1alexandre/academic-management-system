from flask import Blueprint, jsonify, request
from flasgger import swag_from

from modules.pessoa import service


bp_pessoa = Blueprint("Pessoa", __name__)


@swag_from("post.yaml")
@bp_pessoa.route("", methods=["POST"])
def post():
    try:
        data = request.get_json()
        response = service.post(data)

        return jsonify(response), 201
    except Exception as e:
        raise e
