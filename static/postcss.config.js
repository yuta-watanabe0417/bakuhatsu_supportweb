module.exports = () => ({
  plugins: {
    // '@fullhuman/postcss-purgecss': {
    //   content: ['./**/*.html'],
    // },
    autoprefixer: {},
    'node-css-mqpacker': {
      from: '',
      map: {
        inline: false,
      },
      sort: true,
      to: 'assets/css/main.css',
    },
  },
});
