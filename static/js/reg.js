$(function () {
    $('#btnReg').click(function () {
        console.log('click');
        let result = $('.result')
        $.ajaxs({
            url: '/signUp',
            data: $('#regForm').serialize(),
            type: 'POST',
            success: function (response){
                $(result).html(JSON.parse(response)['html'])
            },
            error: function(error){
                $(result).html(JSON.parse(error)['html'])
            },
        })
    })
});