$(function(){
    $('#btnSignUp').click(function(){
        $.ajax({
            url:'/signup',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                console.log(response); 
                alert(response)
                $('#message').html(reponse);
                if (response == 'OK'){
                    window.location.href = '/login';
                }
            },
            error: function(error){
                console.log(error);
                $('#message').html(error);
            }
        });
    });
});