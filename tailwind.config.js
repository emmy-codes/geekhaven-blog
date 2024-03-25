/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        'purple-heart': {
          '50': '#fef6f6',
          '100': '#fde8ed',
          '200': '#fbd0e1',
          '300': '#f8afd7',
          '400': '#f47cd2',
          '500': '#ef48dc',
          '600': '#df27ec',
          '700': '#a817d9',
          '800': '#7309b9',
          '900': '#4b1094',
          '950': '#200571',
        },
      }
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/line-clamp'),
    require('daisyui'),
  ],
  daisyui: {},
  safelist: [
    'alert-info',
    'alert-success',
    'alert-warning',
    'alert-error',
  ],
}

