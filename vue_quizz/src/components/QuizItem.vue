<script>
export default{
    props: {
        quiz : Object
    },
    methods:{
        suppr: function() {
            this.$emit('remove', {id:this.quiz.id});
        },
        modif: function() {
            this.$emit('modify', {id:this.quiz.id, text:this.quiz.nom});
        }
    },
    
    emits: ['remove']
}
</script>

<template>
        <input type="text" :value="quiz.nom">
        <input type="button"
                class="btn btn-danger"
                value="Supprimer"
                @click="suppr">
        <input type="button" value="Modifier" class="btn" @click="modif">
</template>
