// any scripts to be run after <body>
var myDate = new Date();
var footerDate = document.getElementById('footerDate');
if (footerDate != null) {
    footerDate.innerHTML = myDate.toTimeString();
}
