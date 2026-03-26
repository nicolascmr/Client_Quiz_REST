<script>
export default{
    props: {
        quiz : Object,
        index : Number
    },
    data() {
        return {
            editing: []
        }
    },
    methods:{
        suppr: function() {
            this.$emit('remove', {id:this.quiz.id});
        },
        toggleEdit: function() {
            if(this.editing[this.index]){
                this.$emit('modify', {id:this.quiz.id, text:this.quiz.nom})
            }
            this.editing[this.index] = !this.editing[this.index]
        }
    },
    
    emits: ['remove', 'modify']
}
</script>

<template>
    <div>
        <input v-if="editing[index]" v-model="quiz.nom" @keyup.enter="toggleEdit" />
        <span v-else>{{ quiz.nom }}</span>
        <button @click="toggleEdit" type="button">
          {{ editing[index] ? 'OK' : 'Éditer' }}
        </button>
        <input type="button"
                class="btn btn-danger"
                value="Supprimer"
                @click="suppr">
    </div>
</template>
