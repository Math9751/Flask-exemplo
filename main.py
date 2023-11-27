from flask import Flask, make_response, jsonify, request
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='H@pp!n3$',
    database='disco',
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False 

@app.route('/albuns', methods=['GET'])
def get_albuns():

    cursor = conexao.cursor()
    read = f"SELECT * FROM albuns WHERE deletado = 0"
    cursor.execute(read)
    meus_albuns = cursor.fetchall()

    albuns = list()
    for album in meus_albuns:
        albuns.append(
            {
                'id': album[0],
                'album': album[1],
                'artista': album[2],
                'ano': album[3],
                'deletado': album[4]
            }
        )

    return make_response(
        jsonify (
            mensagem='Lista de álbuns.',
            dados=albuns
            )
        )


@app.route('/albuns', methods=['POST'])
def create_album():
    try:
        # Obtenha os dados do corpo da solicitação como JSON
        album = request.get_json()

        # Adicione o novo álbum à lista
        cursor = conexao.cursor()
        create = f"INSERT INTO albuns (album, artista, ano) VALUES ('{album['album']}', '{album['artista']}', '{album['ano']}')"
        cursor.execute(create)
        conexao.commit()

        # Retorne o álbum criado
        return jsonify(
            mensagem='Álbum adicionado com sucesso.',
            álbum=album
            ), 201  # 201 Created

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request
    
@app.route('/albuns', methods=['PUT'])
def update_album():
    try:
        # Obtenha os dados do corpo da solicitação como JSON
        album = request.get_json()

        # Adicione o novo álbum à lista
        cursor = conexao.cursor()

        update = f"UPDATE albuns SET album = '{album['album']}' WHERE artista = '{album['artista']}'"
        cursor.execute(update)
        conexao.commit()

        # Retorne o álbum criado
        return jsonify(
            mensagem='Álbum atualizado com sucesso.',
            álbum=album
            ), 201  # 201 Created

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request

@app.route('/albuns', methods=['DELETE'])
def delete_album():
    try:
        # Obtenha os dados do corpo da solicitação como JSON
        album = request.get_json()

        # Adicione o novo álbum à lista
        cursor = conexao.cursor()

        delete = f"UPDATE albuns SET deletado = 1 WHERE artista = '{album['artista']}'"
        cursor.execute(delete)
        conexao.commit()

        # Retorne o álbum criado
        return jsonify(
            mensagem='Álbum excluído com sucesso.'
            ), 201  # 201 Created

    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request

if __name__ == '__main__':
    app.run(debug=True)