<template lang="pug">
.w-full.flex.items-center.flex-col
  .w-full.bg-white.empty.border-dashed(v-if="isUsersEmpty")
    .text-xl.text-gray-400.text-center There is nothing here!
    .project-logo.flex.justify-center.mt-10(class="h-1/4 ")
      svg-icon(name="box", addClass="fill-current text-gray-300 w-24 h-24")
    .flex.justify-center.mt-10
      t-button.mt-10.w-full.text-center(tagName="a" :href="`users/create`")
        | Create New User
  .gap-y-3.flex.flex-col.w-full(v-if="!isUsersEmpty")
    user-card.card(v-for="u in users" :u="u")

    t-button.mt-10.w-full.text-center(tagName="a" href="users/create" text="Create New User")
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SvgIcon from '@/components/SvgIcon'
import UserCard from '@/components/UserCard'

export default {
  components: {
    SvgIcon, UserCard
  },
  data () {
    return {
      isSpinner: false,
      title: 'Users'
    }
  },
  computed: {
    ...mapGetters('user', ['users']),
    isUsersEmpty () {
      return this.users.length === 0
    }
  },
  methods: {
    ...mapActions('user', ['getUsers', 'createUser']),
    load () {
      this.isSpinner = true
      this.getUsers().finally(() => { this.isSpinner = false })
    }
  },
  mounted () {
    this.load()
  }
}
</script>

<style lang="postcss">
.connections-container .empty {
  @apply  p-3 border-2 w-2/4 rounded-md
}
.empty {
  @apply border-dashed p-3 border-2 rounded-md w-full
}

</style>
