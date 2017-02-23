/**
 * Js libs settings
 */


// Material settings
$.material.init();


// WOW.js settings
var wow = new WOW({
    mobile: false
});
wow.init();

$('.gif').gifplayer();

$('.related-article-title').each(function (i) {
    $clamp(this, {clamp: 2});
});
