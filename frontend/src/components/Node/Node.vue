<script setup>
import { ref } from 'vue'
import { computed } from 'vue'

const point = ref(null)

    const handleClick = (event) => {
    point.value = {
        x: event.clientX,
        y: event.clientY
    }
    console.log("point value:", point.value)

    }

   


    const floatingStyle = computed(() => {
        if (!point.value) return {}

        return {
            position: 'fixed',
            left: point.value.x + 'px',
            top: point.value.y + 'px',
            zIndex: 1000,
            pointerEvents: 'none'
        }
        }
    )

    document.addEventListener('mouseleave', (ev) => {
        handleClick();        
    })

</script>



<template>
  <div @click="handleClick">
    <canvas></canvas>
    <div>transform once in the click</div>
    create element while clicked in the correct possition once than use css to translate n-second in the clicked handle 

    <div
      v-if="point"
      :style="floatingStyle"
      class="floating-element"
    >
      📍
    </div>
  </div>
</template>