export default class API {
    constructor(url = 'http://localhost:5000') {
        this.url = url;
    }

    async getQuizs(){
        const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs`);
        if (response.ok){
            const json = await response.json();
            return json;
        }
        return null;
    }

    async getQuiz(id){
        const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${id}`);
        if (response.ok){
            const json = await response.json();
            return json;
        }
        return null;
    }

    async deleteQuiz(id) {
        try{
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${id}`, {
                method: 'DELETE'
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Erreur de suppression");
            }

            return await response.json();
        } catch (error) {
            console.error("Erreur suppression:", error);
            throw error;
        }
    }

    async addQuiz(nom) {
        try {
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({nom: nom})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Erreur lors de l'ajout");
            }
            return await response.json();
        } catch (error) {
            console.error("Erreur ajout:", error);
            throw error;
        }
    }

    async modifyQuiz(id, nom) {
        try{
            const response = await fetch(`${this.url}/quizz_app/api/v1.0/quizzs/${id}`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({nom : nom})
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Erreur de suppression");
            }

            return await response.json();
        } catch (error) {
            console.error("Erreur suppression:", error);
            throw error;
        }
    }

}
