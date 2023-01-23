<template>
    <h1 v-text="station.address" class="text-center text-5xl mt-16 tracking-wide relative"></h1>
     <div>
        <StationSocketDetail :sockets="station.sockets"/>
     </div>
     <div class="text-center mt-20">
        <p class="w-full px-3 py-2 mb-3 text-lm leading-tight text-red-700 rounded appearance-none focus:outline-none focus:shadow-outline">
            {{response}}
        </p>
	  </div>
     <h1 class="text-center text-4xl mt-16 tracking-wide relative">Energy Providers</h1>   
</template>

<script>
export default {
    data() {
        return {
            station: "",
            id: "",
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth']
        })
        const route = useRoute()// When accessing /posts/1, route.params.id will be 1
        
    },
    created() {
        this.updateStation()
    },

    methods: {
        async updateStation() {
            try{
            this.id = this.$route.params.id
            console.log("ID", this.id)
            if (this.id == null)
                throw new Error("No ID provided")
        
            let {response, json} = await getRequest('CPMS', 'api/getChargingStation/'+ this.id +'/')
            this.station = json
  
            } catch (error) {
                this.response = error
                console.error(error)
            }
        },
    }
};
</script>