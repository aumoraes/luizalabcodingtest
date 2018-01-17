$( document ).ready(function(){
  $("#myModalHorizontal #update_employee").validate({  // initialize plugin on the form
    rules: {
      id:{
        required: true,
      },
      // name: {
      //   required: true,
      //   minlength: 3
      // },
      email: {
        required: true,
        email: true
      },
      department: {
        required: true,
        minlength: 2
      },
    },
    messages: {
      id:{
        required: "<li> ID can't be empty</li>"
      },
      // name: {
      //   required: "<li> Name can't be empty</li>",
      //   minlength: "<li>Your name is not long enough, at least 3 character are required.</li>"
      // },
      email: {
        required: "<li> Email can't be empty</li>"
      },
      department: {
        required: "<li> Department can't be empty</li>",
        minlength: "<li>Department is not long enough, at least 2 character are required.</li>"
      }
    }
  });
});
