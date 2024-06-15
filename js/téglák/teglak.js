/*
1. doboz:
Kattintásra adjunk hozzá egy "blur" nevű class attribútumot, majd újabb kattintásra vegyük
le róla azt.
*/

var isBlurred = false;

document.getElementById("element-one").onclick = function(){
   if(!isBlurred){
    document.getElementById("element-one").classList.add("blur")
   }else{
    document.getElementById("element-one").classList.remove("blur")
   }
   isBlurred = !isBlurred
}


/*
2. doboz:
Ha az egérrel fölé megyünk változzon meg a háttérszíne pirosra, ha levesszük róla az egeret
változzon vissza az eredeti színére.
*/

var isBlurred = false;

document.getElementById("element-two").onmouseover = function(){
    document.getElementById("element-two").style.color = "red"
}
document.getElementById("element-two").onmouseleave = function(){
    document.getElementById("element-two").style.color = ""
}

/*
3. doboz:
Dupla kattintással sorsoljon egy számot 1 és 20 között és módosítsa a kapott számmal a doboz tartalmát. 
*/

document.getElementById("element-three").ondblclick = function(){
    document.getElementById("element-three").firstElementChild.innerHTML = Math.floor(Math.random() * 20) + 1
}

/*
4. doboz:
Kattintásra tűnjön el, majd egy 1 másodperces várakozás után ismét jelenjen meg.
*/


document.getElementById("element-four").onclick = function(){
  document.getElementById("element-four").classList.add("hidden") 
  setTimeout(function(){
    document.getElementById("element-four").classList.remove("hidden") 
  }, 1000)
  
}

/*
5. doboz:
Kattintásra alakítsa kör alakúra az összes dobozt.
*/

document.getElementById("element-five").onclick = function(){
  document.querySelectorAll('.shape').forEach((x) => (x.style.borderRadius = "50%"));
}

/*
6. doboz:
Onchange eseményre módosítsuk a doboz tartalmát az input mezőbe írt értékkel
*/

document.getElementById("box-6").onchange = function(e){
  e.preventDefault()
  document.getElementById("element-six").firstElementChild.innerHTML = e.target.value
}

/*
7. doboz:
Keypress eseményre írjuk be a dobozba az adott karaktert, amit leütöttek
*/


document.getElementById("box7-input").onkeydown = function(e){
  document.getElementById("element-seven").firstElementChild.innerHTML = e.target.value
}

/*
8. doboz:
Egérmozdítás eseményre írjuk be az egér pozíciójának x és y koordinátáját, 
a következő séma szerint: "X: {x-koordináta}, Y: {y-koordináta}"
*/

document.getElementById("element-eight").onmousemove = function(e){
  document.getElementById("element-eight").firstElementChild.innerHTML = "X: " + e.clientX + ", Y: " + e.clientY
}

/*
9. doboz:
Submit eseményre módosítsuk a doboz tartalmát azzal az értékkel ami úgy áll elő, 
hogy végrehajtjuk a select inputban kiválasztott operációt,
a state-en és number inputba beírt értéken.

Az előállt végeredményt tároljuk el új state-ként!

Pl:
  Number input mezőbe írt érték: 5
  Select inputban kiválasztott érték: "mult"
  Aktuális state: 9

  Operáció: 9 * 5
  
  Dobozba és state-be beírandó érték: 45
*/

document.getElementById("box-9").onsubmit = function(e){
  e.preventDefault()
  var muvelet = e.target[0].value
  switch(muvelet){
    case "add":
      document.getElementById("element-nine").firstElementChild.innerHTML = parseInt(e.target[1].value) + parseInt(e.target[2].value)
      break;
    case "sub":
      document.getElementById("element-nine").firstElementChild.innerHTML = e.target[1].value - e.target[2].value
      break;
    case "mult":
      document.getElementById("element-nine").firstElementChild.innerHTML = e.target[1].value * e.target[2].value
      break;
    case "div":
      document.getElementById("element-nine").firstElementChild.innerHTML = e.target[1].value / e.target[2].value
      break;
  }
  
}