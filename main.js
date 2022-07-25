
/* removing this enclosure will allow Dev console invoke and test everything here */
    (function (window) {
    'use strict';

    var FORM_SELECTOR = '[data-coffee-order="form"]';
    var CHECKLIST_SELECTOR = '[data-coffee-order="checklist"]';
    var App = window.App;


  $('#id-select').change(function() {

    console.log("id-select Changed. Value: ", $(this).val(), $('#id-select option:selected').text());

    // clear out the previous text area below
    $('#textInputBox').val("");
    
   })


   $('#textSubmit').click(function() {

    console.log("textSubmit clicked. Input value: ", $('#textInputBox').val());

    sock.onmessage = function(e) {
        
        console.log("Server responded with: " + e.data);

        // parse the server response
        var response = JSON.parse(e.data);
        console.log("Speed: ", response.Speed);
        console.log("Error: ", response.Error);

        // get the current time for result row
        var today= new Date().toLocaleString('en-US', { timeZone: 'UTC' });

        // Results page update - append a new row to the table

        $('#results > tbody:last-child').append('<tr>')
            .append($('<td>').append($('#id-select option:selected').text()))
            .append($('<td>').append(response.Speed))
            .append($('<td>').append(response.Error))
            .append($('<td>').append(today))
            .append('</tr>');

    }
    

    // create a JSON object with info and send to server

    var obj = new Object();
    obj.type = $('#id-select option:selected').text();
    obj.input = $('#textInputBox').val();

    sock.send(JSON.stringify(obj));
    

   })

   var sock = null;
   var wsuri = "ws://127.0.0.1:8081/ws";

   sock = new WebSocket(wsuri);


   window.onload = function() {
    sock = new WebSocket(wsuri);
    console.log("websocket connection with server created");
   }

   sock.onopen = function() {
    console.log("connected to " + wsuri);
    }

    sock.onclose = function(e) {
        console.log("connection closed (" + e.code + ")");
    }


})(window);

