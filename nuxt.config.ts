// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    css: ['~/assets/css/main.css'],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    runtimeConfig: {
        public: {
          EMSP_URL: process.env.EMSP_URL,
          CPMS_URL: process.env.CPMS_URL
        },
        private:{
          EMSP_URL: process.env.EMSP_URL,
          CPMS_URL: process.env.CPMS_URL,
        }
    }
})
