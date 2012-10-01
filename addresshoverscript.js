$(document).ready(function() {
	$("tr").not(":first").hover(
		function () {
			$(this).css("background-color", "#ccc");
		},
		function () {
			$(this).css("background-color", "#fff");
		}
	);
});

