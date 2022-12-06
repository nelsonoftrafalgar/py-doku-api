from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin
from src.mask import Mask

app = Flask(__name__)
cors = CORS(app)

@app.route('/api')
@cross_origin()
def Api():
    level = request.args.get('level')
    mask = Mask()
    board = mask.mask_board(float(level))
    response = jsonify(board)
    return response

if __name__ == '__main__':
    app.run()
