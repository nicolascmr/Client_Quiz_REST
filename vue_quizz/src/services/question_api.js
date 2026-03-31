export default class QuestionAPI {
    constructor(url = 'http://localhost:5000') {
        this.url = url;
    }

    async getQuestions(idQuizz) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}`);
            if (!response.ok) {
                throw new Error("Erreur lors de la récupération des questions");
            }
            const json = await response.json();
            return json;
        } catch (error) {
            console.error("Erreur getQuestions:", error);
            throw error;
        }
    }

    async addQuestionOuverte(idQuizz, enonce, reponse) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"enonce": enonce, "reponse": reponse, "question_type": "questionOuverte"})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erreur lors de l'ajout de la question");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur addQuestion:", error);
            throw error;
        }
    }

    async addQuestionQCM(idQuizz, enonce, options, reponse) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"enonce": enonce, "proposition1": options[0], "proposition2": options[1], "bonne_reponse": reponse, "question_type": "questionChoixMultiple"})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erreur lors de la modification de la question");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur modifyQuestion:", error);
            throw error;
        }
    }

    async modifyQuestionOuverte(idQuizz, idQuestion, enonce, reponse) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}/${idQuestion}`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"enonce": enonce, "reponse": reponse})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erreur lors de la modification de la question");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur modifyQuestion:", error);
            throw error;
        }
    }

    async modifyQuestionQCM(idQuizz, idQuestion, enonce, options, reponse) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}/${idQuestion}`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({"enonce": enonce, "proposition1": options[0], "proposition2": options[1], "bonne_reponse": reponse})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erreur lors de la modification de la question");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur modifyQuestion:", error);
            throw error;
        }
    }

    async deleteQuestion(idQuizz, idQuestion) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${idQuizz}/${idQuestion}`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || "Erreur lors de la suppression de la question");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur deleteQuestion:", error);
            throw error;
        }
    }
}