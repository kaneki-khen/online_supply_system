
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	var actions = $("table td:last-child").html();
	// Append table with add row form on add new button click
    $(".add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" class="form-control" name="Item No." id="Item No."></td>' +
            '<td><input type="text" class="form-control" name="Item Name" id="Item Name"></td>' +
            '<td><input type="text" class="form-control" name="Item Brand/Description" id="Item Brand/Description"></td>' +
			'<td><input type="text" class="form-control" name="Unit" id="Unit"></td>' +
			'<td><input type="text" class="form-control" name="Quantity" id="Quantity"></td>' +
            '<td><input type="text" class="form-control" name="Price" id="Price"></td>' +
        '</tr>';
    	$("table").append(row);		
		$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
	// Add row on add button click
	$(document).on("click", ".add", function(){
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){
			input.each(function(){
				$(this).parent("td").html($(this).val());
			});			
			$(this).parents("tr").find(".add, .edit").toggle();
			$(".add-new").removeAttr("disabled");
		}		
    });
});


// Add an event listener to the form's submit button to call the validatePasswords() function
document.getElementById('register-form').addEventListener('submit', validatePasswords);

function validatePasswords() {
  // Get the values of the password and confirm password fields
  var pass1 = document.getElementById('pass1').value;
  var pass2 = document.getElementById('pass2').value;

  // Check if the passwords match
  if (pass1 != pass2) {
	// If the passwords do not match, display an error message
	alert('Passwords do not match!');

	// Prevent the form from submitting
	return false;
  }

  // If the passwords match, allow the form to submit
  return true;
}

