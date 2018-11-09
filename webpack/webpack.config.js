let APP_NAME = process.env.app_name;

var webpack = require("webpack");
var path = require("path");

var SRC_DIR = path.resolve(__dirname, "src");
var DIST_DIR = path.resolve(__dirname, "../static/js/");

module.exports = {
  entry: [SRC_DIR + "/app/"+APP_NAME+".jsx"],
  output: {
    path: DIST_DIR + "/app",
    filename: APP_NAME+".js",
    publicPath: "/app/"
  },
  module: {
    rules: [
      {
        test: /\.js?/,
        enforce: "pre",
        include: SRC_DIR,
        loader: "babel-loader",
        query: {
          presets: ["react", "es2015", "stage-2"]
        }
      }
    ]
  }
};
