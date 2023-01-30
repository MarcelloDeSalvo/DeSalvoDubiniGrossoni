<template>
  <div>
    <ChargingSocketDetail :ChargeSocket="socket" />
  </div>
  <div class="button">
    <button @click="stopCharge(id)"
      class="group relative h-12 w-48 overflow-hidden rounded-lg bg-white text-lg shadow ">
      <div class="absolute inset-0 w-3 bg-red-400 transition-all duration-[250ms] ease-out group-hover:w-full"></div>
      <span class="relative text-black group-hover:text-white">Finish charging</span>
    </button>
  </div>
  <div class="button">
    <button @click="fakePay(id)" class="group relative h-12 w-48 overflow-hidden rounded-lg bg-white text-lg shadow ">
      <div class="absolute inset-0 w-3 bg-blue-400 transition-all duration-[250ms] ease-out group-hover:w-full"></div>
      <span class="relative text-black group-hover:text-white">Pay</span>
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      socket: "",
      id: "",
      bookingLength: 0,
    }
  },
  mounted() {
    setInterval(() => {
      location.reload()
    }, 60000) // reload every 60 seconds
  },
  setup() {
    definePageMeta({
      layout: "emspnavlayout"
    })
  },
  created() {
    this.updateSocket()
  },

  methods: {
    async updateSocket() {
      try {
        this.id = this.$route.params.id
        console.log("ID", this.id)
        if (this.id == null)
          throw new Error("No ID provided")

        let { response, json } = await getRequestWithToken('emsp', 'OCPI/getSocket/' + this.id + '/')
        this.socket = json
    
      } catch (error) {
        this.response = error
        console.error(error)
      }
    },
    async stopCharge(id) {
      let { response, json } = await getRequestWithToken('emsp', 'OCPI/stopCharge/' + this.id + '/')
      //handles stopcharge button
    }
  }
};
</script>

<style>
.button {
  margin-top: 20px;
  margin-left: 8%;
}
</style>