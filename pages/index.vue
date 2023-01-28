<template>
  <div>
      <HeaderHome />
      <Steps />
      <FooterHome />
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['cpms-auth', 'auth']
})
</script>