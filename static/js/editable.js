$(document).ready(function() {
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    var csrfSafeMethod = function(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    //toggle `popup` / `inline` mode
    $.fn.editable.defaults.mode = 'inline';     
    
        //make titles editable
        $('.title').editable({
            type: 'text',
            title: 'Enter title',
            name: 'title'
        });
        
        //make description editable
        $('.description').editable({
            type: 'text',
            title: 'Enter description',
            name: 'description'
        });

        $('.due_date').editable({
            type: 'text',
            title: 'Enter due date',
            name: 'due_date'
            /*
            //uncomment these lines to send data on server
            ,pk: 1
            ,url: '/post'
            */
        });
});