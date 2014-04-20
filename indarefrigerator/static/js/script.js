$(function(){
    var BASE_URL = '/api/products';
    $('.datepicker').datepicker({
        changeMonth: true,
        changeYear: true,
        dateFormat: "yy-mm-dd"
    });
    $('#product-create').submit(function(e) {
        var data = $(this).serializeArray(), product = {};
        $.each(data, function(_, kv) {
            product[kv.name] = kv.value;
        });

        $.post(BASE_URL, product, function(receivedProduct) {
            console.log(receivedProduct);
        }, 'json');
        e.preventDefault();
    });
    $('.product-delete').click(function(e) {
        if (!confirm('Точно?'))
            return;
        var that = this, productId = $(this).data('product-id');
        $.ajax({
            type: 'DELETE',
            url: BASE_URL + '/' + productId,
            success: function() {
                $(that).closest('tr').remove();
            }
        });
        e.preventDefault();
    });
});
