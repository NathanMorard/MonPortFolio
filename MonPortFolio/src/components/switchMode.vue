<template>
  <label class="switch">
    <input type="checkbox" />
    <span class="slider round"></span>
  </label>
</template>

<script setup>
import { useDark } from '@vueuse/core'

const isDark = useDark();
</script>

<style></style>
