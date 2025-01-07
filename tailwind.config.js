

/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./templates/**/*.html",
      "./**/templates/**/*.html"
    ],
    plugins: [
      require("daisyui")
    ],
    daisyui: {
        themes: true, // This enables all themes
    }
  }