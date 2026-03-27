from .app import app, db
from quizz.models import Questionnaire

@app.cli.command()
def syncdb():
    db.drop_all()
    db.create_all()
    qz1 = Questionnaire.add_questionnaire('Maths')
    qz2 = Questionnaire.add_questionnaire('Francais')
    qz3 = Questionnaire.add_questionnaire('SVT')
    qz1 = Questionnaire.add_questionnaire('dev web')
    qz2 = Questionnaire.add_questionnaire('App mobile')
    qz3 = Questionnaire.add_questionnaire('JS')
    qz1.add_question("Question 1")
    qz1.add_question("Quelle est la capitale de la France ?", question_type="questionOuverte", reponse="Paris")
    qz1.add_question("Combien font 2+2 ?", question_type="questionChoixMultiple", proposition1="4", proposition2="5", bonne_reponse=1)
    qz2.add_question("Question 1")
    qz2.add_question("Qui a écrit Les Misérables ?", question_type="questionOuverte", reponse="Victor Hugo")
    qz2.add_question("Quel est le pluriel de cheval ?", question_type="questionChoixMultiple", proposition1="Chevals", proposition2="Chevaux", bonne_reponse=2)
    qz3.add_question("Question 1")
    qz3.add_question("Question 2")
    qz3.add_question("Question 3")
        
