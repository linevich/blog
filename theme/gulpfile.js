'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass');
const sourcemaps = require('gulp-sourcemaps');
const cleanCSS = require('gulp-clean-css');

const scssSrc = './assets/scss/**/*.scss';
const cssSrc = './static/css';


gulp.task('scss_dev', function () {
  return gulp.src(scssSrc)
    .pipe(sourcemaps.init())
    .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest(cssSrc));
});

gulp.task('scss_prod', function () {
  return gulp.src(scssSrc)
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(cleanCSS({compatibility: 'ie8', level: 2}))
    .pipe(gulp.dest(cssSrc));
});

gulp.task('build_dev', ['scss_dev']);
gulp.task('build_prod', ['scss_prod']);