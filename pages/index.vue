<template>
  <div>
      <HeaderHome />
      <Steps />
      <FooterHome />
  </div>
</template>

<script setup>
definePageMeta({
  middleware: ['cpmsauth', 'auth']
})
</script>