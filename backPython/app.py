from flask import Flask, jsonify, request
from flask_cors import CORS
from mail import mail

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask API!"}
    return jsonify(data)

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        # Vérification du type de contenu
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Validation des données
        required_fields = ['to', 'subject', 'message']
        missing_fields = [field for field in required_fields if not data.get(field)]
        
        if missing_fields:
            return jsonify({
                'status': 'error',
                'message': f'Champs manquants : {", ".join(missing_fields)}'
            }), 400

        email = data['to']
        if '@' not in email or '.' not in email:
            return jsonify({
                'status': 'error',
                'message': 'Format d\'email invalide'
            }), 400

        success, message = mail.send_email(
            message=data['message'],
            dest=data['to'],
            obj=data['subject']
        )

        if success:
            return jsonify({
                'status': 'success',
                'message': message
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': message
            }), 500

    except Exception as e:
        app.logger.error(f"Erreur lors de l'envoi de l'email: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Erreur lors de l\'envoi de l\'email: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)