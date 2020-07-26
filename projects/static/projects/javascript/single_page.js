let title = document.getElementById("titleChange");
let titleForm = title.children[1];
let titleH1 = title.children[0];

let description = document.getElementById("descChange");
let descForm = description.children[1];
let descH3 = description.children[0];

function titleChanger(){
    if(titleH1.style.display === "none"){
        titleH1.style.display = "block";
        titleForm.style.display = "none";
    } else {
        titleH1.style.display = "none";
        titleForm.style.display = "block";
    }
}

function descriptionChanger(){
    if(descH3.style.display === "none"){
        descH3.style.display = "block";
        descForm.style.display = "none";
    }else{
        descH3.style.display = "none";
        descForm.style.display = "block";
    }
}