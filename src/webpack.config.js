var path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: './src/js/app.js', // can be an array, a js object or single file as string. path should be relative to the config file.
    output: {
        path: path.resolve(__dirname, 'dist'), // we use resolve because we need an absolute path
        filename: 'bundle.js',
        publicPath: '/dist/'
    },
    module: {
        rules: [
            {
                // loaders are applaied to every single file
                test: /\.css$/,
                use: [
                    'style-loader',
                    'css-loader' // this loader is applied first
                ]

            },
            {
                test: /\.(png|svg|jpe?g|gif)$/i,
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                        name: '[name].[ext]'
                    }
                  },
                  {
                    loader: 'image-webpack-loader',
                    options: {
                      bypassOnDebug: true,
                    },
                  }
                ]
            },
        ]
    },
    devServer: {
        proxy: {
          '/': 'http://127.0.0.1:8000'
        }
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery'
        })
    ]
};