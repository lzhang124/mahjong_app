const path = require('path');
const webpack = require('webpack');

const isDevelopment = process.env.NODE_ENV !== 'production';

const CONFIG = {
  entry: './src/js/index.jsx',
  mode: isDevelopment ? 'development' : 'production',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'build'),
    publicPath: '/',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        options: { presets: ['@babel/preset-env', '@babel/preset-react'] },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
          },
        ],
      },
    ],
  },
  resolve: { extensions: ['*', '.js', '.jsx'] },
};

if (isDevelopment) {
  CONFIG.devServer = {
    compress: true,
    port: 3000,
    static: path.join(__dirname, 'build'),
    historyApiFallback: true,
    hot: true,
  };
  CONFIG.plugins = [new webpack.HotModuleReplacementPlugin()];
}

module.exports = CONFIG;
