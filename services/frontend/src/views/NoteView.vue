<template>
    <div v-if="note" style="padding-top:3%">
        <p><strong>Title: </strong>{{ note.title }}</p>
        <p><strong>Content: </strong>{{ note.content }}</p>
        <p><strong>Author: </strong>{{ note.author.username }}</p>

        <div v-if="user.id==note.author.id">
            <p><router-link :to="{name: 'EditNoteView', params: {id: note.id}}" class="btn btn-primary">Edit Note</router-link></p>
            <p><button @click="removeNote()" class="btn btn-danger">Delete</button></p>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

    export default {
        name: 'NoteView',
        props: ['id'],
        async created(){
            try{
                await this.viewNote(this.id);
            } catch(error){
                console.error(error);
                this.$route.push('/dashboard');
            }
        },
        computed:{
            ...mapGetters({note: 'stateNote', user: 'stateUser'}),
        },
        methods: {
            ...mapActions(['viewNote', 'deleteNote']),
            async removeNote(){
                try{
                    await this.deleteNote(this.id);
                    this.$router.push('/dashboard');
                } catch(error){
                    console.error(error);
                }
            }
        },
    };
</script>