/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  theme: {
    extend: {
      colors: {
        "gruv-black": "#282828",
        "gruv-red": "#cc241d",
        "gruv-green": "#98971a",
        "gruv-yellow": "#d79921",
        "gruv-blue": "#458588",
        "gruv-magenta": "#b16286",
        "gruv-cyan": "#689d6a",
        "gruv-white": "#a89984",
        "gruv-black-l": "#928374",
        "gruv-red-l": "#fb4934",
        "gruv-green-l": "#b8bb26",
        "gruv-yellow-l": "#fabd2f",
        "gruv-blue-l": "#83a598",
        "gruv-magenta-l": "#d3869b",
        "gruv-cyan-l": "#8ec07c",
        "gruv-white-l": "#ebdbb2",
      },
    },
  },
  plugins: [],
};
