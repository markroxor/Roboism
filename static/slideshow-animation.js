
var index = 1;
slideshow();

function currentImage(x){
  var i;
  index = x;
  $("#slideshow").backstretch("/static/img_"+ index + ".jpg");
  var rounds = document.getElementsByClassName("rounds");
  for(i = 0; i < 5; i++)
    rounds[i].className = rounds[i].className.replace(" w3-white", "");

  rounds[index - 1].className += " w3-white";
}

function Image(n){
  var rounds = document.getElementsByClassName("rounds");
  rounds[index - 1].className = rounds[index - 1].className.replace(" w3-white", "");
  index += n;
  if(index <= 0)
    index = 5;
  else if(index >= 6)
    index = 1;
  $("#slideshow").backstretch("/static/img_"+ index + ".jpg");
  rounds[index - 1].className += " w3-white";
}

function slideshow(){
  Image(1);
  setTimeout(slideshow, 3000);  
}