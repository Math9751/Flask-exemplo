from flask import Flask, make_response, jsonify, request
from bd import Albuns



app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False 

@app.route('/albuns', methods=['GET'])
def get_albuns():
    return make_response(
        jsonify (
            mensagem='Lista de álbuns.',
            dados=Albuns
            )
        )

@app.route('/albuns', methods=['POST'])
def create_album():
    try:
        # Obtenha os dados do corpo da solicitação como JSON
        album_data = request.get_json()

        # Adicione o novo álbum à lista
        Albuns.append(album_data)

        # Retorne o álbum criado
        return jsonify(
            mensagem='Álbum adicionado com sucesso.',
            álbum=album_data
            ), 201  # 201 Created

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request

if __name__ == '__main__':
    app.run(debug=True)