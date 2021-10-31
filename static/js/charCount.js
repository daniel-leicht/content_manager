

    (function($) {
        $.fn.charCount = function(options){
            // default configuration properties
            var defaults = {
                css: 'help',
                counterElement: 'p',
                counterText: ''
            };

            var options = $.extend(defaults, options);
            function calculate(obj){
                var count = $(obj).val().length;
                $(obj).next().html(options.counterText + count);
            };

            this.each(function() {

                $(this).after('<'+ options.counterElement +' class="' + options.css + '">'+ options.counterText +'</'+ options.counterElement +'>');
                calculate(this);
                $(this).keyup(function(){calculate(this); });
                $(this).change(function(){calculate(this)});
            });

        };

    })(jQuery);

/*function init_counters(selector, len){
	$(selector).each(function() {
		//console.log($(this).attr('maxlength'));
		if(len==null){
			len = $(this).attr('maxlength');
		}
		$(this).charCount({
			counterText: 'Characters Remaining: ',
			allowed: len,
		});
	});
}*/

$(document).ready(function(){
    $("input[counted='true']").each(function(){
        console.log($(this));
        len = $(this).attr('maxlength');
        $(this).charCount({
            counterText: 'Character Count: ',
        });
    });
    //init_counters("input[maxlength]", 80);
    //init_counters("textarea[maxlength]");
    //init_counters("#id_abstract", 400);
});

/*
 * <style type="text/css">
form .counter{
	}
form .warning{color:#600;}
form .exceeded{color:#e00;}
</style>
*/