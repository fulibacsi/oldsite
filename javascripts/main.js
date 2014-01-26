jQuery(document).ready(function(){
	jQuery('#main_content').find('div:not(.active)').hide();
	jQuery('#content_triggers').find('span').click(function(){
		jQuery('.active')
			.hide()
			.removeClass('active');
		jQuery('#main_content')
			.find('div.' + jQuery(this).attr('id'))
			.addClass('active')
			.show();
	});
});