<script setup lang="ts">
import { useAuth } from '@/hooks/useAuth' // Adjust path if needed

// Destructure what you need from the hook
const { user, initialized, isAuthenticated, logout } = useAuth()

const handleLogout = async () => {
    try {
        await logout()
    } catch (err) {
        console.error("Failed to log out:", err)
    }
}

console.log(user)

</script>

<template>
    <div class="profile-card">
        <div v-if="!initialized">Loading user session...</div>

        <div v-else-if="isAuthenticated" class="profile-card__wrapper">
            <h2 class="profile-card__title">Welcome back, {{ user?.username }}!</h2>
            <button class="profile-card__logout btn" @click="handleLogout">Log Out</button>
        </div>
    </div>
</template>

<style scoped>
.profile-card {
    margin-bottom: 45px;
}

.profile-card__wrapper {
    display: flex;
    align-items: center;
}

.profile-card__title {
    margin-right: auto;
}

.profile-card__logout {
    height: fit-content;
}
</style>
