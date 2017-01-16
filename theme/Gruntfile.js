module.exports = function (grunt) {
    grunt.initConfig({
        copy: { // Copying files
            main: {
                files: [
                    {   //Fonts
                        expand: true,
                        src: [
                            'vendor/**/fonts/*',
                            'vendor/**/static/fonts/*'
                        ],
                        dest: 'static/fonts/',
                        flatten: true
                    },
                    {   //Images
                        expand: true,
                        src: [
                            'assets/img/*.png',
                            'assets/img/*.jpg'
                        ],
                        dest: 'static/img/',
                        flatten: true
                    },
                    {   //Favicon
                        expand: true,
                        src: [
                            'assets/favicon/*'
                        ],
                        dest: 'static/favicon',
                        flatten: true
                    },
                    {   //Pygments
                        expand: true,
                        src: [
                            'assets/css/pygments/*'
                        ],
                        dest: 'static/css/pygments',
                        flatten: true
                    }
                ]
            }
        },
        less: {
            development: {
                options: {
                    paths: ["design"]
                },
                files: {
                    "static/css/style.css": "assets/less/style.less"
                }
            },
            production: {
                options: {
                    paths: ["design"],
                    plugins: [
                        new (require('less-plugin-autoprefix'))({browsers: ["last 2 versions"]}),
                        new (require('less-plugin-clean-css'))()
                    ]
                },
                files: {
                    "static/css/style.css": "assets/less/style.less"
                }
            }
        },
        uglify: {
            js: {
                files: {
                    'static/js/main.js': [
                        'vendor/jquery/dist/jquery.js',
                        'vendor/jquery.gifplayer/dist/jquery.gifplayer.js',
                        'vendor/**/dist/js/*.min.js',
                        'vendor/wowjs/dist/wow.min.js',
                        'assets/js/*.js'
                    ]
                },
                options: {
                    preserveComments: false,
                    sourceMap: true
                }
            }
        }

    });
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-uglify')
};

