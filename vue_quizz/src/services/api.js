export default class API {
    constructor(url = 'http://localhost:3000') {
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

}
