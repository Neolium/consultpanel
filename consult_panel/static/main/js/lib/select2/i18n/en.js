!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var e=jQuery.fn.select2.amd;return e.define("select2/i18n/en",[],function(){return{errorLoading:function(){return"The results could not be loaded."},inputTooLong:function(e){var n=e.input.length-e.maximum,r="Please delete "+n+" character";return 1!=n&&(r+="s"),r},inputTooShort:function(e){var n=e.minimum-e.input.length,r="Please enter "+n+" or more characters";return r},loadingMore:function(){return"Loading more results…"},maximumSelected:function(e){var n="You can only select "+e.maximum+" item";return 1!=e.maximum&&(n+="s"),n},noResults:function(){return"No results found"},searching:function(){return"Searching…"}}}),{define:e.define,require:e.require}}();