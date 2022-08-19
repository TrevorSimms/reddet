/**
 *  Author: Trevor Simms 
 *  Email: trevor-simms@outlook.com
 * 
 *  Description:
 *      Main JavaScript file for Reddet.
 */
// script variables
let myDate = new Date();
let footerDate = document.getElementById('footerDate');

// simple date string
if(footerDate != null) {
    footerDate.innerHTML = myDate.toTimeString();
}
