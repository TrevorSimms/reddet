// any scripts to be run after <body>
let myDate = new Date();
let footerDate = document.getElementById('footerDate');

if(footerDate != null) {
    footerDate.innerHTML = myDate.toTimeString();
}