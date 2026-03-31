from flask import jsonify, abort, make_response, request, url_for
from .app import app, db
from quizz.models import Questionnaire, QuestionOuverte, QuestionChoixMultiple

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/quizz_app/api/v1.0/quizzs', methods = ['GET'])
def get_quizzs():
    quizzs = Questionnaire.get_all_questionnaires()
    res = []
    for quizz in quizzs:
        res.append(quizz.to_json())
    return jsonify({'questionnaires': res})

@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>', methods = ['GET'])
def get_quizz(questionnaire_id):
    questionnaire = Questionnaire.get_questionnaire(questionnaire_id)
    if questionnaire:
        return jsonify({'questionnaire': questionnaire.to_json()})
    return abort(404)

@app.route('/quizz_app/api/v1.0/quizzs', methods = ['POST'])
def create_quizz():
    if not request.json or not 'nom' in request.json:
        return abort(400)
    questionnaire = Questionnaire.add_questionnaire(request.json['nom'])
    return jsonify ({'questionnaire': questionnaire.to_json()}), 201

@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>', methods = ['POST'])
def create_question(questionnaire_id):
    if not request.json or not 'enonce' in request.json:
        return abort(400)
    
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if not questionnaire:
        return abort(404)
        
    question_type = request.json.get('question_type', 'question')
    reponse = request.json.get('reponse')
    proposition1 = request.json.get('proposition1')
    proposition2 = request.json.get('proposition2')
    bonne_reponse = request.json.get('bonne_reponse')
    
    question = questionnaire.add_question(
        enonce=request.json['enonce'],
        question_type=question_type,
        reponse=reponse,
        proposition1=proposition1,
        proposition2=proposition2,
        bonne_reponse=bonne_reponse
    )
    
    return jsonify ({'question': question.to_json()}), 201
    
@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>', methods = ['PUT'])
def modify_quizz(questionnaire_id):
    if not request.json or not 'nom' in request.json:
        return abort(400)
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if questionnaire:
        questionnaire.nom = request.json['nom']
        db.session.commit()
        return jsonify ({'questionnaire': questionnaire.to_json()}), 201
    return abort(404)

@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>/<int:question_id>', methods = ['PUT'])
def modify_question(questionnaire_id, question_id):
    if not request.json or not 'enonce' in request.json:
        return abort(400)
    questionnaire = Questionnaire.query.get(questionnaire_id)
    question = questionnaire.get_question(question_id)
    if question:
        question.enonce = request.json['enonce']
        if question.question_type == 'questionOuverte':
            question.reponse = request.json.get('reponse')
        elif question.question_type == 'questionChoixMultiple':
            question.proposition1 = request.json.get('proposition1')
            question.proposition2 = request.json.get('proposition2')
            question.bonne_reponse = request.json.get('bonne_reponse')
        
        db.session.commit()
        return jsonify ({'question': question.to_json()}), 201
    return abort(404)

@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>', methods = ['DELETE'])
def delete_quizz(questionnaire_id):
    supprime = Questionnaire.del_questionnaire(questionnaire_id)
    if supprime:
        return make_response(jsonify({'status': 'deleted'}), 200)
    return abort(404)  

@app.route('/quizz_app/api/v1.0/quizzs/<int:questionnaire_id>/<int:question_numero>', methods = ['DELETE'])
def delete_question(questionnaire_id, question_numero):
    questionnaire = Questionnaire.query.get(questionnaire_id)
    if questionnaire:
        supprime = questionnaire.del_question(question_numero)
        if supprime:
            questions = questionnaire.get_questions()
            for i in range(len(questions)):
                questions[i].set_numero(i + 1)
            
            db.session.commit()
            
            return make_response(jsonify({'status': 'deleted'}), 200)
    return abort(404)






