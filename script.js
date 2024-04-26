function showPopup() {
    alert("Thank you for contacting us! We will respond soon.");
    return true; // Submit the form after showing the popup
}

var clevertap = {event:[], profile:[], account:[], onUserLogin:[],region:'in1', notifications:[], privacy:[]};
// replace with the CLEVERTAP_ACCOUNT_ID with the actual ACCOUNT ID value from your Dashboard -> Settings page
clevertap.account.push({"id": "Z44-Z4K-K65Z"});
clevertap.privacy.push({optOut: false}); //set the flag to true, if the user of the device opts out of sharing their data
clevertap.privacy.push({useIP: false}); //set the flag to true, if the user agrees to share their IP data
(function () {
    var wzrk = document.createElement('script');
    wzrk.type = 'text/javascript';
    wzrk.async = true;
    wzrk.src = ('https:' == document.location.protocol ? 'https://d2r1yp2w7bby2u.cloudfront.net' : 'http://static.clevertap.com') + '/js/clevertap.min.js';        
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(wzrk, s);
})();

clevertap.onUserLogin.push({
    "Site": {
      "Name": "Jack Montana",            // String
      "Identity": 61026032,              // String or number
      "Email": "jack@gmail.com",         // Email address of the user
      "Phone": "+14155551234",           // Phone (with the country code)
      "Gender": "M",                     // Can be either M or F
      "DOB": new Date(),                 // Date of Birth. Date object
   // optional fields. controls whether the user will be sent email, push etc.
      "MSG-email": false,                // Disable email notifications
      "MSG-push": true,                  // Enable push notifications
      "MSG-sms": true,                   // Enable sms notifications
      "MSG-whatsapp": true,              // Enable WhatsApp notifications
    }
   })

   clevertap.event.push("Product Viewed");

   clevertap.event.push("Product Viewed", {
    "Product name":"Casio Chronograph Watch",
    "Category":"Mens Accessories",
    "Price":59.99,
    "Date": new Date()
  });

  clevertap.init('Z44-Z4K-K65Z', 'in1', 'TARGET_DOMAIN') // Replace with values applicable to you
clevertap.setLogLevel(LOG_LEVEL)

clevertap.setOffline(true) // sets the sdk in offline mode.Events will be queued locally and             will be fired only when offline mode is set to false
clevertap.setOffline(false) // disables the offline mode. Events will now get fired immediately