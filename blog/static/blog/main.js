 function initMap() {
     const map = new google.maps.Map(document.getElementById("map"), {
         zoom: 5,
         center: {
             lat: 53.350140,
             lng: -6.266155
         }
     });

     const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

     const locations = [
         {lat: 53.360799, lng: -6.251241}
     ];

     const markers = locations.map(function (location, i) {
         return new google.maps.Marker({
             position: location,
             label: labels[i % labels.length]
         });
     });
     const markerCluster = new MarkerClusterer(map, markers, {
         imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
     });
 }

 $(function() {
    $("#payment-form").submit(function() {
        const form = this;
        const card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

        Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        } else {
            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
    });
});


