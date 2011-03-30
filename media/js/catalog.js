function get_coords( coords )
{
	var tmp = coords.split(',');
	for(i in tmp)
		tmp[i] = tmp[i].replace(' ',''); 
	var xy = {x:Number( tmp[0] ),y:Number( tmp[1] )};
	for( var i = 0; i < tmp.length; i+= 2 )
	{
		if( xy.y > Number( tmp[ i + 1 ] ) )
			xy = {x:Number( tmp[ i ] ),y:Number( tmp[ i + 1 ] )};
	}
	return xy;
}

function blockersub()
{
	var img = $(this);
	var w = img.width(), h = img.height();
	$("#draft_x").css('width', w + 'px').css('height', h + 'px');
}

$(document).ready(function(){
	$(".cattbl tr").hover( function() {
		var id = $(this).attr("id");
		$("#show-"+id).show();
	}, function() {
		var id = $(this).attr("id");
		$("#show-"+id).hide();
	});
	$("#maps area").hover( function() {
		var id = $(this).attr("id");
		var cut = id.lastIndexOf('-');
		id = id.substring( 0, cut );
		var coords = get_coords( $(this).attr("coords") );
		$("#sh"+id+"-info").show();
		var o1 = $("#sh"+id+"-info .showiteminfo").outerHeight();
		$("#sh"+id+"-info").css('top', (coords.y - o1 - 16) + 'px').css('left', ( coords.x - 4 ) + 'px');
		$("#sh"+id).show();
	}, function() {
		var id = $(this).attr("id");
		var cut = id.lastIndexOf('-');
		id = id.substring( 0, cut );
		$("#sh"+id+"-info").hide();
		$("#sh"+id).hide();
	});
	$("#selecting").change( function(){
	    var id = $(this).attr("value");
	    $(".hightlight").each(function(){
	    	var $this = $(this);
	    	if( $this.attr( 'id' ) !=  ('show-' + id ) )
	    		$this.hide();
	    });
	    if( id )
	    	$("#show-"+id).show();
	});
});
$(window).unload(function(){
	$('.info-item, .hightlight').hide();
});