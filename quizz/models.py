from .app import db

class Questionnaire(db.Model):
    __tablename__ = 'Questionnaire'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    questions = db.relationship('Question', back_populates='questionnaire', cascade="all, delete, delete-orphan")

    def __init__(self, nom):
        self.nom = nom
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    @staticmethod
    def get_all_questionnaires():
        return Questionnaire.query.all()
    
    @staticmethod
    def get_questionnaire(id):
        q = Questionnaire.query.get(id)
        return q
    
    @staticmethod
    def add_questionnaire(nom):
        q = Questionnaire.query.filter_by(nom=nom).first()
        if not q:
            questionnaire = Questionnaire(nom)
            db.session.add(questionnaire)
            db.session.commit()
            return questionnaire
        return None
    
    @staticmethod
    def del_questionnaire(q_id):
        q = Questionnaire.query.filter_by(id=q_id).first()
        db.session.delete(q)
        db.session.commit()
        return q
            
    def add_question(self, enonce, question_type="question", reponse=None, proposition1=None, proposition2=None, bonne_reponse=None):
        if question_type == 'questionOuverte':
            question = QuestionOuverte(enonce, len(self.questions)+1, self.id, self, reponse)
        elif question_type == 'questionChoixMultiple':
             question = QuestionChoixMultiple(enonce, len(self.questions)+1, self.id, self, 
                                              proposition1, 
                                              proposition2, 
                                              bonne_reponse)
        else:
            question = Question(enonce, len(self.questions)+1, self.id, self)
        
        self.questions.append(question)
        db.session.add(question)
        db.session.commit()
        return question
    
    def get_questions(self):
        return self.questions
    
    def get_question(self, numero):
        for i in range(len(self.questions)):
            if(self.questions[i].numero == numero):
                return self.questions[i]
    
    def del_question(self, numero):
        for i in range(len(self.questions)):
            if(self.questions[i].numero == numero):
                question = self.questions.pop(i)
                db.session.delete(question)
                db.session.commit()
                return question
            
    def to_json(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'questions': [question.to_json() for question in self.questions]
        }


class Question(db.Model):
    __tablename__ = 'Question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer)
    enonce = db.Column(db.String(100))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('Questionnaire.id'))
    questionnaire = db.relationship('Questionnaire', back_populates='questions')
    
    question_type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'polymorphic_on': question_type
    }

    def __init__(self, enonce, numero, questionnaire_id, questionnaire):
        self.numero = numero
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id
        self.questionnaire = questionnaire


    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero

    def to_json(self):
        return {
            'numero': self.numero,
            'enonce': self.enonce,
            'question_type': self.question_type
        }

class QuestionOuverte(Question):
    __tablename__ = 'QuestionOuverte'
    id = db.Column(db.Integer, db.ForeignKey('Question.id'), primary_key=True)
    reponse = db.Column(db.String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'questionOuverte',
    }

    def __init__(self, enonce, numero, questionnaire_id, questionnaire, reponse):
        super().__init__(enonce, numero, questionnaire_id, questionnaire)
        self.reponse = reponse
    
    def to_json(self):
        json = super().to_json()
        json['reponse'] = self.reponse
        return json

class QuestionChoixMultiple(Question):
    __tablename__ = 'QuestionChoixMultiple'
    id = db.Column(db.Integer, db.ForeignKey('Question.id'), primary_key=True)
    proposition1 = db.Column(db.String(100))
    proposition2 = db.Column(db.String(100))
    bonne_reponse = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'questionChoixMultiple',
    }

    def __init__(self, enonce, numero, questionnaire_id, questionnaire, proposition1, proposition2, bonne_reponse):
        super().__init__(enonce, numero, questionnaire_id, questionnaire)
        self.proposition1 = proposition1 
        self.proposition2 = proposition2
        self.bonne_reponse = bonne_reponse

    def to_json(self):
        json = super().to_json()
        json['proposition1'] = self.proposition1
        json['proposition2'] = self.proposition2
        json['bonne_reponse'] = self.bonne_reponse
        return json


