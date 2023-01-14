const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const isDevelopment = process.env.NODE_ENV !== 'production';

const CONFIG = {
  entry: './src/js/index.jsx',
  mode: isDevelopment ? 'development' : 'production',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'build/'),
    publicPath: '/',
  },
  plugins: [new CleanWebpackPlugin(), new HtmlWebpackPlugin({ template: './src/index.html' })],
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        options: { presets: ['@babel/env', '@babel/preset-react'] },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: { extensions: ['*', '.js', '.jsx'] },
};

if (isDevelopment) {
  CONFIG.devServer = {
    compress: true,
    port: 3000,
    static: path.join(__dirname, 'build/'),
    historyApiFallback: true,
    hot: true,
  };
  CONFIG.plugins = [new webpack.HotModuleReplacementPlugin()];
}

module.exports = CONFIG;
