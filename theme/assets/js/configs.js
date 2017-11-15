/**
 * Js libs settings
 */


// Material settings
$.material.init();

$('.gif').gifplayer();

$('.related-article-title').each(function (i) {
    $clamp(this, {clamp: 2});
});