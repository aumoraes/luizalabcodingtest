$( document ).ready(function(){

  $("#myModalHorizontal #submit_form").on("click", function(){
    if( $("#myModalHorizontal #update_employee").valid()){
      employee_json =  serializeFormData( $('form') );
      var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
      url = '/employee/' + employee_json["id"];
      manageEmployeeRequest(url, "PUT", employee_json["id"], employee_json, csrftoken);
      $('#myModalHorizontal').modal('hide');

      $("#employee_" + employee_json["id"]).find(".name").text( employee_json["name"] );
      $("#employee_" + employee_json["id"]).find(".email").text( employee_json["email"] );
      $("#employee_" + employee_json["id"]).find(".department").text( employee_json["department"] );
    }
  });
  $(".update_employee").on("click", function(){
    employee_data = populateEmployeeData($(this));
    $("#myModalHorizontal .modal-header .modal-username").html( employee_data["name"] );
    $("#myModalHorizontal .modal-body #id").val( employee_data["id"] );
    $("#myModalHorizontal .modal-body #id_name").val( employee_data["name"] );
    $("#myModalHorizontal .modal-body  #id_email").val( employee_data["email"] );
    $("#myModalHorizontal .modal-body  #id_department").val( employee_data["department"] );
    $('#myModalHorizontal').modal('show');
  });
  $(".delete_employee").on("click", function(){
    delete_item = $(this);
    delete_item_json = populateEmployeeData(delete_item);
    $("#username").html( delete_item_json["name"] );
    $('#mi-modal').modal({
      backdrop: 'static',
      keyboard: false
    })
    .one('click', '#modal-btn-yes', function(e) {
      $("#mi-modal").modal('hide');
      delete_item.parents("tr").fadeOut();
      var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
      url = '/employee/' + delete_item_json["id"];
      manageEmployeeRequest(url, "DELETE", delete_item_json["id"], null, csrftoken);
    })
    .one('click', '#modal-btn-no', function(e) {
      $("#mi-modal").modal('hide');
    })
  });
});

function serializeFormData(form){
    return  form.serializeArray().reduce(function(obj, item) {
          obj[item.name] = item.value;
          return obj;
        },
      {});

}
function populateEmployeeData(employee_data){
  return {
    id: employee_data.parents("tr").find(".id").text().trim(),
    name: employee_data.parents("tr").find(".name").text().trim(),
    email: employee_data.parents("tr").find(".email").text().trim(),
    department: employee_data.parents("tr").find(".department").text().trim()
  }
}

function manageEmployeeRequest(serverUrl, method, id, new_employee, csrftoken){
  $.ajax({
    url: serverUrl,
    type: method,
    headers: {
      'X-CSRFToken': csrftoken,
      'Content-Type': 'application/json'
    },
    data: JSON.stringify(new_employee),
    success: function(data, status, response) {
      console.log(status)
    },
    error: function(data, status, response){
      console.log("Error method [" + method +"]", data)
    }
  });
}

var getUrlParameter = function getUrlParameter(sParam) {

    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

function paginationController(page){
  page_url = "/employee/?page=" + page;
  window.history.pushState("", "", page_url);

  $.ajax({
    url: '/api/v1/employee/?page=' + page,
    type: "GET",
    headers: {
      'Content-Type': 'application/json'
    },
    success: function(data, status, response) {

      var server_data_length =  data.results.length;
      var table_row_length =  $('.table > tbody  > tr').length;

      missing_table_rows = server_data_length - table_row_length;

      while( missing_table_rows <  server_data_length ){
        $('.table > tbody ').append("<tr id=''>"+
        "<td><p class='id'></p></td>"+
        "<td><p class='name'></p></td>"+
        "<td><p class='email'></p></td>"+
        "<td><p class='department'></p></td>"+
        "</td>"+
        "<td><a href='#' class='update_employee btn btn-warning btn-sm pull-right' role='button'>update</a></td>"+
        "<td><a href='#'  class=' delete_employee btn btn-danger btn-sm pull-right' role='button'>delete</a></td>");

        missing_table_rows++;
      }

      $('.table > tbody  > tr').each(function( table_row_number, table_row ) {
        try {
          $(this).attr("id","employee_"+data.results[table_row_number]["id"]);
          $(table_row).find(".id").text( data.results[table_row_number]["id"] );
          $(table_row).find(".name").text( data.results[table_row_number]["name"] );
          $(table_row).find(".email").text( data.results[table_row_number]["email"] );
          $(table_row).find(".department").text( data.results[table_row_number]["department"] );
          $(table_row).show();
        }catch(err) {
          $(table_row).hide();
        }
      });
    },
    error: function(data, status, response){
      console.log("Error ", data)
    }
  });
}
