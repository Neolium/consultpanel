!function(t){"use strict";t.event.special.destroyed||(t.event.special.destroyed={remove:function(t){t.handler&&t.handler()}}),t.fn.extend({maxlength:function(e,a){function n(t){var a=t.val();a=e.twoCharLinebreak?a.replace(/\r(?!\n)|\n(?!\r)/g,"\r\n"):a.replace(new RegExp("\r?\n","g"),"\n");var n=0;return n=e.utf8?s(a):a.length}function o(t,a){var n=t.val(),o=0;e.twoCharLinebreak&&(n=n.replace(/\r(?!\n)|\n(?!\r)/g,"\r\n"),"\n"===n.substr(n.length-1)&&n.length%2===1&&(o=1)),t.val(n.substr(0,a-o))}function s(t){for(var e=0,a=0;a<t.length;a++){var n=t.charCodeAt(a);128>n?e++:e+=n>127&&2048>n?2:3}return e}function r(t,a,o){var s=!0;return!e.alwaysShow&&o-n(t)>a&&(s=!1),s}function i(t,e){var a=e-n(t);return a}function l(t,e){e.css({display:"block"}),t.trigger("maxlength.shown")}function c(t,a){e.alwaysShow||(a.css({display:"none"}),t.trigger("maxlength.hidden"))}function p(t,a,n){var o="";return e.message?o="function"==typeof e.message?e.message(t,a):e.message.replace("%charsTyped%",n).replace("%charsRemaining%",a-n).replace("%charsTotal%",a):(e.preText&&(o+=e.preText),o+=e.showCharsTyped?n:a-n,e.showMaxLength&&(o+=e.separator+a),e.postText&&(o+=e.postText)),o}function h(t,a,n,o){o&&(o.html(p(a.val(),n,n-t)),t>0?r(a,e.threshold,n)?l(a,o.removeClass(e.limitReachedClass).addClass(e.warningClass)):c(a,o):l(a,o.removeClass(e.warningClass).addClass(e.limitReachedClass))),e.customMaxAttribute&&(0>t?a.addClass("overmax"):a.removeClass("overmax"))}function f(e){var a=e[0];return t.extend({},"function"==typeof a.getBoundingClientRect?a.getBoundingClientRect():{width:a.offsetWidth,height:a.offsetHeight},e.offset())}function u(a,n){var o=f(a);if("function"===t.type(e.placement))return void e.placement(a,n,o);if(t.isPlainObject(e.placement))return void d(e.placement,n);var s=a.outerWidth(),r=n.outerWidth(),i=n.width(),l=n.height();switch(e.appendToParent&&(o.top-=a.parent().offset().top,o.left-=a.parent().offset().left),e.placement){case"bottom":n.css({top:o.top+o.height,left:o.left+o.width/2-i/2});break;case"top":n.css({top:o.top-l,left:o.left+o.width/2-i/2});break;case"left":n.css({top:o.top+o.height/2-l/2,left:o.left-i});break;case"right":n.css({top:o.top+o.height/2-l/2,left:o.left+o.width});break;case"bottom-right":n.css({top:o.top+o.height,left:o.left+o.width});break;case"top-right":n.css({top:o.top-l,left:o.left+s});break;case"top-left":n.css({top:o.top-l,left:o.left-r});break;case"bottom-left":n.css({top:o.top+a.outerHeight(),left:o.left-r});break;case"centered-right":n.css({top:o.top+l/2,left:o.left+s-r-3});break;case"bottom-right-inside":n.css({top:o.top+o.height,left:o.left+o.width-r});break;case"top-right-inside":n.css({top:o.top-l,left:o.left+s-r});break;case"top-left-inside":n.css({top:o.top-l,left:o.left});break;case"bottom-left-inside":n.css({top:o.top+a.outerHeight(),left:o.left})}}function d(a,n){if(a&&n){var o=["top","bottom","left","right","position"],s={};t.each(o,function(t,a){var n=e.placement[a];"undefined"!=typeof n&&(s[a]=n)}),n.css(s)}}function g(){return"bottom-right-inside"===e.placement||"top-right-inside"===e.placement||"function"==typeof e.placement||e.message&&"function"==typeof e.message}function m(t){var a=t.attr("maxlength")||e.customMaxAttribute;if(e.customMaxAttribute&&!e.allowOverMax){var n=t.attr(e.customMaxAttribute);(!a||a>n)&&(a=n)}return a||(a=t.attr("size")),a}var v=t("body"),b={showOnReady:!1,alwaysShow:!1,threshold:10,warningClass:"label label-success",limitReachedClass:"label label-important label-danger",separator:" / ",preText:"",postText:"",showMaxLength:!0,placement:"bottom",message:null,showCharsTyped:!0,validate:!1,utf8:!1,appendToParent:!1,twoCharLinebreak:!0,customMaxAttribute:null,allowOverMax:!1};return t.isFunction(e)&&!a&&(a=e,e={}),e=t.extend(b,e),this.each(function(){function a(){var a=p(r.val(),n,"0");n=m(r),s||(s=t('<span class="bootstrap-maxlength"></span>').css({display:"none",position:"absolute",whiteSpace:"nowrap",zIndex:1099}).html(a)),r.is("textarea")&&(r.data("maxlenghtsizex",r.outerWidth()),r.data("maxlenghtsizey",r.outerHeight()),r.mouseup(function(){r.outerWidth()===r.data("maxlenghtsizex")&&r.outerHeight()===r.data("maxlenghtsizey")||u(r,s),r.data("maxlenghtsizex",r.outerWidth()),r.data("maxlenghtsizey",r.outerHeight())})),e.appendToParent?(r.parent().append(s),r.parent().css("position","relative")):v.append(s);var o=i(r,m(r));h(o,r,n,s),u(r,s)}var n,s,r=t(this);t(window).resize(function(){s&&u(r,s)}),e.showOnReady?r.ready(function(){a()}):r.focus(function(){a()}),r.on("maxlength.reposition",function(){u(r,s)}),r.on("destroyed",function(){s&&s.remove()}),r.on("blur",function(){!s||e.showOnReady||e.alwaysShow||s.remove()}),r.on("input",function(){var t=m(r),a=i(r,t),l=!0;return e.validate&&0>a?(o(r,t),l=!1):h(a,r,n,s),g()&&u(r,s),l})})}})}(jQuery);