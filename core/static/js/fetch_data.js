function fetchData(input, urls) {
    const value = $.trim($(input).val());

    $.ajax({
        url: urls,
        type: 'GET',
        data: {'value': value},
        dataType: 'json',
        success: function (data) {
            console.log(data);
            document.getElementById('product-name').value = data.name;
        }
    });
}