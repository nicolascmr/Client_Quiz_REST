<script>
import API from '../services/api';

export default{
    props: {
        quizList : [],
        api: new API()
    },
    methods:{
        get: async function() {
            json = await this.api.getQuizs();
            return json;
        },
    },
    
}
</script>