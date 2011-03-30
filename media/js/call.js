$(document).ready(function(){
	$(".callback a").click( function() {
		$(".b-overtopbox-bg").show();
		$(".b-overtopbox").show();
		return false;
	});
	$(".b-overtopbox-close-a").click( function() {
		$(".b-overtopbox").hide();
		$(".b-overtopbox-bg").hide();
		return false;
	});
	$(".b-overtopbox-form form").ajaxForm({
		url: '/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B9-%D0%B7%D0%B2%D0%BE%D0%BD%D0%BE%D0%BA',
		dataType: 'json',
		beforeSubmit: function(arr, $form, options) {
			$(".b-overtopbox-text .ifnoerror, .b-overtopbox-text .iferror, .b-overtopbox-text .iftimewait").hide();
			$(".b-overtopbox-form label.iferror").removeClass("iferror");
		},
		success: function( json, statusText, xhr, form ){
			if( json.form_errors && json.form_errors['.timewait'] )
			{
				$(".b-overtopbox-text .iftimewait").show();
				return;
			}
			if( json.form_done )
				$(".b-overtopbox-text .ifnoerror").show();
			else if( json.form_errors )
			{
				$(".b-overtopbox-text .iferror").show();
				for( var id in json.form_errors )
					$( ".b-overtopbox-form label[for=call_" + id +"]" ).addClass("iferror");
			}
			if(json.form_result_call_name)
				$("#call_name").val(json.form_result_call_name);
			if(json.form_result_call_phone)
				$("#call_phone").val(json.form_result_call_phone);
		}
	});
});