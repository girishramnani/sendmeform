/**
 * Created by girish on 1/29/16.
 */
console.log("hello world");

var myMessages = ['info','warning','error','success'];
function hideAllMessages(){
         var messagesHeights = new Array(); // this array will store height for each
         for (i=0; i<myMessages.length; i++){
                   messagesHeights[i] = $('.' + myMessages[i]).outerHeight(); // fill array
                   $('.' + myMessages[i]).css('top', -messagesHeights[i]); //move element outside viewport
         }
}

$(".message").click(hideAllMessages);

function showModal(){
    // initialize modal element
    var modalEl = document.createElement('div');
    modalEl.style.width = '400px';
    modalEl.style.height = '300px';
    modalEl.style.margin = '100px auto';
    modalEl.style.backgroundColor = '#fff';

    // show modal
    mui.overlay('on', modalEl);


  }
