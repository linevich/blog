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
                    "static/css/style.css": "assets/less/style.less",
                    "static/css/editor.css": "assets/less/editor.less"
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
                    "static/css/style.css": "assets/less/style.less",
                    "static/css/editor.css": "assets/less/editor.less"
                }
            }
        },
        uglify: {
            js: {
                files: {
                    'static/js/main.js': [
                        'vendor/**/static/*.min.js',
                        'vendor/**/static/js/*.min.js',
                        'vendor/**/static/js/*.min.js',
                        'vendor/**/*.min.js',
                        'vendor/jquery-ajax-form/*.js',
                        // Assets
                        'assets/*.min.js',
                        'assets/**/*.min.js',
                        'assets/**/*.js'
                    ]
                },
                options: {
                    preserveComments: false
                }
            }
        }

    });
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-uglify')
};

