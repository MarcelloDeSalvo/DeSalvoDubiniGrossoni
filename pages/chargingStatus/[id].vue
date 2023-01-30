<template>
    <div>
        <ChargingSocketDetail :ChargeSocket="socket"/>
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
        console.log(this.socket)
        
       

        // count bookings
        


      } catch (error) {
        this.response = error
        console.error(error)
      }
    },
  }
};
</script>