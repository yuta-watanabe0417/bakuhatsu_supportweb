module.exports = () => ({
  plugins: {
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
