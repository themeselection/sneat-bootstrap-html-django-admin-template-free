const path = require('path');
const { src, dest, series } = require('gulp');
const purgecss = require('gulp-purgecss');
const useref = require('gulp-useref');
var uglify = require('gulp-uglify');
const fs = require('fs');

module.exports = conf => {

  // Combine js vendor assets in single core.js file using UseRef
  // -------------------------------------------------------------------------------
  const prodUseRefTasks = function () {
    return src(`${buildPath}/*.html`).pipe(useref()).pipe(dest(buildPath));
  };

  // Uglify assets/js files
  //--------------------------------------------------------------------------------
  const prodMinifyJSTasks = function () {
    return src(`${buildPath}/assets/js/**/*.js`)
      .pipe(uglify())
      .pipe(dest(`${buildPath}/assets/js/`));
  };

  // Suppress DeprecationWarning for useref()
  process.removeAllListeners('warning');

  process.on('warning', warning => {
    if (warning.name === 'DeprecationWarning' && warning.code === 'DEP0180') {
      return;
    }
    console.warn(warning.name, warning.message);
  });


  const prodAllTask = series(
    prodMinifyJSTasks,
    prodUseRefTasks
  );

  // Exports
  // ---------------------------------------------------------------------------

  return {
    useref: prodUseRefTasks,
    all: prodAllTask
  };
};
