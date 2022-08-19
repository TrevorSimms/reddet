/**
 *  Author: Trevor Simms
 *  Email: trevor-simms@outlook.com
 *
 *  Description:
 *      Main JavaScript file for Reddet.
 */
// script variables
var myDate = new Date();
var footerDate = document.getElementById('footerDate');
// simple date string
if (footerDate != null) {
    footerDate.innerHTML = myDate.toTimeString();
}
