function update_captcha( src, sel )
{
	var src = src + (new Date()).getTime();
	if( window.xrname )
		src += '&' + encodeURIComponent( xrname ) + '=' + encodeURIComponent( xrid );
	$( sel ).attr( 'src', src );
	if( !$( sel ).attr( 'onload' ) )
	{
		$( sel ).attr( 'onload', true );
		$( sel ).load( function(){ alert( 'Внимание! Получен новый код!' ); } );
	}
	return void(0);
}