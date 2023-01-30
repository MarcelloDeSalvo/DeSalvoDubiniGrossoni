<template>
    <section class="text-gray-600 body-font relative">
        <div class="absolute inset-0 bg-gray-300">
            <iframe width="100%" height="100%" frameborder="0" marginheight="0" marginwidth="0" title="map" scrolling="no" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d89547.2303835233!2d9.17773225!3d45.46273385!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4786c6aec34636a1%3A0xab7f4e27101a2e13!2sDuomo%20di%20Milano!5e0!3m2!1sit!2sit!4v1674845010871!5m2!1sit!2sit" style=""></iframe>
        </div>
        <div class="container px-5 py-24 mx-auto flex">
            <div class="lg:w-1/3 md:w-1/2 bg-white rounded-lg p-8 flex flex-col md:ml-auto w-full mt-10 md:mt-0 relative z-10 shadow-md">
            <h2 class="text-gray-900 text-lg mb-1 font-medium title-font">Find nearby charging stations!</h2>
            <p class="leading-relaxed mb-5 text-gray-600">Currently not implemented...</p>
            <div class="relative mb-4">
                <label for="city" class="leading-7 text-sm text-gray-600">City</label>
                <input type="text" id="city" name="city" class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
            <div class="relative mt-2 mb-6">
                <label for="address" class="leading-7 text-sm text-gray-600">Address</label>
                <input id="address" name="address" class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"/>
            </div>
            <button class="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Search</button>
            <p class="text-xs text-gray-500 mt-3">Filter nearby charging stations</p>
            </div>
        </div>
    </section>
</template>