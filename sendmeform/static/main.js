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