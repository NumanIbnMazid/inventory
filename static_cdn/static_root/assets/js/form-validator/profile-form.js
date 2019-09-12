// ===================== Profile Form JS ======================

var form = $("#profile_form");
var first_name = $("#profile_first_name");
var last_name = $("#profile_last_name");
var dob = $("#profile_dob");
var contact = $("#profile_contact");
var address = $("#profile_address");
var input_msg = $(".input-message");


function resetMessage() {
  input_msg.html("");
}


// force to enter only number 0-9
(function($) {
  $.fn.inputFilter = function(inputFilter) {
    return this.on(
      "input keydown keyup mousedown mouseup select contextmenu drop",
      function() {
        if (inputFilter(this.value)) {
          this.oldValue = this.value;
          this.oldSelectionStart = this.selectionStart;
          this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
          this.value = this.oldValue;
          this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        }
      }
    );
  };
})(jQuery);

// contact.inputFilter(function(value) {
//   return /^\d*$/.test(value);
// });

// Contact Input
var contactPattern = new RegExp("^(\\+)?(\\d+)$");

function chkInput() {
  var v = $("#profile_contact").val().charAt($("#profile_contact").val().length - 1);
  return contactPattern.test(v);
}
$("#profile_contact").on('keyup keypress blur change input keydown mousedown mouseup select contextmenu drop', function () {
  if ($(this).val().length == 1 || ($(this).val().length == 2 && $("#profile_contact").val().charAt($("#profile_contact").val().length - 1) == "0")) $(this).val('+');
  else {
    var res = chkInput();
    if (!res) $(this).val($(this).val().slice(0, -1));
  }
});

// date-time picker
$(document).ready(function() {
  function now() {
    var d = new Date();
    var month = d.getMonth() + 1;
    var day = d.getDate();
    var output =
      d.getFullYear() +
      "/" +
      (month < 10 ? "0" : "") +
      month +
      "/" +
      (day < 10 ? "0" : "") +
      day;
    return output;
  }

  $("#profile_dob").datetimepicker({
    timepicker: false,
    format: "Y-m-d",
    maxDate: now(),
    validateOnBlur: true
  });
});


// preventing form from autocomplete
$(document).ready(function() {
  $(document).on("focus", ":input", function() {
    $(this).attr("autocomplete", "off");
  });
});
