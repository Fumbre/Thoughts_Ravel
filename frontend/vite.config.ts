import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from 'path'

export default defineConfig({
	plugins: [vue()],
	root: "src/mainview",
	envDir: path.resolve(__dirname, './'),
	build: {
		outDir: "../../dist",
		emptyOutDir: true,
	},
	server: {
		port: 5173,
		strictPort: false,
		host: true
	},
});
