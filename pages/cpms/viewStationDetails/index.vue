<template>
    <h1 class="text-center text-5xl mt-16 tracking-wide relative">{{ items.address}}</h1>
     <div>
        <StationSocketDetail :sockets="items.sockets"/>
     </div>
     <h1 class="text-center text-4xl mt-16 tracking-wide relative">Energy Providers</h1>   
</template>

<script>
let jsonString = '{"items": {"station":"Station1", "address":"Via Milano 4, Napoli 69420", "price":"€40", "currentDiscount":"10%", "sockets":[{"id": "1", "type": "Slow", "price": "40", "status": "Available"},{"id": "2", "type": "Fast", "price": "50", "status": "Unavailable"}]}}';
let parsedObject = JSON.parse(jsonString);
export default {
    data() {
        return {
            items: parsedObject.items
        }
    },
    setup() {
        definePageMeta({
            middleware: ['auth']
        })
    }
};
</script>