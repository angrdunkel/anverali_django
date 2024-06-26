$(document).on('click', '.js-registration', function(event) {
    event.preventDefault();
    url = $(this).attr('href')
    $.ajax({
    type: "GET",
    url: url,
    })
        .done(function(data) {
            $('.js-modal-static-body').html(data); 
            $('#js-modal-static #js-modal-static-label').text("Test Label")
            $('#js-modal-static').modal('show');
           
        });  
    })

    $(document).on('click', '.js-create-account-btn', function(event) {
    event.preventDefault();
    form = $('.js-form-registration')
    url = form.attr('action')
    update_data = $('.js-moder-users-container')
   
    $.ajax({
    type: "POST",
    url: url,
    data: form.serialize()
    })
        .done(function(data) {
            $(".js-moder-users-container").load(location.href + " .js-moder-users-container");
            $('.js-modal-static-body').html(data); 
            $('#js-modal-static #js-modal-static-label').text("Registration complited")
            
        });  
    })
        
    $(document).on('click', '.js-open-modal', function(event) {
    event.preventDefault();
    url = $(this).attr('href')
    $.ajax({
    type: "GET",
    url: url,
    })
        .done(function(data) {
            $('#js-modal-lg-static').modal('hide');
            $('.js-modal-static-body').html(data.html); 
            $('#js-modal-static #js-modal-static-label').text(data.label)
            $('#js-modal-static').modal('show');
            
        });  
    })    

    $(document).on('click', '.js-update-account-btn', function(event) {
    event.preventDefault();
    form = $('.js-form-update-account')
    url = form.attr('action')
   
    $.ajax({
    type: "POST",
    url: url,
    data: form.serialize()
    })
        .done(function(data) {
            $('#js-modal-static').modal('hide');
            $(".js-moder-users-container").load(location.href + " .js-moder-users-container");
        });  
    })

    $(document).on('click', '.js-open-modal-lg', function(event) {
        event.preventDefault();
        url = $(this).attr('href')
        $.ajax({
        type: "GET",
        url: url,
        })
            .done(function(data) {
                $('.js-modal-lg-static-body').html(data.html); 
                $('#js-modal-lg-static #js-modal-lg-static-label').text(data.label)
                $('#js-modal-lg-static').modal('show');
                
            });  
        })

    $(document).on('click', '.js-create-task-performer-btn', function(event) {
        event.preventDefault();
        form = $('.js-create-task-performer-form')
            $.ajax({
                type: 'POST',
                url: form.attr('action'),
                data: form.serializeArray(),

                success: function(data) {                   
                    if (data.status == true) {
                        $('#js-modal-static').modal('hide');
                        $('.js-modal-sm-body').html(data.html);
                        $('#js-modal-sm').modal('show');
                    } else {
                        $('.js-modal-static-body').html(data.html);
                    }
                    
                },

            });
        
        })